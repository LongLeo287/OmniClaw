---
id: github.com-nalexn-clean-architecture-swiftui-d8076
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:01.757564
---

# KNOWLEDGE EXTRACT: github.com_nalexn_clean-architecture-swiftui_d807655d
> **Extracted on:** 2026-04-01 10:55:18
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521099/github.com_nalexn_clean-architecture-swiftui_d807655d

---

## File: `.gitignore`
```
## Mac OS
.DS_Store

## Xcode workspace
*.xcworkspace

## Build generated
build/
DerivedData/

## Various settings
*.pbxuser
!default.pbxuser
*.mode1v3
!default.mode1v3
*.mode2v3
!default.mode2v3
!default.perspectivev3
*.perspectivev3
xcuserdata/

## Other
*.moved-aside
*.xcuserstate

## Obj-C/Swift specific
*.hmap
*.ipa
*.dSYM.zip
*.dSYM

## Playgrounds
timeline.xctimeline
playground.xcworkspace

## Tools artifacts
cpd-output.xml

## SwiftyBeaver
Hamew.beaver

## Swift Package Manager
# Packages/
.build/

## CocoaPods
# Pods/

## Carthage
Carthage/Checkouts
Carthage/Build

## fastlane
fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots
fastlane/test_output
fastlane/app_archive
```

## File: `.swiftlint.yml`
```yaml
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

## File: `.travis.yml`
```yaml
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

## File: `LICENSE`
```
MIT License

Copyright (c) 2019 Alexey

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

## File: `Package.swift`
```
// swift-tools-version: 6.1
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "CountriesSwiftUI",
    platforms: [
        .iOS(.v18),
        .macOS(.v12)
    ],
    products: [
        .library(name: "CountriesSwiftUI", targets: ["CountriesSwiftUI"])
    ],
    dependencies: [
        .package(url: "https://github.com/nalexn/EnvironmentOverrides", from: "0.0.4"),
        .package(url: "https://github.com/nalexn/ViewInspector", from: "0.10.0")
    ],
    targets: [
        .target(
            name: "CountriesSwiftUI",
            dependencies: [
                .product(name: "EnvironmentOverrides", package: "EnvironmentOverrides")
            ],
            path: "CountriesSwiftUI",
            exclude: [
                "Resources/Preview Assets.xcassets",
            ],
            resources: [
                .process("Resources/Assets.xcassets"),
                .process("Resources/Localizable.xcstrings"),
            ],
            swiftSettings: [
                .swiftLanguageMode(.v5)
            ],
            linkerSettings: [
                .linkedFramework("UIKit")
            ]
        ),
        .testTarget(
            name: "UnitTests",
            dependencies: [
                "CountriesSwiftUI",
                .product(name: "ViewInspector", package: "ViewInspector")
            ],
            path: "UnitTests",
            swiftSettings: [
                .swiftLanguageMode(.v5)
            ],
        )
    ]
)
```

## File: `README.md`
```markdown
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

## File: `CountriesSwiftUI/Core/App.swift`
```
//
//  CountriesApp.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI
import EnvironmentOverrides

@main
struct MainApp: App {
    
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    var body: some Scene {
        WindowGroup {
            appDelegate.rootView
        }
    }
}

extension AppEnvironment {
    var rootView: some View {
        VStack {
            if isRunningTests {
                Text("Running unit tests")
            } else {
                CountriesList()
                    .modifier(RootViewAppearance())
                    .modelContainer(modelContainer)
                    .attachEnvironmentOverrides(onChange: onChangeHandler)
                    .inject(diContainer)
                if modelContainer.isStub {
                    Text("⚠️ There is an issue with local database")
                        .font(.caption2)
                }
            }
        }
    }

    private var onChangeHandler: (EnvironmentValues.Diff) -> Void {
        return { diff in
            if !diff.isDisjoint(with: [.locale, .sizeCategory]) {
                self.diContainer.appState[\.routing] = AppState.ViewRouting()
            }
        }
    }
}
```

## File: `CountriesSwiftUI/Core/AppDelegate.swift`
```
//
//  AppDelegate.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 23.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import UIKit
import SwiftUI
import Combine
import Foundation

@MainActor
final class AppDelegate: UIResponder, UIApplicationDelegate {

    private lazy var environment = AppEnvironment.bootstrap()
    private var systemEventsHandler: SystemEventsHandler { environment.systemEventsHandler }

    var rootView: some View {
        environment.rootView
    }

    func application(_ application: UIApplication, didFinishLaunchingWithOptions
        launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        return true
    }

    func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        let config: UISceneConfiguration = UISceneConfiguration(name: nil, sessionRole: connectingSceneSession.role)
        config.delegateClass = SceneDelegate.self
        SceneDelegate.register(systemEventsHandler)
        return config
    }

    func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        systemEventsHandler.handlePushRegistration(result: .success(deviceToken))
    }

    func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {
        systemEventsHandler.handlePushRegistration(result: .failure(error))
    }

    func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable: Any]) async -> UIBackgroundFetchResult {
        return await systemEventsHandler
            .appDidReceiveRemoteNotification(payload: userInfo)
    }
}

// MARK: - SceneDelegate

@MainActor
final class SceneDelegate: UIResponder, UIWindowSceneDelegate, ObservableObject {

    private static var systemEventsHandler: SystemEventsHandler?
    private var systemEventsHandler: SystemEventsHandler? { Self.systemEventsHandler }

    static func register(_ systemEventsHandler: SystemEventsHandler?) {
        Self.systemEventsHandler = systemEventsHandler
    }

    func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
        systemEventsHandler?.sceneOpenURLContexts(URLContexts)
    }

    func sceneDidBecomeActive(_ scene: UIScene) {
        systemEventsHandler?.sceneDidBecomeActive()
    }

    func sceneWillResignActive(_ scene: UIScene) {
        systemEventsHandler?.sceneWillResignActive()
    }
}
```

## File: `CountriesSwiftUI/Core/AppState.swift`
```
//
//  AppState.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 23.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI
import Combine

struct AppState: Equatable {
    var routing = ViewRouting()
    var system = System()
    var permissions = Permissions()
}

extension AppState {
    struct ViewRouting: Equatable {
        var countriesList = CountriesList.Routing()
        var countryDetails = CountryDetails.Routing()
    }
}

extension AppState {
    struct System: Equatable {
        var isActive: Bool = false
        var keyboardHeight: CGFloat = 0
    }
}

extension AppState {
    struct Permissions: Equatable {
        var push: Permission.Status = .unknown
    }

    static func permissionKeyPath(for permission: Permission) -> WritableKeyPath<AppState, Permission.Status> {
        let pathToPermissions = \AppState.permissions
        switch permission {
        case .pushNotifications:
            return pathToPermissions.appending(path: \.push)
        }
    }
}

func == (lhs: AppState, rhs: AppState) -> Bool {
    return lhs.routing == rhs.routing
        && lhs.system == rhs.system
        && lhs.permissions == rhs.permissions
}
```

## File: `CountriesSwiftUI/Core/DeepLinksHandler.swift`
```
//
//  DeepLinksHandler.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Foundation

enum DeepLink: Equatable {
    
    case showCountryFlag(alpha3Code: String)

    init?(url: URL) {
        guard
            let components = URLComponents(url: url, resolvingAgainstBaseURL: true),
            components.host == "www.example.com",
            let query = components.queryItems
            else { return nil }
        if let item = query.first(where: { $0.name == "alpha3code" }),
            let alpha3Code = item.value {
            self = .showCountryFlag(alpha3Code: alpha3Code)
            return
        }
        return nil
    }
}

// MARK: - DeepLinksHandler

@MainActor
protocol DeepLinksHandler {
    func open(deepLink: DeepLink)
}

struct RealDeepLinksHandler: DeepLinksHandler {
    
    private let container: DIContainer
    
    init(container: DIContainer) {
        self.container = container
    }
    
    func open(deepLink: DeepLink) {
        switch deepLink {
        case let .showCountryFlag(alpha3Code):
            let routeToDestination = {
                self.container.appState.bulkUpdate {
                    $0.routing.countriesList.countryCode = alpha3Code
                    $0.routing.countryDetails.detailsSheet = true
                }
            }
            /*
             SwiftUI is unable to perform complex navigation involving
             simultaneous dismissal or older screens and presenting new ones.
             A work around is to perform the navigation in two steps:
             */
            let defaultRouting = AppState.ViewRouting()
            if container.appState.value.routing != defaultRouting {
                self.container.appState[\.routing] = defaultRouting
                let delay: DispatchTime = .now() + (ProcessInfo.processInfo.isRunningTests ? 0 : 1.5)
                DispatchQueue.main.asyncAfter(deadline: delay, execute: routeToDestination)
            } else {
                routeToDestination()
            }
        }
    }
}
```

## File: `CountriesSwiftUI/Core/PushNotificationsHandler.swift`
```
//
//  PushNotificationsHandler.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import UserNotifications

protocol PushNotificationsHandler { }

final class RealPushNotificationsHandler: NSObject, PushNotificationsHandler {
    
    private let deepLinksHandler: DeepLinksHandler
    
    init(deepLinksHandler: DeepLinksHandler) {
        self.deepLinksHandler = deepLinksHandler
        super.init()
        UNUserNotificationCenter.current().delegate = self
    }
}

// MARK: - UNUserNotificationCenterDelegate

extension RealPushNotificationsHandler: UNUserNotificationCenterDelegate {
    
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
                                withCompletionHandler completionHandler:
        @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.list, .banner, .sound])
    }
    
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
        let userInfo = response.notification.request.content.userInfo
        handleNotification(userInfo: userInfo, completionHandler: completionHandler)
    }
    
    func handleNotification(userInfo: [AnyHashable: Any], completionHandler: @escaping () -> Void) {
        guard let payload = userInfo["aps"] as? [AnyHashable: Any],
            let countryCode = payload["country"] as? String else {
            completionHandler()
            return
        }
        Task { @MainActor in
            deepLinksHandler.open(deepLink: .showCountryFlag(alpha3Code: countryCode))
            completionHandler()
        }
    }
}
```

## File: `CountriesSwiftUI/Core/SystemEventsHandler.swift`
```
//
//  SystemEventsHandler.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 27.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import UIKit
import Combine

@MainActor
protocol SystemEventsHandler {
    func sceneOpenURLContexts(_ urlContexts: Set<UIOpenURLContext>)
    func sceneDidBecomeActive()
    func sceneWillResignActive()
    func handlePushRegistration(result: Result<Data, Error>)
    @MainActor
    func appDidReceiveRemoteNotification(payload: [AnyHashable: Any]) async -> UIBackgroundFetchResult
}

struct RealSystemEventsHandler: SystemEventsHandler {

    let container: DIContainer
    let deepLinksHandler: DeepLinksHandler
    let pushNotificationsHandler: PushNotificationsHandler
    let pushTokenWebRepository: PushTokenWebRepository
    private let cancelBag = CancelBag()

    init(container: DIContainer,
         deepLinksHandler: DeepLinksHandler,
         pushNotificationsHandler: PushNotificationsHandler,
         pushTokenWebRepository: PushTokenWebRepository) {

        self.container = container
        self.deepLinksHandler = deepLinksHandler
        self.pushNotificationsHandler = pushNotificationsHandler
        self.pushTokenWebRepository = pushTokenWebRepository

        installKeyboardHeightObserver()
        installPushNotificationsSubscriberOnLaunch()
    }

    private func installKeyboardHeightObserver() {
        let appState = container.appState
        NotificationCenter.default.keyboardHeightPublisher
            .sink { [appState] height in
                appState[\.system.keyboardHeight] = height
            }
            .store(in: cancelBag)
    }

    private func installPushNotificationsSubscriberOnLaunch() {
        weak var permissions = container.interactors.userPermissions
        container.appState
            .updates(for: AppState.permissionKeyPath(for: .pushNotifications))
            .first(where: { $0 != .unknown })
            .sink { status in
                if status == .granted {
                    // If the permission was granted on previous launch
                    // requesting the push token again:
                    permissions?.request(permission: .pushNotifications)
                }
            }
            .store(in: cancelBag)
    }

    func sceneOpenURLContexts(_ urlContexts: Set<UIOpenURLContext>) {
        guard let url = urlContexts.first?.url else { return }
        handle(url: url)
    }

    private func handle(url: URL) {
        guard let deepLink = DeepLink(url: url) else { return }
        deepLinksHandler.open(deepLink: deepLink)
    }

    func sceneDidBecomeActive() {
        container.appState[\.system.isActive] = true
        container.interactors.userPermissions.resolveStatus(for: .pushNotifications)
    }

    func sceneWillResignActive() {
        container.appState[\.system.isActive] = false
    }

    func handlePushRegistration(result: Result<Data, Error>) {

    }

    func appDidReceiveRemoteNotification(payload: [AnyHashable: Any]) async -> UIBackgroundFetchResult {
        return .noData
    }
}

// MARK: - Notifications

private extension NotificationCenter {
    var keyboardHeightPublisher: AnyPublisher<CGFloat, Never> {
        let willShow = publisher(for: UIApplication.keyboardWillShowNotification)
            .map { $0.keyboardHeight }
        let willHide = publisher(for: UIApplication.keyboardWillHideNotification)
            .map { _ in CGFloat(0) }
        return Publishers.Merge(willShow, willHide)
            .eraseToAnyPublisher()
    }
}

private extension Notification {
    var keyboardHeight: CGFloat {
        return (userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as? NSValue)?
            .cgRectValue.height ?? 0
    }
}
```

## File: `CountriesSwiftUI/DependencyInjection/AppEnvironment.swift`
```
//
//  AppEnvironment.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import UIKit
import SwiftData

@MainActor
struct AppEnvironment {
    let isRunningTests: Bool
    let diContainer: DIContainer
    let modelContainer: ModelContainer
    let systemEventsHandler: SystemEventsHandler
}

extension AppEnvironment {

    static func bootstrap() -> AppEnvironment {
        let appState = Store<AppState>(AppState())
        /*
         To see the deep linking in action:

         1. Launch the app in iOS 13.4 simulator (or newer)
         2. Subscribe on Push Notifications with "Allow Push" button
         3. Minimize the app
         4. Drag & drop "push_with_deeplink.apns" into the Simulator window
         5. Tap on the push notification

         Alternatively, just copy the code below before the "return" and launch:

            DispatchQueue.main.async {
                deepLinksHandler.open(deepLink: .showCountryFlag(alpha3Code: "AFG"))
            }
        */
        let session = configuredURLSession()
        let webRepositories = configuredWebRepositories(session: session)
        let modelContainer = configuredModelContainer()
        let dbRepositories = configuredDBRepositories(modelContainer: modelContainer)
        let interactors = configuredInteractors(appState: appState, webRepositories: webRepositories, dbRepositories: dbRepositories)
        let diContainer = DIContainer(appState: appState, interactors: interactors)
        let deepLinksHandler = RealDeepLinksHandler(container: diContainer)
        let pushNotificationsHandler = RealPushNotificationsHandler(deepLinksHandler: deepLinksHandler)
        let systemEventsHandler = RealSystemEventsHandler(
            container: diContainer,
            deepLinksHandler: deepLinksHandler,
            pushNotificationsHandler: pushNotificationsHandler,
            pushTokenWebRepository: webRepositories.pushToken)
        return AppEnvironment(
            isRunningTests: ProcessInfo.processInfo.isRunningTests,
            diContainer: diContainer,
            modelContainer: modelContainer,
            systemEventsHandler: systemEventsHandler)
    }

    private static func configuredURLSession() -> URLSession {
        let configuration = URLSessionConfiguration.default
        configuration.timeoutIntervalForRequest = 60
        configuration.timeoutIntervalForResource = 120
        configuration.waitsForConnectivity = true
        configuration.httpMaximumConnectionsPerHost = 5
        configuration.requestCachePolicy = .returnCacheDataElseLoad
        configuration.urlCache = .shared
        return URLSession(configuration: configuration)
    }

    private static func configuredWebRepositories(session: URLSession) -> DIContainer.WebRepositories {
        let images = RealImagesWebRepository(session: session)
        let countries = RealCountriesWebRepository(session: session)
        let pushToken = RealPushTokenWebRepository(session: session)
        return .init(images: images,
                     countries: countries,
                     pushToken: pushToken)
    }

    private static func configuredDBRepositories(modelContainer: ModelContainer) -> DIContainer.DBRepositories {
        let mainDBRepository = MainDBRepository(modelContainer: modelContainer)
        return .init(countries: mainDBRepository)
    }

    private static func configuredModelContainer() -> ModelContainer {
        do {
            return try ModelContainer.appModelContainer()
        } catch {
            // Log the error
            return ModelContainer.stub
        }
    }

    private static func configuredInteractors(
        appState: Store<AppState>,
        webRepositories: DIContainer.WebRepositories,
        dbRepositories: DIContainer.DBRepositories
    ) -> DIContainer.Interactors {
        let images = RealImagesInteractor(webRepository: webRepositories.images)
        let countries = RealCountriesInteractor(
            webRepository: webRepositories.countries,
            dbRepository: dbRepositories.countries)
        let userPermissions = RealUserPermissionsInteractor(
            appState: appState, openAppSettings: {
                URL(string: UIApplication.openSettingsURLString).flatMap {
                    UIApplication.shared.open($0, options: [:], completionHandler: nil)
                }
            })
        return .init(images: images,
                     countries: countries,
                     userPermissions: userPermissions)
    }
}
```

## File: `CountriesSwiftUI/DependencyInjection/DIContainer.swift`
```
//
//  DIContainer.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI
import SwiftData

struct DIContainer {

    let appState: Store<AppState>
    let interactors: Interactors

    init(appState: Store<AppState> = .init(AppState()), interactors: Interactors) {
        self.appState = appState
        self.interactors = interactors
    }

    init(appState: AppState, interactors: Interactors) {
        self.init(appState: Store<AppState>(appState), interactors: interactors)
    }
}

extension DIContainer {
    struct WebRepositories {
        let images: ImagesWebRepository
        let countries: CountriesWebRepository
        let pushToken: PushTokenWebRepository
    }
    struct DBRepositories {
        let countries: CountriesDBRepository
    }
    struct Interactors {
        let images: ImagesInteractor
        let countries: CountriesInteractor
        let userPermissions: UserPermissionsInteractor

        static var stub: Self {
            .init(images: StubImagesInteractor(),
                  countries: StubCountriesInteractor(),
                  userPermissions: StubUserPermissionsInteractor())
        }
    }
}

extension EnvironmentValues {
    @Entry var injected: DIContainer = DIContainer(appState: AppState(), interactors: .stub)
}

extension View {
    func inject(_ container: DIContainer) -> some View {
        return self
            .environment(\.injected, container)
    }
}
```

## File: `CountriesSwiftUI/Interactors/CountriesInteractor.swift`
```
//
//  CountriesInteractor.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

protocol CountriesInteractor {
    func refreshCountriesList() async throws
    func loadCountryDetails(country: DBModel.Country, forceReload: Bool) async throws -> DBModel.CountryDetails
}

struct RealCountriesInteractor: CountriesInteractor {

    let webRepository: CountriesWebRepository
    let dbRepository: CountriesDBRepository

    func refreshCountriesList() async throws {
        let apiCountries = try await webRepository.countries()
        try await dbRepository.store(countries: apiCountries)
    }

    func loadCountryDetails(
        country: DBModel.Country, forceReload: Bool
    ) async throws -> DBModel.CountryDetails {
        if !forceReload,
           let stored = try? await dbRepository.countryDetails(for: country) {
            return stored
        }
        let details = try await webRepository.details(country: country)
        try await dbRepository.store(countryDetails: details, for: country)
        guard let stored = try? await dbRepository.countryDetails(for: country) else {
            throw ValueIsMissingError()
        }
        return stored
    }
}

struct StubCountriesInteractor: CountriesInteractor {

    func refreshCountriesList() async throws {
    }

    func loadCountryDetails(country: DBModel.Country, forceReload: Bool) async throws -> DBModel.CountryDetails {
        throw ValueIsMissingError()
    }
}
```

## File: `CountriesSwiftUI/Interactors/ImagesInteractor.swift`
```
//
//  ImagesInteractor.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 09.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Combine
import Foundation
import SwiftUI

protocol ImagesInteractor {
    func load(image: LoadableSubject<UIImage>, url: URL?)
}

struct RealImagesInteractor: ImagesInteractor {
    
    let webRepository: ImagesWebRepository
    
    init(webRepository: ImagesWebRepository) {
        self.webRepository = webRepository
    }
    
    func load(image: LoadableSubject<UIImage>, url: URL?) {
        guard let url else {
            image.wrappedValue = .notRequested; return
        }
        image.load {
            try await webRepository.loadImage(url: url)
        }
    }
}

struct StubImagesInteractor: ImagesInteractor {
    func load(image: LoadableSubject<UIImage>, url: URL?) {
    }
}
```

## File: `CountriesSwiftUI/Interactors/UserPermissionsInteractor.swift`
```
//
//  UserPermissionsInteractor.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Foundation
import UserNotifications

enum Permission {
    case pushNotifications
}

extension Permission {
    enum Status: Equatable {
        case unknown
        case notRequested
        case granted
        case denied
    }
}

protocol UserPermissionsInteractor: AnyObject {
    func resolveStatus(for permission: Permission)
    func request(permission: Permission)
}

protocol SystemNotificationsSettings {
    var authorizationStatus: UNAuthorizationStatus { get }
}

protocol SystemNotificationsCenter {
    func currentSettings() async -> SystemNotificationsSettings
    func requestAuthorization(options: UNAuthorizationOptions) async throws -> Bool
}

extension UNNotificationSettings: SystemNotificationsSettings { }
extension UNUserNotificationCenter: SystemNotificationsCenter {
    func currentSettings() async -> any SystemNotificationsSettings {
        return await notificationSettings()
    }
}

// MARK: - RealUserPermissionsInteractor

final class RealUserPermissionsInteractor: UserPermissionsInteractor {

    private let appState: Store<AppState>
    private let openAppSettings: () -> Void
    private let notificationCenter: SystemNotificationsCenter

    init(appState: Store<AppState>,
         notificationCenter: SystemNotificationsCenter = UNUserNotificationCenter.current(),
         openAppSettings: @escaping () -> Void
    ) {
        self.appState = appState
        self.notificationCenter = notificationCenter
        self.openAppSettings = openAppSettings
    }

    func resolveStatus(for permission: Permission) {
        let keyPath = AppState.permissionKeyPath(for: permission)
        let currentStatus = appState[keyPath]
        guard currentStatus == .unknown else { return }
        let appState = appState
        switch permission {
        case .pushNotifications:
            Task { @MainActor in
                appState[keyPath] = await pushNotificationsPermissionStatus()
            }
        }
    }

    func request(permission: Permission) {
        let keyPath = AppState.permissionKeyPath(for: permission)
        let currentStatus = appState[keyPath]
        guard currentStatus != .denied else {
            openAppSettings()
            return
        }
        switch permission {
        case .pushNotifications:
            Task {
                await requestPushNotificationsPermission()
            }
        }
    }
}

// MARK: - Push Notifications

extension UNAuthorizationStatus {
    var map: Permission.Status {
        switch self {
        case .denied: return .denied
        case .authorized: return .granted
        case .notDetermined, .provisional, .ephemeral: return .notRequested
        @unknown default: return .notRequested
        }
    }
}

private extension RealUserPermissionsInteractor {

    func pushNotificationsPermissionStatus() async -> Permission.Status {
        return await notificationCenter
            .currentSettings()
            .authorizationStatus.map
    }

    func requestPushNotificationsPermission() async {
        let center = notificationCenter
        let isGranted = (try? await center.requestAuthorization(options: [.alert, .sound])) ?? false
        appState[\.permissions.push] = isGranted ? .granted : .denied
    }
}

// MARK: -

final class StubUserPermissionsInteractor: UserPermissionsInteractor {

    func resolveStatus(for permission: Permission) {
    }
    func request(permission: Permission) {
    }
}

```

## File: `CountriesSwiftUI/Repositories/Database/CountriesDBRepository.swift`
```
//
//  CountriesDBRepository.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftData
import Foundation

protocol CountriesDBRepository {
    @MainActor
    func countryDetails(for country: DBModel.Country) async throws -> DBModel.CountryDetails?
    func store(countries: [ApiModel.Country]) async throws
    func store(countryDetails: ApiModel.CountryDetails, for country: DBModel.Country) async throws
}

extension MainDBRepository: CountriesDBRepository {

    @MainActor
    func countryDetails(for country: DBModel.Country) async throws -> DBModel.CountryDetails? {
        let alpha3Code = country.alpha3Code
        let fetchDescriptor = FetchDescriptor(predicate: #Predicate<DBModel.CountryDetails> {
            $0.alpha3Code == alpha3Code
        })
        return try modelContainer.mainContext.fetch(fetchDescriptor).first
    }

    func store(countries: [ApiModel.Country]) async throws {
        try modelContext.transaction {
            countries
                .map { $0.dbModel() }
                .forEach {
                    modelContext.insert($0)
                }
        }
    }

    func store(countryDetails: ApiModel.CountryDetails, for country: DBModel.Country) async throws {
        let alpha3Code = country.alpha3Code
        try modelContext.transaction {
            let currencies = countryDetails.currencies.map { $0.dbModel() }
            let neighborsFetch = FetchDescriptor(predicate: #Predicate<DBModel.Country> { countryDBModel in
                countryDetails.borders?.contains(countryDBModel.alpha3Code) == true
            })
            let neighbors = try modelContext.fetch(neighborsFetch)
            currencies.forEach {
                modelContext.insert($0)
            }
            let object = DBModel.CountryDetails(
                alpha3Code: alpha3Code,
                capital: countryDetails.capital,
                currencies: currencies,
                neighbors: neighbors)
            modelContext.insert(object)
        }
    }
}

internal extension ApiModel.Country {
    func dbModel() -> DBModel.Country {
        return .init(name: name, translations: translations,
                     population: population, flag: flag,
                     alpha3Code: alpha3Code)
    }
}

internal extension ApiModel.Currency {
    func dbModel() -> DBModel.Currency {
        return .init(code: code, symbol: symbol, name: name)
    }
}
```

## File: `CountriesSwiftUI/Repositories/Database/ModelContainer.swift`
```
//
//  ModelContainer.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftData

extension ModelContainer {

    static func appModelContainer(
        inMemoryOnly: Bool = false, isStub: Bool = false
    ) throws -> ModelContainer {
        let schema = Schema.appSchema
        let modelConfiguration = ModelConfiguration(isStub ? "stub" : nil, schema: schema, isStoredInMemoryOnly: inMemoryOnly)
        return try ModelContainer(for: schema, configurations: [modelConfiguration])
    }

    static var stub: ModelContainer {
        try! appModelContainer(inMemoryOnly: true, isStub: true)
    }

    var isStub: Bool {
        return configurations.first?.name == "stub"
    }
}

@ModelActor
final actor MainDBRepository { }
```

## File: `CountriesSwiftUI/Repositories/Models/AppSchema.swift`
```
//
//  AppSchema.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftData

enum DBModel { }

extension Schema {
    private static var actualVersion: Schema.Version = Version(1, 0, 0)

    static var appSchema: Schema {
        Schema([
            DBModel.Country.self,
            DBModel.CountryDetails.self,
            DBModel.Currency.self,
        ], version: actualVersion)
    }
}
```

## File: `CountriesSwiftUI/Repositories/Models/Country.swift`
```
//
//  Country.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import Foundation
import SwiftData

// MARK: - Database Model

extension DBModel {

    @Model final class Country {

        var name: String
        var translations: [String: String?]
        var population: Int
        var flag: URL?
        @Attribute(.unique) var alpha3Code: String
        @Relationship(inverse: \CountryDetails.neighbors) var neighbors: [CountryDetails] = []

        init(name: String, translations: [String: String?], population: Int, flag: URL? = nil, alpha3Code: String) {
            self.name = name
            self.translations = translations
            self.population = population
            self.flag = flag
            self.alpha3Code = alpha3Code
        }

        func name(locale: Locale) -> String {
            let localeId = locale.shortIdentifier
            if let value = translations[localeId], let localizedName = value {
                return localizedName
            }
            return name
        }
    }
}

// MARK: - Web API Model

extension ApiModel {

    struct Country: Codable, Equatable {

        let name: String
        let translations: [String: String?]
        let population: Int
        let flag: URL?
        let alpha3Code: String

        enum CodingKeys: String, CodingKey {
            case name
            case translations
            case population
            case flag = "alpha2Code"
            case alpha3Code
        }

        init(name: String, translations: [String: String?], population: Int, flag: URL?, alpha3Code: String) {
            self.name = name
            self.translations = translations
            self.population = population
            self.flag = flag
            self.alpha3Code = alpha3Code
        }

        init(from decoder: Decoder) throws {
            let values = try decoder.container(keyedBy: CodingKeys.self)
            name = try values.decode(String.self, forKey: .name)
            translations = try values.decode([String: String?].self, forKey: .translations)
            population = try values.decode(Int.self, forKey: .population)
            if let alpha2orFlagURL = try? values.decode(String.self, forKey: .flag) {
                let urlString = alpha2orFlagURL.count == 2 ?
                "https://flagcdn.com/w640/\(alpha2orFlagURL.lowercased()).jpg" : alpha2orFlagURL
                flag = URL(string: urlString)
            } else { flag = nil }
            alpha3Code = try values.decode(String.self, forKey: .alpha3Code)
        }
    }
}
```

## File: `CountriesSwiftUI/Repositories/Models/CountryCurrency.swift`
```
//
//  CountryCurrency.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 8/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftData

// MARK: - Database Model

extension DBModel {
    @Model final class Currency {
        @Relationship(inverse: \CountryDetails.currencies) var countries: [CountryDetails] = []
        @Attribute(.unique) var code: String
        var symbol: String?
        var name: String

        init(code: String, symbol: String?, name: String) {
            self.code = code
            self.symbol = symbol
            self.name = name
        }
    }
}

// MARK: - Web API Model

extension ApiModel {
    struct Currency: Codable, Equatable {
        let code: String
        let symbol: String?
        let name: String
    }
}
```

## File: `CountriesSwiftUI/Repositories/Models/CountryDetails.swift`
```
//
//  CountryDetails.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftData

// MARK: - Database Model

extension DBModel {

    @Model final class CountryDetails {
        @Attribute(.unique) var alpha3Code: String
        var capital: String
        var currencies: [Currency]
        var neighbors: [Country]?

        init(alpha3Code: String, capital: String, currencies: [Currency], neighbors: [Country]) {
            self.alpha3Code = alpha3Code
            self.capital = capital
            self.currencies = currencies
            self.neighbors = neighbors
        }
    }
}

// MARK: - Web API Model

extension ApiModel {
    struct CountryDetails: Codable, Equatable {
        let capital: String
        let currencies: [Currency]
        let borders: [String]?
    }
}
```

## File: `CountriesSwiftUI/Repositories/Models/MockedData.swift`
```
//
//  MockedModel.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 27.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation

#if DEBUG

@MainActor
extension ApiModel.Country {
    static let mockedData: [ApiModel.Country] = [
        ApiModel.Country(name: "United States", translations: [:], population: 125000000,
                flag: URL(string: "https://flagcdn.com/w640/us.jpg"), alpha3Code: "USA"),
        ApiModel.Country(name: "Georgia", translations: [:], population: 2340000, flag: nil, alpha3Code: "GEO"),
        ApiModel.Country(name: "Canada", translations: [:], population: 57600000, flag: nil, alpha3Code: "CAN")
    ]
}

@MainActor
extension ApiModel.CountryDetails {
    static var mockedData: [ApiModel.CountryDetails] = {
        let neighbors = ApiModel.Country.mockedData
        return [
            ApiModel.CountryDetails(capital: "Sin City", currencies: ApiModel.Currency.mockedData, borders: ["abc"]),
            ApiModel.CountryDetails(capital: "Los Angeles", currencies: ApiModel.Currency.mockedData, borders: []),
            ApiModel.CountryDetails(capital: "New York", currencies: [], borders: []),
            ApiModel.CountryDetails(capital: "Moscow", currencies: [], borders: ["xyz"])
        ]
    }()
}

@MainActor
extension ApiModel.Currency {
    static let mockedData: [ApiModel.Currency] = [
        ApiModel.Currency(code: "USD", symbol: "$", name: "US Dollar"),
        ApiModel.Currency(code: "EUR", symbol: "€", name: "Euro"),
        ApiModel.Currency(code: "RUB", symbol: "‡", name: "Rouble")
    ]
}

#endif
```

## File: `CountriesSwiftUI/Repositories/WebAPI/CountriesWebRepository.swift`
```
//
//  CountriesWebRepository.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import Foundation

protocol CountriesWebRepository: WebRepository {
    func countries() async throws -> [ApiModel.Country]
    func details(country: DBModel.Country) async throws -> ApiModel.CountryDetails
}

struct RealCountriesWebRepository: CountriesWebRepository {

    let session: URLSession
    let baseURL: String

    init(session: URLSession) {
        self.session = session
        self.baseURL = "https://restcountries.com/v2"
    }

    func countries() async throws -> [ApiModel.Country] {
        return try await call(endpoint: API.allCountries)
    }

    func details(country: DBModel.Country) async throws -> ApiModel.CountryDetails {
        let response: [ApiModel.CountryDetails] = try await call(endpoint: API.countryDetails(countryName: country.name))
        guard let details = response.first else {
            throw APIError.unexpectedResponse
        }
        return details
    }
}

// MARK: - Endpoints

extension RealCountriesWebRepository {
    enum API {
        case allCountries
        case countryDetails(countryName: String)
    }
}

extension RealCountriesWebRepository.API: APICall {
    var path: String {
        switch self {
        case .allCountries:
            return "/all?fields=name,translations,population,flag,alpha3Code"
        case let .countryDetails(countryName):
            let encodedName = countryName.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed)
            return "/name/\(encodedName ?? countryName)"
        }
    }
    var method: String {
        switch self {
        case .allCountries, .countryDetails:
            return "GET"
        }
    }
    var headers: [String: String]? {
        return ["Accept": "application/json"]
    }
    func body() throws -> Data? {
        return nil
    }
}
```

## File: `CountriesSwiftUI/Repositories/WebAPI/ImagesWebRepository.swift`
```
//
//  ImageWebRepository.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 09.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Combine
import UIKit

protocol ImagesWebRepository: WebRepository {
    func loadImage(url: URL) async throws -> UIImage
}

struct RealImagesWebRepository: ImagesWebRepository {

    let session: URLSession
    let baseURL: String
    
    init(session: URLSession) {
        self.session = session
        self.baseURL = ""
    }
    
    func loadImage(url: URL) async throws -> UIImage {
        let (localURL, _) = try await session.download(from: url)
        let data = try Data(contentsOf: localURL)
        guard let image = UIImage(data: data) else {
            throw APIError.imageDeserialization
        }
        return image
    }
}
```

## File: `CountriesSwiftUI/Repositories/WebAPI/PushTokenWebRepository.swift`
```
//
//  PushTokenWebRepository.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Foundation

protocol PushTokenWebRepository: WebRepository {
    func register(devicePushToken: Data) async throws
}

struct RealPushTokenWebRepository: PushTokenWebRepository {
    
    let session: URLSession
    let baseURL: String
    
    init(session: URLSession) {
        self.session = session
        self.baseURL = "https://your-server.com/api/push-token"
    }
    
    func register(devicePushToken: Data) async throws {
        // upload the push token to your server
        // you can as well call a third party library here instead
    }
}
```

## File: `CountriesSwiftUI/Repositories/WebAPI/WebRepository.swift`
```
//
//  WebRepository.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 23.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation
import Combine

enum ApiModel { }

protocol WebRepository {
    var session: URLSession { get }
    var baseURL: String { get }
}

extension WebRepository {
    func call<Value, Decoder>(
        endpoint: APICall,
        decoder: Decoder = JSONDecoder(),
        httpCodes: HTTPCodes = .success
    ) async throws -> Value
    where Value: Decodable, Decoder: TopLevelDecoder, Decoder.Input == Data {

        let request = try endpoint.urlRequest(baseURL: baseURL)
        let (data, response) = try await session.data(for: request)
        guard let code = (response as? HTTPURLResponse)?.statusCode else {
            throw APIError.unexpectedResponse
        }
        guard httpCodes.contains(code) else {
            throw APIError.httpCode(code)
        }
        do {
            return try decoder.decode(Value.self, from: data)
        } catch {
            throw APIError.unexpectedResponse
        }
    }
}

// MARK: - APICall

protocol APICall {
    var path: String { get }
    var method: String { get }
    var headers: [String: String]? { get }
    func body() throws -> Data?
}

enum APIError: Swift.Error, Equatable {
    case invalidURL
    case httpCode(HTTPCode)
    case unexpectedResponse
    case imageDeserialization
}

extension APIError: LocalizedError {
    var errorDescription: String? {
        switch self {
        case .invalidURL: return "Invalid URL"
        case let .httpCode(code): return "Unexpected HTTP code: \(code)"
        case .unexpectedResponse: return "Unexpected response from the server"
        case .imageDeserialization: return "Cannot deserialize image from Data"
        }
    }
}

extension APICall {
    func urlRequest(baseURL: String) throws -> URLRequest {
        guard let url = URL(string: baseURL + path) else {
            throw APIError.invalidURL
        }
        var request = URLRequest(url: url)
        request.httpMethod = method
        request.allHTTPHeaderFields = headers
        request.httpBody = try body()
        return request
    }
}

typealias HTTPCode = Int
typealias HTTPCodes = Range<HTTPCode>

extension HTTPCodes {
    static let success = 200 ..< 300
}
```

## File: `CountriesSwiftUI/Resources/Localizable.xcstrings`
```
{
  "sourceLanguage" : "en",
  "strings" : {
    "" : {

    },
    "%@" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "%@"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "%@"
          }
        }
      }
    },
    "%lld" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "%lld"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "%lld"
          }
        }
      }
    },
    "⚠️ There is an issue with local database" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "⚠️ Es gibt ein Problem mit der lokalen Datenbank"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "⚠️ ローカルデータベースに問題があります"
          }
        }
      }
    },
    "Allow Push" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Push-Benachrichtigungen erlauben"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "プッシュ通知を許可する"
          }
        }
      }
    },
    "An Error Occured" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Ein Fehler ist aufgetreten"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "エラーが発生しました"
          }
        }
      }
    },
    "Basic Info" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Grundlegende Informationen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "基本情報"
          }
        }
      }
    },
    "Cancel loading" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Laden abbrechen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "読み込みをキャンセル"
          }
        }
      }
    },
    "Canceled by user" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Vom Benutzer abgebrochen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "ユーザーによってキャンセルされました"
          }
        }
      }
    },
    "Capital" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Hauptstadt"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "首都"
          }
        }
      }
    },
    "Close" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Schließen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "閉じる"
          }
        }
      }
    },
    "Code" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Code"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "コード"
          }
        }
      }
    },
    "Countries" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Länder"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "国々"
          }
        }
      }
    },
    "Currencies" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Währungen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "通貨"
          }
        }
      }
    },
    "Data is missing" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Daten fehlen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "データが不足しています"
          }
        }
      }
    },
    "Neighboring countries" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Nachbarländer"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "隣接する国々"
          }
        }
      }
    },
    "No matches found" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Keine Übereinstimmungen gefunden"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "一致するものが見つかりません"
          }
        }
      }
    },
    "Population" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Bevölkerung"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "人口"
          }
        }
      }
    },
    "Population %lld" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Bevölkerung %lld"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "人口 %lld"
          }
        }
      }
    },
    "Retry" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Erneut versuchen"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "再試行"
          }
        }
      }
    },
    "Running unit tests" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Führen von Unit-Tests"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "ユニットテストを実行中"
          }
        }
      }
    },
    "Unable to load image" : {
      "localizations" : {
        "de" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "Bild kann nicht geladen werden"
          }
        },
        "ja" : {
          "stringUnit" : {
            "state" : "translated",
            "value" : "画像を読み込めません"
          }
        }
      }
    }
  },
  "version" : "1.0"
}
```

## File: `CountriesSwiftUI/Resources/Assets.xcassets/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `CountriesSwiftUI/Resources/Assets.xcassets/AccentColor.colorset/Contents.json`
```json
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

## File: `CountriesSwiftUI/Resources/Assets.xcassets/AppIcon.appiconset/Contents.json`
```json
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

## File: `CountriesSwiftUI/Resources/Preview Assets.xcassets/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `CountriesSwiftUI/UI/RootViewModifier.swift`
```
//
//  RootViewModifier.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 09.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI
import Combine

// MARK: - RootViewAppearance

struct RootViewAppearance: ViewModifier {
    
    @Environment(\.injected) private var injected: DIContainer
    @State private var isActive: Bool = false
    internal let inspection = Inspection<Self>()
    
    func body(content: Content) -> some View {
        content
            .blur(radius: isActive ? 0 : 10)
            .ignoresSafeArea()
            .onReceive(stateUpdate) { self.isActive = $0 }
            .onReceive(inspection.notice) { self.inspection.visit(self, $0) }
    }
    
    private var stateUpdate: AnyPublisher<Bool, Never> {
        injected.appState.updates(for: \.system.isActive)
    }
}
```

## File: `CountriesSwiftUI/UI/Common/ErrorView.swift`
```
//
//  ErrorView.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 25.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI

struct ErrorView: View {
    let error: Error
    let retryAction: () -> Void
    
    var body: some View {
        VStack {
            Text("An Error Occured")
                .font(.title)
            Text(error.localizedDescription)
                .font(.callout)
                .multilineTextAlignment(.center)
                .padding(.bottom, 40).padding()
            Button(action: retryAction, label: { Text("Retry").bold() })
        }
    }
}

#Preview {
    ErrorView(error: NSError(domain: "", code: 0, userInfo: [
        NSLocalizedDescriptionKey: "Something went wrong"]),
              retryAction: { })
}
```

## File: `CountriesSwiftUI/UI/Common/ImageView.swift`
```
//
//  ImageView.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 25.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI
import Combine

struct ImageView: View {
    
    private let imageURL: URL
    @Environment(\.injected) var injected: DIContainer
    @State private var image: Loadable<UIImage>
    let inspection = Inspection<Self>()
    
    init(imageURL: URL, image: Loadable<UIImage> = .notRequested) {
        self.imageURL = imageURL
        self._image = .init(initialValue: image)
    }
    
    var body: some View {
        content
            .onReceive(inspection.notice) { self.inspection.visit(self, $0) }
    }
    
    @ViewBuilder private var content: some View {
        switch image {
        case .notRequested:
            defaultView()
        case .isLoading:
            loadingView()
        case let .loaded(image):
            loadedView(image)
        case let .failed(error):
            failedView(error)
        }
    }
}

// MARK: - Side Effects

private extension ImageView {
    func loadImage() {
        injected.interactors.images
            .load(image: $image, url: imageURL)
    }
}

// MARK: - Content

private extension ImageView {
    func defaultView() -> some View {
        Text("").onAppear {
            self.loadImage()
        }
    }
    
    func loadingView() -> some View {
        ProgressView()
            .progressViewStyle(CircularProgressViewStyle())
    }
    
    func failedView(_ error: Error) -> some View {
        Text("Unable to load image")
            .font(.footnote)
            .multilineTextAlignment(.center)
            .padding()
    }
    
    func loadedView(_ uiImage: UIImage) -> some View {
        Image(uiImage: uiImage)
            .resizable()
            .aspectRatio(contentMode: .fit)
    }
}

#Preview {
    VStack {
        ImageView(imageURL: URL(string: "https://flagcdn.com/w640/us.jpg")!)
        ImageView(imageURL: URL(string: "https://flagcdn.com/w640/al.jpg")!)
        ImageView(imageURL: URL(string: "https://flagcdn.com/w640/ru.jpg")!)
    }
}
```

## File: `CountriesSwiftUI/UI/Common/Query+Search.swift`
```
//
//  Query+Search.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 8/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI
import SwiftData

extension View {
    /**
     Allows for recreating the @Query each time a searchText changes
     */
    func query<T: PersistentModel>(
        searchText: String,
        results: Binding<[T]>,
        _ builder: @escaping (String) -> Query<T, [T]>
    ) -> some View {
        background {
            QueryViewContainer(searchText: searchText, builder: builder) { _, values in
                results.wrappedValue = values
            }.equatable()
        }
    }
}

/**
 This view serves as a "shield" over QueryView to avoid dual query
 */
private struct QueryViewContainer<T: PersistentModel>: View, Equatable {

    let searchText: String
    let builder: (String) -> Query<T, [T]>
    let results: ([T], [T]) -> Void

    var body: some View {
        QueryView(query: builder(searchText), results: results)
    }

    static func == (lhs: QueryViewContainer<T>, rhs: QueryViewContainer<T>) -> Bool {
        return lhs.searchText == rhs.searchText
    }
}

private struct QueryView<T: PersistentModel>: View {

    @Query var query: [T]
    let results: ([T], [T]) -> Void

    init(query: Query<T, [T]>, results: @escaping ([T], [T]) -> Void) {
        _query = query
        self.results = results
    }

    var body: some View {
        Rectangle()
            .hidden()
            .onChange(of: query, initial: true, results)
    }
}
```

## File: `CountriesSwiftUI/UI/CountriesList/CountriesListView.swift`
```
//
//  CountriesList.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI
import SwiftData
import Combine

struct CountriesList: View {

    @State private var countries: [DBModel.Country] = []
    @State private(set) var countriesState: Loadable<Void>
    @State private var canRequestPushPermission: Bool = false
    @State internal var searchText = ""
    @State internal var navigationPath = NavigationPath()
    @State private var routingState: Routing = .init()
    private var routingBinding: Binding<Routing> {
        $routingState.dispatched(to: injected.appState, \.routing.countriesList)
    }
    @Environment(\.injected) private var injected: DIContainer
    @Environment(\.locale) private var locale: Locale
    private let localeContainer = LocaleReader.Container()

    let inspection = Inspection<Self>()

    init(state: Loadable<Void> = .notRequested) {
        self._countriesState = .init(initialValue: state)
    }

    var body: some View {
        NavigationStack(path: $navigationPath) {
            content
                .query(searchText: searchText, results: $countries, { search in
                    Query(filter: #Predicate<DBModel.Country> { country in
                        if search.isEmpty {
                            return true
                        } else {
                            return country.name.localizedStandardContains(search)
                        }
                    }, sort: \DBModel.Country.name)
                })
                .navigationTitle("Countries")
        }
        .modifier(LocaleReader(container: localeContainer))
        .onReceive(routingUpdate) { self.routingState = $0 }
        .onReceive(canRequestPushPermissionUpdate) { self.canRequestPushPermission = $0 }
        .onReceive(inspection.notice) { self.inspection.visit(self, $0) }
        .flipsForRightToLeftLayoutDirection(true)
    }

    @ViewBuilder private var content: some View {
        switch countriesState {
        case .notRequested:
            defaultView()
        case .isLoading:
            loadingView()
        case .loaded:
            loadedView()
        case let .failed(error):
            failedView(error)
        }
    }

    @ViewBuilder private var permissionsButton: some View {
        if canRequestPushPermission {
            Button(action: requestPushPermission, label: { Text("Allow Push") })
        }
    }
}

// MARK: - Loading Content

private extension CountriesList {
    func defaultView() -> some View {
        Text("").onAppear {
            if !countries.isEmpty {
                countriesState = .loaded(())
            }
            loadCountriesList(forceReload: false)
        }
    }

    func loadingView() -> some View {
        ProgressView()
            .progressViewStyle(CircularProgressViewStyle())
    }

    func failedView(_ error: Error) -> some View {
        ErrorView(error: error, retryAction: {
            loadCountriesList(forceReload: true)
        })
    }
}

// MARK: - Displaying Content

@MainActor
private extension CountriesList {
    @ViewBuilder
    func loadedView() -> some View {
        if countries.isEmpty && !searchText.isEmpty {
            Text("No matches found")
                .font(.footnote)
        }
        List(countries, id: \.alpha3Code) { country in
            NavigationLink(value: country) {
                CountryCell(country: country)
            }
        }
        .navigationDestination(for: DBModel.Country.self) { country in
            CountryDetails(country: country)
        }
        .searchable(text: $searchText)
        .refreshable {
            loadCountriesList(forceReload: true)
        }
        .toolbar {
            ToolbarItem {
                permissionsButton
            }
        }
        .onChange(of: routingState.countryCode, initial: true, { _, code in
            guard let code,
                  let country = countries.first(where: { $0.alpha3Code == code})
            else { return }
            navigationPath.append(country)
        })
        .onChange(of: navigationPath, { _, path in
            if !path.isEmpty {
                routingBinding.wrappedValue.countryCode = nil
            }
        })
    }
}

// MARK: - Side Effects

private extension CountriesList {

    private func loadCountriesList(forceReload: Bool) {
        guard forceReload || countries.isEmpty else { return }
        $countriesState.load {
            try await injected.interactors.countries
                .refreshCountriesList()
        }
    }

    private func requestPushPermission() {
        injected.interactors.userPermissions
            .request(permission: .pushNotifications)
    }
}

// MARK: - Routing

extension CountriesList {
    struct Routing: Equatable {
        var countryCode: String?
    }
}

// MARK: - State Updates

private extension CountriesList {

    private var routingUpdate: AnyPublisher<Routing, Never> {
        injected.appState.updates(for: \.routing.countriesList)
    }

    private var canRequestPushPermissionUpdate: AnyPublisher<Bool, Never> {
        injected.appState.updates(for: AppState.permissionKeyPath(for: .pushNotifications))
            .map { $0 == .notRequested || $0 == .denied }
            .eraseToAnyPublisher()
    }
}
```

## File: `CountriesSwiftUI/UI/CountriesList/CountryCell.swift`
```
//
//  CountryCell.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI

struct CountryCell: View {

    let country: DBModel.Country
    @Environment(\.locale) var locale: Locale

    var body: some View {
        VStack(alignment: .leading) {
            Text(country.name(locale: locale))
                .font(.title)
            Text("Population \(country.population)")
                .font(.caption)
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: 60, alignment: .leading)
    }
}
```

## File: `CountriesSwiftUI/UI/CountriesList/LocaleReader.swift`
```
//
//  LocaleReader.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 8/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import SwiftUI

extension CountriesList {

    struct LocaleReader: EnvironmentalModifier {

        /**
         Retains the locale, provided by the Environment.
         Variable `@Environment(\.locale) var locale: Locale`
         from the view is not accessible when searching by name
         */
        final class Container {
            var locale: Locale = .backendDefault
        }
        let container: Container

        func resolve(in environment: EnvironmentValues) -> some ViewModifier {
            container.locale = environment.locale
            return DummyViewModifier()
        }

        private struct DummyViewModifier: ViewModifier {
            func body(content: Content) -> some View {
                // Cannot return just `content` because SwiftUI
                // flattens modifiers that do nothing to the `content`
                content.onAppear()
            }
        }
    }
}
```

## File: `CountriesSwiftUI/UI/CountryDetails/CountryDetailsView.swift`
```
//
//  CountryDetails.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 25.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI
import Combine
import SwiftData

@MainActor
struct CountryDetails: View {
    
    private let country: DBModel.Country

    @Environment(\.locale) var locale: Locale
    @Environment(\.injected) private var injected: DIContainer
    @State private var details: Loadable<DBModel.CountryDetails>
    @State private var routingState: Routing = .init()
    private var routingBinding: Binding<Routing> {
        $routingState.dispatched(to: injected.appState, \.routing.countryDetails)
    }
    let inspection = Inspection<Self>()
    
    init(country: DBModel.Country, details: Loadable<DBModel.CountryDetails> = .notRequested) {
        self.country = country
        self._details = .init(initialValue: details)
    }
    
    var body: some View {
        content
            .navigationBarTitle(country.name(locale: locale))
            .onReceive(routingUpdate) { self.routingState = $0 }
            .onReceive(inspection.notice) { self.inspection.visit(self, $0) }
    }
    
    @ViewBuilder private var content: some View {
        switch details {
        case .notRequested:
            defaultView()
        case .isLoading:
            loadingView()
        case let .loaded(countryDetails):
            loadedView(countryDetails)
        case let .failed(error):
            failedView(error)
        }
    }
}

// MARK: - Side Effects

private extension CountryDetails {

    func loadCountryDetails(forceReload: Bool) {
        $details.load {
            try await injected.interactors.countries
                .loadCountryDetails(country: country, forceReload: forceReload)
        }
    }
    
    func showCountryDetailsSheet() {
        injected.appState[\.routing.countryDetails.detailsSheet] = true
    }
}

// MARK: - Loading Content

private extension CountryDetails {
    func defaultView() -> some View {
        Text("").onAppear {
            loadCountryDetails(forceReload: false)
        }
    }
    
    func loadingView() -> some View {
        VStack {
            ProgressView()
                .progressViewStyle(CircularProgressViewStyle())
            Button(action: {
                self.details.cancelLoading()
            }, label: { Text("Cancel loading") })
        }
    }
    
    func failedView(_ error: Error) -> some View {
        ErrorView(error: error, retryAction: {
            self.loadCountryDetails(forceReload: true)
        })
    }
}

// MARK: - Displaying Content

@MainActor
private extension CountryDetails {
    func loadedView(_ countryDetails: DBModel.CountryDetails) -> some View {
        List {
            country.flag.map { url in
                flagView(url: url)
            }
            basicInfoSectionView(countryDetails: countryDetails)
            if countryDetails.currencies.count > 0 {
                currenciesSectionView(currencies: countryDetails.currencies)
            }
            if let neighbors = countryDetails.neighbors {
                if neighbors.count  > 0 {
                    neighborsSectionView(neighbors: neighbors)
                }
            }
        }
        .listStyle(GroupedListStyle())
        .sheet2(isPresented: routingBinding.detailsSheet,
                content: { self.modalDetailsView() })
    }
    
    func flagView(url: URL) -> some View {
        HStack {
            Spacer()
            ImageView(imageURL: url)
                .frame(width: 120, height: 80)
                .onTapGesture {
                    self.showCountryDetailsSheet()
                }
            Spacer()
        }
    }
    
    func basicInfoSectionView(countryDetails: DBModel.CountryDetails) -> some View {
        Section(header: Text("Basic Info")) {
            DetailRow(leftLabel: Text(country.alpha3Code), rightLabel: "Code")
            DetailRow(leftLabel: Text("\(country.population)"), rightLabel: "Population")
            DetailRow(leftLabel: Text("\(countryDetails.capital)"), rightLabel: "Capital")
        }
    }
    
    func currenciesSectionView(currencies: [DBModel.Currency]) -> some View {
        Section(header: Text("Currencies")) {
            ForEach(currencies) { currency in
                DetailRow(leftLabel: Text(currency.title), rightLabel: Text(currency.code))
            }
        }
    }
    
    func neighborsSectionView(neighbors: [DBModel.Country]) -> some View {
        Section(header: Text("Neighboring countries")) {
            ForEach(neighbors) { country in
                NavigationLink(destination: self.neighbourDetailsView(country: country)) {
                    DetailRow(leftLabel: Text(country.name(locale: self.locale)), rightLabel: "")
                }
            }
        }
    }
    
    func neighbourDetailsView(country: DBModel.Country) -> some View {
        CountryDetails(country: country)
    }
    
    func modalDetailsView() -> some View {
        ModalFlagView(country: country,
                      isDisplayed: routingBinding.detailsSheet)
            .inject(injected)
    }
}

// MARK: - Helpers

private extension DBModel.Currency {
    var title: String {
        return name + (symbol.map {" " + $0} ?? "")
    }
}

// MARK: - Routing

extension CountryDetails {
    struct Routing: Equatable {
        var detailsSheet: Bool = false
    }
}

// MARK: - State Updates

private extension CountryDetails {
    
    var routingUpdate: AnyPublisher<Routing, Never> {
        injected.appState.updates(for: \.routing.countryDetails)
    }
}

// MARK: - ViewInspector helper
// https://github.com/nalexn/ViewInspector/blob/master/guide_popups.md#sheet

extension View {
    func sheet2<Sheet>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Sheet
    ) -> some View where Sheet: View {
        return self.modifier(InspectableSheet(isPresented: isPresented, onDismiss: onDismiss, popupBuilder: content))
    }
}

struct InspectableSheet<Sheet>: ViewModifier where Sheet: View {

    let isPresented: Binding<Bool>
    let onDismiss: (() -> Void)?
    let popupBuilder: () -> Sheet

    func body(content: Self.Content) -> some View {
        content.sheet(isPresented: isPresented, onDismiss: onDismiss, content: popupBuilder)
    }
}
```

## File: `CountriesSwiftUI/UI/CountryDetails/DetailRow.swift`
```
//
//  DetailRow.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 25.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI

struct DetailRow: View {
    private let leftLabel: Text
    private let rightLabel: Text
    
    init(leftLabel: Text, rightLabel: Text) {
        self.leftLabel = leftLabel
        self.rightLabel = rightLabel
    }
    
    init(leftLabel: Text, rightLabel: LocalizedStringKey) {
        self.leftLabel = leftLabel
        self.rightLabel = Text(rightLabel)
    }
    
    var body: some View {
        HStack {
            leftLabel
                .font(.headline)
            Spacer()
            rightLabel
                .font(.callout)
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: 40, alignment: .leading)
    }
}

#Preview(traits: .fixedLayout(width: 375, height: 40)) {
    DetailRow(leftLabel: Text("Rate"), rightLabel: Text("$123.99"))
}
```

## File: `CountriesSwiftUI/UI/CountryDetails/ModalFlagView.swift`
```
//
//  ModalFlagView.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 26.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import SwiftUI
import EnvironmentOverrides

struct ModalFlagView: View {

    let country: DBModel.Country
    @Binding var isDisplayed: Bool
    let inspection = Inspection<Self>()
    
    var body: some View {
        NavigationStack {
            country.flag.map { url in
                HStack {
                    Spacer()
                    ImageView(imageURL: url)
                        .frame(width: 300, height: 200)
                    Spacer()
                }
            }
            .navigationTitle(country.name)
            .toolbar {
                ToolbarItem {
                    closeButton
                }
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .onReceive(inspection.notice) { self.inspection.visit(self, $0) }
        .attachEnvironmentOverrides()
    }
    
    private var closeButton: some View {
        Button(action: {
            self.isDisplayed = false
        }, label: { Text("Close") })
    }
}
```

## File: `CountriesSwiftUI/Utilities/CancelBag.swift`
```
//
//  CancelBag.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 04.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Combine

final class CancelBag {
    fileprivate(set) var subscriptions = [any Cancellable]()
    private let equalToAny: Bool
    
    init(equalToAny: Bool = false) {
        self.equalToAny = equalToAny
    }
    
    func cancel() {
        subscriptions.removeAll()
    }
    
    func isEqual(to other: CancelBag) -> Bool {
        return other === self || other.equalToAny || self.equalToAny
    }
}

extension Cancellable {
    
    func store(in cancelBag: CancelBag) {
        cancelBag.subscriptions.append(self)
    }
}

extension Task: @retroactive Cancellable { }
```

## File: `CountriesSwiftUI/Utilities/Helpers.swift`
```
//
//  Helpers.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 7/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import Foundation
import Combine

extension ProcessInfo {
    var isRunningTests: Bool {
        environment["XCTestConfigurationFilePath"] != nil
    }
}

extension String {
    func localized(_ locale: Locale) -> String {
        let localeId = locale.shortIdentifier
        guard let path = Bundle.main.path(forResource: localeId, ofType: "lproj"),
            let bundle = Bundle(path: path) else {
            return NSLocalizedString(self, comment: "")
        }
        return bundle.localizedString(forKey: self, value: nil, table: nil)
    }
}

extension Locale {
    static var backendDefault: Locale {
        return Locale(identifier: "en")
    }

    var shortIdentifier: String {
        return String(identifier.prefix(2))
    }
}

extension Result {
    var isSuccess: Bool {
        switch self {
        case .success: return true
        case .failure: return false
        }
    }
}

// MARK: - View Inspection helper

internal final class Inspection<V> {
    let notice = PassthroughSubject<UInt, Never>()
    var callbacks = [UInt: (V) -> Void]()

    func visit(_ view: V, _ line: UInt) {
        if let callback = callbacks.removeValue(forKey: line) {
            callback(view)
        }
    }
}
```

## File: `CountriesSwiftUI/Utilities/Loadable.swift`
```
//
//  Loadable.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 23.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation
import SwiftUI

typealias LoadableSubject<T> = Binding<Loadable<T>>

enum Loadable<T> {

    case notRequested
    case isLoading(last: T?, cancelBag: CancelBag)
    case loaded(T)
    case failed(Error)

    var value: T? {
        switch self {
        case let .loaded(value): return value
        case let .isLoading(last, _): return last
        default: return nil
        }
    }
    var error: Error? {
        switch self {
        case let .failed(error): return error
        default: return nil
        }
    }
}

extension Loadable {
    
    mutating func setIsLoading(cancelBag: CancelBag) {
        self = .isLoading(last: value, cancelBag: cancelBag)
    }
    
    mutating func cancelLoading() {
        switch self {
        case let .isLoading(last, cancelBag):
            cancelBag.cancel()
            if let last = last {
                self = .loaded(last)
            } else {
                let error = NSError(
                    domain: NSCocoaErrorDomain, code: NSUserCancelledError,
                    userInfo: [NSLocalizedDescriptionKey: NSLocalizedString("Canceled by user", comment: "")])
                self = .failed(error)
            }
        default: break
        }
    }
    
    func map<V>(_ transform: (T) throws -> V) -> Loadable<V> {
        do {
            switch self {
            case .notRequested: return .notRequested
            case let .failed(error): return .failed(error)
            case let .isLoading(value, cancelBag):
                return .isLoading(last: try value.map { try transform($0) },
                                  cancelBag: cancelBag)
            case let .loaded(value):
                return .loaded(try transform(value))
            }
        } catch {
            return .failed(error)
        }
    }
}

protocol SomeOptional {
    associatedtype Wrapped
    func unwrap() throws -> Wrapped
}

struct ValueIsMissingError: Error {
    var localizedDescription: String {
        NSLocalizedString("Data is missing", comment: "")
    }
}

extension Optional: SomeOptional {
    func unwrap() throws -> Wrapped {
        switch self {
        case let .some(value): return value
        case .none: throw ValueIsMissingError()
        }
    }
}

extension Loadable where T: SomeOptional {
    func unwrap() -> Loadable<T.Wrapped> {
        map { try $0.unwrap() }
    }
}

extension Loadable: Equatable where T: Equatable {
    static func == (lhs: Loadable<T>, rhs: Loadable<T>) -> Bool {
        switch (lhs, rhs) {
        case (.notRequested, .notRequested): return true
        case let (.isLoading(lhsV, lhsC), .isLoading(rhsV, rhsC)):
            return lhsV == rhsV && lhsC.isEqual(to: rhsC)
        case let (.loaded(lhsV), .loaded(rhsV)): return lhsV == rhsV
        case let (.failed(lhsE), .failed(rhsE)):
            return lhsE.localizedDescription == rhsE.localizedDescription
        default: return false
        }
    }
}

extension LoadableSubject {
    func load<T>(_ resource: @escaping () async throws -> T) where Value == Loadable<T> {
        let cancelBag = CancelBag()
        wrappedValue.setIsLoading(cancelBag: cancelBag)
        let task = Task {
            do {
                wrappedValue = .loaded(try await resource())
            } catch {
                wrappedValue = .failed(error)
            }
        }
        task.store(in: cancelBag)
    }
}
```

## File: `CountriesSwiftUI/Utilities/Store.swift`
```
//
//  Store.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 04.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import SwiftUI
import Combine

typealias Store<State> = CurrentValueSubject<State, Never>

extension Store {

    subscript<T>(keyPath: WritableKeyPath<Output, T>) -> T where T: Equatable {
        get { value[keyPath: keyPath] }
        set {
            var value = self.value
            if value[keyPath: keyPath] != newValue {
                value[keyPath: keyPath] = newValue
                self.value = value
            }
        }
    }

    func bulkUpdate(_ update: (inout Output) -> Void) {
        var value = self.value
        update(&value)
        self.value = value
    }

    func updates<Value>(for keyPath: KeyPath<Output, Value>) ->
        AnyPublisher<Value, Failure> where Value: Equatable {
        return map(keyPath).removeDuplicates().eraseToAnyPublisher()
    }
}

// MARK: -

extension Binding where Value: Equatable {
    func dispatched<State>(to state: Store<State>,
                           _ keyPath: WritableKeyPath<State, Value>) -> Self {
        return onSet { state[keyPath] = $0 }
    }
}

extension Binding where Value: Equatable {
    typealias ValueClosure = (Value) -> Void

    func onSet(_ perform: @escaping ValueClosure) -> Self {
        return .init(get: { () -> Value in
            self.wrappedValue
        }, set: { value in
            if self.wrappedValue != value {
                self.wrappedValue = value
            }
            perform(value)
        })
    }
}

```

## File: `CountriesSwiftUI.xcodeproj/project.pbxproj`
```
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 77;
	objects = {

/* Begin PBXBuildFile section */
		4819F10E2CDF5819003CA0AE /* EnvironmentOverrides in Frameworks */ = {isa = PBXBuildFile; productRef = 4819F10D2CDF5819003CA0AE /* EnvironmentOverrides */; };
		4819F1172CDF6DD4003CA0AE /* ViewInspector in Frameworks */ = {isa = PBXBuildFile; productRef = 4819F1162CDF6DD4003CA0AE /* ViewInspector */; };
/* End PBXBuildFile section */

/* Begin PBXContainerItemProxy section */
		4887342A2CDCA2DD00B400A3 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = 4887340F2CDCA2DB00B400A3 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = 488734162CDCA2DB00B400A3;
			remoteInfo = CountriesSwiftUI;
		};
/* End PBXContainerItemProxy section */

/* Begin PBXFileReference section */
		488734172CDCA2DB00B400A3 /* CountriesSwiftUI.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = CountriesSwiftUI.app; sourceTree = BUILT_PRODUCTS_DIR; };
		488734292CDCA2DD00B400A3 /* UnitTests.xctest */ = {isa = PBXFileReference; explicitFileType = wrapper.cfbundle; includeInIndex = 0; path = UnitTests.xctest; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFileSystemSynchronizedRootGroup section */
		488734192CDCA2DB00B400A3 /* CountriesSwiftUI */ = {
			isa = PBXFileSystemSynchronizedRootGroup;
			path = CountriesSwiftUI;
			sourceTree = "<group>";
		};
		4887342C2CDCA2DD00B400A3 /* UnitTests */ = {
			isa = PBXFileSystemSynchronizedRootGroup;
			path = UnitTests;
			sourceTree = "<group>";
		};
/* End PBXFileSystemSynchronizedRootGroup section */

/* Begin PBXFrameworksBuildPhase section */
		488734142CDCA2DB00B400A3 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				4819F10E2CDF5819003CA0AE /* EnvironmentOverrides in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		488734262CDCA2DD00B400A3 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				4819F1172CDF6DD4003CA0AE /* ViewInspector in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		4887340E2CDCA2DB00B400A3 = {
			isa = PBXGroup;
			children = (
				488734192CDCA2DB00B400A3 /* CountriesSwiftUI */,
				4887342C2CDCA2DD00B400A3 /* UnitTests */,
				488734182CDCA2DB00B400A3 /* Products */,
			);
			sourceTree = "<group>";
		};
		488734182CDCA2DB00B400A3 /* Products */ = {
			isa = PBXGroup;
			children = (
				488734172CDCA2DB00B400A3 /* CountriesSwiftUI.app */,
				488734292CDCA2DD00B400A3 /* UnitTests.xctest */,
			);
			name = Products;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		488734162CDCA2DB00B400A3 /* CountriesSwiftUI */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 4887343D2CDCA2DD00B400A3 /* Build configuration list for PBXNativeTarget "CountriesSwiftUI" */;
			buildPhases = (
				488734132CDCA2DB00B400A3 /* Sources */,
				488734142CDCA2DB00B400A3 /* Frameworks */,
				488734152CDCA2DB00B400A3 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			fileSystemSynchronizedGroups = (
				488734192CDCA2DB00B400A3 /* CountriesSwiftUI */,
			);
			name = CountriesSwiftUI;
			packageProductDependencies = (
				4819F10D2CDF5819003CA0AE /* EnvironmentOverrides */,
			);
			productName = CountriesSwiftUI;
			productReference = 488734172CDCA2DB00B400A3 /* CountriesSwiftUI.app */;
			productType = "com.apple.product-type.application";
		};
		488734282CDCA2DD00B400A3 /* UnitTests */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 488734402CDCA2DD00B400A3 /* Build configuration list for PBXNativeTarget "UnitTests" */;
			buildPhases = (
				488734252CDCA2DD00B400A3 /* Sources */,
				488734262CDCA2DD00B400A3 /* Frameworks */,
				488734272CDCA2DD00B400A3 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
				4887342B2CDCA2DD00B400A3 /* PBXTargetDependency */,
			);
			fileSystemSynchronizedGroups = (
				4887342C2CDCA2DD00B400A3 /* UnitTests */,
			);
			name = UnitTests;
			packageProductDependencies = (
				4819F1162CDF6DD4003CA0AE /* ViewInspector */,
			);
			productName = CountriesSwiftUITests;
			productReference = 488734292CDCA2DD00B400A3 /* UnitTests.xctest */;
			productType = "com.apple.product-type.bundle.unit-test";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		4887340F2CDCA2DB00B400A3 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1610;
				LastUpgradeCheck = 1610;
				ORGANIZATIONNAME = "Alexey Naumov";
				TargetAttributes = {
					488734162CDCA2DB00B400A3 = {
						CreatedOnToolsVersion = 16.1;
					};
					488734282CDCA2DD00B400A3 = {
						CreatedOnToolsVersion = 16.1;
						TestTargetID = 488734162CDCA2DB00B400A3;
					};
				};
			};
			buildConfigurationList = 488734122CDCA2DB00B400A3 /* Build configuration list for PBXProject "CountriesSwiftUI" */;
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
				ja,
				de,
			);
			mainGroup = 4887340E2CDCA2DB00B400A3;
			minimizedProjectReferenceProxies = 1;
			packageReferences = (
				4819F10C2CDF5819003CA0AE /* XCRemoteSwiftPackageReference "EnvironmentOverrides" */,
				4819F1152CDF6DD4003CA0AE /* XCRemoteSwiftPackageReference "ViewInspector" */,
			);
			preferredProjectObjectVersion = 77;
			productRefGroup = 488734182CDCA2DB00B400A3 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				488734162CDCA2DB00B400A3 /* CountriesSwiftUI */,
				488734282CDCA2DD00B400A3 /* UnitTests */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		488734152CDCA2DB00B400A3 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		488734272CDCA2DD00B400A3 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		488734132CDCA2DB00B400A3 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		488734252CDCA2DD00B400A3 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin PBXTargetDependency section */
		4887342B2CDCA2DD00B400A3 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = 488734162CDCA2DB00B400A3 /* CountriesSwiftUI */;
			targetProxy = 4887342A2CDCA2DD00B400A3 /* PBXContainerItemProxy */;
		};
/* End PBXTargetDependency section */

/* Begin XCBuildConfiguration section */
		4887343B2CDCA2DD00B400A3 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 18.1;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		4887343C2CDCA2DD00B400A3 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 18.1;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_EMIT_LOC_STRINGS = YES;
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		4887343E2CDCA2DD00B400A3 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "\"CountriesSwiftUI/Resources\"";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				IPHONEOS_DEPLOYMENT_TARGET = 18.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 3.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.swiftui.CountriesSwiftUI;
				PRODUCT_NAME = "$(TARGET_NAME)";
				REGISTER_APP_GROUPS = NO;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator macosx";
				SUPPORTS_MACCATALYST = NO;
				SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD = NO;
				SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD = NO;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		4887343F2CDCA2DD00B400A3 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "\"CountriesSwiftUI/Resources\"";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				IPHONEOS_DEPLOYMENT_TARGET = 18.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 3.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.swiftui.CountriesSwiftUI;
				PRODUCT_NAME = "$(TARGET_NAME)";
				REGISTER_APP_GROUPS = NO;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator macosx";
				SUPPORTS_MACCATALYST = NO;
				SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD = NO;
				SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD = NO;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
		488734412CDCA2DD00B400A3 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 18.1;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.swiftui.CountriesSwiftUITests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = NO;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/CountriesSwiftUI.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/CountriesSwiftUI";
			};
			name = Debug;
		};
		488734422CDCA2DD00B400A3 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				BUNDLE_LOADER = "$(TEST_HOST)";
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 18.1;
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.swiftui.CountriesSwiftUITests;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = NO;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
				TEST_HOST = "$(BUILT_PRODUCTS_DIR)/CountriesSwiftUI.app/$(BUNDLE_EXECUTABLE_FOLDER_PATH)/CountriesSwiftUI";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		488734122CDCA2DB00B400A3 /* Build configuration list for PBXProject "CountriesSwiftUI" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				4887343B2CDCA2DD00B400A3 /* Debug */,
				4887343C2CDCA2DD00B400A3 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		4887343D2CDCA2DD00B400A3 /* Build configuration list for PBXNativeTarget "CountriesSwiftUI" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				4887343E2CDCA2DD00B400A3 /* Debug */,
				4887343F2CDCA2DD00B400A3 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		488734402CDCA2DD00B400A3 /* Build configuration list for PBXNativeTarget "UnitTests" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				488734412CDCA2DD00B400A3 /* Debug */,
				488734422CDCA2DD00B400A3 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */

/* Begin XCRemoteSwiftPackageReference section */
		4819F10C2CDF5819003CA0AE /* XCRemoteSwiftPackageReference "EnvironmentOverrides" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/nalexn/EnvironmentOverrides";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 0.0.4;
			};
		};
		4819F1152CDF6DD4003CA0AE /* XCRemoteSwiftPackageReference "ViewInspector" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/nalexn/ViewInspector";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 0.10.0;
			};
		};
/* End XCRemoteSwiftPackageReference section */

/* Begin XCSwiftPackageProductDependency section */
		4819F10D2CDF5819003CA0AE /* EnvironmentOverrides */ = {
			isa = XCSwiftPackageProductDependency;
			package = 4819F10C2CDF5819003CA0AE /* XCRemoteSwiftPackageReference "EnvironmentOverrides" */;
			productName = EnvironmentOverrides;
		};
		4819F1162CDF6DD4003CA0AE /* ViewInspector */ = {
			isa = XCSwiftPackageProductDependency;
			package = 4819F1152CDF6DD4003CA0AE /* XCRemoteSwiftPackageReference "ViewInspector" */;
			productName = ViewInspector;
		};
/* End XCSwiftPackageProductDependency section */
	};
	rootObject = 4887340F2CDCA2DB00B400A3 /* Project object */;
}
```

## File: `CountriesSwiftUI.xcodeproj/xcshareddata/xcschemes/CountriesSwiftUI.xcscheme`
```
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1610"
   version = "1.7">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES"
      buildArchitectures = "Automatic">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "488734162CDCA2DB00B400A3"
               BuildableName = "CountriesSwiftUI.app"
               BlueprintName = "CountriesSwiftUI"
               ReferencedContainer = "container:CountriesSwiftUI.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      shouldUseLaunchSchemeArgsEnv = "YES"
      shouldAutocreateTestPlan = "YES">
      <Testables>
         <TestableReference
            skipped = "NO"
            parallelizable = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "488734282CDCA2DD00B400A3"
               BuildableName = "UnitTests.xctest"
               BlueprintName = "UnitTests"
               ReferencedContainer = "container:CountriesSwiftUI.xcodeproj">
            </BuildableReference>
         </TestableReference>
      </Testables>
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "488734162CDCA2DB00B400A3"
            BuildableName = "CountriesSwiftUI.app"
            BlueprintName = "CountriesSwiftUI"
            ReferencedContainer = "container:CountriesSwiftUI.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Release"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "488734162CDCA2DB00B400A3"
            BuildableName = "CountriesSwiftUI.app"
            BlueprintName = "CountriesSwiftUI"
            ReferencedContainer = "container:CountriesSwiftUI.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>
```

## File: `UnitTests/TestHelpers.swift`
```
//
//  TestHelpers.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 15/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import UIKit.UIColor
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

// MARK: - UI

extension UIColor {
    func image(_ size: CGSize = CGSize(width: 1, height: 1)) -> UIImage {
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        return UIGraphicsImageRenderer(size: size, format: format).image { rendererContext in
            setFill()
            rendererContext.fill(CGRect(origin: .zero, size: size))
        }
    }
}

// MARK: - Errors

enum MockError: Swift.Error {
    case valueNotSet
    case codeDataModel
}

extension NSError {
    static var test: NSError {
        return NSError(domain: "test", code: 0, userInfo: [NSLocalizedDescriptionKey: "Test error"])
    }
}

// MARK: - Misc

extension CancelBag {
    static var test: CancelBag {
        return CancelBag(equalToAny: true)
    }
}

struct TestExpectation {

    private let signal: AsyncStream<Void>.Continuation?
    private let stream: AsyncStream<Void>
    private let expectedCount: Int

    init(expectedCount: Int = 1) {
        precondition(expectedCount > 0)
        self.expectedCount = expectedCount
        var signal: AsyncStream<Void>.Continuation?
        self.stream = AsyncStream<Void> { signal = $0 }
        self.signal = signal
    }

    func fulfill() {
        signal?.yield()
    }

    func fulfillment() async {
        await stream
            .dropFirst(expectedCount - 1)
            .first(where: { _ in true })
    }
}

final class BindingWithHistory<Value> {

    private(set) var binding: Binding<Value>
    private(set) var history: [Value]

    init(value: Value) {
        binding = .constant(value)
        history = [value]
        var value = value
        binding = Binding<Value>(get: {
            value
        }, set: { [weak self] in
            value = $0
            self?.history.append($0)
        })
    }
}

extension Inspection: @retroactive InspectionEmissary { }
```

## File: `UnitTests/Mocks/Mock.swift`
```
//
//  Mock.swift
//  UnitTests
//
//  Created by Alexey Naumov on 07.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
@testable import CountriesSwiftUI

protocol Mock {
    associatedtype Action: Equatable
    var actions: MockActions<Action> { get }
    
    func register(_ action: Action)
    func verify(sourceLocation: SourceLocation)
}

extension Mock {
    func register(_ action: Action) {
        actions.register(action)
    }
    
    func verify(sourceLocation: SourceLocation = #_sourceLocation) {
        actions.verify(sourceLocation: sourceLocation)
    }
}

final class MockActions<Action> where Action: Equatable {
    let expected: [Action]
    var factual: [Action] = []
    
    init(expected: [Action]) {
        self.expected = expected
    }
    
    fileprivate func register(_ action: Action) {
        factual.append(action)
    }
    
    fileprivate func verify(sourceLocation: SourceLocation) {
        let factualNames = factual.map { "." + String(describing: $0) }
        let expectedNames = expected.map { "." + String(describing: $0) }
        let name = name
        #expect(factual == expected, "\(name)\n\nExpected:\n\n\(expectedNames)\n\nReceived:\n\n\(factualNames)", sourceLocation: sourceLocation)
    }
    
    private var name: String {
        let fullName = String(describing: self)
        let nameComponents = fullName.components(separatedBy: ".")
        return nameComponents.dropLast().last ?? fullName
    }
}
```

## File: `UnitTests/Mocks/MockedDBRepositories.swift`
```
//
//  MockedDBRepositories.swift
//  UnitTests
//
//  Created by Alexey Naumov on 18.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import SwiftData
@testable import CountriesSwiftUI

// MARK: - CountriesWebRepository

final class MockedCountriesDBRepository: Mock, CountriesDBRepository {
    
    enum Action: Equatable {
        case fetchCountryDetails(DBModel.Country)
        case storeCountries([ApiModel.Country])
        case storeDetails(ApiModel.CountryDetails, country: DBModel.Country)
    }
    var actions = MockActions<Action>(expected: [])

    var storeCountriesResults: [Result<Void, Error>] = []
    var storeCountryDetailsResults: [Result<Void, Error>] = []
    var countryDetailsResults: [Result<DBModel.CountryDetails?, Error>] = []

    // MARK: - API

    @MainActor
    func countryDetails(for country: DBModel.Country) async throws -> DBModel.CountryDetails? {
        register(.fetchCountryDetails(country))
        guard !countryDetailsResults.isEmpty else { throw MockError.valueNotSet }
        return try countryDetailsResults.removeFirst().get()
    }

    func store(countries: [ApiModel.Country]) async throws {
        register(.storeCountries(countries))
        guard !storeCountriesResults.isEmpty else { throw MockError.valueNotSet }
        try storeCountriesResults.removeFirst().get()
    }

    func store(countryDetails: ApiModel.CountryDetails, for country: DBModel.Country) async throws {
        register(.storeDetails(countryDetails, country: country))
        guard !storeCountryDetailsResults.isEmpty else { throw MockError.valueNotSet }
        try storeCountryDetailsResults.removeFirst().get()
    }
}

extension ModelContainer {

    static var mock: ModelContainer {
        try! appModelContainer(inMemoryOnly: true, isStub: false)
    }
}
```

## File: `UnitTests/Mocks/MockedInteractors.swift`
```
//
//  MockedInteractors.swift
//  UnitTests
//
//  Created by Alexey Naumov on 07.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

extension DIContainer.Interactors {
    static func mocked(
        countries: [MockedCountriesInteractor.Action] = [],
        images: [MockedImagesInteractor.Action] = [],
        permissions: [MockedUserPermissionsInteractor.Action] = []
    ) -> DIContainer.Interactors {
        self.init(
            images: MockedImagesInteractor(expected: images),
            countries: MockedCountriesInteractor(expected: countries),
            userPermissions: MockedUserPermissionsInteractor(expected: permissions))
    }
    
    func verify(sourceLocation: SourceLocation = #_sourceLocation) {
        (countries as? MockedCountriesInteractor)?
            .verify(sourceLocation: sourceLocation)
        (images as? MockedImagesInteractor)?
            .verify(sourceLocation: sourceLocation)
        (userPermissions as? MockedUserPermissionsInteractor)?
            .verify(sourceLocation: sourceLocation)
    }
}

// MARK: - CountriesInteractor

struct MockedCountriesInteractor: Mock, CountriesInteractor {
    
    enum Action: Equatable {
        case refreshCountriesList
        case loadCountryDetails(country: DBModel.Country, forceReload: Bool)
    }
    
    let actions: MockActions<Action>
    var detailsResponse: Result<DBModel.CountryDetails, Error> = .failure(MockError.valueNotSet)

    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }

    func refreshCountriesList() async throws {
        register(.refreshCountriesList)
    }

    func loadCountryDetails(country: DBModel.Country, forceReload: Bool) async throws -> DBModel.CountryDetails {
        register(.loadCountryDetails(country: country, forceReload: forceReload))
        return try detailsResponse.get()
    }
}

// MARK: - ImagesInteractor

struct MockedImagesInteractor: Mock, ImagesInteractor {
    
    enum Action: Equatable {
        case loadImage(URL?)
    }
    
    let actions: MockActions<Action>
    
    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }
    
    func load(image: LoadableSubject<UIImage>, url: URL?) {
        register(.loadImage(url))
    }
}

// MARK: - ImagesInteractor

final class MockedUserPermissionsInteractor: Mock, UserPermissionsInteractor {
    
    enum Action: Equatable {
        case resolveStatus(Permission)
        case request(Permission)
    }
    
    let actions: MockActions<Action>
    
    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }
    
    func resolveStatus(for permission: Permission) {
        register(.resolveStatus(permission))
    }
    
    func request(permission: Permission) {
        register(.request(permission))
    }
}
```

## File: `UnitTests/Mocks/MockedSystemEventsHandler.swift`
```
//
//  MockedSystemEventsHandler.swift
//  UnitTests
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Foundation
import UIKit
@testable import CountriesSwiftUI

// MARK: - SystemEventsHandler

final class MockedSystemEventsHandler: Mock, SystemEventsHandler {
    
    enum Action: Equatable {
        case openURL
        case becomeActive
        case resignActive
        case pushRegistration
        case recevieRemoteNotification
    }
    var actions = MockActions<Action>(expected: [])
    
    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }
    
    func sceneOpenURLContexts(_ urlContexts: Set<UIOpenURLContext>) {
        register(.openURL)
    }
    
    func sceneDidBecomeActive() {
        register(.becomeActive)
    }
    
    func sceneWillResignActive() {
        register(.resignActive)
    }
    
    func handlePushRegistration(result: Result<Data, Error>) {
        register(.pushRegistration)
    }

    func appDidReceiveRemoteNotification(payload: [AnyHashable: Any]) async -> UIBackgroundFetchResult {
        register(.recevieRemoteNotification)
        return .noData
    }
}

// MARK: - PushNotificationsHandler

final class DummyPushNotificationsHandler: PushNotificationsHandler { }

// MARK: - DeepLinksHandler

final class MockedDeepLinksHandler: Mock, DeepLinksHandler {
    enum Action: Equatable {
        case open(DeepLink)
    }
    var actions = MockActions<Action>(expected: [])
    
    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }
    
    func open(deepLink: DeepLink) {
        register(.open(deepLink))
    }
}
```

## File: `UnitTests/Mocks/MockedSystemPermissions.swift`
```
//
//  MockedSystemPermissions.swift
//  CountriesSwiftUI
//
//  Created by Alexey on 22/11/24.
//  Copyright © 2024 Alexey Naumov. All rights reserved.
//

import Foundation
import UserNotifications
@testable import CountriesSwiftUI

final class MockedSystemPushNotifications: Mock, SystemNotificationsCenter {
    enum Action: Equatable {
        case currentSettings
        case requestAuthorization(UNAuthorizationOptions)
    }
    struct NotificationSettings: SystemNotificationsSettings {
        var authorizationStatus: UNAuthorizationStatus
    }
    var actions = MockActions<Action>(expected: [])
    var getResponses: [NotificationSettings] = []
    var requestResponses: [Result<Bool, Error>] = []

    init(expected: [Action]) {
        self.actions = .init(expected: expected)
    }

    func currentSettings() async -> any SystemNotificationsSettings {
        register(.currentSettings)
        guard !getResponses.isEmpty else {
            return NotificationSettings(authorizationStatus: .notDetermined)
        }
        return getResponses.removeFirst()
    }

    func requestAuthorization(options: UNAuthorizationOptions) async throws -> Bool {
        register(.requestAuthorization(options))
        guard !requestResponses.isEmpty else { throw MockError.valueNotSet }
        return try requestResponses.removeFirst().get()
    }
}
```

## File: `UnitTests/Mocks/MockedWebRepositories.swift`
```
//
//  MockedWebRepositories.swift
//  UnitTests
//
//  Created by Alexey Naumov on 31.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation
import UIKit.UIImage
@testable import CountriesSwiftUI

class TestWebRepository: WebRepository {
    let session: URLSession = .mockedResponsesOnly
    let baseURL = "https://test.com"
}

// MARK: - CountriesWebRepository

final class MockedCountriesWebRepository: TestWebRepository, Mock, CountriesWebRepository {
    
    enum Action: Equatable {
        case countries
        case details(country: DBModel.Country)
    }
    var actions = MockActions<Action>(expected: [])
    
    var countriesResponses: [Result<[ApiModel.Country], Error>] = []
    var detailsResponses: [Result<ApiModel.CountryDetails, Error>] = []

    func countries() async throws -> [ApiModel.Country] {
        register(.countries)
        guard !countriesResponses.isEmpty else { throw MockError.valueNotSet }
        return try countriesResponses.removeFirst().get()
    }

    func details(country: DBModel.Country) async throws -> ApiModel.CountryDetails {
        register(.details(country: country))
        guard !detailsResponses.isEmpty else { throw MockError.valueNotSet }
        return try detailsResponses.removeFirst().get()
    }
}

// MARK: - ImageWebRepository

final class MockedImageWebRepository: TestWebRepository, Mock, ImagesWebRepository {

    enum Action: Equatable {
        case loadImage(URL)
    }
    var actions = MockActions<Action>(expected: [])
    
    var imageResponses: [Result<UIImage, Error>] = []

    func loadImage(url: URL) async throws -> UIImage {
        register(.loadImage(url))
        guard !imageResponses.isEmpty else { throw MockError.valueNotSet }
        return try imageResponses.removeFirst().get()
    }
}

// MARK: - PushTokenWebRepository

final class MockedPushTokenWebRepository: TestWebRepository, Mock, PushTokenWebRepository {
    enum Action: Equatable {
        case register(Data)
    }
    let actions: MockActions<Action>

    init(expected: [Action]) {
        self.actions = MockActions<Action>(expected: expected)
    }
    
    func register(devicePushToken: Data) async throws {
        register(.register(devicePushToken))
    }
}
```

## File: `UnitTests/Mocks/Interactors/CountriesInteractorTests.swift`
```
//
//  CountriesInteractorTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 31.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftUI
@testable import CountriesSwiftUI

@MainActor
@Suite class CountriesInteractorTests {

    let mockedWebRepo: MockedCountriesWebRepository
    let mockedDBRepo: MockedCountriesDBRepository
    let sut: RealCountriesInteractor

    init() {
        mockedWebRepo = MockedCountriesWebRepository()
        mockedDBRepo = MockedCountriesDBRepository()
        sut = RealCountriesInteractor(webRepository: mockedWebRepo,
                                      dbRepository: mockedDBRepo)
    }
}

// MARK: - refreshCountriesList()

final class RefreshCountriesListTests: CountriesInteractorTests {

    @Test func happyPath() async throws {
        let countries = ApiModel.Country.mockedData
        mockedWebRepo.actions = .init(expected: [
            .countries
        ])
        mockedWebRepo.countriesResponses = [.success(countries)]
        mockedDBRepo.actions = .init(expected: [
            .storeCountries(countries)
        ])
        mockedDBRepo.storeCountriesResults = [.success(())]
        try await sut.refreshCountriesList()
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func dbFailure() async throws {
        let countries = ApiModel.Country.mockedData
        mockedWebRepo.actions = .init(expected: [
            .countries
        ])
        mockedWebRepo.countriesResponses = [.success(countries)]
        mockedDBRepo.actions = .init(expected: [
            .storeCountries(countries)
        ])
        let error = NSError.test
        mockedDBRepo.storeCountriesResults = [.failure(error)]
        await #expect(throws: error) {
            try await sut.refreshCountriesList()
        }
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func webFailure() async throws {
        mockedWebRepo.actions = .init(expected: [
            .countries
        ])
        let error = NSError.test
        mockedWebRepo.countriesResponses = [.failure(error)]
        mockedDBRepo.actions = .init(expected: [])
        await #expect(throws: error) {
            try await sut.refreshCountriesList()
        }
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }
}

// MARK: - loadCountryDetails(country: DBModel.Country, forceReload: Bool)

final class LoadCountryDetailsTests: CountriesInteractorTests {

    @Test func happyPathCachedData() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [])
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
        ])
        let dbDetails = DBModel.CountryDetails(
            alpha3Code: country.alpha3Code,
            capital: details.capital,
            currencies: details.currencies.map({ $0.dbModel() }),
            neighbors: [])
        mockedDBRepo.countryDetailsResults = [
            .success(dbDetails)
        ]
        let result = try await sut.loadCountryDetails(country: country, forceReload: false)
        #expect(result == dbDetails)
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func happyPathCachedDataForceReload() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.success(details)]
        mockedDBRepo.actions = .init(expected: [
            .storeDetails(details, country: country),
            .fetchCountryDetails(country),
        ])
        let dbDetails = DBModel.CountryDetails(
            alpha3Code: country.alpha3Code,
            capital: details.capital,
            currencies: details.currencies.map({ $0.dbModel() }),
            neighbors: [])
        mockedDBRepo.countryDetailsResults = [
            .success(dbDetails)
        ]
        mockedDBRepo.storeCountryDetailsResults = [.success(())]
        let result = try await sut.loadCountryDetails(country: country, forceReload: true)
        #expect(result == dbDetails)
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func happyPathNoCache() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.success(details)]
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
            .storeDetails(details, country: country),
            .fetchCountryDetails(country),
        ])
        let dbDetails = DBModel.CountryDetails(
            alpha3Code: country.alpha3Code,
            capital: details.capital,
            currencies: details.currencies.map({ $0.dbModel() }),
            neighbors: [])
        mockedDBRepo.countryDetailsResults = [
            .success(nil),
            .success(dbDetails)
        ]
        mockedDBRepo.storeCountryDetailsResults = [.success(())]
        let result = try await sut.loadCountryDetails(country: country, forceReload: false)
        #expect(result == dbDetails)
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func cacheDBFailure() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.success(details)]
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
            .storeDetails(details, country: country),
            .fetchCountryDetails(country),
        ])
        let dbDetails = DBModel.CountryDetails(
            alpha3Code: country.alpha3Code,
            capital: details.capital,
            currencies: details.currencies.map({ $0.dbModel() }),
            neighbors: [])
        mockedDBRepo.countryDetailsResults = [
            .failure(NSError.test),
            .success(dbDetails)
        ]
        mockedDBRepo.storeCountryDetailsResults = [.success(())]
        let result = try await sut.loadCountryDetails(country: country, forceReload: false)
        #expect(result == dbDetails)
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func fetchAfterStoringDBFailure() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.success(details)]
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
            .storeDetails(details, country: country),
            .fetchCountryDetails(country),
        ])
        let error = NSError.test
        mockedDBRepo.countryDetailsResults = [
            .success(nil),
            .failure(error)
        ]
        mockedDBRepo.storeCountryDetailsResults = [.success(())]
        await #expect(throws: ValueIsMissingError.self) {
            try await sut.loadCountryDetails(country: country, forceReload: false)
        }
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func storingDBFailure() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.success(details)]
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
            .storeDetails(details, country: country),
        ])
        let error = NSError.test
        mockedDBRepo.countryDetailsResults = [.success(nil)]
        mockedDBRepo.storeCountryDetailsResults = [.failure(error)]
        await #expect(throws: error) {
            try await sut.loadCountryDetails(country: country, forceReload: false)
        }
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }

    @Test func webFailure() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let error = NSError.test
        mockedWebRepo.actions = .init(expected: [
            .details(country: country),
        ])
        mockedWebRepo.detailsResponses = [.failure(error)]
        mockedDBRepo.actions = .init(expected: [
            .fetchCountryDetails(country),
        ])
        mockedDBRepo.countryDetailsResults = [.success(nil)]
        await #expect(throws: error) {
            try await sut.loadCountryDetails(country: country, forceReload: false)
        }
        mockedWebRepo.verify()
        mockedDBRepo.verify()
    }
}

final class StubCountriesInteractorTests: CountriesInteractorTests {

    @Test func stubInteractor() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let sut = StubCountriesInteractor()
        try await sut.refreshCountriesList()
        await #expect(throws: ValueIsMissingError.self) {
            try await sut.loadCountryDetails(country: country, forceReload: false)
        }
    }
}
```

## File: `UnitTests/Mocks/Interactors/ImagesInteractorTests.swift`
```
//
//  ImagesInteractorTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 10.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import UIKit
import Combine
@testable import CountriesSwiftUI

@Suite struct ImagesInteractorTests {

    let sut: RealImagesInteractor
    let mockedWebRepository: MockedImageWebRepository
    let testImageURL = URL(string: "https://test.com/test.png")!
    let testImage = UIColor.red.image(CGSize(width: 40, height: 40))
    
    init() {
        mockedWebRepository = MockedImageWebRepository()
        sut = RealImagesInteractor(webRepository: mockedWebRepository)
    }
    
    func expectRepoActions(_ actions: [MockedImageWebRepository.Action]) {
        mockedWebRepository.actions = .init(expected: actions)
    }
    
    func verifyRepoActions(sourceLocation: SourceLocation = #_sourceLocation) {
        mockedWebRepository.verify(sourceLocation: sourceLocation)
    }
    
    @Test func loadImageNilURL() async throws {
        let state = BindingWithHistory(value: Loadable<UIImage>.notRequested)
        expectRepoActions([])
        sut.load(image: state.binding, url: nil)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.history == [.notRequested, .notRequested])
        verifyRepoActions()
    }
    
    @Test func loadImageLoadedFromWeb() async throws {
        let state = BindingWithHistory(value: Loadable<UIImage>.notRequested)
        mockedWebRepository.imageResponses = [.success(testImage)]
        expectRepoActions([.loadImage(testImageURL)])
        sut.load(image: state.binding, url: testImageURL)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.history == [
            .notRequested,
            .isLoading(last: nil, cancelBag: .test),
            .loaded(testImage)
        ])
        verifyRepoActions()
    }
    
    @Test func loadImageFailed() async throws {
        let state = BindingWithHistory(value: Loadable<UIImage>.notRequested)
        let error = NSError.test
        mockedWebRepository.imageResponses = [.failure(error)]
        expectRepoActions([.loadImage(testImageURL)])
        sut.load(image: state.binding, url: testImageURL)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.history == [
            .notRequested,
            .isLoading(last: nil, cancelBag: .test),
            .failed(error)
        ])
        verifyRepoActions()
    }
    
    @Test func loadImageHadLoadedImage() async throws {
        let state = BindingWithHistory(value: Loadable<UIImage>.loaded(testImage))
        let error = NSError.test
        mockedWebRepository.imageResponses = [.failure(error)]
        expectRepoActions([.loadImage(testImageURL)])
        sut.load(image: state.binding, url: testImageURL)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.history == [
            .loaded(self.testImage),
            .isLoading(last: self.testImage, cancelBag: .test),
            .failed(error)
        ])
        verifyRepoActions()
    }
    
    @Test func stubInteractor() async throws {
        let sut = StubImagesInteractor()
        let state = BindingWithHistory(value: Loadable<UIImage>.notRequested)
        sut.load(image: state.binding, url: testImageURL)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.history == [.notRequested])
        verifyRepoActions()
    }
}
```

## File: `UnitTests/Mocks/Interactors/UserPermissionsInteractorTests.swift`
```
//
//  UserPermissionsInteractorTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import Combine
import UserNotifications
@testable import CountriesSwiftUI

@Suite struct UserPermissionsInteractorTests {

    @Test func noSideEffectOnInit() async throws {
        let state = Store<AppState>(AppState())
        let notificationsCenter = MockedSystemPushNotifications(expected: [])
        let sut = makeSUT(state: state, notificationsCenter: notificationsCenter)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.value == AppState())
        notificationsCenter.verify()
        _ = sut
    }
    
    // MARK: - Push
    
    @Test func pushFirstResolveStatus() async throws {
        #expect(AppState().permissions.push == .unknown)
        let state = Store<AppState>(AppState())
        let notificationsCenter = MockedSystemPushNotifications(expected: [
            .currentSettings
        ])
        notificationsCenter.getResponses = [.init(authorizationStatus: .authorized)]
        let sut = makeSUT(state: state, notificationsCenter: notificationsCenter)
        sut.resolveStatus(for: .pushNotifications)
        try await SuspendingClock().sleep(for: .seconds(1))
        #expect(state.value.permissions.push == .granted)
        notificationsCenter.verify()
    }
    
    @Test func pushRequestPermissionGrant() async throws {
        let state = Store<AppState>(AppState())
        state[\.permissions.push] = .notRequested
        let notificationsCenter = MockedSystemPushNotifications(expected: [
            .requestAuthorization([.alert, .sound])
        ])
        notificationsCenter.requestResponses = [.success(true)]
        let sut = makeSUT(state: state, notificationsCenter: notificationsCenter)
        sut.request(permission: .pushNotifications)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.value.permissions.push == .granted)
        notificationsCenter.verify()
    }

    @Test func pushRequestPermissionDeny() async throws {
        let state = Store<AppState>(AppState())
        state[\.permissions.push] = .notRequested
        let notificationsCenter = MockedSystemPushNotifications(expected: [
            .requestAuthorization([.alert, .sound])
        ])
        notificationsCenter.requestResponses = [.failure(NSError.test)]
        let sut = makeSUT(state: state, notificationsCenter: notificationsCenter)
        sut.request(permission: .pushNotifications)
        try await SuspendingClock().sleep(for: .seconds(0.5))
        #expect(state.value.permissions.push == .denied)
        notificationsCenter.verify()
    }

    @Test func pushRequestPermissionDeniedBefore() async throws {
        let state = Store<AppState>(AppState())
        state[\.permissions.push] = .denied
        let exp = TestExpectation()
        let notificationsCenter = MockedSystemPushNotifications(expected: [])
        let sut = makeSUT(state: state, notificationsCenter: notificationsCenter) {
            #expect(state.value.permissions.push == .denied)
            exp.fulfill()
        }
        sut.request(permission: .pushNotifications)
        await exp.fulfillment()
        notificationsCenter.verify()
    }
    
    @Test func authorizationStatusMapping() {
        #expect(UNAuthorizationStatus.notDetermined.map == .notRequested)
        #expect(UNAuthorizationStatus.provisional.map == .notRequested)
        #expect(UNAuthorizationStatus.denied.map == .denied)
        #expect(UNAuthorizationStatus.authorized.map == .granted)
        #expect(UNAuthorizationStatus(rawValue: 10)?.map == .notRequested)
    }
    
    // MARK: - Stub
    
    @Test func stubUserPermissionsInteractor() {
        let sut = StubUserPermissionsInteractor()
        sut.request(permission: .pushNotifications)
        sut.resolveStatus(for: .pushNotifications)
    }

    private func makeSUT(state: Store<AppState>,
                         notificationsCenter: MockedSystemPushNotifications,
                         openAppSettings: (() -> Void)? = nil,
                         sourceLocation: SourceLocation = #_sourceLocation
    ) -> RealUserPermissionsInteractor {
        RealUserPermissionsInteractor(
            appState: state, notificationCenter: notificationsCenter) {
                if let openAppSettings {
                    openAppSettings()
                } else {
                    Issue.record("openAppSettings callback not expected", sourceLocation: sourceLocation)
                }
            }
    }
}
```

## File: `UnitTests/Mocks/NetworkMocking/MockedResponse.swift`
```
//
//  MockedResponse.swift
//  UnitTests
//
//  Created by Alexey Naumov on 30.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation
@testable import CountriesSwiftUI

extension RequestMocking {
    struct MockedResponse {
        let url: URL
        let result: Result<Data, Swift.Error>
        let httpCode: HTTPCode
        let headers: [String: String]
        let loadingTime: TimeInterval
        let customResponse: URLResponse?
    }
}

extension RequestMocking.MockedResponse {
    enum Error: Swift.Error {
        case notMockedRequest(URLRequest)
        case responseFactoryFailure
        case mockInitializationFailure
    }
    
    init<T>(apiCall: APICall, baseURL: String,
            result: Result<T, Swift.Error>,
            httpCode: HTTPCode = 200,
            headers: [String: String] = ["Content-Type": "application/json"],
            loadingTime: TimeInterval = 0.1
    ) throws where T: Encodable {
        guard let url = try apiCall.urlRequest(baseURL: baseURL).url
        else { throw Error.mockInitializationFailure }
        self.url = url
        switch result {
        case let .success(value):
            self.result = .success(try JSONEncoder().encode(value))
        case let .failure(error):
            self.result = .failure(error)
        }
        self.httpCode = httpCode
        self.headers = headers
        self.loadingTime = loadingTime
        customResponse = nil
    }
    
    init(apiCall: APICall, baseURL: String, customResponse: URLResponse) throws {
        guard let url = try apiCall.urlRequest(baseURL: baseURL).url
        else { throw Error.mockInitializationFailure }
        self.url = url
        result = .success(Data())
        httpCode = 200
        headers = [String: String]()
        loadingTime = 0
        self.customResponse = customResponse
    }
    
    init(url: URL, result: Result<Data, Swift.Error>) {
        self.url = url
        self.result = result
        httpCode = 200
        headers = [String: String]()
        loadingTime = 0
        customResponse = nil
    }
}
```

## File: `UnitTests/Mocks/NetworkMocking/RequestMocking.swift`
```
//
//  RequestMocking.swift
//  CountriesSwiftUI
//
//  Created by Alexey Naumov on 30.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation

extension URLSession {
    static var mockedResponsesOnly: URLSession {
        let configuration = URLSessionConfiguration.default
        configuration.protocolClasses = [RequestMocking.self, RequestBlocking.self]
        configuration.timeoutIntervalForRequest = 1
        configuration.timeoutIntervalForResource = 1
        return URLSession(configuration: configuration)
    }
}

extension RequestMocking {
    private final class MocksContainer: @unchecked Sendable {
        var mocks: [MockedResponse] = []
    }
    static private let container = MocksContainer()
    static private let lock = NSLock()

    static func add(mock: MockedResponse) {
        lock.withLock {
            container.mocks.append(mock)
        }
    }
    
    static func removeAllMocks() {
        lock.withLock {
            container.mocks.removeAll()
        }
    }
    
    static private func mock(for request: URLRequest) -> MockedResponse? {
        return lock.withLock {
            container.mocks.first { $0.url == request.url }
        }
    }
}

// MARK: - RequestMocking

final class RequestMocking: URLProtocol {

    override class func canInit(with request: URLRequest) -> Bool {
        return mock(for: request) != nil
    }

    override class func canonicalRequest(for request: URLRequest) -> URLRequest {
        return request
    }
    
    // swiftlint:disable identifier_name
    override class func requestIsCacheEquivalent(_ a: URLRequest, to b: URLRequest) -> Bool {
    // swiftlint:enable identifier_name
        return false
    }

    override func startLoading() {
        if let mock = RequestMocking.mock(for: request),
            let url = request.url,
            let response = mock.customResponse ??
                HTTPURLResponse(url: url,
                statusCode: mock.httpCode,
                httpVersion: "HTTP/1.1",
                headerFields: mock.headers) {
            DispatchQueue.main.asyncAfter(deadline: .now() + mock.loadingTime) { [weak self] in
                guard let self else { return }
                self.client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)
                switch mock.result {
                case let .success(data):
                    self.client?.urlProtocol(self, didLoad: data)
                    self.client?.urlProtocolDidFinishLoading(self)
                case let .failure(error):
                    self.client?.urlProtocol(self, didFailWithError: error)
                }
            }
        }
    }

    override func stopLoading() { }
}

// MARK: - RequestBlocking

private class RequestBlocking: URLProtocol {
    enum Error: Swift.Error {
        case requestBlocked
    }
    
    override class func canInit(with request: URLRequest) -> Bool {
        return true
    }

    override class func canonicalRequest(for request: URLRequest) -> URLRequest {
        return request
    }

    override func startLoading() {
        DispatchQueue(label: "").async {
            self.client?.urlProtocol(self, didFailWithError: Error.requestBlocked)
        }
    }
    override func stopLoading() { }
}
```

## File: `UnitTests/Repositories/CountriesDBRepositoryTests.swift`
```
//
//  CountriesDBRepositoryTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 19.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftData
@testable import CountriesSwiftUI

@MainActor
@Suite struct CountriesDBRepositoryTests {

    let container: ModelContainer
    let sut: CountriesDBRepository

    init() {
        container = .mock
        sut = MainDBRepository(modelContainer: container)
    }

    @Test func storeCountries() async throws {
        let countries = ApiModel.Country.mockedData
        try await sut.store(countries: countries)
        let results = try container.mainContext
            .fetch(FetchDescriptor<DBModel.Country>())
        #expect(results.count == countries.count)
    }

    @Test func storeCountryDetails() async throws {
        let country = ApiModel.Country.mockedData[0]
        let details = ApiModel.CountryDetails.mockedData[0]
        try await sut.store(countryDetails: details, for: country.dbModel())
        let results = try container.mainContext
            .fetch(FetchDescriptor<DBModel.CountryDetails>())
        let stored = try #require(results.first)
        #expect(stored.capital == details.capital)
        #expect(stored.currencies.count == details.currencies.count)
    }

    @Test func countryDetailsForCountry() async throws {
        let country = ApiModel.Country.mockedData[0].dbModel()
        let details = ApiModel.CountryDetails.mockedData[0]
        try await sut.store(countryDetails: details, for: country)
        let stored = try #require(try await sut.countryDetails(for: country))
        #expect(stored.capital == details.capital)
        #expect(stored.currencies.count == details.currencies.count)
    }
}

```

## File: `UnitTests/Repositories/CountriesWebRepositoryTests.swift`
```
//
//  CountriesWebRepositoryTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 30.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
@testable import CountriesSwiftUI

@Suite(.serialized) final class CountriesWebRepositoryTests {

    private let sut = RealCountriesWebRepository(session: .mockedResponsesOnly)

    typealias API = RealCountriesWebRepository.API
    typealias Mock = RequestMocking.MockedResponse

    deinit {
        RequestMocking.removeAllMocks()
    }

    // MARK: - All Countries

    @Test func allCountriesSuccess() async throws {
        let data = await ApiModel.Country.mockedData
        try mock(.allCountries, result: .success(data))
        let response = try await sut.countries()
        #expect(response == data)
    }

    @Test func countryDetailsSuccess() async throws {
        let countries = await ApiModel.Country.mockedData
        let value = ApiModel.CountryDetails(
            capital: "London",
            currencies: [ApiModel.Currency(code: "12", symbol: "$", name: "US dollar")],
            borders: countries.map({ $0.alpha3Code }))
        let country = countries[0]
        try mock(.countryDetails(countryName: country.name), result: .success([value]))
        let response = try await sut.details(country: country.dbModel())
        #expect(response == value)
    }

    @Test func countryDetailsWhenDetailsAreEmpty() async throws {
        let countries = await ApiModel.Country.mockedData
        let country = countries[0]
        try mock(.countryDetails(countryName: country.name), result: .success([ApiModel.CountryDetails]()))
        await #expect(throws: APIError.unexpectedResponse) {
            try await sut.details(country: country.dbModel())
        }
    }

    // MARK: - Helper

    private func mock<T>(_ apiCall: API, result: Result<T, Swift.Error>,
                         httpCode: HTTPCode = 200) throws where T: Encodable {
        let mock = try Mock(apiCall: apiCall, baseURL: sut.baseURL, result: result, httpCode: httpCode)
        RequestMocking.add(mock: mock)
    }
}

```

## File: `UnitTests/Repositories/ImageWebRepositoryTests.swift`
```
//
//  ImageWebRepositoryTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 09.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import UIKit.UIImage
@testable import CountriesSwiftUI

@Suite(.serialized) final class ImageWebRepositoryTests {

    private let sut = RealImagesWebRepository(session: .mockedResponsesOnly)
    private let testImage = UIColor.red.image(CGSize(width: 40, height: 40))

    typealias Mock = RequestMocking.MockedResponse

    deinit {
        RequestMocking.removeAllMocks()
    }

    @Test func loadImageSuccess() async throws {
        let imageURL = try #require(URL(string: "https://image.service.com/myimage.png"))
        let imageRef = try #require(testImage.pngData())
        let mock = Mock(url: imageURL, result: .success(imageRef))
        RequestMocking.add(mock: mock)

        let result = try await sut.loadImage(url: imageURL)
        #expect(result.size == testImage.size)
    }

    @Test func loadImageFailure() async throws {
        let imageURL = try #require(URL(string: "https://image.service.com/myimage.png"))
        let errorRef = NSError.test
        let mock = Mock(url: imageURL, result: .failure(errorRef))
        RequestMocking.add(mock: mock)

        do {
            _ = try await sut.loadImage(url: imageURL)
            Issue.record("Above should throw")
        } catch {
            let nsError = error as NSError
            #expect(nsError.domain == errorRef.domain)
            #expect(nsError.code == errorRef.code)
        }
    }
}

```

## File: `UnitTests/Repositories/PushTokenWebRepositoryTests.swift`
```
//
//  PushTokenWebRepositoryTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import Foundation
@testable import CountriesSwiftUI

@Suite struct PushTokenWebRepositoryTests {

    private let sut = RealPushTokenWebRepository(session: .mockedResponsesOnly)

    @Test func register() async throws {
        try await sut.register(devicePushToken: Data())
    }
}

```

## File: `UnitTests/Repositories/WebRepositoryTests.swift`
```
//
//  WebRepositoryTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 30.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import Combine
import Foundation
@testable import CountriesSwiftUI

@Suite(.serialized) final class WebRepositoryTests {

    private let sut = TestWebRepository()

    private typealias API = TestWebRepository.API
    typealias Mock = RequestMocking.MockedResponse

    deinit {
        RequestMocking.removeAllMocks()
    }

    @Test func loadSuccess() async throws {
        let data = TestWebRepository.TestData()
        try mock(.test, result: .success(data))
        let result = try await sut.load(.test)
        #expect(result == data)
    }

    @Test func loadParseError() async throws {
        let data = await ApiModel.Country.mockedData
        try mock(.test, result: .success(data))
        await #expect(throws: APIError.unexpectedResponse) {
            try await sut.load(.test)
        }
    }

    @Test func loadHttpCodeFailure() async throws {
        let data = TestWebRepository.TestData()
        try mock(.test, result: .success(data), httpCode: 500)
        await #expect(throws: APIError.httpCode(500)) {
            try await sut.load(.test)
        }
    }

    @Test func loadNetworkingError() async throws {
        let errorRef = NSError.test
        try mock(.test, result: Result<TestWebRepository.TestData, Error>.failure(errorRef))
        do {
            _ = try await sut.load(.test)
            Issue.record("Above should throw")
        } catch {
            let nsError = error as NSError
            #expect(nsError.domain == errorRef.domain)
            #expect(nsError.code == errorRef.code)
        }
    }

    @Test func loadRequestURLError() async {
        await #expect(throws: APIError.invalidURL) {
            try await sut.load(.urlError)
        }
    }

    @Test func loadRequestBodyError() async {
        await #expect(throws: TestWebRepository.APIError.fail) {
            try await sut.load(.bodyError)
        }
    }

    @Test func loadLoadableError() async {
        await #expect(throws: APIError.invalidURL) {
            try await sut.load(.urlError)
        }
    }

    @Test func loadNoHttpCodeError() async throws {
        let response = URLResponse(url: URL(fileURLWithPath: ""),
                                   mimeType: "example", expectedContentLength: 0, textEncodingName: nil)
        let mock = try Mock(apiCall: API.test, baseURL: sut.baseURL, customResponse: response)
        RequestMocking.add(mock: mock)
        await #expect(throws: APIError.unexpectedResponse) {
            try await sut.load(.test)
        }
    }

    // MARK: - Helper

    private func mock<T>(_ apiCall: API, result: Result<T, Swift.Error>,
                         httpCode: HTTPCode = 200) throws where T: Encodable {
        let mock = try Mock(apiCall: apiCall, baseURL: sut.baseURL, result: result, httpCode: httpCode)
        RequestMocking.add(mock: mock)
    }
}

private extension TestWebRepository {
    func load(_ api: API) async throws -> TestData {
        try await call(endpoint: api)
    }
}

extension TestWebRepository {
    enum API: APICall {

        case test
        case urlError
        case bodyError
        case noHttpCodeError

        var path: String {
            if self == .urlError {
                return "\\"
            }
            return "/test/path"
        }
        var method: String { "POST" }
        var headers: [String: String]? { nil }
        func body() throws -> Data? {
            if self == .bodyError { throw APIError.fail }
            return nil
        }
    }
}

extension TestWebRepository {
    enum APIError: Swift.Error, LocalizedError {
        case fail
        var errorDescription: String? { "fail" }
    }
}

extension TestWebRepository {
    struct TestData: Codable, Equatable {
        let string: String
        let integer: Int

        init() {
            string = "some string"
            integer = 42
        }
    }
}

```

## File: `UnitTests/System/DeepLinksHandlerTests.swift`
```
//
//  DeepLinksHandlerTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
@testable import CountriesSwiftUI

@MainActor
@Suite struct DeepLinksHandlerTests {

    @Test func noSideEffectOnInit() {
        let interactors: DIContainer.Interactors = .mocked()
        let container = DIContainer(appState: AppState(), interactors: interactors)
        _ = RealDeepLinksHandler(container: container)
        interactors.verify()
        #expect(container.appState.value == AppState())
    }

    @Test func openingDeeplinkFromDefaultRouting() {
        let interactors: DIContainer.Interactors = .mocked()
        let initialState = AppState()
        let container = DIContainer(appState: initialState, interactors: interactors)
        let sut = RealDeepLinksHandler(container: container)
        sut.open(deepLink: .showCountryFlag(alpha3Code: "ITA"))
        #expect(initialState.routing.countriesList.countryCode == nil)
        #expect(!initialState.routing.countryDetails.detailsSheet)
        var expectedState = AppState()
        expectedState.routing.countriesList.countryCode = "ITA"
        expectedState.routing.countryDetails.detailsSheet = true
        interactors.verify()
        #expect(container.appState.value == expectedState)
    }

    @Test func openingDeeplinkFromNonDefaultRouting() async throws {
        let interactors: DIContainer.Interactors = .mocked()
        var initialState = AppState()
        initialState.routing.countriesList.countryCode = "FRA"
        initialState.routing.countryDetails.detailsSheet = true
        let container = DIContainer(appState: initialState, interactors: interactors)
        let sut = RealDeepLinksHandler(container: container)
        sut.open(deepLink: .showCountryFlag(alpha3Code: "ITA"))

        let resettedState = AppState()
        var finalState = AppState()
        finalState.routing.countriesList.countryCode = "ITA"
        finalState.routing.countryDetails.detailsSheet = true

        #expect(container.appState.value == resettedState)
        try await Task.sleep(nanoseconds: 10_000_000)
        interactors.verify()
        #expect(container.appState.value == finalState)
    }
}

```

## File: `UnitTests/System/PushNotificationsHandlerTests.swift`
```
//
//  PushNotificationsHandlerTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 26.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import UserNotifications
@testable import CountriesSwiftUI

@MainActor
@Suite struct PushNotificationsHandlerTests {

    @Test func isCenterDelegate() {
        let mockedHandler = MockedDeepLinksHandler(expected: [])
        let sut = RealPushNotificationsHandler(deepLinksHandler: mockedHandler)
        let center = UNUserNotificationCenter.current()
        #expect(center.delegate === sut)
        mockedHandler.verify()
    }

    @Test func emptyPayload() async throws {
        let mockedHandler = MockedDeepLinksHandler(expected: [])
        let sut = RealPushNotificationsHandler(deepLinksHandler: mockedHandler)
        let exp = TestExpectation()
        sut.handleNotification(userInfo: [:]) {
            mockedHandler.verify()
            exp.fulfill()
        }
        await exp.fulfillment()
    }
    
    @Test func deepLinkPayload() async throws {
        let mockedHandler = MockedDeepLinksHandler(expected: [
            .open(.showCountryFlag(alpha3Code: "USA"))
        ])
        let sut = RealPushNotificationsHandler(deepLinksHandler: mockedHandler)
        let exp = TestExpectation()
        let userInfo: [String: Any] = [
            "aps": ["country": "USA"]
        ]
        sut.handleNotification(userInfo: userInfo) {
            mockedHandler.verify()
            exp.fulfill()
        }
        await exp.fulfillment()
    }
}
```

## File: `UnitTests/UI/CountriesListTests.swift`
```
//
//  CountriesListTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 01.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import ViewInspector
import SwiftData
import SwiftUI
@testable import CountriesSwiftUI

@MainActor
@Suite struct CountriesListTests {

    let apiCountries: [ApiModel.Country]
    let dbCountries: [DBModel.Country]

    init() {
        apiCountries = ApiModel.Country.mockedData
        dbCountries = apiCountries.map { $0.dbModel() }
    }

    @Test func noCachedCountries() async throws {
        let container = DIContainer(interactors: .mocked(countries: [
            .refreshCountriesList,
        ]))
        let sut = CountriesList(state: .notRequested)
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }

    @Test func cachedCountries() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .notRequested)
        let modelContainer = ModelContainer.mock
        let dbRepository = MainDBRepository(modelContainer: modelContainer)
        try await dbRepository.store(countries: apiCountries)
        let view = sut.inject(container).modelContainer(modelContainer)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { view in
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }

    @Test func noMatchesWhenSearching() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .loaded(()))
        let modelContainer = ModelContainer.mock
        let dbRepository = MainDBRepository(modelContainer: modelContainer)
        try await dbRepository.store(countries: apiCountries)
        let view = sut.inject(container).modelContainer(modelContainer)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { view in
                try view.actualView().searchText = "whatever"
            }
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(text: "No matches found") }
                container.interactors.verify()
            }
        }
    }

    @Test func listRefresh() async throws {
        let container = DIContainer(interactors: .mocked(countries: [
            .refreshCountriesList
        ]))
        let sut = CountriesList(state: .loaded(()))
        let modelContainer = ModelContainer.mock
        let dbRepository = MainDBRepository(modelContainer: modelContainer)
        try await dbRepository.store(countries: apiCountries)
        let view = sut.inject(container).modelContainer(modelContainer)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { view in
                let list = try view.find(ViewType.List.self)
                try await list.callRefreshable()
                container.interactors.verify()
            }
        }
    }

    @Test func countriesIsLoadingInitial() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .isLoading(last: nil, cancelBag: .test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                let content = try view.content()
                #expect(throws: Never.self) { try content.find(ViewType.ProgressView.self) }
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }

    @Test func countriesLoaded() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .loaded(()))
        let modelContainer = ModelContainer.mock
        let dbRepository = MainDBRepository(modelContainer: modelContainer)
        try await dbRepository.store(countries: apiCountries)
        let view = sut.inject(container).modelContainer(modelContainer)
        let firstRowCountry = try #require(dbCountries.sorted(by: { $0.name < $1.name }).first)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { view in
                let content = try view.content()
                #expect(throws: (any Error).self) { try content.find(ViewType.ProgressView.self) }
                let cell = try content.find(CountryCell.self).actualView()
                #expect(cell.country.name == firstRowCountry.name)
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }
    
    @Test func countriesFailed() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .failed(NSError.test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.content().implicitAnyView().implicitAnyView().implicitAnyView().view(ErrorView.self, 0) }
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }
    
    @Test func countriesFailedRetry() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = CountriesList(state: .failed(NSError.test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                let errorView = try view.content().implicitAnyView().implicitAnyView().implicitAnyView().view(ErrorView.self, 0)
                try errorView.implicitAnyView().vStack().button(2).tap()
                #expect(container.appState.value == AppState())
                container.interactors.verify()
            }
        }
    }

    @Test func requestPush() async throws {
        let container = DIContainer(interactors: .mocked(permissions: [
            .request(.pushNotifications)
        ]))
        container.appState[\.permissions.push] = .notRequested
        let sut = CountriesList(state: .loaded(()))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                try view.find(button: "Allow Push").tap()
                container.interactors.verify()
            }
        }
    }
}

@Suite struct LocalizationTests {

    @Test func countryLocalizedName() {
        let sut = DBModel.Country(name: "Abc", translations: ["fr": "Xyz"], population: 0, flag: nil, alpha3Code: "")
        let locale = Locale(identifier: "fr")
        #expect(sut.name(locale: locale) == "Xyz")
    }
}

// MARK: - CountriesList inspection helper

extension InspectableView where View == ViewType.View<CountriesList> {
    func content() throws -> InspectableView<ViewType.NavigationStack> {
        return try implicitAnyView().navigationStack()
    }
}
```

## File: `UnitTests/UI/DeepLinkUITests.swift`
```
//
//  DeepLinkUITests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 10.01.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftData
import ViewInspector
import UIKit.UIColor
@testable import CountriesSwiftUI

@MainActor
@Suite struct DeepLinkUITests {

    @Test func countriesListSelectsCountry() async throws {
        let store = appStateWithDeepLink()
        let interactors = interactorsWithMockedRepos(store: store)
        let modelContainer = ModelContainer.mock
        let dbRepository = MainDBRepository(modelContainer: modelContainer)
        let countries = ApiModel.Country.mockedData
        try await dbRepository.store(countries: countries)
        let container = DIContainer(appState: store, interactors: interactors)
        let sut = CountriesList()
        let view = sut.inject(container).modelContainer(modelContainer)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { view in
                let actualView = try view.actualView()
                #expect(!actualView.navigationPath.isEmpty)
            }
        }
    }
    
    @Test func countryDetailsPresentsSheet() async throws {
        let store = appStateWithDeepLink()
        let interactors = interactorsWithMockedRepos(store: store)
        let container = DIContainer(appState: store, interactors: interactors)
        let country = ApiModel.Country.mockedData[0].dbModel()
        country.flag = URL(string: "https://sample.com")
        let countryDetails = DBModel.CountryDetails(alpha3Code: country.alpha3Code, capital: "Rome", currencies: [], neighbors: [])
        let sut = CountryDetails(country: country, details: .loaded(countryDetails))
        let view = sut.inject(container)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect(after: .seconds(0.5)) { view in
                #expect(throws: Never.self) { try view.find(ModalFlagView.self) }
                #expect(store.value.routing.countryDetails.detailsSheet)
            }
        }
    }
}

// MARK: - Setup

@MainActor
private extension DeepLinkUITests {
    
    func appStateWithDeepLink() -> Store<AppState> {
        let countries = ApiModel.Country.mockedData
        var appState = AppState()
        appState.routing.countriesList.countryCode = countries[0].alpha3Code
        appState.routing.countryDetails.detailsSheet = true
        return Store(appState)
    }
    
    func interactorsWithMockedRepos(store: Store<AppState>) -> DIContainer.Interactors {

        let countries = ApiModel.Country.mockedData
        let testImage = UIColor.red.image(CGSize(width: 40, height: 40))
        let detailsIntermediate = ApiModel.CountryDetails(capital: "", currencies: [], borders: [])
        let details = DBModel.CountryDetails(alpha3Code: "", capital: "", currencies: [], neighbors: [])

        let countriesDBRepo = MockedCountriesDBRepository()
        let countriesWebRepo = MockedCountriesWebRepository()
        let imagesRepo = MockedImageWebRepository()
        
        // Mocking successful loading the list of countries:
        countriesWebRepo.countriesResponses = [.success(countries)]
        countriesDBRepo.storeCountriesResults = [.success(())]

        // Mocking successful loading the country details:
        countriesDBRepo.countryDetailsResults = [.success(nil), .success(details)]
        countriesWebRepo.detailsResponses = [.success(detailsIntermediate)]
        countriesDBRepo.storeCountryDetailsResults = [.success(())]

        // Mocking successful loading of the flag:
        imagesRepo.imageResponses = [.success(testImage)]

        let countriesInteractor = RealCountriesInteractor(
            webRepository: countriesWebRepo,
            dbRepository: countriesDBRepo)
        let imagesInteractor = RealImagesInteractor(webRepository: imagesRepo)
        let permissionsInteractor = RealUserPermissionsInteractor(
            appState: store, openAppSettings: { })
        return DIContainer.Interactors(
            images: imagesInteractor,
            countries: countriesInteractor,
            userPermissions: permissionsInteractor)
    }
}

extension InspectableSheet: PopupPresenter { }
```

## File: `UnitTests/UI/ImageViewTests.swift`
```
//
//  ImageViewTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 10.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

@MainActor
@Suite struct ImageViewTests {

    let url = URL(string: "https://test.com/test.png")!

    @Test func imageViewNotRequested() async throws {
        let container = DIContainer(interactors: .mocked(
            images: [.loadImage(url)]
        ))
        let sut = ImageView(imageURL: url, image: .notRequested)
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(text: "") }
                container.interactors.verify()
            }
        }
    }
    
    @Test func imageViewIsLoadingInitial() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = ImageView(imageURL: url, image:
            .isLoading(last: nil, cancelBag: .test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(ViewType.ProgressView.self) }
                container.interactors.verify()
            }
        }
    }
    
    @Test func imageViewIsLoadingRefresh() async throws {
        let container = DIContainer(interactors: .mocked())
        let image = UIColor.red.image(CGSize(width: 10, height: 10))
        let sut = ImageView(imageURL: url, image:
            .isLoading(last: image, cancelBag: .test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(ViewType.ProgressView.self) }
                container.interactors.verify()
            }
        }
    }
    
    @Test func imageViewLoaded() async throws {
        let container = DIContainer(interactors: .mocked())
        let image = UIColor.red.image(CGSize(width: 10, height: 10))
        let sut = ImageView(imageURL: url, image: .loaded(image))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                let loadedImage = try view.find(ViewType.Image.self).actualImage().uiImage()
                #expect(loadedImage == image)
                container.interactors.verify()
            }
        }
    }
    
    @Test func imageViewFailed() async throws {
        let container = DIContainer(interactors: .mocked())
        let sut = ImageView(imageURL: url, image: .failed(NSError.test))
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(text: "Unable to load image") }
                container.interactors.verify()
            }
        }
    }
}
```

## File: `UnitTests/UI/ModalFlagViewTests.swift`
```
//
//  ModalFlagViewTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 01.11.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

@MainActor
@Suite struct ModalFlagViewTests {

    private let country: DBModel.Country = ApiModel.Country.mockedData[0].dbModel()

    @Test func modalDetails() async throws {
        let container = DIContainer(interactors: .mocked(
            images: [.loadImage(country.flag)]
        ))
        let isDisplayed = Binding(wrappedValue: true)
        let sut = ModalFlagView(country: country, isDisplayed: isDisplayed)
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(throws: Never.self) { try view.find(ImageView.self) }
                #expect(throws: Never.self) { try view.find(button: "Close") }
                container.interactors.verify()
            }
        }
    }

    @Test func modalDetailsClose() async throws {
        let container = DIContainer(interactors: .mocked(
            images: [.loadImage(country.flag)]
        ))
        let isDisplayed = Binding(wrappedValue: true)
        let sut = ModalFlagView(country: country, isDisplayed: isDisplayed)
        try await ViewHosting.host(sut.inject(container)) {
            try await sut.inspection.inspect { view in
                #expect(isDisplayed.wrappedValue)
                try view.find(button: "Close").tap()
                #expect(!isDisplayed.wrappedValue)
                container.interactors.verify()
            }
        }
    }

    @Test func modalDetailsCloseLocalization() throws {
        let isDisplayed = Binding(wrappedValue: true)
        let sut = ModalFlagView(country: country, isDisplayed: isDisplayed)
        let labelText = try sut.inspect().find(text: "Close")
        #expect(try labelText.string() == "Close")
        #expect(try labelText.string(locale: Locale(identifier: "de")) == "Schließen")
    }
}
```

## File: `UnitTests/UI/RootViewAppearanceTests.swift`
```
//
//  RootViewAppearanceTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 05.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Testing
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

@MainActor
@Suite struct RootViewAppearanceTests {

    @Test func blurWhenInactive() async throws {
        let sut = RootViewAppearance()
        let container = DIContainer(interactors: .mocked())
        #expect(!container.appState.value.system.isActive)
        let view = EmptyView().modifier(sut)
            .inject(container)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { modifier in
                let content = try modifier.implicitAnyView().viewModifierContent()
                #expect(try content.blur().radius == 10)
            }
        }
    }
    
    @Test func blurWhenActive() async throws {
        let sut = RootViewAppearance()
        let container = DIContainer(interactors: .mocked())
        container.appState[\.system.isActive] = true
        #expect(container.appState.value.system.isActive)
        let view = EmptyView().modifier(sut)
            .inject(container)
        try await ViewHosting.host(view) {
            try await sut.inspection.inspect { modifier in
                let content = try modifier.implicitAnyView().viewModifierContent()
                #expect(try content.blur().radius == 0)
            }
        }
    }
}
```

## File: `UnitTests/Utilities/HelpersTests.swift`
```
//
//  HelpersTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 27.04.2020.
//  Copyright © 2020 Alexey Naumov. All rights reserved.
//

import Foundation
import Testing
@testable import CountriesSwiftUI

@Suite struct HelpersTests {

    @Test func localizedDefaultLocale() {
        let sut = "Countries".localized(Locale.backendDefault)
        #expect(sut == "Countries")
    }

    @Test func localizedKnownLocale() {
        let sut = "Countries".localized(Locale(identifier: "de"))
        #expect(sut == "Länder")
    }

    @Test func localizedUnknownLocale() {
        let sut = "Countries".localized(Locale(identifier: "ch"))
        #expect(sut == "Countries")
    }

    @Test func resultIsSuccess() {
        let sut1 = Result<Void, Error>.success(())
        let sut2 = Result<Void, Error>.failure(NSError.test)
        #expect(sut1.isSuccess)
        #expect(!sut2.isSuccess)
    }
}
```

## File: `UnitTests/Utilities/LoadableTests.swift`
```
//
//  LoadableTests.swift
//  UnitTests
//
//  Created by Alexey Naumov on 31.10.2019.
//  Copyright © 2019 Alexey Naumov. All rights reserved.
//

import Foundation
import Testing
import Combine
import SwiftUI
import ViewInspector
@testable import CountriesSwiftUI

@Suite struct LoadableTests {

    @Test func equality() {
        let possibleValues: [Loadable<Int>] = [
            .notRequested,
            .isLoading(last: nil, cancelBag: CancelBag()),
            .isLoading(last: 9, cancelBag: CancelBag()),
            .loaded(5),
            .loaded(6),
            .failed(NSError.test)
        ]
        possibleValues.enumerated().forEach { (index1, value1) in
            possibleValues.enumerated().forEach { (index2, value2) in
                if index1 == index2 {
                    #expect(value1 == value2)
                } else {
                    #expect(value1 != value2)
                }
            }
        }
    }

    @Test func cancelLoading() {
        let cancenBag1 = CancelBag(), cancenBag2 = CancelBag()
        let subject = PassthroughSubject<Int, Never>()
        subject.sink { _ in }
            .store(in: cancenBag1)
        subject.sink { _ in }
            .store(in: cancenBag2)
        var sut1 = Loadable<Int>.isLoading(last: nil, cancelBag: cancenBag1)
        #expect(cancenBag1.subscriptions.count == 1)
        sut1.cancelLoading()
        #expect(cancenBag1.subscriptions.count == 0)
        #expect(sut1.error != nil)
        var sut2 = Loadable<Int>.isLoading(last: 7, cancelBag: cancenBag2)
        #expect(cancenBag2.subscriptions.count == 1)
        sut2.cancelLoading()
        #expect(cancenBag2.subscriptions.count == 0)
        #expect(sut2.value == 7)
    }

    @Test func map() {
        let values: [Loadable<Int>] = [
            .notRequested,
            .isLoading(last: nil, cancelBag: CancelBag()),
            .isLoading(last: 5, cancelBag: CancelBag()),
            .loaded(7),
            .failed(NSError.test)
        ]
        let expect: [Loadable<String>] = [
            .notRequested,
            .isLoading(last: nil, cancelBag: .test),
            .isLoading(last: "5", cancelBag: .test),
            .loaded("7"),
            .failed(NSError.test)
        ]
        let sut = values.map { value in
            value.map { "\($0)" }
        }
        #expect(sut == expect)
    }

    @MainActor
    @Test func loadSuccess() async {
        let resource: () async throws -> String = {
            try await Task.sleep(nanoseconds: 100_000_000)
            return "test"
        }
        let exp = TestExpectation()
        var values: [Loadable<String>] = []
        let sut = Binding<Loadable<String>>.init(get: {
            return values.last ?? .notRequested
        }, set: {
            values.append($0)
            if $0.value != nil {
                exp.fulfill()
            }
        })
        sut.load(resource)
        await exp.fulfillment()
        #expect(values == [.isLoading(last: nil, cancelBag: .test), .loaded("test")])
    }

    @MainActor
    @Test func loadFailure() async {
        let resource: () async throws -> String = {
            try await Task.sleep(nanoseconds: 100_000_000)
            throw NSError.test
        }
        let exp = TestExpectation()
        var values: [Loadable<String>] = []
        let sut = Binding<Loadable<String>>.init(get: {
            return values.last ?? .notRequested
        }, set: {
            values.append($0)
            if $0.error != nil {
                exp.fulfill()
            }
        })
        sut.load(resource)
        await exp.fulfillment()
        #expect(values == [.isLoading(last: nil, cancelBag: .test), .failed(NSError.test)])
    }

    @Test func helperFunctions() {
        let notRequested = Loadable<Int>.notRequested
        let loadingNil = Loadable<Int>.isLoading(last: nil, cancelBag: CancelBag())
        let loadingValue = Loadable<Int>.isLoading(last: 9, cancelBag: CancelBag())
        let loaded = Loadable<Int>.loaded(5)
        let failedErrValue = Loadable<Int>.failed(NSError.test)
        [notRequested, loadingNil].forEach {
            #expect($0.value == nil)
        }
        [loadingValue, loaded].forEach {
            #expect($0.value != nil)
        }
        [notRequested, loadingNil, loadingValue, loaded].forEach {
            #expect($0.error == nil)
        }
        #expect(failedErrValue.error != nil)
    }

    @Test func throwingMap() {
        let value = Loadable<Int>.loaded(5)
        let sut = value.map { _ in throw NSError.test }
        #expect(sut.error != nil)
    }

    @Test func valueIsMissing() {
        #expect(ValueIsMissingError().localizedDescription == "Data is missing")
    }
}
```


---
id: Alamofire
type: knowledge
owner: OA_Triage
---
# Alamofire
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![Alamofire: Elegant Networking in Swift](https://raw.githubusercontent.com/Alamofire/Alamofire/master/Resources/AlamofireLogo.png)

[![Swift](https://img.shields.io/badge/Swift-6.0_6.1_6.2-orange?style=flat-square)](https://img.shields.io/badge/Swift-6.0_6.1_6.2-Orange?style=flat-square)
[![Platforms](https://img.shields.io/badge/Platforms-macOS_iOS_tvOS_watchOS_visionOS_Linux_Windows_Android-yellowgreen?style=flat-square)](https://img.shields.io/badge/Platforms-macOS_iOS_tvOS_watchOS_vision_OS_Linux_Windows_Android-Green?style=flat-square)
[![CocoaPods Compatible](https://img.shields.io/cocoapods/v/Alamofire.svg?style=flat-square)](https://img.shields.io/cocoapods/v/Alamofire.svg)
[![Carthage Compatible](https://img.shields.io/badge/Carthage-compatible-4BC51D.svg?style=flat-square)](https://github.com/Carthage/Carthage)
[![Swift Package Manager](https://img.shields.io/badge/Swift_Package_Manager-compatible-orange?style=flat-square)](https://img.shields.io/badge/Swift_Package_Manager-compatible-orange?style=flat-square)
[![Swift Forums](https://img.shields.io/badge/Swift_Forums-Alamofire-orange?style=flat-square)](https://forums.swift.org/c/related-projects/alamofire/37)

Alamofire is an HTTP networking library written in Swift.

- [Features](#features)
- [Component Libraries](#component-libraries)
- [Requirements](#requirements)
- [Migration Guides](#migration-guides)
- [Communication](#communication)
- [Installation](#installation)
- [Contributing](#contributing)
- [Usage](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#using-alamofire)
  - [**Introduction -**](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#introduction) [Making Requests](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#making-requests), [Response Handling](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#response-handling), [Response Validation](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#response-validation), [Response Caching](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#response-caching)
  - **HTTP -** [HTTP Methods](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#http-methods), [Parameters and Parameter Encoder](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md##request-parameters-and-parameter-encoders), [HTTP Headers](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#http-headers), [Authentication](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#authentication)
  - **Large Data -** [Downloading Data to a File](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#downloading-data-to-a-file), [Uploading Data to a Server](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#uploading-data-to-a-server)
  - **Tools -** [Statistical Metrics](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#statistical-metrics), [cURL Command Output](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Usage.md#curl-command-output)
- [Advanced Usage](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md)
  - **URL Session -** [Session Manager](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#session), [Session Delegate](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#sessiondelegate), [Request](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#request)
  - **Routing -** [Routing Requests](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#routing-requests), [Adapting and Retrying Requests](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#adapting-and-retrying-requests-with-requestinterceptor)
  - **Model Objects -** [Custom Response Handlers](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#customizing-response-handlers)
  - **Advanced Concurrency -** [Swift Concurrency](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#using-alamofire-with-swift-concurrency) and [Combine](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#using-alamofire-with-combine)
  - **Connection -** [Security](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#security), [Network Reachability](https://github.com/Alamofire/Alamofire/blob/master/Documentation/AdvancedUsage.md#network-reachability)
- [Open Radars](#open-radars)
- [FAQ](#faq)
- [Credits](#credits)
- [Donations](#donations)
- [License](#license)

## Features

- [x] Chainable Request / Response Methods
- [x] Swift Concurrency Support Back to iOS 13, macOS 10.15, tvOS 13, and watchOS 6.
- [x] Combine Support
- [x] URL / JSON Parameter Encoding
- [x] Upload File / Data / Stream / MultipartFormData
- [x] Download File using Request or Resume Data
- [x] Authentication with `URLCredential`
- [x] HTTP Response Validation
- [x] Upload and Download Progress Closures with Progress
- [x] cURL Command Output
- [x] Dynamically Adapt and Retry Requests
- [x] TLS Certificate and Public Key Pinning
- [x] Network Reachability
- [x] Comprehensive Unit and Integration Test Coverage
- [x] [Complete Documentation](https://alamofire.github.io/Alamofire)

## Write Requests Fast!

Alamofire's compact syntax and extensive feature set allow requests with powerful features like automatic retry to be written in just a few lines of code.

```swift
// Automatic String to URL conversion, Swift concurrency support, and automatic retry.
let response = await AF.request("https://httpbin.org/get", interceptor: .retryPolicy)
                       // Automatic HTTP Basic Auth.
                       .authenticate(username: "user", password: "pass")
                       // Caching customization.
                       .cacheResponse(using: .cache)
                       // Redirect customization.
                       .redirect(using: .follow)
                       // Validate response code and Content-Type.
                       .validate()
                       // Produce a cURL command for the request.
                       .cURLDescription { description in
                         print(description)
                       }
                       // Automatic Decodable support with background parsing.
                       .serializingDecodable(DecodableType.self)
                       // Await the full response with metrics and a parsed body.
                       .response
// Detailed response description for easy debugging.
debugPrint(response)
```

## Component Libraries

In order to keep Alamofire focused specifically on core networking implementations, additional component libraries have been created by the [Alamofire Software Foundation](https://github.com/Alamofire/Foundation) to bring additional functionality to the Alamofire ecosystem.

- [AlamofireImage](https://github.com/Alamofire/AlamofireImage) - An image library including image response serializers, `UIImage` and `UIImageView` extensions, custom image filters, an auto-purging in-memory cache, and a priority-based image downloading system.
- [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator) - Controls the visibility of the network activity indicator on iOS using Alamofire. It contains configurable delay timers to help mitigate flicker and can support `URLSession` instances not managed by Alamofire.

## Requirements

| Platform                                             | Minimum Swift Version | Installation                                                                                                         | Status                   |
| ---------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| iOS 10.0+ / macOS 10.12+ / tvOS 10.0+ / watchOS 3.0+ | 6.0 / Xcode 16.0      | [CocoaPods](#cocoapods), [Carthage](#carthage), [Swift Package Manager](#swift-package-manager), [Manual](#manually) | Fully Tested             |
| Linux                                                | Latest Only           | [Swift Package Manager](#swift-package-manager)                                                                      | Building But Unsupported |
| Windows                                              | Latest Only           | [Swift Package Manager](#swift-package-manager)                                                                      | Building But Unsupported |
| Android                                              | Latest Only           | [Swift Package Manager](#swift-package-manager)                                                                      | Building But Unsupported |

#### Known Issues on Linux and Windows

Alamofire builds on Linux, Windows, and Android but there are missing features and many issues in the underlying `swift-corelibs-foundation` that prevent full functionality and may cause crashes. These include:

- `ServerTrustManager` and associated certificate functionality is unavailable, so there is no certificate pinning and no client certificate support.
- Various methods of HTTP authentication may crash, including HTTP Basic and HTTP Digest. Crashes may occur if responses contain server challenges.
- Cache control through `CachedResponseHandler` and associated APIs is unavailable, as the underlying delegate methods aren't called.
- `URLSessionTaskMetrics` are never gathered.
- `WebSocketRequest` is not available.

Due to these issues, Alamofire is unsupported on Linux, Windows, and Android. Please report any crashes to the [Swift bug reporter](https://bugs.swift.org).

## Migration Guides

- [Alamofire 5.0 Migration Guide](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%205.0%20Migration%20Guide.md)
- [Alamofire 4.0 Migration Guide](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%204.0%20Migration%20Guide.md)
- [Alamofire 3.0 Migration Guide](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%203.0%20Migration%20Guide.md)
- [Alamofire 2.0 Migration Guide](https://github.com/Alamofire/Alamofire/blob/master/Documentation/Alamofire%202.0%20Migration%20Guide.md)

## Communication

- If you **need help with making network requests** using Alamofire, use [Stack Overflow](https://stackoverflow.com/questions/tagged/alamofire) and tag `alamofire`.
- If you need to **find or understand an API**, check [our documentation](http://alamofire.github.io/Alamofire/) or [Apple's documentation for `URLSession`](https://developer.apple.com/documentation/foundation/url_loading_system), on top of which Alamofire is built.
- If you need **help with an Alamofire feature**, use [our forum on swift.org](https://forums.swift.org/c/related-projects/alamofire).
- If you'd like to **discuss Alamofire best practices**, use [our forum on swift.org](https://forums.swift.org/c/related-projects/alamofire).
- If you'd like to **discuss a feature request**, use [our forum on swift.org](https://forums.swift.org/c/related-projects/alamofire).
- If you **found a bug**, open an issue here on GitHub and follow the guide. The more detail the better!

## Installation

### Swift Package Manager

The [Swift Package Manager](https://swift.org/package-manager/) is a tool for automating the distribution of Swift code and is integrated into the `swift` compiler.

Once you have your Swift package set up, adding Alamofire as a dependency is as easy as adding it to the `dependencies` value of your `Package.swift` or the Package list in Xcode.

```swift
dependencies: [
    .package(url: "https://github.com/Alamofire/Alamofire.git", .upToNextMajor(from: "5.11.0"))
]
```

Normally you'll want to depend on the `Alamofire` target:

```swift
.product(name: "Alamofire", package: "Alamofire")
```

But if you want to force Alamofire to be dynamically linked (do not do this unless you're sure you need it), you can depend on the `AlamofireDynamic` target:

```swift
.product(name: "AlamofireDynamic", package: "Alamofire")
```

### CocoaPods

[CocoaPods](https://cocoapods.org) is a dependency manager for Cocoa projects. For usage and installation instructions, visit their website. To integrate Alamofire into your Xcode project using CocoaPods, specify it in your `Podfile`:

```ruby
pod 'Alamofire'
```

### Carthage

[Carthage](https://github.com/Carthage/Carthage) is a decentralized dependency manager that builds your dependencies and provides you with binary frameworks. To integrate Alamofire into your Xcode project using Carthage, specify it in your `Cartfile`:

```ogdl
github "Alamofire/Alamofire"
```

### Manually

If you prefer not to use any of the aforementioned dependency managers, you can integrate Alamofire into your project manually.

#### Embedded Framework

- Open up Terminal, `cd` into your top-level project directory, and run the following command "if" your project is not initialized as a git repository:

  ```bash
  $ git init
  ```

- Add Alamofire as a git [submodule](https://git-scm.com/docs/git-submodule) by running the following command:

  ```bash
  $ git submodule add https://github.com/Alamofire/Alamofire.git
  ```

- Open the new `Alamofire` folder, and drag the `Alamofire.xcodeproj` into the Project Navigator of your application's Xcode project.

  > It should appear nested underneath your application's blue project icon. Whether it is above or below all the other Xcode groups does not matter.

- Select the `Alamofire.xcodeproj` in the Project Navigator and verify the deployment target matches that of your application target.
- Next, select your application project in the Project Navigator (blue project icon) to navigate to the target configuration window and select the application target under the "Targets" heading in the sidebar.
- In the tab bar at the top of that window, open the "General" panel.
- Click on the `+` button under the "Embedded Binaries" section.
- You will see two different `Alamofire.xcodeproj` folders each with two different versions of the `Alamofire.framework` nested inside a `Products` folder.

  > It does not matter which `Products` folder you choose from, but it does matter whether you choose the top or bottom `Alamofire.framework`.

- Select the top `Alamofire.framework` for iOS and the bottom one for macOS.

  > You can verify which one you selected by inspecting the build log for your project. The build target for `Alamofire` will be listed as `Alamofire iOS`, `Alamofire macOS`, `Alamofire tvOS`, or `Alamofire watchOS`.

- And that's it!

  > The `Alamofire.framework` is automagically added as a target dependency, linked framew
... [TRUNCATED]
```

### File: .jazzy.yaml
```yaml
author: Alamofire Software Foundation
author_url: http://alamofire.org/
github_url: https://github.com/Alamofire/Alamofire
root_url: https://alamofire.github.io/Alamofire/
module: Alamofire
output: docs
theme: fullwidth
xcodebuild_arguments: [-workspace, 'Alamofire.xcworkspace', -scheme, 'Alamofire iOS']

```

### File: CONTRIBUTING.md
```md
# Contributing Guidelines

This document contains information and guidelines about contributing to this project.
Please read it before you start participating.

**Topics**

* [Asking Questions](#asking-questions)
* [Reporting Security Issues](#reporting-security-issues)
* [Reporting Issues](#reporting-other-issues)
* [Triage Issues](#triage-issues)
* [Submitting Pull Requests](#submitting-pull-requests)
* [Developers Certificate of Origin](#developers-certificate-of-origin)
* [Code of Conduct](#code-of-conduct)

## Asking Questions

**We don't use GitHub as a support forum.**
For any usage questions that are not specific to the project itself, please ask on [Stack Overflow](https://stackoverflow.com) instead. By doing so, you'll be more likely to quickly solve your problem, and you'll allow anyone else with the same question to find the answer. This also allows maintainers to focus on improving the project for others.

If you'd like to discuss Alamofire best practices, common usage patterns, ideas for new features, or ongoing development, please use our [Swift Forums](https://forums.swift.org/c/related-projects/alamofire/).

## Reporting Security Issues

The Alamofire Software Foundation takes security seriously.
If you discover a security issue, please bring it to our attention right away!

Please **DO NOT** file a public issue, instead send your report privately to <security@alamofire.org>. This will help ensure that any vulnerabilities that _are_ found can be [disclosed responsibly](https://en.wikipedia.org/wiki/Responsible_disclosure) to any affected parties.

## Reporting Other Issues

A great way to contribute to the project is to send a detailed issue when you encounter a problem. We always appreciate a well-written, thorough bug report.

Check that the project issues database doesn't already include that problem or suggestion before submitting an issue. If you find a match, feel free to vote for the issue by adding a reaction. Doing this helps prioritize the most common problems and requests.

When reporting issues, please fill out our issue template. The information the template asks for will help us review and fix your issue faster.

## Triage Issues [![Open Source Helpers](https://www.codetriage.com/alamofire/alamofire/badges/users.svg)](https://www.codetriage.com/alamofire/alamofire)

You can triage issues which may include reproducing bug reports or asking for vital information, such as version numbers or reproduction instructions. If you would like to start triaging issues, one easy way to get started is to [subscribe to alamofire on CodeTriage](https://www.codetriage.com/alamofire/alamofire).

## Submitting Pull Requests

You can contribute by fixing bugs or adding new features. For larger code changes, we recommend first discussing your ideas on our [GitHub Discussions](https://github.com/Alamofire/Alamofire/discussions) or [Swift Forums](https://forums.swift.org/c/related-projects/alamofire/). When submitting a pull request, please add relevant tests and ensure your changes don't break any existing tests (see [Automated Tests](#automated-tests) below).

### Automated Tests

Alamofire's tests depend on our [Firewalk](https://github.com/Alamofire/Firewalk) test server. To run the automated tests, you first need to have the server running locally. 

In your terminal, run the following commands:
- To install Firewalk: `brew install alamofire/alamofire/firewalk`
- To run and detach the server: `firewalk &`
- To stop the server, run `kill` and provide the pid output after launch.

## Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

- (a) The contribution was created in whole or in part by me and I
      have the right to submit it under the open source license
      indicated in the file; or

- (b) The contribution is based upon previous work that, to the best
      of my knowledge, is covered under an appropriate open source
      license and I have the right under that license to submit that
      work with modifications, whether created in whole or in part
      by me, under the same open source license (unless I am
      permitted to submit under a different license), as indicated
      in the file; or

- (c) The contribution was provided directly to me by some other
      person who certified (a), (b) or (c) and I have not modified
      it.

- (d) I understand and agree that this project and the contribution
      are public and that a record of the contribution (including all
      personal information I submit with it, including my sign-off) is
      maintained indefinitely and may be redistributed consistent with
      this project or the open source license(s) involved.

## Code of Conduct

The Code of Conduct governs how we behave in public or in private
whenever the project will be judged by our actions.
We expect it to be honored by everyone who contributes to this project.

See [CONDUCT.md](https://github.com/Alamofire/Foundation/blob/master/CONDUCT.md) for details.

---

*Some of the ideas and wording for the statements above were based on work by the [Docker](https://github.com/docker/docker/blob/master/CONTRIBUTING.md) and [Linux](https://elinux.org/Developer_Certificate_Of_Origin) communities. We commend them for their efforts to facilitate collaboration in their projects.*

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
### Issue Link :link:
<!-- What issue does this fix? If an issue doesn't exist, remove this section. -->

### Goals :soccer:
<!-- List the high-level objectives of this pull request. -->
<!-- Include any relevant context. -->

### Implementation Details :construction:
<!-- Explain the reasoning behind any architectural changes. -->
<!-- Highlight any new functionality. -->

### Testing Details :mag:
<!-- Describe what tests you've added for your changes. -->

```

### File: docs\Classes.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Classes  Reference</title>
    <link rel="stylesheet" type="text/css" href="css/jazzy.css" />
    <link rel="stylesheet" type="text/css" href="css/highlight.css" />
    <meta charset="utf-8">
    <script src="js/jquery.min.js" defer></script>
    <script src="js/jazzy.js" defer></script>
    
    <script src="js/lunr.min.js" defer></script>
    <script src="js/typeahead.jquery.js" defer></script>
    <script src="js/jazzy.search.js" defer></script>
  </head>
  <body>

    <a name="//apple_ref/swift/Section/Classes" class="dashAnchor"></a>

    <a title="Classes  Reference"></a>

    <header class="header">
      <p class="header-col header-col--primary">
        <a class="header-link" href="index.html">
          Alamofire 5.11.0 Docs
        </a>
         (96% documented)
      </p>
    
      <div class="header-col--secondary">
        <form role="search" action="search.json">
          <input type="text" placeholder="Search documentation" data-typeahead>
        </form>
      </div>
    
        <p class="header-col header-col--secondary">
          <a class="header-link" href="https://github.com/Alamofire/Alamofire">
            <img class="header-icon" src="img/gh.png" alt="GitHub"/>
            View on GitHub
          </a>
        </p>
    
        <p class="header-col header-col--secondary">
          <a class="header-link" href="dash-feed://https%3A%2F%2Falamofire.github.io%2FAlamofire%2Fdocsets%2FAlamofire.xml">
            <img class="header-icon" src="img/dash.png" alt="Dash"/>
            Install in Dash
          </a>
        </p>
    </header>

    <p class="breadcrumbs">
      <a class="breadcrumb" href="index.html">Alamofire</a>
      <img class="carat" src="img/carat.png" alt=""/>
      Classes  Reference
    </p>

    <div class="content-wrapper">
      <nav class="navigation">
        <ul class="nav-groups">
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Classes.html">Classes</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Adapter.html">Adapter</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AlamofireNotifications.html">AlamofireNotifications</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AuthenticationInterceptor.html">AuthenticationInterceptor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AuthenticationInterceptor/RefreshWindow.html">– RefreshWindow</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ClosureEventMonitor.html">ClosureEventMonitor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/CompositeEventMonitor.html">CompositeEventMonitor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/CompositeTrustEvaluator.html">CompositeTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ConnectionLostRetryPolicy.html">ConnectionLostRetryPolicy</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataRequest.html">DataRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataResponseSerializer.html">DataResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest.html">DataStreamRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Stream.html">– Stream</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Event.html">– Event</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Completion.html">– Completion</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/CancellationToken.html">– CancellationToken</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DecodableResponseSerializer.html">DecodableResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DefaultTrustEvaluator.html">DefaultTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DisabledTrustEvaluator.html">DisabledTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest.html">DownloadRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest/Options.html">– Options</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest/Downloadable.html">– Downloadable</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Interceptor.html">Interceptor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/JSONParameterEncoder.html">JSONParameterEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/JSONResponseSerializer.html">JSONResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/MultipartFormData.html">MultipartFormData</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/NetworkReachabilityManager.html">NetworkReachabilityManager</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/NetworkReachabilityManager/NetworkReachabilityStatus.html">– NetworkReachabilityStatus</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/OfflineRetrier.html">OfflineRetrier</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/PinnedCertificatesTrustEvaluator.html">PinnedCertificatesTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/PublicKeysTrustEvaluator.html">PublicKeysTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request.html">Request</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request/State.html">– State</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request/ResponseDisposition.html">– ResponseDisposition</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Retrier.html">Retrier</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RetryPolicy.html">RetryPolicy</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RevocationTrustEvaluator.html">RevocationTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RevocationTrustEvaluator/Options.html">– Options</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ServerTrustManager.html">ServerTrustManager</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Session.html">Session</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Session/RequestSetup.html">– RequestSetup</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/SessionDelegate.html">SessionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/StringResponseSerializer.html">StringResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder.html">URLEncodedFormEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/ArrayEncoding.html">– ArrayEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/BoolEncoding.html">– BoolEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/DataEncoding.html">– DataEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/DateEncoding.html">– DateEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/KeyEncoding.html">– KeyEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/KeyPathEncoding.html">– KeyPathEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/NilEncoding.html">– NilEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/SpaceEncoding.html">– SpaceEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/Error.html">– Error</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormParameterEncoder.html">URLEncodedFormParameterEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormParameterEncoder/Destination.html">– Destination</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/UploadRequest.html">UploadRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/UploadRequest/Uploadable.html">– Uploadable</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Global%20Variables.html">Global Variables</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Global%20Variables.html#/s:9Alamofire2AFAA7SessionCvp">AF</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Enums.html">Enumerations</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError.html">AFError</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/MultipartEncodingFailureReason.html">– MultipartEncodingFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/UnexpectedInputStreamLength.html">– UnexpectedInputStreamLength</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ParameterEncodingFailureReason.html">– ParameterEncodingFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ParameterEncoderFailureReason.html">– ParameterEncoderFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ResponseValidationFailureReason.html">– ResponseValidationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ResponseSerializationFailureReason.html">– ResponseSerializationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ServerTrustFailureReason.html">– ServerTrustFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/URLRequestValidationFailureReason.html">– URLRequestValidationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFInfo.html">AFInfo</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AuthenticationError.html">AuthenticationError</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/RetryResult.html">RetryResult</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Extensions.html">Extensions</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Extension
... [TRUNCATED]
```

### File: docs\Enums.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Enumerations  Reference</title>
    <link rel="stylesheet" type="text/css" href="css/jazzy.css" />
    <link rel="stylesheet" type="text/css" href="css/highlight.css" />
    <meta charset="utf-8">
    <script src="js/jquery.min.js" defer></script>
    <script src="js/jazzy.js" defer></script>
    
    <script src="js/lunr.min.js" defer></script>
    <script src="js/typeahead.jquery.js" defer></script>
    <script src="js/jazzy.search.js" defer></script>
  </head>
  <body>

    <a name="//apple_ref/swift/Section/Enumerations" class="dashAnchor"></a>

    <a title="Enumerations  Reference"></a>

    <header class="header">
      <p class="header-col header-col--primary">
        <a class="header-link" href="index.html">
          Alamofire 5.11.0 Docs
        </a>
         (96% documented)
      </p>
    
      <div class="header-col--secondary">
        <form role="search" action="search.json">
          <input type="text" placeholder="Search documentation" data-typeahead>
        </form>
      </div>
    
        <p class="header-col header-col--secondary">
          <a class="header-link" href="https://github.com/Alamofire/Alamofire">
            <img class="header-icon" src="img/gh.png" alt="GitHub"/>
            View on GitHub
          </a>
        </p>
    
        <p class="header-col header-col--secondary">
          <a class="header-link" href="dash-feed://https%3A%2F%2Falamofire.github.io%2FAlamofire%2Fdocsets%2FAlamofire.xml">
            <img class="header-icon" src="img/dash.png" alt="Dash"/>
            Install in Dash
          </a>
        </p>
    </header>

    <p class="breadcrumbs">
      <a class="breadcrumb" href="index.html">Alamofire</a>
      <img class="carat" src="img/carat.png" alt=""/>
      Enumerations  Reference
    </p>

    <div class="content-wrapper">
      <nav class="navigation">
        <ul class="nav-groups">
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Classes.html">Classes</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Adapter.html">Adapter</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AlamofireNotifications.html">AlamofireNotifications</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AuthenticationInterceptor.html">AuthenticationInterceptor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/AuthenticationInterceptor/RefreshWindow.html">– RefreshWindow</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ClosureEventMonitor.html">ClosureEventMonitor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/CompositeEventMonitor.html">CompositeEventMonitor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/CompositeTrustEvaluator.html">CompositeTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ConnectionLostRetryPolicy.html">ConnectionLostRetryPolicy</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataRequest.html">DataRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataResponseSerializer.html">DataResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest.html">DataStreamRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Stream.html">– Stream</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Event.html">– Event</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/Completion.html">– Completion</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DataStreamRequest/CancellationToken.html">– CancellationToken</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DecodableResponseSerializer.html">DecodableResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DefaultTrustEvaluator.html">DefaultTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DisabledTrustEvaluator.html">DisabledTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest.html">DownloadRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest/Options.html">– Options</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/DownloadRequest/Downloadable.html">– Downloadable</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Interceptor.html">Interceptor</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/JSONParameterEncoder.html">JSONParameterEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/JSONResponseSerializer.html">JSONResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/MultipartFormData.html">MultipartFormData</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/NetworkReachabilityManager.html">NetworkReachabilityManager</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/NetworkReachabilityManager/NetworkReachabilityStatus.html">– NetworkReachabilityStatus</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/OfflineRetrier.html">OfflineRetrier</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/PinnedCertificatesTrustEvaluator.html">PinnedCertificatesTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/PublicKeysTrustEvaluator.html">PublicKeysTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request.html">Request</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request/State.html">– State</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Request/ResponseDisposition.html">– ResponseDisposition</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Retrier.html">Retrier</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RetryPolicy.html">RetryPolicy</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RevocationTrustEvaluator.html">RevocationTrustEvaluator</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/RevocationTrustEvaluator/Options.html">– Options</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/ServerTrustManager.html">ServerTrustManager</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Session.html">Session</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/Session/RequestSetup.html">– RequestSetup</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/SessionDelegate.html">SessionDelegate</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/StringResponseSerializer.html">StringResponseSerializer</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder.html">URLEncodedFormEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/ArrayEncoding.html">– ArrayEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/BoolEncoding.html">– BoolEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/DataEncoding.html">– DataEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/DateEncoding.html">– DateEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/KeyEncoding.html">– KeyEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/KeyPathEncoding.html">– KeyPathEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/NilEncoding.html">– NilEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/SpaceEncoding.html">– SpaceEncoding</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormEncoder/Error.html">– Error</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormParameterEncoder.html">URLEncodedFormParameterEncoder</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/URLEncodedFormParameterEncoder/Destination.html">– Destination</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/UploadRequest.html">UploadRequest</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Classes/UploadRequest/Uploadable.html">– Uploadable</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Global%20Variables.html">Global Variables</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Global%20Variables.html#/s:9Alamofire2AFAA7SessionCvp">AF</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Enums.html">Enumerations</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError.html">AFError</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/MultipartEncodingFailureReason.html">– MultipartEncodingFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/UnexpectedInputStreamLength.html">– UnexpectedInputStreamLength</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ParameterEncodingFailureReason.html">– ParameterEncodingFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ParameterEncoderFailureReason.html">– ParameterEncoderFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ResponseValidationFailureReason.html">– ResponseValidationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ResponseSerializationFailureReason.html">– ResponseSerializationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/ServerTrustFailureReason.html">– ServerTrustFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFError/URLRequestValidationFailureReason.html">– URLRequestValidationFailureReason</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AFInfo.html">AFInfo</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/AuthenticationError.html">AuthenticationError</a>
              </li>
              <li class="nav-group-task">
                <a class="nav-group-task-link" href="Enums/RetryResult.html">RetryResult</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a class="nav-group-name-link" href="Extensions.html">Extensions</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a class="nav-group-task-l
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

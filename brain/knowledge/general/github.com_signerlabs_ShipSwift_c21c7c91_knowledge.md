---
id: github.com-signerlabs-shipswift-c21c7c91-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.135559
---

# KNOWLEDGE EXTRACT: github.com_signerlabs_ShipSwift_c21c7c91
> **Extracted on:** 2026-04-01 14:13:00
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523773/github.com_signerlabs_ShipSwift_c21c7c91

---

## File: `.gitignore`
```
# macOS
.DS_Store
**/.DS_Store

# Xcode
*.xcuserstate
**/UserInterfaceState.xcuserstate
xcuserdata/
DerivedData/
build/
*.moved-aside
*.ipa
*.dSYM
*.dSYM.zip
*.xccheckout
*.xcscmblueprint

# Swift Package Manager
.build/
.swiftpm/
Package.resolved

# CocoaPods (if applicable)
Pods/

# Claude
.claude/

# AWS Amplify
amplify_outputs.json

# Secrets (never commit real credentials)
SWSecrets.swift

# Misc
*.hmap
*.o
*.pch
timeline.xctimeline
playground.xcworkspace
```

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

## Project Overview
- ShipSwift iOS component template library (public repo)

## Directory Structure
- Reusable components live under `ShipSwift/SWPackage/` in five directories:
  - `SWAnimation/` — Self-contained animation components (each works independently, may depend on SWUtil only)
  - `SWChart/` — Self-contained chart components (each works independently, may depend on SWUtil only)
  - `SWComponent/` — Self-contained UI components organized by category:
    - `Display/` — Display components (FloatingLabels, MarkdownText, ScrollingFAQ, RotatingQuote, BulletPointText, GradientDivider, Label, OnboardingView, OrderView, RootTabView)
    - `Feedback/` — Feedback components (Alert, Loading, ThinkingIndicator)
    - `Input/` — Input components (TabButton, Stepper, AddSheet)
  - `SWModule/` — Multi-file frameworks (SWAuth, SWCamera, SWPaywall, SWChat, SWSetting, SWSubjectLifting, SWTikTokTracking)
  - `SWUtil/` — Shared utilities (no dependencies on other SWPackage directories)
- Showcase app views live under `ShipSwift/View/` (HomeView, ChatView, ComponentView, ProPaywallView, RootTabView, SettingView, ShipSwiftAuthView)
- App services live under `ShipSwift/Service/` (ChatService, ComponentRegistry)
- Shared app components live under `ShipSwift/Component/` (ListItem)

## Naming Conventions
- All type names use the `SW` prefix: `SWAlertManager`, `SWStoreManager`, `SWCameraView`
- View modifier methods use `.sw` lowercase prefix: `.swAlert()`, `.swPageLoading()`, `.swPrimary`
- File names match their primary type: `SWAlert.swift` contains `SWAlertManager`
- **Platform suffix rule**: iOS-only files use `+iOS` suffix (e.g. `SWCameraManager+iOS.swift`), macOS-only files use `+macOS` suffix. Cross-platform files have no suffix
- **Xcode Build Phases reminder**: This project supports both iOS and macOS. When adding a `+iOS` or `+macOS` file, remind the user to set the platform filter in Xcode → Build Phases → Compile Sources (change "Always Used" to "iOS" or "macOS"). Do NOT use `#if os(iOS)` / `#if os(macOS)` as a substitute

## Dependency Rules
- `SWUtil` has zero dependencies on other SWPackage directories
- `SWAnimation`, `SWChart`, and `SWComponent` may only depend on `SWUtil`
- `SWModule` may depend on `SWUtil`, `SWComponent`, and other files within the same module

## Self-Containment Principle
- Every file in `SWAnimation/`, `SWChart/`, and `SWComponent/` must work without importing other SWPackage files (except `SWUtil`)
- Alert and Loading merge their managers into the same file for self-containment
- CameraManager uses an `onError` closure instead of directly referencing `SWAlertManager`

## Code Style
- All comments and documentation in English (this is a public repo; overrides the global Chinese rule)
- No external constants file — product IDs, URLs, and config values are inlined or configurable via struct properties
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 SignerLabs

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
# ShipSwift

<div align="center">

![ShipSwift Banner](assets/banner.jpg)

**AI-native SwiftUI component library — production-ready code that LLMs can use to build real apps.**

[![Website](https://img.shields.io/badge/Website-shipswift.app-blue.svg)](https://www.shipswift.app/)
[![App Store](https://img.shields.io/badge/App_Store-Demo_App-black.svg)](https://apps.apple.com/us/app/shipswift-mcp-codebase/id6759209764)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Swift](https://img.shields.io/badge/Swift-5.0+-F05138.svg)](https://swift.org)
[![iOS](https://img.shields.io/badge/iOS-18.0+-000000.svg)](https://developer.apple.com/ios/)
[![Skills](https://img.shields.io/badge/Skills-Powered-8A2BE2.svg)](https://github.com/signerlabs/shipswift-skills)
[![ShipSwift MCP server](https://glama.ai/mcp/servers/signerlabs/ShipSwift/badges/score.svg)](https://glama.ai/mcp/servers/signerlabs/ShipSwift)

[Quick Start](#quick-start) · [Components](#components) · [Directory Structure](#directory-structure) · [Recipes](#recipes) · [Contributing](#contributing)

</div>

---

## What is ShipSwift?

One command gives your AI everything it needs — production-ready SwiftUI components, full-stack recipes, and the context to build real apps without guessing. Check more [MCP recipes](https://www.shipswift.app/).

Download the [Showcase App](https://apps.apple.com/us/app/shipswift-mcp-codebase/id6759209764) to preview every component on your device.

---

## Quick Start

### Option 1: Skills + Recipe Server (Recommended)

**Step 1** — Install ShipSwift Skills:

```bash
npx skills add signerlabs/shipswift-skills
```

**Step 2** — Connect the recipe server so your AI can fetch recipes:

```bash
# Claude Code
claude mcp add --transport http shipswift https://api.shipswift.app/mcp

# Gemini CLI
gemini mcp add --transport http shipswift https://api.shipswift.app/mcp
```

For Cursor, VS Code Copilot, Windsurf, and other tools, see the [Skills repo](https://github.com/signerlabs/shipswift-skills) for MCP setup.

**Step 3** — Ask your AI:
- "Add a shimmer loading animation"
- "Build an authentication flow with Cognito"
- "Show me all chart components"

### Option 2: Local Skills (No MCP Required)

Install skills that read source files directly from this repo — works offline, no server needed:

```bash
npx skills add signerlabs/ShipSwift
```

Your AI can then browse the component catalog and read source code locally. Try:
- "Explore ShipSwift recipes"
- "Add a shimmer animation"
- "Build a chat feature"

> **Tip**: If you also connect the MCP server (Option 1), your AI gets access to additional Pro recipes (backend guides, compliance templates, pitfall docs).

### Option 3: File Copy

1. Clone this repository
2. Copy the files you need from `ShipSwift/SWPackage/` into your Xcode project
3. Each component in `SWAnimation/`, `SWChart/`, and `SWComponent/` is self-contained — just copy the file and `SWUtil/` if needed

### Run the Showcase App

```bash
git clone https://github.com/signerlabs/ShipSwift.git
cd ShipSwift
open ShipSwift.xcodeproj
```

Select a simulator or device, then press **Cmd+R** to build and run.

---

## Components

### SWAnimation — Animation Components

BeforeAfterSlider · TypewriterText · ShakingIcon · Shimmer · GlowSweep · LightSweep · ScanningOverlay · AnimatedMeshGradient · OrbitingLogos

### SWChart — Chart Components

LineChart · BarChart · AreaChart · DonutChart · RingChart · RadarChart · ScatterChart · ActivityHeatmap

### SWComponent — UI Components

**Display:** FloatingLabels · ScrollingFAQ · RotatingQuote · BulletPointText · GradientDivider · Label · OnboardingView · OrderView · RootTabView
**Feedback:** Alert · Loading · ThinkingIndicator
**Input:** TabButton · Stepper · AddSheet

### SWModule — Multi-File Frameworks

- **SWAuth** — User authentication (Amplify/Cognito, social login, email/password, phone sign-in with country code picker)
- **SWCamera** — Camera capture with viewfinder, zoom, photo picker, and face detection with Vision landmark tracking
- **SWPaywall** — Subscription paywall using StoreKit 2 — *iOS client included free. Full-stack recipe (backend + compliance + pitfalls) → [Pro](https://shipswift.app/#pricing)*
- **SWChat** — All-in-one chat view with message list, text input, and optional voice recognition (VolcEngine ASR)
- **SWSetting** — Settings page template with language switch, share, legal links, recommended apps
- **SWSubjectLifting** — Background removal using VisionKit ImageAnalysis
- **SWTikTokTracking** — TikTok Events API integration for attribution tracking — *iOS client included free. Full-stack recipe (backend + compliance + pitfalls) → [Pro](https://shipswift.app/#pricing)*

### SWUtil — Shared Utilities

DebugLog · String/Date/View extensions · LocationManager

---

## Directory Structure

```
ShipSwift/
├── SWPackage/
│   ├── SWAnimation/          # Animation components
│   ├── SWChart/              # Chart components
│   ├── SWComponent/          # UI components
│   │   ├── Display/          #   Display components
│   │   ├── Feedback/         #   Feedback components
│   │   └── Input/            #   Input components
│   ├── SWModule/             # Multi-file frameworks
│   │   ├── SWAuth/           #   Authentication
│   │   ├── SWCamera/         #   Camera + face detection
│   │   ├── SWPaywall/        #   Subscription paywall
│   │   ├── SWChat/           #   Chat + voice input
│   │   ├── SWSetting/        #   Settings page
│   │   ├── SWSubjectLifting/ #   Background removal
│   │   └── SWTikTokTracking/ #   TikTok attribution
│   └── SWUtil/               # Shared utilities
├── View/                     # Showcase app views
├── Service/                  # App services
└── Component/                # Shared app components
```

---

## Naming Convention

All types use the `SW` prefix (e.g., `SWAlertManager`, `SWStoreManager`).
View modifiers use `.sw` lowercase prefix (e.g., `.swAlert()`, `.swPageLoading()`, `.swPrimary`).

## Dependency Rules

```
SWUtil        ← no dependencies on other SWPackage directories
SWAnimation   ← may depend on SWUtil only
SWChart       ← may depend on SWUtil only
SWComponent   ← may depend on SWUtil only
SWModule      ← may depend on SWUtil and SWComponent
```

---

## Recipes

ShipSwift provides **free and pro recipes** via Skills — each recipe includes complete SwiftUI source code, implementation steps, and best practices. Your AI assistant can retrieve any recipe on demand.

| Category | Examples |
|----------|----------|
| Animation | Shimmer, Typewriter, Orbiting Logos |
| Chart | Line, Bar, Donut, Radar, Heatmap |
| Component | Alert, Onboarding, Stepper, FAQ |
| Module | Auth, Camera, Chat, Setting, Infra CDK, Subscription\*, TikTok Tracking\*, Export & Share\* |

\* Pro recipes — includes full backend, compliance templates, and pitfall guides. *Coming soon: Push Notifications, Analytics Dashboard.*

Three tools are available: `listRecipes`, `getRecipe`, `searchRecipes`.

Learn more at [shipswift.app](https://shipswift.app) · Skills repo: [signerlabs/shipswift-skills](https://github.com/signerlabs/shipswift-skills)

---

## Free vs Pro

All iOS client code is open-source under the MIT license. Pro recipes add everything you need to go from prototype to production.

| | Free (Open Source) | Pro Recipe |
|---|---|---|
| iOS client code | Full source | Enhanced version |
| Backend implementation | — | Hono routes, DB schema, webhooks |
| Integration guides | — | End-to-end setup checklists |
| Compliance templates | — | Privacy manifest, App Store labels |
| Known pitfalls | — | 10+ battle-tested tips per recipe |

More Pro recipes coming soon: **Push Notifications**, **Analytics Dashboard**.

See [pricing](https://shipswift.app/#pricing) for details.

---

## Tech Stack

- SwiftUI + Swift
- StoreKit 2
- Amplify SDK (Cognito)
- AVFoundation + Vision
- SpriteKit
- VolcEngine ASR

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- All comments and documentation in English
- All types use the `SW` prefix
- Each file in `SWAnimation/`, `SWChart/`, and `SWComponent/` must be self-contained
- Follow existing code patterns and naming conventions

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Star History

<a href="https://www.star-history.com/?repos=signerlabs%2FShipSwift&type=timeline&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=signerlabs/ShipSwift&type=timeline&theme=dark&legend=bottom-right" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=signerlabs/ShipSwift&type=timeline&legend=bottom-right" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=signerlabs/ShipSwift&type=timeline&legend=bottom-right" />
 </picture>
</a>

---

<div align="center">

Made with ❤️ by [SignerLabs](https://github.com/signerlabs)

</div>
```

## File: `SWSecrets.swift.example`
```
// Copy this file as SWSecrets.swift and fill in your credentials
// SWSecrets.swift is gitignored — never commit real credentials

//enum SWSecrets {
//    enum TikTok {
//        static let appId = "YOUR_APP_STORE_ID"
//        static let tiktokAppId = "YOUR_TIKTOK_APP_ID"
//        static let accessToken = "YOUR_ACCESS_TOKEN"
//    }
//}
```

## File: `glama.json`
```json
{
  "$schema": "https://glama.ai/mcp/schemas/server.json",
  "maintainers": [
    "w-zhong"
  ]
}
```

## File: `ShipSwift/Info.plist`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>SKAdNetworkItems</key>
	<array>
		<dict>
			<key>SKAdNetworkIdentifier</key>
			<string>mj797d8u6f.skadnetwork</string>
		</dict>
	</array>
</dict>
</plist>
```

## File: `ShipSwift/PrivacyInfo.xcprivacy`
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<!-- Cross-app tracking (TikTok ad attribution) -->
	<key>NSPrivacyTracking</key>
	<true/>

	<!-- TikTok SDK tracking domains -->
	<key>NSPrivacyTrackingDomains</key>
	<array>
		<string>analytics.tiktok.com</string>
		<string>business-api.tiktok.com</string>
	</array>

	<!-- Collected data types -->
	<key>NSPrivacyCollectedDataTypes</key>
	<array>
		<!-- Email Address — used for Cognito account authentication -->
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypeEmailAddress</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<true/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<false/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
			</array>
		</dict>
		<!-- Purchase History — used for IAP and Pro status -->
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypePurchaseHistory</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<true/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<false/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
			</array>
		</dict>
		<!-- Device ID (IDFA/IDFV) — third-party advertising and analytics -->
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypeDeviceID</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<false/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<true/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising</string>
				<string>NSPrivacyCollectedDataTypePurposeAnalytics</string>
			</array>
		</dict>
		<!-- Product Interaction — app events for third-party advertising and analytics -->
		<dict>
			<key>NSPrivacyCollectedDataType</key>
			<string>NSPrivacyCollectedDataTypeProductInteraction</string>
			<key>NSPrivacyCollectedDataTypeLinked</key>
			<false/>
			<key>NSPrivacyCollectedDataTypeTracking</key>
			<true/>
			<key>NSPrivacyCollectedDataTypePurposes</key>
			<array>
				<string>NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising</string>
				<string>NSPrivacyCollectedDataTypePurposeAnalytics</string>
			</array>
		</dict>
	</array>

	<!-- Accessed API types -->
	<key>NSPrivacyAccessedAPITypes</key>
	<array>
		<!-- UserDefaults — store user preferences and app state -->
		<dict>
			<key>NSPrivacyAccessedAPIType</key>
			<string>NSPrivacyAccessedAPICategoryUserDefaults</string>
			<key>NSPrivacyAccessedAPITypeReasons</key>
			<array>
				<string>CA92.1</string>
			</array>
		</dict>
	</array>
</dict>
</plist>
```

## File: `ShipSwift/ShipSwift - MCP Codebase.storekit`
```
{
  "appPolicies" : {
    "eula" : "",
    "policies" : [
      {
        "locale" : "en_US",
        "policyText" : "",
        "policyURL" : ""
      }
    ]
  },
  "identifier" : "4C3F1AB8",
  "nonRenewingSubscriptions" : [

  ],
  "products" : [
    {
      "displayPrice" : "89.99",
      "familyShareable" : false,
      "internalID" : "6759789722",
      "localizations" : [
        {
          "description" : "Unlock all Pro features",
          "displayName" : "ShipSwift Pro",
          "locale" : "en_US"
        }
      ],
      "productID" : "com.signerlabs.shipswift.lifetime",
      "referenceName" : "ShipSwift Pro",
      "type" : "NonConsumable"
    }
  ],
  "settings" : {
    "_applicationInternalID" : "6759209764",
    "_askToBuyEnabled" : false,
    "_billingGracePeriodEnabled" : false,
    "_billingIssuesEnabled" : false,
    "_developerTeamID" : "5GS4D3667R",
    "_disableDialogs" : false,
    "_failTransactionsEnabled" : false,
    "_lastSynchronizedDate" : 793882906.67838395,
    "_locale" : "en_US",
    "_renewalBillingIssuesEnabled" : false,
    "_storefront" : "USA",
    "_storeKitErrors" : [

    ],
    "_timeRate" : 0
  },
  "subscriptionGroups" : [

  ],
  "version" : {
    "major" : 4,
    "minor" : 0
  }
}
```

## File: `ShipSwift/ShipSwiftApp.swift`
```
//
//  ShipSwiftApp.swift
//  ShipSwift
//
//  Created by Wei on 2025/12/15.
//

import SwiftUI
import Amplify
import AWSCognitoAuthPlugin
#if os(iOS)
import TikTokBusinessSDK
#endif

@main
struct ShipSwiftApp: App {
    @State private var storeManager = SWStoreManager.shared
    @State private var userManager = SWUserManager()
    @Environment(\.scenePhase) private var scenePhase

    init() {
        configureAmplify()
        configureStore()
        #if os(iOS)
        configureTikTok()
        #endif
    }

    var body: some Scene {
        WindowGroup {
            RootTabView()
                .environment(storeManager)
                .environment(userManager)
                .swAlert()
                #if os(macOS)
                .frame(minWidth: 900, minHeight: 600)
                #endif
        }
        #if os(macOS)
        .defaultSize(width: 1100, height: 700)
        #endif
        #if os(iOS)
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .active {
                SWTikTokTrackingManager.shared.requestTrackingAuthorization()
            }
        }
        #endif
    }

    private func configureAmplify() {
        do {
            try Amplify.add(plugin: AWSCognitoAuthPlugin())
            try Amplify.configure(with: .amplifyOutputs)
        } catch {
            swDebugLog("Failed to configure Amplify: \(error)")
        }
    }

    #if os(iOS)
    private func configureTikTok() {
        guard let config = TikTokConfig(
            accessToken: SWSecrets.TikTok.accessToken,
            appId: SWSecrets.TikTok.appId,
            tiktokAppId: SWSecrets.TikTok.tiktokAppId
        ) else { return }
        #if DEBUG
        config.enableDebugMode()
        #endif
        TikTokBusiness.initializeSdk(config)

        SWTikTokTrackingManager.shared.configure { eventName, properties in
            let event = TikTokBaseEvent(eventName: eventName)
            properties?.forEach { event.addProperty(withKey: $0.key, value: $0.value) }
            TikTokBusiness.trackTTEvent(event)
        }
    }
    #endif

    private func configureStore() {
        storeManager.config.lifetimeProductID = "com.signerlabs.shipswift.lifetime"
        storeManager.config.title = "ShipSwift Pro"
        storeManager.config.privacyPolicyURL = "https://shipswift.app/privacy"
        storeManager.config.termsOfServiceURL = "https://shipswift.app/terms"
        storeManager.config.features = [
            .init(icon: "cpu.fill", text: "AI-optimized recipes for Claude, Cursor & Windsurf"),
            .init(icon: "checkmark.seal.fill", text: "Full-stack iOS + AWS backend, battle-tested"),
            .init(icon: "terminal.fill", text: "One MCP command — zero downloads, instant access"),
            .init(icon: "arrow.triangle.branch", text: "Lifetime updates & new recipes included"),
        ]
    }
}
```

## File: `ShipSwift/amplify_outputs.json`
```json
{
  "$schema": "https://raw.githubusercontent.com/aws-amplify/amplify-backend/main/packages/client-config/src/client-config-schema/schema_v1.json",
  "version": "1",
  "auth": {
    "user_pool_id": "us-east-1_PzjrkPUOG",
    "user_pool_client_id": "2bfom9s38ev1avsiuekcb3j2ps",
    "aws_region": "us-east-1"
  }
}
```

## File: `ShipSwift/Assets.xcassets/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/AccentColor.colorset/Contents.json`
```json
{
  "colors" : [
    {
      "color" : {
        "color-space" : "display-p3",
        "components" : {
          "alpha" : "1.000",
          "blue" : "0x3E",
          "green" : "0x46",
          "red" : "0x31"
        }
      },
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/AppIcon.appiconset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Logo (2).png",
      "idiom" : "universal",
      "platform" : "ios",
      "size" : "1024x1024"
    },
    {
      "filename" : "AppIcon-16 1.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "16x16"
    },
    {
      "filename" : "AppIcon-32 1.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "16x16"
    },
    {
      "filename" : "AppIcon-32 2.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "32x32"
    },
    {
      "filename" : "AppIcon-64 1.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "32x32"
    },
    {
      "filename" : "AppIcon-128 1.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "128x128"
    },
    {
      "filename" : "AppIcon-256 1.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "128x128"
    },
    {
      "filename" : "AppIcon-256 2.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "256x256"
    },
    {
      "filename" : "AppIcon-512 1.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "256x256"
    },
    {
      "filename" : "AppIcon-512 2.png",
      "idiom" : "mac",
      "scale" : "1x",
      "size" : "512x512"
    },
    {
      "filename" : "Logo (2) 1.png",
      "idiom" : "mac",
      "scale" : "2x",
      "size" : "512x512"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/Chocolate.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "2.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/Latte.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "1.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/Matcha.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "3.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/airpods.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "airpods.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/business-shoes.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "bussiness-shoes.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/face-picture.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "照片.png",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/golf-gloves.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "golf-gloves.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/keys.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "keys.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/smile-after.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "smile-after.png",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/smile-before.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "smile-before.png",
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/suit.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "suit.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/sunglasses.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "sunglasses.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/tshirt.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "tshirt.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Demo Image/wide-brimmed-hat.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "wide-brimmed-hat.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/Brushmo Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "icon.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/Fullpack Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Logo (7).png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/Journey Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Journey Logo.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/Lifebang Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "logo-lifebang.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/ShipSwift Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Logo (2).png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/SmileMax Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Logo.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Logo/UtilityMax Logo.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "1.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Welcome Image/Contents.json`
```json
{
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Welcome Image/welcome-0.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "welcome-0.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Welcome Image/welcome-1.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "welcome-1.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Welcome Image/welcome-2.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "Frame 705.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Assets.xcassets/Welcome Image/welcome-3.imageset/Contents.json`
```json
{
  "images" : [
    {
      "filename" : "welcome-3.png",
      "idiom" : "universal",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "scale" : "3x"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
```

## File: `ShipSwift/Component/ListItem.swift`
```
//
//  ListItem.swift
//  ShipSwift
//
//  Created by Wei Zhong on 13/2/26.
//

import SwiftUI

struct ListItem: View {
    let title: String
    let icon: String
    let description: String

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Label(title, systemImage: icon)

            Text(description)
                .font(.caption)
                .foregroundStyle(.secondary)
        }
    }
}

#Preview {
    List {
        ListItem(
            title: "Before / After",
            icon: "slider.horizontal.below.rectangle",
            description: "Image comparison view with auto-oscillating slider and drag gesture."
        )
    }
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWAnimatedMeshGradient.swift`
```
//
//  SWAnimatedMeshGradient.swift
//  ShipSwift
//
//  Animated 3x3 mesh gradient background that smoothly transitions between
//  two color palettes using a repeating easeInOut animation. Designed as a
//  full-screen or section background layer.
//
//  Usage:
//    // Default indigo/blue/cyan palette
//    ZStack {
//        SWAnimatedMeshGradient()
//            .ignoresSafeArea()
//        // Your content here
//    }
//
//    // As a section background
//    myContent
//        .background { SWAnimatedMeshGradient() }
//
//    // Custom color palette
//    SWAnimatedMeshGradient(
//        paletteA: [
//            .red.opacity(0.9),  .orange.opacity(0.85), .yellow.opacity(0.8),
//            .orange.opacity(0.85), .red.opacity(0.9),  .orange.opacity(0.85),
//            .yellow.opacity(0.8),  .orange.opacity(0.85), .red.opacity(0.9)
//        ],
//        paletteB: [
//            .yellow.opacity(0.8),  .red.opacity(0.9),    .orange.opacity(0.85),
//            .red.opacity(0.85),    .orange.opacity(0.9),  .yellow.opacity(0.85),
//            .orange.opacity(0.85), .yellow.opacity(0.8),  .red.opacity(0.9)
//        ]
//    )
//
//    // Custom animation duration
//    SWAnimatedMeshGradient(duration: 8.0)
//
//  Parameters:
//    - paletteA: First 9-color array for the 3x3 mesh (row-major order)
//    - paletteB: Second 9-color array to transition to
//    - duration: Animation cycle duration in seconds (default 5.0)
//
//  Notes:
//    - Both palettes must contain exactly 9 colors for the 3x3 grid
//    - The animation auto-reverses, creating a seamless loop
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWAnimatedMeshGradient: View {
    /// First color palette (9 colors, 3x3 grid, row-major order)
    var paletteA: [Color] = [
        .indigo.opacity(0.9),  .blue.opacity(0.85),   .cyan.opacity(0.8),
        .blue.opacity(0.85),   .indigo.opacity(0.9),  .blue.opacity(0.85),
        .cyan.opacity(0.8),    .blue.opacity(0.85),   .indigo.opacity(0.9)
    ]

    /// Second color palette (9 colors, 3x3 grid, row-major order)
    var paletteB: [Color] = [
        .cyan.opacity(0.8),    .indigo.opacity(0.9),  .blue.opacity(0.85),
        .indigo.opacity(0.85), .blue.opacity(0.9),    .cyan.opacity(0.85),
        .blue.opacity(0.85),   .cyan.opacity(0.8),    .indigo.opacity(0.9)
    ]

    /// Animation cycle duration in seconds
    var duration: Double = 5.0

    @State private var appear = false

    var body: some View {
        MeshGradient(width: 3, height: 3, points: [
            .init(0, 0), .init(0.5, 0), .init(1, 0),
            .init(0, 0.5), .init(0.5, 0.5), .init(1, 0.5),
            .init(0, 1), .init(0.5, 1), .init(1, 1)
        ], colors: appear ? paletteA : paletteB)
        .onAppear {
            withAnimation(.easeInOut(duration: duration).repeatForever(autoreverses: true)) {
                appear = true
            }
        }
    }
}

// MARK: - Preview

#Preview("Default") {
    SWAnimatedMeshGradient()
        .ignoresSafeArea()
}

#Preview("Custom Palette") {
    SWAnimatedMeshGradient(
        paletteA: [
            .red.opacity(0.9),  .orange.opacity(0.85), .yellow.opacity(0.8),
            .orange.opacity(0.85), .red.opacity(0.9),  .orange.opacity(0.85),
            .yellow.opacity(0.8),  .orange.opacity(0.85), .red.opacity(0.9)
        ],
        paletteB: [
            .yellow.opacity(0.8),  .red.opacity(0.9),    .orange.opacity(0.85),
            .red.opacity(0.85),    .orange.opacity(0.9),  .yellow.opacity(0.85),
            .orange.opacity(0.85), .yellow.opacity(0.8),  .red.opacity(0.9)
        ],
        duration: 3.0
    )
    .ignoresSafeArea()
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWBeforeAfterSlider.swift`
```
//
//  SWBeforeAfterSlider.swift
//  ShipSwift
//
//  Before/after image comparison view with an auto-oscillating slider
//  divider. The slider sweeps back and forth to reveal the "before" and
//  "after" images, with optional Before/After labels.
//
//  Usage:
//    // Basic usage with two images
//    SWBeforeAfterSlider(
//        before: Image("photo_before"),
//        after: Image("photo_after")
//    )
//
//    // Customized size, aspect ratio, and animation speed
//    SWBeforeAfterSlider(
//        before: Image("old"),
//        after: Image("new"),
//        width: 300,               // default 360
//        aspectRatio: 16.0 / 9.0,  // default 3/4 (portrait)
//        cornerRadius: 16,         // default 24
//        speed: 1.2,               // oscillation speed, default 0.8
//        showLabels: false,         // hide Before/After labels
//        beforeLabel: "Old",        // custom label text, default "Before"
//        afterLabel: "New"          // custom label text, default "After"
//    )
//
//    // Supports drag gesture — drag the slider to compare manually,
//    // auto-animation resumes seamlessly after release.
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWBeforeAfterSlider: View {
    let before: Image
    let after: Image
    var width: CGFloat = 360
    var aspectRatio: CGFloat = 3.0 / 4.0
    var cornerRadius: CGFloat = 24
    var speed: Double = 0.8
    var showLabels: Bool = true
    var beforeLabel: String = "Before"
    var afterLabel: String = "After"

    private var height: CGFloat { width / aspectRatio }

    @State private var startDate = Date.now
    @State private var isDragging = false
    @State private var dragSliderPos: CGFloat = 0.5

    var body: some View {
        TimelineView(.animation(paused: isDragging)) { timeline in
            let sliderPos: CGFloat = isDragging
                ? dragSliderPos
                : 0.5 + sin(timeline.date.timeIntervalSince(startDate) * speed) * 0.3
            let sliderX = sliderPos * width

            ZStack {
                // Bottom layer (Before)
                before
                    .resizable()
                    .scaledToFill()
                    .frame(width: width, height: height)
                    .clipShape(RoundedRectangle(cornerRadius: cornerRadius))

                // Top layer (After) - clipped by mask
                after
                    .resizable()
                    .scaledToFill()
                    .frame(width: width, height: height)
                    .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
                    .mask(
                        HStack(spacing: 0) {
                            Rectangle()
                                .frame(width: sliderX)
                            Spacer(minLength: 0)
                        }
                        .frame(width: width)
                    )

                // Divider line
                Rectangle()
                    .fill(.ultraThinMaterial)
                    .frame(width: 3, height: height)
                    .offset(x: sliderX - width / 2)

                // Slider handle
                Image(systemName: "arrow.left.and.right.circle.fill")
                    .font(.largeTitle)
                    .foregroundStyle(
                        .tertiary,
                        .white.opacity(0.8)
                    )
                    .offset(x: sliderX - width / 2)

                // Before / After labels
                if showLabels {
                    HStack {
                        labelTag(beforeLabel)
                            .padding(12)
                        Spacer()
                        labelTag(afterLabel)
                            .padding(12)
                    }
                    .frame(width: width, height: height, alignment: .bottom)
                }
            }
            .contentShape(Rectangle())
            .gesture(dragGesture)
        }
    }

    private func labelTag(_ text: String) -> some View {
        Text(text)
            .font(.caption)
            .fontWeight(.medium)
            .foregroundStyle(.white)
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(.ultraThinMaterial, in: Capsule())
    }

    private var dragGesture: some Gesture {
        DragGesture(minimumDistance: 0)
            .onChanged { value in
                if !isDragging { isDragging = true }
                dragSliderPos = min(max(value.location.x / width, 0.05), 0.95)
            }
            .onEnded { _ in
                // Resume auto-animation from the current drag position
                let normalized = min(max((dragSliderPos - 0.5) / 0.3, -1.0), 1.0)
                let phase = Double(asin(normalized)) / speed
                startDate = Date.now.addingTimeInterval(-phase)
                isDragging = false
            }
    }
}

// MARK: - Preview

#Preview {
    SWBeforeAfterSlider(
        before: Image(.smileBefore),
        after: Image(.smileAfter)
    )
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWGlowSweep.swift`
```
//
//  SWGlowSweep.swift
//  ShipSwift
//
//  View wrapper that replaces the content's appearance with a base color and sweeps
//  a glowing highlight band across it. The original content shape is used as a mask,
//  making it ideal for text, icons, and SF Symbols.
//
//  Usage:
//    // Default gray base with white glow sweep effect
//    SWGlowSweep {
//        Text("Start Scan Today")
//            .font(.largeTitle.bold())
//    }
//
//    // Custom colors and speed
//    SWGlowSweep(baseColor: .blue.opacity(0.6), glowColor: .cyan) {
//        Image(systemName: "waveform.circle.fill")
//            .font(.system(size: 80))
//    }
//
//    // Fully custom parameters
//    SWGlowSweep(
//        baseColor: .accentColor,
//        glowColor: .white,
//        duration: 1.5,
//        bandWidth: 200
//    ) {
//        Text("Analyzing...")
//            .font(.title2.bold())
//    }
//
//  Parameters:
//    - baseColor: Color     — Base fill color (default .gray)
//    - glowColor: Color     — Highlight glow color (default .white)
//    - duration: Double     — Single sweep cycle in seconds (default 2.0)
//    - bandWidth: CGFloat   — Light band width in points (default 150)
//    - content: @ViewBuilder — View content to apply the effect on
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWGlowSweep

struct SWGlowSweep<Content: View>: View {
    @State private var animate = false

    var baseColor: Color = .gray
    var glowColor: Color = .white
    var duration: Double = 2.0
    var bandWidth: CGFloat = 150

    @ViewBuilder let content: () -> Content

    init(
        baseColor: Color = .gray,
        glowColor: Color = .white,
        duration: Double = 2.0,
        bandWidth: CGFloat = 150,
        @ViewBuilder content: @escaping () -> Content
    ) {
        self.baseColor = baseColor
        self.glowColor = glowColor
        self.duration = duration
        self.bandWidth = bandWidth
        self.content = content
    }

    var body: some View {
        let inner = content()
        inner
            .hidden()
            .overlay {
                GeometryReader { geo in
                    let totalWidth = geo.size.width

                    Rectangle()
                        .fill(baseColor)
                        .overlay {
                            LinearGradient(
                                colors: [.clear, glowColor, .clear],
                                startPoint: .leading,
                                endPoint: .trailing
                            )
                            .frame(width: bandWidth)
                            .offset(x: animate ? totalWidth / 2 + bandWidth : -totalWidth / 2 - bandWidth)
                        }
                        .animation(
                            .linear(duration: duration)
                            .repeatForever(autoreverses: false),
                            value: animate
                        )
                        .mask { inner }
                }
            }
            .onAppear {
                animate = true
            }
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 26) {
        SWGlowSweep {
            Text("Start Scan Today")
                .font(.largeTitle.bold())
        }
        
        SWGlowSweep(baseColor: .accentColor, glowColor: .white, duration: 1.5) {
            Text("Analyzing...")
                .font(.title2.bold())
        }
        
        SWGlowSweep(baseColor: .green.opacity(0.7), glowColor: .black) {
            Text("Processing")
                .font(.headline)
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWLightSweep.swift`
```
//
//  SWLightSweep.swift
//  ShipSwift
//
//  Animated scan-line overlay View wrapper that sweeps a gradient light band
//  across any content. The content is clipped to a rounded rectangle and the
//  light band loops indefinitely.
//
//  Usage:
//    // Wrap any view with a light sweep effect
//    SWLightSweep {
//        Image("photo")
//            .resizable()
//            .frame(width: 300, height: 200)
//    }
//
//    // Custom light band width, speed, color, and corner radius
//    SWLightSweep(
//        lineWidth: 120,
//        duration: 2.0,
//        lineColor: .blue.opacity(0.4),
//        cornerRadius: 20
//    ) {
//        Rectangle()
//            .fill(.gray)
//            .frame(width: 300, height: 200)
//    }
//
//  Parameters:
//    - lineWidth: CGFloat    — Scan light band width (default 80)
//    - duration: Double      — Single scan duration in seconds (default 1.5)
//    - lineColor: Color      — Light band color (default white semi-transparent)
//    - cornerRadius: CGFloat — Clip corner radius (default 16)
//    - content: @ViewBuilder — View content to be scanned
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWLightSweep<Content: View>: View {
    @State private var animate = false

    var lineWidth: CGFloat = 80
    var duration: Double = 1.5
    var lineColor: Color = .white.opacity(0.6)
    var cornerRadius: CGFloat = 16

    @ViewBuilder let content: () -> Content

    init(
        lineWidth: CGFloat = 80,
        duration: Double = 1.5,
        lineColor: Color = .white.opacity(0.6),
        cornerRadius: CGFloat = 16,
        @ViewBuilder content: @escaping () -> Content
    ) {
        self.lineWidth = lineWidth
        self.duration = duration
        self.lineColor = lineColor
        self.cornerRadius = cornerRadius
        self.content = content
    }

    var body: some View {
        content()
            .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
            .overlay {
                GeometryReader { geo in
                    LinearGradient(
                        colors: [.clear, lineColor, .clear],
                        startPoint: .leading,
                        endPoint: .trailing
                    )
                    .frame(width: lineWidth)
                    .offset(x: animate ? geo.size.width : -lineWidth)
                    .animation(
                        .linear(duration: duration).repeatForever(autoreverses: false),
                        value: animate
                    )
                }
                .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
            }
            .onAppear {
                animate = true
            }
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 26) {
        SWLightSweep {
            Image(.smileAfter)
                .resizable()
                .scaledToFit()
                .frame(width: 180)
        }
        
        SWLightSweep(lineWidth: 120, duration: 0.5, cornerRadius: 20) {
            Image(.smileAfter)
                .resizable()
                .scaledToFit()
                .frame(width: 200)
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWOrbitingLogos.swift`
```
//
//  SWOrbitingLogos.swift
//  ShipSwift
//
//  SpriteKit-powered animated orbit component. Displays multiple concentric rings
//  of colored dots that rotate continuously. Icons from the images array are placed
//  on the outermost ring and periodically pop out with a scale animation. A custom
//  center view is rendered on top using SwiftUI.
//
//  Usage:
//    // Basic usage — array of image names + center view
//    SWOrbitingLogos(
//        images: ["icon1", "icon2", "icon3", "icon4",
//                 "icon5", "icon6", "icon7", "icon8"]
//    ) {
//        Image("AppLogo")
//            .resizable()
//            .aspectRatio(contentMode: .fill)
//            .frame(width: 60, height: 60)
//    }
//
//    // Control size (via frame constraint, component auto-scales)
//    SWOrbitingLogos(images: imageArray) {
//        Circle()
//            .fill(.blue)
//            .frame(width: 50, height: 50)
//    }
//    .frame(width: 150)
//
//    // Custom rotation speed
//    SWOrbitingLogos(images: imageArray, rotationDuration: 15) {
//        Text("Logo")
//    }
//
//  Parameters:
//    - images: [String]          — Array of asset image names (up to 8, evenly distributed on outer ring)
//    - rotationDuration: Double  — Full orbit rotation duration in seconds (default 10)
//    - center: @ViewBuilder      — SwiftUI view displayed at the center
//
//  Notes:
//    - Component maintains 1:1 aspect ratio, auto-scales via GeometryReader
//    - Base design size is 300pt, can be scaled down or up via frame
//    - 4 concentric dot rings, outer ring largest, inner ring smallest
//    - Icons take turns showing a pop-out animation then shrink back
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import SpriteKit

/// Logo display component with orbit animation
/// - Parameters:
///   - images: Array of images on the orbit (up to 8)
///   - rotationDuration: Full orbit rotation duration in seconds (default 10)
///   - center: Custom view displayed at the center
struct SWOrbitingLogos<Center: View>: View {
    let images: [String]
    var rotationDuration: Double = 10
    let center: Center

    private let baseSize: CGFloat = 300  // Base design size

    init(
        images: [String],
        rotationDuration: Double = 10,
        @ViewBuilder center: () -> Center
    ) {
        self.images = images
        self.rotationDuration = rotationDuration
        self.center = center()
    }

    var body: some View {
        GeometryReader { geo in
            let size = min(geo.size.width, geo.size.height)
            let scale = size / baseSize

            ZStack {
                SWOrbitingLogosSpriteView(
                    images: images,
                    scale: scale,
                    rotationDuration: rotationDuration
                )

                center
                    .scaleEffect(scale)
            }
            .frame(width: size, height: size)
        }
        .aspectRatio(1, contentMode: .fit)
    }
}

// MARK: - SpriteKit Bridge View

private struct SWOrbitingLogosSpriteView: View {
    let images: [String]
    let scale: CGFloat
    let rotationDuration: Double

    @State private var scene: SWOrbitingLogosScene?

    var body: some View {
        ZStack {
            if let scene {
                SpriteView(scene: scene, options: [.allowsTransparency])
            }
        }
        .onAppear {
            let newScene = SWOrbitingLogosScene()
            newScene.images = images
            newScene.scaleFactor = scale
            newScene.rotationDuration = rotationDuration
            newScene.scaleMode = .resizeFill
            scene = newScene
        }
        .onChange(of: scale) { _, newScale in
            scene?.updateScale(newScale)
        }
    }
}

// MARK: - SpriteKit Scene

private class SWOrbitingLogosScene: SKScene {
    var images: [String] = []
    var scaleFactor: CGFloat = 1.0
    var rotationDuration: Double = 10

    private let dotsPerCircle = 23
    private let numCircles = 4

    private var outerCircleDots: [SKShapeNode] = []
    private var nextIconIndex = 0
    private var originalPositions: [CGPoint] = []
    private var showingImageDot: SKShapeNode?

    private let container = SKNode()

    private let gradient: [(angle: CGFloat, color: SKColor)] = [
        (0, SKColor(red: 26/255, green: 127/255, blue: 93/255, alpha: 1)),
        (.pi / 2, SKColor(red: 52/255, green: 180/255, blue: 140/255, alpha: 1)),
        (.pi, SKColor(red: 80/255, green: 200/255, blue: 160/255, alpha: 1)),
        (3 * .pi / 2, SKColor(red: 40/255, green: 150/255, blue: 115/255, alpha: 1)),
        (2 * .pi, SKColor(red: 26/255, green: 127/255, blue: 93/255, alpha: 1))
    ]

    override func didMove(to view: SKView) {
        backgroundColor = .clear
        physicsWorld.gravity = .zero
        anchorPoint = CGPoint(x: 0.5, y: 0.5)

        addChild(container)
        container.setScale(scaleFactor)
        buildCircles()
        startRotation()
        animateNextIcon()
    }

    func updateScale(_ newScale: CGFloat) {
        scaleFactor = newScale
        container.setScale(newScale)
    }

    private func buildCircles() {
        let circles = generateCircles()
        var angleOffset: CGFloat = 0
        let step = Int(round(Double(dotsPerCircle) / Double(images.count)))

        for (circleIndex, circle) in circles.enumerated() {
            for dotIndex in 0..<dotsPerCircle {
                var angle = (2 * .pi / CGFloat(dotsPerCircle) * CGFloat(dotIndex)) + angleOffset
                if angle > 2 * .pi { angle -= 2 * .pi }

                let position = CGPoint(x: circle.radius * cos(angle), y: circle.radius * sin(angle))

                let dot = SKShapeNode(circleOfRadius: circle.size)
                dot.position = position
                dot.fillColor = getColor(for: angle)
                dot.strokeColor = .clear
                dot.name = "dot-\(circleIndex)"
                dot.physicsBody = SKPhysicsBody(circleOfRadius: circle.size + 3)
                dot.physicsBody?.isDynamic = true
                dot.physicsBody?.affectedByGravity = false

                if circleIndex == 0, dotIndex % step == 0 {
                    placeIconOnOuterCircle(for: dot)
                    outerCircleDots.append(dot)
                }

                container.addChild(dot)
                originalPositions.append(position)
            }
            angleOffset += 0.4
        }

        outerCircleDots.reverse()
    }

    private func placeIconOnOuterCircle(for dot: SKShapeNode) {
        let maskRadius: CGFloat = 40
        let mask = SKShapeNode(circleOfRadius: maskRadius)
        mask.fillColor = .white
        mask.strokeColor = .clear

        let cropNode = SKCropNode()
        cropNode.maskNode = mask
        cropNode.alpha = 0
        cropNode.name = "sprite"
        cropNode.setScale(0.25)

        let sprite = SKSpriteNode(imageNamed: images[outerCircleDots.count])
        sprite.texture?.filteringMode = .linear

        let imageSize = sprite.size
        let scale = max((maskRadius * 2) / imageSize.width, (maskRadius * 2) / imageSize.height)
        sprite.size = CGSize(width: imageSize.width * scale, height: imageSize.height * scale)

        cropNode.addChild(sprite)
        dot.addChild(cropNode)
    }

    private func startRotation() {
        container.run(.repeatForever(.rotate(byAngle: -.pi * 2, duration: rotationDuration)))
    }

    private func animateNextIcon() {
        let dot = outerCircleDots[nextIconIndex]

        dot.physicsBody = SKPhysicsBody(circleOfRadius: 10)
        dot.physicsBody?.density = 110
        dot.physicsBody?.isDynamic = false

        let scaleIcon = SKAction.run { [weak self] in
            dot.run(.sequence([
                .scale(to: 4.0 * 1.1, duration: 0.1),
                .scale(to: 4.0, duration: 0.1)
            ]))

            self?.showingImageDot = dot
            dot.fillColor = dot.fillColor.withAlphaComponent(0)

            (dot.childNode(withName: "sprite") as? SKCropNode)?.alpha = 1
        }

        let wait = SKAction.wait(forDuration: 1)

        let shrinkIcon = SKAction.run { [weak self] in
            guard let self else { return }

            let scale = SKAction.scale(to: 1.0, duration: 0.6)
            scale.timingMode = .easeIn
            dot.run(scale)

            // Image fade out with delay
            if let cropNode = dot.childNode(withName: "sprite") as? SKCropNode {
                cropNode.run(.sequence([
                    .wait(forDuration: 0.35),
                    .fadeAlpha(to: 0, duration: 0.15)
                ]))
            }

            Task { @MainActor in
                try? await Task.sleep(for: .milliseconds(200))

                // Background fade in
                for i in 1...10 {
                    try? await Task.sleep(for: .milliseconds(25))
                    guard self.showingImageDot === dot else { return }

                    let worldPos = self.container.convert(dot.position, to: self)
                    var angle = atan2(worldPos.y, worldPos.x)
                    if angle < 0 { angle += 2 * .pi }
                    dot.fillColor = self.getColor(for: angle).withAlphaComponent(CGFloat(i) / 10)
                }

                self.showingImageDot = nil
            }
        }

        let moveDots = SKAction.run { [weak self] in
            guard let self else { return }

            for (i, surroundingDot) in container.children.enumerated()
            where !surroundingDot.position.isApproximatelyEqual(to: originalPositions[i]) {
                let moveAction = SKAction.move(to: originalPositions[i], duration: 0.6)
                moveAction.timingMode = .easeIn
                surroundingDot.run(moveAction)
            }

            Task { @MainActor in
                try? await Task.sleep(for: .milliseconds(600))
                self.nextIconIndex = (self.nextIconIndex + 1) % self.outerCircleDots.count
                self.animateNextIcon()
            }
        }

        dot.run(.sequence([scaleIcon, wait, moveDots, shrinkIcon])) {
            dot.physicsBody?.isDynamic = true
        }
    }

    private func generateCircles() -> [(radius: CGFloat, size: CGFloat)] {
        var circles: [(CGFloat, CGFloat)] = []
        var dotSize = 4

        for i in 0..<numCircles {
            circles.append((CGFloat(75 + i * 15), CGFloat(dotSize)))
            dotSize += i == 0 ? 2 : (i % 2 == 0 ? 3 : -1)
        }

        return circles.reversed()
    }

    override func update(_ currentTime: TimeInterval) {
        for case let dot as SKShapeNode in container.children where dot !== showingImageDot {
            let worldPos = container.convert(dot.position, to: self)
            var angle = atan2(worldPos.y, worldPos.x)
            if angle < 0 { angle += 2 * .pi }
            dot.fillColor = getColor(for: angle)
        }

        outerCircleDots[nextIconIndex].zRotation = -container.zRotation
    }

    private func getColor(for angle: CGFloat) -> SKColor {
        guard let startIndex = gradient.lastIndex(where: { $0.angle <= angle }) else { return .white }

        let start = gradient[startIndex]
        let end = gradient[startIndex + 1]
        let percent = (angle - start.angle) / (end.angle - start.angle)

        let r = start.color.rgba.red + (end.color.rgba.red - start.color.rgba.red) * percent
        let g = start.color.rgba.green + (end.color.rgba.green - start.color.rgba.green) * percent
        let b = start.color.rgba.blue + (end.color.rgba.blue - start.color.rgba.blue) * percent

        return SKColor(red: r, green: g, blue: b, alpha: 1)
    }
}

private extension CGPoint {
    func isApproximatelyEqual(to other: CGPoint, tolerance: CGFloat = 0.01) -> Bool {
        abs(x - other.x) < tolerance && abs(y - other.y) < tolerance
    }
}

private extension SKColor {
    var rgba: (red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) {
        var r: CGFloat = 0, g: CGFloat = 0, b: CGFloat = 0, a: CGFloat = 0
        #if canImport(UIKit)
        getRed(&r, green: &g, blue: &b, alpha: &a)
        #else
        // macOS: NSColor may need conversion to sRGB color space first
        let color = usingColorSpace(.sRGB) ?? self
        color.getRed(&r, green: &g, blue: &b, alpha: &a)
        #endif
        return (r, g, b, a)
    }
}

#Preview {
    VStack {
        SWOrbitingLogos(
            images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
        ) {
            Image(.fullpackLogo)
                .resizable()
                .scaledToFit()
                .frame(width: 60, height: 60)
                .clipShape(RoundedRectangle(cornerRadius: 8))
                .offset(y: -5)
        }

        SWOrbitingLogos(
            images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
        ) {
            Circle()
                .fill(.blue)
                .frame(width: 50, height: 50)
        }
        .frame(width: 150)
    }
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWScanningOverlay.swift`
```
//
//  SWScanningOverlay.swift
//  ShipSwift
//
//  Animated scan-line overlay View wrapper that renders a flowing grid, a top-to-bottom
//  sweeping scan band, and a subtle noise layer on top of the provided content.
//  Conveys an "analyzing / processing" visual effect.
//  Uses Canvas for high-performance grid rendering.
//
//  Usage:
//    // Wrap any view with the scanning overlay
//    SWScanningOverlay {
//        Image("myPhoto")
//            .resizable()
//            .scaledToFit()
//    }
//
//    // With custom parameters
//    SWScanningOverlay(
//        gridOpacity: 0.3,        // grid line opacity (0-1), default 0.2
//        bandOpacity: 0.5,        // scan band opacity (0-1), default 0.3
//        bandHeightRatio: 0.25,   // band height relative to view, default 0.2
//        gridSpacing: 20,         // grid spacing in points, default 16
//        speed: 3.0               // scan speed multiplier, default 2.0
//    ) {
//        Image("myPhoto")
//            .resizable()
//            .scaledToFit()
//    }
//
//  Parameters:
//    - gridOpacity: Double      — Grid line opacity (0-1), default 0.2
//    - bandOpacity: Double      — Scan band opacity (0-1), default 0.3
//    - bandHeightRatio: CGFloat — Band height relative to view height, default 0.2
//    - gridSpacing: CGFloat     — Grid spacing in points, default 16
//    - speed: Double            — Scan speed multiplier (1.0 = normal), default 2.0
//    - content: @ViewBuilder    — View content to overlay the scanning effect on
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

/// Image scanning overlay component
///
/// **Features:**
/// - Dynamic grid with subtle flowing effect
/// - Top-to-bottom looping scan band
/// - Lightweight noise effect
/// - All parameters are customizable
///
/// **Performance:**
/// - Uses Canvas for grid rendering (high performance)
/// - TimelineView-driven animation (system-optimized)
/// - No external image assets required
///
struct SWScanningOverlay<Content: View>: View {
    // MARK: - Configurable Parameters

    /// Grid opacity (0-1)
    var gridOpacity: Double = 0.2

    /// Scan band opacity (0-1)
    var bandOpacity: Double = 0.3

    /// Band height ratio (relative to image height)
    var bandHeightRatio: CGFloat = 0.2

    /// Grid spacing (points)
    var gridSpacing: CGFloat = 16

    /// Scan speed multiplier (1.0 = normal speed)
    var speed: Double = 2.0

    /// Content to overlay the scanning effect on
    @ViewBuilder let content: () -> Content

    // Start time anchor so the animation always begins from a consistent position
    @State private var startDate = Date.now

    init(
        gridOpacity: Double = 0.2,
        bandOpacity: Double = 0.3,
        bandHeightRatio: CGFloat = 0.2,
        gridSpacing: CGFloat = 16,
        speed: Double = 2.0,
        @ViewBuilder content: @escaping () -> Content
    ) {
        self.gridOpacity = gridOpacity
        self.bandOpacity = bandOpacity
        self.bandHeightRatio = bandHeightRatio
        self.gridSpacing = gridSpacing
        self.speed = speed
        self.content = content
    }

    // MARK: - Body

    var body: some View {
        content()
            .overlay {
                TimelineView(.animation) { timeline in
                    let t = timeline.date.timeIntervalSince(startDate)
                    GeometryReader { geo in
                        let size = geo.size
                        ZStack {
                            // 1) Dynamic grid with subtle "flowing" motion
                            Canvas { ctx, _ in
                                let phase = CGFloat(t * 0.8)
                                let dx = sin(phase) * 3
                                let dy = cos(phase * 0.9) * 3

                                var path = Path()
                                let step = max(10, gridSpacing)

                                // Vertical lines
                                var x: CGFloat = -step
                                while x <= size.width + step {
                                    let xx = x + dx + sin((x / 80) + phase) * 1.5
                                    path.move(to: CGPoint(x: xx, y: 0))
                                    path.addLine(to: CGPoint(x: xx, y: size.height))
                                    x += step
                                }

                                // Horizontal lines
                                var y: CGFloat = -step
                                while y <= size.height + step {
                                    let yy = y + dy + cos((y / 80) + phase) * 1.5
                                    path.move(to: CGPoint(x: 0, y: yy))
                                    path.addLine(to: CGPoint(x: size.width, y: yy))
                                    y += step
                                }

                                ctx.stroke(
                                    path,
                                    with: .color(.white.opacity(gridOpacity)),
                                    lineWidth: 1
                                )
                            }
                            .blendMode(.screen)

                            // 2) Scan band (top-to-bottom loop)
                            scanBand(size: size, time: t)

                            // 3) Lightweight noise overlay for realism
                            noiseOverlay(time: t)
                                .opacity(0.06)
                                .blendMode(.overlay)
                        }
                        .compositingGroup()
                    }
                }
            }
    }

    // MARK: - Private Views

    private func scanBand(size: CGSize, time t: Double) -> some View {
        let p = CGFloat((t * (0.22 * speed)).truncatingRemainder(dividingBy: 1.0))
        let bandH = size.height * bandHeightRatio
        let y = -bandH + (size.height + bandH * 2) * p

        return ZStack {
            // Main band: bright center, fading edges
            Rectangle()
                .fill(
                    LinearGradient(
                        stops: [
                            .init(color: .clear, location: 0.0),
                            .init(color: .white.opacity(bandOpacity * 0.4), location: 0.25),
                            .init(color: .white.opacity(bandOpacity), location: 0.5),
                            .init(color: .white.opacity(bandOpacity * 0.4), location: 0.75),
                            .init(color: .clear, location: 1.0),
                        ],
                        startPoint: .top,
                        endPoint: .bottom
                    )
                )
                .frame(height: bandH)
                .position(x: size.width/2, y: y)
                .blendMode(.screen)

            // Thin highlight line for scanner effect
            Rectangle()
                .fill(Color.white.opacity(bandOpacity * 0.65))
                .frame(height: 2)
                .position(x: size.width/2, y: y)
                .blur(radius: 0.6)
                .blendMode(.screen)
        }
    }

    private func noiseOverlay(time t: Double) -> some View {
        LinearGradient(
            colors: [
                .white.opacity(0.0),
                .white.opacity(1.0),
                .white.opacity(0.0),
            ],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .scaleEffect(1.6)
        .offset(x: sin(t * 0.9) * 20, y: cos(t * 1.1) * 20)
        .blur(radius: 12)
    }
}

// MARK: - Preview

#Preview("Basic Usage") {
    VStack(spacing: 20) {
        SWScanningOverlay {
            Image(.facePicture)
                .resizable()
                .scaledToFit()
                .frame(width: 180)
                .clipShape(RoundedRectangle(cornerRadius: 12))
        }

        SWScanningOverlay(
            gridOpacity: 0.1,
            bandOpacity: 0.1,
            speed: 3.0
        ) {
            Image(.facePicture)
                .resizable()
                .scaledToFit()
                .frame(width: 200)
                .clipShape(RoundedRectangle(cornerRadius: 12))
        }
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWShakingIcon.swift`
```
//
//  SWShakingIcon.swift
//  ShipSwift
//
//  Animated icon that periodically zooms in and shakes side-to-side,
//  mimicking the iOS home-screen jiggle/notification effect. Uses
//  PhaseAnimator with a multi-step ShakePhase sequence: idle -> zoom in
//  -> three shake pairs (left/right) -> zoom out, then repeats.
//
//  Usage:
//    // SF Symbol
//    SWShakingIcon(image: Image(systemName: "bell.fill"))
//
//    // Asset image (automatically gets corner radius)
//    SWShakingIcon(image: Image(.myLogo), height: 100, cornerRadius: 16)
//
//    // Custom timing
//    SWShakingIcon(
//        image: Image(systemName: "heart.fill"),
//        height: 120,
//        idleDelay: 2.0    // seconds before each shake cycle, default 1.5
//    )
//
//  Parameters:
//    - image: Image to display (SF Symbol or asset)
//    - height: Icon height in points (default 80)
//    - cornerRadius: Corner radius for asset images (default 0, no rounding)
//    - idleDelay: Pause before each shake cycle in seconds (default 1.5)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWShakingIcon: View {
    /// Image to display (SF Symbol or asset image)
    let image: Image
    /// Icon height in points
    var height: CGFloat = 80
    /// Corner radius for asset images (0 = no rounding)
    var cornerRadius: CGFloat = 0
    /// Pause duration before each shake cycle (seconds)
    var idleDelay: Double = 1.5

    enum ShakePhase: CaseIterable {
        case idle
        case zoomIn
        case shake1L, shake1R
        case shake2L, shake2R
        case shake3L, shake3R
        case zoomOut

        var scale: Double {
            switch self {
            case .idle, .zoomOut: 1.0
            case .zoomIn, .shake1L, .shake1R, .shake2L, .shake2R, .shake3L, .shake3R: 1.1
            }
        }

        var rotation: Double {
            switch self {
            case .idle, .zoomIn, .zoomOut: 10
            case .shake1L: 12
            case .shake1R: 8
            case .shake2L: 15
            case .shake2R: 5
            case .shake3L: 12
            case .shake3R: 8
            }
        }
    }

    var body: some View {
        PhaseAnimator(ShakePhase.allCases) { phase in
            image
                .resizable()
                .scaledToFit()
                .frame(height: height)
                .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
                .scaleEffect(phase.scale)
                .rotationEffect(.degrees(phase.rotation))
        } animation: { phase in
            switch phase {
            case .idle: .easeInOut(duration: 0.01)
            case .zoomIn: .easeInOut(duration: 0.2).delay(idleDelay)
            case .shake1L, .shake1R, .shake2L, .shake2R, .shake3L, .shake3R:
                    .easeInOut(duration: 0.08)
            case .zoomOut: .easeInOut(duration: 0.2)
            }
        }
    }

}

// MARK: - Preview

#Preview {
    VStack(spacing: 40) {
        SWShakingIcon(image: Image(systemName: "apple.logo"), height: 20)
        SWShakingIcon(image: Image(.smileAfter), height: 100, cornerRadius: 8)
    }
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWShimmer.swift`
```
//
//  SWShimmer.swift
//  ShipSwift
//
//  Shimmer highlight View wrapper that sweeps a translucent light band across
//  the content in a continuous loop. Commonly used on buttons, skeleton loaders,
//  or cards to draw attention or indicate a loading state.
//
//  Usage:
//    // Apply with default timing (2s sweep, 1s pause)
//    SWShimmer {
//        Text("Upgrade Now")
//            .padding()
//            .background(.blue)
//            .clipShape(.capsule)
//    }
//
//    // Custom duration and delay
//    SWShimmer(duration: 1.5, delay: 2.0) {
//        myView
//    }
//
//  Parameters:
//    - duration: Double     — Time for the band to sweep across (seconds), default 2.0
//    - delay: Double        — Pause between sweeps (seconds), default 1.0
//    - content: @ViewBuilder — View content to apply the shimmer on
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWShimmer

struct SWShimmer<Content: View>: View {
    @State private var animate = false

    var duration: Double = 2.0
    var delay: Double = 1.0

    @ViewBuilder let content: () -> Content

    init(
        duration: Double = 2.0,
        delay: Double = 1.0,
        @ViewBuilder content: @escaping () -> Content
    ) {
        self.duration = duration
        self.delay = delay
        self.content = content
    }

    // White light band gradient
    private var gradient: LinearGradient {
        LinearGradient(
            colors: [
                .clear,
                .clear,
                .white.opacity(0.2),
                .clear,
                .clear
            ],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
    }

    var body: some View {
        content()
            .overlay {
                GeometryReader { geo in
                    let bandWidth = geo.size.width * 0.5
                    gradient
                        .frame(width: bandWidth)
                        // Start fully off-screen left, end fully off-screen right
                        .offset(x: animate ? geo.size.width + bandWidth : -bandWidth * 1.5)
                        .animation(
                            .linear(duration: duration)
                            .delay(delay)
                            .repeatForever(autoreverses: false),
                            value: animate
                        )
                }
                .clipped()
            }
            .task {
                // Delay one frame to ensure the view is fully loaded
                try? await Task.sleep(nanoseconds: 100_000_000)
                animate = true
            }
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 30) {
        // Button
        SWShimmer {
            Button {
                
            } label: {
                Text("Upgrade Now")
                    .font(.largeTitle)
                    .padding(.horizontal)
                    .padding(.vertical, 6)
            }
            .buttonStyle(.borderedProminent)
        }

        // Card
        SWShimmer {
            RoundedRectangle(cornerRadius: 12)
                .fill(.gray.opacity(0.3))
                .frame(width: 280, height: 120)
        }
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWAnimation/SWTypewriterText.swift`
```
//
//  SWTypewriterText.swift
//  ShipSwift
//
//  Typewriter text animation that cycles through an array of strings,
//  typing and deleting characters one by one with configurable animation
//  styles. Ideal for landing page headlines, onboarding prompts, and
//  AI chat UIs.
//
//  Usage:
//    // Basic — cycles through texts with default spring animation
//    SWTypewriterText(texts: ["Hello World", "Welcome Back", "Let's Go"])
//
//    // Choose an animation style (SWTypewriterStyle):
//    //   .none, .spring, .blur, .fade, .scale, .wave
//    SWTypewriterText(texts: ["Line 1", "Line 2"], animationStyle: .blur)
//
//    // Convenience factory methods
//    SWTypewriterText.spring(texts: ["A", "B"])
//    SWTypewriterText.blur(texts: ["A", "B"])
//    SWTypewriterText.fade(texts: ["A", "B"])
//    SWTypewriterText.scale(texts: ["A", "B"])
//
//    // Custom gradient and timing
//    SWTypewriterText(
//        texts: ["Message 1", "Message 2"],
//        typingSpeed: 0.05,       // seconds per character typed
//        deletingSpeed: 0.03,     // seconds per character deleted
//        pauseDuration: 3.0,      // seconds to hold completed text
//        animationStyle: .spring,
//        gradient: LinearGradient(
//            colors: [.pink, .orange],
//            startPoint: .leading,
//            endPoint: .trailing
//        )
//    )
//    .font(.title3.weight(.semibold))
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWTypewriterStyle

/// Animation style applied to each character during type/delete
enum SWTypewriterStyle: Sendable {
    case none       // No animation, plain typewriter
    case spring     // Spring effect: characters bounce in/out
    case blur       // Blur effect: characters transition from blurry to clear
    case fade       // Fade effect: characters fade in/out with slide
    case scale      // Scale effect: characters grow/shrink
    case wave       // Wave effect: characters have vertical oscillation
}

// MARK: - SWTypewriterText

/// Typewriter text component
///
/// Prints text character by character, supporting multiple texts in a cycle with smooth animations.
/// Ideal for landing page headlines, AI chat, onboarding prompts, etc.
///
/// ## Usage
///
/// ```swift
/// // Basic usage
/// SWTypewriterText(texts: ["Hello World", "Welcome Back", "Let's Go"])
///
/// // Custom gradient
/// SWTypewriterText(
///     texts: ["Message 1", "Message 2"],
///     gradient: LinearGradient(colors: [.pink, .orange], startPoint: .leading, endPoint: .trailing)
/// )
///
/// // Custom animation style
/// SWTypewriterText(
///     texts: ["Message 1", "Message 2"],
///     animationStyle: .blur
/// )
///
/// // Full parameters
/// SWTypewriterText(
///     texts: ["Message 1", "Message 2"],
///     typingSpeed: 0.05,      // Typing speed (seconds per character)
///     deletingSpeed: 0.03,    // Deleting speed (seconds per character)
///     pauseDuration: 3.0,     // Pause duration (seconds)
///     animationStyle: .spring,
///     gradient: LinearGradient(colors: [.cyan, .purple], startPoint: .leading, endPoint: .trailing)
/// )
/// .font(.title3.weight(.semibold))
/// ```
///
/// ## Animation Styles (SWTypewriterStyle)
///
/// | Style     | Insertion          | Removal            |
/// |-----------|--------------------|--------------------|
/// | `.none`   | No animation       | No animation       |
/// | `.spring` | Bounce in + fade   | Shrink + fade out  |
/// | `.blur`   | Blur -> clear      | Blur + fade out    |
/// | `.fade`   | Slide down + fade  | Slide down + fade  |
/// | `.scale`  | Scale down + fade  | Scale up + fade    |
/// | `.wave`   | Drop in + fade     | Drop out + fade    |
///
/// ## Parameters
/// - `texts`: Array of texts to cycle through
/// - `typingSpeed`: Interval per character when typing (seconds), default 0.04
/// - `deletingSpeed`: Interval per character when deleting (seconds), default 0.03
/// - `pauseDuration`: How long to display completed text (seconds), default 2.5
/// - `animationStyle`: Animation style, default `.spring`
/// - `gradient`: Text gradient, default cyan -> purple
///
/// ## Notes
/// - The component loops infinitely
/// - Pair with `.font()` modifier to set size and weight
/// - Uses an invisible `|` character as height placeholder to prevent layout jumps

struct SWTypewriterText: View {
    let texts: [String]
    var typingSpeed: Double = 0.04
    var deletingSpeed: Double = 0.03
    var pauseDuration: Double = 2.5
    var animationStyle: SWTypewriterStyle = .spring
    var gradient: LinearGradient = LinearGradient(
        colors: [.cyan, .purple],
        startPoint: .leading,
        endPoint: .trailing
    )

    @State private var displayedText = ""
    @State private var currentIndex = 0
    @State private var isDeleting = false
    @State private var charStates: [SWTypewriterTextCharState] = []
    @State private var isActive = false

    var body: some View {
        HStack(spacing: 0) {
            // Character-level animation
            HStack(spacing: 0) {
                ForEach(charStates) { state in
                    Text(state.character)
                        .foregroundStyle(gradient)
                        .transition(transitionForStyle)
                }
            }
            .animation(animationForCurrentAction, value: charStates.count)

            // Invisible height placeholder to prevent layout jumps
            Text("|")
                .foregroundStyle(.clear)
        }
        .onAppear {
            isActive = true
            displayedText = ""
            charStates = []
            currentIndex = 0
            isDeleting = false
            startTyping()
        }
        .onDisappear {
            isActive = false
        }
    }

    // MARK: - Transition Configuration

    private var transitionForStyle: AnyTransition {
        switch animationStyle {
        case .none:
            return .identity

        case .spring:
            return .asymmetric(
                insertion: .scale(scale: 0.3).combined(with: .opacity),
                removal: .scale(scale: 0.3).combined(with: .opacity)
            )

        case .blur:
            return .asymmetric(
                insertion: .opacity.combined(with: .typewriterBlur),
                removal: .opacity.combined(with: .typewriterBlur)
            )

        case .fade:
            return .asymmetric(
                insertion: .move(edge: .top).combined(with: .opacity),
                removal: .move(edge: .bottom).combined(with: .opacity)
            )

        case .scale:
            return .asymmetric(
                insertion: .scale(scale: 1.5).combined(with: .opacity),
                removal: .scale(scale: 1.5).combined(with: .opacity)
            )

        case .wave:
            return .asymmetric(
                insertion: .offset(y: -8).combined(with: .opacity),
                removal: .offset(y: 8).combined(with: .opacity)
            )
        }
    }

    private var animationForCurrentAction: Animation {
        if isDeleting {
            switch animationStyle {
            case .none: return .linear(duration: 0)
            case .spring: return .easeOut(duration: 0.15)
            case .blur: return .easeOut(duration: 0.12)
            case .fade: return .easeOut(duration: 0.12)
            case .scale: return .easeOut(duration: 0.12)
            case .wave: return .easeOut(duration: 0.12)
            }
        } else {
            switch animationStyle {
            case .none: return .linear(duration: 0)
            case .spring: return .spring(response: 0.3, dampingFraction: 0.6)
            case .blur: return .easeOut(duration: 0.2)
            case .fade: return .easeOut(duration: 0.2)
            case .scale: return .spring(response: 0.25, dampingFraction: 0.7)
            case .wave: return .easeInOut(duration: 0.15)
            }
        }
    }

    // MARK: - Typing Logic

    private func startTyping() {
        guard !texts.isEmpty, isActive else { return }
        typeNextCharacter()
    }

    private func typeNextCharacter() {
        guard isActive else { return }

        let currentText = texts[currentIndex]

        if isDeleting {
            if charStates.isEmpty {
                // All characters deleted, switch to next text
                isDeleting = false
                displayedText = ""
                currentIndex = (currentIndex + 1) % texts.count
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) { [self] in
                    guard isActive else { return }
                    typeNextCharacter()
                }
            } else {
                // Remove last character
                DispatchQueue.main.asyncAfter(deadline: .now() + deletingSpeed) { [self] in
                    guard isActive else { return }
                    if !charStates.isEmpty {
                        _ = charStates.removeLast()
                        displayedText = String(displayedText.dropLast())
                    }
                    typeNextCharacter()
                }
            }
        } else {
            if displayedText.count < currentText.count {
                let charIndex = currentText.index(currentText.startIndex, offsetBy: displayedText.count)
                let newChar = currentText[charIndex]

                DispatchQueue.main.asyncAfter(deadline: .now() + typingSpeed) { [self] in
                    guard isActive else { return }
                    displayedText.append(newChar)
                    charStates.append(SWTypewriterTextCharState(character: String(newChar)))
                    typeNextCharacter()
                }
            } else {
                // Typing complete, wait before deleting
                DispatchQueue.main.asyncAfter(deadline: .now() + pauseDuration) { [self] in
                    guard isActive else { return }
                    isDeleting = true
                    typeNextCharacter()
                }
            }
        }
    }
}

// MARK: - Character State

private struct SWTypewriterTextCharState: Identifiable, Equatable {
    let id = UUID()
    var character: String
}

// MARK: - Custom Blur Transition

fileprivate extension AnyTransition {
    static var typewriterBlur: AnyTransition {
        .modifier(
            active: SWBlurModifier(radius: 10, opacity: 0),
            identity: SWBlurModifier(radius: 0, opacity: 1)
        )
    }
}

private struct SWBlurModifier: ViewModifier {
    let radius: CGFloat
    let opacity: Double

    func body(content: Content) -> some View {
        content
            .blur(radius: radius)
            .opacity(opacity)
    }
}

// MARK: - Convenience Initializers

extension SWTypewriterText {
    /// Spring style (recommended)
    static func spring(texts: [String]) -> SWTypewriterText {
        SWTypewriterText(texts: texts, animationStyle: .spring)
    }

    /// Blur style
    static func blur(texts: [String]) -> SWTypewriterText {
        SWTypewriterText(texts: texts, animationStyle: .blur)
    }

    /// Scale style
    static func scale(texts: [String]) -> SWTypewriterText {
        SWTypewriterText(texts: texts, animationStyle: .scale)
    }

    /// Fade style
    static func fade(texts: [String]) -> SWTypewriterText {
        SWTypewriterText(texts: texts, animationStyle: .fade)
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 26) {
        SWTypewriterText(
            texts: [
                "Level up your smile game",
                "AI-powered smile analysis",
                "Join the glow up era"
            ],
            animationStyle: .spring
        )
        .font(.title3.weight(.semibold))
        
        SWTypewriterText(
            texts: [
                "Level up your smile game",
                "AI-powered smile analysis",
                "Join the glow up era"
            ],
            animationStyle: .blur
        )
        .font(.title3.weight(.semibold))
        
        SWTypewriterText(
            texts: [
                "Hello World",
                "Welcome Back",
                "Let's Go"
            ],
            animationStyle: .spring,
            gradient: LinearGradient(
                colors: [.pink, .orange],
                startPoint: .leading,
                endPoint: .trailing
            )
        )
        .font(.title.weight(.bold))
    }
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .background(Color.black)
}
```

## File: `ShipSwift/SWPackage/SWChart/SWActivityHeatmap.swift`
```
//
//  SWActivityHeatmap.swift
//  ShipSwift
//
//  GitHub-style activity heatmap with streak tracking. Contains three sub-components
//  under the SWActivityHeatmap enum: StreakCard, HeatmapGrid, and HeatmapLegend.
//  Also provides a static calculateStreak(from:) method and StreakInfo model.
//
//  Usage:
//    // 1. Prepare timestamp data
//    let timestamps: [Date] = [Date(), /* ... historical check-in dates ... */]
//
//    // 2. Combine three sub-components in a Form/List
//    Form {
//        // Consecutive check-in days card
//        Section {
//            SWActivityHeatmap.StreakCard(
//                streaks: timestamps,
//                currentStreakTitle: "Current Streak",
//                colors: [.blue, .purple]
//            )
//        }
//        .listRowInsets(EdgeInsets())
//
//        // Heatmap grid
//        Section {
//            SWActivityHeatmap.HeatmapGrid(
//                timestamps: timestamps,
//                days: 60,
//                baseColor: .green,
//                itemSize: 20,
//                spacing: 3
//            )
//        } header: {
//            Text("Past 60 days")
//        } footer: {
//            // Legend
//            SWActivityHeatmap.HeatmapLegend(
//                baseColor: .green,
//                lessText: "Less",
//                moreText: "More"
//            )
//        }
//    }
//
//    // 3. Calculate streak independently
//    let info = SWActivityHeatmap.calculateStreak(from: timestamps)
//    print(info.currentStreak)    // Consecutive days
//    print(info.displayText())    // Description text
//
//  Sub-components:
//    - StreakCard    — Gradient background streak display card
//    - HeatmapGrid  — Flow-layout activity heatmap grid
//    - HeatmapLegend — Less/More color legend
//    - StreakInfo    — Streak info model (currentStreak, startDate, displayText())
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

/// Activity heatmap component collection
enum SWActivityHeatmap {

    // MARK: - Streak Info

    /// Consecutive streak information
    struct StreakInfo {
        /// Current consecutive days
        let currentStreak: Int
        /// Start date
        let startDate: Date?

        /// Generate description text
        func displayText(
            noRecordsText: String = "No records yet. Start today!",
            startedTodayText: String = "Started today. Keep it up!",
            recordedYesterdayText: String = "You recorded yesterday. Continue today to keep the streak!"
        ) -> String {
            guard currentStreak > 0 else {
                return noRecordsText
            }

            if currentStreak == 1 {
                let calendar = Calendar.current
                if let startDate = startDate, calendar.isDateInToday(startDate) {
                    return startedTodayText
                } else {
                    return recordedYesterdayText
                }
            }

            guard let startDate = startDate else {
                return "Current streak started \(currentStreak) days ago."
            }

            let calendar = Calendar.current
            let days = calendar.dateComponents([.day], from: startDate, to: Date()).day ?? 0

            if days == 0 {
                return "Current streak started today."
            } else if days == 1 {
                return "Current streak started yesterday."
            } else if days < 7 {
                return "Current streak started \(days) days ago."
            } else if days < 30 {
                let weeks = days / 7
                return "Current streak started \(weeks) week\(weeks == 1 ? "" : "s") ago."
            } else {
                let months = days / 30
                return "Current streak started \(months) month\(months == 1 ? "" : "s") ago."
            }
        }
    }

    // MARK: - Streak Calculation

    /// Calculate consecutive streak days
    /// - Parameter timestamps: Array of timestamps
    /// - Returns: Streak information
    static func calculateStreak(from timestamps: [Date]) -> StreakInfo {
        guard !timestamps.isEmpty else {
            return StreakInfo(currentStreak: 0, startDate: nil)
        }

        let calendar = Calendar.current
        let today = calendar.startOfDay(for: Date())

        // Group by date
        var recordsByDay: Set<Date> = []
        for timestamp in timestamps {
            let day = calendar.startOfDay(for: timestamp)
            recordsByDay.insert(day)
        }

        // Sort in descending order (most recent first)
        let sortedDays = recordsByDay.sorted(by: >)

        // Filter out future dates
        let validDays = sortedDays.filter { $0 <= today }

        guard let mostRecentDay = validDays.first else {
            return StreakInfo(currentStreak: 0, startDate: nil)
        }

        let daysSinceMostRecent = calendar.dateComponents([.day], from: mostRecentDay, to: today).day ?? 0

        // If the most recent record is more than 1 day ago, the streak is broken
        if daysSinceMostRecent > 1 {
            return StreakInfo(currentStreak: 0, startDate: nil)
        }

        // Calculate consecutive days
        var currentStreak = 1
        var streakStartDate = mostRecentDay
        var expectedDate = calendar.date(byAdding: .day, value: -1, to: mostRecentDay)!

        for day in validDays.dropFirst() {
            let dayDifference = calendar.dateComponents([.day], from: expectedDate, to: day).day ?? 999

            if dayDifference == 0 {
                currentStreak += 1
                streakStartDate = day
                expectedDate = calendar.date(byAdding: .day, value: -1, to: expectedDate)!
            } else {
                break
            }
        }

        return StreakInfo(currentStreak: currentStreak, startDate: streakStartDate)
    }

    // MARK: - Streak Card

    /// Consecutive streak display card
    struct StreakCard: View {
        let streaks: [Date]
        let currentStreakTitle: String
        let dayText: String
        let daysText: String
        let noRecordsText: String
        let startedTodayText: String
        let recordedYesterdayText: String
        let colors: [Color]

        private var streakInfo: StreakInfo {
            calculateStreak(from: streaks)
        }

        /// Create a streak card
        /// - Parameters:
        ///   - streaks: Array of timestamps
        ///   - currentStreakTitle: Title text
        ///   - dayText: Singular day text
        ///   - daysText: Plural days text
        ///   - noRecordsText: No records text
        ///   - startedTodayText: Started today text
        ///   - recordedYesterdayText: Recorded yesterday text
        ///   - colors: Gradient color array
        init(
            streaks: [Date],
            currentStreakTitle: String = "Current Streak",
            dayText: String = "Day",
            daysText: String = "Days",
            noRecordsText: String = "No records yet. Start today!",
            startedTodayText: String = "Started today. Keep it up!",
            recordedYesterdayText: String = "You recorded yesterday. Continue today!",
            colors: [Color] = [.blue, .purple]
        ) {
            self.streaks = streaks
            self.currentStreakTitle = currentStreakTitle
            self.dayText = dayText
            self.daysText = daysText
            self.noRecordsText = noRecordsText
            self.startedTodayText = startedTodayText
            self.recordedYesterdayText = recordedYesterdayText
            self.colors = colors
        }

        var body: some View {
            HStack {
                Spacer()
                VStack {
                    Text(currentStreakTitle)
                        .font(.headline)
                        .foregroundStyle(.regularMaterial)

                    VStack(spacing: -10) {
                        Text("\(streakInfo.currentStreak)")
                            .fontWeight(.bold)
                            .font(.system(size: 80))
                        Text(streakInfo.currentStreak == 1 ? dayText : daysText)
                            .font(.title2)
                            .fontWeight(.semibold)
                    }
                    .foregroundStyle(.white)

                    Text(streakInfo.displayText(
                        noRecordsText: noRecordsText,
                        startedTodayText: startedTodayText,
                        recordedYesterdayText: recordedYesterdayText
                    ))
                    .font(.footnote)
                    .foregroundStyle(.regularMaterial)
                    .multilineTextAlignment(.center)
                }
                Spacer()
            }
            .padding(.vertical)
            .background(
                LinearGradient(
                    colors: colors,
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
            )
        }
    }

    // MARK: - Heatmap Grid

    /// Activity heatmap grid
    struct HeatmapGrid: View {
        let timestamps: [Date]
        let days: Int
        let baseColor: Color
        let itemSize: CGFloat
        let spacing: CGFloat

        private let calendar = Calendar.current

        private var recordCountByDay: [Date: Int] {
            var counts: [Date: Int] = [:]

            for timestamp in timestamps {
                let day = calendar.startOfDay(for: timestamp)
                counts[day, default: 0] += 1
            }

            return counts
        }

        private var targetDays: [Date] {
            let today = calendar.startOfDay(for: Date())
            var daysList: [Date] = []

            for i in stride(from: days - 1, through: 0, by: -1) {
                if let day = calendar.date(byAdding: .day, value: -i, to: today) {
                    daysList.append(day)
                }
            }

            return daysList
        }

        private func colorForRecordCount(_ count: Int) -> Color {
            switch count {
            case 0:
                return baseColor.opacity(0.2)
            case 1:
                return baseColor.opacity(0.4)
            case 2:
                return baseColor.opacity(0.7)
            default:
                return baseColor
            }
        }

        /// Create an activity heatmap grid
        /// - Parameters:
        ///   - timestamps: Array of timestamps
        ///   - days: Number of days to display, default 60
        ///   - baseColor: Base color, default green
        ///   - itemSize: Individual block size, default 20
        ///   - spacing: Block spacing, default 3
        init(
            timestamps: [Date],
            days: Int = 60,
            baseColor: Color = .green,
            itemSize: CGFloat = 20,
            spacing: CGFloat = 3
        ) {
            self.timestamps = timestamps
            self.days = days
            self.baseColor = baseColor
            self.itemSize = itemSize
            self.spacing = spacing
        }

        var body: some View {
            HStack {
                Spacer()
                FlowLayout(spacing: spacing) {
                    ForEach(targetDays, id: \.self) { date in
                        let count = recordCountByDay[date] ?? 0

                        RoundedRectangle(cornerRadius: 2)
                            .fill(colorForRecordCount(count))
                            .frame(width: itemSize, height: itemSize)
                    }
                }
                Spacer()
            }
        }
    }

    // MARK: - Heatmap Legend

    /// Heatmap legend
    struct HeatmapLegend: View {
        let baseColor: Color
        let lessText: String
        let moreText: String

        /// Create a heatmap legend
        /// - Parameters:
        ///   - baseColor: Base color
        ///   - lessText: "Less" text label
        ///   - moreText: "More" text label
        init(
            baseColor: Color = .green,
            lessText: String = "Less",
            moreText: String = "More"
        ) {
            self.baseColor = baseColor
            self.lessText = lessText
            self.moreText = moreText
        }

        var body: some View {
            HStack {
                Spacer()

                Text(lessText)

                HStack(spacing: 3) {
                    Group {
                        RoundedRectangle(cornerRadius: 2)
                            .fill(baseColor.opacity(0.2))
                        RoundedRectangle(cornerRadius: 2)
                            .fill(baseColor.opacity(0.4))
                        RoundedRectangle(cornerRadius: 2)
                            .fill(baseColor.opacity(0.7))
                        RoundedRectangle(cornerRadius: 2)
                            .fill(baseColor)
                    }
                    .frame(width: 12, height: 12)
                }

                Text(moreText)
            }
        }
    }

    // MARK: - Flow Layout

    /// Custom flow layout that arranges items horizontally with automatic line wrapping
    struct FlowLayout: Layout {
        let spacing: CGFloat

        func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
            let result = FlowResult(
                in: proposal.width ?? .infinity,
                subviews: subviews,
                spacing: spacing
            )
            return result.size
        }

        func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
            let result = FlowResult(
                in: bounds.width,
                subviews: subviews,
                spacing: spacing
            )

            for (index, subview) in subviews.enumerated() {
                subview.place(
                    at: CGPoint(
                        x: bounds.minX + result.positions[index].x,
                        y: bounds.minY + result.positions[index].y
                    ),
                    proposal: ProposedViewSize(result.sizes[index])
                )
            }
        }

        struct FlowResult {
            let size: CGSize
            let positions: [CGPoint]
            let sizes: [CGSize]

            init(in maxWidth: CGFloat, subviews: Subviews, spacing: CGFloat) {
                var positions: [CGPoint] = []
                var sizes: [CGSize] = []

                var x: CGFloat = 0
                var y: CGFloat = 0
                var lineHeight: CGFloat = 0
                var maxX: CGFloat = 0

                for subview in subviews {
                    let size = subview.sizeThatFits(.unspecified)
                    sizes.append(size)

                    if x + size.width > maxWidth && x > 0 {
                        x = 0
                        y += lineHeight + spacing
                        lineHeight = 0
                    }

                    positions.append(CGPoint(x: x, y: y))
                    lineHeight = max(lineHeight, size.height)
                    x += size.width + spacing
                    maxX = max(maxX, x - spacing)
                }

                self.size = CGSize(width: maxX, height: y + lineHeight)
                self.positions = positions
                self.sizes = sizes
            }
        }
    }
}

// MARK: - Preview

#Preview {
    // Sample data: random check-ins over the past 60 days
    let timestamps: [Date] = {
        var dates: [Date] = []
        let calendar = Calendar.current
        let today = Date()

        for i in 0..<60 {
            // 70% chance of having a record
            if Int.random(in: 0...100) < 70 {
                if let date = calendar.date(byAdding: .day, value: -i, to: today) {
                    // Each day may have 1-3 records
                    let count = Int.random(in: 1...3)
                    for _ in 0..<count {
                        dates.append(date)
                    }
                }
            }
        }

        return dates
    }()

    NavigationStack {
        Form {
            // Section 1: Full example with data
            Section("With Data") {
                SWActivityHeatmap.StreakCard(
                    streaks: timestamps,
                    colors: [.blue, .purple]
                )
            }
            .listRowInsets(EdgeInsets())

            Section {
                SWActivityHeatmap.HeatmapGrid(
                    timestamps: timestamps,
                    days: 60,
                    baseColor: .green
                )
            } header: {
                Text("Past 60 days")
            } footer: {
                SWActivityHeatmap.HeatmapLegend(
                    baseColor: .green
                )
            }

            // Section 2: Empty state
            Section("Empty Data") {
                SWActivityHeatmap.StreakCard(
                    streaks: [],
                    colors: [.orange, .red]
                )
            }
            .listRowInsets(EdgeInsets())

            Section {
                SWActivityHeatmap.HeatmapGrid(
                    timestamps: [],
                    baseColor: .blue
                )
            } header: {
                Text("Empty heatmap")
            } footer: {
                SWActivityHeatmap.HeatmapLegend(
                    baseColor: .blue
                )
            }
        }
        .navigationTitle("Activity")
    }
}
```

## File: `ShipSwift/SWPackage/SWChart/SWAreaChart.swift`
```
//
//  SWAreaChart.swift
//  ShipSwift
//
//  Horizontally scrollable area chart built on Swift Charts (AreaMark). Supports
//  multiple series with color mapping, configurable area opacity, optional line overlay,
//  and configurable interpolation. Generic over CategoryType for series grouping.
//  Includes a convenience initializer for String categories.
//
//  Usage:
//    // Basic area chart
//    let data: [SWAreaChart<String>.DataPoint] = [
//        .init(date: Date(), value: 72, category: "Downloads"),
//    ]
//    let colors: [String: Color] = ["Downloads": .blue]
//
//    SWAreaChart(dataPoints: data, colorMapping: colors, title: "App Downloads")
//
//    // Stacked area chart with gradient and line overlay
//    SWAreaChart(
//        dataPoints: data,
//        colorMapping: colors,
//        stackMode: .stacked,
//        showLineOverlay: true,
//        interpolationMethod: .catmullRom,
//        gradientOpacity: 0.3,
//        yDomain: 0...500,
//        visibleDays: 14,
//        chartHeight: 240,
//        title: "Traffic Sources"
//    )
//
//  Data Model (built-in):
//    SWAreaChart<CategoryType>.DataPoint
//      - date: Date
//      - value: Double
//      - category: CategoryType
//
//  Parameters:
//    - dataPoints: [DataPoint]                      — Array of data points
//    - colorMapping: [CategoryType: Color]           — Category to color mapping
//    - stackMode: StackMode                         — .standard or .stacked (default .standard)
//    - showLineOverlay: Bool                        — Draw LineMark on top of area (default true)
//    - interpolationMethod: InterpolationMethod      — Line/area interpolation (default .catmullRom)
//    - gradientOpacity: Double                      — Opacity of the area fill (default 0.15)
//    - yDomain: ClosedRange<Double>?                — Y-axis range (default auto)
//    - scrollableDaysBack: Int                      — Scrollable days backward (default 30)
//    - scrollableDaysForward: Int                   — Scrollable days forward (default 7)
//    - visibleDays: Int                             — Visible days range (default 7)
//    - chartHeight: CGFloat                         — Chart height (default 200)
//    - title: String?                               — Optional title
//
//  Notes:
//    - Appear animation: via chartPlotStyle, a mask rectangle expands from left to right
//      (easeOut 1.2s, 0.2s delay) only on the plot area, so axes/labels/legend stay visible.
//      All data points are always rendered so axes stay stable.
//
//  Created by Wei Zhong on 2/13/26.
//

import SwiftUI
import Charts

// MARK: - SWAreaChart

struct SWAreaChart<CategoryType: Hashable & Plottable>: View {
    // MARK: - Enums

    /// Display mode for multi-series areas
    enum StackMode {
        /// Each series rendered independently (overlapping)
        case standard
        /// Series stacked on top of each other
        case stacked
    }

    // MARK: - Built-in Data Model

    /// Data point model for the area chart
    struct DataPoint: Identifiable {
        let id: UUID
        let date: Date
        let value: Double
        let category: CategoryType

        init(id: UUID = UUID(), date: Date, value: Double, category: CategoryType) {
            self.id = id
            self.date = date
            self.value = value
            self.category = category
        }
    }

    // MARK: - Properties

    /// Array of data points
    let dataPoints: [DataPoint]

    /// Color mapping for categories
    let colorMapping: [CategoryType: Color]

    /// Standard or stacked display mode
    var stackMode: StackMode = .standard

    /// Whether to draw a LineMark on top of the area
    var showLineOverlay: Bool = true

    /// Line/area interpolation method
    var interpolationMethod: InterpolationMethod = .catmullRom

    /// Opacity of the area fill (0.0 = hidden, 1.0 = fully opaque)
    var gradientOpacity: Double = 0.15

    /// Y-axis range (nil = automatic)
    var yDomain: ClosedRange<Double>? = nil

    /// X-axis scrollable total range (days back from today)
    var scrollableDaysBack: Int = 30

    /// X-axis scrollable total range (days forward from today)
    var scrollableDaysForward: Int = 7

    /// Visible range (days)
    var visibleDays: Int = 7

    /// Chart height
    var chartHeight: CGFloat = 200

    /// Title (optional)
    var title: String? = nil

    /// Animation progress (0 to 1), Y values multiply by this to animate from 0 to target
    @State private var animationProgress: Double = 0

    // MARK: - Computed Properties

    /// Y-axis domain computed from real data (stays constant during animation to prevent axis rescaling).
    /// In stacked mode, uses the max sum of all series per date; in standard mode, uses the max single data point.
    private var effectiveYDomain: ClosedRange<Double>? {
        if let yDomain = yDomain { return yDomain }
        guard !dataPoints.isEmpty else { return nil }

        let maxVal: Double
        if stackMode == .stacked {
            // Group by date (day), sum each group, take the maximum
            let calendar = Calendar.current
            let grouped = Dictionary(grouping: dataPoints) { calendar.startOfDay(for: $0.date) }
            guard let stackMax = grouped.values.map({ $0.reduce(0) { $0 + $1.value } }).max(), stackMax > 0 else { return nil }
            maxVal = stackMax
        } else {
            guard let singleMax = dataPoints.map(\.value).max(), singleMax > 0 else { return nil }
            maxVal = singleMax
        }
        return 0...maxVal
    }

    /// X-axis scrollable total range
    private var chartXDomain: ClosedRange<Date> {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        let startDate = calendar.date(byAdding: .day, value: -scrollableDaysBack, to: startOfToday)!
        let endDate = calendar.date(byAdding: .day, value: scrollableDaysForward, to: startOfToday)!
        return startDate...endDate
    }

    /// Chart initial scroll position: latest data at right edge
    private var chartInitialScrollDate: Date {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        return calendar.date(byAdding: .day, value: -visibleDays, to: startOfToday)!
    }

    /// Visible range time length (seconds)
    private var visibleDomainLength: Int {
        visibleDays * 24 * 60 * 60
    }

    // MARK: - Body

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Title
            if let title = title {
                Text(title)
                    .font(.title3)
                    .fontWeight(.semibold)
            }

            // Chart
            Chart {
                ForEach(dataPoints) { point in
                    AreaMark(
                        x: .value("Date", point.date),
                        y: .value("Value", point.value * animationProgress),
                        stacking: stackMode == .stacked ? .standard : .unstacked
                    )
                    .foregroundStyle(by: .value("Category", point.category))
                    .interpolationMethod(interpolationMethod)
                    .opacity(gradientOpacity)

                    if showLineOverlay {
                        LineMark(
                            x: .value("Date", point.date),
                            y: .value("Value", point.value * animationProgress)
                        )
                        .foregroundStyle(by: .value("Category", point.category))
                        .interpolationMethod(interpolationMethod)
                        .lineStyle(StrokeStyle(lineWidth: 2))
                    }
                }
            }
            .chartForegroundStyleScale(
                domain: Array(colorMapping.keys),
                range: Array(colorMapping.values)
            )
            .chartXScale(domain: chartXDomain)
            .applyOptionalYDomain(effectiveYDomain)
            .chartScrollableAxes(.horizontal)
            .chartXVisibleDomain(length: visibleDomainLength)
            .chartScrollPosition(initialX: chartInitialScrollDate)
            .chartYAxis {
                AxisMarks(position: .leading, values: .automatic(desiredCount: 5)) { _ in
                    AxisGridLine()
                    AxisValueLabel()
                }
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: .day, count: 1)) { _ in
                    AxisGridLine()
                    AxisValueLabel(format: .dateTime.month(.abbreviated).day())
                }
            }
            .chartLegend(position: .top, alignment: .trailing)
            .frame(height: chartHeight)
            .onAppear {
                withAnimation(.easeOut(duration: 1.2).delay(0.2)) {
                    animationProgress = 1.0
                }
            }
        }
    }

}

// MARK: - Y-Domain Helper

private extension View {
    /// Conditionally apply Y-axis domain when provided
    @ViewBuilder
    func applyOptionalYDomain(_ domain: ClosedRange<Double>?) -> some View {
        if let domain = domain {
            self.chartYScale(domain: domain)
        } else {
            self
        }
    }
}

// MARK: - Convenience Initializer for String Category

extension SWAreaChart where CategoryType == String {
    /// Convenience initializer (using String as category type)
    init(
        dataPoints: [DataPoint],
        colorMapping: [String: Color],
        stackMode: StackMode = .standard,
        showLineOverlay: Bool = true,
        interpolationMethod: InterpolationMethod = .catmullRom,
        gradientOpacity: Double = 0.15,
        yDomain: ClosedRange<Double>? = nil,
        scrollableDaysBack: Int = 30,
        scrollableDaysForward: Int = 7,
        visibleDays: Int = 7,
        chartHeight: CGFloat = 200,
        title: String? = nil
    ) {
        self.dataPoints = dataPoints
        self.colorMapping = colorMapping
        self.stackMode = stackMode
        self.showLineOverlay = showLineOverlay
        self.interpolationMethod = interpolationMethod
        self.gradientOpacity = gradientOpacity
        self.yDomain = yDomain
        self.scrollableDaysBack = scrollableDaysBack
        self.scrollableDaysForward = scrollableDaysForward
        self.visibleDays = visibleDays
        self.chartHeight = chartHeight
        self.title = title
    }
}

// MARK: - Preview

#Preview {
    ScrollView {
        VStack(spacing: 32) {
            // Example 1: Standard multi-series area chart (overlapping)
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let trafficData: [SWAreaChart<String>.DataPoint] = (0..<14).flatMap { dayOffset -> [SWAreaChart<String>.DataPoint] in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return [
                        .init(date: date, value: Double.random(in: 100...300), category: "Organic"),
                        .init(date: date, value: Double.random(in: 50...200), category: "Paid"),
                    ]
                }

                SWAreaChart(
                    dataPoints: trafficData,
                    colorMapping: ["Organic": .green, "Paid": .blue],
                    gradientOpacity: 0.25,
                    title: "Website Traffic"
                )
            }

            Divider()

            // Example 2: Stacked area chart with catmullRom
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let revenueData: [SWAreaChart<String>.DataPoint] = (0..<10).flatMap { dayOffset -> [SWAreaChart<String>.DataPoint] in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return [
                        .init(date: date, value: Double.random(in: 40...120), category: "Product A"),
                        .init(date: date, value: Double.random(in: 30...80), category: "Product B"),
                        .init(date: date, value: Double.random(in: 20...60), category: "Product C"),
                    ]
                }

                SWAreaChart(
                    dataPoints: revenueData,
                    colorMapping: [
                        "Product A": .purple,
                        "Product B": .orange,
                        "Product C": .cyan,
                    ],
                    stackMode: .stacked,
                    interpolationMethod: .catmullRom,
                    gradientOpacity: 0.4,
                    yDomain: 0...300,
                    visibleDays: 10,
                    chartHeight: 240,
                    title: "Revenue by Product (Stacked)"
                )
            }

            Divider()

            // Example 3: Single series area chart (no line overlay)
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let memoryData: [SWAreaChart<String>.DataPoint] = (0..<7).map { dayOffset in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return .init(date: date, value: Double.random(in: 1.5...4.0), category: "Memory")
                }

                SWAreaChart(
                    dataPoints: memoryData,
                    colorMapping: ["Memory": .red],
                    showLineOverlay: false,
                    interpolationMethod: .monotone,
                    gradientOpacity: 0.3,
                    visibleDays: 7,
                    chartHeight: 180,
                    title: "Memory Usage (GB)"
                )
            }
        }
        .padding()
    }
}
```

## File: `ShipSwift/SWPackage/SWChart/SWBarChart.swift`
```
//
//  SWBarChart.swift
//  ShipSwift
//
//  Horizontally scrollable bar chart built on Swift Charts (BarMark). Supports grouped
//  and stacked display modes, multiple series with color mapping, and optional value labels.
//  Generic over CategoryType for series grouping. Includes a convenience initializer for
//  String categories.
//
//  Usage:
//    // Basic grouped bar chart
//    let data: [SWBarChart<String>.DataPoint] = [
//        .init(date: Date(), value: 120, category: "Online"),
//        .init(date: Date(), value: 85, category: "Offline"),
//    ]
//    let colors: [String: Color] = ["Online": .blue, "Offline": .orange]
//
//    SWBarChart(dataPoints: data, colorMapping: colors, title: "Sales Channel")
//
//    // Stacked bar chart with custom config
//    SWBarChart(
//        dataPoints: data,
//        colorMapping: colors,
//        stackMode: .stacked,
//        showValueLabels: true,
//        barCornerRadius: 4,
//        yDomain: 0...300,
//        visibleDays: 14,
//        chartHeight: 250,
//        title: "Revenue Breakdown"
//    )
//
//  Data Model (built-in):
//    SWBarChart<CategoryType>.DataPoint
//      - date: Date
//      - value: Double
//      - category: CategoryType
//
//  Parameters:
//    - dataPoints: [DataPoint]                      — Array of data points
//    - colorMapping: [CategoryType: Color]           — Category to color mapping
//    - stackMode: StackMode                         — .grouped or .stacked (default .grouped)
//    - showValueLabels: Bool                        — Show value above each bar (default false)
//    - barCornerRadius: CGFloat                     — Corner radius for bars (default 3)
//    - yDomain: ClosedRange<Double>?                — Y-axis range (default auto)
//    - scrollableDaysBack: Int                      — Scrollable days backward (default 30)
//    - scrollableDaysForward: Int                   — Scrollable days forward (default 7)
//    - visibleDays: Int                             — Visible days range (default 7)
//    - chartHeight: CGFloat                         — Chart height (default 200)
//    - title: String?                               — Optional title
//
//  Notes:
//    - Appear animation: bars grow from 0 to target value with easeOut 1.2s after 0.2s delay
//    - Y-axis range is fixed to real data bounds during animation (bars grow, axis stays)
//
//  Created by Wei Zhong on 2/13/26.
//

import SwiftUI
import Charts

// MARK: - SWBarChart

struct SWBarChart<CategoryType: Hashable & Plottable>: View {
    // MARK: - Enums

    /// Display mode for multi-series bars
    enum StackMode {
        /// Bars side by side within the same date bucket
        case grouped
        /// Bars stacked on top of each other
        case stacked
    }

    // MARK: - Built-in Data Model

    /// Data point model for the bar chart
    struct DataPoint: Identifiable {
        let id: UUID
        let date: Date
        let value: Double
        let category: CategoryType

        init(id: UUID = UUID(), date: Date, value: Double, category: CategoryType) {
            self.id = id
            self.date = date
            self.value = value
            self.category = category
        }
    }

    // MARK: - Properties

    /// Array of data points
    let dataPoints: [DataPoint]

    /// Color mapping for categories
    let colorMapping: [CategoryType: Color]

    /// Grouped or stacked display mode
    var stackMode: StackMode = .grouped

    /// Whether to show value annotations above bars
    var showValueLabels: Bool = false

    /// Corner radius for bar shape
    var barCornerRadius: CGFloat = 3

    /// Y-axis range (nil = automatic)
    var yDomain: ClosedRange<Double>? = nil

    /// X-axis scrollable total range (days back from today)
    var scrollableDaysBack: Int = 30

    /// X-axis scrollable total range (days forward from today)
    var scrollableDaysForward: Int = 7

    /// Visible range (days)
    var visibleDays: Int = 7

    /// Chart height
    var chartHeight: CGFloat = 200

    /// Title (optional)
    var title: String? = nil

    /// Animation progress (0 to 1), controls bar growth from 0 to target value
    @State private var animationProgress: Double = 0

    // MARK: - Computed Properties

    /// Y-axis domain computed from real data (stays constant during animation to prevent axis rescaling).
    /// In stacked mode, uses the max sum of all series per date; in grouped mode, uses the max single data point.
    private var effectiveYDomain: ClosedRange<Double>? {
        if let yDomain = yDomain { return yDomain }
        guard !dataPoints.isEmpty else { return nil }

        let maxVal: Double
        if stackMode == .stacked {
            // Group by date (day), sum each group, take the maximum
            let calendar = Calendar.current
            let grouped = Dictionary(grouping: dataPoints) { calendar.startOfDay(for: $0.date) }
            guard let stackMax = grouped.values.map({ $0.reduce(0) { $0 + $1.value } }).max(), stackMax > 0 else { return nil }
            maxVal = stackMax
        } else {
            guard let singleMax = dataPoints.map(\.value).max(), singleMax > 0 else { return nil }
            maxVal = singleMax
        }
        return 0...maxVal
    }

    /// X-axis scrollable total range
    private var chartXDomain: ClosedRange<Date> {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        let startDate = calendar.date(byAdding: .day, value: -scrollableDaysBack, to: startOfToday)!
        let endDate = calendar.date(byAdding: .day, value: scrollableDaysForward, to: startOfToday)!
        return startDate...endDate
    }

    /// Chart initial scroll position: center today in the visible range
    private var chartInitialScrollDate: Date {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        let offset = visibleDays / 2
        return calendar.date(byAdding: .day, value: -offset, to: startOfToday)!
    }

    /// Visible range time length (seconds)
    private var visibleDomainLength: Int {
        visibleDays * 24 * 60 * 60
    }

    // MARK: - Body

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Title
            if let title = title {
                Text(title)
                    .font(.title3)
                    .fontWeight(.semibold)
            }

            // Chart (y values multiplied by animationProgress to animate growth from 0)
            Chart(dataPoints) { point in
                if stackMode == .grouped {
                    BarMark(
                        x: .value("Date", point.date, unit: .day),
                        y: .value("Value", point.value * animationProgress)
                    )
                    .foregroundStyle(by: .value("Category", point.category))
                    .position(by: .value("Category", point.category))
                    .clipShape(RoundedRectangle(cornerRadius: barCornerRadius))
                    .annotation(position: .top) {
                        valueLabel(for: point)
                    }
                } else {
                    BarMark(
                        x: .value("Date", point.date, unit: .day),
                        y: .value("Value", point.value * animationProgress)
                    )
                    .foregroundStyle(by: .value("Category", point.category))
                    .clipShape(RoundedRectangle(cornerRadius: barCornerRadius))
                    .annotation(position: .top) {
                        valueLabel(for: point)
                    }
                }
            }
            .chartForegroundStyleScale(
                domain: Array(colorMapping.keys),
                range: Array(colorMapping.values)
            )
            .chartXScale(domain: chartXDomain)
            .applyOptionalYDomain(effectiveYDomain)
            .chartScrollableAxes(.horizontal)
            .chartXVisibleDomain(length: visibleDomainLength)
            .chartScrollPosition(initialX: chartInitialScrollDate)
            .chartYAxis {
                AxisMarks(position: .leading, values: .automatic(desiredCount: 5)) { _ in
                    AxisGridLine()
                    AxisValueLabel()
                }
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: .day, count: 1)) { _ in
                    AxisGridLine()
                    AxisValueLabel(format: .dateTime.month(.abbreviated).day())
                }
            }
            .chartLegend(position: .top, alignment: .trailing)
            .frame(height: chartHeight)
            .onAppear {
                withAnimation(.easeOut(duration: 1.2).delay(0.2)) {
                    animationProgress = 1.0
                }
            }
        }
    }

    // MARK: - Private Helpers

    /// Value label annotation (only rendered when showValueLabels is true)
    @ViewBuilder
    private func valueLabel(for point: DataPoint) -> some View {
        if showValueLabels {
            Text("\(Int(point.value))")
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
    }
}

// MARK: - Y-Domain Helper

private extension View {
    /// Conditionally apply Y-axis domain when provided
    @ViewBuilder
    func applyOptionalYDomain(_ domain: ClosedRange<Double>?) -> some View {
        if let domain = domain {
            self.chartYScale(domain: domain)
        } else {
            self
        }
    }
}

// MARK: - Convenience Initializer for String Category

extension SWBarChart where CategoryType == String {
    /// Convenience initializer (using String as category type)
    init(
        dataPoints: [DataPoint],
        colorMapping: [String: Color],
        stackMode: StackMode = .grouped,
        showValueLabels: Bool = false,
        barCornerRadius: CGFloat = 3,
        yDomain: ClosedRange<Double>? = nil,
        scrollableDaysBack: Int = 30,
        scrollableDaysForward: Int = 7,
        visibleDays: Int = 7,
        chartHeight: CGFloat = 200,
        title: String? = nil
    ) {
        self.dataPoints = dataPoints
        self.colorMapping = colorMapping
        self.stackMode = stackMode
        self.showValueLabels = showValueLabels
        self.barCornerRadius = barCornerRadius
        self.yDomain = yDomain
        self.scrollableDaysBack = scrollableDaysBack
        self.scrollableDaysForward = scrollableDaysForward
        self.visibleDays = visibleDays
        self.chartHeight = chartHeight
        self.title = title
    }
}

// MARK: - Preview

#Preview {
    ScrollView {
        VStack(spacing: 32) {
            // Example 1: Grouped bar chart (two series)
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let salesData: [SWBarChart<String>.DataPoint] = (0..<10).flatMap { dayOffset -> [SWBarChart<String>.DataPoint] in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return [
                        .init(date: date, value: Double.random(in: 50...150), category: "Online"),
                        .init(date: date, value: Double.random(in: 30...100), category: "Offline"),
                    ]
                }

                SWBarChart(
                    dataPoints: salesData,
                    colorMapping: ["Online": .blue, "Offline": .orange],
                    title: "Sales by Channel (Grouped)"
                )
            }

            Divider()

            // Example 2: Stacked bar chart with value labels
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let stackedData: [SWBarChart<String>.DataPoint] = (0..<7).flatMap { dayOffset -> [SWBarChart<String>.DataPoint] in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return [
                        .init(date: date, value: Double.random(in: 30...80), category: "Food"),
                        .init(date: date, value: Double.random(in: 20...50), category: "Transport"),
                        .init(date: date, value: Double.random(in: 10...40), category: "Entertainment"),
                    ]
                }

                SWBarChart(
                    dataPoints: stackedData,
                    colorMapping: [
                        "Food": .green,
                        "Transport": .blue,
                        "Entertainment": .purple,
                    ],
                    stackMode: .stacked,
                    showValueLabels: false,
                    yDomain: 0...200,
                    visibleDays: 7,
                    chartHeight: 250,
                    title: "Daily Expenses (Stacked)"
                )
            }

            Divider()

            // Example 3: Single series bar chart
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let singleData: [SWBarChart<String>.DataPoint] = (0..<14).map { dayOffset in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return .init(date: date, value: Double.random(in: 2000...12000), category: "Steps")
                }

                SWBarChart(
                    dataPoints: singleData,
                    colorMapping: ["Steps": .mint],
                    showValueLabels: true,
                    barCornerRadius: 5,
                    visibleDays: 7,
                    chartHeight: 200,
                    title: "Daily Steps"
                )
            }
        }
        .padding()
    }
}
```

## File: `ShipSwift/SWPackage/SWChart/SWDonutChart.swift`
```
//
//  SWDonutChart.swift
//  ShipSwift
//
//  Interactive donut chart built on Swift Charts. Groups data by category and renders
//  a SectorMark chart with tap-to-select interaction. The selected category expands
//  outward and dims the rest. Center overlay shows the count and category name.
//
//  Usage:
//    @State private var selectedCategory: String? = nil
//
//    // 1. Define categories
//    let work = SWDonutChart.Category(name: "Work")
//    let personal = SWDonutChart.Category(name: "Personal")
//    let health = SWDonutChart.Category(name: "Health")
//
//    // 2. Build data items (when category is nil, grouped into "No Category")
//    let subjects: [SWDonutChart.Subject] = [
//        .init(name: "Meeting", category: work),
//        .init(name: "Report", category: work),
//        .init(name: "Shopping", category: personal),
//        .init(name: "Exercise", category: health),
//        .init(name: "Random Task", category: nil),
//    ]
//
//    // 3. Use the component, bind selected state
//    SWDonutChart(
//        subjects: subjects,
//        selectedCategory: $selectedCategory
//    )
//
//  Data Models:
//    - SWDonutChart.Category — Category (id: UUID, name: String)
//    - SWDonutChart.Subject  — Data item (id: UUID, name: String, category: Category?)
//
//  Parameters:
//    - subjects: [Subject]                — Array of data items
//    - selectedCategory: Binding<String?> — Currently selected category name (nil means all)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import Charts

struct SWDonutChart: View {
    // MARK: - Built-in Data Models

    /// Category model
    struct Category: Identifiable, Hashable {
        let id: UUID
        let name: String

        init(id: UUID = UUID(), name: String) {
            self.id = id
            self.name = name
        }
    }

    /// Data item model
    struct Subject: Identifiable {
        let id: UUID
        let name: String
        let category: Category?

        init(id: UUID = UUID(), name: String, category: Category? = nil) {
            self.id = id
            self.name = name
            self.category = category
        }
    }

    // MARK: - Properties

    let subjects: [Subject]
    @Binding var selectedCategory: String?

    private static let noCategoryKey = "__no_category__"

    // chartAngleSelection binds to cumulative angle value
    @State private var selectedAngle: Int?

    // Group and count by category
    private var categoryData: [CategoryItem] {
        let grouped = Dictionary(grouping: subjects) { subject -> String in
            guard let category = subject.category else {
                return Self.noCategoryKey  // No category
            }
            return category.name  // Category name (may be empty string)
        }
        return grouped.map { CategoryItem(name: $0.key, count: $0.value.count) }
            .sorted { $0.count != $1.count ? $0.count > $1.count : $0.name < $1.name }  // Descending by count, then alphabetical
    }

    private var totalCount: Int {
        subjects.count
    }

    // Category display name
    private func displayName(for categoryName: String) -> String {
        if categoryName == Self.noCategoryKey {
            return String(localized: "No Category")
        } else if categoryName.isEmpty {
            return String(localized: "Unnamed Category")
        }
        return categoryName
    }

    // Find the category corresponding to the cumulative angle value
    private func findCategory(for angle: Int) -> String? {
        var cumulative = 0
        for item in categoryData {
            cumulative += item.count
            if angle <= cumulative {
                return item.name
            }
        }
        return nil
    }

    // Count for the currently selected category
    private var selectedCount: Int {
        guard let selected = selectedCategory else { return totalCount }
        return categoryData.first { $0.name == selected }?.count ?? 0
    }

    // Display name for the currently selected category
    private var selectedDisplayName: String {
        guard let selected = selectedCategory else {
            return String(localized: "All Items")
        }
        return displayName(for: selected)
    }

    var body: some View {
        Group {
            if categoryData.isEmpty {
                EmptyView()
            } else {
                Chart(categoryData) { item in
                    let isSelected = selectedCategory == item.name
                    SectorMark(
                        angle: .value("Count", item.count),
                        innerRadius: .ratio(0.6),
                        outerRadius: .ratio(isSelected ? 1.0 : 0.9),
                        angularInset: isSelected ? 2 : 1
                    )
                    .cornerRadius(6)
                    // Use displayName for legend display while keeping original name for selection matching
                    .foregroundStyle(by: .value("Category", displayName(for: item.name)))
                    .opacity(selectedCategory == nil || isSelected ? 1.0 : 0.3)
                }
                .chartLegend(position: .trailing, alignment: .center, spacing: 16)
                .chartAngleSelection(value: $selectedAngle)
                .onChange(of: selectedAngle) { _, newValue in
                    if let angle = newValue, let category = findCategory(for: angle) {
                        selectedCategory = category
                    } else {
                        selectedCategory = nil
                    }
                }
                .animation(.bouncy, value: selectedCategory)
                .chartBackground { proxy in
                    GeometryReader { geometry in
                        if let plotFrame = proxy.plotFrame {
                            let frame = geometry[plotFrame]
                            VStack(spacing: 2) {
                                Text("\(selectedCount)")
                                    .font(.title.bold())
                                Text(selectedDisplayName)
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                            .position(x: frame.midX, y: frame.midY)
                        }
                    }
                }
                .frame(height: 200)
            }
        }
        .padding(.horizontal)
    }

    struct CategoryItem: Identifiable {
        let name: String
        let count: Int

        var id: String { name }  // Use name as stable id to avoid reordering
    }
}

#Preview {
    @Previewable @State var selectedCategory: String? = nil

    // Sample data
    let workCategory = SWDonutChart.Category(name: "Work")
    let personalCategory = SWDonutChart.Category(name: "Personal")
    let healthCategory = SWDonutChart.Category(name: "Health")

    let sampleSubjects: [SWDonutChart.Subject] = [
        .init(name: "Meeting", category: workCategory),
        .init(name: "Report", category: workCategory),
        .init(name: "Email", category: workCategory),
        .init(name: "Shopping", category: personalCategory),
        .init(name: "Reading", category: personalCategory),
        .init(name: "Exercise", category: healthCategory),
        .init(name: "Meditation", category: healthCategory),
        .init(name: "Running", category: healthCategory),
        .init(name: "Uncategorized Task", category: nil),
    ]

    SWDonutChart(subjects: sampleSubjects, selectedCategory: $selectedCategory)
        .padding()
}
```

## File: `ShipSwift/SWPackage/SWChart/SWLineChart.swift`
```
//
//  SWLineChart.swift
//  ShipSwift
//
//  Horizontally scrollable line chart built on Swift Charts (LineMark). Supports
//  multiple series with color mapping, optional RuleMark reference lines, configurable
//  interpolation methods, and point markers. Generic over CategoryType for series
//  grouping. Includes a convenience initializer for String categories.
//
//  Usage:
//    // Basic multi-series line chart
//    let data: [SWLineChart<String>.DataPoint] = [
//        .init(date: Date(), value: 72, category: "Revenue"),
//        .init(date: Date(), value: 45, category: "Cost"),
//    ]
//    let colors: [String: Color] = ["Revenue": .blue, "Cost": .red]
//
//    SWLineChart(dataPoints: data, colorMapping: colors, title: "Financials")
//
//    // With reference line and custom interpolation
//    SWLineChart(
//        dataPoints: data,
//        colorMapping: colors,
//        referenceLines: [.init(value: 60, label: "Target", color: .orange)],
//        interpolationMethod: .catmullRom,
//        showPointMarkers: true,
//        yDomain: 0...100,
//        visibleDays: 14,
//        chartHeight: 220,
//        title: "Performance"
//    )
//
//  Data Model (built-in):
//    SWLineChart<CategoryType>.DataPoint
//      - date: Date
//      - value: Double
//      - category: CategoryType
//
//    SWLineChart.ReferenceLine
//      - value: Double        — Y-axis position
//      - label: String?       — Optional annotation text
//      - color: Color         — Line color (default .secondary)
//      - style: StrokeStyle   — Dash style
//
//  Parameters:
//    - dataPoints: [DataPoint]                      — Array of data points
//    - colorMapping: [CategoryType: Color]           — Category to color mapping
//    - referenceLines: [ReferenceLine]               — Horizontal reference lines (default [])
//    - interpolationMethod: InterpolationMethod       — Line interpolation (default .linear)
//    - showPointMarkers: Bool                        — Show PointMark on each data point (default false)
//    - yDomain: ClosedRange<Double>?                 — Y-axis range (default auto)
//    - scrollableDaysBack: Int                       — Scrollable days backward (default 30)
//    - scrollableDaysForward: Int                    — Scrollable days forward (default 7)
//    - visibleDays: Int                              — Visible days range (default 7)
//    - chartHeight: CGFloat                          — Chart height (default 200)
//    - title: String?                                — Optional title
//
//  Notes:
//    - Appear animation: via chartPlotStyle, a mask rectangle expands from left to right
//      (easeOut 1.2s, 0.2s delay) only on the plot area, so axes/labels/legend stay visible.
//      All data points are always rendered so axes stay stable.
//    - Reference lines are also revealed progressively by the same mask animation
//
//  Created by Wei Zhong on 2/13/26.
//

import SwiftUI
import Charts

// MARK: - SWLineChart

struct SWLineChart<CategoryType: Hashable & Plottable>: View {
    // MARK: - Built-in Data Models

    /// Data point model for the line chart
    struct DataPoint: Identifiable {
        let id: UUID
        let date: Date
        let value: Double
        let category: CategoryType

        init(id: UUID = UUID(), date: Date, value: Double, category: CategoryType) {
            self.id = id
            self.date = date
            self.value = value
            self.category = category
        }
    }

    /// Horizontal reference line (RuleMark)
    struct ReferenceLine {
        let value: Double
        let label: String?
        let color: Color
        let style: StrokeStyle

        init(
            value: Double,
            label: String? = nil,
            color: Color = .secondary,
            style: StrokeStyle = StrokeStyle(lineWidth: 1, dash: [5, 3])
        ) {
            self.value = value
            self.label = label
            self.color = color
            self.style = style
        }
    }

    // MARK: - Properties

    /// Array of data points
    let dataPoints: [DataPoint]

    /// Color mapping for categories
    let colorMapping: [CategoryType: Color]

    /// Horizontal reference lines rendered via RuleMark
    var referenceLines: [ReferenceLine] = []

    /// Line interpolation method
    var interpolationMethod: InterpolationMethod = .linear

    /// Whether to show PointMark on each data point
    var showPointMarkers: Bool = false

    /// Y-axis range (nil = automatic)
    var yDomain: ClosedRange<Double>? = nil

    /// X-axis scrollable total range (days back from today)
    var scrollableDaysBack: Int = 30

    /// X-axis scrollable total range (days forward from today)
    var scrollableDaysForward: Int = 7

    /// Visible range (days)
    var visibleDays: Int = 7

    /// Chart height
    var chartHeight: CGFloat = 200

    /// Title (optional)
    var title: String? = nil

    /// Animation progress (0 to 1), Y values multiply by this to animate from 0 to target
    @State private var animationProgress: Double = 0

    // MARK: - Computed Properties

    /// Y-axis domain computed from real data (stays constant during animation to prevent axis rescaling)
    private var effectiveYDomain: ClosedRange<Double>? {
        if let yDomain = yDomain { return yDomain }
        let allValues = dataPoints.map(\.value) + referenceLines.map(\.value)
        guard let minVal = allValues.min(), let maxVal = allValues.max(), maxVal > 0 else { return nil }
        return min(minVal, 0)...maxVal
    }

    /// X-axis scrollable total range
    private var chartXDomain: ClosedRange<Date> {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        let startDate = calendar.date(byAdding: .day, value: -scrollableDaysBack, to: startOfToday)!
        let endDate = calendar.date(byAdding: .day, value: scrollableDaysForward, to: startOfToday)!
        return startDate...endDate
    }

    /// Chart initial scroll position: latest data at right edge
    private var chartInitialScrollDate: Date {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        return calendar.date(byAdding: .day, value: -visibleDays, to: startOfToday)!
    }

    /// Visible range time length (seconds)
    private var visibleDomainLength: Int {
        visibleDays * 24 * 60 * 60
    }

    // MARK: - Body

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Title
            if let title = title {
                Text(title)
                    .font(.title3)
                    .fontWeight(.semibold)
            }

            // Chart
            Chart {
                ForEach(dataPoints) { point in
                    LineMark(
                        x: .value("Date", point.date),
                        y: .value("Value", point.value * animationProgress)
                    )
                    .foregroundStyle(by: .value("Category", point.category))
                    .interpolationMethod(interpolationMethod)
                    .lineStyle(StrokeStyle(lineWidth: 2))

                    if showPointMarkers {
                        PointMark(
                            x: .value("Date", point.date),
                            y: .value("Value", point.value * animationProgress)
                        )
                        .foregroundStyle(by: .value("Category", point.category))
                        .symbolSize(30)
                    }
                }

                ForEach(Array(referenceLines.enumerated()), id: \.offset) { _, line in
                    RuleMark(y: .value("Reference", line.value * animationProgress))
                        .foregroundStyle(line.color)
                        .lineStyle(line.style)
                        .annotation(position: .top, alignment: .leading) {
                            if let label = line.label {
                                Text(label)
                                    .font(.caption2)
                                    .foregroundStyle(line.color)
                            }
                        }
                }
            }
            .chartForegroundStyleScale(
                domain: Array(colorMapping.keys),
                range: Array(colorMapping.values)
            )
            .chartXScale(domain: chartXDomain)
            .applyOptionalYDomain(effectiveYDomain)
            .chartScrollableAxes(.horizontal)
            .chartXVisibleDomain(length: visibleDomainLength)
            .chartScrollPosition(initialX: chartInitialScrollDate)
            .chartYAxis {
                AxisMarks(position: .leading, values: .automatic(desiredCount: 5)) { _ in
                    AxisGridLine()
                    AxisValueLabel()
                }
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: .day, count: 1)) { _ in
                    AxisGridLine()
                    AxisValueLabel(format: .dateTime.month(.abbreviated).day())
                }
            }
            .chartLegend(position: .top, alignment: .trailing)
            .frame(height: chartHeight)
            .onAppear {
                withAnimation(.easeOut(duration: 1.2).delay(0.2)) {
                    animationProgress = 1.0
                }
            }
        }
    }
}

// MARK: - Y-Domain Helper

private extension View {
    /// Conditionally apply Y-axis domain when provided
    @ViewBuilder
    func applyOptionalYDomain(_ domain: ClosedRange<Double>?) -> some View {
        if let domain = domain {
            self.chartYScale(domain: domain)
        } else {
            self
        }
    }
}

// MARK: - Convenience Initializer for String Category

extension SWLineChart where CategoryType == String {
    /// Convenience initializer (using String as category type)
    init(
        dataPoints: [DataPoint],
        colorMapping: [String: Color],
        referenceLines: [ReferenceLine] = [],
        interpolationMethod: InterpolationMethod = .linear,
        showPointMarkers: Bool = false,
        yDomain: ClosedRange<Double>? = nil,
        scrollableDaysBack: Int = 30,
        scrollableDaysForward: Int = 7,
        visibleDays: Int = 7,
        chartHeight: CGFloat = 200,
        title: String? = nil
    ) {
        self.dataPoints = dataPoints
        self.colorMapping = colorMapping
        self.referenceLines = referenceLines
        self.interpolationMethod = interpolationMethod
        self.showPointMarkers = showPointMarkers
        self.yDomain = yDomain
        self.scrollableDaysBack = scrollableDaysBack
        self.scrollableDaysForward = scrollableDaysForward
        self.visibleDays = visibleDays
        self.chartHeight = chartHeight
        self.title = title
    }
}

// MARK: - Preview

#Preview {
    ScrollView {
        VStack(spacing: 32) {
            // Example 1: Basic multi-series line chart
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let salesData: [SWLineChart<String>.DataPoint] = (0..<14).flatMap { dayOffset -> [SWLineChart<String>.DataPoint] in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return [
                        .init(date: date, value: Double.random(in: 40...90), category: "Revenue"),
                        .init(date: date, value: Double.random(in: 20...60), category: "Cost"),
                    ]
                }

                SWLineChart(
                    dataPoints: salesData,
                    colorMapping: ["Revenue": .blue, "Cost": .red],
                    title: "Revenue vs Cost"
                )
            }

            Divider()

            // Example 2: With reference line, catmullRom interpolation, and point markers
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let tempData: [SWLineChart<String>.DataPoint] = (0..<10).map { dayOffset in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return .init(date: date, value: Double.random(in: 35.5...38.5), category: "Temperature")
                }

                SWLineChart(
                    dataPoints: tempData,
                    colorMapping: ["Temperature": .orange],
                    referenceLines: [
                        .init(value: 37.0, label: "Normal", color: .green),
                        .init(value: 38.0, label: "Fever", color: .red),
                    ],
                    interpolationMethod: .catmullRom,
                    showPointMarkers: true,
                    yDomain: 35...40,
                    visibleDays: 10,
                    chartHeight: 220,
                    title: "Body Temperature"
                )
            }

            Divider()

            // Example 3: Single series with stepped interpolation
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let stepData: [SWLineChart<String>.DataPoint] = (0..<7).map { dayOffset in
                    let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                    return .init(date: date, value: Double(Int.random(in: 1...5)) * 1000, category: "Steps")
                }

                SWLineChart(
                    dataPoints: stepData,
                    colorMapping: ["Steps": .green],
                    interpolationMethod: .stepCenter,
                    visibleDays: 7,
                    chartHeight: 180,
                    title: "Daily Steps (Stepped)"
                )
            }
        }
        .padding()
    }
}
```

## File: `ShipSwift/SWPackage/SWChart/SWRadarChart.swift`
```
//
//  SWRadarChart.swift
//  ShipSwift
//
//  Animated radar (spider) chart with axis labels, background grid rings, and
//  radial lines. The data polygon animates from center to full size on appear.
//  Supports 3+ axes with customizable max value.
//
//  Usage:
//    SWRadarChart(data: [
//        .init(label: "Tolerance", value: 75),
//        .init(label: "Ambition", value: 50),
//        .init(label: "Acuity", value: 50),
//        .init(label: "Creativity", value: 85),
//        .init(label: "Stability", value: 85)
//    ])
//    .frame(width: 300, height: 300)
//
//    // Custom max value with hidden labels
//    SWRadarChart(
//        data: [
//            .init(label: "Speed", value: 200),
//            .init(label: "Power", value: 150),
//            .init(label: "Defense", value: 180)
//        ],
//        maxValue: 250,
//        showLabels: false
//    )
//
//  Data Model (built-in):
//    SWRadarChart.DataPoint(label: String, value: Double)
//
//  Parameters:
//    - data: [DataPoint]     — Array of data points, each corresponding to one axis
//    - maxValue: Double      — Maximum value, determines grid scale (default 100)
//    - showLabels: Bool      — Whether to show axis labels (default true)
//
//  Notes:
//    - Grid lines are drawn at 20/40/60/80/100 scale marks
//    - Data polygon uses accentColor for fill and stroke
//    - Appear animation is easeOut 1.2 seconds
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWRadarChart: View {
    // MARK: - Built-in Data Models

    /// Radar chart data point
    struct DataPoint: Identifiable {
        let id: UUID
        let label: String
        let value: Double

        init(id: UUID = UUID(), label: String, value: Double) {
            self.id = id
            self.label = label
            self.value = value
        }
    }

    /// Radar chart shape
    private struct RadarShape: Shape {
        let data: [DataPoint]
        var progress: Double
        let maxValue: Double
        let center: CGPoint
        let radius: CGFloat
        let step: Double

        var animatableData: Double {
            get { progress }
            set { progress = newValue }
        }

        func path(in rect: CGRect) -> Path {
            var path = Path()

            for i in data.indices {
                let ratio = (data[i].value / maxValue) * progress
                let angle = step * Double(i) - .pi / 2
                let x = center.x + cos(angle) * radius * ratio
                let y = center.y + sin(angle) * radius * ratio

                if i == data.startIndex {
                    path.move(to: CGPoint(x: x, y: y))
                } else {
                    path.addLine(to: CGPoint(x: x, y: y))
                }
            }
            path.closeSubpath()

            return path
        }
    }

    /// Text label with bullet point
    private struct BulletPointText<Content: View>: View {
        var bulletColor: Color
        @ViewBuilder var content: Content

        var body: some View {
            HStack(spacing: 4) {
                Capsule()
                    .fill(bulletColor)
                    .frame(width: 3, height: 10)

                content
                    .font(.caption)
            }
        }
    }

    // MARK: - Properties

    let data: [DataPoint]
    let maxValue: Double
    let showLabels: Bool

    @State private var progress: Double = 0

    // MARK: - Initializer

    init(data: [DataPoint], maxValue: Double = 100, showLabels: Bool = true) {
        self.data = data
        self.maxValue = maxValue
        self.showLabels = showLabels
    }

    // MARK: - Body

    var body: some View {
        GeometryReader { geo in
            let size = min(geo.size.width, geo.size.height)
            let center = CGPoint(x: geo.size.width / 2, y: geo.size.height / 2)
            // When showLabels is true, shrink the chart so labels (1.3x) stay within bounds:
            // 0.55 * 1.3 = 0.715, leaving space for text within the radius range
            let radiusFactor: CGFloat = showLabels ? 0.55 : 0.8
            let radius = size / 2 * radiusFactor
            let step = 2 * .pi / Double(data.count)

            ZStack {
                // Draw background ring lines
                ForEach([20, 40, 60, 80, 100], id: \.self) { level in
                    Path { path in
                        for i in data.indices {
                            let ratio = Double(level) / maxValue
                            let angle = step * Double(i) - .pi / 2
                            let x = center.x + cos(angle) * radius * ratio
                            let y = center.y + sin(angle) * radius * ratio

                            if i == data.startIndex {
                                path.move(to: CGPoint(x: x, y: y))
                            } else {
                                path.addLine(to: CGPoint(x: x, y: y))
                            }
                        }
                        path.closeSubpath()
                    }
                    .stroke(
                        Color.secondary.opacity(0.3),
                        style: StrokeStyle(
                            lineWidth: level == 100 ? 1.5 : 1,
                            dash: level == 100 ? [] : [4, 4]
                        )
                    )
                }

                // Draw radial lines from center to corners
                ForEach(data.indices, id: \.self) { index in
                    Path { path in
                        let angle = step * Double(index) - .pi / 2
                        let endX = center.x + cos(angle) * radius
                        let endY = center.y + sin(angle) * radius

                        path.move(to: center)
                        path.addLine(to: CGPoint(x: endX, y: endY))
                    }
                    .stroke(Color.secondary.opacity(0.3), lineWidth: 1)
                }

                // Draw data polygon
                RadarShape(data: data, progress: progress, maxValue: maxValue, center: center, radius: radius, step: step)
                    .stroke(Color.accentColor, lineWidth: 2)

                RadarShape(data: data, progress: progress, maxValue: maxValue, center: center, radius: radius, step: step)
                    .fill(Color.accentColor.opacity(0.2))

                // Labels
                if showLabels {
                    ForEach(Array(data.enumerated()), id: \.element.id) { index, point in
                        let angle = step * Double(index) - .pi / 2
                        let x = center.x + cos(angle) * radius * 1.3
                        let y = center.y + sin(angle) * radius * 1.3

                        VStack {
                            BulletPointText(bulletColor: .secondary) {
                                Text(point.label)
                            }

                            Text(point.value, format: .number.precision(.fractionLength(0)))
                                .fontWeight(.semibold)
                                .font(.footnote)
                        }
                        .position(x: x, y: y)
                    }
                }
            }
            .frame(width: geo.size.width, height: geo.size.height)
            .onAppear {
                progress = 0
                withAnimation(.easeOut(duration: 1.2)) {
                    progress = 1
                }
            }
        }
    }
}

#Preview {
    SWRadarChart(data: [
        .init(label: "Tolerance", value: 75),
        .init(label: "Ambition", value: 50),
        .init(label: "Acuity", value: 50),
        .init(label: "Creativity", value: 85),
        .init(label: "Stability", value: 85)
    ])
    .padding(100)
}
```

## File: `ShipSwift/SWPackage/SWChart/SWRingChart.swift`
```
//
//  SWRingChart.swift
//  ShipSwift
//
//  Nested concentric ring progress chart (Apple Watch Activity Rings style).
//  Each ring animates from 0 to its target value on appear. Includes a bottom legend
//  with colored bullet points. Supports optional center content via generic ViewBuilder.
//
//  Usage:
//    // Basic usage (no center content)
//    SWRingChart(data: [
//        .init(label: "Partner", value: 80, color: .accentColor),
//        .init(label: "Family", value: 91, color: .green),
//        .init(label: "Social", value: 63, color: .orange)
//    ])
//    .padding()
//
//    // With custom center content
//    SWRingChart(data: [
//        .init(label: "Move", value: 75, color: .red),
//        .init(label: "Exercise", value: 50, color: .green),
//        .init(label: "Stand", value: 90, color: .cyan)
//    ]) {
//        VStack {
//            Image(systemName: "flame.fill")
//            Text("Activity")
//        }
//    }
//
//    // Custom dimensions
//    SWRingChart(
//        data: ringData,
//        maxValue: 200,
//        size: 300,
//        ringWidth: 30,
//        spacing: 12
//    )
//
//  Data Model (built-in):
//    SWRingChart.DataPoint
//      - label: String    // Legend label
//      - value: Double    // Progress value (0 to maxValue)
//      - color: Color     // Ring color
//
//  Parameters:
//    - data: [DataPoint]              -- Array of ring data (first element is the outermost ring)
//    - maxValue: Double               -- Maximum value for the ring scale (default 100)
//    - size: CGFloat                  -- Overall chart size (default 250)
//    - ringWidth: CGFloat             -- Width of each ring stroke (default 25)
//    - spacing: CGFloat               -- Spacing between concentric rings (default 10)
//    - center: () -> Center           -- Optional center content (default EmptyView)
//
//  Notes:
//    - Appear animation is easeOut 1.2 seconds, triggered after a 0.2 second delay
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWRingChart<Center: View>: View {
    // MARK: - Built-in Data Model

    /// Ring data point
    struct DataPoint: Identifiable {
        let id = UUID()
        let label: String
        let value: Double
        let color: Color
    }

    // MARK: - Properties

    /// Array of ring data (first element is the outermost ring)
    let data: [DataPoint]

    /// Maximum value for the ring scale
    var maxValue: Double = 100

    /// Overall chart size
    var size: CGFloat = 250

    /// Width of each ring stroke
    var ringWidth: CGFloat = 25

    /// Spacing between concentric rings
    var spacing: CGFloat = 10

    /// Optional center content
    @ViewBuilder let center: () -> Center

    @State private var animatedValues: [Double]

    // MARK: - Initializer

    /// Create a ring chart with optional center content
    /// - Parameters:
    ///   - data: Array of ring data points
    ///   - maxValue: Maximum value for ring scale (default 100)
    ///   - size: Overall chart size (default 250)
    ///   - ringWidth: Width of each ring stroke (default 25)
    ///   - spacing: Spacing between rings (default 10)
    ///   - center: ViewBuilder closure for center content
    init(
        data: [DataPoint],
        maxValue: Double = 100,
        size: CGFloat = 250,
        ringWidth: CGFloat = 25,
        spacing: CGFloat = 10,
        @ViewBuilder center: @escaping () -> Center
    ) {
        self.data = data
        self.maxValue = maxValue
        self.size = size
        self.ringWidth = ringWidth
        self.spacing = spacing
        self.center = center
        self._animatedValues = State(initialValue: Array(repeating: 0, count: data.count))
    }

    // MARK: - Body

    var body: some View {
        VStack {
            // Nested rings
            ZStack {
                ForEach(Array(data.enumerated()), id: \.element.id) { index, item in
                    let ringIndex = CGFloat(data.count - 1 - index)
                    let ringSize = size - ringIndex * (ringWidth + spacing) * 2

                    // Background ring (light color)
                    Circle()
                        .stroke(
                            item.color.opacity(0.15),
                            style: StrokeStyle(lineWidth: ringWidth, lineCap: .round)
                        )
                        .frame(width: ringSize, height: ringSize)

                    // Progress ring
                    Circle()
                        .trim(from: 0, to: animatedValues[index] / maxValue)
                        .stroke(
                            item.color,
                            style: StrokeStyle(lineWidth: ringWidth, lineCap: .round)
                        )
                        .rotationEffect(.degrees(-90))
                        .frame(width: ringSize, height: ringSize)
                }

                center()
            }

            // Legend
            HStack(spacing: 20) {
                ForEach(data) { item in
                    BulletPointText(bulletColor: item.color) {
                        Text(item.label)

                        Text("\(Int(item.value))")
                            .fontWeight(.semibold)
                    }
                }
            }
            .padding(.top)
        }
        .onAppear {
            withAnimation(.easeOut(duration: 1.2).delay(0.2)) {
                for i in data.indices {
                    animatedValues[i] = data[i].value
                }
            }
        }
    }

    // MARK: - Private Components

    /// Text label with bullet point
    private struct BulletPointText<Content: View>: View {
        var bulletColor: Color
        @ViewBuilder var content: Content

        var body: some View {
            HStack(spacing: 4) {
                Capsule()
                    .fill(bulletColor)
                    .frame(width: 3, height: 10)

                content
                    .font(.caption)
            }
        }
    }
}

// MARK: - Convenience Initializer (No Center Content)

extension SWRingChart where Center == EmptyView {
    /// Create a ring chart without center content
    /// - Parameters:
    ///   - data: Array of ring data points
    ///   - maxValue: Maximum value for ring scale (default 100)
    ///   - size: Overall chart size (default 250)
    ///   - ringWidth: Width of each ring stroke (default 25)
    ///   - spacing: Spacing between rings (default 10)
    init(
        data: [DataPoint],
        maxValue: Double = 100,
        size: CGFloat = 250,
        ringWidth: CGFloat = 25,
        spacing: CGFloat = 10
    ) {
        self.init(
            data: data,
            maxValue: maxValue,
            size: size,
            ringWidth: ringWidth,
            spacing: spacing
        ) {
            EmptyView()
        }
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 40) {
        // Example 1: With center content
        SWRingChart(data: [
            .init(label: "Move", value: 75, color: .red),
            .init(label: "Exercise", value: 50, color: .green),
            .init(label: "Stand", value: 90, color: .cyan)
        ]) {
            VStack {
                Image(systemName: "flame.fill")
                    .font(.title)
                    .foregroundStyle(.orange)
                Text("Activity")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }

        Divider()

        // Example 2: Without center content, custom dimensions
        SWRingChart(
            data: [
                .init(label: "Partner", value: 80, color: .accentColor),
                .init(label: "Family", value: 91, color: .green),
                .init(label: "Social", value: 63, color: .orange)
            ],
            size: 200,
            ringWidth: 20,
            spacing: 8
        )
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWChart/SWScatterChart.swift`
```
//
//  SWScatterChart.swift
//  ShipSwift
//
//  Horizontally scrollable scatter chart built on Swift Charts. Supports generic
//  category types (must conform to Hashable & Plottable) with color mapping.
//  Includes a convenience initializer for String categories.
//
//  Usage:
//    // Convenience initializer with String categories
//    let sampleData: [SWScatterChart<String>.DataPoint] = [
//        .init(date: Date(), value: 85, category: "Teeth"),
//        .init(date: Date(), value: 52, category: "Food"),
//    ]
//
//    let colorMapping: [String: Color] = [
//        "Teeth": .blue,
//        "Food": .orange
//    ]
//
//    SWScatterChart(
//        dataPoints: sampleData,
//        colorMapping: colorMapping,
//        title: "Scan Trends"
//    )
//    .padding()
//
//    // Custom Y-axis range and visible days
//    SWScatterChart(
//        dataPoints: temperatureData,
//        colorMapping: tempColorMapping,
//        yDomain: 35...40,
//        visibleDays: 5,
//        chartHeight: 200,
//        title: "Body Temperature"
//    )
//
//  Data Model (built-in):
//    SWScatterChart<CategoryType>.DataPoint
//      - date: Date
//      - value: Double
//      - category: CategoryType
//
//  Parameters:
//    - dataPoints: [DataPoint]              — Array of data points
//    - colorMapping: [CategoryType: Color]  — Category to color mapping
//    - yDomain: ClosedRange<Double>         — Y-axis range (default 0...100)
//    - scrollableDaysBack: Int              — Scrollable days backward (default 30)
//    - scrollableDaysForward: Int           — Scrollable days forward (default 7)
//    - visibleDays: Int                     — Visible days range (default 7)
//    - chartHeight: CGFloat                 — Chart height (default 180)
//    - title: String?                       — Optional title
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import Charts

// MARK: - SWScatterChart

struct SWScatterChart<CategoryType: Hashable & Plottable>: View {
    // MARK: - Built-in Data Model

    /// Data point model
    struct DataPoint: Identifiable {
        let id: UUID
        let date: Date
        let value: Double
        let category: CategoryType

        init(id: UUID = UUID(), date: Date, value: Double, category: CategoryType) {
            self.id = id
            self.date = date
            self.value = value
            self.category = category
        }
    }

    // MARK: - Properties

    /// Array of data points
    let dataPoints: [DataPoint]

    /// Color mapping for categories
    let colorMapping: [CategoryType: Color]

    /// Y-axis range
    var yDomain: ClosedRange<Double> = 0...100

    /// X-axis scrollable total range (days back from today)
    var scrollableDaysBack: Int = 30

    /// X-axis scrollable total range (days forward from today)
    var scrollableDaysForward: Int = 7

    /// Visible range (days)
    var visibleDays: Int = 7

    /// Chart height
    var chartHeight: CGFloat = 180

    /// Title (optional)
    var title: String? = nil

    // MARK: - Computed Properties

    /// X-axis scrollable total range
    private var chartXDomain: ClosedRange<Date> {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        let startDate = calendar.date(byAdding: .day, value: -scrollableDaysBack, to: startOfToday)!
        let endDate = calendar.date(byAdding: .day, value: scrollableDaysForward, to: startOfToday)!
        return startDate...endDate
    }

    /// Chart initial scroll position: center today in the visible range
    private var chartInitialScrollDate: Date {
        let calendar = Calendar.current
        let startOfToday = calendar.startOfDay(for: Date())
        // Visible range is N days; to center today, start N/2 days back
        let offset = visibleDays / 2
        return calendar.date(byAdding: .day, value: -offset, to: startOfToday)!
    }

    /// Visible range time length (seconds)
    private var visibleDomainLength: Int {
        visibleDays * 24 * 60 * 60
    }

    // MARK: - Body

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Title
            if let title = title {
                Text(title)
                    .font(.title3)
                    .fontWeight(.semibold)
            }

            // Chart
            Chart(dataPoints) { point in
                PointMark(
                    x: .value("Date", point.date),
                    y: .value("Value", point.value)
                )
                .foregroundStyle(by: .value("Category", point.category))
            }
            .chartForegroundStyleScale(
                domain: Array(colorMapping.keys),
                range: Array(colorMapping.values)
            )
            .chartXScale(domain: chartXDomain)
            .chartYScale(domain: yDomain)
            .chartScrollableAxes(.horizontal)
            .chartXVisibleDomain(length: visibleDomainLength)
            .chartScrollPosition(initialX: chartInitialScrollDate)
            .chartYAxis {
                AxisMarks(position: .leading, values: .automatic(desiredCount: 5)) { value in
                    AxisGridLine()
                    AxisValueLabel()
                }
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: .day, count: 1)) { value in
                    AxisGridLine()
                    AxisValueLabel(format: .dateTime.month(.abbreviated).day())
                }
            }
            .chartLegend(position: .top, alignment: .trailing)
            .frame(height: chartHeight)
        }
    }
}

// MARK: - Convenience Initializer for String Category

extension SWScatterChart where CategoryType == String {
    /// Convenience initializer (using String as category type)
    init(
        dataPoints: [DataPoint],
        colorMapping: [String: Color],
        yDomain: ClosedRange<Double> = 0...100,
        scrollableDaysBack: Int = 30,
        scrollableDaysForward: Int = 7,
        visibleDays: Int = 7,
        chartHeight: CGFloat = 180,
        title: String? = nil
    ) {
        self.dataPoints = dataPoints
        self.colorMapping = colorMapping
        self.yDomain = yDomain
        self.scrollableDaysBack = scrollableDaysBack
        self.scrollableDaysForward = scrollableDaysForward
        self.visibleDays = visibleDays
        self.chartHeight = chartHeight
        self.title = title
    }
}

// MARK: - Preview

#Preview {
    ScrollView {
        VStack(spacing: 32) {
            // Example 1: Basic scatter chart
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let sampleData: [SWScatterChart<String>.DataPoint] = [
                    .init(date: calendar.date(byAdding: .hour, value: 8, to: today)!, value: 85, category: "Teeth"),
                    .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 52, category: "Food"),
                    .init(date: calendar.date(byAdding: .hour, value: 18, to: today)!, value: 78, category: "Food"),
                    .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 72, category: "Teeth"),
                    .init(date: calendar.date(byAdding: .hour, value: -18, to: today)!, value: 65, category: "Food"),
                    .init(date: calendar.date(byAdding: .day, value: -2, to: today)!, value: 90, category: "Teeth"),
                    .init(date: calendar.date(byAdding: .day, value: -3, to: today)!, value: 45, category: "Food"),
                    .init(date: calendar.date(byAdding: .day, value: -3, to: today)!, value: 88, category: "Teeth"),
                ]

                SWScatterChart(
                    dataPoints: sampleData,
                    colorMapping: ["Teeth": .blue, "Food": .orange],
                    title: "Scan Trends"
                )
            }

            Divider()

            // Example 2: Custom Y domain
            Group {
                let calendar = Calendar.current
                let today = calendar.startOfDay(for: Date())

                let temperatureData: [SWScatterChart<String>.DataPoint] = [
                    .init(date: calendar.date(byAdding: .hour, value: 6, to: today)!, value: 36.2, category: "Morning"),
                    .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 36.8, category: "Noon"),
                    .init(date: calendar.date(byAdding: .hour, value: 20, to: today)!, value: 37.1, category: "Evening"),
                    .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 36.5, category: "Morning"),
                ]

                SWScatterChart(
                    dataPoints: temperatureData,
                    colorMapping: ["Morning": .cyan, "Noon": .yellow, "Evening": .purple],
                    yDomain: 35...40,
                    visibleDays: 5,
                    chartHeight: 200,
                    title: "Body Temperature"
                )
            }

            Divider()

            // Example 3: Empty state
            SWScatterChart<String>(
                dataPoints: [],
                colorMapping: ["Type A": .blue, "Type B": .green],
                title: "No Data Yet"
            )
        }
        .padding()
    }
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWBulletPointText.swift`
```
//
//  SWBulletPointText.swift
//  ShipSwift
//
//  Text label with a colored capsule bullet point indicator.
//  Accepts any View content via @ViewBuilder, displayed to the right of the bullet.
//
//  Usage:
//    // Simple text
//    SWBulletPointText(bulletColor: .blue) {
//        Text("Wealth")
//    }
//
//    // Custom content (HStack, Image, etc.)
//    SWBulletPointText(bulletColor: .green) {
//        HStack {
//            Text("Health")
//            Image(systemName: "heart.fill")
//        }
//    }
//
//  Parameters:
//    - bulletColor: Color  — Bullet point color
//    - content: @ViewBuilder — Any view displayed to the right of the bullet
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWBulletPointText<Content: View>: View {
    var bulletColor: Color
    @ViewBuilder var content: Content

    var body: some View {
        HStack(spacing: 6) {
            Capsule()
                .fill(bulletColor)
                .frame(width: 4, height: 12)

            content
                .font(.subheadline)
        }
    }
}

#Preview {
    VStack(alignment: .leading, spacing: 10) {
        // Simple text
        SWBulletPointText(bulletColor: .blue) {
            Text("Wealth")
        }

        // HStack content
        SWBulletPointText(bulletColor: .green) {
            HStack {
                Text("Health")
                Image(systemName: "heart.fill")
            }
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWFloatingLabels.swift`
```
//
//  SWFloatingLabels.swift
//  ShipSwift
//
//  Displays an image with animated floating capsule labels that fade in
//  and out at specified positions around the image. Useful for showcasing
//  feature callouts, AI analysis results, or point-of-interest annotations.
//
//  Usage:
//    SWFloatingLabels(
//        image: Image("myPhoto"),
//        size: 360,               // image frame size, default 360
//        cornerRadius: 24,        // default 24
//        cycleDuration: 3.0,      // animation cycle in seconds, default 3.0
//        labels: [
//            // Normalized position 0-1 where 0.5 is center
//            .init(text: "Teeth mapping",    position: CGPoint(x: 0.3, y: 0.5)),
//            .init(text: "Plaque detection", position: CGPoint(x: 0.9, y: 0.6)),
//            .init(text: "Shape & balance",  position: CGPoint(x: 0.5, y: 0.8))
//        ]
//    )
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWFloatingLabels: View {

    // MARK: - Nested Types

    /// Data model for a single floating label
    struct LabelItem: Identifiable {
        let id = UUID()
        let text: String
        let position: CGPoint
    }

    // MARK: - Configuration

    let image: Image
    var size: CGFloat = 360
    var cornerRadius: CGFloat = 24
    var cycleDuration: Double = 3.0
    var labels: [LabelItem] = []

    // MARK: - Body

    var body: some View {
        TimelineView(.animation) { timeline in
            let t = timeline.date.timeIntervalSinceReferenceDate
            let cycle = t.truncatingRemainder(dividingBy: cycleDuration)

            ZStack {
                // Image with gradient border
                image
                    .resizable()
                    .scaledToFill()
                    .frame(width: size, height: size)
                    .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
                    .overlay(
                        RoundedRectangle(cornerRadius: cornerRadius)
                            .stroke(
                                LinearGradient(
                                    colors: [.cyan.opacity(0.8), .blue.opacity(0.6)],
                                    startPoint: .topLeading,
                                    endPoint: .bottomTrailing
                                ),
                                lineWidth: 2
                            )
                            .opacity(cycle < 0.5 ? cycle * 2 : 1)
                    )

                // Cycle through labels
                ForEach(Array(labels.enumerated()), id: \.element.id) { index, label in
                    let delay = Double(index) * 0.3
                    let labelCycle = (cycle - delay).truncatingRemainder(dividingBy: cycleDuration)
                    let opacity = labelCycle > 0.5 && labelCycle < (cycleDuration - 0.5) ? 1.0 : 0.0

                    FloatingLabel(text: label.text)
                        .offset(
                            x: (label.position.x - 0.5) * (size * 0.78),
                            y: (label.position.y - 0.5) * (size * 0.78)
                        )
                        .opacity(opacity)
                        .scaleEffect(opacity > 0 ? 1 : 0.8)
                        .animation(.easeInOut(duration: 0.3), value: opacity)
                }
            }
        }
    }

    // MARK: - Floating Label (Internal)

    /// Capsule-style label used as an internal implementation detail
    private struct FloatingLabel: View {
        let text: String

        var body: some View {
            Text(text)
                .font(.footnote)
                .foregroundStyle(.white)
                .padding(.horizontal, 12)
                .padding(.vertical, 6)
                .background(
                    Capsule()
                        .fill(.ultraThinMaterial)
                )
        }
    }
}

// MARK: - Preview

#Preview {
    SWFloatingLabels(
        image: Image(.facePicture),
        labels: [
            .init(text: "Teeth mapping",    position: CGPoint(x: 0.3, y: 0.5)),
            .init(text: "Plaque detection", position: CGPoint(x: 0.9, y: 0.6)),
            .init(text: "Shape & balance",  position: CGPoint(x: 0.5, y: 0.8))
        ]
    )
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWGradientDivider.swift`
```
//
//  SWGradientDivider.swift
//  ShipSwift
//
//  Horizontal divider with a center-fade gradient (clear -> color -> clear).
//
//  Usage:
//    SWGradientDivider()                                  // cyan, 0.3 opacity, 1pt
//    SWGradientDivider(color: .purple, opacity: 0.5)      // purple variant
//    SWGradientDivider(color: .mint, height: 2)            // thicker mint line
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWGradientDivider: View {
    var color: Color = .cyan
    var opacity: Double = 0.3
    var height: CGFloat = 1

    var body: some View {
        Rectangle()
            .fill(
                LinearGradient(
                    colors: [.clear, color.opacity(opacity), .clear],
                    startPoint: .leading,
                    endPoint: .trailing
                )
            )
            .frame(height: height)
    }
}

#Preview {
    VStack(spacing: 20) {
        SWGradientDivider()
        SWGradientDivider(color: .purple, opacity: 0.5)
        SWGradientDivider(color: .mint, height: 2)
    }
    .padding()
    .background(Color.black)
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWLabel.swift`
```
//
//  SWLabel.swift
//  ShipSwift
//
//  Reusable label components that pair a leading visual (SF Symbol or image
//  resource) with a localized text name. Commonly used in List rows,
//  settings screens, or menu items.
//
//  Usage:
//    // Label with an SF Symbol icon on a colored circle
//    SWLabelWithIcon(
//        icon: "gearshape",          // SF Symbol name, default "pencil"
//        bg: .orange,                // circle background color, default .blue
//        name: "Settings"            // LocalizedStringResource
//    )
//
//    // Label with a custom image resource
//    SWLabelWithImage(
//        image: .appIcon,            // ImageResource from asset catalog
//        name: "My App"              // LocalizedStringResource
//    )
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWLabelWithIcon: View {
    var icon: String = "pencil"
    var bg: Color = .blue
    var name: LocalizedStringResource = "Name"
    
    var body: some View {
        HStack {
            ZStack {
                Circle()
                    .frame(width: 32, height: 32)
                    .foregroundStyle(bg.gradient.opacity(0.9))
                Image(systemName: icon)
                    .fontWeight(.light)
                    .foregroundStyle(.ultraThickMaterial)
            }
            .padding(5)
            Text(name)
        }
    }
}

struct SWLabelWithImage: View {
    var image: ImageResource
    var name: LocalizedStringResource = "Name"
    var body: some View {
        HStack {
            Image(image)
                .resizable()
                .scaledToFit()
                .frame(width: 32, height: 32)
                .clipShape(RoundedRectangle(cornerRadius: 6))
                .padding(5)
            Text(name)
        }
    }
}

// MARK: - Preview

#Preview {
    VStack(alignment: .leading) {
        SWLabelWithIcon()
        
        SWLabelWithIcon(
            icon: "gearshape",
            bg: .orange,
            name: "Settings"
        )
        
        SWLabelWithIcon(
            icon: "bell.badge",
            bg: .red,
            name: "Notifications"
        )
        
        SWLabelWithIcon(
            icon: "lock.shield",
            bg: .green,
            name: "Privacy"
        )
        
        SWLabelWithIcon(
            icon: "creditcard",
            bg: .purple,
            name: "Subscription"
        )

        Divider()

        SWLabelWithImage(
            image: .fullpackLogo,
            name: "FullPack"
        )
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWMarkdownText.swift`
```
//
//  SWMarkdownText.swift
//  ShipSwift
//
//  Custom Markdown rendering view for common LLM output formats.
//  Supports headings, bold, italic, inline code, fenced code blocks,
//  unordered/ordered lists, and horizontal dividers.
//
//  Works on both iOS and macOS — no platform-specific imports needed.
//
//  Usage:
//    SWMarkdownText("# Hello\nSome **bold** and *italic* text.")
//
//    SWMarkdownText(
//        "```swift\nprint(\"hi\")\n```",
//        codeBackground: .gray.opacity(0.15),
//        codeCornerRadius: 10
//    )
//
//  Parameters:
//    - text: String                — Raw Markdown string to render
//    - codeBackground: Color       — Background color for fenced code blocks (default: secondary fill)
//    - codeBorderColor: Color      — Border color for fenced code blocks (default: secondary)
//    - codeCornerRadius: CGFloat   — Corner radius for code blocks (default: 8)
//    - blockSpacing: CGFloat       — Vertical spacing between blocks (default: 6)
//
//  Created by Wei Zhong on 3/10/26.
//

import SwiftUI

// MARK: - SWMarkdownText

public struct SWMarkdownText: View {
    public let text: String
    public var codeBackground: Color
    public var codeBorderColor: Color
    public var codeCornerRadius: CGFloat
    public var blockSpacing: CGFloat

    public init(
        _ text: String,
        codeBackground: Color = .gray.opacity(0.12),
        codeBorderColor: Color = .secondary,
        codeCornerRadius: CGFloat = 8,
        blockSpacing: CGFloat = 6
    ) {
        self.text = text
        self.codeBackground = codeBackground
        self.codeBorderColor = codeBorderColor
        self.codeCornerRadius = codeCornerRadius
        self.blockSpacing = blockSpacing
    }

    public var body: some View {
        if text.isEmpty {
            EmptyView()
        } else {
            VStack(alignment: .leading, spacing: blockSpacing) {
                ForEach(Array(parseBlocks().enumerated()), id: \.offset) { _, block in
                    blockView(for: block)
                }
            }
        }
    }

    // MARK: - Block Rendering

    @ViewBuilder
    private func blockView(for block: SWMarkdownBlock) -> some View {
        switch block {
        case .heading(let level, let content):
            headingView(level: level, content: content)

        case .codeBlock(let language, let code):
            codeBlockView(language: language, code: code)

        case .divider:
            Divider()
                .padding(.vertical, 4)

        case .listItem(let content):
            HStack(alignment: .firstTextBaseline, spacing: 6) {
                Text("\u{2022}")
                    .foregroundStyle(.secondary)
                inlineMarkdownText(content)
            }
            .padding(.leading, 12)

        case .paragraph(let content):
            inlineMarkdownText(content)
        }
    }

    // MARK: - Heading

    private func headingView(level: Int, content: String) -> some View {
        let font: Font = switch level {
        case 1: .title.bold()
        case 2: .title2.bold()
        case 3: .title3.bold()
        default: .headline.bold()
        }
        return inlineMarkdownText(content)
            .font(font)
            .padding(.top, level <= 2 ? 6 : 2)
    }

    // MARK: - Fenced Code Block

    private func codeBlockView(language: String, code: String) -> some View {
        VStack(alignment: .leading, spacing: 0) {
            // Language label
            if !language.isEmpty {
                Text(language)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .padding(.horizontal, 10)
                    .padding(.top, 6)
                    .padding(.bottom, 2)
            }
            // Code content
            ScrollView(.horizontal, showsIndicators: false) {
                Text(code)
                    .font(.system(.body, design: .monospaced))
                    .textSelection(.enabled)
                    .padding(10)
            }
        }
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(codeBackground.opacity(0.6))
        .clipShape(RoundedRectangle(cornerRadius: codeCornerRadius))
        .overlay(
            RoundedRectangle(cornerRadius: codeCornerRadius)
                .strokeBorder(codeBorderColor.opacity(0.5), lineWidth: 0.5)
        )
    }

    // MARK: - Inline Markdown (bold, italic, inline code)

    private func inlineMarkdownText(_ text: String) -> Text {
        // Parse inline Markdown using AttributedString with whitespace preservation
        if let attributed = try? AttributedString(
            markdown: text,
            options: .init(interpretedSyntax: .inlineOnlyPreservingWhitespace)
        ) {
            return Text(attributed)
        }
        return Text(text)
    }

    // MARK: - Block Parser

    private func parseBlocks() -> [SWMarkdownBlock] {
        var blocks: [SWMarkdownBlock] = []
        let lines = text.components(separatedBy: "\n")
        var i = 0

        while i < lines.count {
            let line = lines[i]
            let trimmed = line.trimmingCharacters(in: .whitespaces)

            // Fenced code block: starts with ```
            if trimmed.hasPrefix("```") {
                let language = String(trimmed.dropFirst(3)).trimmingCharacters(in: .whitespaces)
                var codeLines: [String] = []
                i += 1
                while i < lines.count {
                    let codeLine = lines[i]
                    if codeLine.trimmingCharacters(in: .whitespaces).hasPrefix("```") {
                        i += 1
                        break
                    }
                    codeLines.append(codeLine)
                    i += 1
                }
                blocks.append(.codeBlock(language: language, code: codeLines.joined(separator: "\n")))
                continue
            }

            // Horizontal divider: ---, ***, ___ (at least 3 identical characters)
            if isDivider(trimmed) {
                blocks.append(.divider)
                i += 1
                continue
            }

            // Heading: # through ####
            if let (level, content) = parseHeading(trimmed) {
                blocks.append(.heading(level: level, content: content))
                i += 1
                continue
            }

            // Unordered list item: -, *, or + followed by a space
            if let content = parseUnorderedListItem(trimmed) {
                blocks.append(.listItem(content: content))
                i += 1
                continue
            }

            // Ordered list item: 1. 2. etc.
            if let content = parseOrderedListItem(trimmed) {
                blocks.append(.listItem(content: content))
                i += 1
                continue
            }

            // Empty line — skip
            if trimmed.isEmpty {
                i += 1
                continue
            }

            // Paragraph: merge consecutive non-empty lines
            var paragraphLines: [String] = [line]
            i += 1
            while i < lines.count {
                let nextLine = lines[i]
                let nextTrimmed = nextLine.trimmingCharacters(in: .whitespaces)
                // End paragraph on empty line, heading, list, code fence, or divider
                if nextTrimmed.isEmpty ||
                    parseHeading(nextTrimmed) != nil ||
                    nextTrimmed.hasPrefix("```") ||
                    parseUnorderedListItem(nextTrimmed) != nil ||
                    parseOrderedListItem(nextTrimmed) != nil ||
                    isDivider(nextTrimmed) {
                    break
                }
                paragraphLines.append(nextLine)
                i += 1
            }
            blocks.append(.paragraph(content: paragraphLines.joined(separator: "\n")))
        }

        return blocks
    }

    // MARK: - Parsing Helpers

    /// Parse heading line (# through ####), returning (level, content).
    private func parseHeading(_ line: String) -> (Int, String)? {
        var level = 0
        var idx = line.startIndex
        while idx < line.endIndex && line[idx] == "#" && level < 4 {
            level += 1
            idx = line.index(after: idx)
        }
        guard level > 0, idx < line.endIndex, line[idx] == " " else { return nil }
        let content = String(line[line.index(after: idx)...]).trimmingCharacters(in: .whitespaces)
        guard !content.isEmpty else { return nil }
        return (level, content)
    }

    /// Parse unordered list item: line starting with -, *, or + followed by a space.
    private func parseUnorderedListItem(_ line: String) -> String? {
        guard let first = line.first, "-*+".contains(first),
              line.count >= 2,
              line[line.index(after: line.startIndex)] == " " else { return nil }
        let content = String(line.dropFirst(2)).trimmingCharacters(in: .whitespaces)
        return content.isEmpty ? nil : content
    }

    /// Parse ordered list item: line starting with digits followed by ". ".
    private func parseOrderedListItem(_ line: String) -> String? {
        guard let dotIndex = line.firstIndex(of: ".") else { return nil }
        let prefix = line[line.startIndex..<dotIndex]
        guard !prefix.isEmpty, prefix.allSatisfy(\.isNumber) else { return nil }
        let afterDot = line.index(after: dotIndex)
        guard afterDot < line.endIndex, line[afterDot] == " " else { return nil }
        let content = String(line[line.index(after: afterDot)...]).trimmingCharacters(in: .whitespaces)
        return content.isEmpty ? nil : content
    }

    /// Check whether the line is a horizontal divider (---, ***, or ___).
    private func isDivider(_ line: String) -> Bool {
        guard line.count >= 3 else { return false }
        return line.allSatisfy({ $0 == "-" }) ||
               line.allSatisfy({ $0 == "*" }) ||
               line.allSatisfy({ $0 == "_" })
    }
}

// MARK: - Block Type (internal)

private enum SWMarkdownBlock {
    case heading(level: Int, content: String)
    case codeBlock(language: String, code: String)
    case divider
    case listItem(content: String)
    case paragraph(content: String)
}

// MARK: - Preview

#Preview {
    ScrollView {
        SWMarkdownText("""
        # Heading 1
        ## Heading 2
        ### Heading 3

        This is a paragraph with **bold** and *italic* text.

        Here is `inline code` in a sentence.

        ```swift
        func greet() {
            print("Hello, world!")
        }
        ```

        - First item
        - Second item with **bold**
        - Third item

        1. Ordered item one
        2. Ordered item two

        ---

        Another paragraph after the divider.
        """)
        .padding()
    }
    .frame(width: 500, height: 600)
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWOnboardingView.swift`
```
//
//  SWOnboardingView.swift
//  ShipSwift
//
//  Multi-page onboarding view with swipe-to-navigate support, a "Continue / Get Started"
//  button and a "Skip" button at the bottom. Page content is defined by the OnboardingPage
//  enum (icon / title / description) — add or remove cases freely.
//
//  Usage:
//    // 1. Present the onboarding at app launch or first run; handle completion/skip via onComplete:
//    SWOnboardingView(onComplete: {
//        hasSeenOnboarding = true
//    })
//
//    // 2. Customize pages: modify the OnboardingPage enum, add/remove cases and provide icon / title / description:
//    enum OnboardingPage: CaseIterable {
//        case shipFast
//        case components
//        case modular
//        case launch
//        // To add a new page, simply add a case and implement the three computed properties
//    }
//
//    // 3. Use with fullScreenCover:
//    .fullScreenCover(isPresented: $showOnboarding) {
//        SWOnboardingView(onComplete: { showOnboarding = false })
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - Onboarding Main View
struct SWOnboardingView: View {
    let onComplete: () -> Void

    private let pages = OnboardingPage.allCases
    @State private var currentPage = 0

    var body: some View {
        VStack {
            TabView(selection: $currentPage) {
                ForEach(Array(pages.enumerated()), id: \.element) { index, page in
                    VStack(spacing: 24) {
                        Spacer()

                        Image(systemName: page.icon)
                            .font(.system(size: 80))
                            .foregroundStyle(.tint)
                        Text(page.title)
                            .font(.title)
                            .fontWeight(.bold)
                        Text(page.description)
                            .foregroundStyle(.secondary)

                        Spacer()
                        Spacer()
                    }
                    .tag(index)
                    .padding(.horizontal)
                }
            }
            #if os(iOS)
            .tabViewStyle(.page(indexDisplayMode: .always))
            .indexViewStyle(.page(backgroundDisplayMode: .always))
            #endif

            // Bottom confirm button
            Button {
                if currentPage < pages.count - 1 {
                    withAnimation {
                        currentPage += 1
                    }
                } else {
                    onComplete()
                }
            } label: {
                Text(currentPage < pages.count - 1 ? "Continue" : "Get Started")
            }
            .buttonStyle(.swPrimary)
            .padding(.bottom)

            // Bottom skip button
            Button {
                onComplete()
            } label: {
                Text("Skip")
                    .foregroundStyle(.secondary)
            }
            .opacity(currentPage < pages.count - 1 ? 0 : 1)
        }
        .safeAreaPadding(.horizontal)
    }
}

// MARK: - Onboarding Page Model
enum OnboardingPage: CaseIterable {
    case shipFast
    case components
    case modular
    case launch

    var icon: String {
        switch self {
        case .shipFast: "cpu.fill"
        case .components: "doc.text.fill"
        case .modular: "terminal.fill"
        case .launch: "paperplane.fill"
        }
    }

    var title: String {
        switch self {
        case .shipFast: "AI-First Development"
        case .components: "Production-Ready Recipes"
        case .modular: "One Command Setup"
        case .launch: "Ship 10x Faster"
        }
    }

    var description: String {
        switch self {
        case .shipFast: "Recipes structured for AI models — Claude, Cursor, Windsurf get production-grade context instantly."
        case .components: "Auth, camera, AI chat, in-app purchase — every recipe battle-tested in real App Store apps."
        case .modular: "Connect via MCP with one command. No downloads, no setup, no dependencies to manage."
        case .launch: "Stop rebuilding auth and payments from scratch. Focus on what makes your app unique."
        }
    }
}

// MARK: - Preview
#Preview("Onboarding") {
    SWOnboardingView(onComplete: { print("Done") })
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWOrderView.swift`
```
//
//  SWOrderView.swift
//  ShipSwift
//
//  Animated drink customization demo page showcasing SwiftUI animation capabilities:
//  flavor selection, cup size switching, gradient background animation,
//  matchedGeometryEffect selector, and cup scale/offset animation.
//  Can be used as a reference template for product customization pages.
//
//  Usage:
//    // 1. Present the view directly (best used full-screen; includes built-in gradient background):
//    SWOrderView()
//
//    // 2. Internal components can be reused independently:
//    //    - SWOrderSelector: Capsule-shaped selector with matchedGeometryEffect
//    SWOrderSelector(items: ["S", "M", "L"], sel: $size, ns: sizeNS, label: "Size")
//
//    //    - SWQuantityControl: +/- stepper with numeric text transition
//    SWQuantityControl(qty: $qty)
//
//    //    - SWCupView: Animated cup image display with size-based scaling
//    SWCupView(idx: 0, count: 1, img: "Matcha", size: "Medium")
//
//    // 3. Customize flavors/sizes: modify the flavors and sizes arrays,
//    //    and add corresponding image mappings in SWCupView.image and colors in SWOrderView.bg.
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWOrderView

struct SWOrderView: View {
    @State private var qty: Int = 1
    @State private var flavor: String = "Matcha"
    @State private var size: String = "Medium"
    @Namespace private var sizeNS
    @Namespace private var flavorNS
    
    private let flavors = ["Matcha", "Chocolate", "Latte"]
    private let sizes = ["Medium", "Large", "XL"]
    
    private var bg: Color {
        switch flavor {
        case "Latte":
            return Color(red: 0.76, green: 0.6, blue: 0.42)
        case "Chocolate":
            return .brown
        default:
            return Color(red: 0.2, green: 0.5, blue: 0.3)
        }
    }
    
    var body: some View {
        ZStack {
            backgroundGradient
            #if os(macOS)
            ScrollView {
                contentView
                    .padding(.vertical)
            }
            #else
            contentView
            #endif
        }
    }
    
    private var backgroundGradient: some View {
        LinearGradient(colors: [.black, bg],
                       startPoint: .top, endPoint: .bottom)
        #if os(iOS)
        .ignoresSafeArea()
        #endif
        .animation(.easeInOut, value: flavor)
    }
    
    private var contentView: some View {
        VStack(spacing: 30) {
            cupsSection
            quantityControl
            selectorsSection
            Spacer()
            addToCartButton
        }
    }
    
    private var cupsSection: some View {
        ZStack {
            ForEach(Array(0..<qty), id: \.self) { i in
                SWCupView(idx: i, count: qty, img: flavor, size: size)
            }
        }
        #if os(macOS)
        .frame(height: 280)
        #else
        .frame(height: 500)
        #endif
        .animation(.spring(), value: qty)
    }
    
    private var quantityControl: some View {
        SWQuantityControl(qty: $qty)
    }
    
    private var selectorsSection: some View {
        VStack(spacing: 20) {
            SWOrderSelector(items: sizes, sel: $size, ns: sizeNS, label: "Size")
            SWOrderSelector(items: flavors, sel: $flavor, ns: flavorNS, label: "Flavor")
        }
    }
    
    private var addToCartButton: some View {
        Button {
            
        } label: {
            Text("Add to Cart   ¥\(33 * qty)")
                .font(.title3.bold())
                .frame(maxWidth: .infinity, minHeight: 56)
                .background(.white)
                .foregroundStyle(bg)
                .clipShape(Capsule())
                .padding()
        }
    }
}

// MARK: - SWCupView

struct SWCupView: View {
    let idx: Int
    let count: Int
    let img: String
    let size: String

    private var image: ImageResource {
        switch img {
        case "Matcha":  return .matcha
        case "Chocolate": return .chocolate
        case "Latte": return .latte
        default: return .latte
        }
    }

    private var cupHeight: CGFloat {
        switch size {
        case "Large": return 320
        case "XL": return 380
        default: return 260
        }
    }

    private var isSide: Bool {
        count == 2 || (count >= 3 && idx != 1)
    }

    private var xOffset: CGFloat {
        switch count {
        case 2:  return idx == 0 ? -60 : 60
        case 3:  return idx == 0 ? -80 : idx == 2 ? 80 : 0
        default: return 0
        }
    }

    var body: some View {
        Image(image)
            .resizable()
            .scaledToFit()
            .frame(height: cupHeight)
            .scaleEffect(isSide ? 0.75 : 1.0)
            .offset(x: xOffset)
            .zIndex(count == 3 && idx == 1 ? 10 : Double(idx))
            .shadow(color: .black.opacity(0.3), radius: 15, y: 10)
            .animation(.easeInOut, value: img)
            .animation(.easeInOut, value: size)
            .transition(.asymmetric(
                insertion: .scale(scale: 0.1).combined(with: .opacity),
                removal: .opacity
            ))
    }
}

// MARK: - SWOrderSelector

struct SWOrderSelector: View {
    let items: [String]
    @Binding var sel: String
    var ns: Namespace.ID
    var label: String
    
    var body: some View {
        HStack {
            Text(label)
                .bold()
                .foregroundStyle(.white)
                .frame(width: 60)
            HStack {
                ForEach(items, id: \.self) { item in
                    itemButton(item)
                }
            }
            .padding(4)
            .background(.white.opacity(0.1), in: Capsule())
        }
        .padding(.horizontal)
    }
    
    private func itemButton(_ item: String) -> some View {
        Text(item)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 8)
            .foregroundStyle(sel == item ? .white : .white.opacity(0.6))
            .background {
                if sel == item {
                    Capsule()
                        .fill(.white.opacity(0.2))
                        .matchedGeometryEffect(id: "selector", in: ns)
                }
            }
            .onTapGesture {
                withAnimation(.spring()) {
                    sel = item
                }
            }
    }
}

// MARK: - SWQuantityControl

struct SWQuantityControl: View {
    @Binding var qty: Int
    
    var body: some View {
        HStack(spacing: 40) {
            Button { if qty > 1 { qty -= 1 } } label: {
                Image(systemName: "minus.circle.fill")
                    .font(.largeTitle)
                    .foregroundStyle(.white, .ultraThinMaterial)
            }
            
            Text("\(qty)")
                .font(.system(size: 40, weight: .black))
                .contentTransition(.numericText())
                .frame(width: 60)
            
            Button { if qty < 3 { qty += 1 } } label: {
                Image(systemName: "plus.circle.fill")
                    .font(.largeTitle)
                    .foregroundStyle(.white, .ultraThinMaterial)
            }
        }
        .foregroundStyle(Color.white)
    }
}

// MARK: - SWOrderButton

struct SWOrderButton: View {
    let icon: String
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            Image(systemName: icon)
                .frame(width: 44, height: 44)
                .background(.white.opacity(0.2), in: Circle())
        }
    }
}

#Preview {
    SWOrderView()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWRootTabView.swift`
```
//
//  SWRootTabView.swift
//  ShipSwift
//
//  Root TabView template using the iOS 18+ Tab API, with selected/unselected icon
//  switching, native search tab, and haptic feedback. Uses
//  .environment(\.symbolVariants, .none) to prevent the system from auto-filling icons.
//
//  Usage:
//    // 1. Use directly as the app root view:
//    @main struct MyApp: App {
//        var body: some Scene {
//            WindowGroup { SWRootTabView() }
//        }
//    }
//
//    // 2. Customize tabs: modify the Tab entries inside the TabView. Each tab follows this pattern:
//    Tab(value: "tabID") {
//        YourContentView()           // Replace with your page
//    } label: {
//        Label {
//            Text("Tab Name")
//        } icon: {
//            Image(systemName: selectedTab == "tabID" ? "icon.fill" : "icon")
//        }
//        .environment(\.symbolVariants, .none)
//    }
//
//    // 3. Add or remove tabs: simply add or delete Tab entries in the TabView closure.
//    //    Set the selectedTab default value to the first tab's value string.
//
//    // 4. Search tab: uses .searchable() on NavigationStack for native search bar.
//    //    Replace ContentUnavailableView with your search results view.
//
//    // 5. Haptic feedback: built in via .sensoryFeedback(.increase, trigger: selectedTab),
//    //    triggered automatically on tab switch.
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWRootTabView: View {
    @State private var selectedTab = "home"
    @State private var searchText = ""

    var body: some View {
        TabView(selection: $selectedTab) {
            Tab(value: "home") {
                NavigationStack {
                    ScrollView {
                        ContentUnavailableView("Home", systemImage: "house.fill", description: Text("Your main feed and dashboard content goes here."))
                            .containerRelativeFrame(.vertical)
                    }
                    .navigationTitle("Home")
                }
            } label: {
                Label {
                    Text("Home")
                } icon: {
                    Image(systemName: selectedTab == "home" ? "house.fill" : "house")
                }
                .environment(\.symbolVariants, .none)
            }

            Tab(value: "outfit") {
                NavigationStack {
                    ScrollView {
                        ContentUnavailableView("Outfit", systemImage: "tshirt.fill", description: Text("Browse and manage your outfit collections here."))
                            .containerRelativeFrame(.vertical)
                    }
                    .navigationTitle("Outfit")
                }
            } label: {
                Label {
                    Text("Outfit")
                } icon: {
                    Image(systemName: selectedTab == "outfit" ? "tshirt.fill" : "tshirt")
                }
                .environment(\.symbolVariants, .none)
            }

            Tab(value: "setting") {
                NavigationStack {
                    ScrollView {
                        ContentUnavailableView("Settings", systemImage: "gearshape.fill", description: Text("Adjust preferences, account, and app configuration."))
                            .containerRelativeFrame(.vertical)
                    }
                    .navigationTitle("Setting")
                }
            } label: {
                Label {
                    Text("Setting")
                } icon: {
                    Image(systemName: selectedTab == "setting" ? "gearshape.fill" : "gearshape")
                }
                .environment(\.symbolVariants, .none)
            }

            Tab(value: "search") {
                NavigationStack {
                    ScrollView {
                        ContentUnavailableView.search(text: searchText)
                    }
                    .navigationTitle("Search")
                }
                .searchable(text: $searchText, prompt: "Search...")
            } label: {
                Label {
                    Text("Search")
                } icon: {
                    Image(systemName: "magnifyingglass")
                }
                .environment(\.symbolVariants, .none)
            }
        }
        .sensoryFeedback(.increase, trigger: selectedTab)
    }
}

#Preview {
    SWRootTabView()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWRotatingQuote.swift`
```
//
//  SWRotatingQuote.swift
//  ShipSwift
//
//  Auto-rotating quote display that cycles through an array of quotes with animated
//  transitions. Shows the quote text and an author name aligned to the bottom-right.
//  Uses a hidden placeholder of the longest quote to maintain stable layout height.
//
//  Usage:
//    // Basic usage — multiple quotes rotation
//    SWRotatingQuote(
//        quotes: [
//            "Stay hungry, stay foolish.",
//            "The only way to do great work is to love what you do.",
//            "Innovation distinguishes between a leader and a follower."
//        ],
//        author: "Steve Jobs"
//    )
//
//    // Custom font, interval, and color
//    SWRotatingQuote(
//        quotes: [
//            "Those times when you get up early...",
//            "That is actually the dream."
//        ],
//        author: "Kobe Bryant",
//        interval: 3.0,
//        quoteFont: .body,
//        authorFont: .callout,
//        fontDesign: .serif,
//        foregroundStyle: .primary
//    )
//
//    // Single quote (no rotation, displayed statically)
//    SWRotatingQuote(
//        quotes: ["Stay hungry, stay foolish."],
//        author: "Steve Jobs"
//    )
//
//  Parameters:
//    - quotes: [LocalizedStringResource]  — Array of quotes (at least 1)
//    - author: LocalizedStringResource    — Author name
//    - interval: TimeInterval             — Rotation interval in seconds (default 5.0)
//    - quoteFont: Font                    — Quote font (default .subheadline)
//    - authorFont: Font                   — Author font (default .headline)
//    - fontDesign: Font.Design            — Font design (default .rounded)
//    - foregroundStyle: Color             — Text color (default .secondary)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

/// A component that rotates through multiple quote texts, supporting custom author and rotation interval
struct SWRotatingQuote: View {
    
    // MARK: - Configuration
    
    /// Array of quote texts
    let quotes: [LocalizedStringResource]
    
    /// Author name (displayed at bottom-right)
    let author: LocalizedStringResource
    
    /// Text rotation interval (seconds)
    let interval: TimeInterval
    
    /// Quote text font
    let quoteFont: Font
    
    /// Author font
    let authorFont: Font
    
    /// Font design
    let fontDesign: Font.Design
    
    /// Text color
    let foregroundStyle: Color
    
    // MARK: - State
    
    @State private var currentTextIndex = 0
    @State private var textRotationTimer: Timer?
    
    // MARK: - Initializer
    
    /// Creates a rotating quote text component
    /// - Parameters:
    ///   - quotes: Array of quote texts (at least 1 required)
    ///   - author: Author name
    ///   - interval: Text rotation interval, default 5 seconds
    ///   - quoteFont: Quote text font, default .subheadline
    ///   - authorFont: Author font, default .headline
    ///   - fontDesign: Font design, default .rounded
    ///   - foregroundStyle: Text color, default .secondary
    init(
        quotes: [LocalizedStringResource],
        author: LocalizedStringResource,
        interval: TimeInterval = 5.0,
        quoteFont: Font = .subheadline,
        authorFont: Font = .headline,
        fontDesign: Font.Design = .rounded,
        foregroundStyle: Color = .secondary
    ) {
        self.quotes = quotes
        self.author = author
        self.interval = interval
        self.quoteFont = quoteFont
        self.authorFont = authorFont
        self.fontDesign = fontDesign
        self.foregroundStyle = foregroundStyle
    }
    
    // MARK: - Body
    
    var body: some View {
        ZStack {
            // Hidden placeholder text using the longest quote to determine height
            VStack(alignment: .leading) {
                Text(longestQuote)
                    .font(quoteFont)
                    .contentTransition(.numericText())
                
                Spacer()
                
                HStack {
                    Spacer()
                    
                    Text(author)
                        .font(authorFont)
                }
            }
            .opacity(0)
            
            // Actual displayed content
            VStack(alignment: .leading) {
                Text(quotes[safe: currentTextIndex] ?? quotes[0])
                    .font(quoteFont)
                    .contentTransition(.numericText())
                
                Spacer()
                
                HStack {
                    Spacer()
                    
                    Text(author)
                        .font(authorFont)
                }
            }
            .foregroundStyle(foregroundStyle)
        }
        .fontDesign(fontDesign)
        .onAppear { startTextRotation() }
        .onDisappear { stopTextRotation() }
    }
    
    // MARK: - Helper Properties
    
    /// Find the longest quote text (used for placeholder)
    private var longestQuote: LocalizedStringResource {
        quotes.max { quote1, quote2 in
            String(localized: quote1).count < String(localized: quote2).count
        } ?? quotes[0]
    }
    
    // MARK: - Timer Management
    
    private func startTextRotation() {
        // No rotation needed if there is only one quote
        guard quotes.count > 1 else { return }
        
        // Invalidate any previous timer
        textRotationTimer?.invalidate()
        
        textRotationTimer = Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { _ in
            Task { @MainActor in
                withAnimation {
                    let maxIndex = quotes.count - 1
                    currentTextIndex = (currentTextIndex + 1) % (maxIndex + 1)
                }
            }
        }
    }
    
    private func stopTextRotation() {
        textRotationTimer?.invalidate()
        textRotationTimer = nil
    }
}

// MARK: - Array Safe Access Extension

private extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

// MARK: - Preview

#Preview {
    ScrollView {
        VStack(spacing: 32) {
            // Multiple quotes rotation
            SWRotatingQuote(
                quotes: [
                    "Those times when you get up early, and you work hard, those times when you stay up late, and you work hard.",
                    "Those times when you don't feel like working, you're too tired, you don't want to push yourself, but you do it anyway.",
                    "That is actually the dream.\n It's not the destination, it's the journey."
                ],
                author: "Kobe Bryant"
            )
            .frame(height: 200)
            
            Divider()
            
            // Single quote (no rotation)
            SWRotatingQuote(
                quotes: [
                    "Stay hungry, stay foolish."
                ],
                author: "Steve Jobs",
                quoteFont: .title3,
                authorFont: .title2
            )
            .frame(height: 200)
            
            Divider()
            
            // Custom style
            
            SWRotatingQuote(
                quotes: [
                    "The only way to do great work is to love what you do.",
                    "Innovation distinguishes between a leader and a follower.",
                    "Your time is limited, don't waste it living someone else's life."
                ],
                author: "Steve Jobs",
                interval: 3.0,
                quoteFont: .body,
                authorFont: .callout,
                fontDesign: .serif,
                foregroundStyle: .primary
            )
            .frame(height: 200)
        }
        .padding(30)
    }
}
```

## File: `ShipSwift/SWPackage/SWComponent/Display/SWScrollingFAQ+iOS.swift`
```
//
//  SWScrollingFAQ+iOS.swift
//  ShipSwift
//
//  Auto-scrolling horizontal FAQ carousel that displays rows of
//  question pills scrolling in alternating directions (left, right, left).
//  Uses UIScrollView with a CADisplayLink for smooth infinite looping.
//  Tapping a pill triggers the onTap callback with the question text.
//
//  Usage:
//    SWScrollingFAQ(
//        rows: [
//            ["How does AI work?", "What can I ask?", "How accurate?", "Help with coding?",
//             "Remember chat?", "Languages supported?", "Get started?", "Explain topics?"],
//            ["Write an email", "Summarize article", "Translate text", "Creative ideas",
//             "Debug code", "Explain concept", "Meal plan", "Brainstorm"],
//            ["Best approach?", "How to improve?", "Give examples", "Compare options",
//             "Suggest alternatives", "Pros and cons?", "Help understand", "Walk through"]
//        ],
//        title: "Let's talk about new topics"   // optional, nil hides the title
//    ) { question in
//        swDebugLog("User tapped: \(question)")
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWScrollingFAQ: View {

    // MARK: - Configuration

    /// FAQ data organized by rows. Each inner array is displayed as one scrolling row.
    let rows: [[String]]

    /// Optional title displayed above the scrolling rows
    var title: String? = nil

    /// Callback when a question pill is tapped
    var onTap: (String) -> Void

    // MARK: - Internal

    private enum Direction { case left, right }

    // MARK: - Body

    var body: some View {
        VStack(spacing: 8) {
            if let title {
                Text(title)
                    .padding(8)
                    .font(.headline)
            }

            Group {
                ForEach(Array(rows.enumerated()), id: \.offset) { index, row in
                    InfiniteScrollView(
                        questions: row,
                        direction: index % 2 == 0 ? .left : .right,
                        onTap: onTap
                    )
                    .frame(height: 34)
                }
            }
            .mask(
                LinearGradient(
                    stops: [
                        .init(color: .clear, location: 0),
                        .init(color: .black, location: 0.08),
                        .init(color: .black, location: 0.92),
                        .init(color: .clear, location: 1.0),
                    ],
                    startPoint: .leading,
                    endPoint: .trailing
                )
            )
        }
        .padding(.vertical)
    }

    // MARK: - Infinite Scroll

    private struct InfiniteScrollView: UIViewRepresentable {
        let questions: [String]
        let direction: Direction
        var onTap: (String) -> Void

        func makeUIView(context: Context) -> UIScrollView {
            let scrollView = UIScrollView()
            scrollView.showsHorizontalScrollIndicator = false
            scrollView.showsVerticalScrollIndicator = false
            scrollView.isScrollEnabled = false

            let stackView = UIStackView()
            stackView.axis = .horizontal
            stackView.spacing = 0
            stackView.alignment = .center
            stackView.distribution = .equalSpacing

            // Create 3 copies for seamless looping
            for _ in 0..<3 {
                for question in questions {
                    let button = Button(question) { onTap(question) }
                        .font(.subheadline)
                        .buttonStyle(.bordered)
                    let host = UIHostingController(rootView: button)
                    host.view.backgroundColor = .clear
                    host.safeAreaRegions = []
                    host.view.setContentHuggingPriority(.required, for: .horizontal)
                    host.view.setContentCompressionResistancePriority(.required, for: .horizontal)
                    let size = host.sizeThatFits(in: CGSize(width: CGFloat.greatestFiniteMagnitude, height: 34))
                    host.view.frame = CGRect(origin: .zero, size: size)
                    stackView.addArrangedSubview(host.view)
                }
            }

            scrollView.addSubview(stackView)
            stackView.translatesAutoresizingMaskIntoConstraints = false
            NSLayoutConstraint.activate([
                stackView.topAnchor.constraint(equalTo: scrollView.topAnchor),
                stackView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
                stackView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor),
                stackView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor),
                stackView.heightAnchor.constraint(equalTo: scrollView.heightAnchor)
            ])

            context.coordinator.scrollView = scrollView
            context.coordinator.stackView = stackView
            context.coordinator.direction = direction

            return scrollView
        }

        func updateUIView(_ uiView: UIScrollView, context: Context) {
            DispatchQueue.main.async {
                context.coordinator.startIfNeeded()
            }
        }

        func makeCoordinator() -> Coordinator { Coordinator() }

        class Coordinator {
            weak var scrollView: UIScrollView?
            weak var stackView: UIStackView?
            var direction: Direction = .left

            private var displayLink: CADisplayLink?
            private var unitWidth: CGFloat = 0
            private var started = false

            func startIfNeeded() {
                guard !started, let scrollView, let stackView else { return }

                stackView.layoutIfNeeded()
                let totalWidth = stackView.bounds.width
                guard totalWidth > 0 else { return }

                unitWidth = totalWidth / 3
                scrollView.contentSize = CGSize(width: totalWidth, height: stackView.bounds.height)

                // Start from the middle copy so there's room in both directions
                scrollView.contentOffset.x = unitWidth

                started = true
                displayLink = CADisplayLink(target: self, selector: #selector(tick))
                displayLink?.add(to: .main, forMode: .common)
            }

            @objc private func tick() {
                guard let scrollView, unitWidth > 0 else { return }

                let speed: CGFloat = 30 / 60.0
                var x = scrollView.contentOffset.x

                if direction == .left {
                    x += speed
                    if x >= unitWidth * 2 {
                        x -= unitWidth
                    }
                } else {
                    x -= speed
                    if x <= 0 {
                        x += unitWidth
                    }
                }

                scrollView.contentOffset.x = x
            }

            deinit {
                displayLink?.invalidate()
            }
        }
    }
}

// MARK: - Preview

#Preview {
    SWScrollingFAQ(
        rows: [
            ["How does AI work?", "What can I ask?", "How accurate?", "Help with coding?",
             "Remember chat?", "Languages supported?", "Get started?", "Explain topics?"],
            ["Write an email", "Summarize article", "Translate text", "Creative ideas",
             "Debug code", "Explain concept", "Meal plan", "Brainstorm"],
            ["Best approach?", "How to improve?", "Give examples", "Compare options",
             "Suggest alternatives", "Pros and cons?", "Help understand", "Walk through"]
        ],
        title: "Let's talk about new topics"
    ) { question in
        swDebugLog("Tapped: \(question)")
    }
}

```

## File: `ShipSwift/SWPackage/SWComponent/Feedback/SWAlert.swift`
```
//
//  SWAlert.swift
//  ShipSwift
//
//  Global alert overlay that displays toast-style notifications at the top of
//  the screen. Supports four preset styles (info, success, warning, error)
//  and fully custom styling. Auto-dismisses after a configurable duration.
//
//  Usage:
//    1. Attach the modifier at your App entry point (once):
//
//       @main
//       struct MyApp: App {
//           var body: some Scene {
//               WindowGroup {
//                   ContentView()
//                       .swAlert()
//               }
//           }
//       }
//
//    2. Show an alert from anywhere using the singleton:
//
//       // Preset types: .info, .success, .warning, .error
//       SWAlertManager.shared.show(.success, message: "Saved!")
//       SWAlertManager.shared.show(.error, message: "Something went wrong")
//
//       // With custom duration
//       SWAlertManager.shared.show(.warning, message: "Slow connection", duration: .seconds(5))
//
//       // Dynamic string (e.g. from API error)
//       SWAlertManager.shared.show(.error, message: errorString)
//
//       // Fully custom style
//       SWAlertManager.shared.show(
//           icon: "star.fill",
//           message: "Custom alert",
//           textColor: .yellow,
//           backgroundStyle: AnyShapeStyle(.black),
//           borderColor: .yellow
//       )
//
//    3. Dismiss programmatically (optional — alerts auto-dismiss):
//
//       SWAlertManager.shared.dismiss()
//
//  SWAlertType cases:
//    .info    — blue info circle icon, primary text color
//    .success — green checkmark icon, green text color
//    .warning — orange triangle icon, orange text color
//    .error   — red x-mark icon, red text color
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWAlertType

enum SWAlertType {
    case info
    case success
    case warning
    case error

    var icon: String {
        switch self {
        case .info: "info.circle.fill"
        case .success: "checkmark.circle.fill"
        case .warning: "exclamationmark.triangle.fill"
        case .error: "xmark.circle.fill"
        }
    }

    var textColor: Color {
        switch self {
        case .info: .primary
        case .success: .green
        case .warning: .orange
        case .error: .red
        }
    }

    var backgroundStyle: AnyShapeStyle {
        AnyShapeStyle(.ultraThinMaterial)
    }

    var borderColor: Color {
        switch self {
        case .info: .secondary.opacity(0.6)
        case .success: .green.opacity(0.6)
        case .warning: .orange.opacity(0.6)
        case .error: .red.opacity(0.6)
        }
    }
}

// MARK: - SWAlertManager

@MainActor
@Observable
final class SWAlertManager {
    static let shared = SWAlertManager()

    // MARK: - State

    private(set) var isShowing = false
    private(set) var icon = SWAlertType.info.icon
    private(set) var message: LocalizedStringKey = ""
    private(set) var textColor = SWAlertType.info.textColor
    private(set) var backgroundStyle = SWAlertType.info.backgroundStyle
    private(set) var borderColor = SWAlertType.info.borderColor

    private var dismissTask: Task<Void, Never>?

    private init() {}

    // MARK: - Public Methods (LocalizedStringKey)

    /// Show alert with preset type (LocalizedStringKey, recommended for static text)
    func show(_ type: SWAlertType, message: LocalizedStringKey, duration: Duration = .seconds(2)) {
        showInternal(
            icon: type.icon,
            message: message,
            textColor: type.textColor,
            backgroundStyle: type.backgroundStyle,
            borderColor: type.borderColor,
            duration: duration
        )
    }

    /// Show alert with custom style (LocalizedStringKey)
    func show(
        icon: String,
        message: LocalizedStringKey,
        textColor: Color = .white,
        backgroundStyle: AnyShapeStyle = AnyShapeStyle(.black),
        borderColor: Color = .secondary,
        duration: Duration = .seconds(2)
    ) {
        showInternal(
            icon: icon,
            message: message,
            textColor: textColor,
            backgroundStyle: backgroundStyle,
            borderColor: borderColor,
            duration: duration
        )
    }

    // MARK: - Public Methods (String)

    /// Show alert with preset type (String, for dynamic text like API errors)
    func show(_ type: SWAlertType, message: String, duration: Duration = .seconds(2)) {
        showInternal(
            icon: type.icon,
            message: LocalizedStringKey(message),
            textColor: type.textColor,
            backgroundStyle: type.backgroundStyle,
            borderColor: type.borderColor,
            duration: duration
        )
    }

    /// Show alert with custom style (String)
    func show(
        icon: String,
        message: String,
        textColor: Color = .white,
        backgroundStyle: AnyShapeStyle = AnyShapeStyle(.black),
        borderColor: Color = .secondary,
        duration: Duration = .seconds(2)
    ) {
        showInternal(
            icon: icon,
            message: LocalizedStringKey(message),
            textColor: textColor,
            backgroundStyle: backgroundStyle,
            borderColor: borderColor,
            duration: duration
        )
    }

    // MARK: - Internal

    private func showInternal(
        icon: String,
        message: LocalizedStringKey,
        textColor: Color,
        backgroundStyle: AnyShapeStyle,
        borderColor: Color,
        duration: Duration
    ) {
        dismissTask?.cancel()

        self.icon = icon
        self.message = message
        self.textColor = textColor
        self.backgroundStyle = backgroundStyle
        self.borderColor = borderColor

        withAnimation { isShowing = true }

        dismissTask = Task {
            try? await Task.sleep(for: duration)
            guard !Task.isCancelled else { return }
            withAnimation { isShowing = false }
        }
    }

    func dismiss() {
        dismissTask?.cancel()
        withAnimation { isShowing = false }
    }
}

// MARK: - Alert View

private struct SWAlertView: View {
    let alertManager = SWAlertManager.shared

    var body: some View {
        if alertManager.isShowing {
            HStack(spacing: 6) {
                Image(systemName: alertManager.icon)
                    .font(.footnote)
                Text(alertManager.message)
                    .font(.footnote)
                    .multilineTextAlignment(.center)
            }
            .foregroundStyle(alertManager.textColor)
            .padding(.horizontal, 16)
            .padding(.vertical, 10)
            .background {
                Capsule()
                    .fill(alertManager.backgroundStyle)
                    .strokeBorder(alertManager.borderColor, lineWidth: 0.5)
            }
            .transition(.scale.combined(with: .opacity))
            .onTapGesture { alertManager.dismiss() }
        }
    }
}

// MARK: - View Modifier

private struct SWAlertModifier: ViewModifier {
    let alertManager = SWAlertManager.shared

    func body(content: Content) -> some View {
        content
            .overlay(alignment: .top) {
                SWAlertView()
                    .padding(.top, 40)
            }
            .animation(.spring(duration: 0.3), value: alertManager.isShowing)
    }
}

// MARK: - View Extension

extension View {
    /// Add global alert support
    ///
    /// Use at the App entry point:
    /// ```swift
    /// @main
    /// struct MyApp: App {
    ///     var body: some Scene {
    ///         WindowGroup {
    ///             ContentView()
    ///                 .swAlert()
    ///         }
    ///     }
    /// }
    /// ```
    func swAlert() -> some View {
        modifier(SWAlertModifier())
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 20) {
        Button("Info") {
            SWAlertManager.shared.show(.info, message: "This is an info message")
        }
        .buttonStyle(.bordered)
        
        Button("Success") {
            SWAlertManager.shared.show(.success, message: "Saved successfully")
        }
        .buttonStyle(.bordered)

        Button("Warning") {
            SWAlertManager.shared.show(.warning, message: "Slow connection")
        }
        .buttonStyle(.bordered)

        Button("Error") {
            SWAlertManager.shared.show(.error, message: "Operation failed, please retry")
        }
        .buttonStyle(.bordered)

        Button("Custom") {
            SWAlertManager.shared.show(
                icon: "star.fill",
                message: "Custom alert style",
                textColor: .yellow,
                backgroundStyle: AnyShapeStyle(.black),
                borderColor: .yellow
            )
        }
        .buttonStyle(.bordered)
    }
    .font(.headline)
    .frame(maxWidth: .infinity)
    .swAlert()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Feedback/SWLoading.swift`
```
//
//  SWLoading.swift
//  ShipSwift
//
//  Page-level fullscreen loading overlay with blur material background,
//  customizable message text, optional SF Symbol icon with pulse animation,
//  and a progress indicator. Each page has independent loading state managed
//  through the SWLoadingPage enum.
//
//  Usage:
//    1. Register your pages in the SWLoadingPage enum:
//
//       enum SWLoadingPage: String {
//           case home
//           case settings
//           case profile
//       }
//
//    2. Attach the modifier to the view that should show the overlay:
//
//       var body: some View {
//           MyPageContent()
//               .swPageLoading(.home)
//       }
//
//    3. Show / update / hide from anywhere via the singleton:
//
//       // Show with default message
//       SWLoadingManager.shared.show(page: .home)
//
//       // Show with custom message and icon
//       SWLoadingManager.shared.show(
//           page: .home,
//           message: "Syncing data...",
//           systemImage: "arrow.triangle.2.circlepath"
//       )
//
//       // Update the message while loading
//       SWLoadingManager.shared.updateMessage(page: .home, message: "Almost done...")
//
//       // Hide the overlay
//       SWLoadingManager.shared.hide(page: .home)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - Page Loading State

/// Represents the loading state for a specific page
struct SWPageLoadingState {
    var isShowing: Bool = false
    var message: String = "Loading..."
    var systemImage: String? = nil
}

// MARK: - Page Identifier

/// Page identifier enum - Add your page cases here
enum SWLoadingPage: String {
    case home
    case settings
    case profile
    // Add more pages as needed
}

// MARK: - SWLoadingManager

@MainActor
@Observable
final class SWLoadingManager {
    static let shared = SWLoadingManager()

    private var pageStates: [SWLoadingPage: SWPageLoadingState] = [:]

    private init() {}

    // MARK: - Page-level Loading

    /// Show page loading overlay
    func show(page: SWLoadingPage, message: String = "Loading...", systemImage: String? = nil) {
        pageStates[page] = SWPageLoadingState(isShowing: true, message: message, systemImage: systemImage)
    }

    /// Update page loading message
    func updateMessage(page: SWLoadingPage, message: String) {
        pageStates[page]?.message = message
    }

    /// Hide page loading overlay
    func hide(page: SWLoadingPage) {
        pageStates[page]?.isShowing = false
    }

    /// Get page loading state
    func state(for page: SWLoadingPage) -> SWPageLoadingState {
        pageStates[page] ?? SWPageLoadingState()
    }
}

// MARK: - Page Loading View

struct SWPageLoadingView: View {
    let page: SWLoadingPage

    private var state: SWPageLoadingState {
        SWLoadingManager.shared.state(for: page)
    }

    var body: some View {
        if state.isShowing {
            VStack(spacing: 24) {
                // Icon
                if let systemImage = state.systemImage {
                    Image(systemName: systemImage)
                        .font(.system(size: 64, weight: .light))
                        .foregroundStyle(.primary.opacity(0.8))
                        .symbolEffect(.pulse, options: .repeating)
                }

                // Message + progress indicator
                VStack(spacing: 12) {
                    Text(state.message)
                        .font(.headline)
                        .foregroundStyle(.primary.opacity(0.9))
                        .multilineTextAlignment(.center)

                    ProgressView()
                        .tint(.primary.opacity(0.6))
                }
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(.ultraThinMaterial)
            .ignoresSafeArea(.all)
            .transition(.opacity)
        }
    }
}

// MARK: - View Modifier

private struct SWPageLoadingModifier: ViewModifier {
    let page: SWLoadingPage

    private var state: SWPageLoadingState {
        SWLoadingManager.shared.state(for: page)
    }

    func body(content: Content) -> some View {
        content
            .overlay {
                SWPageLoadingView(page: page)
            }
            .animation(.easeInOut(duration: 0.25), value: state.isShowing)
    }
}

// MARK: - View Extension

extension View {
    /// Add page-level loading support (fullscreen blur overlay)
    func swPageLoading(_ page: SWLoadingPage) -> some View {
        modifier(SWPageLoadingModifier(page: page))
    }
}

// MARK: - Preview

#Preview {
    ZStack {
        LinearGradient(
            colors: [.blue, .purple],
            startPoint: .topLeading,
            endPoint: .bottomTrailing
        )
        .ignoresSafeArea()

        VStack(spacing: 20) {
            Text("Page Content")
                .font(.largeTitle)
                .foregroundStyle(.white)

            Button("Show Default Loading") {
                SWLoadingManager.shared.show(page: .home, message: "Loading data...")
                Task {
                    try? await Task.sleep(for: .seconds(2))
                    SWLoadingManager.shared.hide(page: .home)
                }
            }
            .buttonStyle(.borderedProminent)

            Button("Show Loading with Icon") {
                SWLoadingManager.shared.show(
                    page: .home,
                    message: "Syncing data...",
                    systemImage: "arrow.triangle.2.circlepath"
                )
                Task {
                    try? await Task.sleep(for: .seconds(2))
                    SWLoadingManager.shared.hide(page: .home)
                }
            }
            .buttonStyle(.borderedProminent)

            Button("Hide Loading") {
                SWLoadingManager.shared.hide(page: .home)
            }
            .buttonStyle(.bordered)
        }
    }
    .swPageLoading(.home)
}
```

## File: `ShipSwift/SWPackage/SWComponent/Feedback/SWThinkingIndicator.swift`
```
//
//  SWThinkingIndicator.swift
//  ShipSwift
//
//  Animated thinking/typing indicator with three bouncing dots.
//  Commonly used in chat interfaces to show that the AI or remote user is typing.
//
//  Usage:
//    // Default style
//    SWThinkingIndicator()
//
//    // Custom dot size, color, and spacing
//    SWThinkingIndicator(dotSize: 8, dotColor: .blue, spacing: 5)
//
//    // Show "typing" state in a chat bubble
//    if isThinking {
//        SWThinkingIndicator()
//    }
//
//    // Place in an HStack alongside text
//    HStack {
//        Text("AI is thinking")
//        SWThinkingIndicator()
//    }
//
//  Parameters:
//    - dotSize:  Diameter of each dot (default: 5)
//    - dotColor: Fill color of the dots (default: .secondary)
//    - spacing:  Horizontal spacing between dots (default: 3)
//
//  Notes:
//    - Uses TimelineView for zero-lifecycle-management animation
//    - Three dots bounce up and down sequentially at 0.3 second intervals
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - SWThinkingIndicator

struct SWThinkingIndicator: View {

    // MARK: - Configurable Parameters

    var dotSize: CGFloat = 5
    var dotColor: Color = .secondary
    var spacing: CGFloat = 3

    // MARK: - Body

    var body: some View {
        TimelineView(.periodic(from: .now, by: 0.3)) { timeline in
            let phase = Int(timeline.date.timeIntervalSinceReferenceDate / 0.3) % 3
            HStack(spacing: spacing) {
                ForEach(0..<3) { index in
                    Circle()
                        .fill(dotColor)
                        .frame(width: dotSize, height: dotSize)
                        .offset(y: phase == index ? -(dotSize * 0.6) : 0)
                        .animation(.easeInOut(duration: 0.2), value: phase)
                }
            }
        }
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 40) {
        // Default style
        VStack(spacing: 8) {
            Text("Default")
                .font(.caption)
                .foregroundStyle(.secondary)
            SWThinkingIndicator()
        }

        // Chat bubble usage
        VStack(spacing: 8) {
            Text("Chat Bubble")
                .font(.caption)
                .foregroundStyle(.secondary)
            HStack(alignment: .bottom, spacing: 8) {
                Image(systemName: "brain.head.profile")
                    .font(.title2)
                    .foregroundStyle(.purple)
                HStack(spacing: 4) {
                    Text("Thinking")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                    SWThinkingIndicator()
                }
                .padding(.horizontal, 14)
                .padding(.vertical, 10)
                .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
            }
        }

        // Custom color and size
        VStack(spacing: 8) {
            Text("Custom (blue, large)")
                .font(.caption)
                .foregroundStyle(.secondary)
            SWThinkingIndicator(dotSize: 10, dotColor: .blue, spacing: 6)
        }
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Input/SWAddSheet.swift`
```
//
//  SWAddSheet.swift
//  ShipSwift
//
//  Bottom sheet with a text input field, Cancel and Continue buttons.
//  Presented as a .medium detent sheet for collecting user input (e.g. purpose, wish, notes).
//
//  Usage:
//    @State private var showSheet = false
//
//    Button("Add Item") { showSheet = true }
//    .sheet(isPresented: $showSheet) {
//        SWAddSheet(isPresented: $showSheet) { text in
//            // text is the user input content
//            print("User entered: \(text)")
//        }
//    }
//
//    // Custom title and placeholder text
//    SWAddSheet(
//        isPresented: $showSheet,
//        title: "Your Wish",
//        placeHolderText: "Enter your wish...",
//        minLines: 3
//    ) { text in
//        handleInput(text)
//    }
//
//  Parameters:
//    - isPresented: Binding<Bool>          — Controls sheet show/hide
//    - title: LocalizedStringKey           — Top title (default "Your Generation Purpose")
//    - placeHolderText: LocalizedStringKey — Input field placeholder text
//    - minLines: Int                       — Input field minimum lines (default 5)
//    - onConfirm: ((String) -> Void)?      — Callback when user taps Continue
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWAddSheet: View {
    @Binding var isPresented: Bool
    @State private var inputText = ""

    var title: LocalizedStringKey = "Your Generation Purpose"
    var placeHolderText: LocalizedStringKey = "Enter your purpose/wish/favorite things for this generation (optional)..."
    var minLines: Int = 5
    var onConfirm: ((String) -> Void)?

    var body: some View {
        VStack {
            Text(title)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding()
                .padding(.horizontal)

            InputField(
                text: $inputText,
                placeHolderText: placeHolderText,
                minLines: minLines
            )

            Spacer()
            Spacer()

            HStack {
                Button {
                    isPresented = false
                } label: {
                    Text("Cancel")
                }
                .buttonStyle(.swSecondary)

                Button {
                    onConfirm?(inputText)
                    isPresented = false
                } label: {
                    Text("Continue")
                }
                .buttonStyle(.swPrimary)
                .disabled(inputText.isEmpty)
            }
            .padding()
        }
        .presentationDetents([.medium])
        .presentationDragIndicator(.visible)
    }

    // MARK: - InputField (private)

    private struct InputField: View {
        @Binding var text: String
        var placeHolderText: LocalizedStringKey = "Enter message..."
        var minLines: Int = 1

        @FocusState private var isFocused: Bool

        var body: some View {
            TextField(placeHolderText, text: $text, axis: .vertical)
                .lineLimit(minLines...5)
                .focused($isFocused)
                .padding()
                .overlay(
                    RoundedRectangle(cornerRadius: 16)
                        .stroke(.primary, lineWidth: 1)
                )
                .padding(.horizontal)
                .padding(.vertical, 8)
        }
    }
}

#Preview {
    @Previewable @State var isPresented = true
    VStack {
        Text("Background")
    }
    .sheet(isPresented: $isPresented) {
        SWAddSheet(isPresented: $isPresented)
    }
}
```

## File: `ShipSwift/SWPackage/SWComponent/Input/SWStepper.swift`
```
//
//  SWStepper.swift
//  ShipSwift
//
//  Compact numeric stepper with chevron-style increment/decrement buttons,
//  animated numeric text transitions, and haptic feedback on value change.
//  The decrement button is disabled when the value reaches 0.
//
//  Usage:
//    @State private var quantity = 1
//
//    SWStepper(quantity: $quantity)
//
//  Parameters:
//    quantity — Binding<Int> for the current value (minimum 0)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWStepper: View {
    @Binding var quantity: Int

    var body: some View {
        HStack {
            Button {
                quantity -= 1
            } label: {
                Image(systemName: "chevron.backward")
                    .imageScale(.large)
            }
            .disabled(quantity <= 0)
            .buttonStyle(.plain)

            Text("\(quantity)")
                .frame(minWidth: 26)
                .contentTransition(.numericText())

            Button {
                quantity += 1
            } label: {
                Image(systemName: "chevron.forward")
                    .imageScale(.large)
            }
            .buttonStyle(.plain)
        }
        .animation(.default, value: quantity)
        .sensoryFeedback(.increase, trigger: [quantity])
    }
}

#Preview {
    @Previewable @State var sampleQuantity = 1

    VStack(spacing: 24) {
        // Standalone stepper
        SWStepper(quantity: $sampleQuantity)

        Divider()

        // Real-world usage with a label
        HStack {
            Text("Quantity")
            Spacer()
            SWStepper(quantity: $sampleQuantity)
        }
        .padding(.horizontal)
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWComponent/Input/SWTabButton.swift`
```
//
//  SWTabButton.swift
//  ShipSwift
//
//  Capsule-shaped tab button that toggles between selected (accent color)
//  and unselected (gray) states. Suitable for building custom segmented
//  controls or horizontal filter bars.
//
//  Usage:
//    @State private var selectedTab = 0
//
//    HStack {
//        SWTabButton(title: "All", isSelected: selectedTab == 0) {
//            selectedTab = 0
//        }
//        SWTabButton(title: "Favorites", isSelected: selectedTab == 1) {
//            selectedTab = 1
//        }
//    }
//
//  Parameters:
//    title      — LocalizedStringKey displayed on the button
//    isSelected — drives the visual state (accent bg vs gray bg)
//    action     — closure called on tap
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWTabButton: View {
    let title: LocalizedStringKey
    let isSelected: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(.subheadline)
                .padding(.horizontal, 16)
                .padding(.vertical, 8)
                .background(isSelected ? Color.accentColor : Color.secondary.opacity(0.2))
                .foregroundStyle(isSelected ? .white : .primary)
                .clipShape(Capsule())
        }
        .buttonStyle(.plain)
    }
}

#Preview {
    @Previewable @State var selectedTab = 0

    HStack {
        SWTabButton(title: "All", isSelected: selectedTab == 0) {
            selectedTab = 0
        }
        SWTabButton(title: "Favorites", isSelected: selectedTab == 1) {
            selectedTab = 1
        }
        SWTabButton(title: "Recent", isSelected: selectedTab == 2) {
            selectedTab = 2
        }
    }
    .padding()
}
```

## File: `ShipSwift/SWPackage/SWModule/SWAuth/SWAgreementChecker.swift`
```
//
//  SWAgreementChecker.swift
//  ShipSwift
//
//  A checkbox row for agreeing to Terms of Service and Privacy Policy.
//  Displays a toggle circle icon and two tappable links. URLs are configurable
//  via termsURL and privacyURL parameters (defaults to https://shipswift.app/terms and /privacy).
//
//  Usage:
//    @State private var agreed = false
//
//    VStack {
//        // ... sign-in form ...
//
//        SWAgreementChecker(agreementChecked: $agreed)
//
//        Button("Sign In") { signIn() }
//            .disabled(!agreed)
//    }
//
//    // Custom URLs
//    SWAgreementChecker(
//        agreementChecked: $agreed,
//        termsURL: URL(string: "https://myapp.com/terms")!,
//        privacyURL: URL(string: "https://myapp.com/privacy")!
//    )
//
//  Parameters:
//    - agreementChecked: Binding<Bool> — Whether the user has checked the agreement checkbox
//    - termsURL: URL — Link destination for Terms of Service (default: https://shipswift.app/terms)
//    - privacyURL: URL — Link destination for Privacy Policy (default: https://shipswift.app/privacy)
//
//  Notes:
//    - Tap the circle icon to toggle the checked state
//    - Terms of Service and Privacy Policy are external links that open in the browser
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWAgreementChecker: View {
    @Binding var agreementChecked: Bool

    var termsURL: URL = URL(string: "https://shipswift.app/terms")!
    var privacyURL: URL = URL(string: "https://shipswift.app/privacy")!

    var body: some View {
        HStack(spacing: 6) {
            Button {
                agreementChecked.toggle()
            } label: {
                Image(systemName: agreementChecked ? "checkmark.circle.fill" : "circle")
                    .imageScale(.small)
            }
            .buttonStyle(.plain)

            HStack(spacing: 4) {
                Text("I agree to")
                    .foregroundStyle(.secondary)
                Link("Terms of Service", destination: termsURL)
                Text("and")
                    .foregroundStyle(.secondary)
                Link("Privacy Policy", destination: privacyURL)
            }
            .font(.caption2)
            .lineLimit(1)
        }
        .padding(.top, 4)
    }
}

#Preview {
    @Previewable @State var agreed = false

    SWAgreementChecker(agreementChecked: $agreed)
        .padding()
}
```

## File: `ShipSwift/SWPackage/SWModule/SWAuth/SWAuthView+iOS.swift`
```
//
//  SWAuthView+iOS.swift
//  ShipSwift
//
//  Authentication view with email, phone, Apple, and Google sign-in.
//  Provides a complete auth flow: email sign in/up, phone sign in with
//  country code picker, email verification, forgot password, and reset
//  password — all in a single view.
//
//  Usage:
//    // 1. Present when user is signed out (requires SWUserManager in environment)
//    @State private var userManager = SWUserManager()
//
//    switch userManager.sessionState {
//    case .signedOut:
//        SWAuthView()
//            .environment(userManager)
//    case .ready:
//        MainView()
//    default:
//        LoadingView()
//    }
//
//    // 2. The view handles all auth flows internally:
//    //    - Email/password sign in and sign up
//    //    - Phone number sign in with country code picker
//    //    - 6-digit verification code confirmation (email & phone)
//    //    - Forgot password / reset password flow
//    //    - Apple and Google social sign-in buttons
//    //    - Terms of Service agreement checkbox
//
//    // 3. Error messages are displayed via SWAlertManager.shared
//    //    Make sure to attach .swAlert() modifier in your root view.
//
//    // 4. Preview usage
//    #Preview {
//        SWAuthView()
//            .environment(SWUserManager())
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import Amplify
import AWSCognitoAuthPlugin

struct SWAuthView: View {

    var isDemo: Bool = false

    // MARK: - Environment

    @Environment(SWUserManager.self) private var userManager

    // MARK: - View Mode

    private enum ViewMode {
        case signIn                    // Email sign in
        case signUp                    // Email sign up
        case confirmSignUp             // Confirm email verification code
        case forgotPassword            // Forgot password (enter email)
        case resetPassword             // Reset password (enter code and new password)
        case phoneSignIn               // Phone number sign in
        case phoneVerify               // Phone verification code
    }

    // MARK: - Loading State

    private enum LoadingState {
        case idle
        case sendingCode
        case verifying
        case signingIn
    }

    // Sign-in method enum for the top-bar Email / Phone toggle
    private enum SignInMethod: String, CaseIterable {
        case email = "Email"
        case phone = "Phone"
    }

    // MARK: - State

    @State private var viewMode: ViewMode = .signIn
    @State private var signInMethod: SignInMethod = .email
    @State private var loadingState: LoadingState = .idle
    @State private var agreementChecked = false

    // Email sign-in state
    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    @State private var verificationCode = ""
    @FocusState private var isPasswordFocused: Bool
    @FocusState private var isCodeFocused: Bool

    // Phone sign-in state
    @State private var phoneNumber = ""
    @State private var countryCode = "+1"
    @State private var showingCountryPicker = false
    @State private var countrySearchText = ""
    @State private var isResending = false

    // Reset password state
    @State private var newPassword = ""
    @State private var confirmNewPassword = ""
    @State private var resetCode = ""

    // MARK: - Computed Properties

    private var isValidEmail: Bool {
        let emailRegex = #"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"#
        return email.range(of: emailRegex, options: .regularExpression) != nil
    }

    private var isValidPassword: Bool {
        password.count >= 8
    }

    private var isValidConfirmPassword: Bool { password == confirmPassword && isValidPassword }

    private var isValidCode: Bool { verificationCode.count == 6 }

    private var isValidPhone: Bool {
        let expectedLength = SWCountryData.phoneLength(for: countryCode)
        return expectedLength.contains(phoneNumber.count)
    }

    private var fullPhoneNumber: String { "\(countryCode)\(phoneNumber)" }

    private var isValidResetCode: Bool { resetCode.count == 6 }

    private var isValidNewPassword: Bool {
        newPassword.count >= 8
    }

    private var isValidConfirmNewPassword: Bool { newPassword == confirmNewPassword && isValidNewPassword }

    // MARK: - Body

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {
                    Spacer(minLength: 40)

                    // Icon
                    Image(systemName: "person.circle.fill")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 80, height: 80)
                        .foregroundStyle(Color.accentColor)
                        .padding()

                    // Title
                    VStack(spacing: 8) {
                        Text(headerTitle)
                            .font(.title)
                            .fontWeight(.bold)
                            .multilineTextAlignment(.center)

                        Text(headerSubtitle)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }

                    // Sign-in method toggle buttons, shown only in signIn / phoneSignIn modes
                    if viewMode == .signIn || viewMode == .phoneSignIn {
                        HStack(spacing: 12) {
                            signInMethodButton(.email, icon: "envelope.fill", label: "Email")
                            signInMethodButton(.phone, icon: "phone.fill", label: "Phone")
                        }
                    }

                    Spacer(minLength: 20)

                    // Display different content based on mode
                    switch viewMode {
                    case .signIn, .signUp:
                        mainAuthSection
                    case .confirmSignUp:
                        confirmSignUpSection
                    case .forgotPassword:
                        forgotPasswordSection
                    case .resetPassword:
                        resetPasswordSection
                    case .phoneSignIn:
                        phoneSignInSection
                    case .phoneVerify:
                        phoneVerifySection
                    }
                }
                .padding()
            }
            .scrollDismissesKeyboard(.interactively)
            .onChange(of: signInMethod) { _, newMethod in
                withAnimation {
                    switch newMethod {
                    case .email: viewMode = .signIn
                    case .phone: viewMode = .phoneSignIn
                    }
                }
            }
            .sheet(isPresented: $showingCountryPicker) {
                countryCodePicker
            }
            .task {
                // Pre-trigger network permission request to avoid permission dialog
                // appearing during sign-in which could cause sign-in failure
                await prefetchNetworkPermission()
            }
        }
    }

    // MARK: - Network Permission Prefetch

    private func prefetchNetworkPermission() async {
        guard let url = URL(string: "https://www.apple.com") else { return }
        _ = try? await URLSession.shared.data(from: url)
    }

    private var headerTitle: String {
        switch viewMode {
        case .signIn: return "Welcome"
        case .signUp: return "Create Account"
        case .confirmSignUp: return "Verify Email"
        case .forgotPassword: return "Forgot Password"
        case .resetPassword: return "Reset Password"
        case .phoneSignIn: return "Phone Sign In"
        case .phoneVerify: return "Verify Phone"
        }
    }

    private var headerSubtitle: String {
        switch viewMode {
        case .signIn: return "Sign in to continue"
        case .signUp: return "Sign up with your email"
        case .confirmSignUp: return "Enter the 6-digit code sent to \(email)"
        case .forgotPassword: return "Enter your email to receive a reset code"
        case .resetPassword: return "Enter the code and your new password"
        case .phoneSignIn: return "Sign in with your phone number"
        case .phoneVerify: return "Enter the 6-digit code sent to \(fullPhoneNumber)"
        }
    }

    // MARK: - Main Auth Section (SignIn/SignUp)

    @ViewBuilder
    private var mainAuthSection: some View {
        VStack(spacing: 16) {
            // Email sign-in area
            emailSignInSection

            // Social sign-in area
            if viewMode == .signIn {
                socialSignInSection
            }
        }
    }

    // MARK: - Email Sign-In Section

    @ViewBuilder
    private var emailSignInSection: some View {
        VStack(spacing: 12) {
            // Email input
            HStack {
                Image(systemName: "envelope")
                    .foregroundStyle(.secondary)
                TextField("Email", text: $email)
                    .keyboardType(.emailAddress)
                    .textInputAutocapitalization(.never)
                    .textContentType(.emailAddress)
                    .autocorrectionDisabled()
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 14)
            .background(.accent.opacity(0.1))
            .clipShape(RoundedRectangle(cornerRadius: 12))

            // Password input
            HStack {
                Image(systemName: "lock")
                    .foregroundStyle(.secondary)
                SecureField("Password", text: $password)
                    .textContentType(viewMode == .signUp ? .newPassword : .password)
                    .focused($isPasswordFocused)
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 14)
            .background(.accent.opacity(0.1))
            .clipShape(RoundedRectangle(cornerRadius: 12))

            // Password requirements hint (sign-up mode only)
            if viewMode == .signUp && !password.isEmpty {
                passwordRequirements
            }

            // Confirm password (sign-up mode only)
            if viewMode == .signUp {
                HStack {
                    Image(systemName: "lock.fill")
                        .foregroundStyle(.secondary)
                    SecureField("Confirm Password", text: $confirmPassword)
                        .textContentType(.newPassword)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 14)
                .background(.accent.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))

                if !confirmPassword.isEmpty && password != confirmPassword {
                    Text("Passwords do not match")
                        .font(.caption)
                        .foregroundStyle(.red)
                }
            }

            // Sign-in / Sign-up button
            Button {
                if viewMode == .signUp {
                    signUpWithEmail()
                } else {
                    signInWithEmail()
                }
            } label: {
                HStack {
                    if loadingState == .signingIn {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(emailButtonText)
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isEmailFormValid || loadingState == .signingIn)

            // Forgot password (sign-in mode only)
            if viewMode == .signIn {
                Button {
                    withAnimation {
                        viewMode = .forgotPassword
                    }
                } label: {
                    Text("Forgot Password?")
                        .font(.subheadline)
                        .foregroundStyle(Color.accentColor)
                }
            }

            // Toggle sign-in / sign-up
            Button {
                withAnimation {
                    viewMode = viewMode == .signIn ? .signUp : .signIn
                    confirmPassword = ""
                }
            } label: {
                Text(viewMode == .signUp ? "Already have an account? Sign In" : "Don't have an account? Sign Up")
                    .font(.subheadline)
                    .foregroundStyle(Color.accentColor)
            }
        }
        .padding(.vertical)
    }

    // MARK: - Password Requirements

    @ViewBuilder
    private var passwordRequirements: some View {
        HStack(spacing: 4) {
            Image(systemName: password.count >= 8 ? "checkmark.circle.fill" : "circle")
                .foregroundStyle(password.count >= 8 ? .green : .secondary)
            Text("At least 8 characters")
                .foregroundStyle(password.count >= 8 ? .primary : .secondary)
        }
        .font(.caption)
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(.horizontal, 4)
    }

    private var emailButtonText: String {
        if loadingState == .signingIn {
            return viewMode == .signUp ? "Creating Account..." : "Signing In..."
        }
        return viewMode == .signUp ? "Create Account" : "Sign In"
    }

    private var isEmailFormValid: Bool {
        if viewMode == .signUp {
            return isValidEmail && isValidConfirmPassword
        }
        return isValidEmail && password.count >= 8
    }

    // MARK: - Confirm SignUp Section

    @ViewBuilder
    private var confirmSignUpSection: some View {
        VStack(spacing: 16) {
            // Verification code input
            TextField("000000", text: $verificationCode)
                .keyboardType(.numberPad)
                .textContentType(.oneTimeCode)
                .focused($isCodeFocused)
                .multilineTextAlignment(.center)
                .font(.title2.monospacedDigit())
                .padding(.vertical, 16)
                .background(.accent.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))
                .onChange(of: verificationCode) { _, newValue in
                    verificationCode = String(newValue.filter(\.isNumber).prefix(6))
                }

            // Confirm button
            Button {
                confirmSignUp()
            } label: {
                HStack {
                    if loadingState == .verifying {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(loadingState == .verifying ? "Verifying..." : "Verify Email")
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isValidCode || loadingState == .verifying)

            // Resend verification code
            Button {
                resendEmailCode()
            } label: {
                Text("Resend Code")
                    .font(.subheadline)
                    .foregroundStyle(Color.accentColor)
            }
            .disabled(loadingState == .sendingCode)

            // Back to sign in
            Button {
                withAnimation {
                    signInMethod = .email
                    viewMode = .signIn
                    verificationCode = ""
                }
            } label: {
                Text("Back to Sign In")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical)
        .task {
            try? await Task.sleep(for: .milliseconds(300))
            isCodeFocused = true
        }
    }

    // MARK: - Forgot Password Section

    @ViewBuilder
    private var forgotPasswordSection: some View {
        VStack(spacing: 16) {
            // Email input
            HStack {
                Image(systemName: "envelope")
                    .foregroundStyle(.secondary)
                TextField("Email", text: $email)
                    .keyboardType(.emailAddress)
                    .textInputAutocapitalization(.never)
                    .textContentType(.emailAddress)
                    .autocorrectionDisabled()
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 14)
            .background(.accent.opacity(0.1))
            .clipShape(RoundedRectangle(cornerRadius: 12))

            // Send verification code button
            Button {
                sendResetCode()
            } label: {
                HStack {
                    if loadingState == .sendingCode {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(loadingState == .sendingCode ? "Sending..." : "Send Reset Code")
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isValidEmail || loadingState == .sendingCode)

            // Back to sign in
            Button {
                withAnimation {
                    signInMethod = .email
                    viewMode = .signIn
                }
            } label: {
                Text("Back to Sign In")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical)
    }

    // MARK: - Reset Password Section

    @ViewBuilder
    private var resetPasswordSection: some View {
        VStack(spacing: 16) {
            // Verification code input
            VStack(alignment: .leading, spacing: 4) {
                Text("Verification Code")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                TextField("000000", text: $resetCode)
                    .keyboardType(.numberPad)
                    .textContentType(.oneTimeCode)
                    .multilineTextAlignment(.center)
                    .font(.title2.monospacedDigit())
                    .padding(.vertical, 16)
                    .background(.accent.opacity(0.1))
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                    .onChange(of: resetCode) { _, newValue in
                        resetCode = String(newValue.filter(\.isNumber).prefix(6))
                    }
            }

            // New password
            VStack(alignment: .leading, spacing: 4) {
                Text("New Password")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                HStack {
                    Image(systemName: "lock")
                        .foregroundStyle(.secondary)
                    SecureField("New Password", text: $newPassword)
                        .textContentType(.newPassword)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 14)
                .background(.accent.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))
            }

            // Password requirements hint
            if !newPassword.isEmpty {
                HStack(spacing: 4) {
                    Image(systemName: newPassword.count >= 8 ? "checkmark.circle.fill" : "circle")
                        .foregroundStyle(newPassword.count >= 8 ? .green : .secondary)
                    Text("At least 8 characters")
                        .foregroundStyle(newPassword.count >= 8 ? .primary : .secondary)
                }
                .font(.caption)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.horizontal, 4)
            }

            // Confirm new password
            VStack(alignment: .leading, spacing: 4) {
                Text("Confirm New Password")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                HStack {
                    Image(systemName: "lock.fill")
                        .foregroundStyle(.secondary)
                    SecureField("Confirm New Password", text: $confirmNewPassword)
                        .textContentType(.newPassword)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 14)
                .background(.accent.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))

                if !confirmNewPassword.isEmpty && newPassword != confirmNewPassword {
                    Text("Passwords do not match")
                        .font(.caption)
                        .foregroundStyle(.red)
                }
            }

            // Reset password button
            Button {
                confirmResetPassword()
            } label: {
                HStack {
                    if loadingState == .verifying {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(loadingState == .verifying ? "Resetting..." : "Reset Password")
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isValidResetCode || !isValidConfirmNewPassword || loadingState == .verifying)

            // Back to sign in
            Button {
                withAnimation {
                    signInMethod = .email
                    viewMode = .signIn
                    resetCode = ""
                    newPassword = ""
                    confirmNewPassword = ""
                }
            } label: {
                Text("Back to Sign In")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical)
    }

    // MARK: - Phone Sign-In Section

    @ViewBuilder
    private var phoneSignInSection: some View {
        VStack(spacing: 16) {
            // Country code + phone number input
            HStack(spacing: 8) {
                // Country code selector button
                Button {
                    showingCountryPicker = true
                } label: {
                    HStack(spacing: 4) {
                        Text(SWCountryData.flag(for: countryCode))
                        Text(countryCode)
                        Image(systemName: "chevron.down")
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                    }
                    .padding(.horizontal, 12)
                    .padding(.vertical, 14)
                    .background(.accent.opacity(0.1))
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                }

                // Phone number input
                TextField("Phone Number", text: $phoneNumber)
                    .keyboardType(.phonePad)
                    .textContentType(.telephoneNumber)
                    .padding(.horizontal, 16)
                    .padding(.vertical, 14)
                    .background(.accent.opacity(0.1))
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                    .onChange(of: phoneNumber) { _, newValue in
                        // Remove spaces from auto-filled phone numbers
                        let cleaned = newValue.replacingOccurrences(of: " ", with: "")
                        if cleaned != newValue {
                            phoneNumber = cleaned
                        }
                    }
            }

            // Send verification code button
            Button {
                sendPhoneCode()
            } label: {
                HStack {
                    if loadingState == .sendingCode {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(loadingState == .sendingCode ? "Sending..." : "Send Verification Code")
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isValidPhone || loadingState == .sendingCode)

            // Social sign-in area
            socialSignInSection
        }
        .padding(.vertical)
    }

    // MARK: - Phone Verify Section

    @ViewBuilder
    private var phoneVerifySection: some View {
        VStack(spacing: 16) {
            // 6-digit verification code input
            TextField("000000", text: $verificationCode)
                .keyboardType(.numberPad)
                .textContentType(.oneTimeCode)
                .focused($isCodeFocused)
                .multilineTextAlignment(.center)
                .font(.title2.monospacedDigit())
                .padding(.vertical, 16)
                .background(.accent.opacity(0.1))
                .clipShape(RoundedRectangle(cornerRadius: 12))
                .onChange(of: verificationCode) { _, newValue in
                    verificationCode = String(newValue.filter(\.isNumber).prefix(6))
                }

            // Verify button
            Button {
                verifyPhoneCode()
            } label: {
                HStack {
                    if loadingState == .verifying {
                        ProgressView()
                            .tint(.white)
                    }
                    Text(loadingState == .verifying ? "Verifying..." : "Verify Phone")
                }
            }
            .buttonStyle(.swPrimary)
            .disabled(!isValidCode || loadingState == .verifying)

            // Resend verification code
            Button {
                resendPhoneCode()
            } label: {
                HStack {
                    if isResending {
                        ProgressView()
                    }
                    Text("Resend Code")
                }
                .font(.subheadline)
                .foregroundStyle(Color.accentColor)
            }
            .disabled(isResending)

            // Back to phone sign-in
            Button {
                withAnimation {
                    viewMode = .phoneSignIn
                    verificationCode = ""
                }
            } label: {
                Text("Back")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical)
        .task {
            try? await Task.sleep(for: .milliseconds(300))
            isCodeFocused = true
        }
    }

    // MARK: - Country Code Picker

    private var countryCodePicker: some View {
        // Filter countries by search text
        let filteredCountries: [SWCountry] = countrySearchText.isEmpty
            ? SWCountryData.allCountries
            : SWCountryData.allCountries.filter {
                $0.name.localizedCaseInsensitiveContains(countrySearchText) ||
                $0.code.contains(countrySearchText)
            }
        let groupedCountries = Dictionary(grouping: filteredCountries) { country in
            String(country.name.prefix(1)).uppercased()
        }.sorted { $0.key < $1.key }

        return NavigationStack {
            List {
                ForEach(groupedCountries, id: \.key) { letter, countries in
                    Section(header: Text(letter)) {
                        ForEach(countries, id: \.name) { country in
                            Button {
                                countryCode = country.code
                                countrySearchText = ""
                                showingCountryPicker = false
                            } label: {
                                HStack {
                                    Text(country.flag)
                                        .font(.title2)
                                    HStack(spacing: 8) {
                                        Text(country.name)
                                            .foregroundStyle(.primary)
                                        Text(country.code)
                                            .foregroundStyle(.secondary)
                                    }
                                    Spacer()
                                    if countryCode == country.code {
                                        Image(systemName: "checkmark")
                                            .foregroundStyle(Color.accentColor)
                                    }
                                }
                            }
                        }
                    }
                }
            }
            .searchable(text: $countrySearchText, prompt: "Search")
            .tint(.primary)
            .navigationTitle("Select Country")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") {
                        countrySearchText = ""
                        showingCountryPicker = false
                    }
                }
            }
        }
    }

    // MARK: - Social Sign-In Section

    @ViewBuilder
    private var socialSignInSection: some View {
        VStack(spacing: 16) {
            // Divider
            HStack {
                Rectangle()
                    .fill(.tertiary)
                    .frame(height: 1)
                Text("or continue with")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                Rectangle()
                    .fill(.tertiary)
                    .frame(height: 1)
            }
            .padding(.top, 16)

            // Social sign-in buttons
            HStack(spacing: 12) {
                // Apple sign-in
                Button {
                    signInWithApple()
                } label: {
                    HStack(spacing: 8) {
                        Image(systemName: "apple.logo")
                            .font(.system(size: 18))
                        Text("Apple")
                    }
                }
                .buttonStyle(.swSecondary)

                // Google sign-in
                Button {
                    signInWithGoogle()
                } label: {
                    HStack(spacing: 8) {
                        Image(systemName: "g.circle.fill")
                            .font(.system(size: 18))
                        Text("Google")
                    }
                }
                .buttonStyle(.swSecondary)
            }

            // User agreement
            SWAgreementChecker(agreementChecked: $agreementChecked)
        }
    }

    // MARK: - Actions

    private func demoGuard() -> Bool {
        guard isDemo else { return false }
        SWAlertManager.shared.show(.info, message: "UI Demo — auth actions are not functional")
        return true
    }

    private func signInWithEmail() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        loadingState = .signingIn
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.signIn(email: email, password: password)
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signUpWithEmail() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        loadingState = .signingIn
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.signUp(email: email, password: password)
                withAnimation {
                    viewMode = .confirmSignUp
                }
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func confirmSignUp() {
        guard !demoGuard() else { return }
        loadingState = .verifying
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.confirmSignUp(email: email, code: verificationCode)
                try await userManager.signIn(email: email, password: password)
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func resendEmailCode() {
        guard !demoGuard() else { return }
        loadingState = .sendingCode
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.resendSignUpCode(email: email)
                SWAlertManager.shared.show(.success, message: "Code sent to \(email)")
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func sendResetCode() {
        guard !demoGuard() else { return }
        loadingState = .sendingCode
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.forgotPassword(email: email)
                withAnimation {
                    viewMode = .resetPassword
                }
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func confirmResetPassword() {
        guard !demoGuard() else { return }
        loadingState = .verifying
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.confirmResetPassword(email: email, newPassword: newPassword, code: resetCode)
                SWAlertManager.shared.show(.success, message: "Password reset successfully")
                withAnimation {
                    signInMethod = .email
                    viewMode = .signIn
                    resetCode = ""
                    newPassword = ""
                    confirmNewPassword = ""
                    password = ""
                }
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    // MARK: - Phone Actions

    private func sendPhoneCode() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        loadingState = .sendingCode
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.sendPhoneVerificationCode(phoneNumber: fullPhoneNumber)
                withAnimation { viewMode = .phoneVerify }
                SWAlertManager.shared.show(.success, message: "Code sent to \(fullPhoneNumber)")
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func verifyPhoneCode() {
        guard !demoGuard() else { return }
        loadingState = .verifying
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.confirmPhoneSignIn(phoneNumber: fullPhoneNumber, code: verificationCode)
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func resendPhoneCode() {
        guard !demoGuard() else { return }
        isResending = true
        Task {
            defer { isResending = false }
            do {
                try await userManager.sendPhoneVerificationCode(phoneNumber: fullPhoneNumber)
                SWAlertManager.shared.show(.success, message: "Code sent to \(fullPhoneNumber)")
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signInWithApple() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        Task {
            do {
                try await userManager.signInWithApple()
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signInWithGoogle() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        Task {
            do {
                try await userManager.signInWithGoogle()
            } catch {
                SWAlertManager.shared.show(.error, message: SWAuthErrorHelper.displayMessage(for: error))
            }
        }
    }
    // MARK: - Helpers

    /// Sign-in method toggle button: selected state uses accentColor + capsule background; unselected uses secondary
    private func signInMethodButton(_ method: SignInMethod, icon: String, label: String) -> some View {
        Button {
            withAnimation { signInMethod = method }
        } label: {
            HStack(spacing: 6) {
                Image(systemName: icon)
                Text(label)
            }
            .font(.subheadline)
            .fontWeight(signInMethod == method ? .medium : .regular)
            .foregroundStyle(signInMethod == method ? Color.accentColor : .secondary)
            .padding(.horizontal, 16)
            .padding(.vertical, 8)
            .background(
                signInMethod == method ? Color.accentColor.opacity(0.1) : Color.clear,
                in: Capsule()
            )
        }
    }
}

#Preview {
    SWAuthView()
        .environment(SWUserManager(skipAuthCheck: true))
}

// MARK: - Auth Error Localization

/// Converts auth errors to user-friendly messages.
/// Scoped to this file to avoid polluting the global Error namespace in consuming apps.
private enum SWAuthErrorHelper {

    /// Returns a user-friendly message for any error thrown by Amplify Auth operations
    static func displayMessage(for error: Error) -> String {
        if let authError = error as? AuthError {
            if let cognitoError = authError.underlyingError as? AWSCognitoAuthError {
                return cognitoMessage(for: cognitoError)
            }
            return authMessage(for: authError)
        }
        return error.localizedDescription
    }

    // MARK: - AuthError Messages

    private static func authMessage(for error: AuthError) -> String {
        switch error {
        case .notAuthorized:
            return "Incorrect email or password"
        case .signedOut:
            return "Please sign in first"
        case .validation:
            return "Invalid input"
        case .configuration:
            return "App configuration error"
        case .service, .unknown, .invalidState:
            let desc = error.errorDescription.lowercased()
            if desc.contains("incorrect username or password") {
                return "Incorrect email or password"
            }
            if desc.contains("user does not exist") || desc.contains("user not found") {
                return "This email is not registered"
            }
            if desc.contains("user is not confirmed") {
                return "Please verify your email first"
            }
            return "Service error, please try again"
        default:
            return "Operation failed, please try again"
        }
    }

    // MARK: - AWSCognitoAuthError Messages

    private static func cognitoMessage(for error: AWSCognitoAuthError) -> String {
        switch error {
        case .userNotFound:
            return "This email is not registered"
        case .userNotConfirmed:
            return "Please verify your email first"
        case .usernameExists:
            return "This email is already registered"
        case .codeDelivery:
            return "Failed to send verification code"
        case .codeMismatch:
            return "Incorrect verification code"
        case .codeExpired:
            return "Verification code expired"
        case .invalidPassword:
            return "Password must be at least 8 characters"
        case .limitExceeded, .failedAttemptsLimitExceeded, .requestLimitExceeded, .limitExceededException:
            return "Too many attempts, please try again later"
        case .network, .lambda, .externalServiceException:
            return "Network error, please try again"
        default:
            return "An error occurred, please try again"
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWAuth/SWAuthView+macOS.swift`
```
//
//  SWAuthView+macOS.swift
//  ShipSwift
//
//  macOS-native authentication view.
//  Email sign-in/up, verification, forgot/reset password, Apple and Google sign-in.
//  Phone sign-in is not included (macOS convention).
//
//  Designed as a centered 380pt panel with native macOS control styles.
//
//  Created by Wei Zhong on 3/7/26.
//

import SwiftUI
import Amplify
import AWSCognitoAuthPlugin

struct SWAuthView: View {

    var isDemo: Bool = false

    // MARK: - Environment

    @Environment(SWUserManager.self) private var userManager

    // MARK: - View Mode

    private enum ViewMode {
        case signIn
        case signUp
        case confirmSignUp
        case forgotPassword
        case resetPassword
    }

    private enum LoadingState {
        case idle
        case sendingCode
        case verifying
        case signingIn
    }

    // MARK: - State

    @State private var viewMode: ViewMode = .signIn
    @State private var loadingState: LoadingState = .idle
    @State private var agreementChecked = false

    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    @State private var verificationCode = ""
    @FocusState private var isCodeFocused: Bool

    @State private var newPassword = ""
    @State private var confirmNewPassword = ""
    @State private var resetCode = ""

    // MARK: - Validation

    private var isValidEmail: Bool {
        email.range(of: #"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"#,
                    options: .regularExpression) != nil
    }
    private var isValidPassword: Bool { password.count >= 8 }
    private var passwordsMatch: Bool { password == confirmPassword }
    private var isValidCode: Bool { verificationCode.count == 6 }
    private var isValidResetCode: Bool { resetCode.count == 6 }
    private var isValidNewPassword: Bool { newPassword.count >= 8 }
    private var newPasswordsMatch: Bool { newPassword == confirmNewPassword }

    private var isEmailFormValid: Bool {
        viewMode == .signUp
            ? isValidEmail && isValidPassword && passwordsMatch
            : isValidEmail && isValidPassword
    }

    // MARK: - Body

    var body: some View {
        ZStack {
            Color(NSColor.windowBackgroundColor).ignoresSafeArea()

            ScrollView {
                VStack(spacing: 0) {
                    Spacer(minLength: 40)
                    panel
                    Spacer(minLength: 40)
                }
                .frame(maxWidth: .infinity)
            }
        }
        .task { await prefetchNetworkPermission() }
    }

    // MARK: - Panel

    private var panel: some View {
        VStack(spacing: 28) {
            header

            switch viewMode {
            case .signIn:         signInSection
            case .signUp:         signUpSection
            case .confirmSignUp:  confirmSignUpSection
            case .forgotPassword: forgotPasswordSection
            case .resetPassword:  resetPasswordSection
            }
        }
        .padding(36)
        .frame(maxWidth: 380)
        .background(Color(NSColor.controlBackgroundColor))
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .shadow(color: .black.opacity(0.08), radius: 16, x: 0, y: 4)
    }

    // MARK: - Header

    private var header: some View {
        VStack(spacing: 8) {
            Image(systemName: "person.circle.fill")
                .resizable()
                .scaledToFit()
                .frame(width: 56, height: 56)
                .foregroundStyle(Color.accentColor)

            Text(headerTitle)
                .font(.title2)
                .fontWeight(.semibold)

            Text(headerSubtitle)
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
        }
    }

    private var headerTitle: String {
        switch viewMode {
        case .signIn:         "Welcome Back"
        case .signUp:         "Create Account"
        case .confirmSignUp:  "Verify Email"
        case .forgotPassword: "Forgot Password"
        case .resetPassword:  "Reset Password"
        }
    }

    private var headerSubtitle: String {
        switch viewMode {
        case .signIn:         "Sign in to continue"
        case .signUp:         "Sign up with your email"
        case .confirmSignUp:  "Enter the 6-digit code sent to \(email)"
        case .forgotPassword: "Enter your email to receive a reset code"
        case .resetPassword:  "Enter the code and your new password"
        }
    }

    // MARK: - Sign In

    private var signInSection: some View {
        VStack(spacing: 16) {
            emailField
            passwordField(text: $password, placeholder: "Password", newPassword: false)

            SWAgreementChecker(agreementChecked: $agreementChecked)

            primaryButton(
                title: "Sign In",
                loadingTitle: "Signing In…",
                isLoading: loadingState == .signingIn,
                disabled: !isEmailFormValid || !agreementChecked
            ) { signInWithEmail() }

            HStack(spacing: 20) {
                linkButton("Forgot Password?") {
                    withAnimation { viewMode = .forgotPassword }
                }
                linkButton("Create Account") {
                    withAnimation { viewMode = .signUp; confirmPassword = "" }
                }
            }

            socialDivider

            socialButtons
        }
    }

    // MARK: - Sign Up

    private var signUpSection: some View {
        VStack(spacing: 12) {
            emailField
            passwordField(text: $password, placeholder: "Password", newPassword: true)

            if !password.isEmpty {
                passwordHint(valid: isValidPassword)
            }

            passwordField(text: $confirmPassword, placeholder: "Confirm Password", newPassword: true)

            if !confirmPassword.isEmpty && !passwordsMatch {
                Text("Passwords do not match")
                    .font(.caption)
                    .foregroundStyle(.red)
                    .frame(maxWidth: .infinity, alignment: .leading)
            }

            SWAgreementChecker(agreementChecked: $agreementChecked)

            primaryButton(
                title: "Create Account",
                loadingTitle: "Creating…",
                isLoading: loadingState == .signingIn,
                disabled: !isEmailFormValid || !agreementChecked
            ) { signUpWithEmail() }

            linkButton("Already have an account? Sign In") {
                withAnimation { viewMode = .signIn }
            }
        }
    }

    // MARK: - Confirm Sign Up

    private var confirmSignUpSection: some View {
        VStack(spacing: 16) {
            codeField(text: $verificationCode)

            primaryButton(
                title: "Verify Email",
                loadingTitle: "Verifying…",
                isLoading: loadingState == .verifying,
                disabled: !isValidCode
            ) { confirmSignUp() }

            HStack(spacing: 20) {
                linkButton("Resend Code") { resendEmailCode() }
                linkButton("Back to Sign In") {
                    withAnimation { viewMode = .signIn; verificationCode = "" }
                }
            }
        }
        .task {
            try? await Task.sleep(for: .milliseconds(300))
            isCodeFocused = true
        }
    }

    // MARK: - Forgot Password

    private var forgotPasswordSection: some View {
        VStack(spacing: 16) {
            emailField

            primaryButton(
                title: "Send Reset Code",
                loadingTitle: "Sending…",
                isLoading: loadingState == .sendingCode,
                disabled: !isValidEmail
            ) { sendResetCode() }

            backToSignIn
        }
    }

    // MARK: - Reset Password

    private var resetPasswordSection: some View {
        VStack(spacing: 12) {
            VStack(alignment: .leading, spacing: 4) {
                Text("Verification Code").font(.caption).foregroundStyle(.secondary)
                codeField(text: $resetCode)
            }

            VStack(alignment: .leading, spacing: 4) {
                Text("New Password").font(.caption).foregroundStyle(.secondary)
                passwordField(text: $newPassword, placeholder: "New Password", newPassword: true)
            }

            if !newPassword.isEmpty {
                passwordHint(valid: isValidNewPassword)
            }

            VStack(alignment: .leading, spacing: 4) {
                Text("Confirm New Password").font(.caption).foregroundStyle(.secondary)
                passwordField(text: $confirmNewPassword, placeholder: "Confirm New Password", newPassword: true)
                if !confirmNewPassword.isEmpty && !newPasswordsMatch {
                    Text("Passwords do not match")
                        .font(.caption)
                        .foregroundStyle(.red)
                }
            }

            primaryButton(
                title: "Reset Password",
                loadingTitle: "Resetting…",
                isLoading: loadingState == .verifying,
                disabled: !isValidResetCode || !isValidNewPassword || !newPasswordsMatch
            ) { confirmResetPassword() }

            backToSignIn
        }
    }

    // MARK: - Reusable Controls

    private var emailField: some View {
        TextField("Email", text: $email)
            .textContentType(.emailAddress)
            .autocorrectionDisabled()
            .textFieldStyle(.roundedBorder)
    }

    private func passwordField(text: Binding<String>, placeholder: String, newPassword: Bool) -> some View {
        SecureField(placeholder, text: text)
            .textContentType(newPassword ? .newPassword : .password)
            .textFieldStyle(.roundedBorder)
    }

    private func codeField(text: Binding<String>) -> some View {
        TextField("000000", text: text)
            .textContentType(.oneTimeCode)
            .focused($isCodeFocused)
            .multilineTextAlignment(.center)
            .font(.title2.monospacedDigit())
            .textFieldStyle(.roundedBorder)
            .onChange(of: text.wrappedValue) { _, newValue in
                text.wrappedValue = String(newValue.filter(\.isNumber).prefix(6))
            }
    }

    private func passwordHint(valid: Bool) -> some View {
        HStack(spacing: 4) {
            Image(systemName: valid ? "checkmark.circle.fill" : "circle")
                .foregroundStyle(valid ? .green : .secondary)
            Text("At least 8 characters")
                .foregroundStyle(valid ? .primary : .secondary)
        }
        .font(.caption)
        .frame(maxWidth: .infinity, alignment: .leading)
    }

    private func primaryButton(
        title: String,
        loadingTitle: String,
        isLoading: Bool,
        disabled: Bool,
        action: @escaping () -> Void
    ) -> some View {
        Button(action: action) {
            HStack(spacing: 6) {
                if isLoading { ProgressView().controlSize(.small) }
                Text(isLoading ? loadingTitle : title)
                    .frame(maxWidth: .infinity)
            }
        }
        .buttonStyle(.borderedProminent)
        .controlSize(.large)
        .disabled(disabled || isLoading)
    }

    private func linkButton(_ title: String, action: @escaping () -> Void) -> some View {
        Button(title, action: action)
            .buttonStyle(.plain)
            .font(.subheadline)
            .foregroundStyle(Color.accentColor)
    }

    private var backToSignIn: some View {
        linkButton("Back to Sign In") {
            withAnimation {
                viewMode = .signIn
                verificationCode = ""
                resetCode = ""
                newPassword = ""
                confirmNewPassword = ""
            }
        }
    }

    private var socialDivider: some View {
        HStack {
            Rectangle().fill(.tertiary).frame(height: 1)
            Text("or continue with")
                .font(.caption)
                .foregroundStyle(.secondary)
            Rectangle().fill(.tertiary).frame(height: 1)
        }
    }

    private var socialButtons: some View {
        HStack(spacing: 12) {
            Button {
                signInWithApple()
            } label: {
                Label("Apple", systemImage: "apple.logo")
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .controlSize(.large)

            Button {
                signInWithGoogle()
            } label: {
                Label("Google", systemImage: "g.circle.fill")
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .controlSize(.large)
        }
    }

    // MARK: - Actions

    private func demoGuard() -> Bool {
        guard isDemo else { return false }
        SWAlertManager.shared.show(.info, message: "UI Demo — auth actions are not functional")
        return true
    }

    private func prefetchNetworkPermission() async {
        guard let url = URL(string: "https://www.apple.com") else { return }
        _ = try? await URLSession.shared.data(from: url)
    }

    private func signInWithEmail() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        loadingState = .signingIn
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.signIn(email: email, password: password)
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signUpWithEmail() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        loadingState = .signingIn
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.signUp(email: email, password: password)
                withAnimation { viewMode = .confirmSignUp }
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func confirmSignUp() {
        guard !demoGuard() else { return }
        loadingState = .verifying
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.confirmSignUp(email: email, code: verificationCode)
                try await userManager.signIn(email: email, password: password)
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func resendEmailCode() {
        guard !demoGuard() else { return }
        Task {
            do {
                try await userManager.resendSignUpCode(email: email)
                SWAlertManager.shared.show(.success, message: "Code sent to \(email)")
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func sendResetCode() {
        guard !demoGuard() else { return }
        loadingState = .sendingCode
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.forgotPassword(email: email)
                withAnimation { viewMode = .resetPassword }
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func confirmResetPassword() {
        guard !demoGuard() else { return }
        loadingState = .verifying
        Task {
            defer { loadingState = .idle }
            do {
                try await userManager.confirmResetPassword(email: email, newPassword: newPassword, code: resetCode)
                SWAlertManager.shared.show(.success, message: "Password reset successfully")
                withAnimation {
                    viewMode = .signIn
                    resetCode = ""
                    newPassword = ""
                    confirmNewPassword = ""
                    password = ""
                }
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signInWithApple() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        Task {
            do {
                try await userManager.signInWithApple()
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }

    private func signInWithGoogle() {
        guard !demoGuard() else { return }
        guard agreementChecked else {
            SWAlertManager.shared.show(.error, message: "Please agree to the Terms of Service and Privacy Policy")
            return
        }
        Task {
            do {
                try await userManager.signInWithGoogle()
            } catch {
                SWAlertManager.shared.show(.error, message: SWMacAuthErrorHelper.displayMessage(for: error))
            }
        }
    }
}

#Preview {
    SWAuthView()
        .environment(SWUserManager(skipAuthCheck: true))
        .frame(width: 600, height: 700)
}

// MARK: - Auth Error Localization

private enum SWMacAuthErrorHelper {

    static func displayMessage(for error: Error) -> String {
        if let authError = error as? AuthError {
            if let cognitoError = authError.underlyingError as? AWSCognitoAuthError {
                return cognitoMessage(for: cognitoError)
            }
            return authMessage(for: authError)
        }
        return error.localizedDescription
    }

    private static func authMessage(for error: AuthError) -> String {
        switch error {
        case .notAuthorized:   return "Incorrect email or password"
        case .signedOut:       return "Please sign in first"
        case .validation:      return "Invalid input"
        case .configuration:   return "App configuration error"
        default:
            let desc = error.errorDescription.lowercased()
            if desc.contains("incorrect username or password") { return "Incorrect email or password" }
            if desc.contains("user does not exist")            { return "This email is not registered" }
            if desc.contains("user is not confirmed")          { return "Please verify your email first" }
            return "Service error, please try again"
        }
    }

    private static func cognitoMessage(for error: AWSCognitoAuthError) -> String {
        switch error {
        case .userNotFound:        return "This email is not registered"
        case .userNotConfirmed:    return "Please verify your email first"
        case .usernameExists:      return "This email is already registered"
        case .codeDelivery:        return "Failed to send verification code"
        case .codeMismatch:        return "Incorrect verification code"
        case .codeExpired:         return "Verification code expired"
        case .invalidPassword:     return "Password must be at least 8 characters"
        case .limitExceeded, .failedAttemptsLimitExceeded, .requestLimitExceeded, .limitExceededException:
            return "Too many attempts, please try again later"
        case .network, .lambda, .externalServiceException:
            return "Network error, please try again"
        default:                   return "An error occurred, please try again"
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWAuth/SWCountryData.swift`
```
//
//  SWCountryData.swift
//  ShipSwift
//
//  Phone country code and flag data for international auth.
//  Provides the SWCountry model and a static list of 200+ countries with
//  dial codes, flag emojis, names, and phone number length ranges.
//
//  Usage:
//    // 1. Access the full country list
//    let countries = SWCountryData.allCountries  // [SWCountry]
//
//    // 2. Each SWCountry has: code, flag, name, phoneLength
//    let us = SWCountryData.allCountries.first { $0.name == "United States" }
//    // us?.code == "+1", us?.flag == "...", us?.phoneLength == 10...10
//
//    // 3. Look up flag emoji by phone code
//    let flag = SWCountryData.flag(for: "+86")    // returns China flag
//
//    // 4. Get valid phone number length range by country code
//    let range = SWCountryData.phoneLength(for: "+44")  // 10...10 (UK)
//
//    // 5. Use in a country picker
//    ForEach(SWCountryData.allCountries, id: \.code) { country in
//        Text("\(country.flag) \(country.name) (\(country.code))")
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation

struct SWCountry {
    let code: String
    let flag: String
    let name: String
    let phoneLength: ClosedRange<Int>
}

struct SWCountryData {
    /// Look up country flag by phone code
    static func flag(for code: String) -> String {
        allCountries.first { $0.code == code }?.flag ?? "🌍"
    }

    /// Get phone number length range by country code
    static func phoneLength(for code: String) -> ClosedRange<Int> {
        allCountries.first { $0.code == code }?.phoneLength ?? 8...12
    }

    static let allCountries: [SWCountry] = [
        // A
        SWCountry(code: "+93", flag: "🇦🇫", name: "Afghanistan", phoneLength: 9...9),
        SWCountry(code: "+355", flag: "🇦🇱", name: "Albania", phoneLength: 9...9),
        SWCountry(code: "+213", flag: "🇩🇿", name: "Algeria", phoneLength: 9...9),
        SWCountry(code: "+1", flag: "🇦🇸", name: "American Samoa", phoneLength: 10...10),
        SWCountry(code: "+376", flag: "🇦🇩", name: "Andorra", phoneLength: 6...9),
        SWCountry(code: "+244", flag: "🇦🇴", name: "Angola", phoneLength: 9...9),
        SWCountry(code: "+1", flag: "🇦🇮", name: "Anguilla", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇦🇬", name: "Antigua and Barbuda", phoneLength: 10...10),
        SWCountry(code: "+54", flag: "🇦🇷", name: "Argentina", phoneLength: 10...10),
        SWCountry(code: "+374", flag: "🇦🇲", name: "Armenia", phoneLength: 8...8),
        SWCountry(code: "+297", flag: "🇦🇼", name: "Aruba", phoneLength: 7...7),
        SWCountry(code: "+61", flag: "🇦🇺", name: "Australia", phoneLength: 9...9),
        SWCountry(code: "+43", flag: "🇦🇹", name: "Austria", phoneLength: 10...11),
        SWCountry(code: "+994", flag: "🇦🇿", name: "Azerbaijan", phoneLength: 9...9),

        // B
        SWCountry(code: "+1", flag: "🇧🇸", name: "Bahamas", phoneLength: 10...10),
        SWCountry(code: "+973", flag: "🇧🇭", name: "Bahrain", phoneLength: 8...8),
        SWCountry(code: "+880", flag: "🇧🇩", name: "Bangladesh", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇧🇧", name: "Barbados", phoneLength: 10...10),
        SWCountry(code: "+375", flag: "🇧🇾", name: "Belarus", phoneLength: 9...9),
        SWCountry(code: "+32", flag: "🇧🇪", name: "Belgium", phoneLength: 9...9),
        SWCountry(code: "+501", flag: "🇧🇿", name: "Belize", phoneLength: 7...7),
        SWCountry(code: "+229", flag: "🇧🇯", name: "Benin", phoneLength: 8...8),
        SWCountry(code: "+1", flag: "🇧🇲", name: "Bermuda", phoneLength: 10...10),
        SWCountry(code: "+975", flag: "🇧🇹", name: "Bhutan", phoneLength: 8...8),
        SWCountry(code: "+591", flag: "🇧🇴", name: "Bolivia", phoneLength: 8...8),
        SWCountry(code: "+387", flag: "🇧🇦", name: "Bosnia and Herzegovina", phoneLength: 8...9),
        SWCountry(code: "+267", flag: "🇧🇼", name: "Botswana", phoneLength: 8...8),
        SWCountry(code: "+55", flag: "🇧🇷", name: "Brazil", phoneLength: 10...11),
        SWCountry(code: "+1", flag: "🇻🇬", name: "British Virgin Islands", phoneLength: 10...10),
        SWCountry(code: "+673", flag: "🇧🇳", name: "Brunei", phoneLength: 7...7),
        SWCountry(code: "+359", flag: "🇧🇬", name: "Bulgaria", phoneLength: 9...9),
        SWCountry(code: "+226", flag: "🇧🇫", name: "Burkina Faso", phoneLength: 8...8),
        SWCountry(code: "+257", flag: "🇧🇮", name: "Burundi", phoneLength: 8...8),

        // C
        SWCountry(code: "+855", flag: "🇰🇭", name: "Cambodia", phoneLength: 8...9),
        SWCountry(code: "+237", flag: "🇨🇲", name: "Cameroon", phoneLength: 9...9),
        SWCountry(code: "+1", flag: "🇨🇦", name: "Canada", phoneLength: 10...10),
        SWCountry(code: "+238", flag: "🇨🇻", name: "Cape Verde", phoneLength: 7...7),
        SWCountry(code: "+1", flag: "🇰🇾", name: "Cayman Islands", phoneLength: 10...10),
        SWCountry(code: "+236", flag: "🇨🇫", name: "Central African Republic", phoneLength: 8...8),
        SWCountry(code: "+235", flag: "🇹🇩", name: "Chad", phoneLength: 8...8),
        SWCountry(code: "+56", flag: "🇨🇱", name: "Chile", phoneLength: 9...9),
        SWCountry(code: "+86", flag: "🇨🇳", name: "China", phoneLength: 11...11),
        SWCountry(code: "+57", flag: "🇨🇴", name: "Colombia", phoneLength: 10...10),
        SWCountry(code: "+269", flag: "🇰🇲", name: "Comoros", phoneLength: 7...7),
        SWCountry(code: "+242", flag: "🇨🇬", name: "Congo", phoneLength: 9...9),
        SWCountry(code: "+243", flag: "🇨🇩", name: "Congo (DRC)", phoneLength: 9...9),
        SWCountry(code: "+682", flag: "🇨🇰", name: "Cook Islands", phoneLength: 5...5),
        SWCountry(code: "+506", flag: "🇨🇷", name: "Costa Rica", phoneLength: 8...8),
        SWCountry(code: "+225", flag: "🇨🇮", name: "Côte d'Ivoire", phoneLength: 10...10),
        SWCountry(code: "+385", flag: "🇭🇷", name: "Croatia", phoneLength: 9...9),
        SWCountry(code: "+53", flag: "🇨🇺", name: "Cuba", phoneLength: 8...8),
        SWCountry(code: "+357", flag: "🇨🇾", name: "Cyprus", phoneLength: 8...8),
        SWCountry(code: "+420", flag: "🇨🇿", name: "Czech Republic", phoneLength: 9...9),

        // D
        SWCountry(code: "+45", flag: "🇩🇰", name: "Denmark", phoneLength: 8...8),
        SWCountry(code: "+253", flag: "🇩🇯", name: "Djibouti", phoneLength: 8...8),
        SWCountry(code: "+1", flag: "🇩🇲", name: "Dominica", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇩🇴", name: "Dominican Republic", phoneLength: 10...10),

        // E
        SWCountry(code: "+593", flag: "🇪🇨", name: "Ecuador", phoneLength: 9...9),
        SWCountry(code: "+20", flag: "🇪🇬", name: "Egypt", phoneLength: 10...10),
        SWCountry(code: "+503", flag: "🇸🇻", name: "El Salvador", phoneLength: 8...8),
        SWCountry(code: "+240", flag: "🇬🇶", name: "Equatorial Guinea", phoneLength: 9...9),
        SWCountry(code: "+291", flag: "🇪🇷", name: "Eritrea", phoneLength: 7...7),
        SWCountry(code: "+372", flag: "🇪🇪", name: "Estonia", phoneLength: 7...8),
        SWCountry(code: "+251", flag: "🇪🇹", name: "Ethiopia", phoneLength: 9...9),

        // F
        SWCountry(code: "+500", flag: "🇫🇰", name: "Falkland Islands", phoneLength: 5...5),
        SWCountry(code: "+298", flag: "🇫🇴", name: "Faroe Islands", phoneLength: 6...6),
        SWCountry(code: "+679", flag: "🇫🇯", name: "Fiji", phoneLength: 7...7),
        SWCountry(code: "+358", flag: "🇫🇮", name: "Finland", phoneLength: 9...10),
        SWCountry(code: "+33", flag: "🇫🇷", name: "France", phoneLength: 9...9),
        SWCountry(code: "+594", flag: "🇬🇫", name: "French Guiana", phoneLength: 9...9),
        SWCountry(code: "+689", flag: "🇵🇫", name: "French Polynesia", phoneLength: 8...8),

        // G
        SWCountry(code: "+241", flag: "🇬🇦", name: "Gabon", phoneLength: 7...8),
        SWCountry(code: "+220", flag: "🇬🇲", name: "Gambia", phoneLength: 7...7),
        SWCountry(code: "+995", flag: "🇬🇪", name: "Georgia", phoneLength: 9...9),
        SWCountry(code: "+49", flag: "🇩🇪", name: "Germany", phoneLength: 10...11),
        SWCountry(code: "+233", flag: "🇬🇭", name: "Ghana", phoneLength: 9...9),
        SWCountry(code: "+350", flag: "🇬🇮", name: "Gibraltar", phoneLength: 8...8),
        SWCountry(code: "+30", flag: "🇬🇷", name: "Greece", phoneLength: 10...10),
        SWCountry(code: "+299", flag: "🇬🇱", name: "Greenland", phoneLength: 6...6),
        SWCountry(code: "+1", flag: "🇬🇩", name: "Grenada", phoneLength: 10...10),
        SWCountry(code: "+590", flag: "🇬🇵", name: "Guadeloupe", phoneLength: 9...9),
        SWCountry(code: "+1", flag: "🇬🇺", name: "Guam", phoneLength: 10...10),
        SWCountry(code: "+502", flag: "🇬🇹", name: "Guatemala", phoneLength: 8...8),
        SWCountry(code: "+224", flag: "🇬🇳", name: "Guinea", phoneLength: 9...9),
        SWCountry(code: "+245", flag: "🇬🇼", name: "Guinea-Bissau", phoneLength: 7...7),
        SWCountry(code: "+592", flag: "🇬🇾", name: "Guyana", phoneLength: 7...7),

        // H
        SWCountry(code: "+509", flag: "🇭🇹", name: "Haiti", phoneLength: 8...8),
        SWCountry(code: "+504", flag: "🇭🇳", name: "Honduras", phoneLength: 8...8),
        SWCountry(code: "+852", flag: "🇭🇰", name: "Hong Kong", phoneLength: 8...8),
        SWCountry(code: "+36", flag: "🇭🇺", name: "Hungary", phoneLength: 9...9),

        // I
        SWCountry(code: "+354", flag: "🇮🇸", name: "Iceland", phoneLength: 7...7),
        SWCountry(code: "+91", flag: "🇮🇳", name: "India", phoneLength: 10...10),
        SWCountry(code: "+62", flag: "🇮🇩", name: "Indonesia", phoneLength: 10...12),
        SWCountry(code: "+98", flag: "🇮🇷", name: "Iran", phoneLength: 10...10),
        SWCountry(code: "+964", flag: "🇮🇶", name: "Iraq", phoneLength: 10...10),
        SWCountry(code: "+353", flag: "🇮🇪", name: "Ireland", phoneLength: 9...9),
        SWCountry(code: "+972", flag: "🇮🇱", name: "Israel", phoneLength: 9...9),
        SWCountry(code: "+39", flag: "🇮🇹", name: "Italy", phoneLength: 10...10),

        // J
        SWCountry(code: "+1", flag: "🇯🇲", name: "Jamaica", phoneLength: 10...10),
        SWCountry(code: "+81", flag: "🇯🇵", name: "Japan", phoneLength: 10...10),
        SWCountry(code: "+962", flag: "🇯🇴", name: "Jordan", phoneLength: 9...9),

        // K
        SWCountry(code: "+7", flag: "🇰🇿", name: "Kazakhstan", phoneLength: 10...10),
        SWCountry(code: "+254", flag: "🇰🇪", name: "Kenya", phoneLength: 9...9),
        SWCountry(code: "+686", flag: "🇰🇮", name: "Kiribati", phoneLength: 8...8),
        SWCountry(code: "+383", flag: "🇽🇰", name: "Kosovo", phoneLength: 8...9),
        SWCountry(code: "+965", flag: "🇰🇼", name: "Kuwait", phoneLength: 8...8),
        SWCountry(code: "+996", flag: "🇰🇬", name: "Kyrgyzstan", phoneLength: 9...9),

        // L
        SWCountry(code: "+856", flag: "🇱🇦", name: "Laos", phoneLength: 10...10),
        SWCountry(code: "+371", flag: "🇱🇻", name: "Latvia", phoneLength: 8...8),
        SWCountry(code: "+961", flag: "🇱🇧", name: "Lebanon", phoneLength: 7...8),
        SWCountry(code: "+266", flag: "🇱🇸", name: "Lesotho", phoneLength: 8...8),
        SWCountry(code: "+231", flag: "🇱🇷", name: "Liberia", phoneLength: 7...8),
        SWCountry(code: "+218", flag: "🇱🇾", name: "Libya", phoneLength: 9...9),
        SWCountry(code: "+423", flag: "🇱🇮", name: "Liechtenstein", phoneLength: 7...7),
        SWCountry(code: "+370", flag: "🇱🇹", name: "Lithuania", phoneLength: 8...8),
        SWCountry(code: "+352", flag: "🇱🇺", name: "Luxembourg", phoneLength: 9...9),

        // M
        SWCountry(code: "+853", flag: "🇲🇴", name: "Macau", phoneLength: 8...8),
        SWCountry(code: "+389", flag: "🇲🇰", name: "Macedonia", phoneLength: 8...8),
        SWCountry(code: "+261", flag: "🇲🇬", name: "Madagascar", phoneLength: 9...9),
        SWCountry(code: "+265", flag: "🇲🇼", name: "Malawi", phoneLength: 9...9),
        SWCountry(code: "+60", flag: "🇲🇾", name: "Malaysia", phoneLength: 9...10),
        SWCountry(code: "+960", flag: "🇲🇻", name: "Maldives", phoneLength: 7...7),
        SWCountry(code: "+223", flag: "🇲🇱", name: "Mali", phoneLength: 8...8),
        SWCountry(code: "+356", flag: "🇲🇹", name: "Malta", phoneLength: 8...8),
        SWCountry(code: "+692", flag: "🇲🇭", name: "Marshall Islands", phoneLength: 7...7),
        SWCountry(code: "+596", flag: "🇲🇶", name: "Martinique", phoneLength: 9...9),
        SWCountry(code: "+222", flag: "🇲🇷", name: "Mauritania", phoneLength: 8...8),
        SWCountry(code: "+230", flag: "🇲🇺", name: "Mauritius", phoneLength: 8...8),
        SWCountry(code: "+52", flag: "🇲🇽", name: "Mexico", phoneLength: 10...10),
        SWCountry(code: "+691", flag: "🇫🇲", name: "Micronesia", phoneLength: 7...7),
        SWCountry(code: "+373", flag: "🇲🇩", name: "Moldova", phoneLength: 8...8),
        SWCountry(code: "+377", flag: "🇲🇨", name: "Monaco", phoneLength: 8...9),
        SWCountry(code: "+976", flag: "🇲🇳", name: "Mongolia", phoneLength: 8...8),
        SWCountry(code: "+382", flag: "🇲🇪", name: "Montenegro", phoneLength: 8...8),
        SWCountry(code: "+212", flag: "🇲🇦", name: "Morocco", phoneLength: 9...9),
        SWCountry(code: "+258", flag: "🇲🇿", name: "Mozambique", phoneLength: 9...9),
        SWCountry(code: "+95", flag: "🇲🇲", name: "Myanmar", phoneLength: 8...10),

        // N
        SWCountry(code: "+264", flag: "🇳🇦", name: "Namibia", phoneLength: 9...9),
        SWCountry(code: "+674", flag: "🇳🇷", name: "Nauru", phoneLength: 7...7),
        SWCountry(code: "+977", flag: "🇳🇵", name: "Nepal", phoneLength: 10...10),
        SWCountry(code: "+31", flag: "🇳🇱", name: "Netherlands", phoneLength: 9...9),
        SWCountry(code: "+687", flag: "🇳🇨", name: "New Caledonia", phoneLength: 6...6),
        SWCountry(code: "+64", flag: "🇳🇿", name: "New Zealand", phoneLength: 9...10),
        SWCountry(code: "+505", flag: "🇳🇮", name: "Nicaragua", phoneLength: 8...8),
        SWCountry(code: "+227", flag: "🇳🇪", name: "Niger", phoneLength: 8...8),
        SWCountry(code: "+234", flag: "🇳🇬", name: "Nigeria", phoneLength: 10...10),
        SWCountry(code: "+850", flag: "🇰🇵", name: "North Korea", phoneLength: 10...10),
        SWCountry(code: "+47", flag: "🇳🇴", name: "Norway", phoneLength: 8...8),

        // O
        SWCountry(code: "+968", flag: "🇴🇲", name: "Oman", phoneLength: 8...8),

        // P
        SWCountry(code: "+92", flag: "🇵🇰", name: "Pakistan", phoneLength: 10...10),
        SWCountry(code: "+680", flag: "🇵🇼", name: "Palau", phoneLength: 7...7),
        SWCountry(code: "+507", flag: "🇵🇦", name: "Panama", phoneLength: 8...8),
        SWCountry(code: "+675", flag: "🇵🇬", name: "Papua New Guinea", phoneLength: 8...8),
        SWCountry(code: "+595", flag: "🇵🇾", name: "Paraguay", phoneLength: 9...9),
        SWCountry(code: "+51", flag: "🇵🇪", name: "Peru", phoneLength: 9...9),
        SWCountry(code: "+63", flag: "🇵🇭", name: "Philippines", phoneLength: 10...10),
        SWCountry(code: "+48", flag: "🇵🇱", name: "Poland", phoneLength: 9...9),
        SWCountry(code: "+351", flag: "🇵🇹", name: "Portugal", phoneLength: 9...9),
        SWCountry(code: "+1", flag: "🇵🇷", name: "Puerto Rico", phoneLength: 10...10),

        // Q
        SWCountry(code: "+974", flag: "🇶🇦", name: "Qatar", phoneLength: 8...8),

        // R
        SWCountry(code: "+262", flag: "🇷🇪", name: "Reunion", phoneLength: 9...9),
        SWCountry(code: "+40", flag: "🇷🇴", name: "Romania", phoneLength: 9...9),
        SWCountry(code: "+7", flag: "🇷🇺", name: "Russia", phoneLength: 10...10),
        SWCountry(code: "+250", flag: "🇷🇼", name: "Rwanda", phoneLength: 9...9),

        // S
        SWCountry(code: "+1", flag: "🇰🇳", name: "Saint Kitts and Nevis", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇱🇨", name: "Saint Lucia", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇻🇨", name: "Saint Vincent and the Grenadines", phoneLength: 10...10),
        SWCountry(code: "+685", flag: "🇼🇸", name: "Samoa", phoneLength: 7...7),
        SWCountry(code: "+378", flag: "🇸🇲", name: "San Marino", phoneLength: 8...10),
        SWCountry(code: "+239", flag: "🇸🇹", name: "São Tomé and Príncipe", phoneLength: 7...7),
        SWCountry(code: "+966", flag: "🇸🇦", name: "Saudi Arabia", phoneLength: 9...9),
        SWCountry(code: "+221", flag: "🇸🇳", name: "Senegal", phoneLength: 9...9),
        SWCountry(code: "+381", flag: "🇷🇸", name: "Serbia", phoneLength: 9...9),
        SWCountry(code: "+248", flag: "🇸🇨", name: "Seychelles", phoneLength: 7...7),
        SWCountry(code: "+232", flag: "🇸🇱", name: "Sierra Leone", phoneLength: 8...8),
        SWCountry(code: "+65", flag: "🇸🇬", name: "Singapore", phoneLength: 8...8),
        SWCountry(code: "+421", flag: "🇸🇰", name: "Slovakia", phoneLength: 9...9),
        SWCountry(code: "+386", flag: "🇸🇮", name: "Slovenia", phoneLength: 8...8),
        SWCountry(code: "+677", flag: "🇸🇧", name: "Solomon Islands", phoneLength: 7...7),
        SWCountry(code: "+252", flag: "🇸🇴", name: "Somalia", phoneLength: 8...9),
        SWCountry(code: "+27", flag: "🇿🇦", name: "South Africa", phoneLength: 9...9),
        SWCountry(code: "+82", flag: "🇰🇷", name: "South Korea", phoneLength: 10...11),
        SWCountry(code: "+211", flag: "🇸🇸", name: "South Sudan", phoneLength: 9...9),
        SWCountry(code: "+34", flag: "🇪🇸", name: "Spain", phoneLength: 9...9),
        SWCountry(code: "+94", flag: "🇱🇰", name: "Sri Lanka", phoneLength: 9...9),
        SWCountry(code: "+249", flag: "🇸🇩", name: "Sudan", phoneLength: 9...9),
        SWCountry(code: "+597", flag: "🇸🇷", name: "Suriname", phoneLength: 7...7),
        SWCountry(code: "+268", flag: "🇸🇿", name: "Swaziland", phoneLength: 8...8),
        SWCountry(code: "+46", flag: "🇸🇪", name: "Sweden", phoneLength: 9...9),
        SWCountry(code: "+41", flag: "🇨🇭", name: "Switzerland", phoneLength: 9...9),
        SWCountry(code: "+963", flag: "🇸🇾", name: "Syria", phoneLength: 9...9),

        // T
        SWCountry(code: "+886", flag: "🇹🇼", name: "Taiwan", phoneLength: 9...9),
        SWCountry(code: "+992", flag: "🇹🇯", name: "Tajikistan", phoneLength: 9...9),
        SWCountry(code: "+255", flag: "🇹🇿", name: "Tanzania", phoneLength: 9...9),
        SWCountry(code: "+66", flag: "🇹🇭", name: "Thailand", phoneLength: 9...9),
        SWCountry(code: "+228", flag: "🇹🇬", name: "Togo", phoneLength: 8...8),
        SWCountry(code: "+676", flag: "🇹🇴", name: "Tonga", phoneLength: 7...7),
        SWCountry(code: "+1", flag: "🇹🇹", name: "Trinidad and Tobago", phoneLength: 10...10),
        SWCountry(code: "+216", flag: "🇹🇳", name: "Tunisia", phoneLength: 8...8),
        SWCountry(code: "+90", flag: "🇹🇷", name: "Turkey", phoneLength: 10...10),
        SWCountry(code: "+993", flag: "🇹🇲", name: "Turkmenistan", phoneLength: 8...8),
        SWCountry(code: "+1", flag: "🇹🇨", name: "Turks and Caicos Islands", phoneLength: 10...10),
        SWCountry(code: "+688", flag: "🇹🇻", name: "Tuvalu", phoneLength: 6...6),

        // U
        SWCountry(code: "+256", flag: "🇺🇬", name: "Uganda", phoneLength: 9...9),
        SWCountry(code: "+380", flag: "🇺🇦", name: "Ukraine", phoneLength: 9...9),
        SWCountry(code: "+971", flag: "🇦🇪", name: "United Arab Emirates", phoneLength: 9...9),
        SWCountry(code: "+44", flag: "🇬🇧", name: "United Kingdom", phoneLength: 10...10),
        SWCountry(code: "+1", flag: "🇺🇸", name: "United States", phoneLength: 10...10),
        SWCountry(code: "+598", flag: "🇺🇾", name: "Uruguay", phoneLength: 8...9),
        SWCountry(code: "+998", flag: "🇺🇿", name: "Uzbekistan", phoneLength: 9...9),

        // V
        SWCountry(code: "+678", flag: "🇻🇺", name: "Vanuatu", phoneLength: 7...7),
        SWCountry(code: "+379", flag: "🇻🇦", name: "Vatican City", phoneLength: 10...10),
        SWCountry(code: "+58", flag: "🇻🇪", name: "Venezuela", phoneLength: 10...10),
        SWCountry(code: "+84", flag: "🇻🇳", name: "Vietnam", phoneLength: 9...10),
        SWCountry(code: "+1", flag: "🇻🇮", name: "Virgin Islands (US)", phoneLength: 10...10),

        // Y
        SWCountry(code: "+967", flag: "🇾🇪", name: "Yemen", phoneLength: 9...9),

        // Z
        SWCountry(code: "+260", flag: "🇿🇲", name: "Zambia", phoneLength: 9...9),
        SWCountry(code: "+263", flag: "🇿🇼", name: "Zimbabwe", phoneLength: 9...9)
    ]
}
```

## File: `ShipSwift/SWPackage/SWModule/SWAuth/SWUserManager.swift`
```
//
//  SWUserManager.swift
//  ShipSwift
//
//  User authentication manager with Amplify/Cognito integration.
//  Manages session state, email/password auth, Apple/Google social sign-in,
//  token refresh, guest mode, onboarding flow, and App Store review requests.
//
//  Usage:
//    // 1. Create and inject into SwiftUI environment
//    @State private var userManager = SWUserManager()
//    ContentView()
//        .environment(userManager)
//
//    // 2. Observe session state to control navigation
//    switch userManager.sessionState {
//    case .loading:       LoadingView()
//    case .signedOut:     SWAuthView()
//    case .guest:         MainView()
//    case .onboarding:    OnboardingView()
//    case .ready:         MainView()
//    }
//
//    // 3. Email sign-in / sign-up
//    try await userManager.signUp(email: email, password: password)
//    try await userManager.confirmSignUp(email: email, code: "123456")
//    try await userManager.signIn(email: email, password: password)
//
//    // 4. Social sign-in
//    try await userManager.signInWithApple()
//    try await userManager.signInWithGoogle()
//
//    // 5. Get fresh ID token for API calls (auto-refreshes expired tokens)
//    guard let idToken = await userManager.getFreshIdToken() else { return }
//    await apiService.fetchData(idToken: idToken)
//
//    // 6. Sign out / delete account
//    await userManager.signOut()
//    try await userManager.deleteAccount()
//
//    // 7. Guest mode
//    userManager.skipSignIn()     // enter guest mode
//    userManager.requireSignIn()  // switch back to sign-in page
//
//    // 8. Password reset
//    try await userManager.forgotPassword(email: email)
//    try await userManager.confirmResetPassword(email: email, newPassword: "newPass", code: "123456")
//
//    // 9. Check pro status (requires SWStoreManager)
//    if SWStoreManager.shared.isPro { /* unlock features */ }
//
//    // 10. App Store review request (call after positive user actions)
//    userManager.incrementActionCompletedCount()
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation
import SwiftUI
import StoreKit
import Amplify
import AWSCognitoAuthPlugin
import AWSPluginsCore

#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

// MARK: - Session State

/// User session state
enum SWSessionState: Equatable {
    case loading
    case signedOut(errorMessage: String? = nil)
    case guest                              // Guest mode, skip sign in
    case onboarding(tokens: SWAuthTokens)   // Signed in, onboarding not completed
    case ready(tokens: SWAuthTokens)        // Signed in, onboarding completed

    var isSignedIn: Bool {
        switch self {
        case .onboarding, .ready: return true
        case .signedOut, .loading, .guest: return false
        }
    }

    var isGuest: Bool {
        if case .guest = self { return true }
        return false
    }

    var isLoading: Bool {
        if case .loading = self { return true }
        return false
    }

    var tokens: SWAuthTokens? {
        switch self {
        case .onboarding(let tokens), .ready(let tokens): return tokens
        case .signedOut, .loading, .guest: return nil
        }
    }

    var errorMessage: String? {
        if case .signedOut(let message) = self { return message }
        return nil
    }
}

// MARK: - Auth Tokens

/// Authentication Tokens
struct SWAuthTokens: Equatable {
    let idToken: String
    let accessToken: String
    let refreshToken: String
}

// MARK: - Service Error

/// Service error types
enum SWServiceError: LocalizedError {
    case notSignedIn
    case tokenMissing
    case invalidURL
    case networkError
    case unauthorized
    case serverError(Int)
    case timeout
    case userProfileNotFound
    case userAlreadyExists
    case validationError(String)
    case decodingError
    case encodingError
    case invalidResponse
    case invalidState
    case unknown(String)

    var errorDescription: String? {
        switch self {
        case .notSignedIn: return "Not signed in"
        case .tokenMissing: return "Session expired, please sign in again"
        case .invalidURL: return "Invalid URL"
        case .networkError: return "Network connection failed"
        case .unauthorized: return "Session expired, please sign in again"
        case .serverError(let code): return "Server error (\(code))"
        case .timeout: return "Request timeout, please retry"
        case .userProfileNotFound: return "User profile not found"
        case .userAlreadyExists: return "User profile already exists"
        case .validationError(let message): return "Validation failed: \(message)"
        case .decodingError: return "Data parsing error"
        case .encodingError: return "Data encoding error"
        case .invalidResponse: return "Invalid response"
        case .invalidState: return "Invalid state"
        case .unknown(let message): return message
        }
    }
}

// MARK: - User Manager

@MainActor
@Observable
final class SWUserManager {

    // MARK: - Storage Keys

    private enum StorageKey: String {
        case isFirstLaunch
        case appLaunchCount
        case actionCompletedCount
        case lastReviewRequestDate
        case hasRequestedReview
    }

    // MARK: - Review Request Configuration

    private enum ReviewConfig {
        static let minActions = 2             // At least 2 completed actions
        static let minLaunches = 3            // At least 3 app launches
        static let daysBetweenRequests = 30   // Days between review requests
        static let delayBeforeRequest: Duration = .seconds(1)  // Delay before request
    }

    // MARK: - Properties

    /// Whether to skip the Amplify auth check (used in Preview environments)
    private let skipAuthCheck: Bool

    /// User session state
    var sessionState: SWSessionState = .loading

    /// Whether an authentication operation is in progress
    var isAuthenticating = false

    /// Whether this is the first launch (stored property, trackable by @Observable)
    var isFirstLaunch: Bool = false {
        didSet {
            // Note: stores whether first launch has been completed, so invert the value
            UserDefaults.standard.set(!isFirstLaunch, forKey: StorageKey.isFirstLaunch.rawValue)
        }
    }

    private let authService = SWAuthService.shared

    // Review request related properties
    private var actionCompletedCount: Int {
        get { UserDefaults.standard.integer(forKey: StorageKey.actionCompletedCount.rawValue) }
        set { UserDefaults.standard.set(newValue, forKey: StorageKey.actionCompletedCount.rawValue) }
    }

    private var appLaunchCount: Int {
        get { UserDefaults.standard.integer(forKey: StorageKey.appLaunchCount.rawValue) }
        set { UserDefaults.standard.set(newValue, forKey: StorageKey.appLaunchCount.rawValue) }
    }

    private var hasRequestedReview: Bool {
        get { UserDefaults.standard.bool(forKey: StorageKey.hasRequestedReview.rawValue) }
        set { UserDefaults.standard.set(newValue, forKey: StorageKey.hasRequestedReview.rawValue) }
    }

    private var lastReviewRequestDate: Date? {
        get { UserDefaults.standard.object(forKey: StorageKey.lastReviewRequestDate.rawValue) as? Date }
        set { UserDefaults.standard.set(newValue, forKey: StorageKey.lastReviewRequestDate.rawValue) }
    }

    // MARK: - Initialization

    init(skipAuthCheck: Bool = false) {
        self.skipAuthCheck = skipAuthCheck
        self.isFirstLaunch = !UserDefaults.standard.bool(forKey: StorageKey.isFirstLaunch.rawValue)
        appLaunchCount += 1

        if !skipAuthCheck {
            // Check authentication status
            Task {
                await checkAuthStatus()
            }
        } else {
            sessionState = .signedOut()
        }
    }

    // MARK: - Public Methods

    func completeFirstLaunch() {
        isFirstLaunch = false  // didSet automatically syncs to UserDefaults
    }

    // MARK: - Auth Status Check

    /// Check authentication status and update session state
    func checkAuthStatus() async {
        sessionState = .loading

        let isSignedIn = await authService.isSignedIn()

        if isSignedIn {
            do {
                let tokens = try await authService.fetchTokens()
                // Default to ready state directly
                // If there is an onboarding flow, query backend status here
                sessionState = .ready(tokens: tokens)
            } catch {
                // Session expired or token invalid, sign out to clean up local Amplify cache
                swDebugLog("⚠️ [SWUserManager] Session expired, signing out:", error)
                await authService.signOut()
                sessionState = .signedOut()
            }
        } else {
            sessionState = .signedOut()
        }
    }

    // MARK: - Email/Password Authentication

    /// Sign up
    func signUp(email: String, password: String) async throws {
        isAuthenticating = true
        defer { isAuthenticating = false }
        try await authService.signUp(email: email, password: password)
    }

    /// Confirm email verification code
    func confirmSignUp(email: String, code: String) async throws {
        isAuthenticating = true
        defer { isAuthenticating = false }
        try await authService.confirmSignUp(email: email, code: code)
    }

    /// Resend verification code
    func resendSignUpCode(email: String) async throws {
        try await authService.resendSignUpCode(email: email)
    }

    /// Sign in with email and password
    func signIn(email: String, password: String) async throws {
        isAuthenticating = true
        defer { isAuthenticating = false }

        let tokens = try await authService.signIn(email: email, password: password)
        sessionState = .ready(tokens: tokens)
    }

    // MARK: - Social Sign In

    /// Apple Sign In
    func signInWithApple() async throws {
        swDebugLog("🍎 [Auth] Starting Apple Sign In...")

        guard let window = SWWindowHelper.keyWindow else {
            swDebugLog("🍎 [Auth] ❌ Cannot get window")
            throw SWServiceError.unknown("Cannot get window")
        }

        isAuthenticating = true
        defer { isAuthenticating = false }

        do {
            swDebugLog("🍎 [Auth] Calling authService.signInWithApple...")
            let tokens = try await authService.signInWithApple(presentationAnchor: window)
            swDebugLog("🍎 [Auth] ✅ Apple Sign In successful, got tokens")
            sessionState = .ready(tokens: tokens)
        } catch {
            swDebugLog("🍎 [Auth] ❌ Apple Sign In failed:", error)
            throw error
        }
    }

    /// Google Sign In
    func signInWithGoogle() async throws {
        guard let window = SWWindowHelper.keyWindow else {
            throw SWServiceError.unknown("Cannot get window")
        }

        isAuthenticating = true
        defer { isAuthenticating = false }

        let tokens = try await authService.signInWithGoogle(presentationAnchor: window)
        sessionState = .ready(tokens: tokens)
    }

    // MARK: - Guest Mode

    /// Skip sign in and enter guest mode
    func skipSignIn() {
        sessionState = .guest
    }

    /// Require sign in (switch from guest mode to sign in page)
    func requireSignIn() {
        sessionState = .signedOut()
    }

    // MARK: - Sign Out / Delete Account

    /// Sign out
    func signOut() async {
        await authService.signOut()
        sessionState = .signedOut()
    }

    /// Delete account
    func deleteAccount() async throws {
        try await authService.deleteUser()
        sessionState = .signedOut()
    }

    // MARK: - Phone Authentication

    /// Send phone verification code
    func sendPhoneVerificationCode(phoneNumber: String) async throws {
        isAuthenticating = true
        defer { isAuthenticating = false }
        try await authService.sendPhoneVerificationCode(phoneNumber: phoneNumber)
    }

    /// Confirm phone sign-in with verification code
    func confirmPhoneSignIn(phoneNumber: String, code: String) async throws {
        isAuthenticating = true
        defer { isAuthenticating = false }
        let tokens = try await authService.confirmPhoneSignIn(phoneNumber: phoneNumber, code: code)
        sessionState = .ready(tokens: tokens)
    }

    // MARK: - Password Reset

    /// Forgot password
    func forgotPassword(email: String) async throws {
        try await authService.forgotPassword(email: email)
    }

    /// Reset password
    func confirmResetPassword(email: String, newPassword: String, code: String) async throws {
        try await authService.confirmResetPassword(email: email, newPassword: newPassword, code: code)
    }

    // MARK: - Onboarding

    /// Complete onboarding questionnaire, transition to ready state
    func completeOnboarding() {
        guard let tokens = sessionState.tokens else { return }
        sessionState = .ready(tokens: tokens)
    }

    // MARK: - Token Management

    /// Get the latest ID Token (automatically refreshes expired tokens)
    ///
    /// Important: Use this method to get token before each API call,
    /// instead of directly using the cached `sessionState.tokens?.idToken`
    ///
    /// How it works:
    /// 1. Calls `authService.fetchTokens()` -> `Amplify.Auth.fetchAuthSession()`
    /// 2. SDK automatically checks if ID Token is expired (default 1 hour)
    /// 3. If expired, SDK uses Refresh Token to obtain a new ID Token
    /// 4. Also updates the cached tokens
    ///
    /// Returns nil when:
    /// - User is not signed in
    /// - Refresh Token expired (30 days of inactivity), requires re-sign-in
    ///
    /// Usage example:
    /// ```swift
    /// guard let idToken = await userManager.getFreshIdToken() else { return }
    /// await apiService.fetchData(idToken: idToken)
    /// ```
    func getFreshIdToken() async -> String? {
        guard sessionState.isSignedIn else {
            return nil
        }

        do {
            let tokens = try await authService.fetchTokens()

            // Also update the cached tokens
            switch sessionState {
            case .onboarding:
                sessionState = .onboarding(tokens: tokens)
            case .ready:
                sessionState = .ready(tokens: tokens)
            default:
                break
            }

            return tokens.idToken
        } catch {
            // Refresh token expired, sign out to avoid "fake logged-in" state
            swDebugLog("⚠️ [SWUserManager] Token refresh failed, signing out:", error)
            await authService.signOut()
            sessionState = .signedOut()
            return nil
        }
    }

    /// Refresh session
    func refreshSession() async throws {
        guard sessionState.tokens != nil else {
            throw SWServiceError.tokenMissing
        }

        let newTokens = try await authService.refreshSession()

        switch sessionState {
        case .onboarding:
            sessionState = .onboarding(tokens: newTokens)
        case .ready:
            sessionState = .ready(tokens: newTokens)
        default:
            break
        }
    }

    // MARK: - Review Request

    /// Record completed action count
    func incrementActionCompletedCount() {
        actionCompletedCount += 1
        requestReviewIfAppropriate()
    }

    /// Call after user completes a positive action
    func recordPositiveUserAction() {
        requestReviewIfAppropriate()
    }

    private func requestReviewIfAppropriate() {
        guard shouldRequestReview() else { return }

        Task {
            try? await Task.sleep(for: ReviewConfig.delayBeforeRequest)
            await requestReview()
        }
    }

    private func shouldRequestReview() -> Bool {
        if hasRequestedReview, let lastDate = lastReviewRequestDate {
            let daysSinceLastRequest = Calendar.current.dateComponents(
                [.day],
                from: lastDate,
                to: .now
            ).day ?? 0

            guard daysSinceLastRequest >= ReviewConfig.daysBetweenRequests else {
                return false
            }
        }

        return actionCompletedCount >= ReviewConfig.minActions
            && appLaunchCount >= ReviewConfig.minLaunches
    }

    private func requestReview() async {
        #if os(iOS)
        guard let scene = UIApplication.shared.connectedScenes
            .first(where: { $0.activationState == .foregroundActive }) as? UIWindowScene
        else { return }

        AppStore.requestReview(in: scene)
        #elseif os(macOS)
        // Review request via StoreKit scene API not available on macOS
        #endif

        hasRequestedReview = true
        lastReviewRequestDate = .now
    }
}

// MARK: - Auth Service

/// Authentication Service - uses Amplify SDK directly
actor SWAuthService {
    static let shared = SWAuthService()

    private init() {}

    // MARK: - Email/Password Authentication

    /// Sign up a new user
    func signUp(email: String, password: String) async throws {
        _ = try await Amplify.Auth.signUp(
            username: email,
            password: password,
            options: AuthSignUpRequest.Options(
                userAttributes: [AuthUserAttribute(.email, value: email)]
            )
        )
    }

    /// Confirm email verification code
    func confirmSignUp(email: String, code: String) async throws {
        let result = try await Amplify.Auth.confirmSignUp(
            for: email,
            confirmationCode: code
        )

        guard result.isSignUpComplete else {
            throw SWServiceError.invalidState
        }
    }

    /// Resend verification code
    func resendSignUpCode(email: String) async throws {
        _ = try await Amplify.Auth.resendSignUpCode(for: email)
    }

    /// Sign in with email and password
    func signIn(email: String, password: String) async throws -> SWAuthTokens {
        let result = try await Amplify.Auth.signIn(
            username: email,
            password: password
        )

        guard result.isSignedIn else {
            throw SWServiceError.notSignedIn
        }

        return try await fetchTokens()
    }

    // MARK: - Social Sign In

    /// Apple Sign In
    func signInWithApple(presentationAnchor: AuthUIPresentationAnchor) async throws -> SWAuthTokens {
        swDebugLog("🍎 [SWAuthService] signInWithApple started")

        // If already signed in, sign out first
        if await isSignedIn() {
            swDebugLog("🍎 [SWAuthService] Already signed in, signing out first...")
            await signOut()
        }

        let pluginOptions = AWSAuthWebUISignInOptions(preferPrivateSession: true)
        let options = AuthWebUISignInRequest.Options(pluginOptions: pluginOptions)

        do {
            let result = try await Amplify.Auth.signInWithWebUI(
                for: .apple,
                presentationAnchor: presentationAnchor,
                options: options
            )

            guard result.isSignedIn else {
                throw SWServiceError.notSignedIn
            }

            return try await fetchTokens()
        } catch let error as AuthError {
            swDebugLog("🍎 [SWAuthService] ❌ AuthError:", error.errorDescription)
            throw error
        } catch {
            swDebugLog("🍎 [SWAuthService] ❌ Unknown Error:", String(describing: error))
            throw error
        }
    }

    /// Google Sign In
    func signInWithGoogle(presentationAnchor: AuthUIPresentationAnchor) async throws -> SWAuthTokens {
        // If already signed in, sign out first
        if await isSignedIn() {
            await signOut()
        }

        let pluginOptions = AWSAuthWebUISignInOptions(preferPrivateSession: true)
        let options = AuthWebUISignInRequest.Options(pluginOptions: pluginOptions)

        let result = try await Amplify.Auth.signInWithWebUI(
            for: .google,
            presentationAnchor: presentationAnchor,
            options: options
        )

        guard result.isSignedIn else {
            throw SWServiceError.notSignedIn
        }

        return try await fetchTokens()
    }

    // MARK: - Token Management

    /// Fetch current tokens
    func fetchTokens() async throws -> SWAuthTokens {
        let session = try await Amplify.Auth.fetchAuthSession()

        guard let cognitoSession = session as? AWSAuthCognitoSession else {
            throw SWServiceError.tokenMissing
        }

        let tokensResult = cognitoSession.getCognitoTokens()

        switch tokensResult {
        case .success(let tokens):
            return SWAuthTokens(
                idToken: tokens.idToken,
                accessToken: tokens.accessToken,
                refreshToken: tokens.refreshToken
            )
        case .failure:
            throw SWServiceError.tokenMissing
        }
    }

    /// Refresh tokens
    func refreshSession() async throws -> SWAuthTokens {
        let session = try await Amplify.Auth.fetchAuthSession(options: .forceRefresh())

        guard let cognitoSession = session as? AWSAuthCognitoSession else {
            throw SWServiceError.tokenMissing
        }

        let tokensResult = cognitoSession.getCognitoTokens()

        switch tokensResult {
        case .success(let tokens):
            return SWAuthTokens(
                idToken: tokens.idToken,
                accessToken: tokens.accessToken,
                refreshToken: tokens.refreshToken
            )
        case .failure:
            throw SWServiceError.tokenMissing
        }
    }

    // MARK: - Sign Out / Delete Account

    /// Sign out
    func signOut() async {
        _ = await Amplify.Auth.signOut()
    }

    /// Delete user account
    func deleteUser() async throws {
        try await Amplify.Auth.deleteUser()
    }

    /// Check sign in status
    func isSignedIn() async -> Bool {
        do {
            let session = try await Amplify.Auth.fetchAuthSession()
            return session.isSignedIn
        } catch {
            return false
        }
    }

    // MARK: - Phone Authentication

    /// Send verification code to phone number via custom auth flow
    func sendPhoneVerificationCode(phoneNumber: String) async throws {
        // Sign out any existing session first to start fresh
        if await isSignedIn() {
            await signOut()
        }

        let result = try await Amplify.Auth.signIn(username: phoneNumber)
        // Cognito custom auth flow sends verification code automatically
        guard case .confirmSignInWithCustomChallenge = result.nextStep else {
            if result.isSignedIn {
                return // Already signed in
            }
            throw SWServiceError.invalidState
        }
    }

    /// Confirm phone sign-in with verification code
    func confirmPhoneSignIn(phoneNumber: String, code: String) async throws -> SWAuthTokens {
        let result = try await Amplify.Auth.confirmSignIn(challengeResponse: code)
        guard result.isSignedIn else {
            throw SWServiceError.notSignedIn
        }
        return try await fetchTokens()
    }

    // MARK: - Password Reset

    /// Forgot password - send verification code
    func forgotPassword(email: String) async throws {
        _ = try await Amplify.Auth.resetPassword(for: email)
    }

    /// Reset password - set new password using verification code
    func confirmResetPassword(email: String, newPassword: String, code: String) async throws {
        try await Amplify.Auth.confirmResetPassword(
            for: email,
            with: newPassword,
            confirmationCode: code
        )
    }
}

// MARK: - Window Helper

/// Cross-platform helper to retrieve the key window for auth presentation anchors
private enum SWWindowHelper {
    #if os(iOS)
    static var keyWindow: UIWindow? {
        UIApplication.shared.connectedScenes
            .compactMap { $0 as? UIWindowScene }
            .flatMap { $0.windows }
            .first { $0.isKeyWindow }
    }
    #elseif os(macOS)
    static var keyWindow: NSWindow? {
        NSApplication.shared.keyWindow ?? NSApplication.shared.windows.first
    }
    #endif
}
```

## File: `ShipSwift/SWPackage/SWModule/SWCamera/SWCameraManager+iOS.swift`
```
//
//  SWCameraManager+iOS.swift
//  ShipSwift
//
//  Unified AVCaptureSession manager with photo capture, zoom control,
//  and optional real-time Vision face landmark tracking.
//
//  Base camera features: permission handling, session lifecycle,
//  front/back switching, pinch-to-zoom, and photo capture.
//
//  Face tracking features (opt-in via faceTrackingEnabled):
//  real-time Vision face landmark detection with normalized coordinates,
//  suitable for overlay rendering in SWFaceCameraView.
//
//  Usage:
//    // 1. Create manager (automatically checks camera permission)
//    @State private var cameraManager = SWCameraManager()
//
//    // 2. Wire up error callback for UI alerts
//    cameraManager.onError = { message in
//        SWAlertManager.shared.show(.error, message: message)
//    }
//
//    // 3. Start/stop session (call in onAppear/onDisappear)
//    cameraManager.startSession()
//    cameraManager.stopSession()
//
//    // 4. Capture a photo
//    cameraManager.capturePhoto { image in
//        guard let image else { return }
//        // use captured UIImage
//    }
//
//    // 5. Zoom control
//    cameraManager.setZoom(2.0)               // set absolute zoom
//    cameraManager.zoom(by: 1.5)              // multiply current zoom
//    let current = cameraManager.currentZoom  // read current zoom level
//    // zoom range: cameraManager.minZoom ... cameraManager.maxZoom
//
//    // 6. Check authorization
//    if cameraManager.isAuthorized { /* show camera preview */ }
//
//    // 7. Access the AVCaptureSession for preview
//    SWCameraPreview(session: cameraManager.session)
//
//    // 8. Enable face tracking (for SWFaceCameraView)
//    cameraManager.faceTrackingEnabled = true
//    // Access real-time landmarks:
//    for group in cameraManager.faceLandmarks {
//        // group.region: SWFaceLandmarkRegion
//        // group.points: [CGPoint] in normalized coordinates (0...1)
//    }
//
//    // 9. Initialize with specific camera position
//    @State private var cameraManager = SWCameraManager(position: .front)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import AVFoundation
import Vision

@Observable
final class SWCameraManager: NSObject, @unchecked Sendable {

    // MARK: - Public Properties (Base Camera)

    let session = AVCaptureSession()
    var isAuthorized = false
    var cameraPosition: AVCaptureDevice.Position = .back

    /// Zoom
    var currentZoom: CGFloat = 1.0
    var minZoom: CGFloat = 1.0
    var maxZoom: CGFloat = 5.0

    /// Error callback - wire this up in the view layer
    var onError: ((String) -> Void)?

    // MARK: - Public Properties (Face Tracking, opt-in)

    /// Whether real-time face detection is enabled (default off; SWFaceCameraView turns it on)
    @ObservationIgnored
    nonisolated(unsafe) var faceTrackingEnabled = false

    /// Real-time detected face landmarks (capture device normalized coordinates, top-left origin)
    var faceLandmarks: [SWFaceLandmarkGroup] = []

    // MARK: - Private Properties (Session)

    private let photoOutput = AVCapturePhotoOutput()
    private var captureCompletion: ((UIImage?) -> Void)?
    private var currentDevice: AVCaptureDevice?

    /// Dedicated queue for thread-safe session operations
    private let sessionQueue = DispatchQueue(label: "com.shipswift.camera.session")
    private var isConfigured = false
    private var isConfiguring = false
    private var pendingStartSession = false

    // MARK: - Private Properties (Face Tracking)

    private let videoDataOutput = AVCaptureVideoDataOutput()
    private let videoDataQueue = DispatchQueue(label: "com.shipswift.camera.videodata", qos: .userInitiated)
    @ObservationIgnored
    private nonisolated(unsafe) let sequenceHandler = VNSequenceRequestHandler()
    /// Background-thread-safe copy of camera position (for Vision orientation)
    @ObservationIgnored
    private nonisolated(unsafe) var _bgCameraPosition: AVCaptureDevice.Position = .back

    // MARK: - Initialization

    /// Default initializer (rear camera)
    override init() {
        super.init()
        checkCameraPermission()
    }

    /// Initialize with specific camera position
    init(position: AVCaptureDevice.Position) {
        self.cameraPosition = position
        self._bgCameraPosition = position
        super.init()
        checkCameraPermission()
    }

    // MARK: - Permission Check

    private func checkCameraPermission() {
        switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized:
            DispatchQueue.main.async {
                self.isAuthorized = true
            }
            setupCamera()
        case .notDetermined:
            AVCaptureDevice.requestAccess(for: .video) { granted in
                DispatchQueue.main.async {
                    self.isAuthorized = granted
                    if granted {
                        self.setupCamera()
                    } else {
                        self.onError?(String(localized: "Camera permission denied"))
                    }
                }
            }
        case .denied, .restricted:
            DispatchQueue.main.async {
                self.onError?(String(localized: "Camera permission denied. Please enable in Settings"))
            }
        @unknown default:
            DispatchQueue.main.async {
                self.onError?(String(localized: "Unknown permission status"))
            }
        }
    }

    // MARK: - Camera Configuration

    private func setupCamera() {
        sessionQueue.async { [weak self] in
            guard let self else { return }
            guard !self.isConfigured, !self.isConfiguring else { return }

            self.isConfiguring = true
            self.session.beginConfiguration()

            // Clear existing inputs and outputs
            for input in self.session.inputs {
                self.session.removeInput(input)
            }
            for output in self.session.outputs {
                self.session.removeOutput(output)
            }

            guard let camera = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: self.cameraPosition) else {
                DispatchQueue.main.async {
                    self.onError?(String(localized: "Unable to access camera"))
                }
                self.session.commitConfiguration()
                self.isConfiguring = false
                return
            }

            self.currentDevice = camera

            // Update zoom range
            DispatchQueue.main.async {
                self.minZoom = 1.0
                self.maxZoom = min(camera.activeFormat.videoMaxZoomFactor, 5.0)
                self.currentZoom = 1.0
            }

            do {
                let input = try AVCaptureDeviceInput(device: camera)

                if self.session.canAddInput(input) {
                    self.session.addInput(input)
                } else {
                    DispatchQueue.main.async {
                        self.onError?(String(localized: "Unable to add camera input"))
                    }
                    self.session.commitConfiguration()
                    self.isConfiguring = false
                    return
                }

                self.session.sessionPreset = .photo

                // Photo output
                if self.photoOutput.availablePhotoCodecTypes.contains(AVVideoCodecType.hevc) {
                    self.photoOutput.maxPhotoQualityPrioritization = .balanced
                }

                if self.session.canAddOutput(self.photoOutput) {
                    self.session.addOutput(self.photoOutput)
                } else {
                    DispatchQueue.main.async {
                        self.onError?(String(localized: "Unable to add photo output"))
                    }
                    self.session.commitConfiguration()
                    self.isConfiguring = false
                    return
                }

                // Video data output (for face tracking; always added so tracking can be toggled at runtime)
                self.videoDataOutput.setSampleBufferDelegate(self, queue: self.videoDataQueue)
                self.videoDataOutput.alwaysDiscardsLateVideoFrames = true
                if self.session.canAddOutput(self.videoDataOutput) {
                    self.session.addOutput(self.videoDataOutput)
                }

                // Auto focus / exposure / white balance configuration
                self.configureAutoFocus(camera)

                self.session.commitConfiguration()
                self.isConfigured = true
                self.isConfiguring = false

                // If there's a pending start request, start immediately
                if self.pendingStartSession {
                    self.pendingStartSession = false
                    if !self.session.isRunning {
                        self.session.startRunning()
                    }
                }

            } catch {
                self.session.commitConfiguration()
                self.isConfiguring = false
                DispatchQueue.main.async {
                    self.onError?(String(localized: "Camera setup failed"))
                }
            }
        }
    }

    // MARK: - Session Control

    func startSession() {
        sessionQueue.async { [weak self] in
            guard let self else { return }

            if self.isConfiguring {
                self.pendingStartSession = true
                return
            }

            guard self.isConfigured else {
                self.pendingStartSession = true
                return
            }

            if !self.session.isRunning {
                self.session.startRunning()
            }
        }
    }

    func stopSession() {
        sessionQueue.async { [weak self] in
            guard let self else { return }
            if self.session.isRunning {
                self.session.stopRunning()
            }
        }
    }

    // MARK: - Photo Capture

    func capturePhoto(completion: @escaping (UIImage?) -> Void) {
        self.captureCompletion = completion

        let settings: AVCapturePhotoSettings
        if photoOutput.availablePhotoCodecTypes.contains(AVVideoCodecType.jpeg) {
            settings = AVCapturePhotoSettings(format: [AVVideoCodecKey: AVVideoCodecType.jpeg])
        } else {
            settings = AVCapturePhotoSettings()
        }

        photoOutput.capturePhoto(with: settings, delegate: self)
    }

    // MARK: - Zoom Control

    func setZoom(_ factor: CGFloat) {
        guard let device = currentDevice else { return }

        let zoomFactor = max(minZoom, min(factor, maxZoom))

        do {
            try device.lockForConfiguration()
            device.videoZoomFactor = zoomFactor
            device.unlockForConfiguration()

            DispatchQueue.main.async {
                self.currentZoom = zoomFactor
            }
        } catch {
            // Zoom failed, silently ignore
        }
    }

    func zoom(by delta: CGFloat) {
        setZoom(currentZoom * delta)
    }

    // MARK: - Switch Camera

    func switchCamera() {
        sessionQueue.async { [weak self] in
            guard let self else { return }

            let newPosition: AVCaptureDevice.Position = self.cameraPosition == .front ? .back : .front

            guard let newCamera = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: newPosition) else {
                return
            }

            self.session.beginConfiguration()

            // Remove existing inputs
            for input in self.session.inputs {
                self.session.removeInput(input)
            }

            do {
                let newInput = try AVCaptureDeviceInput(device: newCamera)
                if self.session.canAddInput(newInput) {
                    self.session.addInput(newInput)
                    self.currentDevice = newCamera

                    // Update background-thread-safe camera position (for Vision orientation)
                    self._bgCameraPosition = newPosition

                    // Configure auto focus for the new camera
                    self.configureAutoFocus(newCamera)

                    // Reset zoom
                    self.applyZoom(1.0, to: newCamera)

                    // Update main-thread properties
                    DispatchQueue.main.async {
                        self.cameraPosition = newPosition
                        self.minZoom = 1.0
                        self.maxZoom = min(newCamera.activeFormat.videoMaxZoomFactor, 5.0)
                        self.currentZoom = 1.0
                    }
                }
            } catch {
                // Switch failed, silently ignore
            }

            self.session.commitConfiguration()
        }
    }

    // MARK: - Private Helpers

    private func applyZoom(_ factor: CGFloat, to device: AVCaptureDevice) {
        do {
            try device.lockForConfiguration()
            device.videoZoomFactor = max(1.0, min(factor, device.activeFormat.videoMaxZoomFactor))
            device.unlockForConfiguration()
        } catch {
            // Zoom failed, silently ignore
        }
    }

    /// Configure auto focus, exposure, and white balance for optimal camera performance
    private func configureAutoFocus(_ device: AVCaptureDevice) {
        do {
            try device.lockForConfiguration()

            if device.isFocusModeSupported(.continuousAutoFocus) {
                device.focusMode = .continuousAutoFocus
            } else if device.isFocusModeSupported(.autoFocus) {
                device.focusMode = .autoFocus
            }

            if device.isExposureModeSupported(.continuousAutoExposure) {
                device.exposureMode = .continuousAutoExposure
            }

            if device.isWhiteBalanceModeSupported(.continuousAutoWhiteBalance) {
                device.whiteBalanceMode = .continuousAutoWhiteBalance
            }

            device.unlockForConfiguration()
        } catch {
            // Configuration failed, silently ignore
        }
    }
}

// MARK: - AVCapturePhotoCaptureDelegate

extension SWCameraManager: AVCapturePhotoCaptureDelegate {
    func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: Error?) {
        if error != nil {
            DispatchQueue.main.async {
                self.onError?(String(localized: "Photo capture failed"))
            }
            captureCompletion?(nil)
            return
        }

        guard let imageData = photo.fileDataRepresentation(),
              let image = UIImage(data: imageData) else {
            DispatchQueue.main.async {
                self.onError?(String(localized: "Unable to process photo data"))
            }
            captureCompletion?(nil)
            return
        }

        captureCompletion?(image)
    }
}

// MARK: - Real-time Face Landmark Detection (Vision)

extension SWCameraManager: AVCaptureVideoDataOutputSampleBufferDelegate {
    nonisolated func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        // Skip processing when face tracking is disabled
        guard faceTrackingEnabled else { return }
        guard let pixelBuffer = CMSampleBufferGetImageBuffer(sampleBuffer) else { return }

        // Front camera is mirrored, rear camera is normal
        let orientation: CGImagePropertyOrientation = _bgCameraPosition == .front ? .leftMirrored : .right

        let request = VNDetectFaceLandmarksRequest()
        try? sequenceHandler.perform([request], on: pixelBuffer, orientation: orientation)

        guard let face = request.results?.first,
              let landmarks = face.landmarks else {
            Task { @MainActor in
                self.faceLandmarks = []
            }
            return
        }

        let bbox = face.boundingBox
        var groups: [SWFaceLandmarkGroup] = []

        /// Convert Vision landmark points to capture device normalized coordinates
        func convert(_ region: VNFaceLandmarkRegion2D?, type: SWFaceLandmarkRegion) {
            guard let region else { return }
            let pts = region.normalizedPoints.map { p in
                let x = bbox.origin.x + p.x * bbox.width
                let y = bbox.origin.y + p.y * bbox.height
                return CGPoint(x: x, y: 1.0 - y)
            }
            groups.append(SWFaceLandmarkGroup(region: type, points: pts))
        }

        // Extract all supported face landmarks
        convert(landmarks.faceContour, type: .faceContour)
        convert(landmarks.leftEyebrow, type: .leftEyebrow)
        convert(landmarks.rightEyebrow, type: .rightEyebrow)
        convert(landmarks.leftEye, type: .leftEye)
        convert(landmarks.rightEye, type: .rightEye)
        convert(landmarks.leftPupil, type: .leftPupil)
        convert(landmarks.rightPupil, type: .rightPupil)
        convert(landmarks.nose, type: .nose)
        convert(landmarks.noseCrest, type: .noseCrest)
        convert(landmarks.outerLips, type: .outerLips)
        convert(landmarks.innerLips, type: .innerLips)

        let result = groups
        Task { @MainActor in
            self.faceLandmarks = result
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWCamera/SWCameraView+iOS.swift`
```
//
//  SWCameraView+iOS.swift
//  ShipSwift
//
//  Camera capture view with photo picker and zoom control.
//  Full-screen camera UI with shutter button, photo library picker,
//  pinch-to-zoom gesture, and zoom slider.
//
//  Usage:
//    // 1. Present as a sheet with a @Binding UIImage
//    @State private var capturedImage: UIImage?
//    @State private var showCamera = false
//
//    Button("Take Photo") { showCamera = true }
//    .fullScreenCover(isPresented: $showCamera) {
//        SWCameraView(image: $capturedImage)
//    }
//
//    // 2. The view auto-dismisses after capture or photo selection.
//    //    The captured/selected image is written to the binding.
//
//    // 3. Features included:
//    //    - Live camera preview
//    //    - Shutter button for photo capture
//    //    - PhotosPicker for selecting from photo library
//    //    - Pinch-to-zoom gesture and zoom slider
//    //    - Front/back camera switching
//    //    - Close button (top-left corner)
//    //    - Unauthorized state with "Open Settings" button
//
//    // 4. Errors are shown via SWAlertManager.shared
//    //    Attach .swAlert() in your root view.
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import PhotosUI
import AVFoundation

struct SWCameraView: View {
    @Binding var image: UIImage?
    @Environment(\.dismiss) private var dismiss
    @State private var selectedPhotoItem: PhotosPickerItem?
    @State private var cameraManager = SWCameraManager()
    @State private var isCapturing = false
    @State private var lastScale: CGFloat = 1.0

    var body: some View {
        Group {
            if cameraManager.isAuthorized {
                ZStack {
                    Color.black.ignoresSafeArea()

                    // Camera preview (vertically centered)
                    GeometryReader { geometry in
                        let previewWidth = geometry.size.width
                        let previewHeight = previewWidth * 4 / 3

                        SWCameraPreview(session: cameraManager.session)
                            .frame(width: previewWidth, height: previewHeight)
                            .clipped()
                            .overlay(alignment: .bottom) {
                                zoomControl
                            }
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                    }
                    .gesture(pinchGesture)
                    .onAppear {
                        cameraManager.onError = { SWAlertManager.shared.show(.error, message: $0) }
                        cameraManager.startSession()
                    }
                    .onDisappear { cameraManager.stopSession() }

                    // Bottom control bar
                    VStack {
                        Spacer()
                        controlBar
                    }

                }
            } else {
                unauthorizedView
            }
        }
        .background(.black)
        .onChange(of: selectedPhotoItem) {
            Task {
                await loadSelectedPhoto()
            }
        }
    }

    // MARK: - Pinch-to-Zoom Gesture

    private var pinchGesture: some Gesture {
        MagnifyGesture()
            .onChanged { value in
                let delta = value.magnification / lastScale
                lastScale = value.magnification
                cameraManager.zoom(by: delta)
            }
            .onEnded { _ in
                lastScale = 1.0
            }
    }

    // MARK: - Unauthorized View

    private var unauthorizedView: some View {
        VStack(spacing: 20) {
            Label("Camera permission required", systemImage: "camera.fill")
                .foregroundStyle(.regularMaterial)

            Button("Open Settings") {
                if let url = URL(string: UIApplication.openSettingsURLString) {
                    UIApplication.shared.open(url)
                }
            }
            .buttonStyle(.borderedProminent)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - Zoom Control

    private var zoomControl: some View {
        VStack(spacing: 8) {
            // Current zoom level
            Text(String(format: "%.1fx", cameraManager.currentZoom))
                .font(.system(size: 14, weight: .medium, design: .monospaced))

            // Zoom slider
            HStack(spacing: 12) {
                Text("1x")
                    .font(.caption)

                Slider(
                    value: Binding(
                        get: { cameraManager.currentZoom },
                        set: { cameraManager.setZoom($0) }
                    ),
                    in: cameraManager.minZoom...cameraManager.maxZoom
                )
                .tint(.accent)

                Text(String(format: "%.0fx", cameraManager.maxZoom))
                    .font(.caption)
            }
            .padding(.horizontal, 60)
        }
        .foregroundStyle(.white.opacity(0.7))
        .padding()
    }

    // MARK: - Bottom Control Bar

    private var controlBar: some View {
        HStack(spacing: 50) {
            // Photo library picker
            PhotosPicker(selection: $selectedPhotoItem, matching: .images) {
                controlButton(icon: "photo.on.rectangle")
            }

            // Capture button
            Button {
                capturePhoto()
            } label: {
                shutterButton
            }
            .disabled(!cameraManager.isAuthorized || isCapturing)

            // Switch camera
            Button { cameraManager.switchCamera() } label: {
                controlButton(icon: "camera.rotate.fill")
            }
        }
        .padding(.bottom, 50)
        .padding(.top, 20)
    }

    // MARK: - Control Button Style

    private func controlButton(icon: String) -> some View {
        Image(systemName: icon)
            .font(.title2)
            .foregroundStyle(.white)
            .frame(width: 50, height: 50)
            .background(.black.opacity(0.6), in: RoundedRectangle(cornerRadius: 12))
    }

    // MARK: - Shutter Button

    private var shutterButton: some View {
        Circle()
            .fill(cameraManager.isAuthorized && !isCapturing ? .white : .gray)
            .frame(width: 70, height: 70)
            .overlay {
                Circle()
                    .strokeBorder(.black.opacity(0.2), lineWidth: 2)
                    .frame(width: 60, height: 60)
            }
            .scaleEffect(isCapturing ? 0.9 : 1.0)
            .animation(.easeInOut(duration: 0.1), value: isCapturing)
    }

    // MARK: - Actions

    private func capturePhoto() {
        guard cameraManager.isAuthorized, !isCapturing else { return }

        isCapturing = true
        cameraManager.capturePhoto { photo in
            isCapturing = false
            if let photo {
                image = photo
                dismiss()
            }
        }
    }

    private func loadSelectedPhoto() async {
        guard let item = selectedPhotoItem,
              let data = try? await item.loadTransferable(type: Data.self),
              let selectedImage = UIImage(data: data) else { return }

        image = selectedImage
        dismiss()
    }
}

// MARK: - Camera Preview

struct SWCameraPreview: UIViewRepresentable {
    let session: AVCaptureSession

    func makeUIView(context: Context) -> SWPreviewView {
        let view = SWPreviewView()
        view.session = session
        return view
    }

    func updateUIView(_ uiView: SWPreviewView, context: Context) {
        if uiView.session != session {
            uiView.session = session
        }
    }
}

class SWPreviewView: UIView {
    var session: AVCaptureSession? {
        didSet {
            guard let session = session else { return }
            videoPreviewLayer.session = session
        }
    }

    override class var layerClass: AnyClass {
        return AVCaptureVideoPreviewLayer.self
    }

    var videoPreviewLayer: AVCaptureVideoPreviewLayer {
        return layer as! AVCaptureVideoPreviewLayer
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        videoPreviewLayer.frame = bounds
        videoPreviewLayer.videoGravity = .resizeAspectFill
    }
}

// MARK: - Preview

#Preview("Unauthorized") {
    SWCameraView(image: .constant(nil))
        .swAlert()
        .onAppear {
            SWAlertManager.shared.show(.error, message: "Camera permission denied")
        }
}

```

## File: `ShipSwift/SWPackage/SWModule/SWCamera/SWFaceCameraView+iOS.swift`
```
//
//  SWFaceCameraView+iOS.swift
//  ShipSwift
//
//  Face camera view with real-time landmark overlay.
//  Full camera UI with face landmark visualization, photo capture,
//  camera switching, and landmark display toggle.
//
//  Usage:
//    // 1. Basic usage with onCapture callback
//    SWFaceCameraView { capturedImage in
//        // handle the captured UIImage
//        processPhoto(capturedImage)
//    }
//
//    // 2. Custom landmark color scheme
//    SWFaceCameraView(
//        onCapture: { image in handlePhoto(image) },
//        landmarkColors: .mono   // tech-feel cyan monochrome
//    )
//
//    // 3. Available color schemes
//    //    .default — multi-color (cyan lips, green eyes, purple brows, yellow nose)
//    //    .mono    — all cyan with varying opacity (tech feel)
//    //    .warm    — pink lips, orange eyes, red brows, yellow nose
//
//    // 4. Custom color scheme
//    let colors = SWFaceLandmarkColors(
//        lips: .pink.opacity(0.6),
//        eyes: .green.opacity(0.6),
//        eyebrows: .purple.opacity(0.6),
//        nose: .yellow.opacity(0.6),
//        faceContour: .white.opacity(0.2)
//    )
//    SWFaceCameraView(onCapture: { _ in }, landmarkColors: colors)
//
//    // 5. Controls provided:
//    //    - Camera switch button (front/back)
//    //    - Shutter button for photo capture
//    //    - Landmark overlay toggle button
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import AVFoundation

// MARK: - Face Recognition Camera View

struct SWFaceCameraView: View {
    /// Photo capture callback
    var onCapture: ((UIImage) -> Void)?

    /// Landmark color scheme
    var landmarkColors: SWFaceLandmarkColors = .default

    @State private var cameraManager = SWCameraManager(position: .front)
    @State private var isCapturing = false
    @State private var showLandmarks = true

    var body: some View {
        Group {
            if cameraManager.isAuthorized {
                ZStack {
                    Color.black.ignoresSafeArea()

                    // Camera preview (vertically centered)
                    GeometryReader { geometry in
                        let previewWidth = geometry.size.width
                        let previewHeight = previewWidth * 4 / 3

                        SWFaceCameraPreview(session: cameraManager.session)
                            .frame(width: previewWidth, height: previewHeight)
                            .clipped()
                            .overlay {
                                if showLandmarks {
                                    SWFaceTrackingOverlay(
                                        landmarks: cameraManager.faceLandmarks,
                                        colors: landmarkColors
                                    )
                                }
                            }
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                    }
                    .onAppear {
                        cameraManager.faceTrackingEnabled = true
                        cameraManager.startSession()
                    }
                    .onDisappear {
                        cameraManager.faceTrackingEnabled = false
                        cameraManager.stopSession()
                    }

                    // Bottom control bar
                    VStack {
                        Spacer()
                        controlBar
                    }

                }
            } else {
                unauthorizedView
            }
        }
        .background(.black)
    }

    // MARK: - Unauthorized View

    private var unauthorizedView: some View {
        VStack(spacing: 20) {
            Label("Camera permission required", systemImage: "camera.fill")
                .foregroundStyle(.regularMaterial)

            Button("Open Settings") {
                if let url = URL(string: UIApplication.openSettingsURLString) {
                    UIApplication.shared.open(url)
                }
            }
            .buttonStyle(.borderedProminent)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }

    // MARK: - Bottom Control Bar

    private var controlBar: some View {
        VStack {
            HStack(spacing: 50) {
                // Switch camera
                Button {
                    cameraManager.switchCamera()
                } label: {
                    controlButton(icon: "camera.rotate.fill")
                }

                // Shutter button (same style as SWCameraView)
                Button {
                    capturePhoto()
                } label: {
                    shutterButton
                }
                .disabled(!cameraManager.isAuthorized || isCapturing)

                // Face landmark toggle
                Button {
                    showLandmarks.toggle()
                } label: {
                    controlButton(icon: showLandmarks ? "face.dashed.fill" : "face.dashed")
                }
            }
        }
        .padding(.bottom, 50)
        .padding(.top, 20)
    }

    // MARK: - Control Button Style

    private func controlButton(icon: String) -> some View {
        Image(systemName: icon)
            .font(.title2)
            .foregroundStyle(.white)
            .frame(width: 50, height: 50)
            .background(.black.opacity(0.6), in: RoundedRectangle(cornerRadius: 12))
    }

    // MARK: - Shutter Button

    private var shutterButton: some View {
        Circle()
            .fill(cameraManager.isAuthorized && !isCapturing ? .white : .gray)
            .frame(width: 70, height: 70)
            .overlay {
                Circle()
                    .strokeBorder(.black.opacity(0.2), lineWidth: 2)
                    .frame(width: 60, height: 60)
            }
            .scaleEffect(isCapturing ? 0.9 : 1.0)
            .animation(.easeInOut(duration: 0.1), value: isCapturing)
    }

    // MARK: - Photo Capture

    private func capturePhoto() {
        guard cameraManager.isAuthorized, !isCapturing else { return }

        isCapturing = true
        cameraManager.capturePhoto { photo in
            isCapturing = false
            if let photo {
                onCapture?(photo)
            }
        }
    }
}

// MARK: - Camera Preview

struct SWFaceCameraPreview: UIViewRepresentable {
    let session: AVCaptureSession

    func makeUIView(context: Context) -> SWFacePreviewView {
        let view = SWFacePreviewView()
        view.session = session
        return view
    }

    func updateUIView(_ uiView: SWFacePreviewView, context: Context) {
        if uiView.session != session {
            uiView.session = session
        }
    }
}

final class SWFacePreviewView: UIView {
    var session: AVCaptureSession? {
        didSet {
            guard let session = session else { return }
            videoPreviewLayer.session = session
        }
    }

    override class var layerClass: AnyClass {
        return AVCaptureVideoPreviewLayer.self
    }

    var videoPreviewLayer: AVCaptureVideoPreviewLayer {
        return layer as! AVCaptureVideoPreviewLayer
    }

    override func layoutSubviews() {
        super.layoutSubviews()
        videoPreviewLayer.frame = bounds
        videoPreviewLayer.videoGravity = .resizeAspectFill
    }
}

// MARK: - Face Landmark Real-time Rendering

struct SWFaceTrackingOverlay: View {
    let landmarks: [SWFaceLandmarkGroup]
    var colors: SWFaceLandmarkColors = .default

    var body: some View {
        Canvas { context, size in
            for group in landmarks {
                guard !group.points.isEmpty else { continue }

                let color = colors.color(for: group.region)
                let mapped = group.points.map {
                    CGPoint(x: $0.x * size.width, y: $0.y * size.height)
                }

                // Pupils and other few-point regions only draw dots, not paths
                if group.isClosed {
                    var path = Path()
                    path.addLines(mapped)
                    path.closeSubpath()

                    // Lip regions have semi-transparent fill
                    if group.region == .outerLips || group.region == .innerLips {
                        context.fill(path, with: .color(color.opacity(0.08)))
                    }
                    context.stroke(path, with: .color(color.opacity(0.8)), lineWidth: 1.5)
                }

                // Each point
                let dotSize: CGFloat = group.region == .leftPupil || group.region == .rightPupil ? 5 : 3
                for point in mapped {
                    let rect = CGRect(x: point.x - dotSize / 2, y: point.y - dotSize / 2,
                                      width: dotSize, height: dotSize)
                    context.fill(Circle().path(in: rect), with: .color(color))
                }
            }
        }
        .allowsHitTesting(false)
    }
}

// MARK: - Landmark Color Scheme

struct SWFaceLandmarkColors {
    var lips: Color
    var eyes: Color
    var eyebrows: Color
    var nose: Color
    var faceContour: Color

    func color(for region: SWFaceLandmarkRegion) -> Color {
        switch region {
        case .outerLips, .innerLips:         return lips
        case .leftEye, .rightEye:            return eyes
        case .leftPupil, .rightPupil:        return eyes
        case .leftEyebrow, .rightEyebrow:    return eyebrows
        case .nose, .noseCrest:              return nose
        case .faceContour:                   return faceContour
        }
    }

    /// Default color scheme
    static let `default` = SWFaceLandmarkColors(
        lips: .cyan.opacity(0.6),
        eyes: .green.opacity(0.6),
        eyebrows: .purple.opacity(0.6),
        nose: .yellow.opacity(0.6),
        faceContour: .white.opacity(0.2)
    )

    /// Monochrome scheme (tech feel)
    static let mono = SWFaceLandmarkColors(
        lips: .cyan.opacity(0.7),
        eyes: .cyan.opacity(0.5),
        eyebrows: .cyan.opacity(0.4),
        nose: .cyan.opacity(0.5),
        faceContour: .cyan.opacity(0.15)
    )

    /// Warm color scheme
    static let warm = SWFaceLandmarkColors(
        lips: .pink.opacity(0.6),
        eyes: .orange.opacity(0.6),
        eyebrows: .red.opacity(0.5),
        nose: .yellow.opacity(0.6),
        faceContour: .white.opacity(0.15)
    )
}

// MARK: - Preview

#Preview {
    SWFaceCameraView()
}

```

## File: `ShipSwift/SWPackage/SWModule/SWCamera/SWFaceLandmark+iOS.swift`
```
//
//  SWFaceLandmark+iOS.swift
//  ShipSwift
//
//  Face landmark data models for Vision framework regions.
//  Defines the enum of face landmark region types and a group model
//  that holds normalized coordinate points for each detected region.
//
//  Usage:
//    // 1. SWFaceLandmarkRegion enum cases:
//    //    .faceContour, .leftEye, .rightEye,
//    //    .leftEyebrow, .rightEyebrow,
//    //    .nose, .noseCrest,
//    //    .outerLips, .innerLips,
//    //    .leftPupil, .rightPupil
//
//    // 2. SWFaceLandmarkGroup model
//    let group = SWFaceLandmarkGroup(
//        region: .leftEye,
//        points: [CGPoint(x: 0.3, y: 0.4), CGPoint(x: 0.35, y: 0.42), ...]
//    )
//    group.region    // .leftEye
//    group.points    // [CGPoint] in normalized coordinates (0...1)
//    group.isClosed  // true if points.count > 2 (pupils are not closed)
//
//    // 3. Typically consumed from SWCameraManager.faceLandmarks
//    for group in cameraManager.faceLandmarks {
//        switch group.region {
//        case .outerLips: drawLips(group.points)
//        case .leftEye:   drawEye(group.points)
//        default: break
//        }
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation

/// Face landmark region type
enum SWFaceLandmarkRegion: String, Sendable {
    case faceContour
    case leftEye, rightEye
    case leftEyebrow, rightEyebrow
    case nose, noseCrest
    case outerLips, innerLips
    case leftPupil, rightPupil
}

/// Single face landmark group
struct SWFaceLandmarkGroup: Sendable {
    let region: SWFaceLandmarkRegion
    let points: [CGPoint]
    /// Whether the path is closed (single-point regions like pupils are not closed)
    var isClosed: Bool { points.count > 2 }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWChat/SWChatInputView+iOS.swift`
```
//
//  SWChatInputView+iOS.swift
//  ShipSwift
//
//  Chat text input bar with optional voice recognition (ASR).
//  Provides a text field, optional microphone button for speech-to-text,
//  audio waveform animation during recording, and a send button.
//
//  When asrConfig is nil the microphone button is hidden and the view
//  works as a pure text input bar.
//
//  Usage:
//    // 1. Text-only input (no voice)
//    @State private var text = ""
//
//    SWChatInputView(text: $text) {
//        sendMessage(text)
//        text = ""
//    }
//
//    // 2. With voice input — provide an ASR config
//    let asrConfig = SWASRConfig(
//        appId: "YourVolcEngineAppID",
//        accessToken: "YourAccessToken"
//    )
//
//    SWChatInputView(text: $text, asrConfig: asrConfig) {
//        sendMessage(text)
//        text = ""
//    }
//
//    // 3. Full chat interface with SWMessageList
//    VStack(spacing: 0) {
//        SWMessageList(messages: messages) { message in
//            SWMessageBubble(isFromUser: message.isUser) {
//                Text(message.content)
//            }
//        }
//        SWChatInputView(text: $text, asrConfig: asrConfig) {
//            sendMessage(text)
//            text = ""
//        }
//    }
//
//    // 4. Customization options
//    SWChatInputView(
//        text: $text,
//        asrConfig: asrConfig,
//        isDisabled: isLoading,                    // disable during AI response
//        placeHolderText: "Ask anything...",        // custom placeholder
//        minLines: 2                                // minimum text field height
//    ) {
//        onSend()
//    }
//
//    // 5. Voice flow: tap mic -> recording + waveform -> tap stop ->
//    //    transcribing -> text appears in field -> tap send
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - Chat Input View

/// Chat input view with optional voice recognition.
///
/// Features:
/// - Text input field
/// - Microphone button for speech-to-text (hidden when `asrConfig` is nil)
/// - Audio waveform animation while recording
/// - Loading state during transcription
/// - Send button
///
/// Text-only usage (no voice):
/// ```swift
/// SWChatInputView(text: $text) {
///     sendMessage()
/// }
/// ```
///
/// With voice input:
/// ```swift
/// SWChatInputView(text: $text, asrConfig: asrConfig) {
///     sendMessage()
/// }
/// ```
public struct SWChatInputView: View {
    @Binding public var text: String
    public var onSend: () -> Void
    public var isDisabled: Bool
    public var placeHolderText: LocalizedStringKey
    public var minLines: Int
    public let asrConfig: SWASRConfig?

    @FocusState private var isFocused: Bool
    @State private var asrState: SWASRState = .idle
    @State private var asrService: SWVolcEngineASRService?

    public init(
        text: Binding<String>,
        asrConfig: SWASRConfig? = nil,
        isDisabled: Bool = false,
        placeHolderText: LocalizedStringKey = "Type a message...",
        minLines: Int = 1,
        onSend: @escaping () -> Void
    ) {
        self._text = text
        self.asrConfig = asrConfig
        self.isDisabled = isDisabled
        self.placeHolderText = placeHolderText
        self.minLines = minLines
        self.onSend = onSend
    }

    /// Whether the input field has valid text
    private var hasText: Bool {
        !text.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }

    /// Whether ASR is active (recording or transcribing)
    private var isASRActive: Bool {
        asrState == .recording || asrState == .transcribing
    }

    public var body: some View {
        VStack(spacing: 8) {
            // Input area
            inputArea

            // Voice / send buttons
            HStack(spacing: 16) {
                Spacer()

                // Microphone / stop button
                microphoneButton

                // Send button
                sendButton
            }
            .padding(.bottom, -2)
            .padding(.trailing, -2)
        }
        .padding(10)
        .contentShape(Rectangle()) // Make the entire area tappable
        .onTapGesture {
            if !isDisabled && asrState == .idle {
                isFocused = true
            }
        }
        .overlay(
            RoundedRectangle(cornerRadius: 16)
                .stroke(.accent, lineWidth: 1)
        )
        .padding(.horizontal)
        .padding(.vertical, 8)
    }

    // MARK: - Input Area

    @ViewBuilder
    private var inputArea: some View {
        switch asrState {
        case .idle:
            // Normal text input
            TextField(placeHolderText, text: $text, axis: .vertical)
                .textFieldStyle(.plain)
                .lineLimit(minLines...5)
                .focused($isFocused)
                .disabled(isDisabled)
                .onChange(of: isDisabled) { oldValue, newValue in
                    // When recovering from disabled state, keep the input unfocused to avoid keyboard auto-popup
                    if oldValue && !newValue {
                        isFocused = false
                    }
                }

        case .recording:
            // Show waveform while recording
            SWAudioWaveformView()

        case .transcribing:
            // Show loading during transcription
            HStack {
                ProgressView()
                    .scaleEffect(0.8)
                Text("Transcribing...")
                    .foregroundStyle(.secondary)
                    .font(.subheadline)
                Spacer()
            }
            .frame(minHeight: 24)
        }
    }

    // MARK: - Microphone Button

    @ViewBuilder
    private var microphoneButton: some View {
        if asrConfig != nil {
            switch asrState {
            case .idle:
                // Only show microphone when there is no text
                if !hasText {
                    Button {
                        startRecording()
                    } label: {
                        Image(systemName: "microphone")
                            .imageScale(.large)
                            .foregroundStyle(.blue, .secondary)
                    }
                }

            case .recording:
                // Show stop button while recording
                Button {
                    stopRecording()
                } label: {
                    Image(systemName: "stop.circle.fill")
                        .font(.system(size: 30))
                        .foregroundColor(.red)
                }

            case .transcribing:
                // Show grayed-out microphone during transcription
                Image(systemName: "microphone")
                    .imageScale(.large)
                    .foregroundStyle(.gray)
            }
        }
    }

    // MARK: - Send Button

    @ViewBuilder
    private var sendButton: some View {
        Button {
            guard hasText else { return }
            // Dismiss focus first to avoid keyboard popup
            isFocused = false
            onSend()
        } label: {
            Image(systemName: "arrow.up.circle.fill")
                .font(.system(size: 30))
                .foregroundColor(hasText && !isDisabled && !isASRActive ? .blue : .gray)
        }
        .disabled(!hasText || isDisabled || isASRActive)
    }

    // MARK: - ASR Actions

    private func startRecording() {
        guard let asrConfig else { return }

        text = "" // Clear previous text
        asrState = .recording

        let service = SWVolcEngineASRService(config: asrConfig)
        asrService = service

        // Set callbacks
        service.onTranscriptionUpdate = { transcribedText in
            self.text = transcribedText
        }

        service.onTranscriptionComplete = { finalText in
            self.text = finalText
            self.asrState = .idle
        }

        service.onError = { error in
            swDebugLog("[SWChatInput] ASR error: \(error.localizedDescription)")
            self.asrState = .idle
        }

        // Start recording
        Task {
            do {
                try await service.startRecording()
            } catch {
                swDebugLog("[SWChatInput] Failed to start recording: \(error.localizedDescription)")
                asrState = .idle
            }
        }
    }

    private func stopRecording() {
        asrState = .transcribing

        Task {
            await asrService?.stopRecording()
        }
    }
}

// MARK: - ASR State

/// ASR recording state
fileprivate enum SWASRState: Equatable {
    case idle           // Idle state
    case recording      // Recording
    case transcribing   // Transcribing
}

// MARK: - Audio Waveform View

/// Audio waveform animation view - automatically fills the entire width
fileprivate struct SWAudioWaveformView: View {
    var barWidth: CGFloat = 3
    var spacing: CGFloat = 4
    var minHeight: CGFloat = 4
    var maxHeight: CGFloat = 24
    var color: Color = .accentColor

    @State private var phases: [Double] = []
    @State private var timer: Timer?

    var body: some View {
        GeometryReader { geometry in
            let barCount = Int(geometry.size.width / (barWidth + spacing))
            HStack(spacing: spacing) {
                ForEach(0..<barCount, id: \.self) { index in
                    Capsule()
                        .fill(color)
                        .frame(width: barWidth, height: barHeight(for: index, total: barCount))
                }
            }
            .frame(maxWidth: .infinity)
            .onAppear {
                phases = (0..<barCount).map { Double($0) }
                startAnimation(barCount: barCount)
            }
            .onDisappear {
                timer?.invalidate()
                timer = nil
            }
        }
        .frame(height: maxHeight)
    }

    private func barHeight(for index: Int, total: Int) -> CGFloat {
        guard phases.indices.contains(index) else { return minHeight }
        let phase = phases[index]
        let normalizedHeight = (sin(phase) + 1) / 2 // 0 to 1
        return minHeight + (maxHeight - minHeight) * normalizedHeight
    }

    private func startAnimation(barCount: Int) {
        timer = Timer.scheduledTimer(withTimeInterval: 0.05, repeats: true) { _ in
            withAnimation(.linear(duration: 0.05)) {
                for i in 0..<barCount {
                    if phases.indices.contains(i) {
                        // Each bar has a different phase offset to create a wave effect
                        phases[i] += 0.15 + Double(i % 3) * 0.05
                    }
                }
            }
        }
    }
}

// MARK: - Previews

#Preview("Text Only (No ASR)") {
    SWChatInputView(
        text: .constant("")
    ) {}
}

#Preview("With ASR - Empty") {
    SWChatInputView(
        text: .constant(""),
        asrConfig: SWASRConfig(appId: "test", accessToken: "test")
    ) {}
}

#Preview("With ASR - With Text") {
    SWChatInputView(
        text: .constant("Hello"),
        asrConfig: SWASRConfig(appId: "test", accessToken: "test")
    ) {}
}

#Preview("Interactive") {
    SWChatInputPreview()
}

private struct SWChatInputPreview: View {
    @State private var text = ""

    var body: some View {
        VStack {
            Spacer()
            SWChatInputView(text: $text) {
                swDebugLog("Send: \(text)")
                text = ""
            }
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWChat/SWChatView+iOS.swift`
```
//
//  SWChatView+iOS.swift
//  ShipSwift
//
//  All-in-one chat view that combines SWMessageList, SWMessageBubble,
//  and SWChatInputView into a single, ready-to-use component.
//  Manages input state internally and appends user messages automatically.
//
//  Usage:
//    // 1. Minimal setup — just provide messages and an onSend callback
//    @State private var messages: [SWChatMessage] = []
//
//    SWChatView(messages: $messages) { text in
//        // Called after the user message is already appended.
//        // Use this to send the text to your AI backend and append the response.
//        Task {
//            let reply = await myAI.send(text)
//            messages.append(SWChatMessage(content: reply, isUser: false))
//        }
//    }
//
//    // 2. Enable voice input by providing an ASR config
//    let asrConfig = SWASRConfig(appId: "YourAppID", accessToken: "YourToken")
//
//    SWChatView(messages: $messages, asrConfig: asrConfig) { text in
//        // ...
//    }
//
//    // 3. Disable input while waiting for AI response
//    @State private var isWaiting = false
//
//    SWChatView(
//        messages: $messages,
//        asrConfig: asrConfig,
//        isDisabled: isWaiting,
//        placeholderText: "Ask anything..."
//    ) { text in
//        isWaiting = true
//        Task {
//            let reply = await myAI.send(text)
//            messages.append(SWChatMessage(content: reply, isUser: false))
//            isWaiting = false
//        }
//    }
//
//    // 4. Custom bubble styling via the optional bubbleContent parameter
//    SWChatView(
//        messages: $messages,
//        asrConfig: asrConfig,
//        onSend: { _ in }
//    ) { message in
//        // Return any View to replace the default bubble
//        Text(message.content)
//            .padding(12)
//            .background(.green)
//            .clipShape(Capsule())
//    }
//
//  Created by Wei Zhong on 2/14/26.
//

import SwiftUI

private let swChatBubbleBackground = Color(UIColor.systemGray6)

// MARK: - Chat Message Model

/// A single chat message.
///
/// Conforms to `Identifiable` so it works with `ForEach` / `SWMessageList`.
/// Create user messages with `isUser: true` and AI/system messages with `isUser: false`.
public struct SWChatMessage: Identifiable {
    public let id: UUID
    public let content: String
    public let isUser: Bool
    public let timestamp: Date

    public init(
        id: UUID = UUID(),
        content: String,
        isUser: Bool,
        timestamp: Date = Date()
    ) {
        self.id = id
        self.content = content
        self.isUser = isUser
        self.timestamp = timestamp
    }
}

// MARK: - Chat View

/// All-in-one chat view.
///
/// Integrates `SWMessageList`, `SWMessageBubble`, and `SWChatInputView`
/// into a single component. The view:
/// - Maintains input text state internally
/// - Appends user messages to the binding automatically on send
/// - Displays messages using `SWMessageList` with throttled auto-scroll
/// - Provides default bubble styling (accent for user, gray for AI)
/// - Optionally supports ASR voice input when `asrConfig` is provided
///
/// Minimal usage (text only, no voice):
/// ```swift
/// @State private var messages: [SWChatMessage] = []
///
/// SWChatView(messages: $messages) { text in
///     // Handle AI response
/// }
/// ```
///
/// With voice input:
/// ```swift
/// SWChatView(
///     messages: $messages,
///     asrConfig: SWASRConfig(appId: "id", accessToken: "token")
/// ) { text in
///     // Handle AI response
/// }
/// ```
public struct SWChatView<BubbleContent: View>: View {
    @Binding public var messages: [SWChatMessage]
    public let asrConfig: SWASRConfig?
    public let isDisabled: Bool
    public let placeholderText: LocalizedStringKey
    public let onSend: (String) -> Void
    public let bubbleContent: ((SWChatMessage) -> BubbleContent)?

    @State private var inputText = ""

    /// Initialize with default bubble styling.
    /// - Parameters:
    ///   - messages: Binding to the message array (chronological order, oldest first)
    ///   - asrConfig: ASR configuration for voice input. Pass nil to hide the microphone button.
    ///   - isDisabled: Disable input (e.g. while waiting for AI response)
    ///   - placeholderText: Placeholder text for the input field
    ///   - onSend: Callback fired after the user message is appended.
    ///             Receives the sent text so you can forward it to your backend.
    public init(
        messages: Binding<[SWChatMessage]>,
        asrConfig: SWASRConfig? = nil,
        isDisabled: Bool = false,
        placeholderText: LocalizedStringKey = "Type a message...",
        onSend: @escaping (String) -> Void
    ) where BubbleContent == EmptyView {
        self._messages = messages
        self.asrConfig = asrConfig
        self.isDisabled = isDisabled
        self.placeholderText = placeholderText
        self.onSend = onSend
        self.bubbleContent = nil
    }

    /// Initialize with custom bubble content.
    /// - Parameters:
    ///   - messages: Binding to the message array (chronological order, oldest first)
    ///   - asrConfig: ASR configuration for voice input. Pass nil to hide the microphone button.
    ///   - isDisabled: Disable input (e.g. while waiting for AI response)
    ///   - placeholderText: Placeholder text for the input field
    ///   - onSend: Callback fired after the user message is appended
    ///   - bubbleContent: Custom view builder for each message bubble
    public init(
        messages: Binding<[SWChatMessage]>,
        asrConfig: SWASRConfig? = nil,
        isDisabled: Bool = false,
        placeholderText: LocalizedStringKey = "Type a message...",
        onSend: @escaping (String) -> Void,
        @ViewBuilder bubbleContent: @escaping (SWChatMessage) -> BubbleContent
    ) {
        self._messages = messages
        self.asrConfig = asrConfig
        self.isDisabled = isDisabled
        self.placeholderText = placeholderText
        self.onSend = onSend
        self.bubbleContent = bubbleContent
    }

    public var body: some View {
        VStack(spacing: 0) {
            // Message list
            SWMessageList(messages: messages) { message in
                SWMessageBubble(isFromUser: message.isUser) {
                    if let bubbleContent {
                        bubbleContent(message)
                    } else {
                        defaultBubble(for: message)
                    }
                }
            }

            // Input bar
            SWChatInputView(
                text: $inputText,
                asrConfig: asrConfig,
                isDisabled: isDisabled,
                placeHolderText: placeholderText
            ) {
                send()
            }
        }
    }

    // MARK: - Default Bubble

    /// Default bubble styling: accent background for user, gray for AI.
    @ViewBuilder
    private func defaultBubble(for message: SWChatMessage) -> some View {
        Text(message.content)
            .padding(12)
            .background(message.isUser ? Color.accentColor : swChatBubbleBackground)
            .foregroundStyle(message.isUser ? .white : .primary)
            .clipShape(RoundedRectangle(cornerRadius: 16))
    }

    // MARK: - Send Action

    private func send() {
        let text = inputText.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty else { return }

        // Append user message
        let userMessage = SWChatMessage(content: text, isUser: true)
        messages.append(userMessage)

        // Clear input
        inputText = ""

        // Notify caller
        onSend(text)
    }
}

// MARK: - Previews

#Preview("Chat View") {
    SWChatPreview()
}

private struct SWChatPreview: View {
    @State private var messages: [SWChatMessage] = [
        SWChatMessage(content: "Hello!", isUser: true),
        SWChatMessage(content: "Hi there! How can I help you today?", isUser: false),
        SWChatMessage(content: "Show me how SWChatView works.", isUser: true),
        SWChatMessage(
            content: "SWChatView combines SWMessageList, SWMessageBubble, and SWChatInputView into one component. Just provide a messages binding, ASR config, and an onSend callback.",
            isUser: false
        ),
    ]

    var body: some View {
        SWChatView(messages: $messages) { text in
            // Simulate AI response
            Task {
                try? await Task.sleep(for: .seconds(1))
                messages.append(
                    SWChatMessage(
                        content: "This is a demo response. Connect ShipSwift MCP to enable full AI chat functionality.",
                        isUser: false
                    )
                )
            }
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWChat/SWMessageList+iOS.swift`
```
//
//  SWMessageList+iOS.swift
//  ShipSwift
//
//  Scrollable chat message list with bubble styling.
//  Uses List + ScrollViewReader with throttled auto-scroll to keep
//  the latest message visible. Avoids ScrollView + LazyVStack which
//  causes 100% CPU from infinite layout loops during streaming updates.
//
//  Advantages over the old flip technique:
//  - Text is selectable (no coordinate system inversion)
//  - Smooth, throttled scrolling during streaming (no jank)
//  - Standard coordinate system — no mental overhead for consumers
//
//  Usage:
//    // 1. Basic message list (messages in chronological order, oldest first)
//    SWMessageList(messages: messages) { message in
//        SWMessageBubble(isFromUser: message.isUser) {
//            Text(message.content)
//                .padding(12)
//                .background(message.isUser ? Color.accentColor : Color(.systemGray6))
//                .foregroundStyle(message.isUser ? .white : .primary)
//                .clipShape(RoundedRectangle(cornerRadius: 16))
//        }
//    }
//
//    // 2. Message model must conform to Identifiable
//    struct ChatMessage: Identifiable {
//        let id = UUID()
//        let content: String
//        let isUser: Bool
//    }
//
//    // 3. SWMessageBubble aligns user messages to trailing, others to leading
//    SWMessageBubble(isFromUser: true) {
//        Text("Hello!")  // right-aligned bubble
//    }
//    SWMessageBubble(isFromUser: false) {
//        Text("Hi!")     // left-aligned bubble
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

private let swMessageBubbleBackground = Color(UIColor.systemGray6)

// MARK: - Message List View

/// Scrollable chat message list with automatic bottom-anchoring.
///
/// ## Best Practices
///
/// ### 1. Use List instead of ScrollView + LazyVStack
/// LazyVStack causes infinite layout calculation loops during frequent updates, CPU 100%.
///
/// ### 2. Throttled auto-scroll keeps the latest message visible
/// When `messages.count` changes, the list scrolls to the bottom anchor.
/// Scrolling is throttled (max once per 400ms) with a 450ms trailing
/// guarantee, preventing jank during fast streaming updates.
///
/// ## Bad Example (causes CPU 100%)
/// ```swift
/// ScrollView {
///     LazyVStack {
///         ForEach(messages) { message in
///             MessageBubble(message: message)
///         }
///     }
/// }
/// ```
///
/// ## Correct Example
/// ```swift
/// SWMessageList(messages: messages) { message in
///     MessageBubble(message: message)
/// }
/// ```
public struct SWMessageList<Message: Identifiable, Content: View>: View {
    let messages: [Message]
    let content: (Message) -> Content

    // Throttle state for auto-scroll
    @State private var lastScrollTime: Date = .distantPast
    @State private var trailingScrollTask: Task<Void, Never>?

    /// Initialize the message list
    /// - Parameters:
    ///   - messages: Array of messages (in chronological order, oldest first, newest last)
    ///   - content: Message view builder
    public init(
        messages: [Message],
        @ViewBuilder content: @escaping (Message) -> Content
    ) {
        self.messages = messages
        self.content = content
    }

    public var body: some View {
        ScrollViewReader { proxy in
            List {
                ForEach(messages) { message in
                    content(message)
                        .id(message.id)
                        .listRowSeparator(.hidden)
                        .listRowBackground(Color.clear)
                        .selectionDisabled()
                        #if os(iOS)
                        .listRowInsets(EdgeInsets(top: 4, leading: 12, bottom: 4, trailing: 12))
                        #else
                        .listRowInsets(EdgeInsets(top: 4, leading: 160, bottom: 4, trailing: 160))
                        #endif
                }

                // Bottom anchor — invisible spacer for scroll targeting
                Color.clear
                    .frame(height: 1)
                    .listRowSeparator(.hidden)
                    .listRowBackground(Color.clear)
                    .listRowInsets(EdgeInsets())
                    .id("sw-chat-bottom")
            }
            .listStyle(.plain)
            .scrollContentBackground(.hidden)
            #if os(iOS)
            .scrollDismissesKeyboard(.immediately)
            #endif
            .onChange(of: messages.count) {
                throttleScroll(proxy: proxy)
            }
        }
    }

    /// Throttled scroll to bottom anchor.
    ///
    /// - Fires immediately if >= 400ms since last scroll (leading edge).
    /// - Always schedules a 450ms trailing task to guarantee the final
    ///   position is correct after a burst of rapid updates.
    private func throttleScroll(proxy: ScrollViewProxy) {
        let now = Date()
        if now.timeIntervalSince(lastScrollTime) >= 0.4 {
            lastScrollTime = now
            proxy.scrollTo("sw-chat-bottom", anchor: .bottom)
        }

        // Cancel any pending trailing scroll and schedule a new one
        trailingScrollTask?.cancel()
        trailingScrollTask = Task { @MainActor in
            try? await Task.sleep(for: .milliseconds(450))
            guard !Task.isCancelled else { return }
            lastScrollTime = .now
            proxy.scrollTo("sw-chat-bottom", anchor: .bottom)
        }
    }
}

// MARK: - Message Bubble Base

/// Message bubble base view
///
/// Best practices:
/// - Use `.frame(maxWidth: .infinity)` to fix width, avoiding layout calculation loops
/// - Use `.fixedSize(horizontal: false, vertical: true)` to let content adapt vertically
public struct SWMessageBubble<Content: View>: View {
    let isFromUser: Bool
    let content: Content

    public init(isFromUser: Bool, @ViewBuilder content: () -> Content) {
        self.isFromUser = isFromUser
        self.content = content()
    }

    public var body: some View {
        HStack {
            if isFromUser {
                Spacer(minLength: 60)
            }

            content
                .fixedSize(horizontal: false, vertical: true)

            if !isFromUser {
                Spacer(minLength: 60)
            }
        }
        .frame(maxWidth: .infinity, alignment: isFromUser ? .trailing : .leading)
    }
}

// MARK: - Preview

private struct PreviewMessage: Identifiable {
    let id = UUID()
    let content: String
    let isUser: Bool
}

#Preview("Message List") {
    SWMessageList(messages: [
        PreviewMessage(content: "Hello!", isUser: true),
        PreviewMessage(content: "Hi there! How can I help you today?", isUser: false),
        PreviewMessage(content: "I have a question about SwiftUI performance.", isUser: true),
        PreviewMessage(content: "Sure, I'd be happy to help! What would you like to know about SwiftUI performance optimization?", isUser: false),
        PreviewMessage(content: "Why does my chat view freeze with 100% CPU?", isUser: true),
        PreviewMessage(content: "That's likely caused by using ScrollView + LazyVStack. When messages update frequently during streaming, LazyVStack can enter an infinite layout calculation loop. The solution is to use List instead, which has more stable layout behavior.", isUser: false),
    ]) { message in
        SWMessageBubble(isFromUser: message.isUser) {
            Text(message.content)
                .padding(12)
                .background(message.isUser ? Color.accentColor : swMessageBubbleBackground)
                .foregroundStyle(message.isUser ? .white : .primary)
                .clipShape(RoundedRectangle(cornerRadius: 16))
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWChat/SWVolcEngineASRService+iOS.swift`
```
//
//  SWVolcEngineASRService+iOS.swift
//  ShipSwift
//
//  VolcEngine automatic speech recognition service client.
//  Streams audio over WebSocket to ByteDance's VolcEngine ASR API,
//  providing real-time and final transcription callbacks.
//
//  Usage:
//    // 1. Create config with VolcEngine credentials
//    let config = SWASRConfig(
//        appId: "your-app-id",
//        accessToken: "your-access-token",
//        cluster: "volcengine_streaming_common",  // default
//        language: "zh-CN"                         // default, or "en-US"
//    )
//
//    // 2. Create service and set callbacks
//    let asr = SWVolcEngineASRService(config: config)
//
//    asr.onTranscriptionUpdate = { text in
//        print("Real-time: \(text)")  // partial results while speaking
//    }
//    asr.onTranscriptionComplete = { text in
//        print("Final: \(text)")      // final result after stop
//    }
//    asr.onError = { error in
//        print("Error: \(error.localizedDescription)")
//    }
//
//    // 3. Start/stop recording
//    try await asr.startRecording()   // requests mic permission, connects WebSocket
//    // ... user speaks ...
//    await asr.stopRecording()        // sends end-of-audio, triggers completion
//
//    // 4. Cancel recording (discards results)
//    asr.cancelRecording()
//
//    // 5. Observable state properties
//    asr.isRecording      // Bool
//    asr.transcribedText  // current transcription text
//    asr.error            // last error, if any
//
//  Created by Wei Zhong on 3/1/26.
//

import AVFoundation
import Compression
import Foundation
import Network

// MARK: - Configuration

/// VolcEngine ASR configuration
public struct SWASRConfig {
    public let appId: String
    public let accessToken: String
    public let cluster: String
    public let language: String

    public init(
        appId: String,
        accessToken: String,
        cluster: String = "volcengine_streaming_common",
        language: String = "zh-CN"
    ) {
        self.appId = appId
        self.accessToken = accessToken
        self.cluster = cluster
        self.language = language
    }
}

// MARK: - ASR Service

/// VolcEngine streaming speech recognition service
///
/// Usage:
/// ```swift
/// let config = SWASRConfig(appId: "xxx", accessToken: "xxx")
/// let asr = SWVolcEngineASRService(config: config)
///
/// asr.onTranscriptionUpdate = { text in print("Realtime: \(text)") }
/// asr.onTranscriptionComplete = { text in print("Complete: \(text)") }
///
/// try await asr.startRecording()
/// // ... user speaks ...
/// await asr.stopRecording()
/// ```
@Observable
public final class SWVolcEngineASRService: @unchecked Sendable {

    // MARK: - Configuration

    private let host = "openspeech.bytedance.com"
    private let port: UInt16 = 443
    private let path = "/api/v2/asr"
    private let config: SWASRConfig

    // MARK: - State

    public private(set) var isRecording = false
    public private(set) var transcribedText = ""
    public private(set) var error: Error?

    // MARK: - Callbacks

    /// Realtime transcription update callback
    public var onTranscriptionUpdate: ((String) -> Void)?
    /// Transcription complete callback
    public var onTranscriptionComplete: ((String) -> Void)?
    /// Error callback
    public var onError: ((Error) -> Void)?

    // MARK: - Private Properties

    private var connection: NWConnection?
    private var audioEngine: AVAudioEngine?
    private var isConnected = false
    private var connectionContinuation: CheckedContinuation<Void, Error>?
    private var receiveBuffer = Data()
    private let queue = DispatchQueue(label: "com.shipswift.asr.websocket")
    private var audioConverter: AVAudioConverter?
    private let targetFormat = AVAudioFormat(commonFormat: .pcmFormatInt16, sampleRate: 16000, channels: 1, interleaved: true)!

    // MARK: - Initialization

    public init(config: SWASRConfig) {
        self.config = config
    }

    // MARK: - Public Methods

    /// Start recording and perform speech recognition
    public func startRecording() async throws {
        guard !isRecording else { return }

        let granted = await requestMicrophonePermission()
        guard granted else {
            throw SWASRError.microphonePermissionDenied
        }

        transcribedText = ""
        error = nil

        try await connectWebSocket()
        try sendFullClientRequest()
        try startAudioEngine()

        isRecording = true
    }

    /// Stop recording
    public func stopRecording() async {
        guard isRecording else { return }

        isRecording = false
        stopAudioEngine()
        sendEndOfAudio()
    }

    /// Cancel recording
    public func cancelRecording() {
        isRecording = false
        stopAudioEngine()
        disconnectWebSocket()
        transcribedText = ""
    }

    // MARK: - Microphone Permission

    private func requestMicrophonePermission() async -> Bool {
        await withCheckedContinuation { continuation in
            AVAudioApplication.requestRecordPermission { granted in
                continuation.resume(returning: granted)
            }
        }
    }

    // MARK: - WebSocket Connection

    private func connectWebSocket() async throws {
        let tlsOptions = NWProtocolTLS.Options()
        let tcpOptions = NWProtocolTCP.Options()
        let params = NWParameters(tls: tlsOptions, tcp: tcpOptions)

        connection = NWConnection(host: NWEndpoint.Host(host), port: NWEndpoint.Port(rawValue: port)!, using: params)

        try await withCheckedThrowingContinuation { (continuation: CheckedContinuation<Void, Error>) in
            connectionContinuation = continuation

            connection?.stateUpdateHandler = { [weak self] state in
                guard let self else { return }
                Task { @MainActor in
                    switch state {
                    case .ready:
                        self.performWebSocketHandshake()
                    case .failed(let error):
                        self.connectionContinuation?.resume(throwing: error)
                        self.connectionContinuation = nil
                    default:
                        break
                    }
                }
            }

            connection?.start(queue: queue)
        }
    }

    private func performWebSocketHandshake() {
        var keyBytes = [UInt8](repeating: 0, count: 16)
        _ = SecRandomCopyBytes(kSecRandomDefault, 16, &keyBytes)
        let wsKey = Data(keyBytes).base64EncodedString()

        let request = """
        GET \(path) HTTP/1.1\r
        Host: \(host)\r
        Upgrade: websocket\r
        Connection: Upgrade\r
        Sec-WebSocket-Key: \(wsKey)\r
        Sec-WebSocket-Version: 13\r
        Authorization: Bearer;\(config.accessToken)\r
        \r

        """

        connection?.send(content: request.data(using: .utf8), completion: .contentProcessed { [weak self] error in
            if let error = error {
                self?.connectionContinuation?.resume(throwing: error)
                self?.connectionContinuation = nil
            } else {
                self?.receiveHandshakeResponse()
            }
        })
    }

    private func receiveHandshakeResponse() {
        connection?.receive(minimumIncompleteLength: 1, maximumLength: 4096) { [weak self] content, _, _, error in
            guard let self else { return }

            if let error = error {
                self.connectionContinuation?.resume(throwing: error)
                self.connectionContinuation = nil
                return
            }

            if let data = content, let response = String(data: data, encoding: .utf8) {
                if response.contains("101") && response.lowercased().contains("upgrade") {
                    self.isConnected = true
                    self.connectionContinuation?.resume()
                    self.connectionContinuation = nil
                    self.startReceivingFrames()
                } else {
                    self.connectionContinuation?.resume(throwing: SWASRError.connectionFailed)
                    self.connectionContinuation = nil
                }
            }
        }
    }

    private func startReceivingFrames() {
        guard isConnected else { return }

        connection?.receive(minimumIncompleteLength: 2, maximumLength: 65536) { [weak self] content, _, isComplete, error in
            guard let self else { return }

            if error != nil {
                DispatchQueue.main.async {
                    if !self.transcribedText.isEmpty {
                        self.onTranscriptionComplete?(self.transcribedText)
                    }
                }
                return
            }

            if let data = content {
                self.receiveBuffer.append(data)
                self.processWebSocketFrames()
            }

            if isComplete {
                self.isConnected = false
                DispatchQueue.main.async {
                    if !self.transcribedText.isEmpty {
                        self.onTranscriptionComplete?(self.transcribedText)
                    }
                }
            } else {
                self.startReceivingFrames()
            }
        }
    }

    private func processWebSocketFrames() {
        let bufferCopy = Array(receiveBuffer)
        guard bufferCopy.count >= 2 else { return }

        var offset = 0
        while bufferCopy.count - offset >= 2 {
            let firstByte = bufferCopy[offset]
            let secondByte = bufferCopy[offset + 1]

            let isMasked = (secondByte & 0x80) != 0
            var payloadLength = UInt64(secondByte & 0x7F)
            var headerSize = 2

            if payloadLength == 126 {
                guard bufferCopy.count - offset >= 4 else { break }
                payloadLength = UInt64(bufferCopy[offset + 2]) << 8 | UInt64(bufferCopy[offset + 3])
                headerSize = 4
            } else if payloadLength == 127 {
                guard bufferCopy.count - offset >= 10 else { break }
                payloadLength = 0
                for i in 0..<8 {
                    payloadLength = payloadLength << 8 | UInt64(bufferCopy[offset + 2 + i])
                }
                headerSize = 10
            }

            if isMasked { headerSize += 4 }

            let totalLength = headerSize + Int(payloadLength)
            guard bufferCopy.count - offset >= totalLength else { break }

            var payload = Data(bufferCopy[(offset + headerSize)..<(offset + totalLength)])

            if isMasked {
                let maskStart = offset + headerSize - 4
                let maskKey = Array(bufferCopy[maskStart..<(maskStart + 4)])
                for i in 0..<payload.count {
                    payload[i] ^= maskKey[i % 4]
                }
            }

            offset += totalLength

            let opcode = firstByte & 0x0F
            switch opcode {
            case 0x01, 0x02:
                handleServerResponse(payload)
            case 0x08:
                isConnected = false
                DispatchQueue.main.async {
                    if !self.transcribedText.isEmpty {
                        self.onTranscriptionComplete?(self.transcribedText)
                    }
                }
            case 0x09:
                sendPong(payload)
            default:
                break
            }
        }

        if offset > 0 {
            receiveBuffer.removeFirst(offset)
        }
    }

    private func sendPong(_ data: Data) {
        sendWebSocketFrame(opcode: 0x0A, payload: data)
    }

    private func disconnectWebSocket() {
        if isConnected {
            sendWebSocketFrame(opcode: 0x08, payload: Data())
        }
        connection?.cancel()
        connection = nil
        isConnected = false
        receiveBuffer.removeAll()
    }

    private func sendWebSocketFrame(opcode: UInt8, payload: Data) {
        var frame = Data()
        frame.append(0x80 | opcode)

        let length = payload.count
        if length < 126 {
            frame.append(UInt8(0x80 | length))
        } else if length < 65536 {
            frame.append(0xFE)
            frame.append(UInt8((length >> 8) & 0xFF))
            frame.append(UInt8(length & 0xFF))
        } else {
            frame.append(0xFF)
            for i in (0..<8).reversed() {
                frame.append(UInt8((length >> (i * 8)) & 0xFF))
            }
        }

        var maskKey = [UInt8](repeating: 0, count: 4)
        _ = SecRandomCopyBytes(kSecRandomDefault, 4, &maskKey)
        frame.append(contentsOf: maskKey)

        var maskedPayload = payload
        for i in 0..<maskedPayload.count {
            maskedPayload[i] ^= maskKey[i % 4]
        }
        frame.append(maskedPayload)

        connection?.send(content: frame, completion: .contentProcessed { _ in })
    }

    // MARK: - Binary Protocol

    private func sendFullClientRequest() throws {
        let payload: [String: Any] = [
            "app": [
                "appid": config.appId,
                "token": config.accessToken,
                "cluster": config.cluster
            ],
            "user": ["uid": UUID().uuidString],
            "audio": [
                "format": "pcm",
                "rate": 16000,
                "bits": 16,
                "channel": 1,
                "language": config.language
            ],
            "request": [
                "reqid": UUID().uuidString,
                "workflow": "audio_in,resample,partition,vad,fe,decode,itn,nlu_punctuate",
                "result_type": "full",
                "show_utterances": true
            ]
        ]

        let message = try buildFullClientRequest(payload: payload)
        sendWebSocketMessage(message)
    }

    private func sendAudioData(_ audioData: Data) {
        guard isConnected else { return }
        let message = buildAudioOnlyRequest(audioData: audioData)
        sendWebSocketMessage(message)
    }

    private func sendEndOfAudio() {
        let message = buildAudioOnlyRequest(audioData: Data(), isLast: true)
        sendWebSocketMessage(message)
    }

    private func sendWebSocketMessage(_ data: Data) {
        sendWebSocketFrame(opcode: 0x02, payload: data)
    }

    private func buildFullClientRequest(payload: [String: Any]) throws -> Data {
        let jsonData = try JSONSerialization.data(withJSONObject: payload)
        let compressedPayload = try gzipCompress(jsonData)

        var header = Data()
        header.append(0x11)
        header.append(0x10)
        header.append(0x11)
        header.append(0x00)

        var payloadSize = UInt32(compressedPayload.count).bigEndian
        header.append(Data(bytes: &payloadSize, count: 4))

        return header + compressedPayload
    }

    private func buildAudioOnlyRequest(audioData: Data, isLast: Bool = false) -> Data {
        var header = Data()
        header.append(0x11)
        header.append(isLast ? 0x22 : 0x20)
        header.append(0x00)
        header.append(0x00)

        var payloadSize = UInt32(audioData.count).bigEndian
        header.append(Data(bytes: &payloadSize, count: 4))

        return header + audioData
    }

    private func handleServerResponse(_ data: Data) {
        guard data.count >= 4 else { return }

        let messageType = (data[1] >> 4) & 0x0F
        let compression = data[2] & 0x0F

        if messageType == 0x0B { return }

        if messageType == 0x0F {
            guard data.count >= 8 else { return }
            let payloadSize = data.subdata(in: 4..<8).withUnsafeBytes { $0.load(as: UInt32.self).bigEndian }
            let actualSize = min(Int(payloadSize), data.count - 8)
            guard actualSize > 0 else { return }

            let payloadData = data.subdata(in: 8..<(8 + actualSize))
            var jsonData = payloadData
            if compression == 0x01 {
                jsonData = (try? gzipDecompress(payloadData)) ?? payloadData
            }

            if let json = try? JSONSerialization.jsonObject(with: jsonData) as? [String: Any],
               let message = json["message"] as? String {
                DispatchQueue.main.async {
                    self.onError?(SWASRError.serverError(message))
                }
            }
            return
        }

        guard data.count >= 8 else { return }
        let payloadSize = Int(data.subdata(in: 4..<8).withUnsafeBytes { $0.load(as: UInt32.self).bigEndian })
        let actualPayloadSize = min(payloadSize, data.count - 8)
        guard actualPayloadSize > 0 else { return }

        let payloadData = data.subdata(in: 8..<(8 + actualPayloadSize))
        var jsonData = payloadData

        if compression == 0x01 {
            guard let decompressed = try? gzipDecompress(payloadData) else { return }
            jsonData = decompressed
        }

        if let response = try? JSONSerialization.jsonObject(with: jsonData) as? [String: Any] {
            handleASRResponse(response)
        }
    }

    private func handleASRResponse(_ response: [String: Any]) {
        if let code = response["code"] as? Int, code != 1000 {
            let message = response["message"] as? String ?? "Unknown error"
            DispatchQueue.main.async {
                self.onError?(SWASRError.serverError(message))
            }
            return
        }

        var text: String?
        var isEnd = false

        if let resultArray = response["result"] as? [[String: Any]], let firstResult = resultArray.first {
            text = firstResult["text"] as? String

            if let utterances = firstResult["utterances"] as? [[String: Any]], !utterances.isEmpty {
                if let lastUtterance = utterances.last {
                    text = lastUtterance["text"] as? String
                    isEnd = (lastUtterance["definite"] as? Int ?? 0) == 1
                }
            }
        }

        if text == nil, let directText = response["text"] as? String {
            text = directText
            isEnd = response["is_end"] as? Bool ?? false
        }

        if let text = text, !text.isEmpty {
            DispatchQueue.main.async {
                self.transcribedText = text
                self.onTranscriptionUpdate?(text)
            }
        }

        if isEnd {
            DispatchQueue.main.async {
                self.onTranscriptionComplete?(self.transcribedText)
            }
        }
    }

    // MARK: - Audio Engine

    private func startAudioEngine() throws {
        #if os(iOS)
        let audioSession = AVAudioSession.sharedInstance()
        try audioSession.setCategory(.playAndRecord, mode: .default, options: [.defaultToSpeaker, .allowBluetoothA2DP])
        try audioSession.setActive(true)
        #endif

        let audioEngine = AVAudioEngine()
        let inputNode = audioEngine.inputNode
        let inputFormat = inputNode.outputFormat(forBus: 0)

        guard let converter = AVAudioConverter(from: inputFormat, to: targetFormat) else {
            throw SWASRError.audioConverterFailed
        }
        audioConverter = converter

        inputNode.installTap(onBus: 0, bufferSize: 4096, format: inputFormat) { [weak self] buffer, _ in
            guard let self, self.isRecording else { return }
            if let data = self.convertBuffer(buffer) {
                self.sendAudioData(data)
            }
        }

        try audioEngine.start()
        self.audioEngine = audioEngine
    }

    private func stopAudioEngine() {
        audioEngine?.inputNode.removeTap(onBus: 0)
        audioEngine?.stop()
        audioEngine = nil
        audioConverter = nil
    }

    private func convertBuffer(_ buffer: AVAudioPCMBuffer) -> Data? {
        guard let converter = audioConverter else { return nil }

        let ratio = targetFormat.sampleRate / buffer.format.sampleRate
        let capacity = AVAudioFrameCount(Double(buffer.frameLength) * ratio)

        guard let output = AVAudioPCMBuffer(pcmFormat: targetFormat, frameCapacity: capacity) else { return nil }

        var error: NSError?
        var hasData = false

        converter.convert(to: output, error: &error) { _, outStatus in
            if hasData {
                outStatus.pointee = .noDataNow
                return nil
            }
            hasData = true
            outStatus.pointee = .haveData
            return buffer
        }

        if error != nil { return nil }

        let audioBuffer = output.audioBufferList.pointee.mBuffers
        guard let mData = audioBuffer.mData, audioBuffer.mDataByteSize > 0 else { return nil }
        return Data(bytes: mData, count: Int(audioBuffer.mDataByteSize))
    }

    // MARK: - Compression

    private func gzipCompress(_ data: Data) throws -> Data {
        let buffer = UnsafeMutablePointer<UInt8>.allocate(capacity: data.count)
        defer { buffer.deallocate() }

        let size = data.withUnsafeBytes { src -> Int in
            compression_encode_buffer(buffer, data.count, src.bindMemory(to: UInt8.self).baseAddress!, data.count, nil, COMPRESSION_ZLIB)
        }

        guard size > 0 else { throw SWASRError.compressionFailed }

        var result = Data([0x1F, 0x8B, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03])
        result.append(Data(bytes: buffer, count: size))

        var crc = crc32(data).littleEndian
        result.append(Data(bytes: &crc, count: 4))
        var len = UInt32(data.count).littleEndian
        result.append(Data(bytes: &len, count: 4))

        return result
    }

    private func gzipDecompress(_ data: Data) throws -> Data {
        guard data.count > 18 else { throw SWASRError.decompressionFailed }

        var offset = 10
        if data[3] & 0x04 != 0 { offset += 2 + Int(data[10]) + Int(data[11]) << 8 }
        if data[3] & 0x08 != 0 { while offset < data.count && data[offset] != 0 { offset += 1 }; offset += 1 }
        if data[3] & 0x10 != 0 { while offset < data.count && data[offset] != 0 { offset += 1 }; offset += 1 }
        if data[3] & 0x02 != 0 { offset += 2 }

        let compressed = data.subdata(in: offset..<(data.count - 8))
        let buffer = UnsafeMutablePointer<UInt8>.allocate(capacity: compressed.count * 10)
        defer { buffer.deallocate() }

        let size = compressed.withUnsafeBytes { src -> Int in
            compression_decode_buffer(buffer, compressed.count * 10, src.bindMemory(to: UInt8.self).baseAddress!, compressed.count, nil, COMPRESSION_ZLIB)
        }

        guard size > 0 else { throw SWASRError.decompressionFailed }
        return Data(bytes: buffer, count: size)
    }

    private func crc32(_ data: Data) -> UInt32 {
        var crc: UInt32 = 0xFFFFFFFF
        for byte in data {
            crc ^= UInt32(byte)
            for _ in 0..<8 { crc = crc & 1 != 0 ? (crc >> 1) ^ 0xEDB88320 : crc >> 1 }
        }
        return ~crc
    }
}

// MARK: - Error Types

public enum SWASRError: LocalizedError {
    case microphonePermissionDenied
    case connectionFailed
    case audioConverterFailed
    case compressionFailed
    case decompressionFailed
    case serverError(String)

    public var errorDescription: String? {
        switch self {
        case .microphonePermissionDenied: return "Microphone permission denied"
        case .connectionFailed: return "Connection failed"
        case .audioConverterFailed: return "Failed to create audio converter"
        case .compressionFailed: return "Data compression failed"
        case .decompressionFailed: return "Data decompression failed"
        case .serverError(let msg): return "Server error: \(msg)"
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWPaywall/SWPaywallView.swift`
```
//
//  SWPaywallView.swift
//  ShipSwift
//
//  Subscription paywall view using SubscriptionStoreView.
//  Displays subscription options, feature list, and handles purchase
//  completion with automatic pro status update and dismiss.
//
//  Usage:
//    // 1. Configure SWStoreManager before presenting (see SWStoreManager.swift)
//    //    Make sure product IDs, features, and policy URLs are set.
//
//    // 2. Present as a sheet with SWStoreManager in environment
//    @State private var showPaywall = false
//
//    Button("Upgrade") { showPaywall = true }
//    .sheet(isPresented: $showPaywall) {
//        SWPaywallView()
//            .environment(SWStoreManager.shared)
//    }
//
//    // 3. The view automatically:
//    //    - Shows monthly and yearly subscription options
//    //    - Displays configurable feature list with icons
//    //    - Shows Restore Purchases, Redeem Code, and policy buttons
//    //    - Dismisses on successful purchase
//    //    - Updates SWStoreManager.shared.isPro status
//
//    // 4. Preview usage
//    #Preview {
//        SWPaywallView()
//            .environment(SWStoreManager.shared)
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI
import StoreKit

struct SWPaywallView: View {
    var isDemo: Bool = false

    @Environment(SWStoreManager.self) private var storeManager
    @Environment(\.dismiss) private var dismiss
    @AppStorage("appLanguage") private var appLanguage = "en"

    var body: some View {
        if isDemo {
            demoBody
        } else {
            NavigationStack {
                SubscriptionStoreView(productIDs: storeManager.config.allSubscriptionIDs) {
                    paywallContent
                }
                .storeButton(.visible, for: .policies)
                .storeButton(.visible, for: .restorePurchases)
                .storeButton(.visible, for: .cancellation)
                .storeButton(.visible, for: .redeemCode)
                .scrollIndicators(.hidden)
                .subscriptionStorePolicyDestination(
                    url: URL(string: storeManager.config.privacyPolicyURL)!,
                    for: .privacyPolicy
                )
                .subscriptionStorePolicyDestination(
                    url: URL(string: storeManager.config.termsOfServiceURL)!,
                    for: .termsOfService
                )
                .onInAppPurchaseCompletion { _, result in
                    if case .success(.success(.verified)) = result {
                        Task {
                            await storeManager.updatePurchaseStatus()
                            dismiss()
                        }
                    }
                }
            }
        }
    }

    // MARK: - Demo Body

    @State private var demoPlanSelected = 1   // 0 = monthly, 1 = yearly

    private var demoBody: some View {
        ScrollView {
            VStack(spacing: 28) {
                paywallContent

                // Plan picker rows (mimics macOS SubscriptionStoreView list style)
                VStack(spacing: 0) {
                    demoPlanRow(
                        index: 0,
                        title: "Monthly",
                        price: "$4.99",
                        period: "per month",
                        badge: nil
                    )
                    Divider()
                    demoPlanRow(
                        index: 1,
                        title: "Yearly",
                        price: "$29.99",
                        period: "per year",
                        badge: "Best Value"
                    )
                }
                #if canImport(UIKit)
                .background(Color(UIColor.secondarySystemGroupedBackground))
                #else
                .background(Color(NSColor.controlBackgroundColor))
                #endif
                .clipShape(RoundedRectangle(cornerRadius: 10))
                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.primary.opacity(0.1), lineWidth: 1))

                // Subscribe CTA
                Button {
                    SWAlertManager.shared.show(.info, message: "UI Demo — purchase actions are not functional")
                } label: {
                    Text(demoPlanSelected == 0 ? "Subscribe — $4.99 / month" : "Subscribe — $29.99 / year")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 12)
                }
                .buttonStyle(.borderedProminent)

                // Footer
                VStack(spacing: 6) {
                    Button("Restore Purchases") {
                        SWAlertManager.shared.show(.info, message: "UI Demo — purchase actions are not functional")
                    }
                    .buttonStyle(.plain)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)

                    HStack(spacing: 16) {
                        Text("Terms of Service").font(.caption).foregroundStyle(.tertiary)
                        Text("Privacy Policy").font(.caption).foregroundStyle(.tertiary)
                    }
                }
                .padding(.bottom, 8)
            }
            .padding(.vertical)
            .padding(.horizontal)
            .frame(maxWidth: 480)
            .frame(maxWidth: .infinity)
        }
    }

    private func demoPlanRow(index: Int, title: String, price: String, period: String, badge: String?) -> some View {
        Button {
            withAnimation(.easeInOut(duration: 0.15)) { demoPlanSelected = index }
        } label: {
            HStack(spacing: 12) {
                // Radio indicator
                Image(systemName: demoPlanSelected == index ? "circle.inset.filled" : "circle")
                    .foregroundStyle(demoPlanSelected == index ? Color.accentColor : .secondary)
                    .font(.system(size: 18))

                VStack(alignment: .leading, spacing: 2) {
                    HStack(spacing: 6) {
                        Text(title).fontWeight(.medium)
                        if let badge {
                            Text(badge)
                                .font(.caption2)
                                .fontWeight(.semibold)
                                .foregroundStyle(.white)
                                .padding(.horizontal, 6)
                                .padding(.vertical, 2)
                                .background(Color.accentColor)
                                .clipShape(Capsule())
                        }
                    }
                    if index == 1 {
                        Text("$2.50 / month billed annually")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }

                Spacer()

                VStack(alignment: .trailing, spacing: 2) {
                    Text(price).fontWeight(.semibold)
                    Text(period).font(.caption).foregroundStyle(.secondary)
                }
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 14)
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
    }

    @ViewBuilder
    private var paywallContent: some View {
        VStack(spacing: 20) {
            SWShakingIcon(image: Image(systemName: "apple.logo"))

            Text(storeManager.config.title)
                .font(.largeTitle)
                .fontWeight(.bold)

            VStack(alignment: .leading) {
                ForEach(storeManager.config.features) { feature in
                    HStack {
                        Image(systemName: feature.icon)
                            .imageScale(.small)
                        Text(feature.text)
                            .font(.subheadline)
                            .multilineTextAlignment(.leading)
                    }
                }
            }
            .font(.title3)
            .padding(.vertical)
        }
        .padding(.top)
        .environment(\.locale, Locale(identifier: appLanguage))
    }
}

#Preview {
    SWPaywallView()
        .environment(SWStoreManager.shared)
}
```

## File: `ShipSwift/SWPackage/SWModule/SWPaywall/SWStoreManager.swift`
```
//
//  SWStoreManager.swift
//  ShipSwift
//
//  StoreKit 2 subscription and in-app purchase manager.
//  Manages monthly/yearly subscriptions and lifetime purchases,
//  tracks pro status, and enforces free-user resource limits.
//
//  Usage:
//    // 1. Configure before showing the paywall (e.g. in App init)
//    let store = SWStoreManager.shared
//    store.config.monthlyProductID = "com.myapp.monthly"
//    store.config.yearlyProductID  = "com.myapp.yearly"
//    store.config.lifetimeProductID = "com.myapp.lifetime"
//    store.config.tripLimitForFreeUser = 3
//    store.config.itemLimitForFreeUser = 20
//    store.config.privacyPolicyURL = "https://example.com/privacy"
//    store.config.termsOfServiceURL = "https://example.com/terms"
//    store.config.title = "Go Pro"
//    store.config.features = [
//        .init(icon: "star.fill", text: "Unlimited trips"),
//        .init(icon: "bolt.fill", text: "Priority support"),
//    ]
//
//    // 2. Inject into SwiftUI environment
//    ContentView()
//        .environment(SWStoreManager.shared)
//
//    // 3. Check pro status anywhere
//    if SWStoreManager.shared.isPro { /* unlock premium features */ }
//    // isPro == hasLifetimePurchase || hasActiveSubscription
//
//    // 4. Enforce free-user limits
//    if store.canCreateNewTrip(currentTripCount: trips.count) {
//        createTrip()
//    } else {
//        showPaywall()
//    }
//    let remaining = store.remainingItemsForFreeUser(currentItemCount: items.count)
//
//    // 5. Manually refresh purchase status
//    await store.updatePurchaseStatus()
//
//  Created by Wei Zhong on 3/1/26.
//

import StoreKit
import SwiftUI

@MainActor
@Observable
final class SWStoreManager {

    // MARK: - Singleton

    static let shared = SWStoreManager()

    // MARK: - Product Configuration (inline from app)

    /// Override these in your app's init or via a configure method
    struct PaywallConfig {
        var title = "Pro"
        var monthlyProductID = "com.example.app.monthly"
        var yearlyProductID = "com.example.app.yearly"
        var lifetimeProductID = "com.example.app.lifetime"
        var tripLimitForFreeUser = 3
        var itemLimitForFreeUser = 20
        var privacyPolicyURL = "https://example.com/privacy"
        var termsOfServiceURL = "https://example.com/terms"

        struct Feature: Identifiable {
            let id = UUID()
            let icon: String
            let text: LocalizedStringKey
        }

        var features: [Feature] = []

        var allSubscriptionIDs: [String] {
            [monthlyProductID, yearlyProductID]
        }
    }

    /// Configure this before showing the paywall
    var config = PaywallConfig()

    // MARK: - Product Type

    enum ProductType: CaseIterable {
        case lifetime
        case monthly
        case yearly
    }

    private func productType(for id: String) -> ProductType? {
        if id == config.lifetimeProductID { return .lifetime }
        if id == config.monthlyProductID { return .monthly }
        if id == config.yearlyProductID { return .yearly }
        return nil
    }

    // MARK: - State

    private(set) var hasActiveSubscription = false
    private(set) var hasLifetimePurchase = false

    /// Whether the server has an active Pro API key for this user
    var hasServerPro = false

    /// Cached API key from server
    var apiKey: String?

    var isPro: Bool { hasLifetimePurchase || hasActiveSubscription || hasServerPro }

    // MARK: - Init

    init() {
        Task { await updatePurchaseStatus() }
        startObservingTransactions()
    }

    private func startObservingTransactions() {
        Task { [weak self] in
            for await result in Transaction.updates {
                guard let self, case let .verified(transaction) = result else { continue }
                await transaction.finish()
                await updatePurchaseStatus()
            }
        }
    }

    // MARK: - Purchase Status

    func updatePurchaseStatus() async {
        var subscription = false
        var lifetime = false

        for await result in Transaction.currentEntitlements {
            guard case let .verified(transaction) = result else { continue }

            switch productType(for: transaction.productID) {
            case .lifetime:
                lifetime = true
            case .monthly, .yearly:
                if transaction.revocationDate == nil {
                    subscription = true
                }
            case nil:
                break
            }
        }

        hasLifetimePurchase = lifetime
        hasActiveSubscription = subscription
    }

    // MARK: - Lifetime Product

    /// The loaded lifetime product (for custom paywall UI)
    private(set) var lifetimeProduct: Product?

    /// Load the lifetime product from StoreKit
    func loadLifetimeProduct() async {
        do {
            let products = try await Product.products(for: [config.lifetimeProductID])
            lifetimeProduct = products.first
        } catch {
            swDebugLog("Failed to load lifetime product: \(error)")
        }
    }

    // MARK: - Server Pro Status

    /// Check server pro status using Cognito ID token
    func checkServerProStatus(idToken: String) async {
        do {
            let service = ShipSwiftAPIService()
            let status = try await service.getApiKeyStatus(idToken: idToken)
            hasServerPro = status.hasKey && status.status == "active"
            if hasServerPro {
                apiKey = status.apiKey
            }
        } catch {
            swDebugLog("Failed to check server pro status: \(error)")
        }
    }

    /// Sync App Store purchase to server and get API key
    func syncPurchaseToServer(idToken: String) async -> String? {
        // Get the latest transaction for the lifetime product
        guard let result = await Transaction.latest(for: config.lifetimeProductID),
              case .verified = result else {
            return nil
        }

        do {
            let service = ShipSwiftAPIService()
            let response = try await service.verifyAppStorePurchase(
                idToken: idToken,
                signedTransactionInfo: result.jwsRepresentation
            )
            apiKey = response.apiKey
            hasServerPro = true
            return response.apiKey
        } catch {
            swDebugLog("Failed to sync purchase to server: \(error)")
            return nil
        }
    }

    // MARK: - Free User Limit Checks

    func canCreateNewTrip(currentTripCount: Int) -> Bool {
        isPro || currentTripCount < config.tripLimitForFreeUser
    }

    func remainingTripsForFreeUser(currentTripCount: Int) -> Int? {
        guard !isPro else { return nil }
        return max(0, config.tripLimitForFreeUser - currentTripCount)
    }

    func canCreateNewItem(currentItemCount: Int) -> Bool {
        isPro || currentItemCount < config.itemLimitForFreeUser
    }

    func remainingItemsForFreeUser(currentItemCount: Int) -> Int? {
        guard !isPro else { return nil }
        return max(0, config.itemLimitForFreeUser - currentItemCount)
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWSetting/SWSettingView+iOS.swift`
```
//
//  SWSettingView+iOS.swift
//  ShipSwift
//
//  Generic settings page template with language switching, share app, legal links,
//  recommended apps, and sign out / delete account sections.
//  Use directly as a NavigationStack page — no additional wrapping needed.
//
//  Usage:
//    // 1. Basic usage — embed directly in TabView or NavigationStack:
//    SWSettingView()
//
//    // 2. Customization points (modify the constants in this file):
//    //    - appStoreURL      → App Store URL for the share link
//    //    - termsURL         → Terms of Service URL
//    //    - privacyURL       → Privacy Policy URL
//    //    - appStoreFullpack / appStoreBrushmo / ...  → Recommended app links
//
//    // 3. Replace sign-out and delete-account logic:
//    //    Find the signOut() and deleteAccount() methods and replace the TODO comments with real implementations:
//    private func signOut() {
//        isSigningOut = true
//        Task {
//            await userManager.signOut()
//            isSigningOut = false
//        }
//    }
//
//    // 4. Language switching is based on @AppStorage("appLanguage"),
//    //    pair with SWDateExtension and similar utilities for global English/Chinese switching.
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

struct SWSettingView: View {

    // MARK: - State

    var isDemo: Bool = false

    @AppStorage("appLanguage") private var appLanguage = "en"
    @State private var selectedLanguage = UserDefaults.standard.string(forKey: "appLanguage") ?? "en"
    @State private var showDeleteConfirmation = false
    @State private var showSignOutConfirmation = false
    @State private var isDeleting = false
    @State private var isSigningOut = false
    
    // MARK: - Configuration (modify these values directly)
    
    private let appStoreURL = URL(string: "https://apps.apple.com/app/id6759209764")!
    private let termsURL = URL(string: "https://shipswift.app/terms")!
    private let privacyURL = URL(string: "https://shipswift.app/privacy")!
    
    // App Store URLs (examples, replace with actual URLs)
    private let appStoreFullpack = "https://apps.apple.com/us/app/fullpack-packing-outfit/id6745692929"
    private let appStoreBrushmo = "https://apps.apple.com/us/app/brushmo/id6744569822"
    private let appStoreLifebang = "https://apps.apple.com/us/app/lifebang/id6474886848"
    private let appStoreUtilityMax = "https://apps.apple.com/us/app/utilitymax%E6%95%88%E5%BA%A6%E5%AE%B6-%E7%BB%88%E8%BA%AB%E8%B4%A2%E5%8A%A1%E6%A8%A1%E6%8B%9F%E4%B8%8E%E9%80%80%E4%BC%91%E8%A7%84%E5%88%92%E5%99%A8/id6758595049"
    private let appStoreJourney = "https://apps.apple.com/us/app/journey-goal-tracker-diary/id6748666816"
    private let appStoreSmileMax = "https://apps.apple.com/us/app/smilemax/id6758947123"
    
    /// App version number
    private var appVersion: String {
        Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0.0"
    }
    
    /// App build number
    private var buildNumber: String {
        Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
    }
    
    // MARK: - Body
    
    var body: some View {
        NavigationStack {
            List {
                // MARK: - General Settings
                Section {
                    // Language switcher
                    Picker("Language", selection: $selectedLanguage) {
                        Text("English").tag("en")
                        Text("简体中文").tag("zh-Hans")
                    }
                    .onChange(of: selectedLanguage) { _, newValue in
                        if isDemo {
                            selectedLanguage = appLanguage
                            SWAlertManager.shared.show(.info, message: "UI Demo — language switching is not functional")
                        } else {
                            appLanguage = newValue
                        }
                    }
                    
                    // Share App
                    ShareLink(item: appStoreURL) {
                        HStack {
                            Text("Share App")
                            Spacer()
                            Image(systemName: "square.and.arrow.up")
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                
                // MARK: - Legal
                Section {
                    Link(destination: termsURL) {
                        HStack {
                            Text("Terms of Service")
                            Spacer()
                            Image(systemName: "chevron.right")
                                .font(.footnote)
                                .foregroundStyle(.secondary)
                        }
                    }
                    
                    Link(destination: privacyURL) {
                        HStack {
                            Text("Privacy Policy")
                            Spacer()
                            Image(systemName: "chevron.right")
                                .font(.footnote)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                
                // MARK: - Recommended Apps
                Section("Apps Built with ShipSwift") {
                    Link(destination: URL(string: appStoreSmileMax)!) {
                        labelWithImage(.smileMaxLogo, name: "SmileMax - Glow Up Coach")
                    }
                    Link(destination: URL(string: appStoreFullpack)!) {
                        labelWithImage(.fullpackLogo, name: "Fullpack - Packing & Outfit")
                    }
                    Link(destination: URL(string: appStoreBrushmo)!) {
                        labelWithImage(.brushmoLogo, name: "Brushmo - Oral Health Companion")
                    }
                    Link(destination: URL(string: appStoreLifebang)!) {
                        labelWithImage(.lifebangLogo, name: "Lifebang - Pro Cleaner")
                    }
                    Link(destination: URL(string: appStoreUtilityMax)!) {
                        labelWithImage(.utilityMaxLogo, name: "UtilityMax - Financial Simulator")
                    }
                    Link(destination: URL(string: appStoreJourney)!) {
                        labelWithImage(.journeyLogo, name: "Spark - Goal Tracker & Diary")
                    }
                }

                // MARK: - Account Actions
                Section {
                    Button {
                        showSignOutConfirmation = true
                    } label: {
                        HStack {
                            Text("Sign Out")
                            if isSigningOut {
                                Spacer()
                                ProgressView()
                            }
                        }
                    }
                    .disabled(isDeleting || isSigningOut)
                    
                    Button(role: .destructive) {
                        showDeleteConfirmation = true
                    } label: {
                        HStack {
                            Text("Delete Account")
                            if isDeleting {
                                Spacer()
                                ProgressView()
                            }
                        }
                    }
                    .disabled(isDeleting || isSigningOut)
                }
                
                // MARK: - Version Info
                Section {
                    LabeledContent("Version") {
                        Text("v\(appVersion) (\(buildNumber))")
                            .foregroundStyle(.secondary)
                    }
                }
            }
            .navigationTitle("Settings")
            .navigationBarTitleDisplayMode(.inline)
            .alert("Sign Out?", isPresented: $showSignOutConfirmation) {
                Button("Sign Out", role: .destructive) {
                    signOut()
                }
                Button("Cancel", role: .cancel) {}
            }
            .alert("Delete Account?", isPresented: $showDeleteConfirmation) {
                Button("Delete", role: .destructive) {
                    deleteAccount()
                }
                Button("Cancel", role: .cancel) {}
            } message: {
                Text("This action cannot be undone. All your data will be permanently deleted.")
            }
        }
    }
    
    // MARK: - Label With Image

    @ViewBuilder
    private func labelWithImage(_ image: ImageResource, name: LocalizedStringResource) -> some View {
        HStack {
            Image(image)
                .resizable()
                .scaledToFit()
                .frame(width: 32, height: 32)
                .clipShape(RoundedRectangle(cornerRadius: 6))
                .padding(5)
            Text(name)
        }
    }

    // MARK: - Actions (replace with actual logic)
    
    private func signOut() {
        isSigningOut = true
        Task {
            // TODO: Replace with actual sign-out logic
            // await userManager.signOut()
            try? await Task.sleep(for: .seconds(1))
            isSigningOut = false
        }
    }
    
    private func deleteAccount() {
        isDeleting = true
        Task {
            // TODO: Replace with actual account deletion logic
            // try await userManager.deleteAccount()
            try? await Task.sleep(for: .seconds(1))
            isDeleting = false
        }
    }
}

#Preview {
    SWSettingView()
}
```

## File: `ShipSwift/SWPackage/SWModule/SWSetting/SWSettingView+macOS.swift`
```
//
//  SWSettingView+macOS.swift
//  ShipSwift
//
//  macOS-native settings view using Form with grouped style.
//  Replaces the iOS List-based layout with native macOS Form controls,
//  LabeledContent rows, and macOS-appropriate link presentation.
//
//  Created by Wei Zhong on 3/7/26.
//

import SwiftUI

struct SWSettingView: View {

    // MARK: - State

    var isDemo: Bool = false

    @AppStorage("appLanguage") private var appLanguage = "en"
    @State private var selectedLanguage = UserDefaults.standard.string(forKey: "appLanguage") ?? "en"
    @State private var showDeleteConfirmation = false
    @State private var showSignOutConfirmation = false
    @State private var isDeleting = false
    @State private var isSigningOut = false

    // MARK: - Configuration

    private let appStoreURL = URL(string: "https://apps.apple.com/app/id6759209764")!
    private let termsURL = URL(string: "https://shipswift.app/terms")!
    private let privacyURL = URL(string: "https://shipswift.app/privacy")!

    private let appStoreFullpack    = URL(string: "https://apps.apple.com/us/app/fullpack-packing-outfit/id6745692929")!
    private let appStoreBrushmo     = URL(string: "https://apps.apple.com/us/app/brushmo/id6744569822")!
    private let appStoreLifebang    = URL(string: "https://apps.apple.com/us/app/lifebang/id6474886848")!
    private let appStoreJourney     = URL(string: "https://apps.apple.com/us/app/journey-goal-tracker-diary/id6748666816")!
    private let appStoreSmileMax    = URL(string: "https://apps.apple.com/us/app/smilemax/id6758947123")!
    private let appStoreUtilityMax  = URL(string: "https://apps.apple.com/us/app/utilitymax/id6758595049")!

    private var appVersion: String {
        Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0.0"
    }
    private var buildNumber: String {
        Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
    }

    // MARK: - Body

    var body: some View {
        Form {
            // General
            Section("General") {
                Picker("Language", selection: $selectedLanguage) {
                    Text("English").tag("en")
                    Text("简体中文").tag("zh-Hans")
                }
                .onChange(of: selectedLanguage) { _, newValue in
                    if isDemo {
                        selectedLanguage = appLanguage
                        SWAlertManager.shared.show(.info, message: "UI Demo — language switching is not functional")
                    } else {
                        appLanguage = newValue
                    }
                }

                ShareLink("Share App", item: appStoreURL)
                    .buttonStyle(.plain)
            }

            // Legal
            Section("Legal") {
                Link("Terms of Service", destination: termsURL)
                Link("Privacy Policy", destination: privacyURL)
            }

            // Recommended Apps
            Section("Apps Built with ShipSwift") {
                appRow(.smileMaxLogo,      name: "SmileMax",       url: appStoreSmileMax)
                appRow(.fullpackLogo,      name: "Fullpack",       url: appStoreFullpack)
                appRow(.brushmoLogo,       name: "Brushmo",        url: appStoreBrushmo)
                appRow(.lifebangLogo,      name: "Lifebang",       url: appStoreLifebang)
                appRow(.utilityMaxLogo,    name: "UtilityMax",     url: appStoreUtilityMax)
                appRow(.journeyLogo,       name: "Journey",        url: appStoreJourney)
            }

            // Account
            Section("Account") {
                Button {
                    showSignOutConfirmation = true
                } label: {
                    if isSigningOut {
                        Label("Signing Out…", systemImage: "arrow.right.square")
                    } else {
                        Label("Sign Out", systemImage: "arrow.right.square")
                    }
                }
                .disabled(isDeleting || isSigningOut)
                .buttonStyle(.plain)

                Button(role: .destructive) {
                    showDeleteConfirmation = true
                } label: {
                    if isDeleting {
                        Label("Deleting…", systemImage: "trash")
                    } else {
                        Label("Delete Account", systemImage: "trash")
                    }
                }
                .disabled(isDeleting || isSigningOut)
                .buttonStyle(.plain)
            }

            // Version
            Section {
                LabeledContent("Version", value: "v\(appVersion) (\(buildNumber))")
            }
        }
        .formStyle(.grouped)
        .navigationTitle("Settings")
        .confirmationDialog("Sign Out?", isPresented: $showSignOutConfirmation, titleVisibility: .visible) {
            Button("Sign Out", role: .destructive) { signOut() }
            Button("Cancel", role: .cancel) {}
        }
        .confirmationDialog("Delete Account?", isPresented: $showDeleteConfirmation, titleVisibility: .visible) {
            Button("Delete", role: .destructive) { deleteAccount() }
            Button("Cancel", role: .cancel) {}
        } message: {
            Text("This action cannot be undone. All your data will be permanently deleted.")
        }
    }

    // MARK: - App Row

    private func appRow(_ image: ImageResource, name: String, url: URL) -> some View {
        Link(destination: url) {
            HStack(spacing: 10) {
                Image(image)
                    .resizable()
                    .scaledToFit()
                    .frame(width: 28, height: 28)
                    .clipShape(RoundedRectangle(cornerRadius: 6))
                Text(name)
                Spacer()
                Image(systemName: "arrow.up.right")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
    }

    // MARK: - Actions

    private func signOut() {
        isSigningOut = true
        Task {
            // TODO: Replace with actual sign-out logic
            // await userManager.signOut()
            try? await Task.sleep(for: .seconds(1))
            isSigningOut = false
        }
    }

    private func deleteAccount() {
        isDeleting = true
        Task {
            // TODO: Replace with actual account deletion logic
            // try await userManager.deleteAccount()
            try? await Task.sleep(for: .seconds(1))
            isDeleting = false
        }
    }
}

#Preview {
    SWSettingView()
        .frame(width: 600, height: 700)
}
```

## File: `ShipSwift/SWPackage/SWModule/SWSubjectLifting/SWSubjectLiftingManager+iOS.swift`
```
//
//  SWSubjectLiftingManager.swift
//  ShipSwift
//
//  Subject lifting (background removal) manager using VisionKit's
//  ImageAnalyzer and ImageAnalysisInteraction.
//
//  Analyzes a UIImage, detects the primary subject, and returns
//  a background-removed PNG image.
//
//  Requirements: iOS 17+, VisionKit framework.
//
//  Usage:
//    @State private var manager = SWSubjectLiftingManager()
//
//    // Wire up error callback
//    manager.onError = { message in print(message) }
//
//    // Process an image
//    let result = await manager.processImage(photo)
//    if let result {
//        let extractedImage = result.image  // UIImage with background removed
//        let pngData = result.data          // PNG Data
//    }
//
//    // Check processing state
//    switch manager.processingState {
//    case .idle: // Ready
//    case .processing: // Working
//    case .completed: // Done — result available
//    case .failed: // Error occurred
//    }
//
//    // Cleanup when done
//    manager.cleanup()
//
//  Created by Wei Zhong on 3/8/26.
//

import VisionKit
import SwiftUI

// MARK: - Extracted Result

/// Result of a subject lifting operation containing the extracted image and its PNG data.
struct SWExtractedResult {
    let image: UIImage
    let data: Data
}

// MARK: - Manager

@MainActor
@Observable
final class SWSubjectLiftingManager {

    // MARK: - Processing State

    enum ProcessingState: Equatable {
        case idle
        case processing
        case failed
        case completed
    }

    // MARK: - Public Properties

    var processingState: ProcessingState = .idle

    /// Original image before extraction (set immediately on processImage call)
    var originalImage: UIImage?

    /// Extracted subject image with background removed
    var extractedImage: UIImage?

    /// Error callback — wire this up in the view layer for alert display
    var onError: ((String) -> Void)?

    // MARK: - Private Properties

    private let analyzer = ImageAnalyzer()
    private let configuration = ImageAnalyzer.Configuration(.visualLookUp)
    private var interaction: ImageAnalysisInteraction

    // MARK: - Initialization

    init() {
        let interaction = ImageAnalysisInteraction()
        interaction.preferredInteractionTypes = .imageSubject
        self.interaction = interaction
    }

    // MARK: - Public API

    /// Analyze an image and extract the primary subject with background removed.
    ///
    /// Returns an `SWExtractedResult` on success, or `nil` on failure.
    /// Updates `processingState`, `originalImage`, and `extractedImage` throughout.
    @discardableResult
    func processImage(_ image: UIImage) async -> SWExtractedResult? {
        originalImage = image
        extractedImage = nil
        processingState = .processing

        do {
            // Analyze the image for visual lookup subjects
            let analysis = try await analyzer.analyze(image, configuration: configuration)
            interaction.analysis = analysis

            // Get detected subjects
            let subjects = await interaction.subjects
            guard let firstSubject = subjects.first else {
                processingState = .failed
                onError?(String(localized: "No subject detected in the image"))
                scheduleReset(after: 3)
                return nil
            }

            // Extract the subject image (background removed)
            let subjectImage = try await firstSubject.image

            guard let pngData = subjectImage.pngData() else {
                processingState = .failed
                onError?(String(localized: "Failed to convert extracted image"))
                scheduleReset(after: 3)
                return nil
            }

            let result = SWExtractedResult(image: subjectImage, data: pngData)
            extractedImage = subjectImage
            processingState = .completed

            return result

        } catch {
            processingState = .failed
            onError?(String(localized: "Subject extraction failed"))
            scheduleReset(after: 3)
            return nil
        }
    }

    /// Reset manager to idle state and release image references.
    func cleanup() {
        interaction.analysis = nil
        processingState = .idle
        originalImage = nil
        extractedImage = nil
    }

    // MARK: - Private Helpers

    /// Auto-reset to idle after a delay (for failed/completed states).
    private func scheduleReset(after seconds: Int) {
        Task {
            try? await Task.sleep(for: .seconds(seconds))
            if processingState == .failed {
                processingState = .idle
                originalImage = nil
            }
        }
    }
}
```

## File: `ShipSwift/SWPackage/SWModule/SWSubjectLifting/SWSubjectLiftingView+iOS.swift`
```
//
//  SWSubjectLiftingView.swift
//  ShipSwift
//
//  Demo view showcasing subject lifting (background removal).
//  Provides camera capture and photo library picking, then
//  extracts the primary subject from the selected image.
//
//  Usage:
//    // Present as a full-screen cover or push destination
//    SWSubjectLiftingView()
//
//  Created by Wei Zhong on 3/8/26.
//

import SwiftUI
import PhotosUI

struct SWSubjectLiftingView: View {
    @State private var manager = SWSubjectLiftingManager()

    // Image source
    @State private var showCamera = false
    @State private var selectedPhotoItem: PhotosPickerItem?

    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()

            VStack(spacing: 24) {
                // Result display area
                resultArea
                    .frame(maxWidth: .infinity, maxHeight: .infinity)

                // Action buttons
                actionButtons
                    .padding(.bottom, 32)
            }
            .padding(.horizontal)
        }
        .navigationTitle("Subject Lifting")
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            // Reset button when there's a result
            if manager.extractedImage != nil || manager.originalImage != nil {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Reset") {
                        withAnimation {
                            manager.cleanup()
                        }
                    }
                }
            }
        }
        .fullScreenCover(isPresented: $showCamera) {
            SWCameraView(image: Binding(
                get: { nil },
                set: { image in
                    guard let image else { return }
                    Task { await manager.processImage(image) }
                }
            ))
        }
        .onChange(of: selectedPhotoItem) {
            Task {
                await loadSelectedPhoto()
            }
        }
    }

    // MARK: - Result Area

    @ViewBuilder
    private var resultArea: some View {
        switch manager.processingState {
        case .idle:
            // Empty state — prompt user to pick or capture
            VStack(spacing: 16) {
                Image(systemName: "person.crop.rectangle.badge.plus")
                    .font(.system(size: 56))
                    .foregroundStyle(.secondary)
                Text("Select or capture a photo to extract the subject")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }

        case .processing:
            VStack(spacing: 16) {
                if let original = manager.originalImage {
                    Image(uiImage: original)
                        .resizable()
                        .scaledToFit()
                        .clipShape(RoundedRectangle(cornerRadius: 16))
                        .overlay {
                            RoundedRectangle(cornerRadius: 16)
                                .fill(.black.opacity(0.3))
                        }
                        .overlay {
                            ProgressView()
                                .controlSize(.large)
                                .tint(.white)
                        }
                }
                Text("Extracting subject...")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }

        case .completed:
            VStack(spacing: 16) {
                if let extracted = manager.extractedImage {
                    Image(uiImage: extracted)
                        .resizable()
                        .scaledToFit()
                        .clipShape(RoundedRectangle(cornerRadius: 16))
                        .shadow(color: .black.opacity(0.15), radius: 8, y: 4)
                }
                Text("Subject extracted successfully")
                    .font(.subheadline)
                    .foregroundStyle(.green)
            }

        case .failed:
            VStack(spacing: 16) {
                Image(systemName: "exclamationmark.triangle")
                    .font(.system(size: 48))
                    .foregroundStyle(.orange)
                Text("Could not extract subject")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
    }

    // MARK: - Action Buttons

    private var actionButtons: some View {
        HStack(spacing: 16) {
            // Camera button
            Button {
                showCamera = true
            } label: {
                Label("Camera", systemImage: "camera.fill")
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
            }
            .buttonStyle(.borderedProminent)
            .disabled(manager.processingState == .processing)

            // Photo library picker
            PhotosPicker(selection: $selectedPhotoItem, matching: .images) {
                Label("Library", systemImage: "photo.on.rectangle")
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
            }
            .buttonStyle(.bordered)
            .disabled(manager.processingState == .processing)
        }
    }

    // MARK: - Photo Loading

    private func loadSelectedPhoto() async {
        guard let item = selectedPhotoItem,
              let data = try? await item.loadTransferable(type: Data.self),
              let image = UIImage(data: data) else { return }

        selectedPhotoItem = nil
        await manager.processImage(image)
    }
}

// MARK: - Preview

#Preview {
    NavigationStack {
        SWSubjectLiftingView()
    }
}

```

## File: `ShipSwift/SWPackage/SWModule/SWTikTokTracking/SWTikTokTrackingManager+iOS.swift`
```
//
//  SWTikTokTrackingManager+iOS.swift
//  ShipSwift
//
//  TikTok ad attribution and event tracking manager with ATT permission flow.
//  SDK-agnostic: consumer app injects actual SDK calls via eventHandler closure.
//
//  Prerequisites:
//    Add TikTok Business SDK via SPM in consumer app.
//
//  Usage:
//    // 1. Configure in App init() with event handler:
//    SWTikTokTrackingManager.shared.configure { eventName, properties in
//        let event = TikTokBaseEvent(eventName: eventName)
//        properties?.forEach { event.addProperty(withKey: $0.key, value: $0.value) }
//        TikTokBusiness.trackTTEvent(event)
//    }
//
//    // 2. Request ATT on scenePhase .active:
//    SWTikTokTrackingManager.shared.requestTrackingAuthorization()
//
//    // 3. Track standard events:
//    SWTikTokTrackingManager.shared.track(.subscribe)
//    SWTikTokTrackingManager.shared.track(.viewContent, properties: ["content_type": "report"])
//
//    // 4. Track custom events:
//    SWTikTokTrackingManager.shared.trackCustom("SmileScan")
//

import SwiftUI
import AppTrackingTransparency

// MARK: - Tracking Event Types

/// Standard event types supported by TikTok App Events SDK.
enum SWTikTokTrackingEvent: String, CaseIterable {
    case purchase = "Purchase"
    case subscribe = "Subscribe"
    case viewContent = "ViewContent"
    case completeTutorial = "CompleteTutorial"
    case addToCart = "AddToCart"
    case addPaymentInfo = "AddPaymentInfo"
    case completeRegistration = "CompleteRegistration"
    case search = "Search"
    case startTrial = "StartTrial"
}

// MARK: - ATT Authorization Status

/// Wrapper for AppTrackingTransparency authorization status.
enum SWTikTokTrackingAuthStatus: String {
    case notDetermined = "Not Determined"
    case restricted = "Restricted"
    case denied = "Denied"
    case authorized = "Authorized"

    init(from status: ATTrackingManager.AuthorizationStatus) {
        switch status {
        case .notDetermined: self = .notDetermined
        case .restricted: self = .restricted
        case .denied: self = .denied
        case .authorized: self = .authorized
        @unknown default: self = .notDetermined
        }
    }
}

// MARK: - Tracking Manager

@MainActor
@Observable
final class SWTikTokTrackingManager {

    static let shared = SWTikTokTrackingManager()

    // MARK: - Properties

    /// Current ATT authorization status.
    private(set) var authStatus: SWTikTokTrackingAuthStatus = .notDetermined

    /// Whether the manager has been configured with an event handler.
    private(set) var isConfigured = false

    /// Whether debug logging is enabled.
    private(set) var isDebugMode = false

    // MARK: - Private

    /// Consumer-injected event handler that bridges to the actual tracking SDK.
    private var eventHandler: ((String, [String: String]?) -> Void)?

    private var hasRequestedATT = false

    private init() {
        updateAuthStatus()
    }

    // MARK: - Configuration

    /// Configure tracking with an event handler closure.
    /// The handler bridges to TikTok Business SDK.
    ///
    /// - Parameters:
    ///   - debugMode: Enable verbose logging (default: true in DEBUG builds)
    ///   - eventHandler: Closure that receives event name and optional properties,
    ///                   responsible for calling the actual SDK
    func configure(
        debugMode: Bool? = nil,
        eventHandler: @escaping (String, [String: String]?) -> Void
    ) {
        self.eventHandler = eventHandler
        isConfigured = true

        #if DEBUG
        isDebugMode = debugMode ?? true
        #else
        isDebugMode = debugMode ?? false
        #endif

        debugLog("SWTikTokTrackingManager configured (debug: \(isDebugMode))")
    }

    // MARK: - ATT Permission

    /// Request App Tracking Transparency authorization.
    /// Automatically delays 0.5 second to ensure the app is fully loaded.
    /// Call from scenePhase .active, NOT from App init().
    func requestTrackingAuthorization() {
        guard !hasRequestedATT else { return }
        hasRequestedATT = true

        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) { [weak self] in
            ATTrackingManager.requestTrackingAuthorization { status in
                Task { @MainActor [weak self] in
                    guard let self else { return }
                    self.authStatus = SWTikTokTrackingAuthStatus(from: status)
                    self.debugLog("ATT status: \(self.authStatus.rawValue)")
                    // Reset if not determined (e.g., dialog was blocked by network permission)
                    if status == .notDetermined {
                        self.hasRequestedATT = false
                    }
                }
            }
        }
    }

    // MARK: - Event Tracking

    /// Track a standard event.
    func track(_ event: SWTikTokTrackingEvent, properties: [String: String]? = nil) {
        guard isConfigured else {
            debugLog("SWTikTokTrackingManager not configured. Call configure() first.")
            return
        }

        eventHandler?(event.rawValue, properties)
        debugLog("Track: \(event.rawValue) \(properties ?? [:])")
    }

    /// Track a custom event with an arbitrary name.
    func trackCustom(_ eventName: String, properties: [String: String]? = nil) {
        guard isConfigured else {
            debugLog("SWTikTokTrackingManager not configured. Call configure() first.")
            return
        }

        eventHandler?(eventName, properties)
        debugLog("Track custom: \(eventName) \(properties ?? [:])")
    }

    // MARK: - Status

    /// Refresh the current ATT authorization status.
    func updateAuthStatus() {
        authStatus = SWTikTokTrackingAuthStatus(from: ATTrackingManager.trackingAuthorizationStatus)
    }

    // MARK: - Private

    private func debugLog(_ message: String) {
        #if DEBUG
        if isDebugMode {
            print("[SWTikTokTracking] \(message)")
        }
        #endif
    }
}

```

## File: `ShipSwift/SWPackage/SWModule/SWTikTokTracking/SWTikTokTrackingView+iOS.swift`
```
//
//  SWTikTokTrackingView+iOS.swift
//  ShipSwift
//
//  Informational page for the SWTikTokTracking module.
//  Explains TikTok App Events SDK integration features,
//  setup steps, supported events, and external resources.
//

import SwiftUI

struct SWTikTokTrackingView: View {

    var body: some View {
        List {
            overviewSection
            featuresSection
            integrationStepsSection
            supportedEventsSection
            resourcesSection
        }
        .navigationTitle("TikTok Tracking")
        .toolbarTitleDisplayMode(.inlineLarge)
    }

    // MARK: - Overview

    private var overviewSection: some View {
        Section {
            VStack(alignment: .leading, spacing: 8) {
                Text("Ad Attribution & Conversion Tracking")
                    .font(.subheadline.weight(.semibold))
                Text("Integrate TikTok App Events SDK to measure ad campaign performance, track user conversions, and optimize ad spend with accurate attribution data.")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
            .padding(.vertical, 4)
        } header: {
            Text("Overview")
        }
    }

    // MARK: - Features

    private var featuresSection: some View {
        Section {
            featureRow(icon: "hand.raised.fill", title: "ATT Permission Flow", description: "Built-in App Tracking Transparency request with proper timing")
            featureRow(icon: "chart.bar.fill", title: "Standard Event Tracking", description: "Subscribe, Purchase, ViewContent, and more")
            featureRow(icon: "sparkles", title: "Custom Event Tracking", description: "Track any app-specific event with custom properties")
            featureRow(icon: "arrow.triangle.branch", title: "SKAdNetwork Support", description: "Privacy-preserving attribution via Apple SKAdNetwork")
            featureRow(icon: "ladybug.fill", title: "Debug Mode", description: "Verbose logging for development and testing")
        } header: {
            Text("What You Get")
        }
    }

    // MARK: - Integration Steps

    private var integrationStepsSection: some View {
        Section {
            stepRow(number: 1, text: "Add TikTok Business SDK via Swift Package Manager")
            stepRow(number: 2, text: "Configure credentials in App init()")
            stepRow(number: 3, text: "Request ATT permission on app active")
            stepRow(number: 4, text: "Add event tracking at key touchpoints")
            stepRow(number: 5, text: "Test with TikTok SDK debug mode")
            stepRow(number: 6, text: "Submit to App Store with privacy compliance")
        } header: {
            Text("Integration Steps")
        }
    }

    // MARK: - Supported Events

    private var supportedEventsSection: some View {
        Section {
            ForEach(SWTikTokTrackingEvent.allCases, id: \.rawValue) { event in
                Label(event.rawValue, systemImage: "arrow.right.circle")
            }
        } header: {
            Text("Supported Events")
        } footer: {
            Text("Standard event types supported by TikTok Ads SDK. Custom events can also be tracked with arbitrary names.")
        }
    }

    // MARK: - Resources

    private var resourcesSection: some View {
        Section {
            Link(destination: URL(string: "https://ads.tiktok.com/help/article?aid=10028")!) {
                HStack {
                    Label("TikTok Events Manager", systemImage: "globe")
                    Spacer()
                    Image(systemName: "arrow.up.right")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }

            Link(destination: URL(string: "https://github.com/tiktok/tiktok-business-ios-sdk")!) {
                HStack {
                    Label("TikTok Business SDK (GitHub)", systemImage: "chevron.left.forwardslash.chevron.right")
                    Spacer()
                    Image(systemName: "arrow.up.right")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }
        } header: {
            Text("Resources")
        }
    }

    // MARK: - Row Builders

    private func featureRow(icon: String, title: String, description: String) -> some View {
        HStack(alignment: .top, spacing: 12) {
            Image(systemName: icon)
                .font(.body)
                .foregroundStyle(.tint)
                .frame(width: 24)

            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.subheadline.weight(.medium))
                Text(description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
        }
        .padding(.vertical, 2)
    }

    private func stepRow(number: Int, text: String) -> some View {
        HStack(alignment: .top, spacing: 12) {
            Text("\(number)")
                .font(.caption.weight(.bold))
                .foregroundStyle(.white)
                .frame(width: 22, height: 22)
                .background(Color.accentColor)
                .clipShape(Circle())

            Text(text)
                .font(.subheadline)
        }
        .padding(.vertical, 2)
    }
}

#Preview {
    NavigationStack {
        SWTikTokTrackingView()
    }
}

```

## File: `ShipSwift/SWPackage/SWUtil/SWDateExtension.swift`
```
//
//  SWDateExtension.swift
//  ShipSwift
//
//  Date extension providing English/Chinese date formatting, relative time descriptions,
//  date comparison, date arithmetic, and daily reset helper methods.
//  Language follows the "appLanguage" key in UserDefaults ("en" / "zh-Hans").
//
//  Usage:
//    // Formatted output (automatically adapts to English/Chinese):
//    Date().formatMonth()       // "Jan" or "1月"
//    Date().formatDay()         // "15"
//    Date().formatMonthDay()    // "Jan 15" or "1月15日"
//    Date().formatFullDate()    // "Jan 15, 2025" or "2025年1月15日"
//    Date().formatTime()        // "14:30"
//    Date().formatDateTime()    // "Jan 15, 14:30" or "1月15日 14:30"
//
//    // Relative time:
//    someDate.timeAgo()         // "Just now" / "3 min ago" / "Yesterday" / "Jan 15"
//
//    // Date comparison:
//    date.isToday               // Bool
//    date.isYesterday           // Bool
//    date.isSameDay(as: other)  // Bool
//    date.startOfDay            // Start of the day 00:00:00
//    date.endOfDay              // End of the day 23:59:59
//
//    // Date arithmetic:
//    date.adding(days: 7)       // 7 days later
//    date.adding(months: -1)    // 1 month ago
//    date.days(from: earlier)   // Number of days between two dates
//
//    // Daily reset detection (suitable for check-in / quota scenarios):
//    if Date.shouldResetDaily(dateKey: "lastCheckIn") {
//        resetCounter()
//        Date.updateDailyResetDate(dateKey: "lastCheckIn")
//    }
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation

// MARK: - App Language Helper

private var appLanguage: String {
    UserDefaults.standard.string(forKey: "appLanguage") ?? "en"
}

private var isEnglish: Bool {
    appLanguage == "en"
}

private var currentLocale: Locale {
    Locale(identifier: appLanguage)
}

// MARK: - Date Formatting

extension Date {

    // MARK: - Basic Formatting

    /// Format as month
    /// - Returns: `Jan` / `1月`
    func formatMonth() -> String {
        let formatter = DateFormatter()
        formatter.locale = currentLocale
        formatter.dateFormat = isEnglish ? "MMM" : "M月"
        return formatter.string(from: self)
    }

    /// Format as day
    /// - Returns: `15`
    func formatDay() -> String {
        let formatter = DateFormatter()
        formatter.dateFormat = "d"
        return formatter.string(from: self)
    }

    /// Format as month and day
    /// - Returns: `Jan 15` / `1月15日`
    func formatMonthDay() -> String {
        let formatter = DateFormatter()
        formatter.locale = currentLocale
        formatter.dateFormat = isEnglish ? "MMM d" : "M月d日"
        return formatter.string(from: self)
    }

    /// Format as full date
    /// - Returns: `Jan 15, 2025` / `2025年1月15日`
    func formatFullDate() -> String {
        let formatter = DateFormatter()
        formatter.locale = currentLocale
        formatter.dateFormat = isEnglish ? "MMM d, yyyy" : "yyyy年M月d日"
        return formatter.string(from: self)
    }

    /// Format as time
    /// - Returns: `14:30`
    func formatTime() -> String {
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm"
        return formatter.string(from: self)
    }

    /// Format as date and time
    /// - Returns: `Jan 15, 14:30` / `1月15日 14:30`
    func formatDateTime() -> String {
        "\(formatMonthDay()) \(formatTime())"
    }

    // MARK: - Relative Time

    /// Relative time description
    /// - Returns: `Just now` / `3 min ago` / `2 hours ago` / `Yesterday` / `Jan 15`
    func timeAgo() -> String {
        let now = Date()
        let interval = now.timeIntervalSince(self)

        // Future date
        if interval < 0 {
            return formatMonthDay()
        }

        // Within 1 minute
        if interval < 60 {
            return isEnglish ? "Just now" : "刚刚"
        }

        // Within 1 hour
        if interval < 3600 {
            let minutes = Int(interval / 60)
            return isEnglish ? "\(minutes) min ago" : "\(minutes)分钟前"
        }

        // Within 24 hours
        if interval < 86400 {
            let hours = Int(interval / 3600)
            return isEnglish ? "\(hours) hour\(hours > 1 ? "s" : "") ago" : "\(hours)小时前"
        }

        // Yesterday
        if Calendar.current.isDateInYesterday(self) {
            return isEnglish ? "Yesterday" : "昨天"
        }

        // Within 7 days
        if interval < 604800 {
            let days = Int(interval / 86400)
            return isEnglish ? "\(days) day\(days > 1 ? "s" : "") ago" : "\(days)天前"
        }

        // More than 7 days, show date
        return formatMonthDay()
    }

    // MARK: - Date Comparison

    /// Whether the date is today
    var isToday: Bool {
        Calendar.current.isDateInToday(self)
    }

    /// Whether the date is yesterday
    var isYesterday: Bool {
        Calendar.current.isDateInYesterday(self)
    }

    /// Whether the date is tomorrow
    var isTomorrow: Bool {
        Calendar.current.isDateInTomorrow(self)
    }

    /// Whether this date is the same day as another date
    func isSameDay(as other: Date) -> Bool {
        Calendar.current.isDate(self, inSameDayAs: other)
    }

    /// Get the start of day (00:00:00)
    var startOfDay: Date {
        Calendar.current.startOfDay(for: self)
    }

    /// Get the end of day (23:59:59)
    var endOfDay: Date {
        Calendar.current.date(byAdding: .day, value: 1, to: startOfDay)!.addingTimeInterval(-1)
    }

    // MARK: - Date Arithmetic

    /// Add days
    func adding(days: Int) -> Date {
        Calendar.current.date(byAdding: .day, value: days, to: self) ?? self
    }

    /// Add months
    func adding(months: Int) -> Date {
        Calendar.current.date(byAdding: .month, value: months, to: self) ?? self
    }

    /// Add years
    func adding(years: Int) -> Date {
        Calendar.current.date(byAdding: .year, value: years, to: self) ?? self
    }

    /// Number of days between two dates
    func days(from other: Date) -> Int {
        Calendar.current.dateComponents([.day], from: other.startOfDay, to: self.startOfDay).day ?? 0
    }
}

// MARK: - Daily Reset Helper

extension Date {
    /// Check whether the daily counter needs to be reset
    /// - Parameter key: The key used to store the date in UserDefaults
    /// - Returns: Whether a reset is needed (day has changed)
    static func shouldResetDaily(dateKey: String) -> Bool {
        let today = Date().startOfDay
        let lastDate = UserDefaults.standard.object(forKey: dateKey) as? Date ?? .distantPast
        return !today.isSameDay(as: lastDate)
    }

    /// Update the daily reset date
    /// - Parameter key: The key used to store the date in UserDefaults
    static func updateDailyResetDate(dateKey: String) {
        UserDefaults.standard.set(Date().startOfDay, forKey: dateKey)
    }
}
```

## File: `ShipSwift/SWPackage/SWUtil/SWDebugLog.swift`
```
//
//  SWDebugLog.swift
//  ShipSwift
//
//  Debug logging utility functions that only print in DEBUG mode, with zero overhead
//  in Release builds (#if DEBUG + @inline(__always)). Provides two overloads:
//  simple print and print with file name/line number.
//
//  Usage:
//    // Overload 1 — multi-argument print (similar to print, supports custom separator and terminator):
//    swDebugLog("UserID:", userId, "Status:", status)
//    swDebugLog("A", "B", "C", separator: "-")
//    // Output: A-B-C
//
//    // Overload 2 — print with file name and line number (automatically captures call site):
//    swDebugLog("Network request failed")
//    // Output: [ViewModel.swift:42] Network request failed
//
//    // In Release mode, all swDebugLog calls are completely removed by the compiler with no performance impact.
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation

// MARK: - Debug Logging

/// Prints log messages in Debug mode, completely removed in Release (zero overhead)
@inline(__always)
nonisolated func swDebugLog(_ items: Any..., separator: String = " ", terminator: String = "\n") {
    #if DEBUG
    let output = items.map { "\($0)" }.joined(separator: separator)
    print(output, terminator: terminator)
    #endif
}

/// Prints log messages with file and line info in Debug mode
@inline(__always)
nonisolated func swDebugLog(_ message: @autoclosure () -> String, file: String = #file, line: Int = #line) {
    #if DEBUG
    let filename = (file as NSString).lastPathComponent
    print("[\(filename):\(line)] \(message())")
    #endif
}
```

## File: `ShipSwift/SWPackage/SWUtil/SWLocationManager.swift`
```
//
//  SWLocationManager.swift
//  ShipSwift
//
//  CoreLocation-based location manager (@Observable) that encapsulates authorization
//  requests, location updates, and reverse geocoding. Automatically stops updates after
//  obtaining a location to conserve battery. Results are stored in currentLocation
//  (SWLocationManager.Location).
//
//  Usage:
//    // 1. Initialize (recommended at the App level or in a ViewModel):
//    @State private var locationManager = SWLocationManager()
//
//    // 2. Request location (automatically handles authorization status: requests authorization
//    //    if not determined, starts updates directly if already authorized):
//    locationManager.startLocationServices()
//
//    // 3. Read location results (@Observable drives automatic UI refresh):
//    if let location = locationManager.currentLocation {
//        Text(location.name)                    // City name (reverse geocoding)
//        Text("\(location.latitude), \(location.longitude)")
//        let coord = location.coordinate        // CLLocationCoordinate2D
//    }
//
//    // 4. Check authorization status:
//    locationManager.isAuthorized               // Whether authorized
//    locationManager.isAuthorizationDetermined  // Whether the user has made a choice
//
//    // 5. Guide the user to system Settings (when authorization is denied):
//    locationManager.openSettings()
//
//    // 6. Built-in Location data model (Identifiable, Equatable, Codable):
//    let saved = SWLocationManager.Location(
//        name: "Beijing", latitude: 39.9042, longitude: 116.4074
//    )
//
//  Created by Wei Zhong on 3/1/26.
//

import CoreLocation
#if canImport(UIKit)
import UIKit
#elseif canImport(AppKit)
import AppKit
#endif

@MainActor
@Observable
final class SWLocationManager: NSObject {

    // MARK: - Built-in Data Model

    /// Location info model
    struct Location: Identifiable, Equatable, Codable {
        let id: UUID
        let name: String
        let latitude: Double
        let longitude: Double

        init(id: UUID = UUID(), name: String, latitude: Double, longitude: Double) {
            self.id = id
            self.name = name
            self.latitude = latitude
            self.longitude = longitude
        }

        /// Convert to CLLocationCoordinate2D
        var coordinate: CLLocationCoordinate2D {
            CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
        }

        /// Convert to CLLocation
        var clLocation: CLLocation {
            CLLocation(latitude: latitude, longitude: longitude)
        }
    }

    // MARK: - Properties

    private(set) var userLocation: CLLocation?
    private(set) var currentLocation: Location?
    private(set) var isAuthorized = false

    var isAuthorizationDetermined: Bool {
        manager.authorizationStatus != .notDetermined
    }

    @ObservationIgnored
    private let manager = CLLocationManager()

    @ObservationIgnored
    private let geocoder = CLGeocoder()

    #if os(iOS)
    private static let authorizedStatuses: Set<CLAuthorizationStatus> = [.authorizedAlways, .authorizedWhenInUse]
    #else
    private static let authorizedStatuses: Set<CLAuthorizationStatus> = [.authorizedAlways]
    #endif

    // MARK: - Initialization

    override init() {
        super.init()
        manager.delegate = self
        updateAuthorizationStatus()
    }

    // MARK: - Public Methods

    func startLocationServices() {
        userLocation = nil
        currentLocation = nil
        updateAuthorizationStatus()

        if isAuthorized {
            manager.startUpdatingLocation()
        } else if manager.authorizationStatus == .notDetermined {
            manager.requestWhenInUseAuthorization()
        }
    }

    func openSettings() {
        #if os(iOS)
        guard let url = URL(string: UIApplication.openSettingsURLString) else { return }
        UIApplication.shared.open(url)
        #elseif os(macOS)
        NSWorkspace.shared.open(URL(string: "x-apple.systempreferences:")!)
        #endif
    }

    // MARK: - Private Methods

    private func updateAuthorizationStatus() {
        isAuthorized = Self.authorizedStatuses.contains(manager.authorizationStatus)
    }

    private func resolveLocationName(for location: CLLocation) async -> String {
        let placemarks = try? await geocoder.reverseGeocodeLocation(location)
        return placemarks?.first?.locality ?? ""
    }
}

// MARK: - CLLocationManagerDelegate

extension SWLocationManager: CLLocationManagerDelegate {

    nonisolated func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }

        Task { @MainActor in
            userLocation = location
            let name = await resolveLocationName(for: location)
            currentLocation = Location(
                name: name,
                latitude: location.coordinate.latitude,
                longitude: location.coordinate.longitude
            )
            manager.stopUpdatingLocation()
        }
    }

    nonisolated func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        Task { @MainActor in
            updateAuthorizationStatus()
            if isAuthorized {
                manager.startUpdatingLocation()
            }
        }
    }

    nonisolated func locationManager(_ manager: CLLocationManager, didFailWithError error: any Error) {
        // Silently handle errors
    }
}
```

## File: `ShipSwift/SWPackage/SWUtil/SWStringExtension.swift`
```
//
//  SWStringExtension.swift
//  ShipSwift
//
//  String extension providing computed properties for email and phone number format validation.
//
//  Usage:
//    // Email validation — matches standard email format (user@domain.tld):
//    "hello@example.com".isValidEmail   // true
//    "not-an-email".isValidEmail        // false
//
//    // Phone number validation — digits only, 8-15 characters (supports international numbers):
//    "13800138000".isValidPhone         // true
//    "123".isValidPhone                 // false (fewer than 8 digits)
//    "+1-555-1234".isValidPhone         // false (contains non-digit characters)
//
//    // Common usage — validate before form submission:
//    Button("Submit") { submit() }
//        .disabled(!email.isValidEmail || !phone.isValidPhone)
//
//  Created by Wei Zhong on 3/1/26.
//

import Foundation

extension String {
    /// Validate email format
    var isValidEmail: Bool {
        let emailRegex = #"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"#
        return range(of: emailRegex, options: .regularExpression) != nil
    }

    /// Validate phone number format (8-15 digits, international)
    var isValidPhone: Bool {
        let phoneRegex = #"^\d{8,15}$"#
        return range(of: phoneRegex, options: .regularExpression) != nil
    }
}
```

## File: `ShipSwift/SWPackage/SWUtil/SWViewExtension.swift`
```
//
//  SWViewExtension.swift
//  ShipSwift
//
//  SwiftUI view extensions including SWButtonStyle (primary/secondary button styles) and
//  the swCardStyle card modifier. Button styles are full-width rounded rectangles with
//  automatic pressed/disabled state handling; card style features a gradient stroke.
//
//  Usage:
//    // Primary button (accent background + white text, for confirm/save main actions):
//    Button("Save") { save() }
//        .buttonStyle(.swPrimary)
//
//    // Secondary button (light background, for cancel/close secondary actions):
//    Button("Cancel") { dismiss() }
//        .buttonStyle(.swSecondary)
//
//    // Custom border and corner radius:
//    Button("Submit") { submit() }
//        .buttonStyle(.swPrimary(showBorder: true, cornerRadius: 12))
//
//    // Card style modifier (gradient stroke + translucent background):
//    VStack { content }
//        .swCardStyle()
//
//    // Custom card parameters:
//    VStack { content }
//        .swCardStyle(strokeColor: .cyan, cornerRadius: 24, padding: 24, strokeWidth: 1.0)
//
//  Created by Wei Zhong on 3/1/26.
//

import SwiftUI

// MARK: - Button Style

struct SWButtonStyle: ButtonStyle {
    enum Variant {
        case primary
        case secondary
    }

    @Environment(\.isEnabled) private var isEnabled

    let variant: Variant
    var showBorder: Bool = false
    var cornerRadius: CGFloat = 16

    private var backgroundColor: Color {
        switch variant {
        case .primary: .accent
        case .secondary: .accent.opacity(0.1)
        }
    }

    private var foregroundColor: Color {
        switch variant {
        case .primary: .white
        case .secondary: .primary.opacity(0.8)
        }
    }

    private var borderColor: Color {
        switch variant {
        case .primary: .primary
        case .secondary: .secondary.opacity(0.8)
        }
    }

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .frame(maxWidth: .infinity)
            .padding()
            .background(
                RoundedRectangle(cornerRadius: cornerRadius)
                    .fill(backgroundColor)
            )
            .foregroundStyle(foregroundColor)
            .overlay(
                RoundedRectangle(cornerRadius: cornerRadius)
                    .strokeBorder(
                        showBorder ? borderColor : .clear,
                        lineWidth: 1.5
                    )
            )
            .contentShape(RoundedRectangle(cornerRadius: cornerRadius))
            .opacity(isEnabled ? (configuration.isPressed ? 0.7 : 1) : 0.5)
    }
}

extension ButtonStyle where Self == SWButtonStyle {
    /// Primary button style (confirm / save, etc.)
    static var swPrimary: SWButtonStyle { .init(variant: .primary) }
    /// Secondary button style (cancel / close, etc.)
    static var swSecondary: SWButtonStyle { .init(variant: .secondary) }

    static func swPrimary(showBorder: Bool = true, cornerRadius: CGFloat = 12) -> SWButtonStyle {
        .init(variant: .primary, showBorder: showBorder, cornerRadius: cornerRadius)
    }

    static func swSecondary(showBorder: Bool = true, cornerRadius: CGFloat = 12) -> SWButtonStyle {
        .init(variant: .secondary, showBorder: showBorder, cornerRadius: cornerRadius)
    }
}

// MARK: - Card Style
// Usage:
//   Text("Content").swCardStyle()
//   Text("Content").swCardStyle(strokeColor: .cyan, cornerRadius: 20)

extension View {
    /// Card style modifier
    /// - Parameters:
    ///   - strokeColor: Starting color for the border gradient
    ///   - background: Background color
    ///   - cornerRadius: Corner radius
    ///   - padding: Inner padding
    ///   - strokeWidth: Border width
    func swCardStyle(
        strokeColor: Color = .accentColor,
        background: Color = .white.opacity(0.1),
        cornerRadius: CGFloat = 16,
        padding: CGFloat = 16,
        strokeWidth: CGFloat = 0.6
    ) -> some View {
        self
            .padding(padding)
            .background(background)
            .clipShape(RoundedRectangle(cornerRadius: cornerRadius))
            .overlay(
                RoundedRectangle(cornerRadius: cornerRadius)
                    .strokeBorder(
                        LinearGradient(
                            colors: [
                                strokeColor,
                                strokeColor.opacity(0.6),
                                strokeColor.opacity(0.3),
                                .clear
                            ],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        ),
                        lineWidth: strokeWidth
                    )
            )
    }
}

// MARK: - Preview

#Preview("Button Styles") {
    VStack(spacing: 20) {
        Button("Primary Button") { }
            .buttonStyle(.swPrimary)

        Button("Secondary Button") { }
            .buttonStyle(.swSecondary)

        Button("Disabled") { }
            .buttonStyle(.swPrimary)
            .disabled(true)
    }
    .padding()
}

#Preview("Card Styles") {
    VStack(spacing: 20) {
        VStack {
            ForEach(0..<3, id: \.self) { _ in
                Text("Default Card")
            }
        }
        .frame(maxWidth: .infinity)
        .swCardStyle()

        VStack {
            ForEach(0..<3, id: \.self) { _ in
                Text("Custom Card")
            }
        }
        .frame(maxWidth: .infinity)
        .swCardStyle(strokeColor: .cyan, cornerRadius: 24, padding: 24)
    }
    .padding()
}
```

## File: `ShipSwift/Service/ChatService.swift`
```
//
//  ChatService.swift
//  ShipSwift
//
//  Handles communication with the ShipSwift Chat API backend.
//  Sends user messages and receives AI responses with optional component IDs.
//
//  Created by Wei Zhong on 18/2/26.
//

#if os(iOS)

import Foundation

// MARK: - Chat Response Model

/// Response from the POST /api/chat endpoint.
struct ChatResponse: Decodable {
    let reply: String
    let component: String?
}

// MARK: - Chat Service

/// Communicates with the ShipSwift backend chat API.
///
/// The backend proxies requests to OpenAI GPT and returns a text reply
/// along with an optional component ID when a matching SwiftUI component is found.
struct ChatService {
    private let endpoint = URL(string: "https://api.shipswift.app/api/chat")!

    /// Build the history array for the API request from existing messages.
    private func buildHistory(from messages: [ChatMessage]) -> [[String: String]] {
        messages.compactMap { message in
            // Skip component preview messages (they add no meaningful context for LLM)
            if message.componentId != nil { return nil }
            return [
                "role": message.isUser ? "user" : "assistant",
                "content": message.content
            ]
        }
    }

    /// Send a message to the chat API and return the response.
    /// - Parameters:
    ///   - message: The user's message text
    ///   - history: Previous messages for context
    /// - Returns: ChatResponse with reply text and optional component ID
    func send(message: String, history: [ChatMessage]) async -> ChatResponse {
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.timeoutInterval = 30

        let body: [String: Any] = [
            "message": message,
            "history": buildHistory(from: history)
        ]

        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: body)
            let (data, response) = try await URLSession.shared.data(for: request)

            guard let httpResponse = response as? HTTPURLResponse,
                  (200...299).contains(httpResponse.statusCode) else {
                return ChatResponse(
                    reply: "Sorry, I couldn't reach the server. Please try again later.",
                    component: nil
                )
            }

            return try JSONDecoder().decode(ChatResponse.self, from: data)
        } catch {
            swDebugLog("[ChatService] Error: \(error.localizedDescription)")
            return ChatResponse(
                reply: "Something went wrong. Please try again.",
                component: nil
            )
        }
    }
}

#endif
```

## File: `ShipSwift/Service/ComponentRegistry.swift`
```
//
//  ComponentRegistry.swift
//  ShipSwift
//
//  Maps component IDs to SwiftUI views for chat-inline previews
//  and full-screen demos. Used by ChatView to render real components
//  inside chat bubbles when the AI recommends a component.
//
//  Created by Wei Zhong on 18/2/26.
//

import SwiftUI
import Charts

// MARK: - Component Entry

/// Metadata and view factories for a single registered component.
struct ComponentEntry {
    let title: String
    let icon: String
    let description: String
    /// Compact preview for chat bubble (max width ~280pt, max height ~300pt)
    let preview: () -> AnyView
    /// Full demo view for fullscreen/sheet presentation
    let fullView: () -> AnyView
    /// Presentation style for the full view
    let presentation: ComponentPresentation
}

/// How the full view should be presented.
enum ComponentPresentation {
    case push
    case sheet
    case fullScreenCover
}

// MARK: - Component Registry

/// Central registry mapping component IDs to SwiftUI views.
///
/// Provides three lookups:
/// - `view(for:)` — compact preview for chat bubble embedding
/// - `fullView(for:)` — full demo view for expanded presentation
/// - `title(for:)` — display name
struct ComponentRegistry {

    /// All registered components keyed by ID.
    let entries: [String: ComponentEntry] = Self.buildRegistry()

    /// Compact preview view for embedding in a chat bubble.
    func view(for id: String) -> AnyView? {
        entries[id]?.preview()
    }

    /// Full demo view for expanded presentation.
    func fullView(for id: String) -> AnyView? {
        entries[id]?.fullView()
    }

    /// Display title for a component.
    func title(for id: String) -> String {
        entries[id]?.title ?? id
    }

    /// Presentation style for the full view.
    func presentation(for id: String) -> ComponentPresentation {
        entries[id]?.presentation ?? .push
    }

    /// Icon SF Symbol name.
    func icon(for id: String) -> String {
        entries[id]?.icon ?? "square.grid.2x2"
    }

    /// Short description.
    func description(for id: String) -> String {
        entries[id]?.description ?? ""
    }

    // MARK: - Registry Builder

    private static func buildRegistry() -> [String: ComponentEntry] {
        var reg: [String: ComponentEntry] = [:]

        // -- Module (7) --

        reg["auth"] = ComponentEntry(
            title: "Auth",
            icon: "person.badge.key.fill",
            description: "Complete auth flow with email, phone, Apple & Google sign-in",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "person.badge.key.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Auth Module")
                            .font(.headline)
                        Text("Email / Phone / Apple / Google sign-in with verification flow")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(NavigationStack { ComponentDemoViews.authDemo() }) },
            presentation: .fullScreenCover
        )

        reg["camera"] = ComponentEntry(
            title: "Camera",
            icon: "camera.fill",
            description: "Full camera capture with viewfinder overlay, zoom, and photo picker",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "camera.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Camera Module")
                            .font(.headline)
                        Text("Viewfinder overlay, pinch-to-zoom, photo library picker")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(ComponentDemoViews.cameraDemo().swAlert()) },
            presentation: .fullScreenCover
        )

        reg["face-camera"] = ComponentEntry(
            title: "Face Camera",
            icon: "face.smiling.inverse",
            description: "Camera with real-time Vision face landmark detection",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "face.smiling.inverse")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Face Camera")
                            .font(.headline)
                        Text("Vision face landmark detection with front/back switching")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(ComponentDemoViews.faceCameraDemo()) },
            presentation: .fullScreenCover
        )

        reg["paywall"] = ComponentEntry(
            title: "Paywall",
            icon: "creditcard.fill",
            description: "Pro paywall with lifetime purchase, feature list, and restore purchases",
            preview: {
                AnyView(
                    VStack(spacing: 8) {
                        Image(.shipSwiftLogo)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 40, height: 40)
                            .clipShape(RoundedRectangle(cornerRadius: 8))
                        Text("ShipSwift Pro")
                            .font(.headline)
                        Text("One-time purchase")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                        HStack(spacing: 6) {
                            Image(systemName: "checkmark.seal.fill")
                                .foregroundStyle(.accent)
                                .imageScale(.small)
                            Text("Full-stack iOS + AWS backend")
                                .font(.caption)
                        }
                        HStack(spacing: 6) {
                            Image(systemName: "terminal.fill")
                                .foregroundStyle(.accent)
                                .imageScale(.small)
                            Text("One MCP command, instant access")
                                .font(.caption)
                        }
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(ComponentDemoViews.paywallDemo()) },
            presentation: .sheet
        )

        reg["chat"] = ComponentEntry(
            title: "Chat",
            icon: "bubble.left.and.bubble.right.fill",
            description: "Chat interface with message bubbles and text input",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "bubble.left.and.bubble.right.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Chat Module")
                            .font(.headline)
                        Text("Message bubbles, text input, voice recording waveform")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(NavigationStack { ComponentDemoViews.chatDemo() }) },
            presentation: .fullScreenCover
        )

        reg["setting"] = ComponentEntry(
            title: "Setting",
            icon: "gearshape.fill",
            description: "Generic settings page with language switch, share, and legal links",
            preview: {
                AnyView(
                    VStack(spacing: 8) {
                        ForEach(["Language", "Share App", "Privacy Policy"], id: \.self) { item in
                            HStack {
                                Text(item)
                                    .font(.subheadline)
                                Spacer()
                                Image(systemName: "chevron.right")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                            .padding(.horizontal)
                            if item != "Privacy Policy" { Divider() }
                        }
                    }
                    .padding(.vertical, 8)
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(SWSettingView(isDemo: true)) },
            presentation: .push
        )

        reg["tiktok-tracking"] = ComponentEntry(
            title: "TikTok Tracking",
            icon: "chart.bar.xaxis.ascending",
            description: "TikTok App Events SDK with ATT permission flow and event tracking for ad attribution",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "chart.bar.xaxis.ascending")
                            .font(.system(size: 36))
                            .foregroundStyle(.blue)
                        Text("Ad Tracking")
                            .font(.headline)
                        Text("ATT permission + event tracking for ad attribution")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(ComponentDemoViews.tiktokTrackingDemo()) },
            presentation: .push
        )

        reg["subject-lifting"] = ComponentEntry(
            title: "Subject Lifting",
            icon: "person.crop.rectangle.badge.minus",
            description: "Background removal using VisionKit — extract the primary subject from any photo",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "person.crop.rectangle.badge.minus")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Subject Lifting")
                            .font(.headline)
                        Text("Extract subject with background removed via VisionKit")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(ComponentDemoViews.subjectLiftingDemo()) },
            presentation: .fullScreenCover
        )

        // -- Animation (9) --

        reg["before-after-slider"] = ComponentEntry(
            title: "Before / After Slider",
            icon: "slider.horizontal.below.rectangle",
            description: "Draggable image comparison slider with auto-oscillation",
            preview: {
                AnyView(
                    SWBeforeAfterSlider(
                        before: Image(.smileBefore),
                        after: Image(.smileAfter)
                    )
                    .scaledToFit()
                    .frame(maxWidth: 200, maxHeight: 200)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                )
            },
            fullView: {
                AnyView(
                    SWBeforeAfterSlider(
                        before: Image(.smileBefore),
                        after: Image(.smileAfter)
                    )
                    .padding()
                )
            },
            presentation: .push
        )

        reg["typewriter-text"] = ComponentEntry(
            title: "Typewriter Text",
            icon: "character.cursor.ibeam",
            description: "Typing and deleting text animation with multiple styles",
            preview: {
                AnyView(
                    SWTypewriterText(
                        texts: ["Level up your smile game", "AI-powered smile analysis"],
                        animationStyle: .spring
                    )
                    .font(.headline)
                    .frame(height: 40)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.black)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 26) {
                        SWTypewriterText(
                            texts: ["Level up your smile game", "AI-powered smile analysis", "Join the glow up era"],
                            animationStyle: .spring
                        )
                        .font(.title3.weight(.semibold))
                        SWTypewriterText(
                            texts: ["Hello World", "Welcome Back", "Let's Go"],
                            animationStyle: .spring,
                            gradient: LinearGradient(colors: [.pink, .orange], startPoint: .leading, endPoint: .trailing)
                        )
                        .font(.title.weight(.bold))
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .background(Color.black)
                )
            },
            presentation: .push
        )

        reg["shaking-icon"] = ComponentEntry(
            title: "Shaking Icon",
            icon: "iphone.radiowaves.left.and.right",
            description: "Periodically zooms in and shakes, mimicking iOS jiggle effect",
            preview: {
                AnyView(
                    SWShakingIcon(image: Image(.shipSwiftLogo), height: 60, cornerRadius: 8)
                        .frame(maxWidth: .infinity)
                        .padding()
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 40) {
                        SWShakingIcon(image: Image(systemName: "apple.logo"), height: 20)
                        SWShakingIcon(image: Image(.smileAfter), height: 100, cornerRadius: 8)
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["shimmer"] = ComponentEntry(
            title: "Shimmer",
            icon: "light.max",
            description: "Translucent light band sweep for buttons and skeleton loaders",
            preview: {
                AnyView(
                    SWShimmer {
                        RoundedRectangle(cornerRadius: 12)
                            .fill(.gray.opacity(0.3))
                            .frame(height: 60)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 30) {
                        SWShimmer {
                            Button {} label: {
                                Text("Upgrade Now")
                                    .font(.largeTitle)
                                    .padding(.horizontal)
                                    .padding(.vertical, 6)
                            }
                            .buttonStyle(.borderedProminent)
                        }
                        SWShimmer {
                            RoundedRectangle(cornerRadius: 12)
                                .fill(.gray.opacity(0.3))
                                .frame(width: 280, height: 120)
                        }
                    }
                    .padding()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["glow-sweep"] = ComponentEntry(
            title: "Glow Sweep",
            icon: "wand.and.rays",
            description: "Sweeps a glowing highlight using content shape as mask",
            preview: {
                AnyView(
                    SWGlowSweep {
                        Text("Start Scan Today")
                            .font(.title2.bold())
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 26) {
                        SWGlowSweep {
                            Text("Start Scan Today")
                                .font(.largeTitle.bold())
                        }
                        SWGlowSweep(baseColor: .accentColor, glowColor: .white, duration: 1.5) {
                            Text("Analyzing...")
                                .font(.title2.bold())
                        }
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["light-sweep"] = ComponentEntry(
            title: "Light Sweep",
            icon: "light.beacon.max",
            description: "Gradient light band that sweeps across content",
            preview: {
                AnyView(
                    SWLightSweep {
                        Image(.smileAfter)
                            .resizable()
                            .scaledToFit()
                            .frame(height: 120)
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 26) {
                        SWLightSweep {
                            Image(.smileAfter)
                                .resizable()
                                .scaledToFit()
                                .frame(width: 180)
                        }
                        SWLightSweep(lineWidth: 120, duration: 0.5, cornerRadius: 20) {
                            Image(.smileAfter)
                                .resizable()
                                .scaledToFit()
                                .frame(width: 200)
                        }
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["scanning-overlay"] = ComponentEntry(
            title: "Scanning Overlay",
            icon: "barcode.viewfinder",
            description: "Grid lines, sweep band, and noise layer overlay",
            preview: {
                AnyView(
                    SWScanningOverlay {
                        Image(.facePicture)
                            .resizable()
                            .scaledToFit()
                            .frame(height: 140)
                            .clipShape(RoundedRectangle(cornerRadius: 12))
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 20) {
                        SWScanningOverlay {
                            Image(.facePicture)
                                .resizable()
                                .scaledToFit()
                                .frame(width: 180)
                                .clipShape(RoundedRectangle(cornerRadius: 12))
                        }
                    }
                    .padding()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["animated-mesh-gradient"] = ComponentEntry(
            title: "Animated Mesh Gradient",
            icon: "circle.hexagongrid.fill",
            description: "3x3 mesh gradient background with color palette transitions",
            preview: {
                AnyView(
                    SWAnimatedMeshGradient()
                        .frame(height: 150)
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                )
            },
            fullView: {
                AnyView(
                    SWAnimatedMeshGradient()
                        .ignoresSafeArea()
                )
            },
            presentation: .push
        )

        reg["orbiting-logos"] = ComponentEntry(
            title: "Orbiting Logos",
            icon: "atom",
            description: "SpriteKit-powered concentric rings with orbiting icons",
            preview: {
                AnyView(
                    SWOrbitingLogos(
                        images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
                    ) {
                        Image(.fullpackLogo)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 40, height: 40)
                            .clipShape(RoundedRectangle(cornerRadius: 6))
                            .offset(y: -3)
                    }
                    .frame(height: 200)
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    VStack {
                        SWOrbitingLogos(
                            images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
                        ) {
                            Image(.fullpackLogo)
                                .resizable()
                                .scaledToFit()
                                .frame(width: 60, height: 60)
                                .clipShape(RoundedRectangle(cornerRadius: 8))
                                .offset(y: -5)
                        }
                    }
                )
            },
            presentation: .push
        )

        // -- Chart (8) --

        reg["line-chart"] = ComponentEntry(
            title: "Line Chart",
            icon: "chart.xyaxis.line",
            description: "Multi-series line chart with scrolling and reference lines",
            preview: { AnyView(ChartPreviews.lineChart) },
            fullView: { AnyView(ChartPreviews.lineChartFull) },
            presentation: .push
        )

        reg["bar-chart"] = ComponentEntry(
            title: "Bar Chart",
            icon: "chart.bar.fill",
            description: "Grouped or stacked bar chart with horizontal scrolling",
            preview: { AnyView(ChartPreviews.barChart) },
            fullView: { AnyView(ChartPreviews.barChartFull) },
            presentation: .push
        )

        reg["area-chart"] = ComponentEntry(
            title: "Area Chart",
            icon: "chart.line.uptrend.xyaxis",
            description: "Standard or stacked area chart with smooth interpolation",
            preview: { AnyView(ChartPreviews.areaChart) },
            fullView: { AnyView(ChartPreviews.areaChartFull) },
            presentation: .push
        )

        reg["scatter-chart"] = ComponentEntry(
            title: "Scatter Chart",
            icon: "chart.dots.scatter",
            description: "Scrollable scatter chart with generic category types",
            preview: { AnyView(ChartPreviews.scatterChart) },
            fullView: { AnyView(ChartPreviews.scatterChartFull) },
            presentation: .push
        )

        reg["donut-chart"] = ComponentEntry(
            title: "Donut Chart",
            icon: "chart.pie.fill",
            description: "Interactive donut chart with tap-to-select categories",
            preview: { AnyView(ChartPreviews.donutChart) },
            fullView: { AnyView(ChartPreviews.donutChartFull) },
            presentation: .push
        )

        reg["radar-chart"] = ComponentEntry(
            title: "Radar Chart",
            icon: "pentagon",
            description: "Animated radar chart with axis labels and grid rings",
            preview: { AnyView(ChartPreviews.radarChart) },
            fullView: { AnyView(ChartPreviews.radarChartFull) },
            presentation: .push
        )

        reg["ring-chart"] = ComponentEntry(
            title: "Ring Chart",
            icon: "circle.circle",
            description: "Activity Rings style concentric ring progress chart",
            preview: { AnyView(ChartPreviews.ringChart) },
            fullView: { AnyView(ChartPreviews.ringChartFull) },
            presentation: .push
        )

        reg["activity-heatmap"] = ComponentEntry(
            title: "Activity Heatmap",
            icon: "square.grid.3x3.fill",
            description: "GitHub-style activity heatmap with streak tracking",
            preview: { AnyView(ChartPreviews.activityHeatmap) },
            fullView: { AnyView(ChartPreviews.activityHeatmapFull) },
            presentation: .push
        )

        // -- Display (9) --

        reg["floating-labels"] = ComponentEntry(
            title: "Floating Labels",
            icon: "tag.fill",
            description: "Animated floating capsule labels over an image",
            preview: {
                AnyView(
                    SWFloatingLabels(
                        image: Image(.facePicture),
                        labels: [
                            .init(text: "Teeth mapping", position: CGPoint(x: 0.3, y: 0.5)),
                            .init(text: "Plaque detection", position: CGPoint(x: 0.9, y: 0.6)),
                        ]
                    )
                    .frame(height: 200)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                )
            },
            fullView: {
                AnyView(
                    SWFloatingLabels(
                        image: Image(.facePicture),
                        labels: [
                            .init(text: "Teeth mapping", position: CGPoint(x: 0.3, y: 0.5)),
                            .init(text: "Plaque detection", position: CGPoint(x: 0.9, y: 0.6)),
                            .init(text: "Shape & balance", position: CGPoint(x: 0.5, y: 0.8)),
                        ]
                    )
                )
            },
            presentation: .push
        )

        #if os(iOS)
        reg["scrolling-faq"] = ComponentEntry(
            title: "Scrolling FAQ",
            icon: "bubble.left.and.text.bubble.right",
            description: "Auto-scrolling horizontal FAQ carousel",
            preview: {
                AnyView(
                    SWScrollingFAQ(
                        rows: [
                            ["How does AI work?", "What can I ask?", "How accurate?"],
                            ["Write an email", "Summarize article", "Translate text"],
                        ],
                        title: "Let's talk"
                    ) { _ in }
                    .frame(height: 200)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                )
            },
            fullView: {
                AnyView(
                    SWScrollingFAQ(
                        rows: [
                            ["How does AI work?", "What can I ask?", "How accurate?", "Help with coding?",
                             "Remember chat?", "Languages supported?", "Get started?", "Explain topics?"],
                            ["Write an email", "Summarize article", "Translate text", "Creative ideas",
                             "Debug code", "Explain concept", "Meal plan", "Brainstorm"],
                        ],
                        title: "Let's talk about new topics"
                    ) { _ in }
                )
            },
            presentation: .push
        )
        #endif

        reg["rotating-quote"] = ComponentEntry(
            title: "Rotating Quote",
            icon: "text.quote",
            description: "Auto-rotating quote display with author attribution",
            preview: {
                AnyView(
                    SWRotatingQuote(
                        quotes: [
                            "Stay hungry, stay foolish.",
                            "The only way to do great work is to love what you do."
                        ],
                        author: "Steve Jobs"
                    )
                    .frame(height: 100)
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    ScrollView {
                        VStack(spacing: 32) {
                            SWRotatingQuote(
                                quotes: [
                                    "Stay hungry, stay foolish.",
                                    "The only way to do great work is to love what you do.",
                                    "Innovation distinguishes between a leader and a follower."
                                ],
                                author: "Steve Jobs"
                            )
                            .frame(height: 140)
                        }
                        .padding()
                    }
                )
            },
            presentation: .push
        )

        reg["bullet-point-text"] = ComponentEntry(
            title: "Bullet Point Text",
            icon: "list.bullet",
            description: "Colored capsule bullet indicator with custom content",
            preview: {
                AnyView(
                    VStack(alignment: .leading, spacing: 8) {
                        SWBulletPointText(bulletColor: .blue) { Text("Wealth") }
                        SWBulletPointText(bulletColor: .green) { Text("Health") }
                        SWBulletPointText(bulletColor: .orange) { Text("Happiness") }
                    }
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                )
            },
            fullView: {
                AnyView(
                    ScrollView {
                        VStack(alignment: .leading, spacing: 10) {
                            SWBulletPointText(bulletColor: .blue) { Text("Wealth") }
                            SWBulletPointText(bulletColor: .green) { Text("Health") }
                            SWBulletPointText(bulletColor: .orange) { Text("Happiness") }
                            SWBulletPointText(bulletColor: .purple) { Text("Wisdom") }
                        }
                        .padding()
                    }
                )
            },
            presentation: .push
        )

        reg["gradient-divider"] = ComponentEntry(
            title: "Gradient Divider",
            icon: "minus",
            description: "Gradient divider with configurable color and opacity",
            preview: {
                AnyView(
                    VStack(spacing: 16) {
                        SWGradientDivider()
                        SWGradientDivider(color: .purple, opacity: 0.5)
                        SWGradientDivider(color: .mint, height: 2)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 20) {
                        SWGradientDivider()
                        SWGradientDivider(color: .purple, opacity: 0.5)
                        SWGradientDivider(color: .mint, height: 2)
                    }
                    .padding()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        reg["label"] = ComponentEntry(
            title: "Label",
            icon: "tag",
            description: "Reusable label components with icon and image variants",
            preview: {
                AnyView(
                    VStack(alignment: .leading, spacing: 6) {
                        SWLabelWithIcon()
                        SWLabelWithIcon(icon: "gearshape", bg: .orange, name: "Settings")
                        SWLabelWithIcon(icon: "bell.badge", bg: .red, name: "Notifications")
                    }
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                )
            },
            fullView: {
                AnyView(
                    VStack(alignment: .leading, spacing: 8) {
                        SWLabelWithIcon()
                        SWLabelWithIcon(icon: "gearshape", bg: .orange, name: "Settings")
                        SWLabelWithIcon(icon: "bell.badge", bg: .red, name: "Notifications")
                        SWLabelWithIcon(icon: "lock.shield", bg: .green, name: "Privacy")
                        SWLabelWithIcon(icon: "creditcard", bg: .purple, name: "Subscription")
                    }
                    .padding()
                    .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .leading)
                )
            },
            presentation: .push
        )

        reg["onboarding-view"] = ComponentEntry(
            title: "Onboarding",
            icon: "hand.wave.fill",
            description: "Multi-page welcome flow with swipe navigation and skip",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "hand.wave.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Onboarding View")
                            .font(.headline)
                        Text("Multi-page swipe flow with skip support")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(OnboardingDemoWrapper()) },
            presentation: .fullScreenCover
        )

        reg["order-view"] = ComponentEntry(
            title: "Order",
            icon: "cup.and.saucer.fill",
            description: "Animated drink customization demo with flavor/size selectors",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "cup.and.saucer.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.brown)
                        Text("Order View")
                            .font(.headline)
                        Text("Animated drink customization with cup animations")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(OrderDemoWrapper()) },
            presentation: .fullScreenCover
        )

        reg["root-tab-view"] = ComponentEntry(
            title: "Tab",
            icon: "rectangle.split.3x1.fill",
            description: "TabView template with selected/unselected icons",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "rectangle.split.3x1.fill")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Tab View Template")
                            .font(.headline)
                        Text("iOS 18+ TabView with haptic feedback")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(SWRootTabView()) },
            presentation: .sheet
        )

        reg["markdown-text"] = ComponentEntry(
            title: "Markdown Text",
            icon: "text.badge.checkmark",
            description: "Custom Markdown renderer for headings, bold/italic, code blocks, lists, and dividers",
            preview: {
                AnyView(
                    SWMarkdownText("""
                    ## Quick Demo
                    A paragraph with **bold** and *italic*.

                    - Bullet one
                    - Bullet two

                    ```swift
                    print("Hello!")
                    ```
                    """)
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                )
            },
            fullView: {
                AnyView(
                    ScrollView {
                        SWMarkdownText("""
                        # Heading 1
                        ## Heading 2
                        ### Heading 3

                        This is a paragraph with **bold** and *italic* text.

                        Here is `inline code` in a sentence.

                        ```swift
                        func greet() {
                            print("Hello, world!")
                        }
                        ```

                        - First item
                        - Second item with **bold**
                        - Third item

                        1. Ordered item one
                        2. Ordered item two

                        ---

                        Another paragraph after the divider.
                        """)
                        .padding()
                    }
                )
            },
            presentation: .push
        )

        // -- Feedback (3) --

        reg["alert"] = ComponentEntry(
            title: "SWAlert",
            icon: "bell.badge",
            description: "Toast-style alert with four presets and custom styling",
            preview: {
                AnyView(
                    VStack(spacing: 8) {
                        ForEach(["Info", "Success", "Warning", "Error"], id: \.self) { type in
                            Text(type)
                                .font(.caption)
                                .padding(.horizontal, 12)
                                .padding(.vertical, 4)
                                .background(alertColor(for: type).opacity(0.15))
                                .foregroundStyle(alertColor(for: type))
                                .clipShape(Capsule())
                        }
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 12) {
                        Spacer()
                        VStack(spacing: 10) {
                            Button { SWAlertManager.shared.show(.info, message: "Info message") } label: {
                                Label("Info", systemImage: "info.circle.fill").frame(maxWidth: .infinity, alignment: .leading)
                            }.tint(.primary)
                            Button { SWAlertManager.shared.show(.success, message: "Success") } label: {
                                Label("Success", systemImage: "checkmark.circle.fill").frame(maxWidth: .infinity, alignment: .leading)
                            }.tint(.green)
                            Button { SWAlertManager.shared.show(.warning, message: "Warning") } label: {
                                Label("Warning", systemImage: "exclamationmark.triangle.fill").frame(maxWidth: .infinity, alignment: .leading)
                            }.tint(.orange)
                            Button { SWAlertManager.shared.show(.error, message: "Error") } label: {
                                Label("Error", systemImage: "xmark.circle.fill").frame(maxWidth: .infinity, alignment: .leading)
                            }.tint(.red)
                        }
                        .buttonStyle(.bordered)
                        .controlSize(.large)
                        Spacer()
                    }
                    .padding(.horizontal, 24)
                )
            },
            presentation: .push
        )

        reg["loading"] = ComponentEntry(
            title: "SWLoading",
            icon: "hourglass",
            description: "Fullscreen loading overlay with blur and optional icon",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        ProgressView()
                            .scaleEffect(1.5)
                        Text("Loading data...")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    ZStack {
                        LinearGradient(colors: [.blue, .purple], startPoint: .topLeading, endPoint: .bottomTrailing)
                            .ignoresSafeArea()
                        VStack(spacing: 20) {
                            Text("Page Content").font(.largeTitle).foregroundStyle(.white)
                            Button("Show Loading") {
                                SWLoadingManager.shared.show(page: .home, message: "Loading data...")
                                Task {
                                    try? await Task.sleep(for: .seconds(2))
                                    SWLoadingManager.shared.hide(page: .home)
                                }
                            }
                            .buttonStyle(.borderedProminent)
                        }
                    }
                    .swPageLoading(.home)
                )
            },
            presentation: .push
        )

        reg["thinking-indicator"] = ComponentEntry(
            title: "SWThinkingIndicator",
            icon: "ellipsis.bubble",
            description: "Animated three-dot bouncing indicator for chat typing states",
            preview: {
                AnyView(
                    HStack(spacing: 4) {
                        Text("Thinking")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                        SWThinkingIndicator()
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: {
                AnyView(
                    VStack(spacing: 40) {
                        SWThinkingIndicator()
                        SWThinkingIndicator(dotSize: 10, dotColor: .blue, spacing: 6)
                    }
                    .padding()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                )
            },
            presentation: .push
        )

        // -- Input (3) --

        reg["tab-button"] = ComponentEntry(
            title: "SWTabButton",
            icon: "rectangle.compress.vertical",
            description: "Capsule-shaped tab button for segmented controls",
            preview: {
                AnyView(
                    HStack {
                        SWTabButton(title: "All", isSelected: true) {}
                        SWTabButton(title: "Recent", isSelected: false) {}
                        SWTabButton(title: "Trending", isSelected: false) {}
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(TabButtonFullDemo()) },
            presentation: .push
        )

        reg["stepper"] = ComponentEntry(
            title: "SWStepper",
            icon: "minus.forwardslash.plus",
            description: "Compact numeric stepper with animated transitions",
            preview: { AnyView(StepperPreviewWrapper()) },
            fullView: { AnyView(StepperFullDemo()) },
            presentation: .push
        )

        reg["add-sheet"] = ComponentEntry(
            title: "SWAddSheet",
            icon: "plus.rectangle.on.rectangle",
            description: "Bottom sheet with text input for collecting user input",
            preview: {
                AnyView(
                    VStack(spacing: 12) {
                        Image(systemName: "plus.rectangle.on.rectangle")
                            .font(.system(size: 36))
                            .foregroundStyle(.accent)
                        Text("Add Sheet")
                            .font(.headline)
                        Text("Bottom sheet with text input and confirm button")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .frame(maxWidth: .infinity)
                )
            },
            fullView: { AnyView(AddSheetFullDemo()) },
            presentation: .push
        )

        return reg
    }

    // MARK: - Alert Color Helper

    private static func alertColor(for type: String) -> Color {
        switch type {
        case "Info": return .primary
        case "Success": return .green
        case "Warning": return .orange
        case "Error": return .red
        default: return .primary
        }
    }
}

// MARK: - Module Demo View Factories

/// Factory methods for module demo views.
/// These create the same demo views used in ComponentView but accessible
/// from outside for the ComponentRegistry and ChatView.
enum ComponentDemoViews {
    @ViewBuilder
    static func authDemo() -> some View {
        SWAuthView(isDemo: true)
            .environment(SWUserManager(skipAuthCheck: true))
    }

    @ViewBuilder
    static func cameraDemo() -> some View {
        #if os(iOS)
        ComponentViewCameraDemo()
        #else
        EmptyView()
        #endif
    }

    @ViewBuilder
    static func faceCameraDemo() -> some View {
        #if os(iOS)
        SWFaceCameraView()
        #else
        EmptyView()
        #endif
    }

    @ViewBuilder
    static func paywallDemo() -> some View {
        SWPaywallView(isDemo: true)
            .environment(SWStoreManager.shared)
    }

    @ViewBuilder
    static func chatDemo() -> some View {
        #if os(iOS)
        ComponentViewChatDemo()
        #else
        EmptyView()
        #endif
    }

    @ViewBuilder
    static func tiktokTrackingDemo() -> some View {
        #if os(iOS)
        SWTikTokTrackingView()
        #else
        EmptyView()
        #endif
    }

    @ViewBuilder
    static func subjectLiftingDemo() -> some View {
        #if os(iOS)
        NavigationStack {
            SWSubjectLiftingView()
        }
        #else
        EmptyView()
        #endif
    }
}

// MARK: - Chart Preview Data Helpers

/// Pre-built chart views for compact previews and full demos.
private enum ChartPreviews {

    // MARK: - Line Chart

    static var lineChart: some View {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: Date())
        let data: [SWLineChart<String>.DataPoint] = (0..<7).flatMap { (dayOffset: Int) -> [SWLineChart<String>.DataPoint] in
            let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
            return [
                SWLineChart<String>.DataPoint(date: date, value: Double.random(in: 40...90), category: "Revenue"),
            ]
        }
        return SWLineChart(dataPoints: data, colorMapping: ["Revenue": .blue], chartHeight: 160, title: "Revenue")
            .padding(.horizontal)
    }

    static var lineChartFull: some View {
        ScrollView {
            VStack(spacing: 32) {
                Group {
                    let calendar = Calendar.current
                    let today = calendar.startOfDay(for: Date())
                    let data: [SWLineChart<String>.DataPoint] = (0..<14).flatMap { (dayOffset: Int) -> [SWLineChart<String>.DataPoint] in
                        let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                        return [
                            .init(date: date, value: Double.random(in: 40...90), category: "Revenue"),
                            .init(date: date, value: Double.random(in: 20...60), category: "Cost"),
                        ]
                    }
                    SWLineChart(dataPoints: data, colorMapping: ["Revenue": .blue, "Cost": .red], title: "Revenue vs Cost")
                }
            }
            .padding()
        }
    }

    // MARK: - Bar Chart

    static var barChart: some View {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: Date())
        let data: [SWBarChart<String>.DataPoint] = (0..<5).flatMap { (dayOffset: Int) -> [SWBarChart<String>.DataPoint] in
            let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
            return [
                .init(date: date, value: Double.random(in: 50...150), category: "Online"),
                .init(date: date, value: Double.random(in: 30...100), category: "Offline"),
            ]
        }
        return SWBarChart(dataPoints: data, colorMapping: ["Online": .blue, "Offline": .orange], visibleDays: 5, chartHeight: 160, title: "Sales")
            .padding(.horizontal)
    }

    static var barChartFull: some View {
        ScrollView {
            VStack(spacing: 32) {
                Group {
                    let calendar = Calendar.current
                    let today = calendar.startOfDay(for: Date())
                    let data: [SWBarChart<String>.DataPoint] = (0..<10).flatMap { (dayOffset: Int) -> [SWBarChart<String>.DataPoint] in
                        let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                        return [
                            .init(date: date, value: Double.random(in: 50...150), category: "Online"),
                            .init(date: date, value: Double.random(in: 30...100), category: "Offline"),
                        ]
                    }
                    SWBarChart(dataPoints: data, colorMapping: ["Online": .blue, "Offline": .orange], title: "Sales by Channel")
                }
            }
            .padding()
        }
    }

    // MARK: - Area Chart

    static var areaChart: some View {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: Date())
        let data: [SWAreaChart<String>.DataPoint] = (0..<7).flatMap { (dayOffset: Int) -> [SWAreaChart<String>.DataPoint] in
            let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
            return [
                .init(date: date, value: Double.random(in: 100...300), category: "Organic"),
            ]
        }
        return SWAreaChart(dataPoints: data, colorMapping: ["Organic": .green], gradientOpacity: 0.25, visibleDays: 7, chartHeight: 160, title: "Traffic")
            .padding(.horizontal)
    }

    static var areaChartFull: some View {
        ScrollView {
            VStack(spacing: 32) {
                Group {
                    let calendar = Calendar.current
                    let today = calendar.startOfDay(for: Date())
                    let data: [SWAreaChart<String>.DataPoint] = (0..<14).flatMap { (dayOffset: Int) -> [SWAreaChart<String>.DataPoint] in
                        let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                        return [
                            .init(date: date, value: Double.random(in: 100...300), category: "Organic"),
                            .init(date: date, value: Double.random(in: 50...200), category: "Paid"),
                        ]
                    }
                    SWAreaChart(dataPoints: data, colorMapping: ["Organic": .green, "Paid": .blue], gradientOpacity: 0.25, title: "Website Traffic")
                }
            }
            .padding()
        }
    }

    // MARK: - Scatter Chart

    static var scatterChart: some View {
        let calendar = Calendar.current
        let today = calendar.startOfDay(for: Date())
        let data: [SWScatterChart<String>.DataPoint] = [
            .init(date: calendar.date(byAdding: .hour, value: 8, to: today)!, value: 85, category: "Teeth"),
            .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 52, category: "Food"),
            .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 72, category: "Teeth"),
            .init(date: calendar.date(byAdding: .day, value: -2, to: today)!, value: 90, category: "Teeth"),
        ]
        return SWScatterChart(dataPoints: data, colorMapping: ["Teeth": .blue, "Food": .orange], visibleDays: 3, chartHeight: 160, title: "Scans")
            .padding(.horizontal)
    }

    static var scatterChartFull: some View {
        ScrollView {
            VStack(spacing: 32) {
                Group {
                    let calendar = Calendar.current
                    let today = calendar.startOfDay(for: Date())
                    let data: [SWScatterChart<String>.DataPoint] = [
                        .init(date: calendar.date(byAdding: .hour, value: 8, to: today)!, value: 85, category: "Teeth"),
                        .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 52, category: "Food"),
                        .init(date: calendar.date(byAdding: .hour, value: 18, to: today)!, value: 78, category: "Food"),
                        .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 72, category: "Teeth"),
                        .init(date: calendar.date(byAdding: .day, value: -2, to: today)!, value: 90, category: "Teeth"),
                        .init(date: calendar.date(byAdding: .day, value: -3, to: today)!, value: 45, category: "Food"),
                    ]
                    SWScatterChart(dataPoints: data, colorMapping: ["Teeth": .blue, "Food": .orange], title: "Scan Trends")
                }
            }
            .padding()
        }
    }

    // MARK: - Donut Chart

    static var donutChart: some View {
        DonutPreviewWrapper()
    }

    static var donutChartFull: some View {
        DonutFullWrapper()
    }

    // MARK: - Radar Chart

    static var radarChart: some View {
        SWRadarChart(data: [
            .init(label: "Tolerance", value: 75),
            .init(label: "Ambition", value: 50),
            .init(label: "Acuity", value: 50),
            .init(label: "Creativity", value: 85),
            .init(label: "Stability", value: 85),
        ])
        .padding(60)
        .frame(height: 220)
    }

    static var radarChartFull: some View {
        SWRadarChart(data: [
            .init(label: "Tolerance", value: 75),
            .init(label: "Ambition", value: 50),
            .init(label: "Acuity", value: 50),
            .init(label: "Creativity", value: 85),
            .init(label: "Stability", value: 85),
        ])
        .padding(100)
    }

    // MARK: - Ring Chart

    static var ringChart: some View {
        SWRingChart(data: [
            .init(label: "Move", value: 75, color: .red),
            .init(label: "Exercise", value: 50, color: .green),
            .init(label: "Stand", value: 90, color: .cyan),
        ], size: 120, ringWidth: 12)
        .frame(height: 160)
        .frame(maxWidth: .infinity)
    }

    static var ringChartFull: some View {
        VStack(spacing: 40) {
            SWRingChart(data: [
                .init(label: "Move", value: 75, color: .red),
                .init(label: "Exercise", value: 50, color: .green),
                .init(label: "Stand", value: 90, color: .cyan),
            ]) {
                VStack {
                    Image(systemName: "flame.fill")
                        .font(.title)
                        .foregroundStyle(.orange)
                    Text("Activity")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
            }
        }
        .padding()
    }

    // MARK: - Activity Heatmap

    static var activityHeatmap: some View {
        let timestamps: [Date] = {
            var dates: [Date] = []
            let calendar = Calendar.current
            let today = Date()
            for i in 0..<30 {
                if Int.random(in: 0...100) < 70 {
                    if let date = calendar.date(byAdding: .day, value: -i, to: today) {
                        dates.append(date)
                    }
                }
            }
            return dates
        }()
        return SWActivityHeatmap.HeatmapGrid(timestamps: timestamps, days: 30, baseColor: .green)
            .padding()
    }

    static var activityHeatmapFull: some View {
        let timestamps: [Date] = {
            var dates: [Date] = []
            let calendar = Calendar.current
            let today = Date()
            for i in 0..<60 {
                if Int.random(in: 0...100) < 70 {
                    if let date = calendar.date(byAdding: .day, value: -i, to: today) {
                        let count = Int.random(in: 1...3)
                        for _ in 0..<count { dates.append(date) }
                    }
                }
            }
            return dates
        }()
        return NavigationStack {
            Form {
                Section {
                    SWActivityHeatmap.StreakCard(streaks: timestamps, colors: [.blue, .purple])
                }
                .listRowInsets(EdgeInsets())
                Section {
                    SWActivityHeatmap.HeatmapGrid(timestamps: timestamps, days: 60, baseColor: .green)
                } header: {
                    Text("Past 60 days")
                } footer: {
                    SWActivityHeatmap.HeatmapLegend(baseColor: .green)
                }
            }
            .navigationTitle("Activity")
        }
    }
}

// MARK: - Stateful Wrapper Views

/// Donut chart preview needs its own state for selectedCategory.
private struct DonutPreviewWrapper: View {
    @State private var selected: String? = nil
    var body: some View {
        let work = SWDonutChart.Category(name: "Work")
        let personal = SWDonutChart.Category(name: "Personal")
        SWDonutChart(
            subjects: [
                .init(name: "Meeting", category: work),
                .init(name: "Shopping", category: personal),
                .init(name: "Exercise", category: nil),
            ],
            selectedCategory: $selected
        )
        .frame(height: 200)
        .padding(.horizontal)
    }
}

private struct DonutFullWrapper: View {
    @State private var selected: String? = nil
    var body: some View {
        let work = SWDonutChart.Category(name: "Work")
        let personal = SWDonutChart.Category(name: "Personal")
        let health = SWDonutChart.Category(name: "Health")
        SWDonutChart(
            subjects: [
                .init(name: "Meeting", category: work),
                .init(name: "Report", category: work),
                .init(name: "Email", category: work),
                .init(name: "Shopping", category: personal),
                .init(name: "Reading", category: personal),
                .init(name: "Exercise", category: health),
                .init(name: "Meditation", category: health),
                .init(name: "Running", category: health),
                .init(name: "Uncategorized Task", category: nil),
            ],
            selectedCategory: $selected
        )
        .padding()
    }
}

private struct StepperPreviewWrapper: View {
    @State private var value = 1
    var body: some View {
        SWStepper(quantity: $value)
            .padding()
            .frame(maxWidth: .infinity)
    }
}

private struct StepperFullDemo: View {
    @State private var value = 1
    var body: some View {
        VStack(spacing: 30) {
            SWStepper(quantity: $value)
            Divider()
            HStack {
                Text("Quantity")
                Spacer()
                SWStepper(quantity: $value)
            }
            .padding(.horizontal)
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

private struct TabButtonFullDemo: View {
    @State private var selected = 0
    var body: some View {
        List {
            HStack {
                SWTabButton(title: "All", isSelected: selected == 0) {
                    withAnimation(.easeInOut(duration: 0.2)) { selected = 0 }
                }
                SWTabButton(title: "Favorites", isSelected: selected == 1) {
                    withAnimation(.easeInOut(duration: 0.2)) { selected = 1 }
                }
                SWTabButton(title: "Recent", isSelected: selected == 2) {
                    withAnimation(.easeInOut(duration: 0.2)) { selected = 2 }
                }
            }
            .listRowInsets(EdgeInsets())
            .listRowBackground(Color.clear)

            Section {
                ForEach(["Item A", "Item B", "Item C"], id: \.self) { item in
                    Label(item, systemImage: "doc.text")
                }
            }
        }
    }
}

private struct AddSheetFullDemo: View {
    @State private var showSheet = false
    var body: some View {
        VStack {
            Spacer()
            Button("Show Add Sheet") { showSheet = true }
                .buttonStyle(.borderedProminent)
            Spacer()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .sheet(isPresented: $showSheet) {
            SWAddSheet(isPresented: $showSheet) { _ in }
        }
    }
}

/// Wraps SWOnboardingView with dismiss logic for fullScreenCover.
private struct OnboardingDemoWrapper: View {
    @Environment(\.dismiss) private var dismiss
    var body: some View {
        SWOnboardingView(onComplete: { dismiss() })
    }
}

/// Wraps SWOrderView with a close button for fullScreenCover.
private struct OrderDemoWrapper: View {
    @Environment(\.dismiss) private var dismiss
    var body: some View {
        ZStack(alignment: .topTrailing) {
            SWOrderView()
            Button {
                dismiss()
            } label: {
                Image(systemName: "xmark.circle.fill")
                    .font(.title)
                    .symbolRenderingMode(.hierarchical)
                    .foregroundStyle(.white)
                    .padding()
            }
        }
    }
}
```

## File: `ShipSwift/Service/ShipSwiftAPIService.swift`
```
//
//  ShipSwiftAPIService.swift
//  ShipSwift
//
//  API client for ShipSwift server endpoints.
//  Handles App Store purchase verification and API key management.
//
//  Created by ShipSwift on 2/27/26.
//

import Foundation

struct ShipSwiftAPIService {
    private let baseURL = "https://api.shipswift.app"

    // MARK: - Response Types

    struct VerifyResponse: Decodable {
        let apiKey: String
        let message: String
        let isExisting: Bool
    }

    struct KeyStatusResponse: Decodable {
        let hasKey: Bool
        let plan: String?
        let status: String?
        let apiKey: String?
        let email: String?
        let purchasedAt: String?
        let lastUsedAt: String?
    }

    struct RevealResponse: Decodable {
        let apiKey: String
    }

    // MARK: - App Store Purchase Verification

    /// Verify an App Store purchase and get an API key
    func verifyAppStorePurchase(idToken: String, signedTransactionInfo: String) async throws -> VerifyResponse {
        let url = URL(string: "\(baseURL)/api/appstore/verify")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("Bearer \(idToken)", forHTTPHeaderField: "Authorization")
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(["signedTransactionInfo": signedTransactionInfo])

        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse else {
            throw URLError(.badServerResponse)
        }

        guard httpResponse.statusCode == 200 else {
            throw URLError(.init(rawValue: httpResponse.statusCode))
        }

        return try JSONDecoder().decode(VerifyResponse.self, from: data)
    }

    // MARK: - API Key Management

    /// Get current API key status (masked)
    func getApiKeyStatus(idToken: String) async throws -> KeyStatusResponse {
        let url = URL(string: "\(baseURL)/api/dashboard/key")!
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("Bearer \(idToken)", forHTTPHeaderField: "Authorization")

        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }

        return try JSONDecoder().decode(KeyStatusResponse.self, from: data)
    }

    /// Reveal the full API key
    func revealApiKey(idToken: String) async throws -> String {
        let url = URL(string: "\(baseURL)/api/dashboard/key/reveal")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("Bearer \(idToken)", forHTTPHeaderField: "Authorization")

        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }

        let result = try JSONDecoder().decode(RevealResponse.self, from: data)
        return result.apiKey
    }
}
```

## File: `ShipSwift/View/ChatView.swift`
```
//
//  ChatView.swift
//  ShipSwift
//
//  Chat tab (iOS only) — AI-powered component discovery and preview.
//  Users describe what they need in natural language, and the AI
//  recommends matching SwiftUI components rendered inline as real views.
//
//  Created by Wei Zhong on 18/2/26.
//

#if os(iOS)

import SwiftUI

// MARK: - Chat Message Model

/// Extended chat message supporting optional component rendering.
///
/// When `componentId` is non-nil, the chat bubble renders a live SwiftUI
/// component preview instead of plain text.
struct ChatMessage: Identifiable, Codable {
    let id: UUID
    let content: String
    let isUser: Bool
    let timestamp: Date
    let componentId: String?

    init(
        content: String,
        isUser: Bool,
        componentId: String? = nil
    ) {
        self.id = UUID()
        self.content = content
        self.isUser = isUser
        self.timestamp = Date()
        self.componentId = componentId
    }

    // MARK: - Local Persistence

    private static let fileName = "chat_history.json"

    private static var fileURL: URL {
        FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent(fileName)
    }

    static func loadFromDisk() -> [ChatMessage]? {
        guard let data = try? Data(contentsOf: fileURL),
              let messages = try? JSONDecoder().decode([ChatMessage].self, from: data),
              !messages.isEmpty else { return nil }
        return messages
    }

    static func saveToDisk(_ messages: [ChatMessage]) {
        guard let data = try? JSONEncoder().encode(messages) else { return }
        try? data.write(to: fileURL, options: .atomic)
    }

    static func clearDisk() {
        try? FileManager.default.removeItem(at: fileURL)
    }
}

// MARK: - Chat View

struct ChatView: View {
    @State private var messages: [ChatMessage] = []
    @State private var isWaiting = false

    private let chatService = ChatService()
    private let registry = ComponentRegistry()

    var body: some View {
        NavigationStack {
            VStack(spacing: 0) {
                // Message list
                SWMessageList(messages: messages) { message in
                    SWMessageBubble(isFromUser: message.isUser) {
                        if let componentId = message.componentId,
                           registry.entries[componentId] != nil {
                            ComponentPreviewBubble(
                                componentId: componentId,
                                registry: registry
                            )
                        } else {
                            // Default text bubble
                            Text(message.content)
                                .padding(12)
                                .background(message.isUser ? Color.accentColor : Color(UIColor.systemGray6))
                                .foregroundStyle(message.isUser ? .white : .primary)
                                .clipShape(RoundedRectangle(cornerRadius: 16))
                        }
                    }
                }

                // Quick suggestions — shown only at initial state
                if messages.count <= 1 && !isWaiting {
                    SWScrollingFAQ(
                        rows: [
                            ["Paywall", "Auth Flow", "Camera", "Chat UI", "Settings", "Face Camera"],
                            ["Bar Chart", "Line Chart", "Donut Chart", "Heatmap", "Radar Chart", "Area Chart"],
                            ["Shimmer", "Onboarding", "Alert", "Loading", "Stepper", "Typewriter Text"]
                        ]
                    ) { question in
                        inputText = question
                        sendMessage()
                    }
                }

                // Thinking indicator when waiting for AI response
                if isWaiting {
                    HStack {
                        HStack(spacing: 4) {
                            Text("Thinking")
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                            SWThinkingIndicator()
                        }
                        .padding(.horizontal, 14)
                        .padding(.vertical, 8)
                        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
                        Spacer()
                    }
                    .padding(.horizontal, 12)
                    .padding(.vertical, 4)
                }

                // Input bar
                SWChatInputView(
                    text: $inputText,
                    isDisabled: isWaiting,
                    placeHolderText: "Describe a component..."
                ) {
                    sendMessage()
                }
                .frame(maxWidth: 760)
                .frame(maxWidth: .infinity)
                .padding(.horizontal)
            }
            .navigationTitle("ShipSwift AI")
            .toolbarTitleDisplayMode(.inlineLarge)
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    NavigationLink {
                        SettingView()
                    } label: {
                        Image(systemName: "gearshape.fill")
                    }
                }
            }
        }
        .task {
            if let saved = ChatMessage.loadFromDisk() {
                messages = saved
            } else {
                let welcome = ChatMessage(
                    content: "Hi! Describe what you need, and I'll show you the best SwiftUI component from our library.",
                    isUser: false
                )
                messages = [welcome]
            }
        }
        .onChange(of: messages.count) {
            ChatMessage.saveToDisk(messages)
        }
    }

    @State private var inputText = ""

    // MARK: - Send Message

    private func sendMessage() {
        let text = inputText.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty else { return }

        // Append user message
        let userMessage = ChatMessage(content: text, isUser: true)
        messages.append(userMessage)

        inputText = ""
        isWaiting = true

        Task {
            let response = await chatService.send(message: text, history: messages)

            // Append AI text reply
            let replyMessage = ChatMessage(content: response.reply, isUser: false)
            messages.append(replyMessage)

            // If a component was matched, append a component preview message
            if let componentId = response.component, registry.entries[componentId] != nil {
                let componentMessage = ChatMessage(
                    content: registry.title(for: componentId),
                    isUser: false,
                    componentId: componentId
                )
                messages.append(componentMessage)
            }

            isWaiting = false
        }
    }

}

// MARK: - Component Preview Bubble

/// Renders a live SwiftUI component preview inside a chat bubble.
///
/// Tapping the bubble opens the full component view in a sheet.
struct ComponentPreviewBubble: View {
    let componentId: String
    let registry: ComponentRegistry

    @State private var showSheet = false

    var body: some View {
        Button {
            showSheet = true
        } label: {
            VStack(alignment: .leading, spacing: 10) {
                // Header with icon and title
                HStack(spacing: 8) {
                    Image(systemName: registry.icon(for: componentId))
                        .foregroundStyle(.accent)
                    Text(registry.title(for: componentId))
                        .font(.headline)
                    Spacer()
                    Image(systemName: "chevron.right")
                        .font(.footnote)
                        .foregroundStyle(.tertiary)
                }

                // Component preview area
                if let preview = registry.view(for: componentId) {
                    preview
                        .frame(maxHeight: 300)
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                        .allowsHitTesting(false)
                }
            }
            .padding(12)
            .background(Color(UIColor.secondarySystemGroupedBackground))
            .clipShape(RoundedRectangle(cornerRadius: 16))
            .overlay(
                RoundedRectangle(cornerRadius: 16)
                    .stroke(Color.primary.opacity(0.08), lineWidth: 1)
            )
            .contentShape(Rectangle())
        }
        .buttonStyle(.plain)
        .sheet(isPresented: $showSheet) {
            registry.fullView(for: componentId)
                .presentationDragIndicator(.visible)
                .presentationCornerRadius(44)
        }
    }
}

// MARK: - Preview

#Preview {
    ChatView()
        .swAlert()
}

#endif
```

## File: `ShipSwift/View/ComponentView.swift`
```
//
//  ComponentView.swift
//  ShipSwift
//
//  Components tab — showcases all component categories:
//  Module, Animation, Chart, Display, Feedback, and Input.
//
//  Created by Wei Zhong on 12/2/26.
//

import SwiftUI
import Charts

/// Sidebar categories for the macOS NavigationSplitView layout.
enum ComponentSection: String, CaseIterable, Identifiable {
    case module = "Module"
    case animation = "Animation"
    case chart = "Chart"
    case display = "Display"
    case feedback = "Feedback"
    case input = "Input"

    var id: String { rawValue }

    var icon: String {
        switch self {
        case .module: "square.3.layers.3d"
        case .animation: "sparkles"
        case .chart: "chart.bar"
        case .display: "rectangle.on.rectangle"
        case .feedback: "bell"
        case .input: "keyboard"
        }
    }
}

struct ComponentView: View {
    @Binding var scrollTarget: String?

    // Input section state
    @State private var selectedInputTab = 0
    @State private var stepperValue = 1

    // Display section state
    @State private var showAddSheet = false


    // Chart section state
    @State private var donutSelectedCategory: String? = nil

    // macOS sidebar selection
    #if os(macOS)
    private enum MacSidebarItem: Hashable {
        case home
        case section(ComponentSection)
    }

    @State private var selectedMacItem: MacSidebarItem? = .home

    /// Maps HomeView's tab-string binding to the macOS sidebar selection,
    /// using scrollTarget to determine the correct component section.
    private var homeTabBinding: Binding<String> {
        Binding(
            get: { "home" },
            set: { newValue in
                guard newValue == "component" else { return }
                switch scrollTarget {
                case "animation": selectedMacItem = .section(.animation)
                case "chart":     selectedMacItem = .section(.chart)
                case "display":   selectedMacItem = .section(.display)
                case "feedback":  selectedMacItem = .section(.feedback)
                case "input":     selectedMacItem = .section(.input)
                default:          selectedMacItem = .section(.module)
                }
            }
        )
    }
    #endif

    var body: some View {
        #if os(macOS)
        macOSBody
        #else
        iOSBody
        #endif
    }

    // MARK: - iOS Body

    #if os(iOS)
    private var iOSBody: some View {
        NavigationStack {
            ScrollViewReader { proxy in
                List {
                    moduleSection
                    animationSection
                    chartSection
                    displaySection
                    feedbackSection
                    inputSection
                }
                .onChange(of: scrollTarget) { _, target in
                    guard let target else { return }
                    withAnimation {
                        proxy.scrollTo(target, anchor: .top)
                    }
                    // Reset after scrolling
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                        scrollTarget = nil
                    }
                }
            }
            .navigationTitle("Components")
            .toolbarTitleDisplayMode(.inlineLarge)
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    NavigationLink {
                        SettingView()
                            .hideTabBar()
                    } label: {
                        Image(systemName: "gearshape.fill")
                    }
                }
            }
        }
    }
    #endif

    // MARK: - macOS Body

    #if os(macOS)
    private var macOSBody: some View {
        NavigationSplitView {
            List(selection: $selectedMacItem) {
                Label("ShipSwift", systemImage: "house.fill")
                    .tag(MacSidebarItem.home)

                Section("Components") {
                    ForEach(ComponentSection.allCases) { section in
                        Label(section.rawValue, systemImage: section.icon)
                            .tag(MacSidebarItem.section(section))
                    }
                }
            }
            .navigationTitle("ShipSwift")
            .navigationSplitViewColumnWidth(min: 160, ideal: 180)
        } detail: {
            switch selectedMacItem {
            case .home, nil:
                HomeView(selectedTab: homeTabBinding, scrollTarget: $scrollTarget)
            case .section(let section):
                NavigationStack {
                    Group {
                        switch section {
                        case .module: List { moduleSection }
                        case .animation: List { animationSection }
                        case .chart: List { chartSection }
                        case .display: List { displaySection }
                        case .feedback: List { feedbackSection }
                        case .input: List { inputSection }
                        }
                    }
                    .navigationTitle(section.rawValue)
                    .toolbarBackground(.hidden, for: .windowToolbar)
                    .toolbar {
                        ToolbarItem(placement: .primaryAction) {
                            NavigationLink {
                                SettingView()
                            } label: {
                                Image(systemName: "gearshape.fill")
                            }
                        }
                    }
                }
            }
        }
        .toolbarBackground(.hidden, for: .windowToolbar)
    }
    #endif

    // MARK: - Module Section

    private var moduleSection: some View {
        Section {
            // Auth demo — renders SWAuthView (iOS or macOS version automatically)
            NavigationLink {
                SWAuthView(isDemo: true)
                    .environment(SWUserManager(skipAuthCheck: true))
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Auth",
                    icon: "person.badge.key.fill",
                    description: "Complete auth flow: email sign-in/up, phone sign-in with country code picker, verification code, forgot/reset password, Apple & Google social sign-in."
                )
            }

            // Camera demo — iOS only
            #if os(iOS)
            NavigationLink {
                ComponentViewCameraDemo()
                    .swAlert()
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Camera",
                    icon: "camera.fill",
                    description: "Full camera capture view with viewfinder overlay, pinch-to-zoom, zoom slider, photo library picker, and permission handling."
                )
            }

            // Face Camera demo — iOS only
            NavigationLink {
                ComponentViewFaceCameraDemo()
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Face Camera",
                    icon: "face.smiling.inverse",
                    description: "Camera with real-time Vision face landmark detection, front/back switching, landmark overlay toggle, and configurable color schemes."
                )
            }
            #endif

            // Paywall — Pro paywall with lifetime purchase
            NavigationLink {
                SWPaywallView(isDemo: true)
                    .environment(SWStoreManager.shared)
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Paywall",
                    icon: "creditcard.fill",
                    description: "Pro paywall with lifetime purchase, feature list, restore purchases, and sign-in for API key management."
                )
            }

            // Chat demo — iOS only
            #if os(iOS)
            NavigationLink {
                ComponentViewChatDemo()
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Chat",
                    icon: "bubble.left.and.bubble.right.fill",
                    description: "Chat interface with message bubbles, text input, voice recording waveform, and simple echo response simulation."
                )
            }
            #endif

            // TikTok Tracking demo — iOS only
            #if os(iOS)
            NavigationLink {
                SWTikTokTrackingView()
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "TikTok Tracking",
                    icon: "chart.bar.xaxis.ascending",
                    description: "TikTok App Events SDK with ATT permission flow and event tracking for ad attribution."
                )
            }
            #endif

            // Subject Lifting demo — iOS only
            #if os(iOS)
            NavigationLink {
                SWSubjectLiftingView()
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Subject Lifting",
                    icon: "person.and.background.dotted",
                    description: "Background removal using VisionKit ImageAnalyzer. Capture or pick a photo to extract the primary subject."
                )
            }
            #endif

            // Settings module
            NavigationLink {
                SWSettingView(isDemo: true)
                    .hideTabBar()
            } label: {
                ListItem(
                    title: "Setting",
                    icon: "gearshape.fill",
                    description: "Generic settings page with language switch, share, legal links, and account actions. Pushed via NavigationLink."
                )
            }
        } header: {
            #if os(iOS)
            Text("Module")
                .font(.title3.bold())
                .textCase(nil)
                .id("module")
            #endif
        }
    }

    // MARK: - Animation Section

    private var animationSection: some View {
        Section {
            NavigationLink {
                SWBeforeAfterSlider(
                    before: Image(.smileBefore),
                    after: Image(.smileAfter)
                )
                .padding()
            } label: {
                ListItem(
                    title: "Before / After Slider",
                    icon: "slider.horizontal.below.rectangle",
                    description: "Draggable image comparison slider with auto-oscillating animation. Supports custom labels, speed, and aspect ratio."
                )
            }

            NavigationLink {
                VStack(spacing: 26) {
                    SWTypewriterText(
                        texts: ["Level up your smile game", "AI-powered smile analysis", "Join the glow up era"],
                        animationStyle: .spring
                    )
                    .font(.title3.weight(.semibold))

                    SWTypewriterText(
                        texts: ["Level up your smile game", "AI-powered smile analysis", "Join the glow up era"],
                        animationStyle: .blur
                    )
                    .font(.title3.weight(.semibold))

                    SWTypewriterText(
                        texts: ["Hello World", "Welcome Back", "Let's Go"],
                        animationStyle: .spring,
                        gradient: LinearGradient(colors: [.pink, .orange], startPoint: .leading, endPoint: .trailing)
                    )
                    .font(.title.weight(.bold))
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .background(Color.black)
            } label: {
                ListItem(
                    title: "Typewriter Text",
                    icon: "character.cursor.ibeam",
                    description: "Typing and deleting text animation that cycles through strings. Six animation styles: spring, blur, fade, scale, wave, none."
                )
            }

            NavigationLink {
                VStack(spacing: 40) {
                    SWShakingIcon(image: Image(systemName: "apple.logo"), height: 20)
                    SWShakingIcon(image: Image(.smileAfter), height: 100, cornerRadius: 8)
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "Shaking Icon",
                    icon: "iphone.radiowaves.left.and.right",
                    description: "Periodically zooms in and shakes side-to-side, mimicking the iOS home-screen jiggle effect. Supports SF Symbols and asset images."
                )
            }

            NavigationLink {
                VStack(spacing: 30) {
                    SWShimmer {
                        Button {} label: {
                            Text("Hello World")
                                .font(.largeTitle)
                                .padding(.horizontal)
                                .padding(.vertical, 6)
                        }
                        .buttonStyle(.borderedProminent)
                    }

                    SWShimmer {
                        RoundedRectangle(cornerRadius: 12)
                            .fill(.gray.opacity(0.3))
                            .frame(width: 280, height: 120)
                    }
                }
                .padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "Shimmer",
                    icon: "light.max",
                    description: "Translucent light band sweep across any view. Commonly used on buttons, skeleton loaders, or cards to draw attention."
                )
            }

            NavigationLink {
                VStack(spacing: 26) {
                    SWGlowSweep {
                        Text("Start Scan Today")
                            .font(.largeTitle.bold())
                    }

                    SWGlowSweep(baseColor: .accentColor, glowColor: .white, duration: 1.5) {
                        Text("Analyzing...")
                            .font(.title2.bold())
                    }

                    SWGlowSweep(baseColor: .green.opacity(0.7), glowColor: .black) {
                        Text("Processing")
                            .font(.headline)
                    }
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "Glow Sweep",
                    icon: "wand.and.rays",
                    description: "Sweeps a glowing highlight band using the original content shape as mask. Ideal for text, icons, and SF Symbols."
                )
            }

            NavigationLink {
                VStack(spacing: 26) {
                    SWLightSweep {
                        Image(.smileAfter)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 180)
                    }

                    SWLightSweep(lineWidth: 120, duration: 0.5, cornerRadius: 20) {
                        Image(.smileAfter)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 200)
                    }
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "Light Sweep",
                    icon: "light.beacon.max",
                    description: "Gradient light band that sweeps across content in a rounded rectangle. Great for image cards and thumbnails."
                )
            }

            NavigationLink {
                VStack(spacing: 20) {
                    SWScanningOverlay {
                        Image(.facePicture)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 180)
                            .clipShape(RoundedRectangle(cornerRadius: 12))
                    }

                    SWScanningOverlay(gridOpacity: 0.1, bandOpacity: 0.1, speed: 3.0) {
                        Image(.facePicture)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 200)
                            .clipShape(RoundedRectangle(cornerRadius: 12))
                    }
                }
                .padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "Scanning Overlay",
                    icon: "barcode.viewfinder",
                    description: "Grid lines, sweeping scan band, and noise layer overlay. Conveys an analyzing / processing visual effect."
                )
            }

            NavigationLink {
                SWAnimatedMeshGradient()
                    .ignoresSafeArea()
            } label: {
                ListItem(
                    title: "Animated Mesh Gradient",
                    icon: "circle.hexagongrid.fill",
                    description: "3x3 mesh gradient background that transitions between two color palettes. Designed as a full-screen or section background."
                )
            }

            NavigationLink {
                VStack {
                    SWOrbitingLogos(
                        images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
                    ) {
                        Image(.fullpackLogo)
                            .resizable()
                            .scaledToFit()
                            .frame(width: 60, height: 60)
                            .clipShape(RoundedRectangle(cornerRadius: 8))
                            .offset(y: -5)
                    }

                    SWOrbitingLogos(
                        images: ["airpods", "business-shoes", "sunglasses", "tshirt", "wide-brimmed-hat", "golf-gloves", "suit", "golf-gloves"]
                    ) {
                        Circle()
                            .fill(.blue)
                            .frame(width: 50, height: 50)
                    }
                    .frame(width: 150)
                }
            } label: {
                ListItem(
                    title: "Orbiting Logos",
                    icon: "atom",
                    description: "SpriteKit-powered concentric rings of colored dots with icons on the outermost ring. Custom center view via SwiftUI."
                )
            }
        } header: {
            #if os(iOS)
            Text("Animation")
                .font(.title3.bold())
                .textCase(nil)
                .id("animation")
            #endif
        }
    }

    // MARK: - Chart Section

    private var chartSection: some View {
        Section {
            NavigationLink {
                ScrollView {
                    VStack(spacing: 32) {
                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let salesData: [SWLineChart<String>.DataPoint] = (0..<14).flatMap { (dayOffset: Int) -> [SWLineChart<String>.DataPoint] in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return [
                                    .init(date: date, value: Double.random(in: 40...90), category: "Revenue"),
                                    .init(date: date, value: Double.random(in: 20...60), category: "Cost"),
                                ]
                            }

                            SWLineChart(
                                dataPoints: salesData,
                                colorMapping: ["Revenue": .blue, "Cost": .red],
                                title: "Revenue vs Cost"
                            )
                        }

                        Divider()

                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let tempData: [SWLineChart<String>.DataPoint] = (0..<10).map { dayOffset in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return .init(date: date, value: Double.random(in: 35.5...38.5), category: "Temperature")
                            }

                            SWLineChart(
                                dataPoints: tempData,
                                colorMapping: ["Temperature": .orange],
                                referenceLines: [
                                    .init(value: 37.0, label: "Normal", color: .green),
                                    .init(value: 38.0, label: "Fever", color: .red),
                                ],
                                interpolationMethod: .catmullRom,
                                showPointMarkers: true,
                                yDomain: 35...40,
                                visibleDays: 10,
                                chartHeight: 220,
                                title: "Body Temperature"
                            )
                        }
                    }
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Line Chart",
                    icon: "chart.xyaxis.line",
                    description: "Multi-series line chart with horizontal scrolling, reference lines, point markers, and configurable interpolation methods."
                )
            }

            NavigationLink {
                ScrollView {
                    VStack(spacing: 32) {
                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let salesData: [SWBarChart<String>.DataPoint] = (0..<10).flatMap { (dayOffset: Int) -> [SWBarChart<String>.DataPoint] in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return [
                                    .init(date: date, value: Double.random(in: 50...150), category: "Online"),
                                    .init(date: date, value: Double.random(in: 30...100), category: "Offline"),
                                ]
                            }

                            SWBarChart(
                                dataPoints: salesData,
                                colorMapping: ["Online": .blue, "Offline": .orange],
                                title: "Sales by Channel (Grouped)"
                            )
                        }

                        Divider()

                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let stackedData: [SWBarChart<String>.DataPoint] = (0..<7).flatMap { (dayOffset: Int) -> [SWBarChart<String>.DataPoint] in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return [
                                    .init(date: date, value: Double.random(in: 30...80), category: "Food"),
                                    .init(date: date, value: Double.random(in: 20...50), category: "Transport"),
                                    .init(date: date, value: Double.random(in: 10...40), category: "Entertainment"),
                                ]
                            }

                            SWBarChart(
                                dataPoints: stackedData,
                                colorMapping: ["Food": .green, "Transport": .blue, "Entertainment": .purple],
                                stackMode: .stacked,
                                yDomain: 0...200,
                                visibleDays: 7,
                                chartHeight: 250,
                                title: "Daily Expenses (Stacked)"
                            )
                        }
                    }
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Bar Chart",
                    icon: "chart.bar.fill",
                    description: "Grouped or stacked bar chart with horizontal scrolling, optional value labels, and configurable bar corner radius."
                )
            }

            NavigationLink {
                ScrollView {
                    VStack(spacing: 32) {
                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let trafficData: [SWAreaChart<String>.DataPoint] = (0..<14).flatMap { (dayOffset: Int) -> [SWAreaChart<String>.DataPoint] in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return [
                                    .init(date: date, value: Double.random(in: 100...300), category: "Organic"),
                                    .init(date: date, value: Double.random(in: 50...200), category: "Paid"),
                                ]
                            }

                            SWAreaChart(
                                dataPoints: trafficData,
                                colorMapping: ["Organic": .green, "Paid": .blue],
                                gradientOpacity: 0.25,
                                title: "Website Traffic"
                            )
                        }

                        Divider()

                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let revenueData: [SWAreaChart<String>.DataPoint] = (0..<10).flatMap { (dayOffset: Int) -> [SWAreaChart<String>.DataPoint] in
                                let date = calendar.date(byAdding: .day, value: -dayOffset, to: today)!
                                return [
                                    .init(date: date, value: Double.random(in: 40...120), category: "Product A"),
                                    .init(date: date, value: Double.random(in: 30...80), category: "Product B"),
                                    .init(date: date, value: Double.random(in: 20...60), category: "Product C"),
                                ]
                            }

                            SWAreaChart(
                                dataPoints: revenueData,
                                colorMapping: ["Product A": .purple, "Product B": .orange, "Product C": .cyan],
                                stackMode: .stacked,
                                gradientOpacity: 0.4,
                                yDomain: 0...300,
                                visibleDays: 10,
                                chartHeight: 240,
                                title: "Revenue by Product (Stacked)"
                            )
                        }
                    }
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Area Chart",
                    icon: "chart.line.uptrend.xyaxis",
                    description: "Standard or stacked area chart with smooth interpolation, optional line overlay, and configurable area opacity."
                )
            }

            NavigationLink {
                ScrollView {
                    VStack(spacing: 32) {
                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let sampleData: [SWScatterChart<String>.DataPoint] = [
                                .init(date: calendar.date(byAdding: .hour, value: 8, to: today)!, value: 85, category: "Teeth"),
                                .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 52, category: "Food"),
                                .init(date: calendar.date(byAdding: .hour, value: 18, to: today)!, value: 78, category: "Food"),
                                .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 72, category: "Teeth"),
                                .init(date: calendar.date(byAdding: .hour, value: -18, to: today)!, value: 65, category: "Food"),
                                .init(date: calendar.date(byAdding: .day, value: -2, to: today)!, value: 90, category: "Teeth"),
                                .init(date: calendar.date(byAdding: .day, value: -3, to: today)!, value: 45, category: "Food"),
                                .init(date: calendar.date(byAdding: .day, value: -3, to: today)!, value: 88, category: "Teeth"),
                            ]

                            SWScatterChart(
                                dataPoints: sampleData,
                                colorMapping: ["Teeth": .blue, "Food": .orange],
                                title: "Scan Trends"
                            )
                        }

                        Divider()

                        Group {
                            let calendar = Calendar.current
                            let today = calendar.startOfDay(for: Date())

                            let temperatureData: [SWScatterChart<String>.DataPoint] = [
                                .init(date: calendar.date(byAdding: .hour, value: 6, to: today)!, value: 36.2, category: "Morning"),
                                .init(date: calendar.date(byAdding: .hour, value: 12, to: today)!, value: 36.8, category: "Noon"),
                                .init(date: calendar.date(byAdding: .hour, value: 20, to: today)!, value: 37.1, category: "Evening"),
                                .init(date: calendar.date(byAdding: .day, value: -1, to: today)!, value: 36.5, category: "Morning"),
                            ]

                            SWScatterChart(
                                dataPoints: temperatureData,
                                colorMapping: ["Morning": .cyan, "Noon": .yellow, "Evening": .purple],
                                yDomain: 35...40,
                                visibleDays: 5,
                                chartHeight: 200,
                                title: "Body Temperature"
                            )
                        }
                    }
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Scatter Chart",
                    icon: "chart.dots.scatter",
                    description: "Horizontally scrollable scatter chart with generic category types, color mapping, and configurable axis ranges."
                )
            }

            NavigationLink {
                SWDonutChart(
                    subjects: {
                        let work = SWDonutChart.Category(name: "Work")
                        let personal = SWDonutChart.Category(name: "Personal")
                        let health = SWDonutChart.Category(name: "Health")
                        return [
                            .init(name: "Meeting", category: work),
                            .init(name: "Report", category: work),
                            .init(name: "Email", category: work),
                            .init(name: "Shopping", category: personal),
                            .init(name: "Reading", category: personal),
                            .init(name: "Exercise", category: health),
                            .init(name: "Meditation", category: health),
                            .init(name: "Running", category: health),
                            .init(name: "Uncategorized Task", category: nil),
                        ]
                    }(),
                    selectedCategory: $donutSelectedCategory
                )
                .padding()
            } label: {
                ListItem(
                    title: "Donut Chart",
                    icon: "chart.pie.fill",
                    description: "Interactive donut chart with tap-to-select categories. Selected segment expands with center overlay showing count and name."
                )
            }

            NavigationLink {
                SWRadarChart(data: [
                    .init(label: "Tolerance", value: 75),
                    .init(label: "Ambition", value: 50),
                    .init(label: "Acuity", value: 50),
                    .init(label: "Creativity", value: 85),
                    .init(label: "Stability", value: 85)
                ])
                .padding(100)
            } label: {
                ListItem(
                    title: "Radar Chart",
                    icon: "pentagon",
                    description: "Animated radar (spider) chart with axis labels, grid rings, and radial lines. Supports 3+ axes with customizable max value."
                )
            }

            NavigationLink {
                VStack(spacing: 40) {
                    SWRingChart(data: [
                        .init(label: "Move", value: 75, color: .red),
                        .init(label: "Exercise", value: 50, color: .green),
                        .init(label: "Stand", value: 90, color: .cyan)
                    ]) {
                        VStack {
                            Image(systemName: "flame.fill")
                                .font(.title)
                                .foregroundStyle(.orange)
                            Text("Activity")
                                .font(.caption)
                                .foregroundStyle(.secondary)
                        }
                    }

                    Divider()

                    SWRingChart(
                        data: [
                            .init(label: "Partner", value: 80, color: .accentColor),
                            .init(label: "Family", value: 91, color: .green),
                            .init(label: "Social", value: 63, color: .orange)
                        ],
                        size: 200,
                        ringWidth: 20,
                        spacing: 8
                    )
                }
                .padding()
            } label: {
                ListItem(
                    title: "Ring Chart",
                    icon: "circle.circle",
                    description: "Apple Watch Activity Rings style concentric ring progress chart. Supports custom center content, dimensions, and animated appear."
                )
            }

            NavigationLink {
                let timestamps: [Date] = {
                    var dates: [Date] = []
                    let calendar = Calendar.current
                    let today = Date()
                    for i in 0..<60 {
                        if Int.random(in: 0...100) < 70 {
                            if let date = calendar.date(byAdding: .day, value: -i, to: today) {
                                let count = Int.random(in: 1...3)
                                for _ in 0..<count {
                                    dates.append(date)
                                }
                            }
                        }
                    }
                    return dates
                }()

                NavigationStack {
                    Form {
                        Section {
                            SWActivityHeatmap.StreakCard(
                                streaks: timestamps,
                                colors: [.blue, .purple]
                            )
                        }
                        .listRowInsets(EdgeInsets())

                        Section {
                            SWActivityHeatmap.HeatmapGrid(
                                timestamps: timestamps,
                                days: 60,
                                baseColor: .green
                            )
                        } header: {
                            Text("Past 60 days")
                        } footer: {
                            SWActivityHeatmap.HeatmapLegend(
                                baseColor: .green
                            )
                        }
                    }
                    .navigationTitle("Activity")
                }
            } label: {
                ListItem(
                    title: "Activity Heatmap",
                    icon: "square.grid.3x3.fill",
                    description: "GitHub-style activity heatmap with streak tracking. Includes StreakCard, HeatmapGrid, HeatmapLegend sub-components."
                )
            }
        } header: {
            #if os(iOS)
            Text("Chart")
                .font(.title3.bold())
                .textCase(nil)
                .id("chart")
            #endif
        }
    }

    // MARK: - Display Section

    private var displaySection: some View {
        Section {
            // Floating labels — animated capsule labels hovering over an image
            NavigationLink {
                SWFloatingLabels(
                    image: Image(.facePicture),
                    labels: [
                        .init(text: "Teeth mapping",    position: CGPoint(x: 0.3, y: 0.5)),
                        .init(text: "Plaque detection", position: CGPoint(x: 0.9, y: 0.6)),
                        .init(text: "Shape & balance",  position: CGPoint(x: 0.5, y: 0.8))
                    ]
                )
            } label: {
                ListItem(
                    title: "Floating Labels",
                    icon: "tag.fill",
                    description: "Animated floating capsule labels over an image. Labels fade in/out at specified positions, ideal for feature callouts."
                )
            }

            // Scrolling FAQ — iOS only (UIScrollView + CADisplayLink)
            #if os(iOS)
            NavigationLink {
                SWScrollingFAQ(
                    rows: [
                        ["How does AI work?", "What can I ask?", "How accurate?", "Help with coding?",
                         "Remember chat?", "Languages supported?", "Get started?", "Explain topics?"],
                        ["Write an email", "Summarize article", "Translate text", "Creative ideas",
                         "Debug code", "Explain concept", "Meal plan", "Brainstorm"],
                        ["Best approach?", "How to improve?", "Give examples", "Compare options",
                         "Suggest alternatives", "Pros and cons?", "Help understand", "Walk through"]
                    ],
                    title: "Let's talk about new topics"
                ) { _ in }
            } label: {
                ListItem(
                    title: "Scrolling FAQ",
                    icon: "bubble.left.and.text.bubble.right",
                    description: "Auto-scrolling horizontal FAQ carousel with alternating row directions. Tapping a pill triggers a callback."
                )
            }
            #endif

            // Rotating quote — auto-cycling famous quotes display
            NavigationLink {
                ScrollView {
                    VStack(spacing: 32) {
                        // Multiple quotes rotation
                        SWRotatingQuote(
                            quotes: [
                                "Those times when you get up early, and you work hard, those times when you stay up late, and you work hard.",
                                "Those times when you don't feel like working, you're too tired, you don't want to push yourself, but you do it anyway.",
                                "That is actually the dream. It's not the destination, it's the journey."
                            ],
                            author: "Kobe Bryant"
                        )
                        .frame(height: 140)

                        Divider()

                        // Single quote (no rotation)
                        SWRotatingQuote(
                            quotes: [
                                "Stay hungry, stay foolish."
                            ],
                            author: "Steve Jobs",
                            quoteFont: .title3,
                            authorFont: .title2
                        )
                        .frame(height: 100)

                        Divider()

                        // Custom style (serif, faster rotation)
                        SWRotatingQuote(
                            quotes: [
                                "The only way to do great work is to love what you do.",
                                "Innovation distinguishes between a leader and a follower.",
                                "Your time is limited, don't waste it living someone else's life."
                            ],
                            author: "Steve Jobs",
                            interval: 3.0,
                            quoteFont: .body,
                            authorFont: .callout,
                            fontDesign: .serif,
                            foregroundStyle: .primary
                        )
                        .frame(height: 120)
                    }
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Rotating Quote",
                    icon: "text.quote",
                    description: "Auto-rotating quote display that cycles through texts with animated transitions and author attribution."
                )
            }

            // Basic display elements — BulletPointText + GradientDivider + Label
            NavigationLink {
                ScrollView {
                    VStack(alignment: .leading, spacing: 24) {

                        // Section 1: SWBulletPointText demo
                        Text("Bullet Point Text")
                            .font(.headline)
                            .padding(.horizontal)

                        VStack(alignment: .leading, spacing: 10) {
                            SWBulletPointText(bulletColor: .blue) {
                                Text("Wealth")
                            }
                            SWBulletPointText(bulletColor: .green) {
                                HStack {
                                    Text("Health")
                                    Image(systemName: "heart.fill")
                                }
                            }
                            SWBulletPointText(bulletColor: .orange) {
                                Text("Happiness")
                            }
                            SWBulletPointText(bulletColor: .purple) {
                                Text("Wisdom")
                            }
                        }
                        .padding(.horizontal)

                        Divider()

                        // Section 2: SWGradientDivider demo
                        Text("Gradient Divider")
                            .font(.headline)
                            .padding(.horizontal)

                        VStack(spacing: 20) {
                            SWGradientDivider()
                            SWGradientDivider(color: .purple, opacity: 0.5)
                            SWGradientDivider(color: .mint, height: 2)
                        }
                        .padding(.horizontal)

                        Divider()

                        // Section 3: SWLabelWithIcon demo
                        Text("Label with Icon")
                            .font(.headline)
                            .padding(.horizontal)

                        VStack(alignment: .leading, spacing: 8) {
                            SWLabelWithIcon()
                            SWLabelWithIcon(
                                icon: "gearshape",
                                bg: .orange,
                                name: "Settings"
                            )
                            SWLabelWithIcon(
                                icon: "bell.badge",
                                bg: .red,
                                name: "Notifications"
                            )
                            SWLabelWithIcon(
                                icon: "lock.shield",
                                bg: .green,
                                name: "Privacy"
                            )
                            SWLabelWithIcon(
                                icon: "creditcard",
                                bg: .purple,
                                name: "Subscription"
                            )

                            Divider()

                            SWLabelWithImage(
                                image: .fullpackLogo,
                                name: "FullPack"
                            )
                        }
                        .padding(.horizontal)
                    }
                    .padding(.vertical)
                }
            } label: {
                ListItem(
                    title: "Basic Display Elements",
                    icon: "rectangle.3.group",
                    description: "BulletPointText, GradientDivider, and LabelWithIcon — simple building blocks for lists, settings, and content sections."
                )
            }
            // Onboarding — multi-page welcome flow with swipe navigation and skip
            NavigationLink {
                SWOnboardingView(onComplete: {})
            } label: {
                ListItem(
                    title: "Onboarding",
                    icon: "hand.wave.fill",
                    description: "Multi-page welcome flow with swipe navigation and skip support."
                )
            }

            // Order — animated drink customization demo
            NavigationLink {
                SWOrderView()
            } label: {
                ListItem(
                    title: "Order",
                    icon: "cup.and.saucer.fill",
                    description: "Animated drink customization demo with flavor/size selectors and cup animations."
                )
            }

            // Tab — TabView template
            NavigationLink {
                SWRootTabView()
            } label: {
                ListItem(
                    title: "Tab",
                    icon: "rectangle.split.3x1.fill",
                    description: "TabView template with selected/unselected icons and haptic feedback."
                )
            }

            // Markdown Text — renders common LLM Markdown output
            NavigationLink {
                ScrollView {
                    SWMarkdownText("""
                    # Heading 1
                    ## Heading 2
                    ### Heading 3

                    This is a paragraph with **bold** and *italic* text.

                    Here is `inline code` in a sentence.

                    ```swift
                    func greet() {
                        print("Hello, world!")
                    }
                    ```

                    - First item
                    - Second item with **bold**
                    - Third item

                    1. Ordered item one
                    2. Ordered item two

                    ---

                    Another paragraph after the divider.
                    """)
                    .padding()
                }
            } label: {
                ListItem(
                    title: "Markdown Text",
                    icon: "text.badge.checkmark",
                    description: "Custom Markdown renderer supporting headings, bold/italic, code blocks, lists, and dividers — ideal for LLM output."
                )
            }
        } header: {
            #if os(iOS)
            Text("Display")
                .font(.title3.bold())
                .textCase(nil)
                .id("display")
            #endif
        }
    }

    // MARK: - Feedback Section

    private var feedbackSection: some View {
        Section {
            // Global toast alert — supports info/success/warning/error presets and custom styles
            NavigationLink {
                VStack(spacing: 12) {
                    Spacer()

                    Text("Tap to trigger alerts")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)

                    VStack(spacing: 10) {
                        Button {
                            SWAlertManager.shared.show(.info, message: "This is an info message")
                        } label: {
                            Label("Info", systemImage: "info.circle.fill")
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }
                        .tint(.primary)

                        Button {
                            SWAlertManager.shared.show(.success, message: "Saved successfully")
                        } label: {
                            Label("Success", systemImage: "checkmark.circle.fill")
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }
                        .tint(.green)

                        Button {
                            SWAlertManager.shared.show(.warning, message: "Slow connection")
                        } label: {
                            Label("Warning", systemImage: "exclamationmark.triangle.fill")
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }
                        .tint(.orange)

                        Button {
                            SWAlertManager.shared.show(.error, message: "Operation failed, please retry")
                        } label: {
                            Label("Error", systemImage: "xmark.circle.fill")
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }
                        .tint(.red)

                        Button {
                            SWAlertManager.shared.show(
                                icon: "star.fill",
                                message: "Custom alert style",
                                textColor: .yellow,
                                backgroundStyle: AnyShapeStyle(.black),
                                borderColor: .yellow
                            )
                        } label: {
                            Label("Custom", systemImage: "star.fill")
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }
                        .tint(.yellow)
                    }
                    .buttonStyle(.bordered)
                    .controlSize(.large)

                    Spacer()
                }
                .padding(.horizontal, 24)
            } label: {
                ListItem(
                    title: "SWAlert",
                    icon: "bell.badge",
                    description: "Toast-style alert overlay with four preset styles (info, success, warning, error) and custom styling. Auto-dismisses after configurable duration."
                )
            }

            // Fullscreen loading overlay — blur material background + optional icon pulse animation
            NavigationLink {
                ZStack {
                    LinearGradient(
                        colors: [.blue, .purple],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    )
                    .ignoresSafeArea()

                    VStack(spacing: 20) {
                        Text("Page Content")
                            .font(.largeTitle)
                            .foregroundStyle(.white)

                        Button("Show Default Loading") {
                            SWLoadingManager.shared.show(page: .home, message: "Loading data...")
                            Task {
                                try? await Task.sleep(for: .seconds(2))
                                SWLoadingManager.shared.hide(page: .home)
                            }
                        }
                        .buttonStyle(.borderedProminent)

                        Button("Show Loading with Icon") {
                            SWLoadingManager.shared.show(
                                page: .home,
                                message: "Syncing data...",
                                systemImage: "arrow.triangle.2.circlepath"
                            )
                            Task {
                                try? await Task.sleep(for: .seconds(2))
                                SWLoadingManager.shared.hide(page: .home)
                            }
                        }
                        .buttonStyle(.borderedProminent)
                    }
                }
                .swPageLoading(.home)
            } label: {
                ListItem(
                    title: "SWLoading",
                    icon: "hourglass",
                    description: "Fullscreen loading overlay with blur material background, customizable message, optional SF Symbol icon with pulse animation."
                )
            }

            // Thinking indicator — three-dot bouncing animation for chat typing state
            NavigationLink {
                VStack(spacing: 40) {
                    // Default style
                    VStack(spacing: 8) {
                        Text("Default")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        SWThinkingIndicator()
                    }

                    // Inside a chat bubble
                    VStack(spacing: 8) {
                        Text("Chat Bubble")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        HStack(alignment: .bottom, spacing: 8) {
                            Image(systemName: "brain.head.profile")
                                .font(.title2)
                                .foregroundStyle(.purple)
                            HStack(spacing: 4) {
                                Text("Thinking")
                                    .font(.subheadline)
                                    .foregroundStyle(.secondary)
                                SWThinkingIndicator()
                            }
                            .padding(.horizontal, 14)
                            .padding(.vertical, 10)
                            .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16))
                        }
                    }

                    // Custom color and size
                    VStack(spacing: 8) {
                        Text("Custom (blue, large)")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                        SWThinkingIndicator(dotSize: 10, dotColor: .blue, spacing: 6)
                    }
                }
                .padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "SWThinkingIndicator",
                    icon: "ellipsis.bubble",
                    description: "Animated three-dot bouncing indicator for chat typing states. Configurable dot size, color, and spacing."
                )
            }
        } header: {
            #if os(iOS)
            Text("Feedback")
                .font(.title3.bold())
                .textCase(nil)
                .id("feedback")
            #endif
        }
    }

    // MARK: - Input Section

    private var inputSection: some View {
        Section {
            // Capsule tab button — for custom segmented controls and filter bars
            NavigationLink {
                List {
                    HStack {
                        SWTabButton(title: "All", isSelected: selectedInputTab == 0) {
                            withAnimation(.easeInOut(duration: 0.2)) { selectedInputTab = 0 }
                        }
                        SWTabButton(title: "Favorites", isSelected: selectedInputTab == 1) {
                            withAnimation(.easeInOut(duration: 0.2)) { selectedInputTab = 1 }
                        }
                        SWTabButton(title: "Recent", isSelected: selectedInputTab == 2) {
                            withAnimation(.easeInOut(duration: 0.2)) { selectedInputTab = 2 }
                        }
                        SWTabButton(title: "Trending", isSelected: selectedInputTab == 3) {
                            withAnimation(.easeInOut(duration: 0.2)) { selectedInputTab = 3 }
                        }
                    }
                    .listRowInsets(EdgeInsets())
                    .listRowBackground(Color.clear)

                    Section {
                        if selectedInputTab == 0 {
                            ForEach(["Meeting notes", "Grocery list", "Workout plan", "Travel ideas", "Book wishlist"], id: \.self) { item in
                                Label(item, systemImage: "doc.text")
                            }
                        } else if selectedInputTab == 1 {
                            ForEach(["Workout plan", "Travel ideas"], id: \.self) { item in
                                Label(item, systemImage: "star.fill")
                                    .foregroundStyle(.orange)
                            }
                        } else if selectedInputTab == 2 {
                            ForEach(["Grocery list", "Meeting notes"], id: \.self) { item in
                                Label(item, systemImage: "clock")
                                    .foregroundStyle(.secondary)
                            }
                        } else {
                            ForEach(["AI prompts", "Fitness trends", "Recipe hacks"], id: \.self) { item in
                                Label(item, systemImage: "flame.fill")
                                    .foregroundStyle(.red)
                            }
                        }
                    }
                }
            } label: {
                ListItem(
                    title: "SWTabButton",
                    icon: "rectangle.compress.vertical",
                    description: "Capsule-shaped tab button for custom segmented controls and filter bars. Toggles between selected and unselected states."
                )
            }

            // Numeric stepper — compact control with animated transitions and haptic feedback
            NavigationLink {
                VStack(spacing: 30) {
                    SWStepper(quantity: $stepperValue)

                    Divider()

                    HStack {
                        Text("Quantity")
                        Spacer()
                        SWStepper(quantity: $stepperValue)
                    }
                    .padding(.horizontal)
                }
                .padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            } label: {
                ListItem(
                    title: "SWStepper",
                    icon: "minus.forwardslash.plus",
                    description: "Compact numeric stepper with animated transitions and haptic feedback. Chevron-style increment/decrement buttons."
                )
            }

            // Add sheet — bottom sheet with text input
            NavigationLink {
                VStack {
                    Spacer()

                    Button("Show Add Sheet") {
                        showAddSheet = true
                    }
                    .buttonStyle(.borderedProminent)

                    Spacer()
                }
                .frame(maxWidth: .infinity, maxHeight: .infinity)
                .sheet(isPresented: $showAddSheet) {
                    SWAddSheet(isPresented: $showAddSheet) { _ in }
                }
            } label: {
                ListItem(
                    title: "SWAddSheet",
                    icon: "plus.rectangle.on.rectangle",
                    description: "Bottom sheet with text input, cancel and confirm buttons. Presented as medium detent for collecting user input."
                )
            }
        } header: {
            #if os(iOS)
            Text("Input")
                .font(.title3.bold())
                .textCase(nil)
                .id("input")
            #endif
        }
    }
}
// MARK: - Face Camera Demo View (Real Camera with Face Tracking)

#if os(iOS)
/// SWFaceCameraView includes its own close button — present it directly.
struct ComponentViewFaceCameraDemo: View {
    var body: some View {
        SWFaceCameraView()
    }
}

// MARK: - Camera Demo View (Real Camera, No Processing)

/// Demo using real SWCameraView — captured or selected photos are not processed or saved.
struct ComponentViewCameraDemo: View {
    @State private var capturedImage: UIImage?

    var body: some View {
        SWCameraView(image: $capturedImage)
            .swAlert()
    }
}
#endif

// MARK: - Chat Demo View (SWChatView with Simulated Response)

#if os(iOS)
/// Demo showcasing SWChatView with a simulated echo-style AI response.
/// No ASR config is provided so the microphone button is hidden in demo mode.
struct ComponentViewChatDemo: View {
    @State private var messages: [SWChatMessage] = [
        SWChatMessage(
            content: "Welcome! Send a message to see the demo response.",
            isUser: false
        ),
    ]
    @State private var isWaiting = false

    var body: some View {
        SWChatView(
            messages: $messages,
            isDisabled: isWaiting
        ) { text in
            // Simulate AI response with a 1-second delay
            isWaiting = true
            Task {
                try? await Task.sleep(for: .seconds(1))
                messages.append(
                    SWChatMessage(
                        content: "This is a demo response. Connect ShipSwift MCP to enable full AI chat functionality.",
                        isUser: false
                    )
                )
                isWaiting = false
            }
        }
        .navigationBarTitleDisplayMode(.inline)
    }
}
#endif

// MARK: - Helpers

/// Hides the tab bar when a view is pushed via NavigationLink on iOS.
/// No-op on macOS where tab bars don't exist.
private extension View {
    @ViewBuilder func hideTabBar() -> some View {
        #if os(iOS)
        self.toolbar(.hidden, for: .tabBar)
        #else
        self
        #endif
    }
}

#Preview {
    ComponentView(scrollTarget: .constant(nil))
        .environment(SWStoreManager.shared)
}
```

## File: `ShipSwift/View/HomeView.swift`
```
//
//  HomeView.swift
//  ShipSwift
//
//  Showcase App home page — hero section, Skills card, module overview grid,
//  and footer with link to shipswift.app.
//
//  Created by Wei Zhong on 14/2/26.
//

import SwiftUI

struct HomeView: View {
    @Environment(SWStoreManager.self) private var storeManager
    @Environment(SWUserManager.self) private var userManager
    @Binding var selectedTab: String
    @Binding var scrollTarget: String?

    @State private var showPaywall = false
    @State private var copied = false

    private let skillsCommand = "npx skills add signerlabs/shipswift-skills"

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {
                    heroSection
                    proStatusRow
                    skillsCard
                    linksRow
                    moduleGrid
                    footer
                }
                .frame(maxWidth: 680)
                .frame(maxWidth: .infinity)
                .padding(.horizontal)
                .padding(.bottom, 32)
            }
            .scrollIndicators(.never)
            .navigationTitle("ShipSwift")
            .toolbarTitleDisplayMode(.inlineLarge)
            .toolbar {
                ToolbarItem(placement: .primaryAction) {
                    NavigationLink {
                        SettingView()
                    } label: {
                        Image(systemName: "gearshape.fill")
                    }
                }
            }
            .sheet(isPresented: $showPaywall) {
                ProPaywallView()
                    .environment(storeManager)
                    .environment(userManager)
            }
        }
    }

    // MARK: - Hero Section

    private var heroSection: some View {
        VStack(spacing: 12) {
            SWShakingIcon(
                image: Image(.shipSwiftLogo),
                height: 120,
                cornerRadius: 16,
                idleDelay: 6
            )
            .padding(.vertical, 60)

            Text("AI-native iOS component library")
                .font(.title3)
                .foregroundStyle(.secondary)

            Text("Production-ready SwiftUI components that LLMs can use to build real apps. Every component you see here is open-source.")
                .font(.subheadline)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 8)
        }
        .padding(.vertical, 8)
    }

    // MARK: - Skills Card (Refined Terminal)

    private var skillsCard: some View {
        VStack(alignment: .leading, spacing: 16) {
            // -- Header --
            HStack {
                // Terminal icon in gradient badge
                Image(systemName: "terminal.fill")
                    .foregroundStyle(.accent)
                
                Text("Install")
            }
            .font(.headline)

            // -- Command block (tap to copy) --
            Button {
                #if os(iOS)
                UIPasteboard.general.string = skillsCommand
                #else
                NSPasteboard.general.clearContents()
                NSPasteboard.general.setString(skillsCommand, forType: .string)
                #endif
                SWAlertManager.shared.show(.success, message: "Copied to clipboard")
                withAnimation(.easeInOut(duration: 0.2)) {
                    copied = true
                }
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                    withAnimation(.easeInOut(duration: 0.2)) {
                        copied = false
                    }
                }
            } label: {
                ZStack(alignment: .topTrailing) {
                    HStack(alignment: .top, spacing: 0) {
                        Text("$")
                            .font(.system(.footnote, design: .monospaced))
                            .foregroundStyle(Color(hue: 0.38, saturation: 0.7, brightness: 0.75))

                        Spacer(minLength: 6)

                        Text(skillsCommand)
                            .font(.system(.footnote, design: .monospaced))
                            .foregroundStyle(.primary)
                            .lineLimit(2)
                            .multilineTextAlignment(.leading)
                            .frame(maxWidth: .infinity, alignment: .leading)
                    }
                    .padding(.horizontal, 14)
                    .padding(.vertical, 12)
                    .padding(.trailing, 24) // Leave room for the copy icon

                    // Copy / checkmark icon overlay
                    Image(systemName: copied ? "checkmark" : "doc.on.doc")
                        .font(.caption)
                        .foregroundStyle(copied ? .green : .secondary)
                        .contentTransition(.symbolEffect(.replace))
                        .padding(8)
                }
                .background(
                    Color.accentColor.opacity(0.1),
                    in: RoundedRectangle(cornerRadius: 8)
                )
            }
            .buttonStyle(.plain)

            // -- Subtitle --
            Text("Works with Claude Code, Codex, Gemini, Cursor, Copilot, Windsurf, and all other AI tools.")
                .font(.caption)
                .foregroundStyle(.secondary)
                .padding(.top, 2)
        }
    }

    // MARK: - Links Row

    private var linksRow: some View {
        HStack(spacing: 12) {
            Link(destination: URL(string: "https://shipswift.app")!) {
                Label("Website", systemImage: "globe")
                    .font(.subheadline)
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .tint(.secondary)

            Link(destination: URL(string: "https://github.com/signerlabs/ShipSwift")!) {
                Label("GitHub", systemImage: "chevron.left.forwardslash.chevron.right")
                    .font(.subheadline)
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .tint(.secondary)
        }
    }

    // MARK: - Pro Status Row

    private var proStatusRow: some View {
        Group {
            if storeManager.isPro {
                Label("Pro Recipes unlocked", systemImage: "checkmark.seal.fill")
                    .foregroundStyle(.secondary)
            } else {
                Button { showPaywall = true } label: {
                    Label("Unlock Pro Recipes", systemImage: "lock.open.fill")
                        .foregroundStyle(.secondary)
                }
            }
        }
    }

    // MARK: - Module Grid

    private var moduleGrid: some View {
        LazyVGrid(
            columns: [
                GridItem(.flexible(), spacing: 12),
                GridItem(.flexible(), spacing: 12)
            ],
            spacing: 12
        ) {
            ModuleCard(
                icon: "puzzlepiece.extension.fill",
                color: .blue,
                title: "Module",
                subtitle: "Frameworks",
                description: "Auth, Camera, Face Camera, Chat, Paywall, Settings"
            ) { selectedTab = "component"; scrollTarget = "module" }

            ModuleCard(
                icon: "sparkles.tv.fill",
                color: .orange,
                title: "Animation",
                subtitle: "Components",
                description: "Shimmer, TypewriterText, OrbitingLogos, and more"
            ) { selectedTab = "component"; scrollTarget = "animation" }

            ModuleCard(
                icon: "chart.bar.fill",
                color: .green,
                title: "Chart",
                subtitle: "Components",
                description: "Line, Bar, Area, Donut, Radar, Scatter, and more"
            ) { selectedTab = "component"; scrollTarget = "chart" }

            ModuleCard(
                icon: "square.grid.2x2.fill",
                color: .purple,
                title: "Component",
                subtitle: "Components",
                description: "Display, Feedback, Input — ready to use"
            ) { selectedTab = "component"; scrollTarget = "display" }
        }
    }

    // MARK: - Footer

    private var footer: some View {
        Link(destination: URL(string: "https://shipswift.app")!) {
            Text("Made with \u{2661} by SignerLabs")
                .font(.caption)
                .foregroundStyle(.secondary)
        }
        .padding(.top, 8)
    }
}

// MARK: - Module Card

private struct ModuleCard: View {
    let icon: String
    let color: Color
    let title: String
    let subtitle: String
    let description: String
    let onTap: () -> Void

    var body: some View {
        Button {
            onTap()
        } label: {
            VStack(alignment: .leading, spacing: 6) {
                Image(systemName: icon)
                    .font(.title2)
                    .foregroundStyle(color)

                Text(title)
                    .font(.headline)
                    .foregroundStyle(.primary)

                Text(subtitle)
                    .font(.caption)
                    .foregroundStyle(color)

                Text(description)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .lineLimit(2)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding(12)
            .background(
                RoundedRectangle(cornerRadius: 12)
                    #if canImport(UIKit)
                    .fill(Color(UIColor.secondarySystemGroupedBackground))
                    #else
                    .fill(Color(NSColor.controlBackgroundColor))
                    #endif
            )
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Preview

#Preview {
    HomeView(selectedTab: .constant("home"), scrollTarget: .constant(nil))
        .environment(SWStoreManager.shared)
        .environment(SWUserManager(skipAuthCheck: true))
        .swAlert()
}
```

## File: `ShipSwift/View/ProPaywallView.swift`
```
//
//  ProPaywallView.swift
//  ShipSwift
//
//  Custom paywall for non-consumable lifetime purchase.
//  Handles purchase flow without requiring sign-in.
//  After purchase, prompts user to sign in to get their API key.
//
//  Created by ShipSwift on 2/27/26.
//

import SwiftUI
import StoreKit

struct ProPaywallView: View {
    @Environment(SWStoreManager.self) private var storeManager
    @Environment(SWUserManager.self) private var userManager
    @Environment(\.dismiss) private var dismiss

    @State private var isPurchasing = false
    @State private var showAuth = false
    @State private var isSyncing = false

    private let features: [(icon: String, text: String)] = [
        ("cpu.fill", "AI-optimized recipes for all llm"),
        ("checkmark.seal.fill", "Full-stack iOS + AWS backend"),
        ("terminal.fill", "One MCP command — instant access"),
        ("arrow.triangle.branch", "Lifetime updates"),
    ]

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 24) {
                    header
                    featureList
                    purchaseSection
                    footerLinks
                }
                .padding()
                .padding(.bottom, 20)
            }
            #if canImport(UIKit)
            .background(Color(UIColor.systemGroupedBackground))
            #else
            .background(Color(NSColor.windowBackgroundColor))
            #endif
            .toolbarTitleDisplayMode(.inline)
            #if os(iOS)
            .fullScreenCover(isPresented: $showAuth) {
                NavigationStack {
                    ShipSwiftAuthView()
                        .environment(userManager)
                }
            }
            #else
            .sheet(isPresented: $showAuth) {
                NavigationStack {
                    ShipSwiftAuthView()
                        .environment(userManager)
                }
            }
            #endif
            .onChange(of: userManager.sessionState) { _, newState in
                if newState.isSignedIn {
                    showAuth = false
                    // Auto-sync purchase to server after sign-in
                    Task { await syncAndDismiss() }
                }
            }
            .task {
                // Pre-load the lifetime product for display
                await storeManager.loadLifetimeProduct()
            }
        }
    }

    // MARK: - Header

    private var header: some View {
        VStack(spacing: 16) {
            SWShakingIcon(
                image: Image(.shipSwiftLogo),
                height: 80,
                cornerRadius: 12,
                idleDelay: 6
            )
            .padding(.vertical)

            Text("ShipSwift Pro")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Ship your iOS app 10x faster")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding(.top, 8)
    }

    // MARK: - Feature List

    private var featureList: some View {
        VStack(alignment: .leading, spacing: 10) {
            ForEach(features, id: \.icon) { feature in
                HStack(spacing: 10) {
                    Image(systemName: feature.icon)
                        .foregroundStyle(.accent)
                        .imageScale(.small)
                        .frame(width: 20)
                    Text(feature.text)
                        .font(.subheadline)
                }
            }
        }
        .padding(.vertical, 8)
    }

    // MARK: - Purchase Section

    private var purchaseSection: some View {
        VStack(spacing: 16) {
            if storeManager.isPro {
                // Already Pro
                proStatusSection
            } else if let product = storeManager.lifetimeProduct {
                // Show purchase button
                Button {
                    Task { await purchase(product) }
                } label: {
                    HStack {
                        if isPurchasing {
                            ProgressView()
                                .tint(.white)
                        }
                        Text(isPurchasing ? "Processing..." : "Buy Now — \(product.displayPrice)")
                            .font(.headline)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
                }
                .buttonStyle(.borderedProminent)
                .clipShape(RoundedRectangle(cornerRadius: 14))
                .disabled(isPurchasing)

                Text("One-time purchase. No subscription.")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            } else {
                // Loading product
                ProgressView("Loading...")
            }
        }
    }

    private var proStatusSection: some View {
        VStack(spacing: 12) {
            Label("Pro Unlocked", systemImage: "checkmark.seal.fill")
                .font(.headline)
                .foregroundStyle(.green)

            if !userManager.sessionState.isSignedIn {
                Button {
                    showAuth = true
                } label: {
                    Text("Sign in to get your API Key")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 14)
                }
                .buttonStyle(.borderedProminent)
                .clipShape(RoundedRectangle(cornerRadius: 14))
            } else if isSyncing {
                ProgressView("Syncing purchase...")
            } else {
                Button { dismiss() } label: {
                    Text("Done")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 14)
                }
                .buttonStyle(.borderedProminent)
                .clipShape(RoundedRectangle(cornerRadius: 14))
            }
        }
    }

    // MARK: - Footer Links

    private var footerLinks: some View {
        VStack(spacing: 12) {
            Button("Restore Purchases") {
                Task { await restorePurchases() }
            }
            .font(.subheadline)

            HStack(spacing: 16) {
                Link("Terms of Service", destination: URL(string: "https://shipswift.app/terms")!)
                Link("Privacy Policy", destination: URL(string: "https://shipswift.app/privacy")!)
            }
            .font(.caption)
            .foregroundStyle(.secondary)
        }
        .padding(.top, 8)
    }

    // MARK: - Actions

    private func purchase(_ product: Product) async {
        isPurchasing = true
        defer { isPurchasing = false }

        do {
            let result = try await product.purchase()
            switch result {
            case .success(let verification):
                if case .verified(let transaction) = verification {
                    await transaction.finish()
                    await storeManager.updatePurchaseStatus()
                    #if os(iOS)
                    SWTikTokTrackingManager.shared.track(.purchase, properties: [
                        "product_id": product.id,
                        "price": product.displayPrice
                    ])
                    #endif

                    // If already signed in, auto-sync to server
                    if userManager.sessionState.isSignedIn {
                        await syncAndDismiss()
                    }
                    // Otherwise, UI will show "Sign in to get your API Key"
                }
            case .pending:
                SWAlertManager.shared.show(.info, message: "Purchase pending approval")
            case .userCancelled:
                break
            @unknown default:
                break
            }
        } catch {
            SWAlertManager.shared.show(.error, message: "Purchase failed: \(error.localizedDescription)")
        }
    }

    private func syncAndDismiss() async {
        isSyncing = true
        defer { isSyncing = false }

        guard let idToken = await userManager.getFreshIdToken() else { return }
        let apiKey = await storeManager.syncPurchaseToServer(idToken: idToken)
        if apiKey != nil {
            SWAlertManager.shared.show(.success, message: "API Key generated!")
        }
        dismiss()
    }

    private func restorePurchases() async {
        do {
            try await AppStore.sync()
            await storeManager.updatePurchaseStatus()
            if storeManager.isPro {
                SWAlertManager.shared.show(.success, message: "Purchases restored!")
            } else {
                SWAlertManager.shared.show(.info, message: "No previous purchases found")
            }
        } catch {
            SWAlertManager.shared.show(.error, message: "Restore failed: \(error.localizedDescription)")
        }
    }
}
```

## File: `ShipSwift/View/RootTabView.swift`
```
//
//  RootTabView.swift
//  ShipSwift
//
//  Created by Wei Zhong on 12/2/26.
//

import SwiftUI

struct RootTabView: View {
    @State private var selectedTab = "home"
    @State private var scrollTarget: String?

    var body: some View {
        #if os(iOS)
        iOSBody
        #else
        macOSBody
        #endif
    }
}

// MARK: - iOS Body

#if os(iOS)
extension RootTabView {
    var iOSBody: some View {
        TabView(selection: $selectedTab) {
            Tab(value: "home") {
                HomeView(selectedTab: $selectedTab, scrollTarget: $scrollTarget)
            } label: {
                Label {
                    Text("ShipSwift")
                } icon: {
                    Image(systemName: selectedTab == "home" ? "house.fill" : "house")
                }
                .environment(\.symbolVariants, .none)
            }

            Tab(value: "chat") {
                ChatView()
            } label: {
                Label {
                    Text("Chat")
                } icon: {
                    Image(systemName: selectedTab == "chat" ? "bubble.left.and.bubble.right.fill" : "bubble.left.and.bubble.right")
                }
                .environment(\.symbolVariants, .none)
            }

            Tab(value: "component") {
                ComponentView(scrollTarget: $scrollTarget)
            } label: {
                Label {
                    Text("Component")
                } icon: {
                    Image(systemName: selectedTab == "component" ? "square.grid.2x2.fill" : "square.grid.2x2")
                }
                .environment(\.symbolVariants, .none)
            }
        }
        .sensoryFeedback(.increase, trigger: selectedTab)
    }
}
#endif

// MARK: - macOS Body

#if os(macOS)
extension RootTabView {
    var macOSBody: some View {
        ComponentView(scrollTarget: $scrollTarget)
    }
}
#endif

// MARK: - Preview

#Preview {
    RootTabView()
}
```

## File: `ShipSwift/View/SettingView.swift`
```
//
//  SettingView.swift
//  ShipSwift
//
//  Settings page for the ShipSwift Showcase App.
//  Includes Pro status, API key management, account, recommended apps,
//  share, legal links, and version info.
//
//  Created by Wei Zhong on 13/2/26.
//

import SwiftUI
import StoreKit

struct SettingView: View {
    @Environment(SWStoreManager.self) private var storeManager
    @Environment(SWUserManager.self) private var userManager

    // MARK: - State

    @State private var showPaywall = false
    @State private var showAuth = false
    @State private var isSyncing = false
    @State private var showDeleteConfirmation = false

    // MARK: - Configuration

    private let appStoreURL = URL(string: "https://apps.apple.com/app/id6759209764")!
    private let termsURL = URL(string: "https://shipswift.app/terms")!
    private let privacyURL = URL(string: "https://shipswift.app/privacy")!

    // App Store links for recommended apps
    private let appStoreFullpack = "https://apps.apple.com/us/app/fullpack-packing-outfit/id6745692929"
    private let appStoreBrushmo = "https://apps.apple.com/us/app/brushmo/id6744569822"
    private let appStoreLifebang = "https://apps.apple.com/us/app/lifebang/id6474886848"
    private let appStoreUtilityMax = "https://apps.apple.com/us/app/utilitymax%E6%95%88%E5%BA%A6%E5%AE%B6-%E7%BB%88%E8%BA%AB%E8%B4%A2%E5%8A%A1%E6%A8%A1%E6%8B%9F%E4%B8%8E%E9%80%80%E4%BC%91%E8%A7%84%E5%88%92%E5%99%A8/id6758595049"
    private let appStoreJourney = "https://apps.apple.com/us/app/journey-goal-tracker-diary/id6748666816"
    private let appStoreSmileMax = "https://apps.apple.com/us/app/smilemax/id6758947123"

    /// App version number
    private var appVersion: String {
        Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0.0"
    }

    /// App build number
    private var buildNumber: String {
        Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
    }

    // MARK: - Body

    var body: some View {
        NavigationStack {
            List {
                proSection
                if userManager.sessionState.isSignedIn { accountSection }
                recommendedAppsSection
                generalSection
                legalSection
                versionSection
            }
            .navigationTitle("Settings")
            .toolbarTitleDisplayMode(.inlineLarge)
            .sheet(isPresented: $showPaywall) {
                ProPaywallView()
                    .environment(storeManager)
                    .environment(userManager)
            }
            #if os(iOS)
            .fullScreenCover(isPresented: $showAuth) {
                NavigationStack {
                    ShipSwiftAuthView()
                        .environment(userManager)
                }
            }
            #else
            .sheet(isPresented: $showAuth) {
                NavigationStack {
                    ShipSwiftAuthView()
                        .environment(userManager)
                }
            }
            #endif
            .onChange(of: userManager.sessionState) { _, newState in
                if newState.isSignedIn {
                    showAuth = false
                    Task { await syncProStatus() }
                }
            }
            .alert("Delete Account", isPresented: $showDeleteConfirmation) {
                Button("Delete", role: .destructive) {
                    Task {
                        try? await userManager.deleteAccount()
                    }
                }
                Button("Cancel", role: .cancel) {}
            } message: {
                Text("This action cannot be undone. Your account and all associated data will be permanently deleted.")
            }
        }
    }

    // MARK: - Pro Section

    private var proSection: some View {
        Section {
            if storeManager.isPro {
                // Pro status
                HStack {
                    Label("ShipSwift Pro", systemImage: "checkmark.seal.fill")
                        .foregroundStyle(.green)
                    Spacer()
                    Text("Active")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }

                // API Key management
                if userManager.sessionState.isSignedIn {
                    apiKeyRow
                } else {
                    Button {
                        showAuth = true
                    } label: {
                        Label("Sign in to get your API Key", systemImage: "person.badge.key.fill")
                    }
                }
            } else {
                // Upgrade button
                Button {
                    showPaywall = true
                } label: {
                    HStack {
                        Label("Upgrade to Pro", systemImage: "star.fill")
                            .foregroundStyle(.accent)
                        Spacer()
                        Image(systemName: "chevron.right")
                            .font(.footnote)
                            .foregroundStyle(.secondary)
                    }
                }
            }

            // Restore Purchases
            Button {
                Task { await restorePurchases() }
            } label: {
                Label("Restore Purchases", systemImage: "arrow.clockwise")
            }
        } header: {
            Text("Pro")
        }
    }

    // MARK: - API Key Row

    private var apiKeyRow: some View {
        Group {
            if let masked = storeManager.apiKey {
                Button {
                    Task { await copyKey() }
                } label: {
                    HStack {
                        Label {
                            Text(masked)
                                .font(.system(.subheadline, design: .monospaced))
                                .lineLimit(1)
                        } icon: {
                            Image(systemName: "key.fill")
                        }
                        Spacer()
                        Image(systemName: "doc.on.doc")
                            .foregroundStyle(.secondary)
                    }
                }
            } else if isSyncing {
                HStack {
                    Label("Syncing purchase...", systemImage: "key.fill")
                    Spacer()
                    ProgressView()
                }
            } else {
                Button {
                    Task { await syncProStatus() }
                } label: {
                    Label("Get API Key", systemImage: "key.fill")
                }
            }
        }
    }

    // MARK: - Account Section

    private var accountSection: some View {
        Section("Account") {
            HStack {
                Label("Email", systemImage: "envelope")
                Spacer()
                Text(extractEmail())
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
            }

            Button {
                Task { await userManager.signOut() }
            } label: {
                Label("Sign Out", systemImage: "rectangle.portrait.and.arrow.right")
            }

            Button(role: .destructive) {
                showDeleteConfirmation = true
            } label: {
                Label("Delete Account", systemImage: "trash")
                    .foregroundStyle(.red)
            }
        }
    }

    // MARK: - Other Sections

    private var recommendedAppsSection: some View {
        Section("Apps Built with ShipSwift") {
            Link(destination: URL(string: appStoreSmileMax)!) {
                labelWithImage(.smileMaxLogo, name: "SmileMax - Glow Up Coach")
            }
            Link(destination: URL(string: appStoreFullpack)!) {
                labelWithImage(.fullpackLogo, name: "Fullpack - Packing & Outfit")
            }
            Link(destination: URL(string: appStoreBrushmo)!) {
                labelWithImage(.brushmoLogo, name: "Brushmo - Oral Health Companion")
            }
            Link(destination: URL(string: appStoreLifebang)!) {
                labelWithImage(.lifebangLogo, name: "Lifebang - Pro Cleaner")
            }
            Link(destination: URL(string: appStoreUtilityMax)!) {
                labelWithImage(.utilityMaxLogo, name: "UtilityMax - Financial Simulator")
            }
            Link(destination: URL(string: appStoreJourney)!) {
                labelWithImage(.journeyLogo, name: "Spark - Goal Tracker & Diary")
            }
        }
    }

    private var generalSection: some View {
        Section {
            ShareLink(item: appStoreURL) {
                HStack {
                    Text("Share App")
                    Spacer()
                    Image(systemName: "square.and.arrow.up")
                        .foregroundStyle(.secondary)
                }
            }
        }
    }

    private var legalSection: some View {
        Section {
            Link(destination: termsURL) {
                HStack {
                    Text("Terms of Service")
                    Spacer()
                    Image(systemName: "chevron.right")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }

            Link(destination: privacyURL) {
                HStack {
                    Text("Privacy Policy")
                    Spacer()
                    Image(systemName: "chevron.right")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }

    private var versionSection: some View {
        Section {
            LabeledContent("Version") {
                Text("v\(appVersion) (\(buildNumber))")
                    .foregroundStyle(.secondary)
            }
        }
    }

    // MARK: - Helpers

    @ViewBuilder
    private func labelWithImage(_ image: ImageResource, name: LocalizedStringResource) -> some View {
        HStack {
            Image(image)
                .resizable()
                .scaledToFit()
                .frame(width: 32, height: 32)
                .clipShape(RoundedRectangle(cornerRadius: 6))
                .padding(5)
            Text(name)
        }
    }

    private func extractEmail() -> String {
        // Decode email from JWT id token
        guard let idToken = userManager.sessionState.tokens?.idToken else { return "" }
        let parts = idToken.split(separator: ".")
        guard parts.count >= 2,
              let data = Data(base64Encoded: String(parts[1]).padding(toLength: ((parts[1].count + 3) / 4) * 4, withPad: "=", startingAt: 0)),
              let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
              let email = json["email"] as? String else {
            return ""
        }
        return email
    }

    // MARK: - Actions

    private func syncProStatus() async {
        guard let idToken = await userManager.getFreshIdToken() else { return }
        isSyncing = true
        defer { isSyncing = false }

        // If user has a local purchase, sync it to server
        if storeManager.hasLifetimePurchase {
            _ = await storeManager.syncPurchaseToServer(idToken: idToken)
        }

        // Check server status
        await storeManager.checkServerProStatus(idToken: idToken)
    }

    private func copyKey() async {
        guard let idToken = await userManager.getFreshIdToken() else { return }
        do {
            let service = ShipSwiftAPIService()
            let key = try await service.revealApiKey(idToken: idToken)
            #if os(iOS)
            UIPasteboard.general.string = key
            #else
            NSPasteboard.general.clearContents()
            NSPasteboard.general.setString(key, forType: .string)
            #endif
            SWAlertManager.shared.show(.success, message: "API Key copied to clipboard")
        } catch {
            SWAlertManager.shared.show(.error, message: "Failed to copy API key")
        }
    }

    private func restorePurchases() async {
        do {
            try await AppStore.sync()
            await storeManager.updatePurchaseStatus()
            if storeManager.isPro {
                SWAlertManager.shared.show(.success, message: "Purchases restored!")
            } else {
                SWAlertManager.shared.show(.info, message: "No previous purchases found")
            }
        } catch {
            SWAlertManager.shared.show(.error, message: "Restore failed")
        }
    }
}

#Preview {
    SettingView()
        .environment(SWStoreManager.shared)
        .environment(SWUserManager(skipAuthCheck: true))
}
```

## File: `ShipSwift/View/ShipSwiftAuthView.swift`
```
//
//  ShipSwiftAuthView.swift
//  ShipSwift
//
//  Email-only authentication view for the ShipSwift Showcase app.
//  Supports sign in, sign up, email verification, and password reset.
//  No phone, Apple, or Google sign-in (to ensure cross-platform account linking).
//
//  Created by ShipSwift on 2/27/26.
//

import SwiftUI
import Amplify
import AWSCognitoAuthPlugin

#if os(iOS)
private typealias SWTextContentType = UITextContentType
#else
private typealias SWTextContentType = NSTextContentType
#endif

struct ShipSwiftAuthView: View {

    // MARK: - Environment

    @Environment(SWUserManager.self) private var userManager
    @Environment(\.dismiss) private var dismiss

    // MARK: - View Mode

    private enum ViewMode {
        case signIn
        case signUp
        case confirmSignUp
        case forgotPassword
        case resetPassword
    }

    private enum LoadingState {
        case idle
        case loading
    }

    // MARK: - State

    @State private var viewMode: ViewMode = .signIn
    @State private var loadingState: LoadingState = .idle
    @State private var agreementChecked = false
    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    @State private var verificationCode = ""
    @State private var newPassword = ""
    @State private var confirmNewPassword = ""
    @State private var resetCode = ""
    @FocusState private var isCodeFocused: Bool

    private let termsURL = URL(string: "https://www.shipswift.app/terms")!
    private let privacyURL = URL(string: "https://www.shipswift.app/privacy")!

    // MARK: - Validation

    private var isValidEmail: Bool {
        email.range(of: #"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"#, options: .regularExpression) != nil
    }

    private var isValidPassword: Bool { password.count >= 8 }
    private var passwordsMatch: Bool { password == confirmPassword }
    private var isValidCode: Bool { verificationCode.count == 6 }
    private var isValidResetCode: Bool { resetCode.count == 6 }
    private var isValidNewPassword: Bool { newPassword.count >= 8 }
    private var newPasswordsMatch: Bool { newPassword == confirmNewPassword }

    private var isLoading: Bool { loadingState == .loading }

    // MARK: - Body

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                Spacer(minLength: 40)
                header
                Spacer(minLength: 20)

                switch viewMode {
                case .signIn:       signInSection
                case .signUp:       signUpSection
                case .confirmSignUp: confirmSignUpSection
                case .forgotPassword: forgotPasswordSection
                case .resetPassword: resetPasswordSection
                }
            }
            .padding()
        }
        #if os(iOS)
        .scrollDismissesKeyboard(.interactively)
        .navigationBarTitleDisplayMode(.inline)
        #endif
        .toolbar {
            ToolbarItem(placement: .cancellationAction) {
                Button { dismiss() } label: {
                    Image(systemName: "xmark")
                        .foregroundStyle(.secondary)
                }
            }
        }
        .swAlert()
    }

    // MARK: - Header

    private var header: some View {
        VStack(spacing: 8) {
            Image(.shipSwiftLogo)
                .resizable()
                .scaledToFit()
                .frame(width: 80, height: 80)
                .clipShape(RoundedRectangle(cornerRadius: 16))

            Text(headerTitle)
                .font(.title)
                .fontWeight(.bold)

            Text(headerSubtitle)
                .foregroundStyle(.secondary)
                .multilineTextAlignment(.center)
        }
    }

    private var headerTitle: String {
        switch viewMode {
        case .signIn:         "Welcome Back"
        case .signUp:         "Create Account"
        case .confirmSignUp:  "Verify Email"
        case .forgotPassword: "Forgot Password"
        case .resetPassword:  "Reset Password"
        }
    }

    private var headerSubtitle: String {
        switch viewMode {
        case .signIn:         "Sign in to manage your API key"
        case .signUp:         "Create an account with your email"
        case .confirmSignUp:  "Enter the 6-digit code sent to \(email)"
        case .forgotPassword: "Enter your email to receive a reset code"
        case .resetPassword:  "Enter the code and your new password"
        }
    }

    // MARK: - Sign In

    private var signInSection: some View {
        VStack(spacing: 12) {
            emailField
            passwordField(text: $password, placeholder: "Password", contentType: .password)

            SWAgreementChecker(
                agreementChecked: $agreementChecked,
                termsURL: termsURL,
                privacyURL: privacyURL
            )

            actionButton(
                title: "Sign In",
                loadingTitle: "Signing In...",
                disabled: !isValidEmail || !isValidPassword || !agreementChecked
            ) {
                await signIn()
            }

            Button {
                withAnimation { viewMode = .forgotPassword }
            } label: {
                Text("Forgot Password?")
                    .font(.subheadline)
                    .foregroundStyle(.accent)
            }

            Button {
                withAnimation { viewMode = .signUp; confirmPassword = "" }
            } label: {
                Text("Don't have an account? Sign Up")
                    .font(.subheadline)
                    .foregroundStyle(.accent)
            }
        }
        .padding(.vertical)
    }

    // MARK: - Sign Up

    private var signUpSection: some View {
        VStack(spacing: 12) {
            emailField
            passwordField(text: $password, placeholder: "Password", contentType: .newPassword)

            if !password.isEmpty {
                passwordHint(valid: isValidPassword)
            }

            passwordField(text: $confirmPassword, placeholder: "Confirm Password", contentType: .newPassword)

            if !confirmPassword.isEmpty && !passwordsMatch {
                Text("Passwords do not match")
                    .font(.caption)
                    .foregroundStyle(.red)
            }

            SWAgreementChecker(
                agreementChecked: $agreementChecked,
                termsURL: termsURL,
                privacyURL: privacyURL
            )

            actionButton(
                title: "Create Account",
                loadingTitle: "Creating Account...",
                disabled: !isValidEmail || !isValidPassword || !passwordsMatch || !agreementChecked
            ) {
                await signUp()
            }

            Button {
                withAnimation { viewMode = .signIn }
            } label: {
                Text("Already have an account? Sign In")
                    .font(.subheadline)
                    .foregroundStyle(.accent)
            }
        }
        .padding(.vertical)
    }

    // MARK: - Confirm Sign Up

    private var confirmSignUpSection: some View {
        VStack(spacing: 16) {
            codeField(text: $verificationCode)

            actionButton(
                title: "Verify Email",
                loadingTitle: "Verifying...",
                disabled: !isValidCode
            ) {
                await confirmSignUp()
            }

            Button {
                Task { await resendCode() }
            } label: {
                Text("Resend Code")
                    .font(.subheadline)
                    .foregroundStyle(.accent)
            }

            backToSignIn
        }
        .padding(.vertical)
        .task {
            try? await Task.sleep(for: .milliseconds(300))
            isCodeFocused = true
        }
    }

    // MARK: - Forgot Password

    private var forgotPasswordSection: some View {
        VStack(spacing: 16) {
            emailField

            actionButton(
                title: "Send Reset Code",
                loadingTitle: "Sending...",
                disabled: !isValidEmail
            ) {
                await sendResetCode()
            }

            backToSignIn
        }
        .padding(.vertical)
    }

    // MARK: - Reset Password

    private var resetPasswordSection: some View {
        VStack(spacing: 16) {
            VStack(alignment: .leading, spacing: 4) {
                Text("Verification Code")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                codeField(text: $resetCode)
            }

            VStack(alignment: .leading, spacing: 4) {
                Text("New Password")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                passwordField(text: $newPassword, placeholder: "New Password", contentType: .newPassword)
            }

            if !newPassword.isEmpty {
                passwordHint(valid: isValidNewPassword)
            }

            VStack(alignment: .leading, spacing: 4) {
                Text("Confirm New Password")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                passwordField(text: $confirmNewPassword, placeholder: "Confirm New Password", contentType: .newPassword)

                if !confirmNewPassword.isEmpty && !newPasswordsMatch {
                    Text("Passwords do not match")
                        .font(.caption)
                        .foregroundStyle(.red)
                }
            }

            actionButton(
                title: "Reset Password",
                loadingTitle: "Resetting...",
                disabled: !isValidResetCode || !isValidNewPassword || !newPasswordsMatch
            ) {
                await confirmResetPassword()
            }

            backToSignIn
        }
        .padding(.vertical)
    }

    // MARK: - Reusable Components

    private var emailField: some View {
        HStack {
            Image(systemName: "envelope")
                .foregroundStyle(.secondary)
            TextField("Email", text: $email)
                #if os(iOS)
                .keyboardType(.emailAddress)
                #endif
                .textContentType(.emailAddress)
                #if os(iOS)
                .textInputAutocapitalization(.never)
                #endif
                .autocorrectionDisabled()
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 14)
        .background(.accent.opacity(0.1))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }

    private func passwordField(text: Binding<String>, placeholder: String, contentType: SWTextContentType) -> some View {
        HStack {
            Image(systemName: "lock")
                .foregroundStyle(.secondary)
            SecureField(placeholder, text: text)
                .textContentType(contentType)
        }
        .padding(.horizontal, 16)
        .padding(.vertical, 14)
        .background(.accent.opacity(0.1))
        .clipShape(RoundedRectangle(cornerRadius: 12))
    }

    private func codeField(text: Binding<String>) -> some View {
        TextField("000000", text: text)
            #if os(iOS)
            .keyboardType(.numberPad)
            #endif
            .textContentType(.oneTimeCode)
            .focused($isCodeFocused)
            .multilineTextAlignment(.center)
            .font(.title2.monospacedDigit())
            .padding(.vertical, 16)
            .background(.accent.opacity(0.1))
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .onChange(of: text.wrappedValue) { _, newValue in
                text.wrappedValue = String(newValue.filter(\.isNumber).prefix(6))
            }
    }

    private func passwordHint(valid: Bool) -> some View {
        HStack(spacing: 4) {
            Image(systemName: valid ? "checkmark.circle.fill" : "circle")
                .foregroundStyle(valid ? .green : .secondary)
            Text("At least 8 characters")
                .foregroundStyle(valid ? .primary : .secondary)
        }
        .font(.caption)
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(.horizontal, 4)
    }

    private func actionButton(title: String, loadingTitle: String, disabled: Bool, action: @escaping () async -> Void) -> some View {
        Button {
            Task { await action() }
        } label: {
            HStack {
                if isLoading {
                    ProgressView()
                        .tint(.white)
                }
                Text(isLoading ? loadingTitle : title)
            }
            .font(.headline)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 14)
        }
        .buttonStyle(.borderedProminent)
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .disabled(disabled || isLoading)
    }

    private var backToSignIn: some View {
        Button {
            withAnimation {
                viewMode = .signIn
                verificationCode = ""
                resetCode = ""
                newPassword = ""
                confirmNewPassword = ""
            }
        } label: {
            Text("Back to Sign In")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }

    // MARK: - Actions

    private func signIn() async {
        loadingState = .loading
        defer { loadingState = .idle }
        do {
            try await userManager.signIn(email: email, password: password)
        } catch {
            showError(error)
        }
    }

    private func signUp() async {
        loadingState = .loading
        defer { loadingState = .idle }
        do {
            try await userManager.signUp(email: email, password: password)
            withAnimation { viewMode = .confirmSignUp }
        } catch {
            showError(error)
        }
    }

    private func confirmSignUp() async {
        loadingState = .loading
        defer { loadingState = .idle }
        do {
            try await userManager.confirmSignUp(email: email, code: verificationCode)
            try await userManager.signIn(email: email, password: password)
            #if os(iOS)
            SWTikTokTrackingManager.shared.track(.completeRegistration)
            #endif
        } catch {
            showError(error)
        }
    }

    private func resendCode() async {
        do {
            try await userManager.resendSignUpCode(email: email)
            SWAlertManager.shared.show(.success, message: "Code sent to \(email)")
        } catch {
            showError(error)
        }
    }

    private func sendResetCode() async {
        loadingState = .loading
        defer { loadingState = .idle }
        do {
            try await userManager.forgotPassword(email: email)
            withAnimation { viewMode = .resetPassword }
        } catch {
            showError(error)
        }
    }

    private func confirmResetPassword() async {
        loadingState = .loading
        defer { loadingState = .idle }
        do {
            try await userManager.confirmResetPassword(email: email, newPassword: newPassword, code: resetCode)
            SWAlertManager.shared.show(.success, message: "Password reset successfully")
            withAnimation {
                viewMode = .signIn
                resetCode = ""
                newPassword = ""
                confirmNewPassword = ""
                password = ""
            }
        } catch {
            showError(error)
        }
    }

    // MARK: - Error Handling

    private func showError(_ error: Error) {
        swDebugLog("Auth error: \(error)")
        let message: String
        if let authError = error as? AuthError {
            swDebugLog("AuthError: \(authError.errorDescription), underlying: \(String(describing: authError.underlyingError))")
            if let cognitoError = authError.underlyingError as? AWSCognitoAuthError {
                message = cognitoMessage(cognitoError)
            } else {
                message = authMessage(authError)
            }
        } else {
            message = error.localizedDescription
        }
        SWAlertManager.shared.show(.error, message: message)
    }

    private func authMessage(_ error: AuthError) -> String {
        switch error {
        case .notAuthorized:
            return "Incorrect email or password"
        case .validation:
            return "Invalid input"
        default:
            let desc = error.errorDescription.lowercased()
            if desc.contains("incorrect username or password") { return "Incorrect email or password" }
            if desc.contains("user does not exist") { return "This email is not registered" }
            if desc.contains("user is not confirmed") { return "Please verify your email first" }
            return "Something went wrong, please try again"
        }
    }

    private func cognitoMessage(_ error: AWSCognitoAuthError) -> String {
        switch error {
        case .userNotFound:      "This email is not registered"
        case .userNotConfirmed:  "Please verify your email first"
        case .usernameExists:    "This email is already registered"
        case .codeMismatch:      "Incorrect verification code"
        case .codeExpired:       "Verification code expired"
        case .invalidPassword:   "Password must be at least 8 characters"
        case .limitExceeded, .requestLimitExceeded:
            "Too many attempts, please try again later"
        default:                 "An error occurred, please try again"
        }
    }
}

#Preview {
    NavigationStack {
        ShipSwiftAuthView()
            .environment(SWUserManager(skipAuthCheck: true))
    }
}
```

## File: `ShipSwift.xcodeproj/project.pbxproj`
```
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 77;
	objects = {

/* Begin PBXBuildFile section */
		9B1A79252F51C2C800DDF343 /* TikTokBusinessSDK in Frameworks */ = {isa = PBXBuildFile; platformFilter = ios; productRef = 9B1A79242F51C2C800DDF343 /* TikTokBusinessSDK */; };
		9B98BB222F27490700CA9857 /* AWSAPIPlugin in Frameworks */ = {isa = PBXBuildFile; productRef = 9B98BB212F27490700CA9857 /* AWSAPIPlugin */; };
		9B98BB242F27490700CA9857 /* AWSCognitoAuthPlugin in Frameworks */ = {isa = PBXBuildFile; productRef = 9B98BB232F27490700CA9857 /* AWSCognitoAuthPlugin */; };
		9B98BB262F27490700CA9857 /* AWSPluginsCore in Frameworks */ = {isa = PBXBuildFile; productRef = 9B98BB252F27490700CA9857 /* AWSPluginsCore */; };
		9B98BB282F27490700CA9857 /* Amplify in Frameworks */ = {isa = PBXBuildFile; productRef = 9B98BB272F27490700CA9857 /* Amplify */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		B69605ED2EEFD462006F81F3 /* ShipSwift.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = ShipSwift.app; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFileSystemSynchronizedBuildFileExceptionSet section */
		9B1A7E4B2F57B31600DDF343 /* Exceptions for "ShipSwift" folder in "ShipSwift" target */ = {
			isa = PBXFileSystemSynchronizedBuildFileExceptionSet;
			membershipExceptions = (
				Info.plist,
			);
			platformFiltersByRelativePath = {
				"SWPackage/SWComponent/Display/SWScrollingFAQ+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWAuth/SWAuthView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWAuth/SWAuthView+macOS.swift" = (macos, );
				"SWPackage/SWModule/SWCamera/SWCameraManager+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWCamera/SWCameraView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWCamera/SWFaceCameraView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWCamera/SWFaceLandmark+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWChat/SWChatInputView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWChat/SWChatView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWChat/SWMessageList+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWChat/SWVolcEngineASRService+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWSetting/SWSettingView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWSetting/SWSettingView+macOS.swift" = (macos, );
				"SWPackage/SWModule/SWSubjectLifting/SWSubjectLiftingManager+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWSubjectLifting/SWSubjectLiftingView+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWTikTokTracking/SWTikTokTrackingManager+iOS.swift" = (ios, );
				"SWPackage/SWModule/SWTikTokTracking/SWTikTokTrackingView+iOS.swift" = (ios, );
			};
			target = B69605EC2EEFD462006F81F3 /* ShipSwift */;
		};
/* End PBXFileSystemSynchronizedBuildFileExceptionSet section */

/* Begin PBXFileSystemSynchronizedRootGroup section */
		B69605EF2EEFD462006F81F3 /* ShipSwift */ = {
			isa = PBXFileSystemSynchronizedRootGroup;
			exceptions = (
				9B1A7E4B2F57B31600DDF343 /* Exceptions for "ShipSwift" folder in "ShipSwift" target */,
			);
			path = ShipSwift;
			sourceTree = "<group>";
		};
/* End PBXFileSystemSynchronizedRootGroup section */

/* Begin PBXFrameworksBuildPhase section */
		B69605EA2EEFD462006F81F3 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				9B98BB222F27490700CA9857 /* AWSAPIPlugin in Frameworks */,
				9B1A79252F51C2C800DDF343 /* TikTokBusinessSDK in Frameworks */,
				9B98BB282F27490700CA9857 /* Amplify in Frameworks */,
				9B98BB242F27490700CA9857 /* AWSCognitoAuthPlugin in Frameworks */,
				9B98BB262F27490700CA9857 /* AWSPluginsCore in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		B69605E42EEFD462006F81F3 = {
			isa = PBXGroup;
			children = (
				B69605EF2EEFD462006F81F3 /* ShipSwift */,
				B69605EE2EEFD462006F81F3 /* Products */,
			);
			sourceTree = "<group>";
		};
		B69605EE2EEFD462006F81F3 /* Products */ = {
			isa = PBXGroup;
			children = (
				B69605ED2EEFD462006F81F3 /* ShipSwift.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		B69605EC2EEFD462006F81F3 /* ShipSwift */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = B69605F82EEFD464006F81F3 /* Build configuration list for PBXNativeTarget "ShipSwift" */;
			buildPhases = (
				B69605E92EEFD462006F81F3 /* Sources */,
				B69605EA2EEFD462006F81F3 /* Frameworks */,
				B69605EB2EEFD462006F81F3 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			fileSystemSynchronizedGroups = (
				B69605EF2EEFD462006F81F3 /* ShipSwift */,
			);
			name = ShipSwift;
			packageProductDependencies = (
				9B98BB212F27490700CA9857 /* AWSAPIPlugin */,
				9B98BB232F27490700CA9857 /* AWSCognitoAuthPlugin */,
				9B98BB252F27490700CA9857 /* AWSPluginsCore */,
				9B98BB272F27490700CA9857 /* Amplify */,
				9B1A79242F51C2C800DDF343 /* TikTokBusinessSDK */,
			);
			productName = ShipSwift;
			productReference = B69605ED2EEFD462006F81F3 /* ShipSwift.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		B69605E52EEFD462006F81F3 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 2620;
				LastUpgradeCheck = 2620;
				TargetAttributes = {
					B69605EC2EEFD462006F81F3 = {
						CreatedOnToolsVersion = 26.2;
					};
				};
			};
			buildConfigurationList = B69605E82EEFD462006F81F3 /* Build configuration list for PBXProject "ShipSwift" */;
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = B69605E42EEFD462006F81F3;
			minimizedProjectReferenceProxies = 1;
			packageReferences = (
				9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */,
				9B1A79232F51C2C800DDF343 /* XCRemoteSwiftPackageReference "tiktok-business-ios-sdk" */,
			);
			preferredProjectObjectVersion = 77;
			productRefGroup = B69605EE2EEFD462006F81F3 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				B69605EC2EEFD462006F81F3 /* ShipSwift */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		B69605EB2EEFD462006F81F3 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		B69605E92EEFD462006F81F3 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		B69605F62EEFD464006F81F3 /* Debug */ = {
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
				DEAD_CODE_STRIPPING = YES;
				DEBUG_INFORMATION_FORMAT = dwarf;
				DEVELOPMENT_TEAM = 5GS4D3667R;
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
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				STRING_CATALOG_GENERATE_SYMBOLS = YES;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		B69605F72EEFD464006F81F3 /* Release */ = {
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
				DEAD_CODE_STRIPPING = YES;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				DEVELOPMENT_TEAM = 5GS4D3667R;
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
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				STRING_CATALOG_GENERATE_SYMBOLS = YES;
				SWIFT_COMPILATION_MODE = wholemodule;
			};
			name = Release;
		};
		B69605F92EEFD464006F81F3 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEAD_CODE_STRIPPING = YES;
				ENABLE_APP_SANDBOX = YES;
				ENABLE_HARDENED_RUNTIME = YES;
				ENABLE_OUTGOING_NETWORK_CONNECTIONS = YES;
				ENABLE_PREVIEWS = YES;
				ENABLE_RESOURCE_ACCESS_AUDIO_INPUT = YES;
				"ENABLE_RESOURCE_ACCESS_AUDIO_INPUT[sdk=macosx*]" = NO;
				ENABLE_RESOURCE_ACCESS_CAMERA = YES;
				"ENABLE_RESOURCE_ACCESS_CAMERA[sdk=macosx*]" = NO;
				ENABLE_USER_SELECTED_FILES = readonly;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_FILE = ShipSwift/Info.plist;
				INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
				INFOPLIST_KEY_LSApplicationCategoryType = "public.app-category.developer-tools";
				INFOPLIST_KEY_NSCameraUsageDescription = "ShipSwift uses the camera to let you try the Camera module demo. For example, you can take a photo to see how the camera component captures and displays images.";
				INFOPLIST_KEY_NSMicrophoneUsageDescription = "ShipSwift uses the microphone for the voice input demo in the Chat module. For example, you can speak a message to see how voice-to-text works in the chat component.";
				INFOPLIST_KEY_NSUserTrackingUsageDescription = "We use this to measure advertising performance and deliver relevant content to you.";
				"INFOPLIST_KEY_UIApplicationSceneManifest_Generation[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UIApplicationSceneManifest_Generation[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UILaunchScreen_Generation[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UILaunchScreen_Generation[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UIStatusBarStyle[sdk=iphoneos*]" = UIStatusBarStyleDefault;
				"INFOPLIST_KEY_UIStatusBarStyle[sdk=iphonesimulator*]" = UIStatusBarStyleDefault;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				IPHONEOS_DEPLOYMENT_TARGET = 18.0;
				LD_RUNPATH_SEARCH_PATHS = "@executable_path/Frameworks";
				"LD_RUNPATH_SEARCH_PATHS[sdk=macosx*]" = "@executable_path/../Frameworks";
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MARKETING_VERSION = 1.1.0;
				PRODUCT_BUNDLE_IDENTIFIER = "com.signerlabs.ship-swift-ios";
				PRODUCT_NAME = "$(TARGET_NAME)";
				REGISTER_APP_GROUPS = YES;
				SDKROOT = auto;
				STRING_CATALOG_GENERATE_SYMBOLS = YES;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator macosx";
				SUPPORTS_MACCATALYST = NO;
				SWIFT_APPROACHABLE_CONCURRENCY = YES;
				SWIFT_DEFAULT_ACTOR_ISOLATION = MainActor;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 1;
				XROS_DEPLOYMENT_TARGET = 26.0;
			};
			name = Debug;
		};
		B69605FA2EEFD464006F81F3 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEAD_CODE_STRIPPING = YES;
				ENABLE_APP_SANDBOX = YES;
				ENABLE_HARDENED_RUNTIME = YES;
				ENABLE_OUTGOING_NETWORK_CONNECTIONS = YES;
				ENABLE_PREVIEWS = YES;
				ENABLE_RESOURCE_ACCESS_AUDIO_INPUT = YES;
				"ENABLE_RESOURCE_ACCESS_AUDIO_INPUT[sdk=macosx*]" = NO;
				ENABLE_RESOURCE_ACCESS_CAMERA = YES;
				"ENABLE_RESOURCE_ACCESS_CAMERA[sdk=macosx*]" = NO;
				ENABLE_USER_SELECTED_FILES = readonly;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_FILE = ShipSwift/Info.plist;
				INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
				INFOPLIST_KEY_LSApplicationCategoryType = "public.app-category.developer-tools";
				INFOPLIST_KEY_NSCameraUsageDescription = "ShipSwift uses the camera to let you try the Camera module demo. For example, you can take a photo to see how the camera component captures and displays images.";
				INFOPLIST_KEY_NSMicrophoneUsageDescription = "ShipSwift uses the microphone for the voice input demo in the Chat module. For example, you can speak a message to see how voice-to-text works in the chat component.";
				INFOPLIST_KEY_NSUserTrackingUsageDescription = "We use this to measure advertising performance and deliver relevant content to you.";
				"INFOPLIST_KEY_UIApplicationSceneManifest_Generation[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UIApplicationSceneManifest_Generation[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UILaunchScreen_Generation[sdk=iphoneos*]" = YES;
				"INFOPLIST_KEY_UILaunchScreen_Generation[sdk=iphonesimulator*]" = YES;
				"INFOPLIST_KEY_UIStatusBarStyle[sdk=iphoneos*]" = UIStatusBarStyleDefault;
				"INFOPLIST_KEY_UIStatusBarStyle[sdk=iphonesimulator*]" = UIStatusBarStyleDefault;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				IPHONEOS_DEPLOYMENT_TARGET = 18.0;
				LD_RUNPATH_SEARCH_PATHS = "@executable_path/Frameworks";
				"LD_RUNPATH_SEARCH_PATHS[sdk=macosx*]" = "@executable_path/../Frameworks";
				MACOSX_DEPLOYMENT_TARGET = 15.0;
				MARKETING_VERSION = 1.1.0;
				PRODUCT_BUNDLE_IDENTIFIER = "com.signerlabs.ship-swift-ios";
				PRODUCT_NAME = "$(TARGET_NAME)";
				REGISTER_APP_GROUPS = YES;
				SDKROOT = auto;
				STRING_CATALOG_GENERATE_SYMBOLS = YES;
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator macosx";
				SUPPORTS_MACCATALYST = NO;
				SWIFT_APPROACHABLE_CONCURRENCY = YES;
				SWIFT_DEFAULT_ACTOR_ISOLATION = MainActor;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_UPCOMING_FEATURE_MEMBER_IMPORT_VISIBILITY = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 1;
				XROS_DEPLOYMENT_TARGET = 26.0;
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		B69605E82EEFD462006F81F3 /* Build configuration list for PBXProject "ShipSwift" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				B69605F62EEFD464006F81F3 /* Debug */,
				B69605F72EEFD464006F81F3 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		B69605F82EEFD464006F81F3 /* Build configuration list for PBXNativeTarget "ShipSwift" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				B69605F92EEFD464006F81F3 /* Debug */,
				B69605FA2EEFD464006F81F3 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */

/* Begin XCRemoteSwiftPackageReference section */
		9B1A79232F51C2C800DDF343 /* XCRemoteSwiftPackageReference "tiktok-business-ios-sdk" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/tiktok/tiktok-business-ios-sdk";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 1.6.0;
			};
		};
		9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */ = {
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/aws-amplify/amplify-swift";
			requirement = {
				kind = upToNextMajorVersion;
				minimumVersion = 2.53.3;
			};
		};
/* End XCRemoteSwiftPackageReference section */

/* Begin XCSwiftPackageProductDependency section */
		9B1A79242F51C2C800DDF343 /* TikTokBusinessSDK */ = {
			isa = XCSwiftPackageProductDependency;
			package = 9B1A79232F51C2C800DDF343 /* XCRemoteSwiftPackageReference "tiktok-business-ios-sdk" */;
			productName = TikTokBusinessSDK;
		};
		9B98BB212F27490700CA9857 /* AWSAPIPlugin */ = {
			isa = XCSwiftPackageProductDependency;
			package = 9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */;
			productName = AWSAPIPlugin;
		};
		9B98BB232F27490700CA9857 /* AWSCognitoAuthPlugin */ = {
			isa = XCSwiftPackageProductDependency;
			package = 9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */;
			productName = AWSCognitoAuthPlugin;
		};
		9B98BB252F27490700CA9857 /* AWSPluginsCore */ = {
			isa = XCSwiftPackageProductDependency;
			package = 9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */;
			productName = AWSPluginsCore;
		};
		9B98BB272F27490700CA9857 /* Amplify */ = {
			isa = XCSwiftPackageProductDependency;
			package = 9B98BB202F27490700CA9857 /* XCRemoteSwiftPackageReference "amplify-swift" */;
			productName = Amplify;
		};
/* End XCSwiftPackageProductDependency section */
	};
	rootObject = B69605E52EEFD462006F81F3 /* Project object */;
}
```

## File: `ShipSwift.xcodeproj/project.xcworkspace/contents.xcworkspacedata`
```
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>
```

## File: `ShipSwift.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved`
```
{
  "originHash" : "988d2205465f6710f6e461862d45ac9cf497881119a146b49c44a66a7f4d3631",
  "pins" : [
    {
      "identity" : "amplify-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/aws-amplify/amplify-swift",
      "state" : {
        "revision" : "d46019eea8299879a1e24a5d39cc67e1433c198a",
        "version" : "2.53.3"
      }
    },
    {
      "identity" : "amplify-swift-utils-notifications",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/aws-amplify/amplify-swift-utils-notifications.git",
      "state" : {
        "revision" : "959eec669ba97c7d923b963c3e66ca8a0b2737f6",
        "version" : "1.1.1"
      }
    },
    {
      "identity" : "async-http-client",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/swift-server/async-http-client.git",
      "state" : {
        "revision" : "4b99975677236d13f0754339864e5360142ff5a1",
        "version" : "1.30.3"
      }
    },
    {
      "identity" : "aws-crt-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/awslabs/aws-crt-swift",
      "state" : {
        "revision" : "8241ad06622f7351e8843dfab6bbce14fe6bce5d",
        "version" : "0.54.2"
      }
    },
    {
      "identity" : "aws-sdk-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/awslabs/aws-sdk-swift",
      "state" : {
        "revision" : "61d0ab5b429599f22c44b71b0737f030dc82f76b",
        "version" : "1.6.7"
      }
    },
    {
      "identity" : "grpc-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/grpc/grpc-swift.git",
      "state" : {
        "revision" : "a56a157218877ef3e9625f7e1f7b2cb7e46ead1b",
        "version" : "1.26.1"
      }
    },
    {
      "identity" : "opentelemetry-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/open-telemetry/opentelemetry-swift",
      "state" : {
        "revision" : "ef63c346d05f4fa7c9ca883f92631fd139eb2cfe",
        "version" : "1.17.1"
      }
    },
    {
      "identity" : "opentracing-objc",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/undefinedlabs/opentracing-objc",
      "state" : {
        "revision" : "18c1a35ca966236cee0c5a714a51a73ff33384c1",
        "version" : "0.5.2"
      }
    },
    {
      "identity" : "smithy-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/smithy-lang/smithy-swift",
      "state" : {
        "revision" : "0f3fb709fd034ad4b7a19567858571d08a5f4cbe",
        "version" : "0.175.0"
      }
    },
    {
      "identity" : "sqlite.swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/stephencelis/SQLite.swift.git",
      "state" : {
        "revision" : "a95fc6df17d108bd99210db5e8a9bac90fe984b8",
        "version" : "0.15.3"
      }
    },
    {
      "identity" : "swift-algorithms",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-algorithms.git",
      "state" : {
        "revision" : "87e50f483c54e6efd60e885f7f5aa946cee68023",
        "version" : "1.2.1"
      }
    },
    {
      "identity" : "swift-argument-parser",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-argument-parser.git",
      "state" : {
        "revision" : "c5d11a805e765f52ba34ec7284bd4fcd6ba68615",
        "version" : "1.7.0"
      }
    },
    {
      "identity" : "swift-asn1",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-asn1.git",
      "state" : {
        "revision" : "810496cf121e525d660cd0ea89a758740476b85f",
        "version" : "1.5.1"
      }
    },
    {
      "identity" : "swift-async-algorithms",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-async-algorithms.git",
      "state" : {
        "revision" : "6c050d5ef8e1aa6342528460db614e9770d7f804",
        "version" : "1.1.1"
      }
    },
    {
      "identity" : "swift-atomics",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-atomics.git",
      "state" : {
        "revision" : "b601256eab081c0f92f059e12818ac1d4f178ff7",
        "version" : "1.3.0"
      }
    },
    {
      "identity" : "swift-certificates",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-certificates.git",
      "state" : {
        "revision" : "7d5f6124c91a2d06fb63a811695a3400d15a100e",
        "version" : "1.17.1"
      }
    },
    {
      "identity" : "swift-collections",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-collections.git",
      "state" : {
        "revision" : "7b847a3b7008b2dc2f47ca3110d8c782fb2e5c7e",
        "version" : "1.3.0"
      }
    },
    {
      "identity" : "swift-crypto",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-crypto.git",
      "state" : {
        "revision" : "6f70fa9eab24c1fd982af18c281c4525d05e3095",
        "version" : "4.2.0"
      }
    },
    {
      "identity" : "swift-distributed-tracing",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-distributed-tracing.git",
      "state" : {
        "revision" : "baa932c1336f7894145cbaafcd34ce2dd0b77c97",
        "version" : "1.3.1"
      }
    },
    {
      "identity" : "swift-http-structured-headers",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-http-structured-headers.git",
      "state" : {
        "revision" : "76d7627bd88b47bf5a0f8497dd244885960dde0b",
        "version" : "1.6.0"
      }
    },
    {
      "identity" : "swift-http-types",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-http-types.git",
      "state" : {
        "revision" : "45eb0224913ea070ec4fba17291b9e7ecf4749ca",
        "version" : "1.5.1"
      }
    },
    {
      "identity" : "swift-log",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-log.git",
      "state" : {
        "revision" : "2778fd4e5a12a8aaa30a3ee8285f4ce54c5f3181",
        "version" : "1.9.1"
      }
    },
    {
      "identity" : "swift-metrics",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-metrics.git",
      "state" : {
        "revision" : "0743a9364382629da3bf5677b46a2c4b1ce5d2a6",
        "version" : "2.7.1"
      }
    },
    {
      "identity" : "swift-nio",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-nio.git",
      "state" : {
        "revision" : "233f61bc2cfbb22d0edeb2594da27a20d2ce514e",
        "version" : "2.93.0"
      }
    },
    {
      "identity" : "swift-nio-extras",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-nio-extras.git",
      "state" : {
        "revision" : "cc599775aa85d04340f09b47e5432564f9889ae7",
        "version" : "1.32.0"
      }
    },
    {
      "identity" : "swift-nio-http2",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-nio-http2.git",
      "state" : {
        "revision" : "c2ba4cfbb83f307c66f5a6df6bb43e3c88dfbf80",
        "version" : "1.39.0"
      }
    },
    {
      "identity" : "swift-nio-ssl",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-nio-ssl.git",
      "state" : {
        "revision" : "173cc69a058623525a58ae6710e2f5727c663793",
        "version" : "2.36.0"
      }
    },
    {
      "identity" : "swift-nio-transport-services",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-nio-transport-services.git",
      "state" : {
        "revision" : "60c3e187154421171721c1a38e800b390680fb5d",
        "version" : "1.26.0"
      }
    },
    {
      "identity" : "swift-numerics",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-numerics.git",
      "state" : {
        "revision" : "0c0290ff6b24942dadb83a929ffaaa1481df04a2",
        "version" : "1.1.1"
      }
    },
    {
      "identity" : "swift-protobuf",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-protobuf.git",
      "state" : {
        "revision" : "c169a5744230951031770e27e475ff6eefe51f9d",
        "version" : "1.33.3"
      }
    },
    {
      "identity" : "swift-service-context",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-service-context.git",
      "state" : {
        "revision" : "1983448fefc717a2bc2ebde5490fe99873c5b8a6",
        "version" : "1.2.1"
      }
    },
    {
      "identity" : "swift-service-lifecycle",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/swift-server/swift-service-lifecycle.git",
      "state" : {
        "revision" : "1de37290c0ab3c5a96028e0f02911b672fd42348",
        "version" : "2.9.1"
      }
    },
    {
      "identity" : "swift-system",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/apple/swift-system.git",
      "state" : {
        "revision" : "7c6ad0fc39d0763e0b699210e4124afd5041c5df",
        "version" : "1.6.4"
      }
    },
    {
      "identity" : "thrift-swift",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/undefinedlabs/Thrift-Swift",
      "state" : {
        "revision" : "18ff09e6b30e589ed38f90a1af23e193b8ecef8e",
        "version" : "1.1.2"
      }
    },
    {
      "identity" : "tiktok-business-ios-sdk",
      "kind" : "remoteSourceControl",
      "location" : "https://github.com/tiktok/tiktok-business-ios-sdk",
      "state" : {
        "revision" : "79faf4f1a8a15b039cb0d41a5186ea32fff86cb2",
        "version" : "1.6.0"
      }
    }
  ],
  "version" : 3
}
```

## File: `ShipSwift.xcodeproj/xcshareddata/xcschemes/ShipSwift.xcscheme`
```
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "2620"
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
               BlueprintIdentifier = "B69605EC2EEFD462006F81F3"
               BuildableName = "ShipSwift.app"
               BlueprintName = "ShipSwift"
               ReferencedContainer = "container:ShipSwift.xcodeproj">
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
            BlueprintIdentifier = "B69605EC2EEFD462006F81F3"
            BuildableName = "ShipSwift.app"
            BlueprintName = "ShipSwift"
            ReferencedContainer = "container:ShipSwift.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
      <StoreKitConfigurationFileReference
         identifier = "../../ShipSwift/ShipSwift - MCP Codebase.storekit">
      </StoreKitConfigurationFileReference>
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
            BlueprintIdentifier = "B69605EC2EEFD462006F81F3"
            BuildableName = "ShipSwift.app"
            BlueprintName = "ShipSwift"
            ReferencedContainer = "container:ShipSwift.xcodeproj">
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

## File: `skills/catalog.md`
```markdown
# ShipSwift Recipe Catalog

All source files are under `ShipSwift/SWPackage/`. Each component is self-contained — copy the file(s) plus `SWUtil/` into your project.

## Animation (`SWAnimation/`)

| Component | File | Description |
|-----------|------|-------------|
| AnimatedMeshGradient | `SWAnimatedMeshGradient.swift` | Animated mesh gradient background |
| BeforeAfterSlider | `SWBeforeAfterSlider.swift` | Drag-to-compare before/after image slider |
| GlowSweep | `SWGlowSweep.swift` | Glowing sweep animation overlay |
| LightSweep | `SWLightSweep.swift` | Light sweep / skeleton loading effect |
| OrbitingLogos | `SWOrbitingLogos.swift` | Logos orbiting around a center point |
| ScanningOverlay | `SWScanningOverlay.swift` | Scanning line animation overlay |
| ShakingIcon | `SWShakingIcon.swift` | Icon with shake animation on trigger |
| Shimmer | `SWShimmer.swift` | Shimmer / skeleton loading placeholder |
| TypewriterText | `SWTypewriterText.swift` | Character-by-character typing animation |

## Chart (`SWChart/`)

| Component | File | Description |
|-----------|------|-------------|
| ActivityHeatmap | `SWActivityHeatmap.swift` | GitHub-style contribution heatmap |
| AreaChart | `SWAreaChart.swift` | Filled area chart with gradient |
| BarChart | `SWBarChart.swift` | Vertical bar chart |
| DonutChart | `SWDonutChart.swift` | Donut / pie chart with center label |
| LineChart | `SWLineChart.swift` | Line chart with markers |
| RadarChart | `SWRadarChart.swift` | Spider / radar chart |
| RingChart | `SWRingChart.swift` | Circular progress ring chart |
| ScatterChart | `SWScatterChart.swift` | Scatter plot chart |

## Component — Display (`SWComponent/Display/`)

| Component | File | Description |
|-----------|------|-------------|
| BulletPointText | `SWBulletPointText.swift` | Styled bullet point list |
| FloatingLabels | `SWFloatingLabels.swift` | Floating animated labels |
| GradientDivider | `SWGradientDivider.swift` | Gradient-styled divider line |
| Label | `SWLabel.swift` | Styled label with icon support |
| MarkdownText | `SWMarkdownText.swift` | Markdown-rendered text view |
| OnboardingView | `SWOnboardingView.swift` | Multi-page onboarding flow |
| OrderView | `SWOrderView.swift` | Order / receipt summary view |
| RootTabView | `SWRootTabView.swift` | Tab bar navigation root view |
| RotatingQuote | `SWRotatingQuote.swift` | Auto-rotating quote display |
| ScrollingFAQ | `SWScrollingFAQ+iOS.swift` | Expandable FAQ list (iOS) |

## Component — Feedback (`SWComponent/Feedback/`)

| Component | File | Description |
|-----------|------|-------------|
| Alert | `SWAlert.swift` | Custom alert with SWAlertManager |
| Loading | `SWLoading.swift` | Page loading overlay |
| ThinkingIndicator | `SWThinkingIndicator.swift` | AI thinking / typing indicator |

## Component — Input (`SWComponent/Input/`)

| Component | File | Description |
|-----------|------|-------------|
| AddSheet | `SWAddSheet.swift` | Bottom sheet for adding items |
| Stepper | `SWStepper.swift` | Custom stepper control |
| TabButton | `SWTabButton.swift` | Styled tab bar button |

## Module (`SWModule/`)

Multi-file modules. Copy the entire module folder plus `SWUtil/`.

| Module | Files | Description |
|--------|-------|-------------|
| **SWAuth** | `SWAuthView+iOS.swift`, `SWAuthView+macOS.swift`, `SWUserManager.swift`, `SWCountryData.swift`, `SWAgreementChecker.swift` | Authentication with Amplify/Cognito — social login, email/password, phone sign-in with country code picker |
| **SWCamera** | `SWCameraManager+iOS.swift`, `SWCameraView+iOS.swift`, `SWFaceCameraView+iOS.swift`, `SWFaceLandmark+iOS.swift` | Camera capture with viewfinder, zoom, photo picker, face detection with Vision landmarks |
| **SWChat** | `SWChatView+iOS.swift`, `SWChatInputView+iOS.swift`, `SWMessageList+iOS.swift`, `SWVolcEngineASRService+iOS.swift` | Chat view with message list, text input, optional voice recognition (VolcEngine ASR) |
| **SWPaywall** | `SWPaywallView.swift`, `SWStoreManager.swift` | StoreKit 2 subscription paywall |
| **SWSetting** | `SWSettingView+iOS.swift`, `SWSettingView+macOS.swift` | Settings page with language switch, share, legal links |
| **SWSubjectLifting** | `SWSubjectLiftingManager+iOS.swift`, `SWSubjectLiftingView+iOS.swift` | Background removal using VisionKit |
| **SWTikTokTracking** | `SWTikTokTrackingManager+iOS.swift`, `SWTikTokTrackingView+iOS.swift` | TikTok Events API attribution tracking |

## Utilities (`SWUtil/`)

| File | Description |
|------|-------------|
| `SWDateExtension.swift` | Date formatting extensions |
| `SWDebugLog.swift` | Debug logging utility |
| `SWLocationManager.swift` | Location manager wrapper |
| `SWStringExtension.swift` | String utility extensions |
| `SWViewExtension.swift` | View modifier extensions (`.swAlert()`, `.swPageLoading()`, `.swPrimary`) |

## Dependency Rules

```
SWUtil         ← no dependencies
SWAnimation    ← SWUtil only
SWChart        ← SWUtil only
SWComponent    ← SWUtil only
SWModule       ← SWUtil + SWComponent + same-module files
```

## Naming Conventions

- Types: `SW` prefix (`SWAlertManager`, `SWStoreManager`)
- View modifiers: `.sw` prefix (`.swAlert()`, `.swPageLoading()`)
- iOS-only files: `+iOS` suffix
- macOS-only files: `+macOS` suffix
```

## File: `skills/add-component/SKILL.md`
```markdown
---
name: add-component
description: >
  Add a SwiftUI component from ShipSwift. Use when the user says "add component",
  "add a view", "add X view", "I need a chart", "add animation", or wants a specific UI element.
---

# Add Component from ShipSwift

Add production-ready SwiftUI components to your project from ShipSwift's local source library.

## Workflow

1. **Identify the component**: Read `skills/catalog.md` to find the right component. Common mappings:
   - "shimmer" / "loading skeleton" → `SWAnimation/SWShimmer.swift`
   - "donut chart" / "pie chart" → `SWChart/SWDonutChart.swift`
   - "alert" / "popup" → `SWComponent/Feedback/SWAlert.swift`
   - "auth" / "login" → `SWModule/SWAuth/` (all files)
   - "camera" → `SWModule/SWCamera/` (all files)

2. **Read the source file**: Read the Swift file from `ShipSwift/SWPackage/<path>`. The file contains the complete implementation.

3. **Integrate into the project**:
   - Copy the file(s) into the user's project
   - Also copy `SWUtil/` if not already present
   - Adapt naming, colors, and data models to match the project
   - For `+iOS`/`+macOS` files, set the platform filter in Xcode Build Phases

4. **Verify**: Walk through any dependencies or setup steps needed.

## Guidelines

- Types use `SW` prefix (`SWDonutChart`, `SWTypewriter`).
- View modifiers use `.sw` prefix (`.swShimmer()`, `.swGlowScan()`).
- Chart components use a generic `CategoryType` pattern with `String` convenience initializer.
- Internal helper types should be `private` with `SW` prefix.
- Components in `SWAnimation/`, `SWChart/`, and `SWComponent/` are each self-contained (single file + SWUtil).
- Modules in `SWModule/` are multi-file — copy the entire folder.
```

## File: `skills/build-feature/SKILL.md`
```markdown
---
name: build-feature
description: >
  Build an iOS feature using ShipSwift components. Use when the user says
  "build", "create", "add a feature", or describes an iOS feature they want to implement.
---

# Build Feature with ShipSwift

Build production-ready iOS features by combining ShipSwift components — copy-paste-ready SwiftUI implementations covering animations, charts, UI components, and full-stack modules.

## Workflow

1. **Browse the catalog**: Read `skills/catalog.md` to see all available components organized by category.

2. **Read the source**: For each relevant component, read the Swift file directly from `ShipSwift/SWPackage/`. For example:
   - Shimmer animation → read `ShipSwift/SWPackage/SWAnimation/SWShimmer.swift`
   - Donut chart → read `ShipSwift/SWPackage/SWChart/SWDonutChart.swift`
   - Auth module → read all files in `ShipSwift/SWPackage/SWModule/SWAuth/`

3. **Present an integration plan**: Before writing code, show the user:
   - Which components will be used
   - How they connect together
   - What customizations are needed

4. **Generate code**: Adapt the component patterns to the user's project. Combine multiple components when the feature spans several areas (e.g., a chart view with shimmer loading).

5. **Integration checklist**: List required dependencies, Info.plist entries, or Xcode build phase settings (especially for `+iOS`/`+macOS` platform-filtered files).

## Guidelines

- Always check the catalog before writing code from scratch — ShipSwift likely has a ready-made solution.
- Use `SW`-prefixed naming (`SWShimmer`, `SWDonutChart`).
- View modifiers use `.sw` lowercase prefix (`.swShimmer()`, `.swGlowScan()`).
- Copy `SWUtil/` alongside any component — it provides shared extensions.
- For modules (`SWModule/`), copy the entire module folder.
- Support Dark Mode and Dynamic Type by default.

## Pro Recipes (MCP)

Some full-stack recipes (backend + compliance + pitfall guides) are available via the MCP server at `https://api.shipswift.app/mcp`. If MCP tools (`listRecipes`, `searchRecipes`, `getRecipe`) are available, use them for extended content. The local source code works independently.
```

## File: `skills/explore-recipes/SKILL.md`
```markdown
---
name: explore-recipes
description: >
  Explore and browse available ShipSwift components. Use when the user says
  "explore", "browse", "show recipes", "list components", "what's available",
  or wants to discover what ShipSwift offers.
---

# Explore ShipSwift Recipes

Browse the full catalog of ShipSwift components — production-ready SwiftUI implementations.

## Workflow

1. **Show the catalog**: Read `skills/catalog.md` and present components organized by category:

   | Category | Count | Examples |
   |----------|-------|---------|
   | Animation | 9 | Shimmer, Typewriter, GlowSweep, MeshGradient, OrbitingLogos |
   | Chart | 8 | Line, Bar, Area, Donut, Ring, Radar, Scatter, Heatmap |
   | Component | 13 | Alert, Loading, Onboarding, Stepper, FloatingLabels |
   | Module | 7 | Auth, Camera, Chat, Paywall, Settings, SubjectLifting, TikTokTracking |
   | Util | 5 | Date/String/View extensions, DebugLog, LocationManager |

2. **Show details on request**: When the user picks a component, read the source file and present:
   - What it does
   - Key features and customization points
   - Code structure overview
   - Dependencies

3. **Suggest combinations**: Recommend components that work well together:
   - **Onboarding flow**: OnboardingView + TypewriterText + Shimmer
   - **Analytics dashboard**: LineChart + BarChart + DonutChart + ActivityHeatmap
   - **Social feature**: Camera + Chat + Auth
   - **E-commerce**: OrderView + Loading + Alert + Stepper

## Guidelines

- Present in a scannable format (tables or bullet lists).
- When showing details, include the file path so the user can find it.
- All source is local under `ShipSwift/SWPackage/` — no network required.
```


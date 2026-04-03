---
id: claude-usage-tracker-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.596122
---

# KNOWLEDGE EXTRACT: claude-usage-tracker
> **Extracted on:** 2026-03-30 13:25:16
> **Source:** claude-usage-tracker

---

## File: `.gitignore`
```
.DS_Store
data/data.js
data/sessions-cache.json
data/sessions-cache.json.tmp
*.app/
node_modules/
```

## File: `App.swift`
```
// App.swift — Native macOS app for Claude Usage Dashboard
// Renders the dashboard in a WKWebView instead of opening a browser.

import Cocoa
import WebKit

class AppDelegate: NSObject, NSApplicationDelegate, WKNavigationDelegate, WKScriptMessageHandler {
    var window: NSWindow!
    var webView: WKWebView!
    var dashboardNavigation: WKNavigation?

    // MARK: - App Lifecycle

    func applicationDidFinishLaunching(_ notification: Notification) {
        setupMainMenu()
        setupWindow()
        showLoadingScreen()
        collectDataAndLoadDashboard()
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool {
        return true
    }

    func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool {
        return false
    }

    // MARK: - Menu Bar

    func setupMainMenu() {
        let mainMenu = NSMenu()

        // App menu
        let appMenuItem = NSMenuItem()
        mainMenu.addItem(appMenuItem)
        let appMenu = NSMenu()
        appMenu.addItem(withTitle: "About Claude Usage Dashboard",
                        action: #selector(NSApplication.orderFrontStandardAboutPanel(_:)),
                        keyEquivalent: "")
        appMenu.addItem(.separator())
        appMenu.addItem(withTitle: "Hide Claude Usage Dashboard",
                        action: #selector(NSApplication.hide(_:)),
                        keyEquivalent: "h")
        let hideOthers = appMenu.addItem(withTitle: "Hide Others",
                        action: #selector(NSApplication.hideOtherApplications(_:)),
                        keyEquivalent: "h")
        hideOthers.keyEquivalentModifierMask = [.command, .option]
        appMenu.addItem(withTitle: "Show All",
                        action: #selector(NSApplication.unhideAllApplications(_:)),
                        keyEquivalent: "")
        appMenu.addItem(.separator())
        appMenu.addItem(withTitle: "Quit Claude Usage Dashboard",
                        action: #selector(NSApplication.terminate(_:)),
                        keyEquivalent: "q")
        appMenuItem.submenu = appMenu

        // Edit menu (enables copy/paste in WebView)
        let editMenuItem = NSMenuItem()
        mainMenu.addItem(editMenuItem)
        let editMenu = NSMenu(title: "Edit")
        editMenu.addItem(withTitle: "Undo", action: Selector(("undo:")), keyEquivalent: "z")
        editMenu.addItem(withTitle: "Redo", action: Selector(("redo:")), keyEquivalent: "Z")
        editMenu.addItem(.separator())
        editMenu.addItem(withTitle: "Cut", action: #selector(NSText.cut(_:)), keyEquivalent: "x")
        editMenu.addItem(withTitle: "Copy", action: #selector(NSText.copy(_:)), keyEquivalent: "c")
        editMenu.addItem(withTitle: "Paste", action: #selector(NSText.paste(_:)), keyEquivalent: "v")
        editMenu.addItem(withTitle: "Select All", action: #selector(NSText.selectAll(_:)), keyEquivalent: "a")
        editMenuItem.submenu = editMenu

        // View menu
        let viewMenuItem = NSMenuItem()
        mainMenu.addItem(viewMenuItem)
        let viewMenu = NSMenu(title: "View")
        viewMenu.addItem(withTitle: "Refresh Data",
                         action: #selector(reloadDashboard),
                         keyEquivalent: "r")
        viewMenuItem.submenu = viewMenu

        // Window menu
        let windowMenuItem = NSMenuItem()
        mainMenu.addItem(windowMenuItem)
        let windowMenu = NSMenu(title: "Window")
        windowMenu.addItem(withTitle: "Minimize",
                           action: #selector(NSWindow.miniaturize(_:)),
                           keyEquivalent: "m")
        windowMenu.addItem(withTitle: "Zoom",
                           action: #selector(NSWindow.zoom(_:)),
                           keyEquivalent: "")
        windowMenu.addItem(.separator())
        windowMenu.addItem(withTitle: "Close",
                           action: #selector(NSWindow.performClose(_:)),
                           keyEquivalent: "w")
        windowMenuItem.submenu = windowMenu

        NSApp.mainMenu = mainMenu
        NSApp.windowsMenu = windowMenu
    }

    // MARK: - Window Setup

    func setupWindow() {
        let screen = NSScreen.main?.visibleFrame ?? NSRect(x: 0, y: 0, width: 1280, height: 800)
        let w = min(1440, screen.width * 0.88)
        let h = min(960, screen.height * 0.9)
        let frame = NSRect(
            x: screen.origin.x + (screen.width - w) / 2,
            y: screen.origin.y + (screen.height - h) / 2,
            width: w, height: h
        )

        window = NSWindow(
            contentRect: frame,
            styleMask: [.titled, .closable, .miniaturizable, .resizable, .fullSizeContentView],
            backing: .buffered,
            defer: false
        )
        window.title = "Claude Usage Dashboard"
        window.appearance = NSAppearance(named: .darkAqua)
        window.backgroundColor = NSColor(red: 0.039, green: 0.055, blue: 0.09, alpha: 1.0)
        window.titlebarAppearsTransparent = true
        window.titleVisibility = .hidden
        window.isMovableByWindowBackground = true
        window.minSize = NSSize(width: 800, height: 600)

        // WKWebView — enable local file access for ES6 modules
        let config = WKWebViewConfiguration()
        let prefs = WKPreferences()
        prefs.setValue(true, forKey: "allowFileAccessFromFileURLs")
        config.preferences = prefs
        config.setValue(true, forKey: "allowUniversalAccessFromFileURLs")

        // Register message handlers
        let contentController = WKUserContentController()
        contentController.add(self, name: "reload")
        contentController.add(self, name: "exportData")
        contentController.add(self, name: "importData")
        config.userContentController = contentController

        webView = WKWebView(frame: window.contentView!.bounds, configuration: config)
        webView.autoresizingMask = [.width, .height]
        webView.navigationDelegate = self

        // GPU acceleration: layer-backed, async drawing
        webView.wantsLayer = true
        webView.layer?.drawsAsynchronously = true
        webView.layer?.backgroundColor = NSColor(red: 0.039, green: 0.055, blue: 0.09, alpha: 1.0).cgColor
        webView.allowsBackForwardNavigationGestures = false

        window.contentView?.addSubview(webView)
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    // MARK: - WKScriptMessageHandler

    func userContentController(_ userContentController: WKUserContentController, didReceive message: WKScriptMessage) {
        switch message.name {
        case "reload":
            reloadDashboard()
        case "exportData":
            handleExport(message.body as? String ?? "")
        case "importData":
            handleImport()
        default:
            break
        }
    }

    // MARK: - Export (NSSavePanel)

    func handleExport(_ jsonString: String) {
        let panel = NSSavePanel()
        let dateStr = ISO8601DateFormatter().string(from: Date()).prefix(10)
        panel.nameFieldStringValue = "claude-usage-\(dateStr).json"
        panel.allowedContentTypes = [.json]
        panel.canCreateDirectories = true
        panel.title = "Export Usage Data"

        panel.beginSheetModal(for: window) { [weak self] response in
            guard response == .OK, let url = panel.url else { return }
            do {
                try jsonString.write(to: url, atomically: true, encoding: .utf8)
                let count = (try? JSONSerialization.jsonObject(with: Data(jsonString.utf8)) as? [String: Any])?["sessions"]
                let sessionCount = (count as? [[String: Any]])?.count ?? 0
                self?.webView.evaluateJavaScript("window._showExportToast('Exported \(sessionCount) sessions to file')")
            } catch {
                self?.webView.evaluateJavaScript("window._showExportToast('Export failed: \(error.localizedDescription)', true)")
            }
        }
    }

    // MARK: - Import (NSOpenPanel)

    func handleImport() {
        let panel = NSOpenPanel()
        panel.allowedContentTypes = [.json]
        panel.allowsMultipleSelection = false
        panel.canChooseDirectories = false
        panel.title = "Import Usage Data"
        panel.message = "Select a claude-usage JSON file exported from another device"

        panel.beginSheetModal(for: window) { [weak self] response in
            guard response == .OK, let url = panel.url else {
                self?.webView.evaluateJavaScript("if(window._importDataResolver) window._importDataResolver(null)")
                return
            }
            do {
                let jsonString = try String(contentsOf: url, encoding: .utf8)
                // Escape for JS string literal
                let escaped = jsonString
                    .replacingOccurrences(of: "\\", with: "\\\\")
                    .replacingOccurrences(of: "'", with: "\\'")
                    .replacingOccurrences(of: "\n", with: "\\n")
                    .replacingOccurrences(of: "\r", with: "\\r")
                self?.webView.evaluateJavaScript("if(window._importDataResolver) window._importDataResolver('\(escaped)')")
            } catch {
                self?.webView.evaluateJavaScript("window._showExportToast('Failed to read file', true)")
                self?.webView.evaluateJavaScript("if(window._importDataResolver) window._importDataResolver(null)")
            }
        }
    }

    // MARK: - Loading Screen

    func showLoadingScreen() {
        webView.alphaValue = 1
        webView.loadHTMLString(loadingHTML(), baseURL: nil)
    }

    // MARK: - Data Collection

    func collectDataAndLoadDashboard() {
        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            self?.collectData()
            DispatchQueue.main.async {
                self?.loadDashboard()
            }
        }
    }

    func collectData() {
        let resourcesPath = Bundle.main.resourcePath ?? "."

        guard let node = findNode() else {
            DispatchQueue.main.async {
                let alert = NSAlert()
                alert.messageText = "Node.js not found"
                alert.informativeText = "Claude Usage Dashboard requires Node.js to collect data.\nInstall it from https://nodejs.org"
                alert.alertStyle = .critical
                alert.runModal()
                NSApp.terminate(nil)
            }
            return
        }

        // Ensure data directory exists
        let dataDir = resourcesPath + "/data"
        try? FileManager.default.createDirectory(atPath: dataDir, withIntermediateDirectories: true)

        let process = Process()
        process.executableURL = URL(fileURLWithPath: node)
        process.arguments = [resourcesPath + "/collect-usage.js"]
        process.currentDirectoryURL = URL(fileURLWithPath: resourcesPath)

        // Ensure child process has a usable PATH
        var env = ProcessInfo.processInfo.environment
        let extra = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
        env["PATH"] = extra + ":" + (env["PATH"] ?? "")
        process.environment = env

        let logPath = dataDir + "/launcher.log"
        FileManager.default.createFile(atPath: logPath, contents: nil)
        if let logHandle = FileHandle(forWritingAtPath: logPath) {
            process.standardOutput = logHandle
            process.standardError = logHandle
            try? process.run()
            process.waitUntilExit()
            logHandle.closeFile()
        } else {
            process.standardOutput = FileHandle.nullDevice
            process.standardError = FileHandle.nullDevice
            try? process.run()
            process.waitUntilExit()
        }
    }

    func findNode() -> String? {
        let candidates = [
            "/opt/homebrew/bin/node",
            "/usr/local/bin/node",
            "/usr/bin/node"
        ]
        for path in candidates {
            if FileManager.default.isExecutableFile(atPath: path) { return path }
        }

        // Fallback: which node
        let which = Process()
        which.executableURL = URL(fileURLWithPath: "/usr/bin/which")
        which.arguments = ["node"]
        let pipe = Pipe()
        which.standardOutput = pipe
        which.standardError = FileHandle.nullDevice
        try? which.run()
        which.waitUntilExit()

        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        if let path = String(data: data, encoding: .utf8)?
            .trimmingCharacters(in: .whitespacesAndNewlines),
           !path.isEmpty, FileManager.default.isExecutableFile(atPath: path) {
            return path
        }
        return nil
    }

    // MARK: - Dashboard Loading

    func loadDashboard() {
        let resourcesPath = Bundle.main.resourcePath ?? "."
        let dashboardURL = URL(fileURLWithPath: resourcesPath + "/dashboard.html")
        let resourcesDir = URL(fileURLWithPath: resourcesPath, isDirectory: true)

        webView.alphaValue = 0
        dashboardNavigation = webView.loadFileURL(dashboardURL, allowingReadAccessTo: resourcesDir)
    }

    @objc func reloadDashboard() {
        showLoadingScreen()
        collectDataAndLoadDashboard()
    }

    // MARK: - WKNavigationDelegate

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        guard navigation == dashboardNavigation else { return }
        dashboardNavigation = nil

        NSAnimationContext.runAnimationGroup({ context in
            context.duration = 0.35
            context.timingFunction = CAMediaTimingFunction(name: .easeOut)
            webView.animator().alphaValue = 1
        })
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        webView.alphaValue = 1
        let alert = NSAlert()
        alert.messageText = "Failed to load dashboard"
        alert.informativeText = error.localizedDescription
        alert.alertStyle = .warning
        alert.runModal()
    }

    // MARK: - Loading HTML

    func loadingHTML() -> String {
        return """
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            html, body {
                background: #0a0e17;
                color: #e2e8f0;
                font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', sans-serif;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                overflow: hidden;
                -webkit-font-smoothing: antialiased;
            }

            /* Aurora background — no blur filter, use pre-softened gradients */
            .aurora {
                position: fixed;
                inset: 0;
                pointer-events: none;
            }
            .aurora-blob {
                position: absolute;
                border-radius: 50%;
                will-change: transform;
                animation: auroraDrift 12s ease-in-out infinite alternate;
            }
            .aurora-blob:nth-child(1) {
                width: 600px; height: 600px;
                top: -20%; right: -10%;
                background: radial-gradient(circle, rgba(34,211,238,0.08) 0%, rgba(34,211,238,0.02) 40%, transparent 70%);
            }
            .aurora-blob:nth-child(2) {
                width: 500px; height: 500px;
                bottom: -15%; left: -8%;
                background: radial-gradient(circle, rgba(251,191,36,0.05) 0%, rgba(251,191,36,0.01) 40%, transparent 70%);
                animation-duration: 15s;
                animation-delay: -4s;
            }
            .aurora-blob:nth-child(3) {
                width: 450px; height: 450px;
                top: 25%; left: 15%;
                background: radial-gradient(circle, rgba(167,139,250,0.05) 0%, rgba(167,139,250,0.01) 40%, transparent 70%);
                animation-duration: 18s;
                animation-delay: -8s;
            }
            @keyframes auroraDrift {
                0%   { transform: translate3d(0, 0, 0) scale(1); }
                100% { transform: translate3d(25px, -15px, 0) scale(1.1); }
            }

            /* Floating particles — GPU-composited */
            .particles {
                position: fixed;
                inset: 0;
                pointer-events: none;
            }
            .dot {
                position: absolute;
                border-radius: 50%;
                opacity: 0;
                will-change: transform, opacity;
                animation: particleFloat linear infinite;
            }
            .dot:nth-child(1) { width:3px; height:3px; left:15%; top:80%; background:#22d3ee; animation-duration:8s;  animation-delay:0s;   }
            .dot:nth-child(2) { width:2px; height:2px; left:40%; top:88%; background:#a78bfa; animation-duration:10s; animation-delay:2s;   }
            .dot:nth-child(3) { width:3px; height:3px; left:65%; top:85%; background:#34d399; animation-duration:9s;  animation-delay:1s;   }
            .dot:nth-child(4) { width:2px; height:2px; left:85%; top:90%; background:#fbbf24; animation-duration:11s; animation-delay:3.5s; }
            .dot:nth-child(5) { width:3px; height:3px; left:8%;  top:92%; background:#60a5fa; animation-duration:9s;  animation-delay:5s;   }
            @keyframes particleFloat {
                0%   { transform: translate3d(0, 0, 0); opacity: 0; }
                10%  { opacity: 0.5; }
                90%  { opacity: 0.3; }
                100% { transform: translate3d(15px, -100vh, 0); opacity: 0; }
            }

            /* Main container */
            .loader {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 40px;
                position: relative;
                z-index: 1;
                animation: loaderIn 0.6s ease-out;
            }
            @keyframes loaderIn {
                from { opacity: 0; transform: translate3d(0, 16px, 0); }
                to   { opacity: 1; transform: translate3d(0, 0, 0); }
            }

            /* Logo with orbital rings */
            .logo-orbit {
                position: relative;
                width: 140px;
                height: 140px;
            }
            .logo {
                position: absolute;
                top: 50%; left: 50%;
                transform: translate(-50%, -50%);
                width: 80px; height: 80px;
                will-change: transform;
                animation: logoFloat 3s ease-in-out infinite;
            }
            @keyframes logoFloat {
                0%, 100% { transform: translate(-50%, -50%) translate3d(0, 0, 0); }
                50%      { transform: translate(-50%, -50%) translate3d(0, -8px, 0); }
            }

            /* Orbit rings — GPU composited via transform */
            .orbit {
                position: absolute;
                border-radius: 50%;
                border: 1px solid transparent;
                will-change: transform;
            }
            .orbit-1 {
                inset: 0;
                border-color: rgba(34,211,238,0.12);
                animation: orbitSpin 6s linear infinite;
            }
            .orbit-1::after {
                content: '';
                position: absolute;
                top: -3px; left: 50%;
                width: 6px; height: 6px;
                margin-left: -3px;
                background: #22d3ee;
                border-radius: 50%;
            }
            .orbit-2 {
                inset: -14px;
                border-color: rgba(167,139,250,0.08);
                animation: orbitSpin 10s linear infinite reverse;
            }
            .orbit-2::after {
                content: '';
                position: absolute;
                bottom: -2px; right: 20%;
                width: 4px; height: 4px;
                background: #a78bfa;
                border-radius: 50%;
            }
            .orbit-3 {
                inset: -28px;
                border-color: rgba(52,211,153,0.05);
                animation: orbitSpin 14s linear infinite;
            }
            .orbit-3::after {
                content: '';
                position: absolute;
                top: 30%; right: -2px;
                width: 3px; height: 3px;
                background: #34d399;
                border-radius: 50%;
            }
            @keyframes orbitSpin {
                to { transform: rotate(360deg); }
            }

            /* Title with shimmer */
            .title {
                position: relative;
                font-size: 28px;
                font-weight: 700;
                letter-spacing: -0.5px;
                overflow: hidden;
            }
            .title em {
                font-style: normal;
                background: linear-gradient(135deg, #22d3ee, #a78bfa);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .title::after {
                content: '';
                position: absolute;
                top: 0;
                width: 60%; height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
                will-change: transform;
                animation: shimmerSweep 4s ease-in-out infinite;
                pointer-events: none;
            }
            @keyframes shimmerSweep {
                0%, 100% { transform: translate3d(-400%, 0, 0); }
                50%      { transform: translate3d(400%, 0, 0); }
            }

            /* Progress track */
            .progress {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 24px;
                width: 100%;
            }
            .progress-track {
                width: 220px;
                height: 2px;
                background: rgba(30,41,59,0.6);
                border-radius: 2px;
                overflow: hidden;
            }
            .progress-fill {
                width: 35%;
                height: 100%;
                background: linear-gradient(90deg, #22d3ee, #a78bfa, #fb7185);
                border-radius: 2px;
                will-change: transform;
                animation: progressSlide 1.8s ease-in-out infinite;
            }
            @keyframes progressSlide {
                0%   { transform: translate3d(-100%, 0, 0); }
                100% { transform: translate3d(620%, 0, 0); }
            }

            .status {
                font-size: 13px;
                color: #64748b;
                letter-spacing: 0.5px;
            }
            .status span {
                display: inline-block;
                animation: statusFade 2.5s ease-in-out infinite;
            }
            .status span:nth-child(1) { animation-delay: 0s; }
            .status span:nth-child(2) { animation-delay: 0.15s; }
            .status span:nth-child(3) { animation-delay: 0.3s; }
            @keyframes statusFade {
                0%, 100% { opacity: 0.35; }
                50%      { opacity: 1; }
            }

            /* Animated bars — use scaleY (GPU) instead of height (layout) */
            .bars {
                display: flex;
                align-items: flex-end;
                gap: 6px;
                height: 36px;
            }
            .bar {
                height: 32px;
                border-radius: 3px;
                transform-origin: bottom;
                will-change: transform, opacity;
                animation: barWave 2s ease-in-out infinite;
            }
            .bar:nth-child(1) { width:6px; background:linear-gradient(to top,#22d3ee,#34d399); animation-delay:0s; }
            .bar:nth-child(2) { width:6px; background:linear-gradient(to top,#60a5fa,#22d3ee); animation-delay:.15s; }
            .bar:nth-child(3) { width:6px; background:linear-gradient(to top,#a78bfa,#60a5fa); animation-delay:.3s; }
            .bar:nth-child(4) { width:6px; background:linear-gradient(to top,#fb7185,#a78bfa); animation-delay:.45s; }
            .bar:nth-child(5) { width:6px; background:linear-gradient(to top,#fbbf24,#fb7185); animation-delay:.6s; }
            .bar:nth-child(6) { width:6px; background:linear-gradient(to top,#34d399,#22d3ee); animation-delay:.75s; }
            .bar:nth-child(7) { width:6px; background:linear-gradient(to top,#22d3ee,#60a5fa); animation-delay:.9s; }
            @keyframes barWave {
                0%   { transform: scaleY(0.25); opacity: 0.4; }
                25%  { transform: scaleY(1);    opacity: 0.9; }
                50%  { transform: scaleY(0.5);  opacity: 0.6; }
                75%  { transform: scaleY(0.85); opacity: 0.85; }
                100% { transform: scaleY(0.25); opacity: 0.4; }
            }

            /* Skeleton preview cards */
            .skeleton-row {
                display: flex;
                gap: 14px;
                margin-top: 8px;
            }
            .skeleton-card {
                width: 90px;
                height: 56px;
                border-radius: 10px;
                background: rgba(21,29,46,0.6);
                border: 1px solid rgba(30,41,59,0.3);
                overflow: hidden;
                position: relative;
            }
            .skeleton-card::after {
                content: '';
                position: absolute;
                inset: 0;
                background: linear-gradient(90deg, transparent 0%, rgba(34,211,238,0.04) 50%, transparent 100%);
                will-change: transform;
                animation: skeletonShimmer 2s ease-in-out infinite;
            }
            .skeleton-card:nth-child(2)::after { animation-delay: 0.3s; }
            .skeleton-card:nth-child(3)::after { animation-delay: 0.6s; }
            .skeleton-card:nth-child(4)::after { animation-delay: 0.9s; }
            @keyframes skeletonShimmer {
                0%   { transform: translate3d(-100%, 0, 0); }
                100% { transform: translate3d(200%, 0, 0); }
            }
        </style>
        </head>
        <body>
        <div class="aurora">
            <div class="aurora-blob"></div>
            <div class="aurora-blob"></div>
            <div class="aurora-blob"></div>
        </div>

        <div class="particles">
            <div class="dot"></div><div class="dot"></div><div class="dot"></div>
            <div class="dot"></div><div class="dot"></div>
        </div>

        <div class="loader">
            <div class="logo-orbit">
                <div class="orbit orbit-1"></div>
                <div class="orbit orbit-2"></div>
                <div class="orbit orbit-3"></div>
                <svg class="logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none">
                    <defs>
                        <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient>
                        <linearGradient id="gw" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#34d399" stop-opacity="0.25"/><stop offset="50%" stop-color="#22d3ee" stop-opacity="0.08"/><stop offset="100%" stop-color="#a78bfa" stop-opacity="0.25"/></linearGradient>
                        <linearGradient id="b1" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#34d399"/></linearGradient>
                        <linearGradient id="b2" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#22d3ee"/></linearGradient>
                        <linearGradient id="b3" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#60a5fa"/></linearGradient>
                        <linearGradient id="b4" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#fb7185"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient>
                        <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#fb7185"/></linearGradient>
                        <linearGradient id="af" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fbbf24" stop-opacity="0.15"/><stop offset="100%" stop-color="#fb7185" stop-opacity="0.02"/></linearGradient>
                    </defs>
                    <rect width="512" height="512" rx="108" ry="108" fill="#0f1629"/>
                    <rect width="512" height="512" rx="108" ry="108" fill="url(#gw)" opacity="0.5"/>
                    <rect x="3" y="3" width="506" height="506" rx="105" ry="105" fill="none" stroke="url(#g)" stroke-width="1.5" opacity="0.4"/>
                    <rect x="80" y="100" width="352" height="312" rx="20" ry="20" fill="#131b2e" opacity="0.6"/>
                    <line x1="110" y1="370" x2="402" y2="370" stroke="#253147" stroke-width="1.5" opacity="0.6"/>
                    <rect x="122" y="238" width="50" height="132" rx="8" ry="8" fill="url(#b1)" opacity="0.92"/>
                    <rect x="192" y="168" width="50" height="202" rx="8" ry="8" fill="url(#b2)" opacity="0.92"/>
                    <rect x="262" y="206" width="50" height="164" rx="8" ry="8" fill="url(#b3)" opacity="0.92"/>
                    <rect x="332" y="128" width="50" height="242" rx="8" ry="8" fill="url(#b4)" opacity="0.92"/>
                    <polygon points="147,226 217,156 287,192 357,122 357,370 147,370" fill="url(#af)" opacity="0.6"/>
                    <polyline points="147,226 217,156 287,192 357,122" fill="none" stroke="url(#lg)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/>
                    <circle cx="147" cy="226" r="4.5" fill="#fbbf24"/>
                    <circle cx="217" cy="156" r="4.5" fill="#f59e0b"/>
                    <circle cx="287" cy="192" r="4.5" fill="#e879a0"/>
                    <circle cx="357" cy="122" r="4.5" fill="#fb7185"/>
                </svg>
            </div>

            <div class="title"><em>Claude</em> Usage Tracker</div>

            <div class="progress">
                <div class="progress-track"><div class="progress-fill"></div></div>
                <div class="status">
                    <span>Collecting</span> <span>usage</span> <span>data&hellip;</span>
                </div>
            </div>

            <div class="bars">
                <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
                <div class="bar"></div><div class="bar"></div><div class="bar"></div>
            </div>

            <div class="skeleton-row">
                <div class="skeleton-card"></div>
                <div class="skeleton-card"></div>
                <div class="skeleton-card"></div>
                <div class="skeleton-card"></div>
            </div>
        </div>
        </body>
        </html>
        """
    }
}

// MARK: - Entry Point

let app = NSApplication.shared
let delegate = AppDelegate()
app.delegate = delegate
app.run()
```

## File: `build-app.sh`
```bash
#!/bin/bash
# Build a standalone macOS .app for Claude Usage Dashboard
# Double-click to collect fresh data + view dashboard in a native window.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_NAME="Claude Usage Dashboard"
APP_DIR="$SCRIPT_DIR/$APP_NAME.app"
CONTENTS="$APP_DIR/Contents"
MACOS="$CONTENTS/MacOS"
RESOURCES="$CONTENTS/Resources"

echo "🔨 Building $APP_NAME.app ..."

# Clean previous build
rm -rf "$APP_DIR"

# Create .app bundle structure
mkdir -p "$MACOS" "$RESOURCES/data"

# ─── Compile native Swift app ─────────────────────────────
echo "⚙️  Compiling native app ..."
swiftc -O \
    -o "$MACOS/ClaudeUsageDashboard" \
    "$SCRIPT_DIR/App.swift" \
    -framework Cocoa \
    -framework WebKit \
    -target "$(uname -m)-apple-macos12.0"
echo "  ✅ Binary compiled"

# Copy the core files into Resources
cp "$SCRIPT_DIR/collect-usage.js" "$RESOURCES/"
cp "$SCRIPT_DIR/dashboard.html" "$RESOURCES/"

# Copy the modular CSS and JS directories
cp -r "$SCRIPT_DIR/css" "$RESOURCES/"
cp -r "$SCRIPT_DIR/js" "$RESOURCES/"

# Create Info.plist
cat > "$CONTENTS/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>ClaudeUsageDashboard</string>
    <key>CFBundleName</key>
    <string>Claude Usage Dashboard</string>
    <key>CFBundleDisplayName</key>
    <string>Claude Usage Dashboard</string>
    <key>CFBundleIdentifier</key>
    <string>com.openclaw.usage-dashboard</string>
    <key>CFBundleVersion</key>
    <string>2.0</string>
    <key>CFBundleShortVersionString</key>
    <string>2.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>LSMinimumSystemVersion</key>
    <string>12.0</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>
PLIST

# ─── Generate app icon from logo.svg ─────────────────────
SVG="$SCRIPT_DIR/logo.svg"
if [ -f "$SVG" ]; then
    echo "🎨 Generating app icon from logo.svg ..."
    ICONSET="$RESOURCES/AppIcon.iconset"
    mkdir -p "$ICONSET"

    # Render SVG at each required size using Swift (preserves transparency)
    swift - "$SVG" "$ICONSET" << 'SWIFT'
    import Cocoa
    let args = CommandLine.arguments
    let svgPath = args[1]
    let outDir = args[2]
    let sizes = [16, 32, 64, 128, 256, 512, 1024]
    let svgData = try! Data(contentsOf: URL(fileURLWithPath: svgPath))
    let svgImage = NSImage(data: svgData)!
    for size in sizes {
        let s = CGFloat(size)
        let rep = NSBitmapImageRep(
            bitmapDataPlanes: nil, pixelsWide: size, pixelsHigh: size,
            bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true,
            isPlanar: false, colorSpaceName: .deviceRGB,
            bytesPerRow: 0, bitsPerPixel: 0)!
        rep.size = NSSize(width: s, height: s)
        NSGraphicsContext.saveGraphicsState()
        NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
        svgImage.draw(in: NSRect(x: 0, y: 0, width: s, height: s))
        NSGraphicsContext.restoreGraphicsState()
        let png = rep.representation(using: .png, properties: [:])!
        let outURL = URL(fileURLWithPath: outDir).appendingPathComponent("icon_\(size)x\(size).png")
        try! png.write(to: outURL)
    }
SWIFT

    # Map to Apple's expected @2x naming
    cd "$ICONSET"
    cp icon_32x32.png   icon_16x16@2x.png   2>/dev/null
    cp icon_64x64.png   icon_32x32@2x.png   2>/dev/null
    cp icon_256x256.png icon_128x128@2x.png 2>/dev/null
    cp icon_512x512.png icon_256x256@2x.png 2>/dev/null
    cp icon_1024x1024.png icon_512x512@2x.png 2>/dev/null
    rm -f icon_64x64.png icon_1024x1024.png
    cd "$SCRIPT_DIR"

    # Convert iconset → icns
    if command -v iconutil &>/dev/null; then
        iconutil -c icns "$ICONSET" -o "$RESOURCES/AppIcon.icns" 2>/dev/null \
            && echo "  ✅ AppIcon.icns created" \
            || echo "  ⚠️  iconutil failed — app will use default icon"
    fi
    rm -rf "$ICONSET"
else
    echo "  ⚠️  logo.svg not found — app will use default icon"
fi

# ─── Done ─────────────────────────────────────────────────
echo ""
echo "✅ Built: $APP_DIR"
echo ""
echo "You can now:"
echo "  • Double-click '$APP_NAME.app' in Finder"
echo "  • Drag it to /Applications or your Desktop"
echo "  • It opens as a native app — no browser or Python needed"
```

## File: `collect-usage.js`
```javascript
#!/usr/bin/env node
/**
 * Claude Usage Collector v4
 * 
 * Tracks usage across ALL local Claude tools:
 *   ✅ OpenClaw / Clawdbot      (~/.openclaw/ , ~/.clawdbot/)
 *   ✅ Claude Code CLI           (~/.claude/projects/)
 *   ✅ Claude Desktop (Agent)    (~/Library/Application Support/Claude/local-agent-mode-sessions/)
 *   ✅ Cursor                    (~/.cursor/ or ~/Library/Application Support/Cursor/)
 *   ✅ Windsurf                  (~/.windsurf/ or ~/Library/Application Support/Windsurf/)
 *   ✅ Cline (VS Code ext)       (~/.cline/ or VS Code extension storage)
 *   ✅ Roo Code (VS Code ext)    (~/.roo-code/ or VS Code extension storage)
 *   ✅ Continue.dev              (~/.continue/)
 *   ✅ Aider                     (~/.aider/)
 * 
 * Auto-detects which tools are installed and parses their JSONL/log files.
 * Attributes costs to actual dates from timestamps (not file mod dates).
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const OUTPUT_DIR = path.join(__dirname, 'data');
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
const CACHE_FILE = path.join(OUTPUT_DIR, 'sessions-cache.json');

const HOME = os.homedir();
const TZ_OFFSET = -new Date().getTimezoneOffset() / 60;

// ─── Helpers ─────────────────────────────────────────────

function toLocalDate(timestampMs) {
  if (!timestampMs) return null;
  const d = new Date(timestampMs + TZ_OFFSET * 3600000);
  return d.toISOString().split('T')[0];
}

function toLocalTime(timestampMs) {
  if (!timestampMs) return null;
  const d = new Date(timestampMs + TZ_OFFSET * 3600000);
  return d.toISOString().split('T')[1].substring(0, 5);
}

function parseTimestamp(ts) {
  if (!ts) return null;
  if (typeof ts === 'number') return ts;
  if (typeof ts === 'string') {
    const d = new Date(ts);
    return isNaN(d.getTime()) ? null : d.getTime();
  }
  return null;
}

function getPricing(model) {
  if (!model) return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
  const m = model.toLowerCase();
  if (m.includes('opus-4-6') || m.includes('opus-4.6') || m.includes('opus-4-5') || m.includes('opus-4.5'))
    return { input: 5, output: 25, cacheWrite: 6.25, cacheRead: 0.50 };
  if (m.includes('opus-4-1') || m.includes('opus-4.1'))
    return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };
  if (m.includes('opus'))
    return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };
  if (m.includes('sonnet'))
    return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
  if (m.includes('haiku-4-5') || m.includes('haiku-4.5'))
    return { input: 1, output: 5, cacheWrite: 1.25, cacheRead: 0.10 };
  if (m.includes('haiku'))
    return { input: 0.25, output: 1.25, cacheWrite: 0.30, cacheRead: 0.03 };
  return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
}

// Recursively find JSONL files
function findJsonl(dir, maxDepth = 10) {
  const results = [];
  if (maxDepth <= 0) return results;
  try {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory() && !entry.name.startsWith('.git')) {
        results.push(...findJsonl(fullPath, maxDepth - 1));
      } else if (entry.name.endsWith('.jsonl') && !entry.name.includes('audit')) {
        results.push(fullPath);
      }
    }
  } catch {}
  return results;
}

function makeDayEntry() {
  return { cost: 0, input_tokens: 0, output_tokens: 0, cache_read: 0, cache_write: 0, models: new Set(), times: [] };
}

/**
 * Clean raw message text: strip XML tags, system markers, cron prefixes.
 */
function cleanMessageText(text) {
  text = text.replace(/<[^>]+>[\s\S]*?<\/[^>]+>/g, '').trim();
  text = text.replace(/<[^>]+>/g, '').trim();
  text = text.replace(/^\[SUGGESTION MODE:[^\]]*\]\s*/i, '').trim();
  const cronMatch = text.match(/^\[cron:[a-f0-9-]+\s+([^\]]*)\]\s*(.*)/i);
  if (cronMatch) {
    text = cronMatch[1].trim() + (cronMatch[2] ? ' — ' + cronMatch[2].trim() : '');
  }
  return text;
}

/**
 * Extract text content from a JSONL message entry's content field.
 */
function extractText(msg) {
  if (!msg || typeof msg !== 'object') return '';
  const content = msg.content;
  if (typeof content === 'string') return content;
  if (Array.isArray(content)) {
    // Check if this is a tool_result (skip it)
    if (content.some(b => b.type === 'tool_result')) return '';
    const textBlock = content.find(c => c.type === 'text' && c.text && c.text.trim());
    return textBlock ? textBlock.text : '';
  }
  return '';
}

/**
 * Extract session metadata + conversation history from a JSONL file.
 * Returns: { title, sessionId, cwd, history: [{role, text}] }
 */
function extractSessionMeta(filePath) {
  const meta = { title: '', sessionId: '', cwd: '', history: [] };
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split('\n').filter(l => l.trim());
    let foundTitle = false;

    for (const line of lines) {
      let entry;
      try { entry = JSON.parse(line); } catch { continue; }

      // Extract sessionId and cwd from any entry that has them
      if (!meta.sessionId && entry.sessionId) meta.sessionId = entry.sessionId;
      if (!meta.cwd && entry.cwd) meta.cwd = entry.cwd;

      // Skip non-conversation entries
      const msg = entry.message;
      if (!msg || typeof msg !== 'object') continue;
      const role = msg.role;
      if (role !== 'user' && role !== 'assistant') continue;

      const rawText = extractText(msg);
      if (!rawText) continue;
      const text = cleanMessageText(rawText);
      if (!text) continue;

      // Set title from first user message
      if (!foundTitle && role === 'user') {
        meta.title = text.length > 80 ? text.substring(0, 77) + '...' : text;
        foundTitle = true;
      }

      // Add to history (max 15 turns, 120 chars each)
      if (meta.history.length < 15) {
        meta.history.push({
          role: role === 'user' ? 'user' : 'ai',
          text: text.length > 120 ? text.substring(0, 117) + '...' : text
        });
      }
    }
  } catch {}
  // Fallback: derive sessionId from filename
  if (!meta.sessionId) {
    const base = path.basename(filePath, '.jsonl');
    if (/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/.test(base)) {
      meta.sessionId = base;
    }
  }
  return meta;
}

function pushSessions(sessions, dayData, source, fileName, meta) {
  meta = meta || {};
  for (const [date, data] of Object.entries(dayData)) {
    if (data.cost < 0.0001) continue;
    const models = [...data.models];
    const time = data.times.length > 0 ? data.times.sort()[0] : '00:00';
    const entry = {
      date,
      time,
      source,
      file: fileName,
      cost: parseFloat(data.cost.toFixed(4)),
      input_tokens: data.input_tokens,
      output_tokens: data.output_tokens,
      cache_read: data.cache_read,
      cache_write: data.cache_write,
      model: models[models.length - 1] || ''
    };
    if (meta.title) entry.title = meta.title;
    if (meta.sessionId) entry.sessionId = meta.sessionId;
    if (meta.cwd) entry.cwd = meta.cwd;
    if (meta.history && meta.history.length > 0) entry.history = meta.history;
    sessions.push(entry);
  }
}

// ─── Cache helpers ───────────────────────────────────────

function loadCache() {
  try {
    if (!fs.existsSync(CACHE_FILE)) return [];
    const raw = fs.readFileSync(CACHE_FILE, 'utf-8');
    const data = JSON.parse(raw);
    if (!Array.isArray(data)) {
      console.warn('⚠️  Cache file has unexpected format, ignoring.');
      return [];
    }
    // Per-entry validation: keep only entries with required fields
    const valid = data.filter(s =>
      s && typeof s.source === 'string' && typeof s.file === 'string' &&
      typeof s.date === 'string' && typeof s.cost === 'number'
    );
    if (valid.length < data.length) {
      console.warn(`⚠️  Filtered out ${data.length - valid.length} malformed cache entries`);
    }
    return valid;
  } catch (e) {
    if (e.code !== 'ENOENT') {
      console.warn(`⚠️  Could not load cache: ${e.message}`);
    }
    return [];
  }
}

function saveCache(sessions) {
  try {
    const tmpFile = CACHE_FILE + '.tmp';
    fs.writeFileSync(tmpFile, JSON.stringify(sessions));
    fs.renameSync(tmpFile, CACHE_FILE);
  } catch (e) {
    console.warn(`⚠️  Could not save cache: ${e.message}`);
  }
}

function mergeSessions(freshSessions, cachedSessions) {
  const freshKeys = new Set();
  for (const s of freshSessions) {
    freshKeys.add(`${s.source}|${s.file}|${s.date}`);
  }
  const merged = [...freshSessions];
  for (const s of cachedSessions) {
    const key = `${s.source}|${s.file}|${s.date}`;
    if (!freshKeys.has(key)) {
      merged.push(s);
    }
  }
  return merged;
}

// ─── Parser: OpenClaw / Clawdbot format ──────────────────
// usage fields: usage.input, usage.output, usage.cacheRead, usage.cacheWrite
// OR pre-computed usage.cost.total
function parseOpenClawFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    const msg = entry.message;
    const usage = (msg && msg.usage) || entry.usage;
    if (!usage) continue;
    if (!usage.cost && !usage.input && !usage.output) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(msg && msg.timestamp);
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = (msg && msg.model) || entry.model || '';
    if (model && model.startsWith('claude')) dd.models.add(model);

    if (usage.cost && usage.cost.total) {
      dd.cost += usage.cost.total;
    } else {
      const pricing = getPricing(model);
      const inp = usage.input || 0;
      const out = usage.output || 0;
      const cr = usage.cacheRead || 0;
      const cw = usage.cacheWrite || 0;
      dd.cost += (inp * pricing.input + out * pricing.output + cw * pricing.cacheWrite + cr * pricing.cacheRead) / 1000000;
    }
    dd.input_tokens += (usage.input || 0);
    dd.output_tokens += (usage.output || 0);
    dd.cache_read += (usage.cacheRead || 0);
    dd.cache_write += (usage.cacheWrite || 0);
  }
  return dayData;
}

// ─── Parser: Claude Code / Desktop / Cursor / Windsurf format ────
// usage fields: usage.input_tokens, usage.output_tokens,
//               usage.cache_creation_input_tokens, usage.cache_read_input_tokens
function parseClaudeCodeFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }
    const msg = entry.message;
    const usage = (msg && msg.usage) || entry.usage;
    if (!usage) continue;

    const inputTok = usage.input_tokens || 0;
    const outputTok = usage.output_tokens || 0;
    const cacheWrite = usage.cache_creation_input_tokens || 0;
    const cacheRead = usage.cache_read_input_tokens || 0;
    if (inputTok === 0 && outputTok === 0 && cacheRead === 0 && cacheWrite === 0) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(msg && msg.timestamp);
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = (msg && msg.model) || entry.model || '';
    if (model && model.startsWith('claude')) dd.models.add(model);

    dd.input_tokens += inputTok;
    dd.output_tokens += outputTok;
    dd.cache_read += cacheRead;
    dd.cache_write += cacheWrite;

    const pricing = getPricing(model);
    dd.cost += (inputTok * pricing.input + outputTok * pricing.output + cacheWrite * pricing.cacheWrite + cacheRead * pricing.cacheRead) / 1000000;
  }
  return dayData;
}

// ─── Parser: Aider format ────────────────────────────────
// Aider uses a different log format — .aider.input.history and .aider.chat.history
// It also can write JSONL with litellm format
function parseAiderFormat(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  const dayData = {};
  let fallbackDate = null;
  try { fallbackDate = toLocalDate(fs.statSync(filePath).mtimeMs); } catch {}

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch { continue; }

    // Aider litellm JSONL: { model, usage: { prompt_tokens, completion_tokens, total_tokens }, ... }
    const usage = entry.usage || entry.response?.usage;
    if (!usage) continue;

    const inputTok = usage.prompt_tokens || usage.input_tokens || 0;
    const outputTok = usage.completion_tokens || usage.output_tokens || 0;
    const cacheRead = usage.cache_read_input_tokens || 0;
    const cacheWrite = usage.cache_creation_input_tokens || 0;
    if (inputTok === 0 && outputTok === 0) continue;

    let tsMs = parseTimestamp(entry.timestamp) || parseTimestamp(entry.created);
    // Aider sometimes uses Unix epoch seconds
    if (entry.created && typeof entry.created === 'number' && entry.created < 2000000000) {
      tsMs = entry.created * 1000;
    }
    let date = tsMs ? toLocalDate(tsMs) : fallbackDate;
    let time = tsMs ? toLocalTime(tsMs) : '00:00';
    if (!date) continue;

    if (!dayData[date]) dayData[date] = makeDayEntry();
    const dd = dayData[date];
    if (time) dd.times.push(time);

    const model = entry.model || '';
    if (model && model.includes('claude')) dd.models.add(model);

    dd.input_tokens += inputTok;
    dd.output_tokens += outputTok;
    dd.cache_read += cacheRead;
    dd.cache_write += cacheWrite;

    const pricing = getPricing(model);
    dd.cost += (inputTok * pricing.input + outputTok * pricing.output + cacheWrite * pricing.cacheWrite + cacheRead * pricing.cacheRead) / 1000000;
  }
  return dayData;
}

// ─── Parser: Continue.dev format ─────────────────────────
// Continue stores in ~/.continue/sessions/ as JSON with completions
function parseContinueFormat(filePath) {
  const dayData = {};
  try {
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const steps = data.steps || data.history || [];
    for (const step of steps) {
      const usage = step.usage || step.promptTokens ? { input_tokens: step.promptTokens || 0, output_tokens: step.completionTokens || 0 } : null;
      if (!usage && !step.tokens) continue;

      const inputTok = usage?.input_tokens || step.promptTokens || 0;
      const outputTok = usage?.output_tokens || step.completionTokens || 0;
      if (inputTok === 0 && outputTok === 0) continue;

      let tsMs = parseTimestamp(step.timestamp) || parseTimestamp(data.dateCreated);
      let date = tsMs ? toLocalDate(tsMs) : null;
      let time = tsMs ? toLocalTime(tsMs) : '00:00';
      if (!date) {
        try { date = toLocalDate(fs.statSync(filePath).mtimeMs); } catch { continue; }
      }

      if (!dayData[date]) dayData[date] = makeDayEntry();
      const dd = dayData[date];
      if (time) dd.times.push(time);

      const model = step.model || data.model || '';
      if (model && model.includes('claude')) dd.models.add(model);

      dd.input_tokens += inputTok;
      dd.output_tokens += outputTok;

      const pricing = getPricing(model);
      dd.cost += (inputTok * pricing.input + outputTok * pricing.output) / 1000000;
    }
  } catch {}
  return dayData;
}

// ─── Source Collectors ───────────────────────────────────

function collectOpenClaw() {
  const sessions = [];
  const seenFiles = new Set();
  for (const dirName of ['openclaw', 'clawdbot']) {
    const sessDir = path.join(HOME, `.${dirName}/agents/main/sessions`);
    if (!fs.existsSync(sessDir)) continue;
    const source = dirName === 'openclaw' ? 'OpenClaw' : 'Clawdbot';
    const files = fs.readdirSync(sessDir).filter(f => f.endsWith('.jsonl'));
    for (const file of files) {
      if (seenFiles.has(file)) continue;
      seenFiles.add(file);
      try {
        const fullPath = path.join(sessDir, file);
        const dayData = parseOpenClawFormat(fullPath);
        const meta = extractSessionMeta(fullPath);
        pushSessions(sessions, dayData, source, file, meta);
      } catch (e) { console.error(`  Error: ${file}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectClaudeCode() {
  const sessions = [];
  const claudeDir = path.join(HOME, '.claude/projects');
  if (!fs.existsSync(claudeDir)) return sessions;
  const files = findJsonl(claudeDir);
  for (const filePath of files) {
    try {
      const dayData = parseClaudeCodeFormat(filePath);
      const meta = extractSessionMeta(filePath);
      pushSessions(sessions, dayData, 'Claude Code', path.basename(filePath), meta);
    } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
  }
  return sessions;
}

function collectClaudeDesktop() {
  const sessions = [];
  const baseDir = path.join(HOME, 'Library/Application Support/Claude/local-agent-mode-sessions');
  if (!fs.existsSync(baseDir)) return sessions;
  // Find all JSONL files recursively (exclude audit.jsonl)
  const files = findJsonl(baseDir);
  for (const filePath of files) {
    try {
      const dayData = parseClaudeCodeFormat(filePath); // Same format as Claude Code
      const meta = extractSessionMeta(filePath);
      pushSessions(sessions, dayData, 'Claude Desktop', path.basename(filePath), meta);
    } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
  }
  return sessions;
}

function collectCursor() {
  const sessions = [];
  // Cursor stores projects in multiple possible locations
  const searchDirs = [
    path.join(HOME, '.cursor/projects'),
    path.join(HOME, 'Library/Application Support/Cursor/User/workspaceStorage'),
  ];
  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    const files = findJsonl(dir);
    for (const filePath of files) {
      try {
        const dayData = parseClaudeCodeFormat(filePath);
        const meta = extractSessionMeta(filePath);
        pushSessions(sessions, dayData, 'Cursor', path.basename(filePath), meta);
      } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectWindsurf() {
  const sessions = [];
  const searchDirs = [
    path.join(HOME, '.windsurf/projects'),
    path.join(HOME, '.windsurf'),
    path.join(HOME, 'Library/Application Support/Windsurf/User/workspaceStorage'),
  ];
  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    const files = findJsonl(dir);
    for (const filePath of files) {
      try {
        const dayData = parseClaudeCodeFormat(filePath);
        const meta = extractSessionMeta(filePath);
        pushSessions(sessions, dayData, 'Windsurf', path.basename(filePath), meta);
      } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectCline() {
  const sessions = [];
  // Cline stores task data in VS Code extension globalStorage
  const searchDirs = [
    path.join(HOME, '.cline'),
    path.join(HOME, 'Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev'),
    path.join(HOME, 'Library/Application Support/Code/User/globalStorage/cline.cline'),
  ];
  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    const files = findJsonl(dir);
    for (const filePath of files) {
      try {
        // Cline uses a mix of formats — try Claude Code format first
        const dayData = parseClaudeCodeFormat(filePath);
        const meta = extractSessionMeta(filePath);
        pushSessions(sessions, dayData, 'Cline', path.basename(filePath), meta);
      } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectRooCode() {
  const sessions = [];
  const searchDirs = [
    path.join(HOME, '.roo-code'),
    path.join(HOME, 'Library/Application Support/Code/User/globalStorage/rooveterinaryinc.roo-cline'),
  ];
  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    const files = findJsonl(dir);
    for (const filePath of files) {
      try {
        const dayData = parseClaudeCodeFormat(filePath);
        const meta = extractSessionMeta(filePath);
        pushSessions(sessions, dayData, 'Roo Code', path.basename(filePath), meta);
      } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectAider() {
  const sessions = [];
  const searchDirs = [
    path.join(HOME, '.aider'),
    path.join(HOME, '.aider/logs'),
  ];
  for (const dir of searchDirs) {
    if (!fs.existsSync(dir)) continue;
    const files = [];
    try {
      for (const f of fs.readdirSync(dir)) {
        if (f.endsWith('.jsonl') || f.endsWith('.json')) {
          files.push(path.join(dir, f));
        }
      }
    } catch {}
    for (const filePath of files) {
      try {
        const dayData = parseAiderFormat(filePath);
        pushSessions(sessions, dayData, 'Aider', path.basename(filePath), {});
      } catch (e) { console.error(`  Error: ${filePath}: ${e.message}`); }
    }
  }
  return sessions;
}

function collectContinue() {
  const sessions = [];
  const sessDir = path.join(HOME, '.continue/sessions');
  if (!fs.existsSync(sessDir)) return sessions;
  try {
    for (const f of fs.readdirSync(sessDir)) {
      if (!f.endsWith('.json')) continue;
      try {
        const dayData = parseContinueFormat(path.join(sessDir, f));
        pushSessions(sessions, dayData, 'Continue', f, {});
      } catch {}
    }
  } catch {}
  return sessions;
}

// ─── Main ────────────────────────────────────────────────

console.log('Claude Usage Collector v4');
console.log('========================\n');

const sources = [
  { name: 'OpenClaw / Clawdbot', fn: collectOpenClaw },
  { name: 'Claude Code CLI',     fn: collectClaudeCode },
  { name: 'Claude Desktop',      fn: collectClaudeDesktop },
  { name: 'Cursor',              fn: collectCursor },
  { name: 'Windsurf',            fn: collectWindsurf },
  { name: 'Cline',               fn: collectCline },
  { name: 'Roo Code',            fn: collectRooCode },
  { name: 'Aider',               fn: collectAider },
  { name: 'Continue.dev',        fn: collectContinue },
];

let allSessions = [];
const sourceResults = {};

for (const { name, fn } of sources) {
  process.stdout.write(`Scanning ${name}... `);
  const sessions = fn();
  if (sessions.length > 0) {
    console.log(`✅ ${sessions.length} session-day entries`);
    sourceResults[name] = sessions.length;
  } else {
    console.log(`— not found or empty`);
  }
  allSessions.push(...sessions);
}

console.log('');

// Load cached historical sessions and merge with fresh data
const cachedSessions = loadCache();
if (cachedSessions.length > 0) {
  console.log(`📦 Loaded ${cachedSessions.length} cached session entries`);
}
allSessions = mergeSessions(allSessions, cachedSessions);
if (cachedSessions.length > 0) {
  console.log(`📊 Total after merge: ${allSessions.length} session-day entries\n`);
}

// Generate summary
const today = toLocalDate(Date.now());
const currentMonth = today.substring(0, 7);

const sourceTotals = {};
const sourceCounts = {};
allSessions.forEach(s => {
  sourceTotals[s.source] = (sourceTotals[s.source] || 0) + s.cost;
  sourceCounts[s.source] = (sourceCounts[s.source] || 0) + 1;
});
const grandTotal = allSessions.reduce((s, x) => s + x.cost, 0);

for (const key of Object.keys(sourceTotals)) {
  sourceTotals[key] = parseFloat(sourceTotals[key].toFixed(2));
}

const todayCost = allSessions.filter(s => s.date === today).reduce((s, x) => s + x.cost, 0);
const monthCost = allSessions.filter(s => s.date.startsWith(currentMonth)).reduce((s, x) => s + x.cost, 0);

const summary = {
  generated_at: new Date().toISOString(),
  today,
  current_month: currentMonth,
  totals: {
    ...sourceTotals,
    grand_total: parseFloat(grandTotal.toFixed(2))
  },
  today_cost: parseFloat(todayCost.toFixed(2)),
  month_cost: parseFloat(monthCost.toFixed(2)),
  session_counts: {
    ...sourceCounts,
    total: allSessions.length
  }
};

// Separate sessions by type for backward-compatible data.js
const openclawSessions = allSessions.filter(s => s.source === 'OpenClaw' || s.source === 'Clawdbot');
const otherSessions = allSessions.filter(s => s.source !== 'OpenClaw' && s.source !== 'Clawdbot');

// Save cache (atomic write) before generating data.js
saveCache(allSessions);

const dataJs = `// Auto-generated by collect-usage.js v4 — ${new Date().toISOString()}
window.__SUMMARY__ = ${JSON.stringify(summary, null, 2)};
window.__OPENCLAW_SESSIONS__ = ${JSON.stringify(openclawSessions)};
window.__CLAUDE_SESSIONS__ = ${JSON.stringify(otherSessions)};
`;
fs.writeFileSync(path.join(OUTPUT_DIR, 'data.js'), dataJs);
console.log(`📄 Data written to: ${path.join(OUTPUT_DIR, 'data.js')}`);

console.log('\n✅ Done!');
console.log('================================');
console.log(JSON.stringify(summary, null, 2));
```

## File: `dashboard.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claude Usage Dashboard</title>
    <script src="data/data.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <!-- Base styles -->
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/layout.css">

    <!-- Component styles -->
    <link rel="stylesheet" href="css/components/header.css">
    <link rel="stylesheet" href="css/components/stat-cards.css">
    <link rel="stylesheet" href="css/components/charts.css">
    <link rel="stylesheet" href="css/components/filter-bar.css">
    <link rel="stylesheet" href="css/components/sessions-table.css">
    <link rel="stylesheet" href="css/components/table-rows.css">
    <link rel="stylesheet" href="css/components/detail-panel.css">
    <link rel="stylesheet" href="css/components/badges.css">
    <link rel="stylesheet" href="css/components/heatmap.css">
    <link rel="stylesheet" href="css/components/projects-table.css">
    <link rel="stylesheet" href="css/components/expensive-callout.css">
    <link rel="stylesheet" href="css/components/footer.css">
    <link rel="stylesheet" href="css/components/reload-fab.css">
    <link rel="stylesheet" href="css/components/data-transfer.css">

    <!-- Utilities -->
    <link rel="stylesheet" href="css/utilities.css">
</head>
<body>
    <div class="ambient-blob"></div>
    <div class="container">
        <header>
            <div class="header-left">
                <div class="logo-mark"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="none"><defs><linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient><linearGradient id="glowGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#34d399" stop-opacity="0.25"/><stop offset="50%" stop-color="#22d3ee" stop-opacity="0.08"/><stop offset="100%" stop-color="#a78bfa" stop-opacity="0.25"/></linearGradient><linearGradient id="bar1" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#34d399"/></linearGradient><linearGradient id="bar2" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#22d3ee"/></linearGradient><linearGradient id="bar3" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#60a5fa"/></linearGradient><linearGradient id="bar4" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#fb7185"/><stop offset="100%" stop-color="#a78bfa"/></linearGradient><linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#fb7185"/></linearGradient><linearGradient id="areaFill" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fbbf24" stop-opacity="0.15"/><stop offset="100%" stop-color="#fb7185" stop-opacity="0.02"/></linearGradient></defs><rect width="512" height="512" rx="108" ry="108" fill="#0f1629"/><rect width="512" height="512" rx="108" ry="108" fill="url(#glowGrad)" opacity="0.5"/><rect x="3" y="3" width="506" height="506" rx="105" ry="105" fill="none" stroke="url(#bgGrad)" stroke-width="1.5" opacity="0.4"/><rect x="80" y="100" width="352" height="312" rx="20" ry="20" fill="#131b2e" opacity="0.6"/><line x1="110" y1="370" x2="402" y2="370" stroke="#253147" stroke-width="1.5" opacity="0.6"/><line x1="110" y1="296" x2="402" y2="296" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="3,5" opacity="0.4"/><line x1="110" y1="222" x2="402" y2="222" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="3,5" opacity="0.4"/><rect x="122" y="238" width="50" height="132" rx="8" ry="8" fill="url(#bar1)" opacity="0.92"/><rect x="192" y="168" width="50" height="202" rx="8" ry="8" fill="url(#bar2)" opacity="0.92"/><rect x="262" y="206" width="50" height="164" rx="8" ry="8" fill="url(#bar3)" opacity="0.92"/><rect x="332" y="128" width="50" height="242" rx="8" ry="8" fill="url(#bar4)" opacity="0.92"/><polygon points="147,226 217,156 287,192 357,122 357,370 147,370" fill="url(#areaFill)" opacity="0.6"/><polyline points="147,226 217,156 287,192 357,122" fill="none" stroke="url(#lineGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.95"/><circle cx="147" cy="226" r="4.5" fill="#fbbf24"/><circle cx="217" cy="156" r="4.5" fill="#f59e0b"/><circle cx="287" cy="192" r="4.5" fill="#e879a0"/><circle cx="357" cy="122" r="4.5" fill="#fb7185"/></svg></div>
                <div>
                    <h1><span>Claude</span> Usage Tracker</h1>
                </div>
            </div>
            <div class="header-meta">
                <span class="updated"><span class="status-dot"></span>Last sync: <span id="last-updated">—</span></span>
                <div class="dt-actions">
                    <button class="dt-btn dt-btn-export" id="dt-export-btn" type="button" title="Export data as JSON">
                        <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                        Export
                    </button>
                    <button class="dt-btn dt-btn-import" id="dt-import-btn" type="button" title="Import data from another device">
                        <svg viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                        Import
                    </button>
                </div>
            </div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="label">Today</div>
                <div class="value" id="today-cost">$0.00</div>
                <div class="yesterday-delta" id="yesterday-delta"></div>
                <div class="subtext" id="today-date">—</div>
            </div>
            <div class="stat-card">
                <div class="label">This Week</div>
                <div class="value" id="week-cost">$0.00</div>
                <div class="subtext" id="week-range">&mdash;</div>
            </div>
            <div class="stat-card">
                <div class="label">This Month</div>
                <div class="value" id="month-cost">$0.00</div>
                <div class="subtext" id="month-name">—</div>
                <div class="projection-line" id="month-projection" style="display:none;"></div>
            </div>
            <div class="stat-card">
                <div class="label">All Time</div>
                <div class="value" id="total-cost">$0.00</div>
                <div class="subtext">Since tracking began</div>
            </div>
            <div class="stat-card">
                <div class="label">Sessions</div>
                <div class="value" id="session-count">0</div>
                <div class="subtext">Across all sources</div>
            </div>
        </div>

        <div class="chart-card chart-card-full">
            <h3>Daily Spend by Source <span class="chart-hint">click bar to filter</span></h3>
            <div class="chart-canvas-wrap">
                <canvas id="dailyChart"></canvas>
            </div>
        </div>

        <div id="day-filter-bar" style="display:none">
            <span class="day-filter-label">Filtered: <strong id="day-filter-date"></strong></span>
            <button class="day-filter-clear" onclick="clearDayFilter()">&#x2715; clear</button>
        </div>

        <div class="charts-grid-half">
            <div class="chart-card">
                <h3>By Source</h3>
                <div class="chart-canvas-wrap">
                    <canvas id="sourceChart"></canvas>
                </div>
            </div>
            <div class="chart-card">
                <h3>Spend by Model</h3>
                <div class="chart-canvas-wrap">
                    <canvas id="modelChart"></canvas>
                </div>
            </div>
        </div>

        <div class="heatmap-section">
            <div class="heatmap-header">
                <h3 id="heatmap-title">Peak Hours</h3>
                <div class="heatmap-toggle" id="heatmap-toggle">
                    <div class="heatmap-toggle-slider" id="heatmap-toggle-slider"></div>
                    <button class="heatmap-toggle-btn active" data-view="hours" id="toggle-hours-btn">Hours</button>
                    <button class="heatmap-toggle-btn" data-view="days" id="toggle-days-btn">Days</button>
                </div>
            </div>

            <!-- Hours View — actual dates × 24 hour columns -->
            <div class="heatmap-view heatmap-view-active" id="heatmap-hours-view">
                <div class="heatmap-hours-grid" id="heatmap-hours-grid"></div>
            </div>

            <!-- Days View (new) -->
            <div class="heatmap-view" id="heatmap-days-view">
                <div class="heatmap-days-container">
                    <div class="heatmap-days-day-labels" id="heatmap-days-day-labels"></div>
                    <div class="heatmap-days-grid-wrapper">
                        <div class="heatmap-days-month-labels" id="heatmap-days-month-labels"></div>
                        <div class="heatmap-days-grid" id="heatmap-days-grid"></div>
                    </div>
                </div>
            </div>

            <div class="heatmap-legend">
                <span class="heatmap-legend-label">Less</span>
                <div class="heatmap-legend-cell" style="background: rgba(30, 41, 59, 0.25); border: 1px solid rgba(30, 41, 59, 0.15);"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(34, 211, 238, 0.15), rgba(34, 211, 238, 0.25));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(34, 211, 238, 0.4), rgba(96, 165, 250, 0.55));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.55), rgba(249, 158, 11, 0.7));"></div>
                <div class="heatmap-legend-cell" style="background: linear-gradient(135deg, rgba(251, 113, 133, 0.7), rgba(244, 63, 94, 0.85));"></div>
                <span class="heatmap-legend-label">More</span>
            </div>
        </div>
        <div class="heatmap-tooltip" id="heatmap-tooltip">
            <div class="tip-day"></div>
            <div class="tip-hour"></div>
            <div class="tip-stats">
                <div class="tip-stat"><span class="tip-label">Sessions</span><span class="tip-value tip-count"></span></div>
                <div class="tip-stat"><span class="tip-label">Cost</span><span class="tip-value tip-cost"></span></div>
            </div>
        </div>

        <!-- Most Expensive Session Callout -->
        <div class="expensive-callout" id="expensive-session-callout" style="display: none;">
            <div class="expensive-callout-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/>
                    <path d="M12 8v4"/>
                    <path d="M12 16h.01"/>
                </svg>
            </div>
            <div class="expensive-callout-content">
                <div class="expensive-callout-title">Most Expensive Session Today</div>
                <div class="expensive-callout-details">
                    <span class="expensive-detail" id="exp-source"></span>
                    <span class="expensive-detail" id="exp-model"></span>
                    <span class="expensive-detail expensive-detail-time" id="exp-time"></span>
                    <span class="expensive-detail expensive-detail-cost" id="exp-cost"></span>
                </div>
                <div class="expensive-callout-tokens" id="exp-tokens"></div>
            </div>
        </div>

        <div class="sessions-section">
            <div class="sessions-header">
                <h3>Session Log</h3>
                <div class="view-toggle" id="sessions-view-toggle">
                    <div class="view-toggle-slider"></div>
                    <button class="view-toggle-btn active" data-view="timeline">Timeline</button>
                    <button class="view-toggle-btn" data-view="projects">Projects</button>
                </div>
                <div class="sessions-header-right">
                    <span class="hint">click a row to expand</span>
                    <button class="toggle-all-btn" id="toggle-all-btn" onclick="toggleAllDays()" title="Expand or collapse all date rows (Shift+E)">
                        Expand All<span class="arrow">&#9660;</span><span class="kbd-hint">Shift+E</span>
                    </button>
                </div>
            </div>
            <div class="filter-bar" id="filter-bar">
                <div class="filter-controls">
                    <!-- Source multi-select -->
                    <div class="filter-group" id="source-filter-group">
                        <button class="filter-btn" id="source-filter-btn" type="button">
                            Source <span class="chevron-down">&#9662;</span>
                        </button>
                        <div class="filter-dropdown" id="source-dropdown">
                            <!-- Populated dynamically -->
                        </div>
                    </div>

                    <!-- Model multi-select -->
                    <div class="filter-group" id="model-filter-group">
                        <button class="filter-btn" id="model-filter-btn" type="button">
                            Model <span class="chevron-down">&#9662;</span>
                        </button>
                        <div class="filter-dropdown" id="model-dropdown">
                            <!-- Populated dynamically -->
                        </div>
                    </div>

                    <!-- Date range -->
                    <span class="filter-label">From</span>
                    <input type="date" class="filter-date" id="filter-date-from" />
                    <span class="filter-label">To</span>
                    <input type="date" class="filter-date" id="filter-date-to" />

                    <!-- Min cost -->
                    <div class="filter-cost-wrapper">
                        <span class="dollar-sign">$</span>
                        <input type="number" class="filter-cost" id="filter-min-cost"
                               placeholder="Min" step="0.01" min="0" />
                    </div>

                    <!-- Status -->
                    <div class="filter-status">
                        <span class="filter-count" id="filter-count"></span>
                        <button class="filter-clear-btn" id="filter-clear-btn" type="button">Clear All</button>
                    </div>
                </div>
                <div class="filter-chips" id="filter-chips"></div>
            </div>
            <div class="sessions-table-wrap">
                <table>
                    <thead id="sessions-thead">
                        <tr>
                            <th>Date</th>
                            <th>Sessions</th>
                            <th>Models</th>
                            <th>Input</th>
                            <th>Output</th>
                            <th>Cache Read</th>
                            <th>Cache Write</th>
                            <th style="text-align:right">Cost</th>
                        </tr>
                    </thead>
                    <tbody id="sessions-body">
                        <tr><td colspan="8" class="no-data">Loading data…</td></tr>
                    </tbody>
                    <tfoot id="sessions-tfoot">
                    </tfoot>
                </table>
            </div>
        </div>

        <div class="footer">
            <span id="footer-text">claude usage dashboard</span>
        </div>
    </div>

    <!-- Floating Reload Button -->
    <button class="reload-fab" id="reload-fab" type="button" aria-label="Refresh data">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <defs>
                <linearGradient id="reloadGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#22d3ee"/>
                    <stop offset="100%" stop-color="#a78bfa"/>
                </linearGradient>
            </defs>
            <polyline points="23 4 23 10 17 10" stroke="url(#reloadGrad)"/>
            <polyline points="1 20 1 14 7 14" stroke="url(#reloadGrad)"/>
            <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" stroke="url(#reloadGrad)"/>
        </svg>
        <span class="fab-tip">Refresh Data <span class="kbd">&#8984;R</span></span>
    </button>

    <script type="module" src="js/main.js"></script>
</body>
</html>
```

## File: `README.md`
```markdown
# 🧾 Claude Usage Tracker

> Track and visualize Claude AI usage costs across all your local development tools.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey.svg)
![Node](https://img.shields.io/badge/node-%3E%3D16-green.svg)

## Overview

**Claude Usage Tracker** is a local-first tool that automatically discovers and aggregates your Claude AI usage across **9+ development tools**, including:

- **OpenClaw / Clawdbot** — AI agent framework
- **Claude Code CLI** — Anthropic's official CLI
- **Claude Desktop** — Anthropic's desktop app (local agent mode)
- **Cursor** — AI-powered code editor
- **Windsurf** — Codeium's AI IDE
- **Cline** — VS Code Claude extension
- **Roo Code** — VS Code AI assistant
- **Aider** — AI pair programming (litellm)
- **Continue.dev** — Open-source AI code assistant

It scans known data directories, parses JSONL/log files, calculates costs using model-specific pricing, and presents everything in a beautiful **dark-themed interactive dashboard** powered by Chart.js.

No cloud. No telemetry. Everything stays on your machine.

---

## ✨ Features

| Category | Details |
|----------|---------|
| **Multi-Source Tracking** | Auto-detects 9+ Claude-integrated tools and merges usage data |
| **Beautiful Dashboard** | Dark-themed UI with Chart.js visualizations |
| **Cost Breakdown** | Daily, weekly, monthly, and all-time cost tracking |
| **Model Analytics** | Per-model cost breakdown across Opus, Sonnet, and Haiku families |

| **Heatmaps** | Two views — Peak Hours (day × hour grid) and Peak Days (GitHub-style calendar) |
| **Session Log** | Expandable day-by-day session details with color-coded source cards |
| **Projects View** | Group sessions by working directory to see per-project cost breakdown |
| **Filtering** | Multi-criteria filtering (source, model, date range, min cost) with visual chips |
| **Monthly Projections** | Projected monthly cost based on current spending pace |
| **Yesterday Delta** | Compare today's spending vs yesterday at a glance |
| **Most Expensive Session** | Callout highlighting the priciest session of the day |
| **Keyboard Shortcuts** | `Shift+E` to expand/collapse all session rows |
| **macOS App** | Build a standalone `.app` bundle for double-click launching |
| **Animated Counters** | Smooth easing animations on stat cards |
| **Responsive Design** | Adapts to different screen sizes |

---

## 📸 Screenshots

<p align="center">
  <img src="screenshots/dashboard-overview.png" alt="Dashboard Overview" width="800" />
</p>
<p align="center"><em>Dashboard — stats, daily spend chart, source & model breakdowns</em></p>

<p align="center">
  <img src="screenshots/heatmap.png" alt="Peak Hours Heatmap" width="800" />
</p>
<p align="center"><em>Peak Hours heatmap & most expensive session callout</em></p>

<p align="center">
  <img src="screenshots/session-log.png" alt="Session Log" width="800" />
</p>
<p align="center"><em>Session log with filters, expandable day rows, and per-session costs</em></p>

<p align="center">
  <img src="screenshots/projects-view.png" alt="Projects View" width="800" />
</p>
<p align="center"><em>Projects view — see cost breakdown grouped by working directory</em></p>

<p align="center">
  <img src="screenshots/session-detail.png" alt="Session Detail" width="500" />
</p>
<p align="center"><em>Session detail panel — token breakdown, conversation history, resume command</em></p>

---

## 🚀 Quick Start

### Download (Recommended)

**Latest Release: v2.1.0**

| Platform | Download |
|----------|----------|
| macOS (Apple Silicon) | [GitHub](https://github.com/658jjh/claude-usage-tracker/releases/download/v2.1.0/Claude-Usage-Tracker-macOS-AppleSilicon.zip) |
| macOS (Intel) | [GitHub](https://github.com/658jjh/claude-usage-tracker/releases/download/v2.1.0/Claude-Usage-Tracker-macOS-Intel.zip) |

> Requires **Node.js** (v16+) and **macOS 12.0+**

Unzip, drag **Claude Usage Dashboard.app** to Applications, and double-click to launch.

[View all releases →](https://github.com/658jjh/claude-usage-tracker/releases)

### Build from Source

```bash
git clone https://github.com/658jjh/claude-usage-tracker.git
cd claude-usage-tracker
./build-app.sh
```

Then double-click **Claude Usage Dashboard.app** — it collects fresh data and renders everything in a native window.

### Browser Mode (Any OS)

```bash
node collect-usage.js
python3 -m http.server 8765
open http://localhost:8765/dashboard.html
```

---

## 📊 Supported Tools

| Tool | Data Location | Format |
|------|---------------|--------|
| **OpenClaw / Clawdbot** | `~/.openclaw/agents/main/sessions/` or `~/.clawdbot/...` | JSONL |
| **Claude Code CLI** | `~/.claude/projects/` | JSONL |
| **Claude Desktop** | `~/Library/Application Support/Claude/local-agent-mode-sessions/` | JSONL |
| **Cursor** | `~/.cursor/projects/` or `~/Library/Application Support/Cursor/` | JSONL |
| **Windsurf** | `~/.windsurf/` or `~/Library/Application Support/Windsurf/` | JSONL |
| **Cline** | `~/.cline/` or VS Code extension storage | JSONL |
| **Roo Code** | `~/.roo-code/` or VS Code extension storage | JSONL |
| **Aider** | `~/.aider/` | JSONL (litellm) |
| **Continue.dev** | `~/.continue/sessions/` | JSON |

> **Note:** Tool detection is automatic. If a tool isn't installed or has no data, it's silently skipped.

---

## 💰 Pricing Models

Costs are calculated using Anthropic's per-million-token pricing. The tracker supports all current and upcoming model families:

### Current Models

| Model | Input ($/MTok) | Output ($/MTok) | Cache Write ($/MTok) | Cache Read ($/MTok) |
|-------|:--------------:|:---------------:|:--------------------:|:-------------------:|
| **Opus 4.5 / 4.6** | $5.00 | $25.00 | $6.25 | $0.50 |
| **Opus 4.0 / 4.1** | $15.00 | $75.00 | $18.75 | $1.50 |
| **Sonnet 3.5 / 3.7 / 4.0 / 4.5 / 4.6** | $3.00 | $15.00 | $3.75 | $0.30 |
| **Haiku 4.0 / 4.5** | $1.00 | $5.00 | $1.25 | $0.10 |
| **Haiku 3.0 / 3.5** | $0.25 | $1.25 | $0.30 | $0.03 |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/my-feature`
3. **Commit** your changes: `git commit -m "feat: add my feature"`
4. **Push** to your fork: `git push origin feat/my-feature`
5. **Open** a Pull Request

Please follow the existing code style and commit message conventions (`feat:`, `fix:`, `docs:`, `chore:`).

### Ideas for Contributions

- Add support for additional AI tools
- Improve mobile responsiveness
- Add data export (CSV, JSON)
- Add cost alerts / budget thresholds
- Linux / Windows path support
- Electron or Tauri desktop app

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ for the Claude community

</div>
```

## File: `css/base.css`
```css
:root {
    --bg-primary: #0a0e17;
    --bg-secondary: #111827;
    --bg-card: #151d2e;
    --bg-card-hover: #1a2540;
    --bg-elevated: #1e293b;
    --border: #1e293b;
    --border-light: #253147;
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent-cyan: #22d3ee;
    --accent-cyan-dim: rgba(34, 211, 238, 0.15);
    --accent-amber: #fbbf24;
    --accent-amber-dim: rgba(251, 191, 36, 0.12);
    --accent-emerald: #34d399;
    --accent-emerald-dim: rgba(52, 211, 153, 0.12);
    --accent-rose: #fb7185;
    --accent-rose-dim: rgba(251, 113, 133, 0.12);
    --accent-violet: #a78bfa;
    --accent-violet-dim: rgba(167, 139, 250, 0.12);
    --accent-blue: #60a5fa;
    --accent-blue-dim: rgba(96, 165, 250, 0.12);
    --glow-cyan: 0 0 20px rgba(34, 211, 238, 0.15);
    --radius: 12px;
    --radius-sm: 8px;
    --radius-pill: 20px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Outfit', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    overflow-x: hidden;
}

/* Ambient glow blobs — static, no filters */
body::after {
    content: '';
    position: fixed;
    top: -20%;
    right: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(34, 211, 238, 0.06) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
    will-change: auto;
}

.ambient-blob {
    position: fixed;
    bottom: -15%;
    left: -5%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(251, 191, 36, 0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}
```

## File: `css/layout.css`
```css
.container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 32px 40px;
    position: relative;
    z-index: 1;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    margin-bottom: 32px;
}

/* Charts */
.charts-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
}

.charts-grid-half {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
}

/* Responsive */
@media (max-width: 1280px) {
    .stats-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 1024px) {
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .charts-grid { grid-template-columns: 1fr; }
    .charts-grid-half { grid-template-columns: 1fr; }
    .container { padding: 20px; }
    .filter-controls { gap: 8px; }
}

@media (max-width: 640px) {
    .stats-grid { grid-template-columns: 1fr; }
    header { flex-direction: column; align-items: flex-start; gap: 12px; }
    .header-meta { align-items: flex-start; }
    header h1 { font-size: 1.3rem; }

    .expensive-callout {
        flex-direction: column;
        gap: 10px;
    }

    .expensive-callout-details {
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
    }

    .filter-controls {
        flex-direction: column;
        align-items: stretch;
    }
    .filter-status { margin-left: 0; justify-content: space-between; }
    .filter-date { width: 100%; }
    .filter-cost { width: 100%; }
}
```

## File: `css/utilities.css`
```css
/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-light); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* Global Animations */
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Selection styling */
::selection {
    background: rgba(34, 211, 238, 0.2);
    color: var(--text-primary);
}
```

## File: `css/components/badges.css`
```css
/* Badges */
.source-badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.03em;
}

.source-openclaw {
    background: var(--accent-amber-dim);
    color: var(--accent-amber);
    border: 1px solid rgba(251, 191, 36, 0.2);
}

.source-claude {
    background: var(--accent-blue-dim);
    color: var(--accent-blue);
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.source-desktop {
    background: var(--accent-violet-dim);
    color: var(--accent-violet);
    border: 1px solid rgba(167, 139, 250, 0.2);
}

.source-cursor {
    background: var(--accent-cyan-dim);
    color: var(--accent-cyan);
    border: 1px solid rgba(34, 211, 238, 0.2);
}

.source-windsurf {
    background: var(--accent-emerald-dim);
    color: var(--accent-emerald);
    border: 1px solid rgba(52, 211, 153, 0.2);
}

.source-cline {
    background: var(--accent-rose-dim);
    color: var(--accent-rose);
    border: 1px solid rgba(251, 113, 133, 0.2);
}

.source-aider {
    background: rgba(45, 212, 191, 0.12);
    color: #2dd4bf;
    border: 1px solid rgba(45, 212, 191, 0.2);
}

.source-continue {
    background: var(--accent-amber-dim);
    color: var(--accent-amber);
    border: 1px solid rgba(251, 191, 36, 0.2);
}

.model-badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    letter-spacing: 0.03em;
}

.model-opus {
    background: var(--accent-violet-dim);
    color: var(--accent-violet);
    border: 1px solid rgba(167, 139, 250, 0.2);
}

.model-sonnet {
    background: var(--accent-blue-dim);
    color: var(--accent-blue);
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.model-haiku {
    background: var(--accent-emerald-dim);
    color: var(--accent-emerald);
    border: 1px solid rgba(52, 211, 153, 0.2);
}

.cost-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: var(--radius-pill);
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.75rem;
}

.cost-low {
    background: var(--accent-emerald-dim);
    color: var(--accent-emerald);
}

.cost-medium {
    background: var(--accent-amber-dim);
    color: var(--accent-amber);
}

.cost-high {
    background: var(--accent-rose-dim);
    color: var(--accent-rose);
}
```

## File: `css/components/charts.css`
```css
/* Chart Cards — compact, constrained, clean */

.chart-card {
    background: linear-gradient(135deg, rgba(21, 29, 46, 0.95) 0%, rgba(17, 24, 39, 0.95) 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    animation: fadeSlideUp 0.6s ease forwards;
    animation-delay: 0.25s;
    opacity: 0;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, background 0.3s ease, box-shadow 0.3s ease;
    contain: content;
}

/* Subtle top gradient accent line */
.chart-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(34, 211, 238, 0.3), rgba(167, 139, 250, 0.3), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.chart-card:hover {
    border-color: rgba(34, 211, 238, 0.12);
    background: linear-gradient(135deg, rgba(26, 37, 64, 0.95) 0%, rgba(21, 29, 46, 0.95) 100%);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.chart-card:hover::before {
    opacity: 1;
}

.chart-card h3 {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.8rem;
    color: var(--text-primary);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
    letter-spacing: 0.01em;
}

.chart-card h3::before {
    content: '';
    display: inline-block;
    width: 3px;
    height: 14px;
    background: linear-gradient(180deg, var(--accent-cyan), var(--accent-violet));
    border-radius: 2px;
    flex-shrink: 0;
}

/* Full-width bar chart card */
.chart-card-full {
    margin-bottom: 16px;
}

.chart-card-full h3::before {
    background: linear-gradient(180deg, var(--accent-cyan), var(--accent-blue));
}

/* Constrain bar chart height */
.chart-card-full .chart-canvas-wrap {
    position: relative;
    height: 260px;
}

/* Constrain doughnut chart height */
.chart-card .chart-canvas-wrap {
    position: relative;
    height: 220px;
}

.chart-card canvas {
    border-radius: 4px;
}

/* "click bar to filter" hint beside chart title */
.chart-hint {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    font-weight: 400;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    margin-left: auto;
    opacity: 0.7;
}

/* Day filter indicator bar */
#day-filter-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
    padding: 7px 14px;
    background: rgba(34, 211, 238, 0.06);
    border: 1px solid rgba(34, 211, 238, 0.18);
    border-radius: var(--radius-sm);
    animation: fadeSlideUp 0.25s ease forwards;
}

.day-filter-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--text-secondary);
}

.day-filter-label strong {
    color: var(--accent-cyan);
    font-weight: 600;
}

.day-filter-clear {
    margin-left: auto;
    background: none;
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: var(--radius-pill);
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    padding: 3px 10px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.day-filter-clear:hover {
    border-color: rgba(34, 211, 238, 0.5);
    color: var(--accent-cyan);
    background: rgba(34, 211, 238, 0.06);
}
```

## File: `css/components/data-transfer.css`
```css
/* ── Data Transfer (Export / Import) ─────────── */

.dt-actions {
    display: flex;
    gap: 8px;
}

.dt-btn {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 6px 12px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.02em;
    cursor: pointer;
    transition: border-color 0.2s ease, color 0.2s ease, background 0.2s ease, box-shadow 0.2s ease;
    white-space: nowrap;
    -webkit-app-region: no-drag;
}

.dt-btn svg {
    width: 14px;
    height: 14px;
    stroke: currentColor;
    fill: none;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex-shrink: 0;
}

.dt-btn:hover {
    border-color: var(--accent-cyan);
    color: var(--text-primary);
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.08);
}

.dt-btn:active {
    transform: scale(0.97);
    transition-duration: 0.05s;
}

.dt-btn-export:hover {
    border-color: var(--accent-emerald);
    color: var(--accent-emerald);
    box-shadow: 0 0 12px rgba(52, 211, 153, 0.1);
}

.dt-btn-import:hover {
    border-color: var(--accent-violet);
    color: var(--accent-violet);
    box-shadow: 0 0 12px rgba(167, 139, 250, 0.1);
}

/* ── Toast ──────────────────────────────────── */

.dt-toast {
    position: fixed;
    bottom: 90px;
    right: 28px;
    z-index: 1100;
    padding: 10px 18px;
    background: var(--bg-card);
    border: 1px solid var(--accent-emerald);
    border-radius: var(--radius-sm);
    color: var(--accent-emerald);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4), 0 0 16px rgba(52, 211, 153, 0.08);
    opacity: 0;
    transform: translateY(8px);
    pointer-events: none;
    transition: opacity 0.25s ease, transform 0.25s ease;
}

.dt-toast-visible {
    opacity: 1;
    transform: translateY(0);
}

.dt-toast-error {
    border-color: var(--accent-rose);
    color: var(--accent-rose);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4), 0 0 16px rgba(251, 113, 133, 0.08);
}

/* ── Import banner ──────────────────────────── */

.dt-import-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 20px;
    margin-bottom: 20px;
    background: var(--accent-violet-dim);
    border: 1px solid rgba(167, 139, 250, 0.25);
    border-radius: var(--radius-sm);
    animation: fadeSlideUp 0.3s ease forwards;
}

.dt-import-banner-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--accent-violet);
}

.dt-import-banner-text strong {
    color: var(--text-primary);
    font-weight: 600;
}

.dt-import-dismiss {
    padding: 4px 10px;
    background: transparent;
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: var(--radius-sm);
    color: var(--accent-violet);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    cursor: pointer;
    transition: background 0.2s ease;
}

.dt-import-dismiss:hover {
    background: rgba(167, 139, 250, 0.12);
}

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
```

## File: `css/components/detail-panel.css`
```css
/* Detail panel */
.day-detail-row td {
    padding: 0 !important;
    border-bottom: 1px solid var(--border);
}

.day-detail-wrapper {
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: opacity 0.25s ease;
}

.day-detail-wrapper.open {
    max-height: none;
    opacity: 1;
}

.day-detail {
    padding: 20px 24px;
    background: rgba(0, 0, 0, 0.15);
    border-top: 1px solid var(--border);
}

/* Source breakdown */
.source-breakdown {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 12px;
    margin-bottom: 16px;
}

.source-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    padding: 16px;
    border-left: 3px solid var(--text-muted);
    animation: fadeSlideUp 0.35s ease forwards;
    opacity: 0;
}

.source-card:nth-child(1) { animation-delay: 0.05s; }
.source-card:nth-child(2) { animation-delay: 0.12s; }

.source-card.border-openclaw { border-left-color: var(--accent-amber); }
.source-card.border-claude { border-left-color: var(--accent-blue); }
.source-card.border-desktop { border-left-color: var(--accent-violet); }
.source-card.border-cursor { border-left-color: var(--accent-cyan); }
.source-card.border-windsurf { border-left-color: var(--accent-emerald); }
.source-card.border-cline { border-left-color: var(--accent-rose); }
.source-card.border-aider { border-left-color: #2dd4bf; }
.source-card.border-continue { border-left-color: var(--accent-amber); }

.source-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.source-card-header .source-name { font-weight: 600; font-size: 0.85rem; }
.source-card-header .source-cost { font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 1rem; }
.source-card-header .source-cost.cost-low-text { color: var(--accent-emerald); }
.source-card-header .source-cost.cost-medium-text { color: var(--accent-amber); }
.source-card-header .source-cost.cost-high-text { color: var(--accent-rose); }

.source-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px 16px;
}

.source-stat {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
}

.source-stat .stat-label { color: var(--text-muted); }
.source-stat .stat-value {
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-secondary);
    font-weight: 500;
}

/* Cost bar */
.cost-bar-container { margin-top: 10px; }
.cost-bar-bg {
    height: 4px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
}

.cost-bar-fill {
    height: 100%;
    border-radius: 2px;
    transform-origin: left;
    transform: scaleX(0);
    transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}

.cost-bar-fill.fill-openclaw { background: linear-gradient(90deg, var(--accent-amber), #f59e0b); }
.cost-bar-fill.fill-claude { background: linear-gradient(90deg, var(--accent-blue), var(--accent-violet)); }
.cost-bar-fill.fill-desktop { background: linear-gradient(90deg, var(--accent-violet), #c4b5fd); }
.cost-bar-fill.fill-cursor { background: linear-gradient(90deg, var(--accent-cyan), #67e8f9); }
.cost-bar-fill.fill-windsurf { background: linear-gradient(90deg, var(--accent-emerald), #6ee7b7); }
.cost-bar-fill.fill-cline { background: linear-gradient(90deg, var(--accent-rose), #fda4af); }
.cost-bar-fill.fill-aider { background: linear-gradient(90deg, #2dd4bf, #5eead4); }
.cost-bar-fill.fill-continue { background: linear-gradient(90deg, var(--accent-amber), #fcd34d); }

/* Sub-table */
.session-subtable { width: 100%; border-collapse: collapse; margin-top: 12px; }

.session-subtable th {
    background: rgba(0, 0, 0, 0.3);
    color: var(--text-muted);
    font-size: 0.6rem;
    padding: 8px 12px;
}

.session-subtable td {
    padding: 8px 12px;
    font-size: 0.78rem;
    border-bottom: 1px solid var(--border);
}

.session-subtable tr:last-child td { border-bottom: none; }
.session-subtable tr:hover { background: rgba(34, 211, 238, 0.03); }

.session-title-cell {
    max-width: 220px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 0.72rem;
    color: var(--text-muted);
}

/* Clickable session rows */
.session-clickable { cursor: pointer; }
.session-clickable:hover { background: rgba(34, 211, 238, 0.08) !important; }

/* ─── Session Detail Modal ───────────────────────────── */
.session-modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.7);
    z-index: 900;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease;
}
.session-modal-overlay.visible { opacity: 1; pointer-events: auto; }

.session-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.95);
    width: 520px;
    max-width: 92vw;
    max-height: 85vh;
    overflow-y: auto;
    background: linear-gradient(135deg, rgba(21, 29, 46, 0.98) 0%, rgba(13, 18, 30, 0.98) 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(34, 211, 238, 0.08);
    z-index: 901;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease, transform 0.2s ease;
}
.session-modal.visible { opacity: 1; pointer-events: auto; transform: translate(-50%, -50%) scale(1); }

.session-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 20px 24px 16px;
    border-bottom: 1px solid var(--border);
    gap: 12px;
}

.session-modal-title {
    font-family: 'Outfit', sans-serif;
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.4;
    word-break: break-word;
}

.session-modal-close {
    background: none;
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text-muted);
    font-size: 1.2rem;
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0;
    transition: color 0.15s ease, border-color 0.15s ease;
}
.session-modal-close:hover { color: var(--text-primary); border-color: var(--text-muted); }

.session-modal-body { padding: 16px 24px 24px; }

.session-modal-meta {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 18px;
}

.session-meta-row {
    display: flex;
    align-items: center;
    gap: 12px;
}

.meta-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    width: 80px;
    flex-shrink: 0;
}

.meta-value {
    font-size: 0.82rem;
    color: var(--text-secondary);
}

.meta-mono {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    word-break: break-all;
}

.session-modal-tokens {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 2px;
    background: rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 18px;
}

.token-stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 6px;
    background: rgba(21, 29, 46, 0.6);
}

.token-stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--text-muted);
    margin-bottom: 4px;
}

.token-stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-secondary);
}

.token-stat-value.cost-value {
    font-size: 0.85rem;
}

/* Conversation History */
.session-modal-history {
    margin-bottom: 18px;
}

.history-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-bottom: 10px;
}

.history-timeline {
    display: flex;
    flex-direction: column;
    gap: 6px;
    max-height: 260px;
    overflow-y: auto;
    padding-right: 4px;
}

.history-msg {
    padding: 8px 12px;
    border-radius: 8px;
    border: 1px solid var(--border);
}

.history-user {
    background: rgba(99, 102, 241, 0.06);
    border-color: rgba(99, 102, 241, 0.15);
    margin-right: 24px;
}

.history-ai {
    background: rgba(34, 211, 238, 0.04);
    border-color: rgba(34, 211, 238, 0.10);
    margin-left: 24px;
}

.history-role {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 3px;
}

.history-user .history-role { color: rgba(129, 140, 248, 0.8); }
.history-ai .history-role { color: rgba(34, 211, 238, 0.7); }

.history-text {
    font-size: 0.75rem;
    line-height: 1.45;
    color: var(--text-secondary);
    word-break: break-word;
}

.history-truncated {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    color: var(--text-muted);
    padding: 6px 0 2px;
}

/* Resume section */
.session-modal-resume {
    background: rgba(34, 211, 238, 0.04);
    border: 1px solid rgba(34, 211, 238, 0.15);
    border-radius: 8px;
    padding: 14px 16px;
}

.resume-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--accent-cyan);
    margin-bottom: 10px;
}

.resume-cmd-row {
    display: flex;
    align-items: center;
    gap: 8px;
}

.resume-cmd {
    flex: 1;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-secondary);
    background: rgba(0, 0, 0, 0.3);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 12px;
    overflow-x: auto;
    white-space: nowrap;
}

.resume-copy-btn {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    color: var(--accent-cyan);
    background: var(--accent-cyan-dim);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 6px;
    padding: 8px 14px;
    cursor: pointer;
    white-space: nowrap;
    transition: color 0.2s ease, background 0.2s ease, border-color 0.2s ease;
    flex-shrink: 0;
}
.resume-copy-btn:hover {
    background: rgba(34, 211, 238, 0.22);
    border-color: var(--accent-cyan);
}
.resume-copy-btn.copied {
    color: var(--accent-emerald);
    border-color: rgba(52, 211, 153, 0.3);
    background: rgba(52, 211, 153, 0.1);
}
```

## File: `css/components/expensive-callout.css`
```css
/* Most Expensive Session Callout */
.expensive-callout {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    background: linear-gradient(135deg, rgba(251, 113, 133, 0.06) 0%, rgba(251, 191, 36, 0.04) 100%);
    border: 1px solid rgba(251, 113, 133, 0.15);
    border-left: 2px solid var(--accent-rose);
    border-radius: var(--radius);
    padding: 18px 24px;
    margin-bottom: 24px;
    animation: fadeSlideUp 0.6s ease forwards;
    animation-delay: 0.28s;
    opacity: 0;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    contain: content;
}

.expensive-callout:hover {
    border-color: rgba(251, 113, 133, 0.25);
    box-shadow: 0 4px 20px rgba(251, 113, 133, 0.06);
}

.expensive-callout-icon {
    flex-shrink: 0;
    width: 36px;
    height: 36px;
    background: var(--accent-rose-dim);
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent-rose);
    margin-top: 2px;
}

.expensive-callout-content {
    flex: 1;
    min-width: 0;
}

.expensive-callout-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    color: var(--accent-rose);
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.expensive-callout-details {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
}

.expensive-detail {
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.expensive-detail-time {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-muted);
}

.expensive-detail-cost {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--accent-rose);
    background: var(--accent-rose-dim);
    padding: 3px 10px;
    border-radius: var(--radius-pill);
}

.expensive-callout-tokens {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--text-muted);
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
}

.expensive-callout-tokens .token-label {
    color: var(--text-muted);
}

.expensive-callout-tokens .token-value {
    color: var(--text-secondary);
    font-weight: 500;
}
```

## File: `css/components/filter-bar.css`
```css
/* ── Filter Bar ──────────────────────────────── */
.filter-bar {
    padding: 16px 24px 12px;
    border-bottom: 1px solid var(--border);
    background: rgba(0, 0, 0, 0.15);
}

.filter-controls {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
}

.filter-group {
    position: relative;
}

.filter-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 7px 12px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    cursor: pointer;
    transition: border-color 0.2s ease, color 0.2s ease, background 0.2s ease;
    white-space: nowrap;
}

.filter-btn:hover {
    border-color: var(--accent-cyan);
    color: var(--text-primary);
}

.filter-btn.active {
    border-color: var(--accent-cyan);
    background: var(--accent-cyan-dim);
    color: var(--accent-cyan);
}

.filter-btn .chevron-down {
    font-size: 0.5rem;
    transition: transform 0.2s ease;
}

.filter-btn.open .chevron-down {
    transform: rotate(180deg);
}

/* Multi-select dropdown */
.filter-dropdown {
    position: absolute;
    top: calc(100% + 6px);
    left: 0;
    min-width: 200px;
    background: var(--bg-card);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    z-index: 50;
    display: none;
    padding: 6px 0;
    max-height: 280px;
    overflow-y: auto;
}

.filter-dropdown.open {
    display: block;
}

.filter-dropdown label {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    cursor: pointer;
    font-size: 0.78rem;
    color: var(--text-secondary);
    transition: background 0.15s ease;
}

.filter-dropdown label:hover {
    background: var(--bg-card-hover);
}

.filter-dropdown input[type="checkbox"] {
    appearance: none;
    -webkit-appearance: none;
    width: 14px;
    height: 14px;
    border: 1.5px solid var(--border-light);
    border-radius: 3px;
    background: var(--bg-elevated);
    cursor: pointer;
    position: relative;
    flex-shrink: 0;
}

.filter-dropdown input[type="checkbox"]:checked {
    background: var(--accent-cyan);
    border-color: var(--accent-cyan);
}

.filter-dropdown input[type="checkbox"]:checked::after {
    content: '';
    position: absolute;
    left: 3.5px;
    top: 1px;
    width: 4px;
    height: 7px;
    border: solid var(--bg-primary);
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
}

/* Date inputs */
.filter-date {
    padding: 7px 10px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    width: 130px;
    color-scheme: dark;
    transition: border-color 0.2s ease;
}

.filter-date:focus {
    outline: none;
    border-color: var(--accent-cyan);
}

.filter-date::-webkit-calendar-picker-indicator {
    filter: invert(0.6);
    cursor: pointer;
}

/* Min cost input */
.filter-cost-wrapper {
    position: relative;
    display: flex;
    align-items: center;
}

.filter-cost-wrapper .dollar-sign {
    position: absolute;
    left: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    pointer-events: none;
}

.filter-cost {
    padding: 7px 10px 7px 22px;
    background: var(--bg-elevated);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    color: var(--text-secondary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    width: 90px;
    transition: border-color 0.2s ease;
}

.filter-cost:focus {
    outline: none;
    border-color: var(--accent-cyan);
}

/* Remove spinner arrows from number input */
.filter-cost::-webkit-outer-spin-button,
.filter-cost::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
.filter-cost { -moz-appearance: textfield; }

/* Filter status & clear */
.filter-status {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 12px;
}

.filter-count {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-muted);
    white-space: nowrap;
}

.filter-count .count-highlight {
    color: var(--accent-cyan);
    font-weight: 600;
}

.filter-clear-btn {
    padding: 6px 12px;
    background: transparent;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    cursor: pointer;
    transition: border-color 0.2s ease, color 0.2s ease;
    display: none;
}

.filter-clear-btn.visible {
    display: inline-flex;
}

.filter-clear-btn:hover {
    border-color: var(--accent-rose);
    color: var(--accent-rose);
}

/* Filter chips row */
.filter-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding-top: 10px;
}

.filter-chips:empty {
    display: none;
}

.filter-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 3px 8px 3px 10px;
    border-radius: var(--radius-pill);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.02em;
    border: 1px solid;
    animation: fadeSlideUp 0.2s ease forwards;
}

.filter-chip .chip-remove {
    cursor: pointer;
    font-size: 0.7rem;
    opacity: 0.6;
    transition: opacity 0.15s ease;
    line-height: 1;
}

.filter-chip .chip-remove:hover {
    opacity: 1;
}

/* Chip color variants (reuse existing source/model dim colors) */
.chip-source {
    background: var(--accent-blue-dim);
    color: var(--accent-blue);
    border-color: rgba(96, 165, 250, 0.25);
}

.chip-model {
    background: var(--accent-violet-dim);
    color: var(--accent-violet);
    border-color: rgba(167, 139, 250, 0.25);
}

.chip-date {
    background: var(--accent-emerald-dim);
    color: var(--accent-emerald);
    border-color: rgba(52, 211, 153, 0.25);
}

.chip-cost {
    background: var(--accent-amber-dim);
    color: var(--accent-amber);
    border-color: rgba(251, 191, 36, 0.25);
}

/* Label before date/cost inputs */
.filter-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
```

## File: `css/components/footer.css`
```css
/* Footer */
.footer {
    text-align: center;
    padding: 24px 0 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
}

.no-data {
    text-align: center;
    padding: 48px;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
}
```

## File: `css/components/header.css`
```css
/* Header */
header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 40px;
    padding-bottom: 28px;
    border-bottom: 1px solid var(--border);
}

.header-left { display: flex; align-items: center; gap: 16px; }

.logo-mark {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 24px rgba(34, 211, 238, 0.2);
    overflow: hidden;
}
.logo-mark svg {
    width: 100%;
    height: 100%;
}

header h1 {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1.6rem;
    letter-spacing: -0.02em;
    color: var(--text-primary);
}

header h1 span {
    background: linear-gradient(90deg, var(--accent-cyan), var(--accent-violet));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.header-meta {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 4px;
}

.header-meta .updated {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
}

.header-meta .status-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    background: var(--accent-emerald);
    border-radius: 50%;
    margin-right: 6px;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
```

## File: `css/components/heatmap.css`
```css
/* Peak Heatmap — toggle, hours view, days view, animations, tooltip */

.heatmap-section {
    background: linear-gradient(135deg, rgba(21, 29, 46, 0.95) 0%, rgba(17, 24, 39, 0.95) 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 28px;
    margin-bottom: 32px;
    animation: fadeSlideUp 0.6s ease forwards;
    animation-delay: 0.28s;
    opacity: 0;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    contain: content;
}

/* Subtle top accent line */
.heatmap-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(251, 113, 133, 0.3), rgba(251, 191, 36, 0.2), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.heatmap-section:hover {
    border-color: rgba(251, 113, 133, 0.12);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.heatmap-section:hover::before {
    opacity: 1;
}

/* ─── Header with Toggle ─────────────────────────────────── */

.heatmap-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}

.heatmap-section h3 {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-bottom: 0;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.01em;
}

.heatmap-section h3::before {
    content: '';
    display: inline-block;
    width: 3px;
    height: 16px;
    background: linear-gradient(180deg, var(--accent-rose), var(--accent-amber));
    border-radius: 2px;
}

/* ─── Segmented Toggle Control ───────────────────────────── */

.heatmap-toggle {
    position: relative;
    display: flex;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(30, 41, 59, 0.6);
    border-radius: 10px;
    padding: 3px;
    gap: 0;
}

.heatmap-toggle-slider {
    position: absolute;
    top: 3px;
    left: 3px;
    width: calc(50% - 3px);
    height: calc(100% - 6px);
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.15), rgba(96, 165, 250, 0.2));
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 8px;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 0;
}

.heatmap-toggle-btn {
    position: relative;
    z-index: 1;
    background: none;
    border: none;
    padding: 6px 16px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    color: var(--text-muted);
    cursor: pointer;
    transition: color 0.25s ease;
    letter-spacing: 0.02em;
    white-space: nowrap;
}

.heatmap-toggle-btn:hover {
    color: var(--text-secondary);
}

.heatmap-toggle-btn.active {
    color: var(--accent-cyan);
}

/* ─── View Transitions ───────────────────────────────────── */

.heatmap-view {
    display: none;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity 0.25s ease, transform 0.25s ease;
}

.heatmap-view-active {
    display: block;
    opacity: 1;
    transform: translateY(0);
    animation: heatmapViewIn 0.3s ease forwards;
}

.heatmap-view-exiting {
    display: block;
    opacity: 0;
    transform: translateY(-6px);
    animation: heatmapViewOut 0.2s ease forwards;
}

@keyframes heatmapViewIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes heatmapViewOut {
    from { opacity: 1; transform: translateY(0); }
    to { opacity: 0; transform: translateY(-6px); }
}

/* ─── Hours View (unified grid: date labels + hour cells) ── */

.heatmap-hours-grid {
    display: grid;
    grid-template-columns: 90px repeat(24, 1fr);
    /* grid-template-rows set dynamically by JS */
    gap: 3px;
    overflow-x: auto;
}

.heatmap-corner {
    /* Empty top-left cell */
}

.heatmap-day-label {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.heatmap-hour-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    color: var(--text-muted);
    text-align: center;
    letter-spacing: 0.02em;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* ─── Days View (GitHub-style calendar) ──────────────────── */

.heatmap-days-container {
    display: flex;
    gap: 0;
}

.heatmap-days-day-labels {
    display: flex;
    flex-direction: column;
    gap: 3px;
    padding-top: 22px;
}

.heatmap-days-day-label {
    height: 18px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    min-width: 36px;
}

.heatmap-days-grid-wrapper {
    flex: 1;
    overflow-x: auto;
}

.heatmap-days-month-labels {
    display: grid;
    gap: 3px;
    margin-bottom: 3px;
    height: 16px;
}

.heatmap-days-month-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
}

.heatmap-days-grid {
    display: grid;
    grid-template-rows: repeat(7, 18px);
    gap: 3px;
    grid-auto-flow: column;
}

.heatmap-days-cell {
    min-width: 14px;
    min-height: 14px;
    border-radius: 3px;
}

.heatmap-days-cell.is-empty {
    visibility: hidden;
}

/* Today indicator - subtle ring */
.heatmap-days-cell.is-today {
    outline: 2px solid rgba(34, 211, 238, 0.5);
    outline-offset: 1px;
}

/* Clickable cursor for days with data */
.heatmap-days-cell:not(.is-empty) {
    cursor: pointer;
}

/* Click pulse animation */
@keyframes cellPulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.4); opacity: 0.7; }
    100% { transform: scale(1.5); opacity: 0; }
}

.heatmap-days-cell.clicked {
    animation: cellPulse 0.4s ease-out;
}

/* ─── Shared Cell Styles ─────────────────────────────────── */

/* Cell entrance animation */
@keyframes heatmapCellIn {
    from {
        opacity: 0;
        transform: scale(0.6);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.heatmap-cell {
    border-radius: 4px;
    min-width: 14px;
    min-height: 14px;
    cursor: pointer;
    position: relative;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.heatmap-cell:hover {
    transform: scale(1.3);
    z-index: 10;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.4);
}

/* Refined intensity color palette with subtle gradients */
.heatmap-cell.level-0 {
    background: rgba(30, 41, 59, 0.25);
    border: 1px solid rgba(30, 41, 59, 0.15);
}

.heatmap-cell.level-1 {
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.15), rgba(34, 211, 238, 0.25));
    border: 1px solid rgba(34, 211, 238, 0.08);
}

.heatmap-cell.level-2 {
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.4), rgba(96, 165, 250, 0.55));
    border: 1px solid rgba(34, 211, 238, 0.12);
}

.heatmap-cell.level-3 {
    background: linear-gradient(135deg, rgba(251, 191, 36, 0.55), rgba(249, 158, 11, 0.7));
    border: 1px solid rgba(251, 191, 36, 0.15);
}

.heatmap-cell.level-4 {
    background: linear-gradient(135deg, rgba(251, 113, 133, 0.7), rgba(244, 63, 94, 0.85));
    border: 1px solid rgba(251, 113, 133, 0.2);
    box-shadow: 0 0 8px rgba(251, 113, 133, 0.15);
}

/* ─── Tooltip — frosted glass effect ─────────────────────── */

.heatmap-tooltip {
    position: fixed;
    background: rgba(15, 23, 42, 0.97);
    border: 1px solid rgba(34, 211, 238, 0.12);
    border-radius: 10px;
    padding: 12px 16px;
    pointer-events: none;
    opacity: 0;
    transform: translateY(4px);
    transition: opacity 0.15s ease, transform 0.15s ease;
    z-index: 1000;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    min-width: 150px;
}

.heatmap-tooltip.visible {
    opacity: 1;
    transform: translateY(0);
}

.heatmap-tooltip .tip-day {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.82rem;
    color: var(--text-primary);
    margin-bottom: 2px;
}

.heatmap-tooltip .tip-hour {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-muted);
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(30, 41, 59, 0.6);
}

.heatmap-tooltip .tip-stats {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.heatmap-tooltip .tip-stat {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    font-size: 0.72rem;
}

.heatmap-tooltip .tip-stat .tip-label {
    color: var(--text-muted);
}

.heatmap-tooltip .tip-stat .tip-value {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    color: var(--accent-cyan);
}

/* ─── Legend ──────────────────────────────────────────────── */

.heatmap-legend {
    display: flex;
    align-items: center;
    gap: 4px;
    margin-top: 16px;
    justify-content: flex-end;
}

.heatmap-legend-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
    padding: 0 4px;
}

.heatmap-legend-cell {
    width: 16px;
    height: 16px;
    border-radius: 4px;
    transition: transform 0.2s ease;
}

.heatmap-legend-cell:hover {
    transform: scale(1.2);
}

/* ─── Scroll Highlight on Session Row ────────────────────── */

@keyframes scrollHighlightPulse {
    0% { background-color: transparent; }
    15% { background-color: rgba(34, 211, 238, 0.04); }
    100% { background-color: transparent; }
}

.day-row.heatmap-scroll-highlight {
    animation: scrollHighlightPulse 1.5s ease-out;
}

/* ─── Responsive ─────────────────────────────────────────── */

/* Click pulse for hours cells too */
.heatmap-cell.clicked {
    animation: cellPulse 0.4s ease-out;
}

@media (max-width: 1024px) {
    .heatmap-hours-grid {
        grid-template-columns: 80px repeat(24, minmax(14px, 1fr));
    }
    .heatmap-days-grid {
        gap: 2px;
    }
}

@media (max-width: 640px) {
    .heatmap-section { padding: 20px; }
    .heatmap-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
    }
    .heatmap-hours-grid {
        grid-template-columns: 64px repeat(24, minmax(10px, 1fr));
        gap: 2px;
    }
    .heatmap-day-label {
        font-size: 0.48rem;
        padding-right: 6px;
    }
    .heatmap-days-day-label {
        font-size: 0.5rem;
        min-width: 24px;
        padding-right: 6px;
    }
    .heatmap-hour-label {
        font-size: 0.45rem;
    }
    .heatmap-days-grid {
        gap: 2px;
        grid-template-rows: repeat(7, 14px);
    }
    .heatmap-days-cell {
        min-width: 10px;
        min-height: 10px;
        border-radius: 2px;
    }
    .heatmap-toggle-btn {
        padding: 5px 12px;
        font-size: 0.65rem;
    }
}
```

## File: `css/components/projects-table.css`
```css
/* ─── Session View Toggle ─────────────────────────────── */

.view-toggle {
    position: relative;
    display: flex;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(30, 41, 59, 0.6);
    border-radius: 10px;
    padding: 3px;
    gap: 0;
}

.view-toggle-slider {
    position: absolute;
    top: 3px;
    left: 3px;
    width: calc(50% - 3px);
    height: calc(100% - 6px);
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.15), rgba(96, 165, 250, 0.2));
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 8px;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 0;
}

.view-toggle-btn {
    position: relative;
    z-index: 1;
    background: none;
    border: none;
    padding: 6px 16px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    color: var(--text-muted);
    cursor: pointer;
    transition: color 0.25s ease;
    letter-spacing: 0.02em;
    white-space: nowrap;
}

.view-toggle-btn:hover {
    color: var(--text-secondary);
}

.view-toggle-btn.active {
    color: var(--accent-cyan);
}

/* ─── Project Rows ────────────────────────────────────── */

.project-row {
    cursor: pointer;
    transition: background 0.2s ease;
}

.project-row:hover {
    background: rgba(34, 211, 238, 0.03);
}

.project-row td:first-child {
    position: relative;
    padding-left: 36px;
    font-weight: 500;
    color: var(--text-primary);
}

.project-row .chevron {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-size: 0.6rem;
    color: var(--text-muted);
}

.project-row.expanded .chevron {
    transform: translateY(-50%) rotate(90deg);
    color: var(--accent-cyan);
}

.project-row.expanded {
    background: rgba(34, 211, 238, 0.04);
}

.project-icon {
    margin-right: 6px;
    font-size: 0.85rem;
}

.project-name {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-primary);
    max-width: 260px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: inline-block;
    vertical-align: middle;
}

.project-meta {
    margin-left: 8px;
    font-size: 0.7rem;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
    vertical-align: middle;
}

/* ─── Project Detail (Expand) ─────────────────────────── */

.project-detail-row td {
    padding: 0 !important;
    border-bottom: 1px solid var(--border);
}

.project-detail-wrapper {
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: opacity 0.25s ease;
}

.project-detail-wrapper.open {
    max-height: none;
    opacity: 1;
}

.project-detail {
    padding: 16px 24px 20px;
    background: rgba(0, 0, 0, 0.15);
    border-top: 1px solid var(--border);
}

/* Reuse session-subtable styles from detail-panel.css — no duplication needed.
   The .session-subtable, .session-clickable, .session-title-cell classes
   are already defined globally. */
```

## File: `css/components/reload-fab.css`
```css
/* Floating Reload Button (FAB) */
.reload-fab {
    position: fixed;
    bottom: 28px;
    right: 28px;
    z-index: 1000;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-card);
    box-shadow:
        0 4px 16px rgba(0, 0, 0, 0.35),
        inset 0 0 0 1px rgba(34, 211, 238, 0.12);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    outline: none;
    -webkit-app-region: no-drag;
}

.reload-fab::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 50%;
    padding: 1px;
    background: linear-gradient(135deg, rgba(34, 211, 238, 0.3), rgba(167, 139, 250, 0.3));
    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.reload-fab:hover {
    transform: scale(1.1);
    box-shadow:
        0 6px 24px rgba(0, 0, 0, 0.4),
        0 0 24px rgba(34, 211, 238, 0.12),
        inset 0 0 0 1px rgba(34, 211, 238, 0.25);
}

.reload-fab:hover::before {
    opacity: 1;
}

.reload-fab:active {
    transform: scale(0.95);
    transition-duration: 0.1s;
}

.reload-fab svg {
    width: 22px;
    height: 22px;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    flex-shrink: 0;
}

/* Spinning state while reloading */
.reload-fab.is-reloading svg {
    animation: fabSpin 0.7s linear infinite;
}

.reload-fab.is-reloading {
    pointer-events: none;
    box-shadow:
        0 4px 16px rgba(0, 0, 0, 0.35),
        0 0 20px rgba(34, 211, 238, 0.2),
        inset 0 0 0 1px rgba(34, 211, 238, 0.3);
}

.reload-fab.is-reloading::before {
    opacity: 1;
    animation: fabGlowPulse 1s ease-in-out infinite;
}

@keyframes fabSpin {
    to { transform: rotate(360deg); }
}

@keyframes fabGlowPulse {
    0%, 100% { opacity: 0.6; }
    50%      { opacity: 1; }
}

/* Tooltip */
.reload-fab .fab-tip {
    position: absolute;
    right: 60px;
    top: 50%;
    transform: translateY(-50%) translateX(4px);
    background: var(--bg-elevated);
    color: var(--text-secondary);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 6px 10px;
    border-radius: var(--radius-sm);
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease, transform 0.2s ease;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
    border: 1px solid var(--border);
}

.reload-fab .fab-tip .kbd {
    display: inline-block;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border-light);
    border-radius: 4px;
    padding: 1px 5px;
    margin-left: 6px;
    font-size: 10px;
    color: var(--text-muted);
}

.reload-fab:hover .fab-tip {
    opacity: 1;
    transform: translateY(-50%) translateX(0);
}
```

## File: `css/components/sessions-table.css`
```css
/* Sessions Table */
.sessions-section {
    background: linear-gradient(135deg, rgba(21, 29, 46, 0.95) 0%, rgba(17, 24, 39, 0.95) 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    animation: fadeSlideUp 0.6s ease forwards;
    animation-delay: 0.3s;
    opacity: 0;
    display: flex;
    flex-direction: column;
    contain: content;
}

.sessions-header {
    padding: 20px 24px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sessions-header h3 {
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.01em;
}

.sessions-header h3::before {
    content: '';
    display: inline-block;
    width: 3px;
    height: 16px;
    background: linear-gradient(180deg, var(--accent-amber), var(--accent-rose));
    border-radius: 2px;
}

.sessions-header .hint {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
}

.sessions-header-right {
    display: flex;
    align-items: center;
    gap: 16px;
}

.toggle-all-btn {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    color: var(--accent-cyan);
    background: var(--accent-cyan-dim);
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: var(--radius-sm);
    padding: 5px 12px;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    white-space: nowrap;
    user-select: none;
}

.toggle-all-btn:hover {
    background: rgba(34, 211, 238, 0.22);
    border-color: var(--accent-cyan);
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.15);
}

.toggle-all-btn:active {
    transform: scale(0.97);
}

.toggle-all-btn .arrow {
    display: inline-block;
    margin-left: 4px;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.toggle-all-btn.is-expanded .arrow {
    transform: rotate(180deg);
}

.toggle-all-btn .kbd-hint {
    display: inline-block;
    margin-left: 6px;
    font-size: 0.55rem;
    color: var(--text-muted);
    background: rgba(0, 0, 0, 0.25);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 1px 4px;
    vertical-align: middle;
    line-height: 1.3;
}

table { width: 100%; border-collapse: collapse; }

th {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    background: rgba(21, 29, 46, 1);
    position: sticky;
    top: 0;
    z-index: 3;
}

td {
    padding: 14px 16px;
    font-size: 0.85rem;
    border-bottom: 1px solid var(--border);
    color: var(--text-secondary);
}

/* Table scroll wrapper */
.sessions-table-wrap {
    max-height: 70vh;
    overflow-y: auto;
    flex: 1;
}

/* Totals row (tfoot) */
tfoot#sessions-tfoot tr {
    position: sticky;
    bottom: 0;
    z-index: 2;
}

tfoot#sessions-tfoot td {
    background: #1a2540;
    border-top: 2px solid var(--accent-cyan);
    border-bottom: none;
    padding: 14px 16px;
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.85rem;
}

tfoot#sessions-tfoot td:first-child {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent-cyan);
}

tfoot#sessions-tfoot .token-cell {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-secondary);
}

tfoot#sessions-tfoot .totals-session-count {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--text-primary);
}

tfoot#sessions-tfoot .totals-models-placeholder {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
}

.token-cell {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-muted);
}
```

## File: `css/components/stat-cards.css`
```css
.stat-card {
    background: linear-gradient(135deg, rgba(21, 29, 46, 0.95) 0%, rgba(17, 24, 39, 0.95) 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease, background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeSlideUp 0.6s ease forwards;
    opacity: 0;
    contain: content;
}

.stat-card:nth-child(1) { animation-delay: 0.05s; }
.stat-card:nth-child(2) { animation-delay: 0.1s; }
.stat-card:nth-child(3) { animation-delay: 0.15s; }
.stat-card:nth-child(4) { animation-delay: 0.2s; }
.stat-card:nth-child(5) { animation-delay: 0.25s; }

.stat-card:hover {
    border-color: rgba(34, 211, 238, 0.1);
    background: linear-gradient(135deg, rgba(26, 37, 64, 0.95) 0%, rgba(21, 29, 46, 0.95) 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 1px;
    opacity: 0.7;
}

.stat-card:nth-child(1)::before { background: linear-gradient(90deg, var(--accent-cyan), transparent); }
.stat-card:nth-child(2)::before { background: linear-gradient(90deg, var(--accent-blue), transparent); }
.stat-card:nth-child(3)::before { background: linear-gradient(90deg, var(--accent-amber), transparent); }
.stat-card:nth-child(4)::before { background: linear-gradient(90deg, var(--accent-emerald), transparent); }
.stat-card:nth-child(5)::before { background: linear-gradient(90deg, var(--accent-violet), transparent); }

.stat-card .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-bottom: 12px;
}

.stat-card .value {
    font-family: 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1;
    margin-bottom: 6px;
}

.stat-card:nth-child(1) .value { color: var(--accent-cyan); }
.stat-card:nth-child(2) .value { color: var(--accent-blue); }
.stat-card:nth-child(3) .value { color: var(--accent-amber); }
.stat-card:nth-child(4) .value { color: var(--accent-emerald); }
.stat-card:nth-child(5) .value { color: var(--accent-violet); }

.stat-card .subtext {
    font-size: 0.78rem;
    color: var(--text-muted);
}

/* Yesterday delta indicator */
.yesterday-delta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.01em;
    margin-bottom: 4px;
    min-height: 0;
    line-height: 1.4;
}

.yesterday-delta:empty {
    display: none;
}

.yesterday-delta .delta-arrow {
    font-weight: 700;
    margin-right: 2px;
}

.yesterday-delta.delta-up {
    color: var(--accent-rose);
}

.yesterday-delta.delta-down {
    color: var(--accent-emerald);
}

.yesterday-delta.delta-neutral {
    color: var(--text-muted);
}

.stat-card .projection-line {
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.70rem;
    color: var(--text-muted);
    line-height: 1.4;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
}

.stat-card .projection-line .proj-arrow {
    color: var(--text-muted);
    font-size: 0.65rem;
}

.stat-card .projection-line .proj-value {
    font-weight: 700;
    letter-spacing: -0.01em;
}

.stat-card .projection-line .proj-value.proj-low {
    color: var(--accent-emerald);
}

.stat-card .projection-line .proj-value.proj-mid {
    color: var(--accent-amber);
}

.stat-card .projection-line .proj-value.proj-high {
    color: var(--accent-rose);
}

.stat-card .projection-line .proj-sep {
    color: var(--border-light);
    font-weight: 300;
}

.stat-card .projection-line .proj-daily {
    color: var(--text-muted);
    font-weight: 500;
}

.stat-card .projection-line .proj-note {
    font-size: 0.60rem;
    color: var(--text-muted);
    opacity: 0.6;
    width: 100%;
}
```

## File: `css/components/table-rows.css`
```css
/* Day rows */
.day-row {
    cursor: pointer;
    transition: background 0.2s ease;
}

.day-row:hover {
    background: rgba(34, 211, 238, 0.03);
}

.day-row td:first-child {
    position: relative;
    padding-left: 36px;
    font-weight: 500;
    color: var(--text-primary);
}

.day-row .chevron {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-size: 0.6rem;
    color: var(--text-muted);
}

.day-row.expanded .chevron {
    transform: translateY(-50%) rotate(90deg);
    color: var(--accent-cyan);
}

.day-row.expanded {
    background: rgba(34, 211, 238, 0.04);
}

/* Weekly summary strip — full-width separator between week groups */
.week-row td {
    padding: 0 !important;
    border-bottom: none;
    background: rgba(30, 41, 59, 0.6);
    border-top: 1px solid rgba(96, 165, 250, 0.15);
    border-bottom: 1px solid rgba(96, 165, 250, 0.15);
}

.week-strip {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 16px;
}

.week-strip-left {
    display: flex;
    align-items: center;
    gap: 8px;
}

.week-strip-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    font-weight: 700;
    background: rgba(96, 165, 250, 0.12);
    color: var(--accent-blue);
    border-radius: 4px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.week-strip-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    color: var(--text-muted);
}

.week-strip-stats {
    display: flex;
    align-items: center;
    gap: 12px;
}

.week-stat {
    display: flex;
    align-items: center;
    gap: 5px;
}

.week-stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.58rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-muted);
    opacity: 0.7;
}

.week-stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--text-secondary);
}

.week-stat-divider {
    width: 1px;
    height: 14px;
    background: var(--border);
}

.week-strip-cost {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--accent-blue);
    padding: 2px 10px;
    background: rgba(96, 165, 250, 0.1);
    border-radius: var(--radius-pill);
    border: 1px solid rgba(96, 165, 250, 0.2);
}

/* Most expensive session row highlight */
.expensive-session-row {
    background: rgba(251, 113, 133, 0.06) !important;
    border-left: 3px solid var(--accent-rose);
}

.expensive-session-row td:first-child {
    padding-left: 9px; /* compensate for 3px border-left so alignment stays */
}

.expensive-session-row:hover {
    background: rgba(251, 113, 133, 0.10) !important;
}

.expensive-session-row td:last-child .cost-badge {
    box-shadow: 0 0 8px rgba(251, 113, 133, 0.3);
}
```

## File: `js/main.js`
```javascript
/**
 * main.js
 *
 * Main orchestrator for the Usage Tracker Dashboard.
 * Coordinates data loading and component initialization.
 */

// === Imports ===

// Config
import { sourceColors, defaultColors, modelColorMap } from './config/constants.js';
import { initChartDefaults } from './config/chart-config.js';

// Utils
import { formatNumber } from './utils/formatters.js';
import { getWeekStart, getWeekEnd, formatWeekLabel } from './utils/date-utils.js';
import { sourceClass } from './utils/class-utils.js';
import { getModelInfo } from './utils/model-utils.js';

// Components
import { initCounterAnimations } from './components/animations.js';

import { initCharts, clearDayFilter } from './components/charts.js';
import {
    initFilterDropdowns,
    applyFilters,
    updateFilterCount,
    setupFilterListeners
} from './components/filters.js';
import { initHeatmap } from './components/heatmap.js';
import { renderMonthlyProjection, updateYesterdayDelta } from './components/projections.js';
import {
    renderSessionTable,
    setMostExpensive,
    toggleDay,
    toggleAllDays,
    initKeyboardShortcuts
} from './components/sessions-table.js';
import {
    renderProjectsTable,
    toggleAllProjects
} from './components/projects-table.js';
import {
    exportData,
    importData,
    mergeSessions,
    recalcSummary
} from './components/data-transfer.js';

// === Global State ===

let allSessionsData = [];
let totalSessionCount = 0;
let currentSessionView = 'timeline';

// === Expose Functions to Window (for onclick handlers) ===

// toggleDay and filter removal functions are already exposed by their respective modules
// We just need to expose toggleAllDays and set up the filter callback
window.toggleAllDays = toggleAllDays;
window.toggleAllProjects = toggleAllProjects;
window.clearDayFilter = clearDayFilter;

function getCurrentRenderer() {
    return currentSessionView === 'projects' ? renderProjectsTable : renderSessionTable;
}

function applyCurrentFilters() {
    applyFilters(allSessionsData, totalSessionCount, getCurrentRenderer());
}

function toggleAllForCurrentView() {
    if (currentSessionView === 'projects') {
        toggleAllProjects();
    } else {
        toggleAllDays();
    }
}

function updateTableHeader(view) {
    const thead = document.getElementById('sessions-thead');
    if (!thead) return;
    const cells = thead.querySelectorAll('th');
    if (cells.length < 2) return;
    cells[0].textContent = view === 'projects' ? 'Project' : 'Date';
    cells[1].textContent = view === 'projects' ? 'Sources' : 'Sessions';
}

// === Main Data Loading Function ===

/**
 * Load data from window globals and initialize all dashboard components.
 * This is the main entry point after the page loads.
 */
async function loadData() {
    try {
        // Load data from window globals
        const summary = window.__SUMMARY__;
        const openclawSessions = window.__OPENCLAW_SESSIONS__ || window.__CLAWDBOT_SESSIONS__ || [];
        const claudeSessions = window.__CLAUDE_SESSIONS__ || [];

        // Check if data is available
        if (!summary) {
            document.getElementById('sessions-body').innerHTML =
                '<tr><td colspan="8" class="no-data">No data found. Run collect-usage.sh then reload.</td></tr>';
            return;
        }

        // === Static Text Values ===
        document.getElementById('today-date').textContent = summary.today;
        document.getElementById('month-name').textContent = new Date(summary.today + 'T00:00:00').toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        document.getElementById('last-updated').textContent = new Date(summary.generated_at).toLocaleString();

        // === Monthly Projection ===
        renderMonthlyProjection(summary);

        // === Prepare Animated Counter Elements ===
        // Store target values as data attributes, set initial display to zero
        const todayCostEl = document.getElementById('today-cost');
        todayCostEl.dataset.target = summary.today_cost;
        todayCostEl.dataset.prefix = '$';
        todayCostEl.dataset.decimals = '2';
        todayCostEl.textContent = '$0.00';

        const monthCostEl = document.getElementById('month-cost');
        monthCostEl.dataset.target = summary.month_cost;
        monthCostEl.dataset.prefix = '$';
        monthCostEl.dataset.decimals = '2';
        monthCostEl.textContent = '$0.00';

        const totalCostEl = document.getElementById('total-cost');
        totalCostEl.dataset.target = summary.totals.grand_total;
        totalCostEl.dataset.prefix = '$';
        totalCostEl.dataset.decimals = '2';
        totalCostEl.textContent = '$0.00';

        const sessionCountEl = document.getElementById('session-count');
        sessionCountEl.dataset.target = summary.session_counts.total;
        sessionCountEl.dataset.prefix = '';
        sessionCountEl.dataset.decimals = '0';
        sessionCountEl.textContent = '0';

        // === Combine All Sessions ===
        const allSessions = [...openclawSessions, ...claudeSessions];

        // === Calculate This Week Cost ===
        const thisWeekStart = getWeekStart(summary.today);
        const thisWeekEnd = getWeekEnd(thisWeekStart);
        const weekCost = allSessions
            .filter(s => s.date >= thisWeekStart && s.date <= thisWeekEnd)
            .reduce((sum, s) => sum + s.cost, 0);

        const weekCostEl = document.getElementById('week-cost');
        weekCostEl.dataset.target = weekCost;
        weekCostEl.dataset.prefix = '$';
        weekCostEl.dataset.decimals = '2';
        weekCostEl.textContent = '$0.00';
        document.getElementById('week-range').textContent = formatWeekLabel(thisWeekStart);

        // === Yesterday Delta ===
        updateYesterdayDelta(summary, allSessions);

        // === Find Most Expensive Session ===
        const todaySessions = allSessions.filter(s => s.date === summary.today);
        let mostExpensiveSession = null;
        let mostExpensiveFile = null;
        let mostExpensiveDate = null;

        if (todaySessions.length > 0) {
            mostExpensiveSession = todaySessions.reduce(
                (max, s) => s.cost > max.cost ? s : max,
                todaySessions[0]
            );
            mostExpensiveFile = mostExpensiveSession.file;
            mostExpensiveDate = mostExpensiveSession.date;
        }

        // Populate the expensive session callout banner
        const callout = document.getElementById('expensive-session-callout');
        if (mostExpensiveSession && mostExpensiveSession.cost > 0) {
            const ms = mostExpensiveSession;
            const sc = sourceClass(ms.source);
            const mi = getModelInfo(ms.model);

            document.getElementById('exp-source').innerHTML =
                `<span class="source-badge source-${sc}">${ms.source}</span>`;
            document.getElementById('exp-model').innerHTML =
                `<span class="model-badge ${mi.cls}">${mi.name}</span>`;
            document.getElementById('exp-time').textContent = ms.time || '---';
            document.getElementById('exp-cost').textContent = `$${ms.cost.toFixed(2)}`;
            document.getElementById('exp-tokens').innerHTML =
                `<span><span class="token-label">In:</span> <span class="token-value">${formatNumber(ms.input_tokens || 0)}</span></span>` +
                `<span><span class="token-label">Out:</span> <span class="token-value">${formatNumber(ms.output_tokens || 0)}</span></span>` +
                `<span><span class="token-label">Cache Read:</span> <span class="token-value">${formatNumber(ms.cache_read || 0)}</span></span>` +
                `<span><span class="token-label">Cache Write:</span> <span class="token-value">${formatNumber(ms.cache_write || 0)}</span></span>`;

            callout.style.display = 'flex';
        } else {
            callout.style.display = 'none';
        }

        // Pass most expensive session info to sessions-table module
        setMostExpensive(mostExpensiveFile, mostExpensiveDate);

        // === Store Global State ===
        allSessionsData = allSessions;
        totalSessionCount = allSessions.length;

        // === Initialize Filter Dropdowns ===
        initFilterDropdowns(allSessions);

        // === Render Session Table ===
        renderSessionTable(allSessions);
        updateFilterCount(allSessions.length, totalSessionCount);

        // === Initialize Chart.js Defaults ===
        initChartDefaults();

        // === Initialize Charts ===
        initCharts(allSessions);

        // === Initialize Heatmap ===
        initHeatmap(allSessions);

        // === Initialize Animated Counters ===
        initCounterAnimations();

        // === Setup Filter Listeners ===
        window._applyFiltersCallback = applyCurrentFilters;
        setupFilterListeners(applyCurrentFilters);

        // === Initialize Keyboard Shortcuts ===
        initKeyboardShortcuts(toggleAllForCurrentView);

        // === Setup Session View Toggle ===
        setupSessionViewToggle();

    } catch (error) {
        console.error('Error loading data:', error);
        document.getElementById('sessions-body').innerHTML =
            '<tr><td colspan="8" class="no-data">Error loading data. Run collect-usage.sh first.</td></tr>';
    }
}

// === Reload FAB Handler ===

function initReloadButton() {
    const fab = document.getElementById('reload-fab');
    if (!fab) return;

    fab.addEventListener('click', () => {
        fab.classList.add('is-reloading');
        // Fade out then trigger reload
        document.body.style.transition = 'opacity 0.25s ease-out';
        document.body.style.opacity = '0';
        setTimeout(() => {
            try {
                window.webkit.messageHandlers.reload.postMessage('');
            } catch (_) {
                location.reload();
            }
        }, 250);
    });
}

// === Export / Import Handlers ===

function initDataTransfer() {
    const exportBtn = document.getElementById('dt-export-btn');
    const importBtn = document.getElementById('dt-import-btn');
    if (!exportBtn || !importBtn) return;

    exportBtn.addEventListener('click', () => {
        const summary = window.__SUMMARY__;
        if (!summary || allSessionsData.length === 0) return;
        exportData(summary, allSessionsData);
    });

    importBtn.addEventListener('click', async () => {
        const result = await importData();
        if (!result) return;

        // Merge imported sessions with current data
        const merged = mergeSessions(allSessionsData, result.sessions);
        const newSummary = recalcSummary(merged);

        // Update global state
        allSessionsData = merged;
        totalSessionCount = merged.length;

        // Show import banner
        showImportBanner(result.sessions.length, merged.length);

        // Re-render with merged data
        reRenderDashboard(newSummary, merged);
    });
}

function showImportBanner(importedCount, totalCount) {
    // Remove existing banner
    const old = document.getElementById('dt-import-banner');
    if (old) old.remove();

    const banner = document.createElement('div');
    banner.id = 'dt-import-banner';
    banner.className = 'dt-import-banner';
    banner.innerHTML = `
        <span class="dt-import-banner-text">
            Viewing merged data — <strong>${totalCount}</strong> total sessions (imported ${importedCount})
        </span>
        <button class="dt-import-dismiss" onclick="location.reload()">Dismiss &amp; Reload</button>
    `;

    const container = document.querySelector('.container');
    const statsGrid = document.querySelector('.stats-grid');
    container.insertBefore(banner, statsGrid);
}

function reRenderDashboard(summary, sessions) {
    // Update stat card targets
    document.getElementById('today-cost').textContent = '$' + summary.today_cost.toFixed(2);
    document.getElementById('month-cost').textContent = '$' + summary.month_cost.toFixed(2);
    document.getElementById('total-cost').textContent = '$' + summary.totals.grand_total.toFixed(2);
    document.getElementById('session-count').textContent = sessions.length.toString();

    // Recalc week cost
    const thisWeekStart = getWeekStart(summary.today);
    const thisWeekEnd = getWeekEnd(thisWeekStart);
    const weekCost = sessions
        .filter(s => s.date >= thisWeekStart && s.date <= thisWeekEnd)
        .reduce((sum, s) => sum + s.cost, 0);
    document.getElementById('week-cost').textContent = '$' + weekCost.toFixed(2);

    // Re-render components
    initFilterDropdowns(sessions);
    getCurrentRenderer()(sessions);
    updateFilterCount(sessions.length, totalSessionCount);
    initCharts(sessions);
    initHeatmap(sessions);

    // Re-bind filter callback
    window._applyFiltersCallback = applyCurrentFilters;
    setupFilterListeners(applyCurrentFilters);
}

// === Session View Toggle ===

function setupSessionViewToggle() {
    const toggle = document.getElementById('sessions-view-toggle');
    if (!toggle) return;

    const buttons = toggle.querySelectorAll('.view-toggle-btn');
    const slider = toggle.querySelector('.view-toggle-slider');
    const toggleAllBtn = document.getElementById('toggle-all-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const view = btn.dataset.view;
            if (view === currentSessionView) return;

            // Update active button
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Slide the slider
            if (view === 'projects') {
                slider.style.transform = 'translateX(100%)';
            } else {
                slider.style.transform = 'translateX(0)';
            }

            // Update state
            currentSessionView = view;

            // Update table header
            updateTableHeader(view);

            // Update Expand All button onclick
            if (toggleAllBtn) {
                toggleAllBtn.onclick = view === 'projects' ? toggleAllProjects : toggleAllDays;
            }

            applyCurrentFilters();
        });
    });
}

// === Initialize on DOM Ready ===

function init() {
    loadData();
    initReloadButton();
    initDataTransfer();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
```

## File: `js/components/animations.js`
```javascript
/**
 * animations.js
 *
 * Smooth counter animations for stat cards with easing effects.
 * Uses IntersectionObserver to trigger animations when elements enter viewport.
 */

/**
 * Easing function: decelerate curve (ease-out cubic)
 *
 * @param {number} t - Progress value between 0 and 1
 * @returns {number} Eased progress value
 */
export function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
}

/**
 * Format a number with commas (e.g. 1234567.89 -> "1,234,567.89")
 *
 * @param {number} value - The numeric value to format
 * @param {number} decimals - Number of decimal places
 * @returns {string} Formatted number string with commas
 */
function formatWithCommas(value, decimals) {
    const parts = value.toFixed(decimals).split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
}

/**
 * Animate a single stat card value from 0 to targetValue.
 *
 * @param {HTMLElement} element - The DOM element whose textContent to update
 * @param {number} target - The final numeric value (e.g. 95.64 or 135)
 * @param {number} duration - Animation duration in ms (default 1500)
 * @param {string} prefix - String prepended to the displayed value (e.g. '$')
 * @param {number} decimals - Number of decimal places (0 for integers, 2 for dollars)
 */
export function animateCounter(element, target, duration = 1500, prefix = '', decimals = 0) {
    // If target is 0, just display it immediately -- nothing to animate
    if (target === 0) {
        element.textContent = prefix + formatWithCommas(0, decimals);
        return;
    }

    const startTime = performance.now();

    function tick(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easedProgress = easeOutCubic(progress);
        const currentValue = easedProgress * target;

        element.textContent = prefix + formatWithCommas(currentValue, decimals);

        if (progress < 1) {
            requestAnimationFrame(tick);
        } else {
            // Ensure the final value is exact (no floating-point drift)
            element.textContent = prefix + formatWithCommas(target, decimals);
        }
    }

    requestAnimationFrame(tick);
}

/**
 * Set up an IntersectionObserver on .stats-grid. When the grid enters the
 * viewport, trigger animateCounter for every stat card value element.
 *
 * Each .value element must have three data attributes set by loadData():
 *   data-target   : the numeric target value (e.g. "95.64")
 *   data-prefix   : the string prefix (e.g. "$" or "")
 *   data-decimals : number of decimal places (e.g. "2" or "0")
 */
export function initCounterAnimations() {
    const grid = document.querySelector('.stats-grid');
    if (!grid) return;

    const DURATION = 1500; // ms
    let hasAnimated = false;

    function runAnimations() {
        if (hasAnimated) return;
        hasAnimated = true;

        grid.querySelectorAll('.value[data-target]').forEach((el, index) => {
            const target = parseFloat(el.dataset.target) || 0;
            const prefix = el.dataset.prefix || '';
            const decimals = parseInt(el.dataset.decimals, 10) || 0;

            // Stagger each card by 80ms so they don't all start at the exact same moment.
            // This complements the existing CSS fadeSlideUp stagger (50ms, 100ms, 150ms, 200ms).
            setTimeout(() => {
                animateCounter(el, target, DURATION, prefix, decimals);
            }, index * 80);
        });
    }

    // Use IntersectionObserver if available (all modern browsers)
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    runAnimations();
                    observer.unobserve(grid);
                }
            });
        }, {
            threshold: 0.2  // trigger when 20% of the grid is visible
        });
        observer.observe(grid);
    } else {
        // Fallback for very old browsers: animate immediately
        runAnimations();
    }
}
```

## File: `js/components/charts.js`
```javascript
/**
 * charts.js
 *
 * Chart.js visualization components with compact sizing,
 * gradient fills, smooth animations, and center text plugin.
 */

import { getModelFamily } from '../utils/model-utils.js';

let dailyChart = null;
let sourceChart = null;
let modelChart = null;

// Day-filter state
let selectedDayIndex = null;
let allSessionsRef = [];
let chartDaysRef = [];

const modelColorMap = {
    'Opus': '#fb7185',
    'Sonnet': '#60a5fa',
    'Haiku': '#34d399',
    'Unknown': '#a78bfa',
};

const sourceColors = {
    'OpenClaw': '#fbbf24',
    'Clawdbot': '#fbbf24',
    'Claude Code': '#60a5fa',
    'Claude Desktop': '#a78bfa',
    'Cursor': '#22d3ee',
    'Windsurf': '#34d399',
    'Cline': '#fb7185',
    'Roo Code': '#f472b6',
    'Aider': '#2dd4bf',
    'Continue': '#f59e0b',
};

const defaultColors = ['#34d399', '#fb7185', '#a78bfa', '#f472b6', '#2dd4bf'];
let colorIdx = 0;

function getSourceColor(source) {
    if (sourceColors[source]) return sourceColors[source];
    if (!sourceColors[source]) {
        sourceColors[source] = defaultColors[colorIdx % defaultColors.length];
        colorIdx++;
    }
    return sourceColors[source];
}

function createBarGradient(ctx, color) {
    const gradient = ctx.createLinearGradient(0, 0, 0, ctx.canvas.height);
    gradient.addColorStop(0, color + 'E6');
    gradient.addColorStop(1, color + '66');
    return gradient;
}

/**
 * Center text plugin for doughnut charts.
 */
const centerTextPlugin = {
    id: 'centerText',
    afterDraw(chart) {
        if (chart.config.type !== 'doughnut') return;
        const centerText = chart.config.options?.plugins?.centerText;
        if (!centerText) return;

        const { ctx, chartArea: { top, bottom, left, right } } = chart;
        const centerX = (left + right) / 2;
        const centerY = (top + bottom) / 2;

        ctx.save();
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.font = "700 1.1rem 'Outfit', sans-serif";
        ctx.fillStyle = centerText.color || '#e2e8f0';
        ctx.fillText(centerText.text || '', centerX, centerY - 6);

        if (centerText.subText) {
            ctx.font = "500 0.5rem 'JetBrains Mono', monospace";
            ctx.fillStyle = '#94a3b8';
            ctx.fillText(centerText.subText, centerX, centerY + 10);
        }
        ctx.restore();
    }
};

Chart.register(centerTextPlugin);

/**
 * Compact tooltip config.
 */
const tooltipConfig = {
    backgroundColor: 'rgba(15, 23, 42, 0.92)',
    borderColor: 'rgba(34, 211, 238, 0.15)',
    borderWidth: 1,
    titleColor: '#e2e8f0',
    bodyColor: '#94a3b8',
    footerColor: '#e2e8f0',
    padding: { top: 8, bottom: 8, left: 10, right: 10 },
    cornerRadius: 8,
    titleFont: { family: "'Outfit', sans-serif", size: 11, weight: '600' },
    bodyFont: { family: "'JetBrains Mono', monospace", size: 10 },
    footerFont: { family: "'JetBrains Mono', monospace", size: 10, weight: '600' },
    boxPadding: 4,
    usePointStyle: true,
    caretSize: 5,
    caretPadding: 6,
};

/**
 * Compact legend config.
 */
const legendConfig = {
    labels: {
        padding: 12,
        usePointStyle: true,
        pointStyleWidth: 6,
        color: '#cbd5e1',
        font: {
            family: "'JetBrains Mono', monospace",
            size: 10,
            weight: '400'
        }
    }
};

export function initCharts(allSessions) {
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.borderColor = 'rgba(30, 41, 59, 0.4)';
    Chart.defaults.font.family = "'JetBrains Mono', monospace";
    Chart.defaults.font.size = 10;

    allSessionsRef = allSessions;

    buildDailyChart(allSessions);
    buildSourceChart(allSessions);
    buildModelChart(allSessions);
}

function buildDailyChart(allSessions) {
    const dailyBySource = {};
    const allSourcesSet = new Set();
    allSessions.forEach(s => {
        if (!dailyBySource[s.date]) dailyBySource[s.date] = {};
        dailyBySource[s.date][s.source] = (dailyBySource[s.date][s.source] || 0) + s.cost;
        allSourcesSet.add(s.source);
    });
    const chartDays = Object.keys(dailyBySource).sort().slice(-15);
    chartDaysRef = chartDays;
    const allSources = Array.from(allSourcesSet);

    const canvas = document.getElementById('dailyChart');
    const ctx = canvas.getContext('2d');
    canvas.style.cursor = 'pointer';

    const dailyDatasets = allSources.map(source => {
        const color = getSourceColor(source);
        return {
            label: source,
            data: chartDays.map(d => dailyBySource[d][source] || 0),
            backgroundColor: createBarGradient(ctx, color),
            hoverBackgroundColor: color,
            borderRadius: 3,
            borderSkipped: false,
            borderWidth: 0,
            barPercentage: 0.7,
            categoryPercentage: 0.8,
        };
    });

    if (dailyChart) dailyChart.destroy();
    dailyChart = new Chart(canvas, {
        type: 'bar',
        data: {
            labels: chartDays.map(d => {
                const dt = new Date(d + 'T00:00:00');
                return dt.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            }),
            datasets: dailyDatasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 400,
                easing: 'easeOutQuart',
                delay: (ctx) => ctx.dataIndex * 10 + ctx.datasetIndex * 20,
            },
            interaction: {
                mode: 'index',
                intersect: false,
            },
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                    align: 'end',
                    ...legendConfig,
                },
                tooltip: {
                    ...tooltipConfig,
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        title: (items) => items.length ? items[0].label : '',
                        label: (ctx) => {
                            if (ctx.raw === 0) return null;
                            return ` ${ctx.dataset.label}: $${ctx.raw.toFixed(2)}`;
                        },
                        footer: (items) => {
                            const total = items.reduce((sum, item) => sum + item.raw, 0);
                            return `  Total: $${total.toFixed(2)}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    stacked: true,
                    grid: { display: false },
                    ticks: {
                        color: '#94a3b8',
                        font: { size: 9 },
                        maxRotation: 0,
                    },
                    border: { display: false },
                },
                y: {
                    stacked: true,
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(30, 41, 59, 0.3)',
                        drawBorder: false,
                    },
                    ticks: {
                        callback: v => '$' + v.toFixed(0),
                        color: '#94a3b8',
                        font: { size: 9 },
                        padding: 6,
                    },
                    border: { display: false },
                }
            }
        }
    });

    canvas.addEventListener('click', e => {
        const elements = dailyChart.getElementsAtEventForMode(e, 'index', { intersect: false }, false);
        if (!elements.length) return;
        const idx = elements[0].index;
        selectedDayIndex = idx === selectedDayIndex ? null : idx;
        applyDaySelection();
    });
}

// ─── Day Filter Logic ────────────────────────────────────────

function applyDaySelection() {
    const isFiltered = selectedDayIndex !== null;

    // Update bar highlight — dim unselected bars
    dailyChart.data.datasets.forEach(dataset => {
        const color = getSourceColor(dataset.label);
        dataset.backgroundColor = chartDaysRef.map((_, i) =>
            !isFiltered || i === selectedDayIndex ? color + 'CC' : color + '22'
        );
        dataset.hoverBackgroundColor = chartDaysRef.map((_, i) =>
            !isFiltered || i === selectedDayIndex ? color : color + '44'
        );
    });
    dailyChart.update('none');

    const sessions = isFiltered
        ? allSessionsRef.filter(s => s.date === chartDaysRef[selectedDayIndex])
        : allSessionsRef;

    const dateLabel = isFiltered ? dailyChart.data.labels[selectedDayIndex] : null;

    updateDoughnutCharts(sessions);
    updateDayFilterBadge(dateLabel);
}

function updateDoughnutCharts(sessions) {
    // --- Source Chart ---
    const sourceTotals = {};
    sessions.forEach(s => {
        sourceTotals[s.source] = (sourceTotals[s.source] || 0) + s.cost;
    });
    const sourceEntries = Object.entries(sourceTotals).sort((a, b) => b[1] - a[1]);
    const sourceLabels = sourceEntries.map(([name]) => name);
    const sourceData = sourceEntries.map(([, cost]) => cost);
    const sourceBgColors = sourceLabels.map(s => getSourceColor(s));
    const totalCostSrc = sourceData.reduce((a, b) => a + b, 0);

    sourceChart.data.labels = sourceLabels;
    sourceChart.data.datasets[0].data = sourceData;
    sourceChart.data.datasets[0].backgroundColor = sourceBgColors.map(c => c + 'CC');
    sourceChart.data.datasets[0].hoverBackgroundColor = sourceBgColors;
    sourceChart.options.plugins.centerText.text = '$' + totalCostSrc.toFixed(2);
    sourceChart.update();

    // --- Model Chart ---
    const modelTotals = {};
    sessions.forEach(s => {
        const family = getModelFamily(s.model);
        modelTotals[family] = (modelTotals[family] || 0) + s.cost;
    });
    const modelEntries = Object.entries(modelTotals).sort((a, b) => b[1] - a[1]);
    const modelLabels = modelEntries.map(([name]) => name);
    const modelData = modelEntries.map(([, cost]) => cost);
    const mColors = modelLabels.map(name => modelColorMap[name] || '#a78bfa');
    const totalCostMdl = modelData.reduce((a, b) => a + b, 0);

    modelChart.data.labels = modelLabels;
    modelChart.data.datasets[0].data = modelData;
    modelChart.data.datasets[0].backgroundColor = mColors.map(c => c + 'CC');
    modelChart.data.datasets[0].hoverBackgroundColor = mColors;
    modelChart.options.plugins.centerText.text = '$' + totalCostMdl.toFixed(2);
    modelChart.update();
}

function updateDayFilterBadge(dateLabel) {
    const bar = document.getElementById('day-filter-bar');
    const dateEl = document.getElementById('day-filter-date');
    if (dateLabel) {
        dateEl.textContent = dateLabel;
        bar.style.display = 'flex';
    } else {
        bar.style.display = 'none';
    }
}

export function clearDayFilter() {
    selectedDayIndex = null;
    applyDaySelection();
}

function buildSourceChart(allSessions) {
    const sourceTotals = {};
    allSessions.forEach(s => {
        sourceTotals[s.source] = (sourceTotals[s.source] || 0) + s.cost;
    });

    const sourceEntries = Object.entries(sourceTotals).sort((a, b) => b[1] - a[1]);
    const sourceLabels = sourceEntries.map(([name]) => name);
    const sourceData = sourceEntries.map(([, cost]) => cost);
    const sourceBgColors = sourceLabels.map(s => getSourceColor(s));
    const totalCost = sourceData.reduce((a, b) => a + b, 0);

    if (sourceChart) sourceChart.destroy();
    sourceChart = new Chart(document.getElementById('sourceChart'), {
        type: 'doughnut',
        data: {
            labels: sourceLabels,
            datasets: [{
                data: sourceData,
                backgroundColor: sourceBgColors.map(c => c + 'CC'),
                hoverBackgroundColor: sourceBgColors,
                borderColor: 'rgba(10, 14, 23, 0.8)',
                borderWidth: 2,
                hoverOffset: 6,
                hoverBorderColor: 'rgba(255,255,255,0.1)',
                spacing: 2,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            animation: {
                animateRotate: true,
                animateScale: true,
                duration: 500,
                easing: 'easeOutQuart',
            },
            layout: {
                padding: { top: 0, bottom: 0, left: 0, right: 0 },
            },
            plugins: {
                centerText: {
                    text: '$' + totalCost.toFixed(2),
                    subText: 'TOTAL',
                    color: '#e2e8f0',
                },
                legend: {
                    position: 'right',
                    align: 'center',
                    ...legendConfig,
                    labels: {
                        ...legendConfig.labels,
                        padding: 8,
                        color: '#cbd5e1',
                        font: { family: "'JetBrains Mono', monospace", size: 9 },
                        generateLabels: function(chart) {
                            const data = chart.data;
                            const total = data.datasets[0].data.reduce((a, b) => a + b, 0);
                            return data.labels.map((label, i) => {
                                const value = data.datasets[0].data[i];
                                const pct = total > 0 ? (value / total * 100).toFixed(0) : '0';
                                return {
                                    text: `${label} ${pct}%`,
                                    fontColor: '#cbd5e1',
                                    fillStyle: data.datasets[0].hoverBackgroundColor[i],
                                    strokeStyle: 'transparent',
                                    lineWidth: 0,
                                    hidden: false,
                                    index: i,
                                    pointStyle: 'rectRounded',
                                };
                            });
                        }
                    }
                },
                tooltip: {
                    ...tooltipConfig,
                    callbacks: {
                        label: ctx => {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = total > 0 ? (ctx.raw / total * 100).toFixed(1) : '0.0';
                            return ` $${ctx.raw.toFixed(2)}  (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}

function buildModelChart(allSessions) {
    const modelTotals = {};
    allSessions.forEach(s => {
        const family = getModelFamily(s.model);
        modelTotals[family] = (modelTotals[family] || 0) + s.cost;
    });

    const modelEntries = Object.entries(modelTotals).sort((a, b) => b[1] - a[1]);
    const modelLabels = modelEntries.map(([name]) => name);
    const modelData = modelEntries.map(([, cost]) => cost);
    const modelColors = modelLabels.map(name => modelColorMap[name] || '#a78bfa');
    const totalCost = modelData.reduce((a, b) => a + b, 0);

    if (modelChart) modelChart.destroy();
    modelChart = new Chart(document.getElementById('modelChart'), {
        type: 'doughnut',
        data: {
            labels: modelLabels,
            datasets: [{
                data: modelData,
                backgroundColor: modelColors.map(c => c + 'CC'),
                hoverBackgroundColor: modelColors,
                borderColor: 'rgba(10, 14, 23, 0.8)',
                borderWidth: 2,
                hoverOffset: 6,
                hoverBorderColor: 'rgba(255,255,255,0.1)',
                spacing: 2,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            animation: {
                animateRotate: true,
                animateScale: true,
                duration: 500,
                easing: 'easeOutQuart',
                delay: 80,
            },
            layout: {
                padding: { top: 0, bottom: 0, left: 0, right: 0 },
            },
            plugins: {
                centerText: {
                    text: '$' + totalCost.toFixed(2),
                    subText: 'BY MODEL',
                    color: '#e2e8f0',
                },
                legend: {
                    position: 'right',
                    align: 'center',
                    ...legendConfig,
                    labels: {
                        ...legendConfig.labels,
                        padding: 8,
                        color: '#cbd5e1',
                        font: { family: "'JetBrains Mono', monospace", size: 9 },
                        generateLabels: function(chart) {
                            const data = chart.data;
                            const total = data.datasets[0].data.reduce((a, b) => a + b, 0);
                            return data.labels.map((label, i) => {
                                const value = data.datasets[0].data[i];
                                const pct = total > 0 ? (value / total * 100).toFixed(1) : '0.0';
                                return {
                                    text: `${label}  $${value.toFixed(2)}  (${pct}%)`,
                                    fontColor: '#cbd5e1',
                                    fillStyle: data.datasets[0].hoverBackgroundColor[i],
                                    strokeStyle: 'transparent',
                                    lineWidth: 0,
                                    hidden: false,
                                    index: i,
                                    pointStyle: 'rectRounded',
                                };
                            });
                        }
                    }
                },
                tooltip: {
                    ...tooltipConfig,
                    callbacks: {
                        label: function(ctx) {
                            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
                            const pct = total > 0 ? (ctx.raw / total * 100).toFixed(1) : '0.0';
                            return ` $${ctx.raw.toFixed(2)} (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}
```

## File: `js/components/data-transfer.js`
```javascript
/**
 * data-transfer.js
 *
 * Export and import session data as JSON for cross-device viewing.
 * Uses native WKWebView message handlers (NSSavePanel / NSOpenPanel).
 */

const EXPORT_VERSION = 1;

/**
 * Export all session data as a downloadable JSON file.
 * Sends data to native Swift handler which shows NSSavePanel.
 *
 * @param {Object} summary - The __SUMMARY__ object
 * @param {Array} sessions - All session objects
 */
export function exportData(summary, sessions) {
    const payload = {
        _format: 'claude-usage-tracker',
        _version: EXPORT_VERSION,
        exported_at: new Date().toISOString(),
        summary,
        sessions,
    };

    const json = JSON.stringify(payload, null, 2);

    try {
        window.webkit.messageHandlers.exportData.postMessage(json);
    } catch {
        // Fallback for browser testing
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const dateStr = new Date().toISOString().slice(0, 10);
        const a = document.createElement('a');
        a.href = url;
        a.download = `claude-usage-${dateStr}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast('Exported ' + sessions.length + ' sessions');
    }
}

/**
 * Prompt user to pick a JSON file and import its session data.
 * Uses native NSOpenPanel via Swift message handler.
 * Returns a promise that resolves to the parsed payload, or null on cancel/error.
 *
 * @returns {Promise<{summary: Object, sessions: Array}|null>}
 */
export function importData() {
    return new Promise((resolve) => {
        // Store the resolver on window so Swift can call back
        window._importDataResolver = (jsonString) => {
            delete window._importDataResolver;
            if (!jsonString) return resolve(null);

            try {
                const data = JSON.parse(jsonString);
                if (data._format !== 'claude-usage-tracker' || !Array.isArray(data.sessions)) {
                    showToast('Invalid file format', true);
                    return resolve(null);
                }
                showToast('Imported ' + data.sessions.length + ' sessions');
                resolve(data);
            } catch {
                showToast('Failed to parse file', true);
                resolve(null);
            }
        };

        try {
            window.webkit.messageHandlers.importData.postMessage('');
        } catch {
            // Fallback for browser testing
            delete window._importDataResolver;
            const input = document.createElement('input');
            input.type = 'file';
            input.accept = '.json';
            input.addEventListener('change', () => {
                const file = input.files[0];
                if (!file) return resolve(null);
                const reader = new FileReader();
                reader.onload = () => {
                    try {
                        const data = JSON.parse(reader.result);
                        if (data._format !== 'claude-usage-tracker' || !Array.isArray(data.sessions)) {
                            showToast('Invalid file format', true);
                            return resolve(null);
                        }
                        showToast('Imported ' + data.sessions.length + ' sessions');
                        resolve(data);
                    } catch {
                        showToast('Failed to parse file', true);
                        resolve(null);
                    }
                };
                reader.readAsText(file);
            });
            input.addEventListener('cancel', () => resolve(null));
            input.click();
        }
    });
}

/**
 * Merge imported sessions with existing sessions, deduplicating by sessionId+date.
 *
 * @param {Array} existing - Current session array
 * @param {Array} incoming - Imported session array
 * @returns {Array} Merged and sorted sessions
 */
export function mergeSessions(existing, incoming) {
    const seen = new Set();
    const merged = [];

    for (const s of existing) {
        const key = (s.sessionId || s.file || '') + '|' + s.date;
        seen.add(key);
        merged.push(s);
    }

    for (const s of incoming) {
        const key = (s.sessionId || s.file || '') + '|' + s.date;
        if (!seen.has(key)) {
            seen.add(key);
            merged.push(s);
        }
    }

    // Sort newest first
    merged.sort((a, b) => {
        if (a.date !== b.date) return b.date.localeCompare(a.date);
        return (b.time || '').localeCompare(a.time || '');
    });

    return merged;
}

/**
 * Recalculate summary totals from a session array.
 *
 * @param {Array} sessions - All sessions
 * @returns {Object} Updated summary
 */
export function recalcSummary(sessions) {
    const today = new Date().toISOString().slice(0, 10);
    const currentMonth = today.slice(0, 7);

    const totals = {};
    let grandTotal = 0;
    const sourceCounts = {};
    let todayCost = 0;
    let monthCost = 0;

    for (const s of sessions) {
        const src = s.source || 'Unknown';
        totals[src] = (totals[src] || 0) + s.cost;
        grandTotal += s.cost;
        sourceCounts[src] = (sourceCounts[src] || 0) + 1;

        if (s.date === today) todayCost += s.cost;
        if (s.date && s.date.startsWith(currentMonth)) monthCost += s.cost;
    }

    totals.grand_total = grandTotal;
    sourceCounts.total = sessions.length;

    return {
        generated_at: new Date().toISOString(),
        today,
        current_month: currentMonth,
        totals,
        today_cost: todayCost,
        month_cost: monthCost,
        session_counts: sourceCounts,
    };
}

// ── Toast notification (also called from Swift via window._showExportToast) ──

let toastTimer = null;

export function showToast(message, isError = false) {
    let toast = document.getElementById('data-transfer-toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'data-transfer-toast';
        toast.className = 'dt-toast';
        document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.classList.toggle('dt-toast-error', isError);
    toast.classList.remove('dt-toast-visible');

    // force reflow
    void toast.offsetWidth;
    toast.classList.add('dt-toast-visible');

    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
        toast.classList.remove('dt-toast-visible');
    }, 2500);
}

// Expose toast to Swift callbacks
window._showExportToast = (msg, isErr) => showToast(msg, isErr);
```

## File: `js/components/filters.js`
```javascript
/**
 * filters.js
 *
 * Session filtering system with multi-criteria support:
 * - Source filtering (checkboxes)
 * - Model filtering (checkboxes)
 * - Date range filtering
 * - Minimum cost filtering
 * - Filter chips for active filters
 */

import { getModelInfo } from '../utils/model-utils.js';
import { sourceClass } from '../utils/class-utils.js';

/**
 * Initialize filter dropdowns with data from sessions.
 * Populates source and model checkboxes, sets date input ranges.
 *
 * @param {Array} sessions - Array of all session objects
 */
export function initFilterDropdowns(sessions) {
    // Collect unique sources
    const sources = [...new Set(sessions.map(s => s.source))].sort();
    const sourceDropdown = document.getElementById('source-dropdown');
    sourceDropdown.innerHTML = sources.map(source => {
        const sc = sourceClass(source);
        return `<label>
            <input type="checkbox" value="${source}" data-filter="source" />
            <span class="source-badge source-${sc}">${source}</span>
        </label>`;
    }).join('');

    // Collect unique models (use display name, store raw value)
    const modelMap = {};
    sessions.forEach(s => {
        if (s.model) {
            const mi = getModelInfo(s.model);
            if (!modelMap[s.model]) {
                modelMap[s.model] = mi;
            }
        }
    });
    // Sort by family then name
    const modelEntries = Object.entries(modelMap).sort((a, b) => {
        const order = { 'model-opus': 0, 'model-sonnet': 1, 'model-haiku': 2 };
        const aOrder = order[a[1].cls] ?? 3;
        const bOrder = order[b[1].cls] ?? 3;
        if (aOrder !== bOrder) return aOrder - bOrder;
        return a[1].name.localeCompare(b[1].name);
    });

    const modelDropdown = document.getElementById('model-dropdown');
    modelDropdown.innerHTML = modelEntries.map(([rawModel, mi]) => {
        return `<label>
            <input type="checkbox" value="${rawModel}" data-filter="model" />
            <span class="model-badge ${mi.cls}">${mi.name}</span>
        </label>`;
    }).join('');

    // Set date input min/max from data
    if (sessions.length > 0) {
        const dates = sessions.map(s => s.date).sort();
        const minDate = dates[0];
        const maxDate = dates[dates.length - 1];
        document.getElementById('filter-date-from').min = minDate;
        document.getElementById('filter-date-from').max = maxDate;
        document.getElementById('filter-date-to').min = minDate;
        document.getElementById('filter-date-to').max = maxDate;
    }
}

/**
 * Get currently active filter values from the UI.
 *
 * @returns {Object} Filter object with sources, models, dateFrom, dateTo, minCost
 */
export function getActiveFilters() {
    const filters = {
        sources: [],
        models: [],
        dateFrom: null,
        dateTo: null,
        minCost: null,
    };

    // Collect checked sources
    document.querySelectorAll('#source-dropdown input[type="checkbox"]:checked').forEach(cb => {
        filters.sources.push(cb.value);
    });

    // Collect checked models
    document.querySelectorAll('#model-dropdown input[type="checkbox"]:checked').forEach(cb => {
        filters.models.push(cb.value);
    });

    // Date range
    const dateFrom = document.getElementById('filter-date-from').value;
    const dateTo = document.getElementById('filter-date-to').value;
    if (dateFrom) filters.dateFrom = dateFrom;
    if (dateTo) filters.dateTo = dateTo;

    // Min cost
    const minCostVal = document.getElementById('filter-min-cost').value;
    if (minCostVal !== '' && !isNaN(parseFloat(minCostVal))) {
        filters.minCost = parseFloat(minCostVal);
    }

    return filters;
}

/**
 * Filter sessions based on active filter criteria.
 *
 * @param {Array} sessions - Array of all session objects
 * @param {Object} filters - Filter object from getActiveFilters()
 * @returns {Array} Filtered array of session objects
 */
export function filterSessions(sessions, filters) {
    return sessions.filter(s => {
        // Source filter (OR within)
        if (filters.sources.length > 0 && !filters.sources.includes(s.source)) {
            return false;
        }

        // Model filter (OR within)
        if (filters.models.length > 0 && !filters.models.includes(s.model)) {
            return false;
        }

        // Date from (inclusive)
        if (filters.dateFrom && s.date < filters.dateFrom) {
            return false;
        }

        // Date to (inclusive)
        if (filters.dateTo && s.date > filters.dateTo) {
            return false;
        }

        // Min cost
        if (filters.minCost !== null && s.cost < filters.minCost) {
            return false;
        }

        return true;
    });
}

/**
 * Apply filters and re-render the table.
 * Updates filter button states, clear button visibility, and filter chips.
 *
 * @param {Array} allSessionsData - Global array of all sessions
 * @param {number} totalSessionCount - Total number of sessions
 * @param {Function} renderCallback - Callback to re-render table with filtered data
 */
export function applyFilters(allSessionsData, totalSessionCount, renderCallback) {
    const filters = getActiveFilters();
    const hasAnyFilter = filters.sources.length > 0
        || filters.models.length > 0
        || filters.dateFrom !== null
        || filters.dateTo !== null
        || filters.minCost !== null;
    const filtered = hasAnyFilter ? filterSessions(allSessionsData, filters) : allSessionsData;

    // Re-render the table with filtered sessions
    renderCallback(filtered);

    // Update session count
    updateFilterCount(filtered.length, totalSessionCount);

    // Update filter button active states
    const sourceBtn = document.getElementById('source-filter-btn');
    sourceBtn.classList.toggle('active', filters.sources.length > 0);

    const modelBtn = document.getElementById('model-filter-btn');
    modelBtn.classList.toggle('active', filters.models.length > 0);

    document.getElementById('filter-clear-btn').classList.toggle('visible', hasAnyFilter);

    // Render chips
    renderFilterChips(filters);
}

/**
 * Update the filter count display showing filtered vs total sessions.
 *
 * @param {number} shown - Number of sessions after filtering
 * @param {number} total - Total number of sessions
 */
export function updateFilterCount(shown, total) {
    const el = document.getElementById('filter-count');
    if (shown === total) {
        el.innerHTML = `<span class="count-highlight">${total}</span> sessions`;
    } else {
        el.innerHTML = `<span class="count-highlight">${shown}</span> of ${total} sessions`;
    }
}

/**
 * Render filter chips showing active filters with remove buttons.
 *
 * @param {Object} filters - Filter object from getActiveFilters()
 */
export function renderFilterChips(filters) {
    const container = document.getElementById('filter-chips');
    let html = '';

    filters.sources.forEach(source => {
        html += `<span class="filter-chip chip-source">
            Source: ${source}
            <span class="chip-remove" onclick="removeSourceFilter('${source.replace(/'/g, "\\'")}')">&times;</span>
        </span>`;
    });

    filters.models.forEach(model => {
        const mi = getModelInfo(model);
        html += `<span class="filter-chip chip-model">
            Model: ${mi.name}
            <span class="chip-remove" onclick="removeModelFilter('${model.replace(/'/g, "\\'")}')">&times;</span>
        </span>`;
    });

    if (filters.dateFrom) {
        html += `<span class="filter-chip chip-date">
            From: ${filters.dateFrom}
            <span class="chip-remove" onclick="removeDateFromFilter()">&times;</span>
        </span>`;
    }

    if (filters.dateTo) {
        html += `<span class="filter-chip chip-date">
            To: ${filters.dateTo}
            <span class="chip-remove" onclick="removeDateToFilter()">&times;</span>
        </span>`;
    }

    if (filters.minCost !== null) {
        html += `<span class="filter-chip chip-cost">
            Min: $${filters.minCost.toFixed(2)}
            <span class="chip-remove" onclick="removeMinCostFilter()">&times;</span>
        </span>`;
    }

    container.innerHTML = html;
}

/**
 * Remove a specific source filter.
 *
 * @param {string} source - Source name to remove from filter
 */
export function removeSourceFilter(source) {
    const cb = document.querySelector(`#source-dropdown input[value="${source}"]`);
    if (cb) cb.checked = false;
    // applyFilters will be called by the caller
}

/**
 * Remove a specific model filter.
 *
 * @param {string} model - Model identifier to remove from filter
 */
export function removeModelFilter(model) {
    const cb = document.querySelector(`#model-dropdown input[value="${model}"]`);
    if (cb) cb.checked = false;
    // applyFilters will be called by the caller
}

/**
 * Remove the date-from filter.
 */
export function removeDateFromFilter() {
    document.getElementById('filter-date-from').value = '';
    // applyFilters will be called by the caller
}

/**
 * Remove the date-to filter.
 */
export function removeDateToFilter() {
    document.getElementById('filter-date-to').value = '';
    // applyFilters will be called by the caller
}

/**
 * Remove the minimum cost filter.
 */
export function removeMinCostFilter() {
    document.getElementById('filter-min-cost').value = '';
    // applyFilters will be called by the caller
}

/**
 * Clear all active filters and reset UI.
 */
export function clearAllFilters() {
    // Uncheck all source checkboxes
    document.querySelectorAll('#source-dropdown input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
    });

    // Uncheck all model checkboxes
    document.querySelectorAll('#model-dropdown input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
    });

    // Clear date inputs
    document.getElementById('filter-date-from').value = '';
    document.getElementById('filter-date-to').value = '';

    // Clear min cost
    document.getElementById('filter-min-cost').value = '';

    // Close any open dropdowns
    closeAllDropdowns();

    // applyFilters will be called by the caller
}

/**
 * Setup event listeners for all filter controls.
 *
 * @param {Function} applyFiltersCallback - Callback to apply filters when changed
 */
export function setupFilterListeners(applyFiltersCallback) {
    // Dropdown toggle for Source
    const sourceBtn = document.getElementById('source-filter-btn');
    const sourceDropdown = document.getElementById('source-dropdown');
    sourceBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = sourceDropdown.classList.contains('open');
        closeAllDropdowns();
        if (!isOpen) {
            sourceDropdown.classList.add('open');
            sourceBtn.classList.add('open');
        }
    });

    // Dropdown toggle for Model
    const modelBtn = document.getElementById('model-filter-btn');
    const modelDropdown = document.getElementById('model-dropdown');
    modelBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = modelDropdown.classList.contains('open');
        closeAllDropdowns();
        if (!isOpen) {
            modelDropdown.classList.add('open');
            modelBtn.classList.add('open');
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.filter-group')) {
            closeAllDropdowns();
        }
    });

    // Prevent dropdown close when clicking inside dropdown
    sourceDropdown.addEventListener('click', (e) => e.stopPropagation());
    modelDropdown.addEventListener('click', (e) => e.stopPropagation());

    // Checkbox change listeners (delegated)
    sourceDropdown.addEventListener('change', () => applyFiltersCallback());
    modelDropdown.addEventListener('change', () => applyFiltersCallback());

    // Date input listeners
    document.getElementById('filter-date-from').addEventListener('change', () => applyFiltersCallback());
    document.getElementById('filter-date-to').addEventListener('change', () => applyFiltersCallback());

    // Min cost listener (debounced for typing)
    let costTimeout;
    document.getElementById('filter-min-cost').addEventListener('input', () => {
        clearTimeout(costTimeout);
        costTimeout = setTimeout(() => applyFiltersCallback(), 300);
    });

    // Clear all button
    document.getElementById('filter-clear-btn').addEventListener('click', () => {
        clearAllFilters();
        applyFiltersCallback();
    });
}

/**
 * Close all open filter dropdowns.
 */
export function closeAllDropdowns() {
    document.querySelectorAll('.filter-dropdown').forEach(d => d.classList.remove('open'));
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('open'));
}

// Make filter removal functions available globally for onclick handlers
window.removeSourceFilter = function(source) {
    removeSourceFilter(source);
    // Trigger applyFilters from global context
    if (window._applyFiltersCallback) {
        window._applyFiltersCallback();
    }
};

window.removeModelFilter = function(model) {
    removeModelFilter(model);
    if (window._applyFiltersCallback) {
        window._applyFiltersCallback();
    }
};

window.removeDateFromFilter = function() {
    removeDateFromFilter();
    if (window._applyFiltersCallback) {
        window._applyFiltersCallback();
    }
};

window.removeDateToFilter = function() {
    removeDateToFilter();
    if (window._applyFiltersCallback) {
        window._applyFiltersCallback();
    }
};

window.removeMinCostFilter = function() {
    removeMinCostFilter();
    if (window._applyFiltersCallback) {
        window._applyFiltersCallback();
    }
};
```

## File: `js/components/heatmap.js`
```javascript
/**
 * heatmap.js
 *
 * Peak activity heatmap with two switchable views:
 *   - Hours: actual dates × 24 hour columns (only dates with data)
 *   - Days:  GitHub-style calendar grid (actual dates, last ~16 weeks)
 *
 * Features: segmented toggle, staggered cell animations, smooth view
 * transitions, polished tooltips, and click-to-scroll on cells.
 */

import { toggleDay } from './sessions-table.js';

const DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
const DAY_NAMES_FULL = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
const MONTH_NAMES = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

let currentView = 'hours';
let cachedSessions = [];

/**
 * Determine heatmap intensity level based on cost.
 */
function heatmapLevel(cost, maxCost) {
    if (cost === 0 || maxCost === 0) return 0;
    const ratio = cost / maxCost;
    if (ratio <= 0.2) return 1;
    if (ratio <= 0.4) return 2;
    if (ratio <= 0.65) return 3;
    return 4;
}

// ─── Hours View ─────────────────────────────────────────────

function renderHoursView(allSessions) {
    // Group sessions by date → hour
    const byDate = {};
    allSessions.forEach(s => {
        if (!s.time || !s.date) return;
        const hour = parseInt(s.time.split(':')[0], 10);
        if (isNaN(hour) || hour < 0 || hour > 23) return;
        if (!byDate[s.date]) byDate[s.date] = Array.from({ length: 24 }, () => ({ cost: 0, count: 0 }));
        byDate[s.date][hour].cost += s.cost;
        byDate[s.date][hour].count += 1;
    });

    // Only dates with data, last 30 days, sorted newest first
    const cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - 29);
    const cutoffStr = formatDateStr(cutoff);
    const dates = Object.keys(byDate).filter(d => d >= cutoffStr).sort().reverse();
    const numRows = dates.length;
    if (numRows === 0) return;

    // Find max cost across all cells for scaling
    let maxCost = 0;
    for (const date of dates) {
        for (const cell of byDate[date]) {
            if (cell.cost > maxCost) maxCost = cell.cost;
        }
    }

    // Unified grid: 1 date-label column + 24 hour columns
    // Row 0 = hour labels, rows 1..N = date rows
    const gridEl = document.getElementById('heatmap-hours-grid');
    gridEl.style.gridTemplateRows = `18px repeat(${numRows}, 22px)`;

    let html = '';

    // Row 0: corner cell + 24 hour labels
    html += '<div class="heatmap-corner"></div>';
    for (let i = 0; i < 24; i++) {
        const label = i % 3 === 0 ? i.toString() : '';
        html += `<div class="heatmap-hour-label">${label}</div>`;
    }

    // Date rows
    for (let r = 0; r < numRows; r++) {
        const date = dates[r];
        const dateObj = new Date(date + 'T00:00:00');
        const label = dateObj.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });

        html += `<div class="heatmap-day-label" title="${date}">${label}</div>`;

        for (let hour = 0; hour < 24; hour++) {
            const cell = byDate[date][hour];
            const level = heatmapLevel(cell.cost, maxCost);
            html += `<div class="heatmap-cell level-${level}"
                data-date="${date}" data-hour="${hour}"
                data-cost="${cell.cost.toFixed(2)}" data-count="${cell.count}"></div>`;
        }
    }

    gridEl.innerHTML = html;
    setupHoursTooltip(gridEl);
    setupHoursClick(gridEl);
}

// ─── Days View ──────────────────────────────────────────────

function renderDaysView(allSessions) {
    // Aggregate sessions by date
    const byDate = {};
    allSessions.forEach(s => {
        if (!s.date) return;
        if (!byDate[s.date]) byDate[s.date] = { cost: 0, count: 0, sources: {} };
        byDate[s.date].cost += s.cost;
        byDate[s.date].count += 1;
        const src = s.source || 'Unknown';
        byDate[s.date].sources[src] = (byDate[s.date].sources[src] || 0) + 1;
    });

    // Calculate date range: go back ~16 weeks from today
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    // Find the Monday of 15 weeks ago
    const startDate = new Date(today);
    const todayDow = startDate.getDay();
    const daysToMonday = todayDow === 0 ? 6 : todayDow - 1;
    startDate.setDate(startDate.getDate() - daysToMonday - (15 * 7));

    // Build list of all dates from startDate to today
    const allDates = [];
    const cursor = new Date(startDate);
    while (cursor <= today) {
        allDates.push(formatDateStr(cursor));
        cursor.setDate(cursor.getDate() + 1);
    }

    // Find max cost for scaling
    let maxCost = 0;
    for (const d of allDates) {
        if (byDate[d] && byDate[d].cost > maxCost) maxCost = byDate[d].cost;
    }

    // Organize into weeks (columns) and days (rows, Mon=0 .. Sun=6)
    const weeks = [];
    let currentWeek = [];
    for (let i = 0; i < allDates.length; i++) {
        const dateStr = allDates[i];
        const dateObj = new Date(dateStr + 'T00:00:00');
        const dow = dateObj.getDay();
        const dayIdx = dow === 0 ? 6 : dow - 1; // Mon=0..Sun=6

        // Start a new week on Monday
        if (dayIdx === 0 && currentWeek.length > 0) {
            weeks.push(currentWeek);
            currentWeek = [];
        }

        currentWeek.push({
            date: dateStr,
            dayIdx,
            data: byDate[dateStr] || { cost: 0, count: 0, sources: {} }
        });
    }
    if (currentWeek.length > 0) weeks.push(currentWeek);

    const numWeeks = weeks.length;

    // Render day-of-week labels (Sun at top, Mon at bottom)
    const dayLabelsEl = document.getElementById('heatmap-days-day-labels');
    const reversedDays = [...DAY_NAMES].reverse(); // Sun, Sat, Fri, Thu, Wed, Tue, Mon
    dayLabelsEl.innerHTML = reversedDays.map((d, i) => {
        const show = i % 2 === 0; // Show Sun, Fri, Wed, Mon
        return `<div class="heatmap-days-day-label">${show ? d : ''}</div>`;
    }).join('');

    // Render month labels (newest first, track last seen month)
    const monthLabelsEl = document.getElementById('heatmap-days-month-labels');
    let monthLabelsHTML = '';
    let lastMonth = -1;
    for (let w = 0; w < numWeeks; w++) {
        const firstDay = weeks[w][0];
        const dateObj = new Date(firstDay.date + 'T00:00:00');
        const month = dateObj.getMonth();
        if (month !== lastMonth) {
            monthLabelsHTML += `<div class="heatmap-days-month-label" style="grid-column: ${w + 1}">${MONTH_NAMES[month]}</div>`;
            lastMonth = month;
        }
    }
    monthLabelsEl.innerHTML = monthLabelsHTML;
    monthLabelsEl.style.gridTemplateColumns = `repeat(${numWeeks}, 1fr)`;

    // Render grid cells
    const gridEl = document.getElementById('heatmap-days-grid');
    gridEl.style.gridTemplateColumns = `repeat(${numWeeks}, 1fr)`;

    // Build a 7-row × numWeeks-col grid
    // CSS grid-auto-flow: column fills top-to-bottom per column,
    // so we iterate week-by-week (column-by-column), Mon-Sun within each
    let cellsHTML = '';
    for (let w = 0; w < numWeeks; w++) {
        for (let dayRow = 6; dayRow >= 0; dayRow--) {
            const entry = weeks[w].find(e => e.dayIdx === dayRow);
            if (entry) {
                const level = heatmapLevel(entry.data.cost, maxCost);
                const isToday = entry.date === formatDateStr(today);
                cellsHTML += `<div class="heatmap-cell heatmap-days-cell${isToday ? ' is-today' : ''} level-${level}"
                    data-date="${entry.date}"
                    data-cost="${entry.data.cost.toFixed(2)}"
                    data-count="${entry.data.count}"></div>`;
            } else {
                cellsHTML += `<div class="heatmap-cell heatmap-days-cell level-0 is-empty"></div>`;
            }
        }
    }
    gridEl.innerHTML = cellsHTML;

    // Attach sources data as element property (avoids JSON.parse in hot path)
    let cellIdx = 0;
    const allCells = gridEl.querySelectorAll('.heatmap-days-cell:not(.is-empty)');
    for (let w = 0; w < numWeeks; w++) {
        for (let dayRow = 6; dayRow >= 0; dayRow--) {
            const entry = weeks[w].find(e => e.dayIdx === dayRow);
            if (entry) {
                const cell = allCells[cellIdx++];
                if (cell) cell._sources = entry.data.sources;
            }
        }
    }

    setupDaysTooltip(gridEl);
    setupDaysClick(gridEl);
}

/**
 * Format a Date object to YYYY-MM-DD string.
 */
function formatDateStr(d) {
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const dd = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${dd}`;
}

// ─── Tooltips ───────────────────────────────────────────────

function setupHoursTooltip(gridEl) {
    const tooltip = document.getElementById('heatmap-tooltip');
    const tipDay = tooltip.querySelector('.tip-day');
    const tipHour = tooltip.querySelector('.tip-hour');
    const tipCount = tooltip.querySelector('.tip-count');
    const tipCost = tooltip.querySelector('.tip-cost');

    gridEl.addEventListener('mouseover', e => {
        const cell = e.target.closest('.heatmap-cell');
        if (!cell || !cell.dataset.date) return;

        const dateStr = cell.dataset.date;
        const hour = parseInt(cell.dataset.hour, 10);
        const cost = cell.dataset.cost;
        const count = cell.dataset.count;

        const dateObj = new Date(dateStr + 'T00:00:00');
        const dayName = DAY_NAMES_FULL[dateObj.getDay() === 0 ? 6 : dateObj.getDay() - 1];
        const formatted = dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

        const hourEnd = (hour + 1) % 24;
        const hourStr = hour.toString().padStart(2, '0') + ':00';
        const hourEndStr = hourEnd.toString().padStart(2, '0') + ':00';

        tipDay.textContent = `${dayName}, ${formatted}`;
        tipHour.textContent = `${hourStr} \u2014 ${hourEndStr}`;
        tipCount.textContent = count;
        tipCost.textContent = '$' + cost;
        resetTooltipCache();
        tooltip.classList.add('visible');
    });

    gridEl.addEventListener('mousemove', e => {
        positionTooltip(tooltip, e);
    });

    gridEl.addEventListener('mouseleave', () => {
        tooltip.classList.remove('visible');
    });
}

function setupDaysTooltip(gridEl) {
    const tooltip = document.getElementById('heatmap-tooltip');
    const tipDay = tooltip.querySelector('.tip-day');
    const tipHour = tooltip.querySelector('.tip-hour');
    const tipCount = tooltip.querySelector('.tip-count');
    const tipCost = tooltip.querySelector('.tip-cost');

    gridEl.addEventListener('mouseover', e => {
        const cell = e.target.closest('.heatmap-days-cell');
        if (!cell || cell.classList.contains('is-empty')) return;
        const dateStr = cell.dataset.date;
        if (!dateStr) return;

        const dateObj = new Date(dateStr + 'T00:00:00');
        const dayName = DAY_NAMES_FULL[dateObj.getDay() === 0 ? 6 : dateObj.getDay() - 1];
        const formatted = dateObj.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

        const count = parseInt(cell.dataset.count, 10);
        const cost = cell.dataset.cost;

        // Build sources summary from element property
        let sourcesText = '';
        const sources = cell._sources;
        if (sources) {
            const entries = Object.entries(sources).sort((a, b) => b[1] - a[1]);
            if (entries.length > 0) {
                sourcesText = entries.map(([src, cnt]) => `${src}: ${cnt}`).join(', ');
            }
        }

        tipDay.textContent = `${dayName}, ${formatted}`;
        tipHour.textContent = count > 0
            ? (sourcesText || `${count} session${count !== 1 ? 's' : ''}`)
            : 'No activity';
        tipCount.textContent = count;
        tipCost.textContent = '$' + cost;
        resetTooltipCache();
        tooltip.classList.add('visible');
    });

    gridEl.addEventListener('mousemove', e => {
        positionTooltip(tooltip, e);
    });

    gridEl.addEventListener('mouseleave', () => {
        tooltip.classList.remove('visible');
    });
}

let _tooltipW = 0, _tooltipH = 0;
function positionTooltip(tooltip, e) {
    // Cache dimensions — only re-read when likely stale (zero)
    if (!_tooltipW) {
        _tooltipW = tooltip.offsetWidth || 180;
        _tooltipH = tooltip.offsetHeight || 100;
    }
    const x = e.clientX + 14;
    const y = e.clientY - 12;
    const maxX = window.innerWidth - _tooltipW - 12;
    const maxY = window.innerHeight - _tooltipH - 12;
    tooltip.style.left = Math.min(x, maxX) + 'px';
    tooltip.style.top = Math.min(y, maxY) + 'px';
}

// Reset cached tooltip size when content changes
function resetTooltipCache() { _tooltipW = 0; _tooltipH = 0; }

// ─── Click to Scroll ────────────────────────────────────────

function scrollToSessionDay(cell) {
    const dateStr = cell.dataset.date;
    if (!dateStr) return;

    const count = parseInt(cell.dataset.count, 10);
    if (count === 0) return;

    // Add a brief pulse animation to the clicked cell
    cell.classList.add('clicked');
    setTimeout(() => cell.classList.remove('clicked'), 400);

    // Find the day row in the session log
    const dayRow = document.getElementById('day-' + dateStr);
    if (!dayRow) return;

    // Scroll to the row with smooth animation
    dayRow.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // Expand the day after scroll settles
    setTimeout(() => {
        if (!dayRow.classList.contains('expanded')) {
            toggleDay(dateStr);
        }
        // Briefly highlight the row
        dayRow.classList.add('heatmap-scroll-highlight');
        setTimeout(() => dayRow.classList.remove('heatmap-scroll-highlight'), 1500);
    }, 400);
}

function setupHoursClick(gridEl) {
    gridEl.addEventListener('click', e => {
        const cell = e.target.closest('.heatmap-cell');
        if (!cell || !cell.dataset.date) return;
        scrollToSessionDay(cell);
    });
}

function setupDaysClick(gridEl) {
    gridEl.addEventListener('click', e => {
        const cell = e.target.closest('.heatmap-days-cell');
        if (!cell || cell.classList.contains('is-empty')) return;
        scrollToSessionDay(cell);
    });
}

// ─── Toggle Logic ───────────────────────────────────────────

function setupToggle() {
    const toggle = document.getElementById('heatmap-toggle');
    const hoursBtn = document.getElementById('toggle-hours-btn');
    const daysBtn = document.getElementById('toggle-days-btn');
    const slider = document.getElementById('heatmap-toggle-slider');
    const hoursView = document.getElementById('heatmap-hours-view');
    const daysView = document.getElementById('heatmap-days-view');
    const title = document.getElementById('heatmap-title');

    function switchView(view) {
        if (view === currentView) return;
        currentView = view;

        // Update button states
        hoursBtn.classList.toggle('active', view === 'hours');
        daysBtn.classList.toggle('active', view === 'days');

        // Animate slider
        if (view === 'days') {
            slider.style.transform = 'translateX(100%)';
        } else {
            slider.style.transform = 'translateX(0)';
        }

        // Update title
        title.textContent = view === 'hours' ? 'Peak Hours' : 'Peak Days';

        // Animate view transition
        const outgoing = view === 'hours' ? daysView : hoursView;
        const incoming = view === 'hours' ? hoursView : daysView;

        outgoing.classList.add('heatmap-view-exiting');
        outgoing.classList.remove('heatmap-view-active');

        setTimeout(() => {
            outgoing.classList.remove('heatmap-view-exiting');
            incoming.classList.add('heatmap-view-active');
        }, 200);
    }

    hoursBtn.addEventListener('click', () => switchView('hours'));
    daysBtn.addEventListener('click', () => switchView('days'));
}

// ─── Public API ─────────────────────────────────────────────

/**
 * Initialize and render both heatmap views with session data.
 */
export function initHeatmap(allSessions) {
    cachedSessions = allSessions;
    renderHoursView(allSessions);
    renderDaysView(allSessions);
    setupToggle();
}
```

## File: `js/components/projections.js`
```javascript
/**
 * projections.js
 *
 * Monthly cost projection calculations and rendering.
 * Includes yesterday delta comparison for daily spend analysis.
 */

/**
 * Determine color class for monthly projection based on projected amount.
 *
 * @param {number} monthlyAmount - Projected monthly cost in dollars
 * @returns {string} CSS class name ('proj-low', 'proj-mid', or 'proj-high')
 */
export function projectionColorClass(monthlyAmount) {
    if (monthlyAmount < 50) return 'proj-low';
    if (monthlyAmount <= 200) return 'proj-mid';
    return 'proj-high';
}

/**
 * Render the monthly projection based on current month-to-date spending.
 *
 * Calculates daily average and projects to end of month.
 * Shows confidence note for early-month projections (first 3 days).
 *
 * @param {Object} summary - Summary object containing today, month_cost, etc.
 */
export function renderMonthlyProjection(summary) {
    const el = document.getElementById('month-projection');
    if (!el) return;

    const today = new Date(summary.today + 'T00:00:00');
    const year = today.getFullYear();
    const month = today.getMonth();
    const dayOfMonth = today.getDate();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    // No data yet
    if (summary.month_cost === 0) {
        el.style.display = 'none';
        return;
    }

    const dailyAvg = summary.month_cost / dayOfMonth;
    const projection = dailyAvg * daysInMonth;
    const colorCls = projectionColorClass(projection);

    // Format projection: use ~$ for estimates, round to nearest dollar if >= $10
    let projStr;
    if (projection >= 10) {
        projStr = '~$' + Math.round(projection);
    } else {
        projStr = '~$' + projection.toFixed(2);
    }

    // Format daily average
    let dailyStr = '$' + dailyAvg.toFixed(2) + '/day';

    // Build the HTML
    let html = '';
    html += '<span class="proj-arrow">\u2192</span>';
    html += '<span class="proj-value ' + colorCls + '">' + projStr + '/mo</span>';
    html += '<span class="proj-sep">|</span>';
    html += '<span class="proj-daily">' + dailyStr + '</span>';

    // Confidence note for early-month projections
    if (dayOfMonth <= 3) {
        html += '<span class="proj-note">based on ' + dayOfMonth + ' day' + (dayOfMonth > 1 ? 's' : '') + ' of ' + daysInMonth + '</span>';
    }

    el.innerHTML = html;
    el.style.display = 'flex';
}

/**
 * IIFE: Update yesterday delta comparison for today's cost card.
 *
 * Compares today's cost to yesterday's cost and displays:
 * - Up arrow (↑) with red/rose color if spending more
 * - Down arrow (↓) with green/emerald color if spending less
 * - Neutral indicator if same or no data
 *
 * Shows percentage change if >= 1%.
 *
 * This is an IIFE that should be called within loadData() context.
 *
 * @param {Object} summary - Summary object with today and today_cost
 * @param {Array} allSessions - Array of all session objects
 */
export function updateYesterdayDelta(summary, allSessions) {
    const deltaEl = document.getElementById('yesterday-delta');
    if (!deltaEl) return;

    const todayCost = summary.today_cost;

    // Calculate yesterday's date string
    const todayDate = new Date(summary.today + 'T00:00:00');
    const yesterdayDate = new Date(todayDate);
    yesterdayDate.setDate(yesterdayDate.getDate() - 1);
    const yy = yesterdayDate.getFullYear();
    const ym = String(yesterdayDate.getMonth() + 1).padStart(2, '0');
    const yd = String(yesterdayDate.getDate()).padStart(2, '0');
    const yesterdayStr = `${yy}-${ym}-${yd}`;

    // Find yesterday's sessions and cost
    const yesterdaySessions = allSessions.filter(s => s.date === yesterdayStr);
    const hasYesterdayData = yesterdaySessions.length > 0;
    const yesterdayCost = yesterdaySessions.reduce((sum, s) => sum + s.cost, 0);

    // No data for yesterday at all
    if (!hasYesterdayData) {
        // Check if there is ANY prior data
        const hasPriorData = allSessions.some(s => s.date < summary.today);
        if (!hasPriorData) {
            deltaEl.textContent = '';
            deltaEl.className = 'yesterday-delta';
            return;
        }
        deltaEl.innerHTML = '<span class="delta-arrow">--</span> no data yesterday';
        deltaEl.className = 'yesterday-delta delta-neutral';
        return;
    }

    // Both days have data -- compute delta
    const diff = todayCost - yesterdayCost;
    const absDiff = Math.abs(diff);

    // Same cost (within 1 cent tolerance)
    if (absDiff < 0.01) {
        deltaEl.innerHTML = '<span class="delta-arrow">--</span> same as yesterday';
        deltaEl.className = 'yesterday-delta delta-neutral';
        return;
    }

    // Percentage change
    let pctStr = '';
    if (yesterdayCost > 0) {
        const pct = (absDiff / yesterdayCost) * 100;
        if (pct >= 1) {
            pctStr = ` (${pct.toFixed(0)}%)`;
        }
    }

    if (diff > 0) {
        // Spending MORE than yesterday -- rose/red, up arrow
        deltaEl.innerHTML =
            `<span class="delta-arrow">\u2191</span> $${absDiff.toFixed(2)}${pctStr} vs yesterday`;
        deltaEl.className = 'yesterday-delta delta-up';
    } else {
        // Spending LESS than yesterday -- emerald/green, down arrow
        deltaEl.innerHTML =
            `<span class="delta-arrow">\u2193</span> $${absDiff.toFixed(2)}${pctStr} vs yesterday`;
        deltaEl.className = 'yesterday-delta delta-down';
    }
}
```

## File: `js/components/projects-table.js`
```javascript
/**
 * projects-table.js
 *
 * Projects view for the session log. Groups sessions by working directory (cwd),
 * with expandable project detail sub-tables rendered lazily on first expand.
 */

import { formatNumber } from '../utils/formatters.js';
import { getModelInfo } from '../utils/model-utils.js';
import { costClass, sourceClass } from '../utils/class-utils.js';
import { updateTotalsRow, updateToggleAllButton, resetSessionStore, pushToSessionStore } from './sessions-table.js';

const _builtProjects = new Set();
let _projectsData = [];

export function extractProjectName(cwd) {
    if (!cwd) return '(No Project)';
    const cleaned = cwd.replace(/\/+$/, '');
    const parts = cleaned.split('/');
    return parts[parts.length - 1] || cwd;
}

export function groupByProject(sessions) {
    const map = {};
    for (const s of sessions) {
        const key = s.cwd || '';
        if (!map[key]) map[key] = [];
        map[key].push(s);
    }

    const projects = [];
    for (const [cwd, items] of Object.entries(map)) {
        projects.push({
            cwd,
            name: extractProjectName(cwd || null),
            sessions: items,
            totalCost: items.reduce((sum, s) => sum + s.cost, 0),
        });
    }

    projects.sort((a, b) => {
        if (!a.cwd && b.cwd) return 1;
        if (a.cwd && !b.cwd) return -1;
        return b.totalCost - a.totalCost;
    });

    return projects;
}

export function renderProjectsTable(sessions) {
    resetSessionStore();
    _builtProjects.clear();

    const projects = groupByProject(sessions);
    const tbody = document.getElementById('sessions-body');

    if (projects.length === 0) {
        tbody.innerHTML = '<tr><td colspan="8" class="no-data">No sessions match the current filters.</td></tr>';
        updateTotalsRow([]);
        return;
    }

    let html = '';
    projects.forEach((project, idx) => {
        let totalInput = 0, totalOutput = 0, totalCacheRead = 0, totalCacheWrite = 0;
        const sourceSet = new Set();
        const modelSet = new Set();
        for (const s of project.sessions) {
            totalInput += s.input_tokens || 0;
            totalOutput += s.output_tokens || 0;
            totalCacheRead += s.cache_read || 0;
            totalCacheWrite += s.cache_write || 0;
            sourceSet.add(s.source);
            if (s.model) modelSet.add(s.model);
        }
        const sources = [...sourceSet];
        const models = [...modelSet];

        const sourceBadges = sources.map(src => {
            const sc = sourceClass(src);
            return `<span class="source-badge source-${sc}">${src}</span>`;
        }).join(' ');

        const modelBadges = models.map(m => {
            const mi = getModelInfo(m);
            return `<span class="model-badge ${mi.cls}">${mi.name}</span>`;
        }).join(' ');

        const displayName = project.name;
        const fullPath = project.cwd || '(no working directory)';

        html += `<tr class="project-row" id="project-${idx}" onclick="toggleProject(${idx})">
            <td>
                <span class="chevron">\u25B6</span>
                <span class="project-icon">\uD83D\uDCC1</span>
                <span class="project-name" title="${fullPath.replace(/"/g, '&quot;')}">${displayName.replace(/</g, '&lt;')}</span>
                <span class="project-meta">${project.sessions.length} session${project.sessions.length !== 1 ? 's' : ''}</span>
            </td>
            <td>${sourceBadges}</td>
            <td>${modelBadges}</td>
            <td class="token-cell">${formatNumber(totalInput)}</td>
            <td class="token-cell">${formatNumber(totalOutput)}</td>
            <td class="token-cell">${formatNumber(totalCacheRead)}</td>
            <td class="token-cell">${formatNumber(totalCacheWrite)}</td>
            <td style="text-align:right"><span class="cost-badge ${costClass(project.totalCost)}">$${project.totalCost.toFixed(2)}</span></td>
        </tr>`;

        html += `<tr class="project-detail-row"><td colspan="8">
            <div class="project-detail-wrapper" id="project-detail-wrapper-${idx}"></div>
        </td></tr>`;
    });

    tbody.innerHTML = html;

    _projectsData = projects;

    updateTotalsRow(sessions);
    updateToggleAllButton(false);
}

function buildProjectDetail(project) {
    const sorted = [...project.sessions].sort((a, b) => {
        const dateCmp = (b.date || '').localeCompare(a.date || '');
        if (dateCmp !== 0) return dateCmp;
        return (b.time || '').localeCompare(a.time || '');
    });

    let subTableHTML = `
        <table class="session-subtable">
            <thead><tr>
                <th>Date</th><th>Time</th><th>Title</th><th>Source</th><th>Model</th>
                <th>Input</th><th>Output</th><th>Cache R</th><th>Cache W</th><th style="text-align:right">Cost</th>
            </tr></thead><tbody>`;

    for (const s of sorted) {
        const mi = getModelInfo(s.model);
        const sc = sourceClass(s.source);
        const titleText = s.title ? s.title.replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;') : '\u2014';
        const sessionIdx = pushToSessionStore(s);
        const dateLabel = s.date ? new Date(s.date + 'T00:00:00').toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) : '\u2014';

        subTableHTML += `<tr class="session-clickable" onclick="showSessionDetail(${sessionIdx})">
            <td style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;">${dateLabel}</td>
            <td style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;">${s.time || '\u2014'}</td>
            <td class="session-title-cell" title="${titleText}">${titleText}</td>
            <td><span class="source-badge source-${sc}">${s.source}</span></td>
            <td><span class="model-badge ${mi.cls}">${mi.name}</span></td>
            <td class="token-cell">${formatNumber(s.input_tokens || 0)}</td>
            <td class="token-cell">${formatNumber(s.output_tokens || 0)}</td>
            <td class="token-cell">${formatNumber(s.cache_read || 0)}</td>
            <td class="token-cell">${formatNumber(s.cache_write || 0)}</td>
            <td style="text-align:right"><span class="cost-badge ${costClass(s.cost)}">$${s.cost.toFixed(2)}</span></td>
        </tr>`;
    }

    subTableHTML += '</tbody></table>';
    return `<div class="project-detail">${subTableHTML}</div>`;
}

export function toggleProject(idx) {
    const row = document.getElementById('project-' + idx);
    const wrapper = document.getElementById('project-detail-wrapper-' + idx);
    if (!row || !wrapper) return;

    if (row.classList.contains('expanded')) {
        row.classList.remove('expanded');
        wrapper.classList.remove('open');
    } else {
        if (!_builtProjects.has(idx) && _projectsData[idx]) {
            wrapper.innerHTML = buildProjectDetail(_projectsData[idx]);
            _builtProjects.add(idx);
        }
        row.classList.add('expanded');
        wrapper.classList.add('open');
    }

    const anyExpanded = document.querySelectorAll('.project-row.expanded').length > 0;
    updateToggleAllButton(anyExpanded);
}

export function toggleAllProjects() {
    const projectRows = document.querySelectorAll('.project-row');
    if (projectRows.length === 0) return;

    const anyExpanded = document.querySelectorAll('.project-row.expanded').length > 0;
    const shouldExpand = !anyExpanded;

    projectRows.forEach((row, index) => {
        const idx = parseInt(row.id.replace('project-', ''), 10);
        const wrapper = document.getElementById('project-detail-wrapper-' + idx);
        if (!wrapper) return;

        setTimeout(() => {
            if (shouldExpand && !row.classList.contains('expanded')) {
                if (!_builtProjects.has(idx) && _projectsData[idx]) {
                    wrapper.innerHTML = buildProjectDetail(_projectsData[idx]);
                    _builtProjects.add(idx);
                }
                row.classList.add('expanded');
                wrapper.classList.add('open');
            } else if (!shouldExpand && row.classList.contains('expanded')) {
                row.classList.remove('expanded');
                wrapper.classList.remove('open');
            }
        }, index * 10);
    });

    updateToggleAllButton(shouldExpand);
}

// Expose to window for onclick handlers
window.toggleProject = toggleProject;
```

## File: `js/components/sessions-table.js`
```javascript
/**
 * sessions-table.js
 *
 * Session table rendering with day/week grouping, expandable details,
 * and keyboard shortcuts for toggling.
 */

import { formatNumber } from '../utils/formatters.js';
import { getWeekStart, getWeekEnd, formatWeekLabel } from '../utils/date-utils.js';
import { getModelInfo } from '../utils/model-utils.js';
import { costClass, sourceClass } from '../utils/class-utils.js';

// Global reference to most expensive session (set by main.js)
let mostExpensiveFile = null;
let mostExpensiveDate = null;

let _sessionDetailStore = [];
const _builtDays = new Set();
let _daySessionsMap = {};

export function resetSessionStore() {
    _sessionDetailStore = [];
}

export function pushToSessionStore(session) {
    _sessionDetailStore.push(session);
    return _sessionDetailStore.length - 1;
}

/**
 * Set the most expensive session reference (called from main.js)
 *
 * @param {string} file - File path of most expensive session
 * @param {string} date - Date of most expensive session
 */
export function setMostExpensive(file, date) {
    mostExpensiveFile = file;
    mostExpensiveDate = date;
}

/**
 * Toggle expansion state of a single day row.
 *
 * @param {string} date - The date string (YYYY-MM-DD) to toggle
 */
export function toggleDay(date) {
    const row = document.getElementById('day-' + date);
    const detailWrapper = document.getElementById('detail-wrapper-' + date);

    if (row.classList.contains('expanded')) {
        row.classList.remove('expanded');
        detailWrapper.classList.remove('open');
    } else {
        if (!_builtDays.has(date) && _daySessionsMap[date]) {
            detailWrapper.innerHTML = buildDayDetail(date, _daySessionsMap[date]);
            _builtDays.add(date);
        }

        row.classList.add('expanded');
        detailWrapper.classList.add('open');

        setTimeout(() => {
            detailWrapper.querySelectorAll('.cost-bar-fill').forEach(bar => {
                bar.style.transform = `scaleX(${parseFloat(bar.dataset.width) / 100})`;
            });
        }, 50);
    }

    // Keep the toggle-all button label in sync
    const anyExpanded = document.querySelectorAll('.day-row.expanded').length > 0;
    updateToggleAllButton(anyExpanded);
}

/**
 * Toggle all day rows between expanded and collapsed states.
 * Includes staggered animation for visual effect.
 */
export function toggleAllDays() {
    const dayRows = document.querySelectorAll('.day-row');
    if (dayRows.length === 0) return;

    const anyExpanded = document.querySelectorAll('.day-row.expanded').length > 0;
    const shouldExpand = !anyExpanded;

    dayRows.forEach((row, index) => {
        const date = row.id.replace('day-', '');
        const detailWrapper = document.getElementById('detail-wrapper-' + date);
        if (!detailWrapper) return;

        setTimeout(() => {
            if (shouldExpand && !row.classList.contains('expanded')) {
                if (!_builtDays.has(date) && _daySessionsMap[date]) {
                    detailWrapper.innerHTML = buildDayDetail(date, _daySessionsMap[date]);
                    _builtDays.add(date);
                }

                row.classList.add('expanded');
                detailWrapper.classList.add('open');

                setTimeout(() => {
                    detailWrapper.querySelectorAll('.cost-bar-fill').forEach(bar => {
                        bar.style.transform = `scaleX(${parseFloat(bar.dataset.width) / 100})`;
                    });
                }, 50);
            } else if (!shouldExpand && row.classList.contains('expanded')) {
                row.classList.remove('expanded');
                detailWrapper.classList.remove('open');
            }
        }, index * 10);
    });

    updateToggleAllButton(shouldExpand);
}

/**
 * Update the "Expand All" / "Collapse All" button label and state.
 *
 * @param {boolean} anyExpanded - Whether any rows are currently expanded
 */
export function updateToggleAllButton(anyExpanded) {
    const btn = document.getElementById('toggle-all-btn');
    if (!btn) return;

    if (anyExpanded) {
        btn.innerHTML = 'Collapse All<span class="arrow">&#9660;</span><span class="kbd-hint">Shift+E</span>';
        btn.classList.add('is-expanded');
    } else {
        btn.innerHTML = 'Expand All<span class="arrow">&#9660;</span><span class="kbd-hint">Shift+E</span>';
        btn.classList.remove('is-expanded');
    }
}

/**
 * Update the totals row in the table footer.
 *
 * @param {Array} sessions - Array of session objects to total
 */
export function updateTotalsRow(sessions) {
    const tfoot = document.getElementById('sessions-tfoot');
    if (!tfoot) return;

    if (!sessions || sessions.length === 0) {
        tfoot.innerHTML = '';
        return;
    }

    const totalSessions = sessions.length;
    let totalInput = 0, totalOutput = 0, totalCacheRead = 0, totalCacheWrite = 0, totalCost = 0;
    for (const s of sessions) {
        totalInput += s.input_tokens || 0;
        totalOutput += s.output_tokens || 0;
        totalCacheRead += s.cache_read || 0;
        totalCacheWrite += s.cache_write || 0;
        totalCost += s.cost;
    }

    tfoot.innerHTML = `<tr>
        <td>TOTAL</td>
        <td><span class="totals-session-count">${totalSessions}</span></td>
        <td><span class="totals-models-placeholder">--</span></td>
        <td class="token-cell">${formatNumber(totalInput)}</td>
        <td class="token-cell">${formatNumber(totalOutput)}</td>
        <td class="token-cell">${formatNumber(totalCacheRead)}</td>
        <td class="token-cell">${formatNumber(totalCacheWrite)}</td>
        <td style="text-align:right"><span class="cost-badge ${costClass(totalCost)}">$${totalCost.toFixed(2)}</span></td>
    </tr>`;
}

/**
 * Build the expandable detail panel HTML for a single day.
 *
 * Includes:
 * - Source breakdown cards with cost bars
 * - Detailed session sub-table
 *
 * @param {string} date - The date string (YYYY-MM-DD)
 * @param {Array} sessions - Array of session objects for this day
 * @returns {string} HTML string for the detail panel
 */
export function buildDayDetail(date, sessions) {
    const bySource = {};
    sessions.forEach(s => {
        if (!bySource[s.source]) bySource[s.source] = [];
        bySource[s.source].push(s);
    });

    const totalCost = sessions.reduce((sum, s) => sum + s.cost, 0);
    const maxSourceCost = Math.max(...Object.values(bySource).map(arr => arr.reduce((s, x) => s + x.cost, 0)));

    let sourceCardsHTML = '';
    for (const [source, items] of Object.entries(bySource)) {
        const sCost = items.reduce((s, x) => s + x.cost, 0);
        const sInput = items.reduce((s, x) => s + (x.input_tokens || 0), 0);
        const sOutput = items.reduce((s, x) => s + (x.output_tokens || 0), 0);
        const sCacheRead = items.reduce((s, x) => s + (x.cache_read || 0), 0);
        const sCacheWrite = items.reduce((s, x) => s + (x.cache_write || 0), 0);
        const models = [...new Set(items.map(x => x.model).filter(Boolean))];
        const sc = sourceClass(source);
        const barPct = maxSourceCost > 0 ? (sCost / maxSourceCost * 100).toFixed(1) : 0;

        sourceCardsHTML += `
            <div class="source-card border-${sc}">
                <div class="source-card-header">
                    <span class="source-name">
                        <span class="source-badge source-${sc}">${source}</span>
                        <span style="margin-left:6px;font-size:0.7rem;color:var(--text-muted);">${items.length} session${items.length > 1 ? 's' : ''}</span>
                    </span>
                    <span class="source-cost ${costClass(sCost) + '-text'}">${'$' + sCost.toFixed(2)}</span>
                </div>
                <div class="source-stats">
                    <div class="source-stat"><span class="stat-label">Input</span><span class="stat-value">${formatNumber(sInput)}</span></div>
                    <div class="source-stat"><span class="stat-label">Output</span><span class="stat-value">${formatNumber(sOutput)}</span></div>
                    <div class="source-stat"><span class="stat-label">Cache Read</span><span class="stat-value">${formatNumber(sCacheRead)}</span></div>
                    <div class="source-stat"><span class="stat-label">Cache Write</span><span class="stat-value">${formatNumber(sCacheWrite)}</span></div>
                    <div class="source-stat"><span class="stat-label">Models</span><span class="stat-value">${models.map(m => getModelInfo(m).name).join(', ') || '—'}</span></div>
                    <div class="source-stat"><span class="stat-label">% of Day</span><span class="stat-value">${totalCost > 0 ? (sCost / totalCost * 100).toFixed(1) : 0}%</span></div>
                </div>
                <div class="cost-bar-container">
                    <div class="cost-bar-bg">
                        <div class="cost-bar-fill fill-${sc}" data-width="${barPct}%"></div>
                    </div>
                </div>
            </div>`;
    }

    let subTableHTML = `
        <table class="session-subtable">
            <thead><tr>
                <th>Time</th><th>Title</th><th>Source</th><th>Model</th>
                <th>Input</th><th>Output</th><th>Cache R</th><th>Cache W</th><th style="text-align:right">Cost</th>
            </tr></thead><tbody>`;
    sessions.sort((a, b) => (b.time || '').localeCompare(a.time || ''));
    for (const s of sessions) {
        const mi = getModelInfo(s.model);
        const sc = sourceClass(s.source);
        const isExpensive = (s.file === mostExpensiveFile && date === mostExpensiveDate);
        const titleText = s.title ? s.title.replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;') : '—';
        const sessionIdx = pushToSessionStore(s);
        subTableHTML += `<tr class="session-clickable${isExpensive ? ' expensive-session-row' : ''}" onclick="showSessionDetail(${sessionIdx})">
            <td style="font-family:'JetBrains Mono',monospace;font-size:0.72rem;">${s.time || '—'}</td>
            <td class="session-title-cell" title="${titleText}">${titleText}</td>
            <td><span class="source-badge source-${sc}">${s.source}</span></td>
            <td><span class="model-badge ${mi.cls}">${mi.name}</span></td>
            <td class="token-cell">${formatNumber(s.input_tokens || 0)}</td>
            <td class="token-cell">${formatNumber(s.output_tokens || 0)}</td>
            <td class="token-cell">${formatNumber(s.cache_read || 0)}</td>
            <td class="token-cell">${formatNumber(s.cache_write || 0)}</td>
            <td style="text-align:right"><span class="cost-badge ${costClass(s.cost)}">$${s.cost.toFixed(2)}</span></td>
        </tr>`;
    }
    subTableHTML += '</tbody></table>';

    return `
        <div class="day-detail">
            <div class="source-breakdown">${sourceCardsHTML}</div>
            ${subTableHTML}
        </div>`;
}

/**
 * Render the sessions table with day and week groupings.
 *
 * Groups sessions by date, then by ISO week (Monday-Sunday).
 * Each week shows individual day rows followed by a week summary row.
 *
 * @param {Array} sessions - Array of session objects to render
 */
export function renderSessionTable(sessions) {
    resetSessionStore();
    _builtDays.clear();

    const byDate = {};
    sessions.forEach(s => {
        if (!byDate[s.date]) byDate[s.date] = [];
        byDate[s.date].push(s);
    });
    _daySessionsMap = byDate;

    const sortedDates = Object.keys(byDate).sort().reverse();

    const tbody = document.getElementById('sessions-body');
    if (sortedDates.length === 0) {
        tbody.innerHTML = '<tr><td colspan="8" class="no-data">No sessions match the current filters.</td></tr>';
        updateTotalsRow([]);
        return;
    }

    // Group dates into ISO weeks
    const weekGroups = {}; // weekStart -> [dates]
    for (const date of sortedDates) {
        const ws = getWeekStart(date);
        if (!weekGroups[ws]) weekGroups[ws] = [];
        weekGroups[ws].push(date);
    }

    // Sort week start dates in reverse order (newest first)
    const sortedWeeks = Object.keys(weekGroups).sort().reverse();

    let html = '';
    for (const weekStart of sortedWeeks) {
        const weekDates = weekGroups[weekStart];

        // Accumulators for weekly totals
        let weekTotalCost = 0;
        let weekTotalInput = 0;
        let weekTotalOutput = 0;
        let weekTotalCacheRead = 0;
        let weekTotalCacheWrite = 0;
        let weekTotalSessions = 0;
        const weekModels = new Set();

        // Emit day rows for this week
        for (const date of weekDates) {
            const daySessions = byDate[date];
            let dayCost = 0, dayInput = 0, dayOutput = 0, dayCacheRead = 0, dayCacheWrite = 0;
            const modelSet = new Set();
            for (const x of daySessions) {
                dayCost += x.cost;
                dayInput += x.input_tokens || 0;
                dayOutput += x.output_tokens || 0;
                dayCacheRead += x.cache_read || 0;
                dayCacheWrite += x.cache_write || 0;
                if (x.model) modelSet.add(x.model);
            }
            const models = [...modelSet];
            const modelBadges = models.map(m => {
                const mi = getModelInfo(m);
                return `<span class="model-badge ${mi.cls}">${mi.name}</span>`;
            }).join(' ');

            // Accumulate into weekly totals
            weekTotalCost += dayCost;
            weekTotalInput += dayInput;
            weekTotalOutput += dayOutput;
            weekTotalCacheRead += dayCacheRead;
            weekTotalCacheWrite += dayCacheWrite;
            weekTotalSessions += daySessions.length;
            models.forEach(m => weekModels.add(m));

            const dateLabel = new Date(date + 'T00:00:00').toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });

            html += `<tr class="day-row" id="day-${date}" onclick="toggleDay('${date}')">
                <td><span class="chevron">\u25B6</span>${dateLabel}</td>
                <td>${daySessions.length}</td>
                <td>${modelBadges}</td>
                <td class="token-cell">${formatNumber(dayInput)}</td>
                <td class="token-cell">${formatNumber(dayOutput)}</td>
                <td class="token-cell">${formatNumber(dayCacheRead)}</td>
                <td class="token-cell">${formatNumber(dayCacheWrite)}</td>
                <td style="text-align:right"><span class="cost-badge ${costClass(dayCost)}">$${dayCost.toFixed(2)}</span></td>
            </tr>`;

            html += `<tr class="day-detail-row"><td colspan="8">
                <div class="day-detail-wrapper" id="detail-wrapper-${date}"></div>
            </td></tr>`;
        }

        // Emit weekly summary row after all days in this week
        const weekLabel = formatWeekLabel(weekStart);
        html += `<tr class="week-row">
            <td colspan="8">
                <div class="week-strip">
                    <div class="week-strip-left">
                        <span class="week-strip-icon">\u03A3</span>
                        <span class="week-strip-label">${weekLabel}</span>
                    </div>
                    <div class="week-strip-stats">
                        <span class="week-stat"><span class="week-stat-label">Sessions</span><span class="week-stat-value">${weekTotalSessions}</span></span>
                        <span class="week-stat-divider"></span>
                        <span class="week-stat"><span class="week-stat-label">In</span><span class="week-stat-value">${formatNumber(weekTotalInput)}</span></span>
                        <span class="week-stat"><span class="week-stat-label">Out</span><span class="week-stat-value">${formatNumber(weekTotalOutput)}</span></span>
                        <span class="week-stat-divider"></span>
                        <span class="week-strip-cost">$${weekTotalCost.toFixed(2)}</span>
                    </div>
                </div>
            </td>
        </tr>`;
    }
    tbody.innerHTML = html;
    updateTotalsRow(sessions);
    updateToggleAllButton(false);
}

/**
 * Show the session detail modal for a given session index.
 */
export function showSessionDetail(idx) {
    const s = _sessionDetailStore[idx];
    if (!s) return;

    const mi = getModelInfo(s.model);
    const sc = sourceClass(s.source);
    const titleText = s.title || '(untitled session)';
    const sessionId = s.sessionId || s.file?.replace('.jsonl', '') || '—';
    const hasSessionId = s.sessionId || (s.file && s.file.endsWith('.jsonl'));
    const isClaudeCode = s.source === 'Claude Code';
    const resumeCmd = `claude --resume ${sessionId}`;

    let modalHTML = `
        <div class="session-modal-header">
            <div class="session-modal-title">${titleText.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</div>
            <button class="session-modal-close" onclick="closeSessionDetail()">&times;</button>
        </div>
        <div class="session-modal-body">
            <div class="session-modal-meta">
                <div class="session-meta-row">
                    <span class="meta-label">Date</span>
                    <span class="meta-value">${s.date} ${s.time || ''}</span>
                </div>
                <div class="session-meta-row">
                    <span class="meta-label">Source</span>
                    <span class="meta-value"><span class="source-badge source-${sc}">${s.source}</span></span>
                </div>
                <div class="session-meta-row">
                    <span class="meta-label">Model</span>
                    <span class="meta-value"><span class="model-badge ${mi.cls}">${mi.name}</span></span>
                </div>
                ${s.cwd ? `<div class="session-meta-row">
                    <span class="meta-label">Project</span>
                    <span class="meta-value meta-mono">${s.cwd.replace(/</g, '&lt;')}</span>
                </div>` : ''}
                <div class="session-meta-row">
                    <span class="meta-label">Session ID</span>
                    <span class="meta-value meta-mono">${sessionId}</span>
                </div>
            </div>
            <div class="session-modal-tokens">
                <div class="token-stat"><span class="token-stat-label">Input</span><span class="token-stat-value">${formatNumber(s.input_tokens || 0)}</span></div>
                <div class="token-stat"><span class="token-stat-label">Output</span><span class="token-stat-value">${formatNumber(s.output_tokens || 0)}</span></div>
                <div class="token-stat"><span class="token-stat-label">Cache Read</span><span class="token-stat-value">${formatNumber(s.cache_read || 0)}</span></div>
                <div class="token-stat"><span class="token-stat-label">Cache Write</span><span class="token-stat-value">${formatNumber(s.cache_write || 0)}</span></div>
                <div class="token-stat"><span class="token-stat-label">Cost</span><span class="token-stat-value cost-value ${costClass(s.cost)}">$${s.cost.toFixed(2)}</span></div>
            </div>
            ${s.history && s.history.length > 0 ? `
            <div class="session-modal-history">
                <div class="history-label">Conversation History</div>
                <div class="history-timeline">
                    ${s.history.map(h => `
                        <div class="history-msg history-${h.role}">
                            <div class="history-role">${h.role === 'user' ? 'You' : 'Claude'}</div>
                            <div class="history-text">${h.text.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</div>
                        </div>`).join('')}
                    ${s.history.length >= 15 ? '<div class="history-truncated">... conversation continues</div>' : ''}
                </div>
            </div>` : ''}
            ${hasSessionId && isClaudeCode ? `
            <div class="session-modal-resume">
                <div class="resume-label">Resume this session</div>
                <div class="resume-cmd-row">
                    <code class="resume-cmd">${resumeCmd}</code>
                    <button class="resume-copy-btn" onclick="copySessionCmd('${resumeCmd}', this)">Copy</button>
                </div>
                ${s.cwd ? `<div class="resume-cmd-row" style="margin-top:6px;">
                    <code class="resume-cmd">cd ${s.cwd.replace(/'/g, "\\'")} && ${resumeCmd}</code>
                    <button class="resume-copy-btn" onclick="copySessionCmd('cd ${s.cwd.replace(/'/g, "\\\\'")} && ${resumeCmd}', this)">Copy</button>
                </div>` : ''}
            </div>` : ''}
        </div>`;

    let overlay = document.getElementById('session-modal-overlay');
    let modal = document.getElementById('session-modal');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'session-modal-overlay';
        overlay.className = 'session-modal-overlay';
        overlay.onclick = closeSessionDetail;
        document.body.appendChild(overlay);
    }
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'session-modal';
        modal.className = 'session-modal';
        document.body.appendChild(modal);
    }
    modal.innerHTML = modalHTML;
    // Trigger animation
    requestAnimationFrame(() => {
        overlay.classList.add('visible');
        modal.classList.add('visible');
    });
}

/**
 * Close the session detail modal.
 */
export function closeSessionDetail() {
    const overlay = document.getElementById('session-modal-overlay');
    const modal = document.getElementById('session-modal');
    if (overlay) overlay.classList.remove('visible');
    if (modal) modal.classList.remove('visible');
}

/**
 * Copy a command string to clipboard and show feedback on the button.
 */
export function copySessionCmd(cmd, btn) {
    navigator.clipboard.writeText(cmd).then(() => {
        const orig = btn.textContent;
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = orig; btn.classList.remove('copied'); }, 1500);
    });
}

/**
 * Initialize keyboard shortcuts for table interactions.
 * Shift+E toggles all day rows.
 */
export function initKeyboardShortcuts(toggleAllFn) {
    const toggleAll = toggleAllFn || toggleAllDays;
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeSessionDetail();
            return;
        }
        if (e.shiftKey && e.key === 'E') {
            const tag = document.activeElement.tagName.toLowerCase();
            if (tag === 'input' || tag === 'textarea' || tag === 'select') return;
            e.preventDefault();
            toggleAll();
        }
    });
}

// Make functions available globally for onclick handlers
window.toggleDay = toggleDay;
window.showSessionDetail = showSessionDetail;
window.closeSessionDetail = closeSessionDetail;
window.copySessionCmd = copySessionCmd;
```

## File: `js/config/chart-config.js`
```javascript
/**
 * Chart Configuration Module
 *
 * Contains Chart.js default settings and shared configuration.
 * Sets global defaults for all charts in the dashboard.
 */

/**
 * Initialize Chart.js global defaults.
 * Must be called before creating any Chart instances.
 */
export function initChartDefaults() {
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.borderColor = 'rgba(30, 41, 59, 0.4)';
    Chart.defaults.font.family = "'JetBrains Mono', monospace";
    Chart.defaults.font.size = 11;
}

/**
 * Shared tooltip configuration for all charts.
 * Uses frosted glass aesthetic for a polished look.
 */
export const commonTooltipConfig = {
    backgroundColor: 'rgba(15, 23, 42, 0.92)',
    borderColor: 'rgba(34, 211, 238, 0.15)',
    borderWidth: 1,
    titleColor: '#e2e8f0',
    bodyColor: '#94a3b8',
    footerColor: '#e2e8f0',
    padding: { top: 12, bottom: 12, left: 14, right: 14 },
    cornerRadius: 10,
    titleFont: { family: "'Outfit', sans-serif", size: 13, weight: '600' },
    bodyFont: { family: "'JetBrains Mono', monospace", size: 11 },
    footerFont: { family: "'JetBrains Mono', monospace", size: 11, weight: '600' },
    boxPadding: 6,
    usePointStyle: true,
    caretSize: 6,
    caretPadding: 8,
};

/**
 * Shared legend configuration for chart legends.
 */
export const commonLegendConfig = {
    labels: {
        padding: 20,
        usePointStyle: true,
        pointStyleWidth: 8,
        color: '#cbd5e1',
        font: {
            family: "'JetBrains Mono', monospace",
            size: 11,
            weight: '400'
        }
    }
};
```

## File: `js/config/constants.js`
```javascript
/**
 * Constants Module
 *
 * Contains all constant values used throughout the application:
 * - Source color palette for charts
 * - Default fallback colors
 * - Model pricing tiers
 * - Day name arrays for heatmap
 */

/**
 * Source color palette mapping source names to hex colors.
 * Used by charts to ensure consistent color coding across visualizations.
 */
export const sourceColors = {
    'OpenClaw': '#fbbf24',
    'Clawdbot': '#fbbf24',
    'Claude Code': '#60a5fa',
    'Claude Desktop': '#a78bfa',
    'Cursor': '#22d3ee',
    'Windsurf': '#34d399',
    'Cline': '#fb7185',
    'Roo Code': '#f472b6',
    'Aider': '#2dd4bf',
    'Continue': '#f59e0b',
};

/**
 * Default color palette for sources not explicitly mapped.
 * Colors are assigned cyclically when a new unknown source is encountered.
 */
export const defaultColors = ['#34d399', '#fb7185', '#a78bfa', '#f472b6', '#2dd4bf'];

/**
 * Model family color mapping for model breakdown charts.
 */
export const modelColorMap = {
    'Opus': '#fb7185',
    'Sonnet': '#60a5fa',
    'Haiku': '#34d399',
    'Unknown': '#a78bfa',
};

/**
 * Abbreviated day names for heatmap column headers.
 * Order: Monday through Sunday (ISO week standard).
 */
export const DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

/**
 * Full day names for heatmap tooltips.
 * Order: Monday through Sunday (ISO week standard).
 */
export const DAY_NAMES_FULL = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
```

## File: `js/utils/class-utils.js`
```javascript
/**
 * Class Utilities Module
 *
 * CSS class name generation utilities for badges and styling.
 * Provides consistent class names based on cost levels and sources.
 */

/**
 * Get CSS class for a cost badge based on cost value.
 *
 * @param {number} cost - The cost amount in dollars
 * @returns {string} CSS class name ('cost-low', 'cost-medium', or 'cost-high')
 *
 * @example
 * costClass(0.50) // "cost-low"
 * costClass(10.00) // "cost-medium"
 * costClass(50.00) // "cost-high"
 */
export function costClass(cost) {
    return cost < 1 ? 'cost-low' : cost < 20 ? 'cost-medium' : 'cost-high';
}

/**
 * Get CSS class for cost text color based on cost value.
 *
 * @param {number} cost - The cost amount in dollars
 * @returns {string} CSS class name for text color
 *
 * @example
 * costTextClass(0.50) // "cost-low-text"
 * costTextClass(10.00) // "cost-medium-text"
 * costTextClass(50.00) // "cost-high-text"
 */
export function costTextClass(cost) {
    return cost < 1 ? 'cost-low-text' : cost < 20 ? 'cost-medium-text' : 'cost-high-text';
}

/**
 * Get CSS class for a source badge.
 *
 * @param {string} source - The source name
 * @returns {string} CSS class name for source badge
 *
 * @example
 * sourceClass('Claude Desktop') // "desktop"
 * sourceClass('Cursor') // "cursor"
 * sourceClass('OpenClaw') // "openclaw"
 */
export function sourceClass(source) {
    if (source === 'Clawdbot' || source === 'OpenClaw') return 'openclaw';
    if (source === 'Claude Desktop') return 'desktop';
    if (source === 'Cursor') return 'cursor';
    if (source === 'Windsurf') return 'windsurf';
    if (source === 'Cline' || source === 'Roo Code') return 'cline';
    if (source === 'Aider') return 'aider';
    if (source === 'Continue') return 'continue';
    return 'claude';
}
```

## File: `js/utils/date-utils.js`
```javascript
/**
 * Date Utilities Module
 *
 * Date calculation and formatting functions.
 * Handles ISO week calculations (Monday as week start) and date formatting.
 */

/**
 * Get the Monday (week start) for a given date.
 * Uses ISO 8601 week standard (Monday = start of week).
 *
 * @param {string} dateStr - Date in YYYY-MM-DD format
 * @returns {string} ISO week start date in YYYY-MM-DD format
 *
 * @example
 * getWeekStart('2024-01-15') // Returns the Monday of that week
 */
export function getWeekStart(dateStr) {
    const d = new Date(dateStr + 'T00:00:00');
    const day = d.getDay();
    const diff = (day === 0 ? 6 : day - 1);
    d.setDate(d.getDate() - diff);
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const dd = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${dd}`;
}

/**
 * Get the Sunday (week end) for a given week start date.
 *
 * @param {string} weekStartStr - Week start date in YYYY-MM-DD format (Monday)
 * @returns {string} Week end date in YYYY-MM-DD format (Sunday)
 *
 * @example
 * getWeekEnd('2024-01-08') // Returns '2024-01-14' (the following Sunday)
 */
export function getWeekEnd(weekStartStr) {
    const d = new Date(weekStartStr + 'T00:00:00');
    d.setDate(d.getDate() + 6);
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const dd = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${dd}`;
}

/**
 * Format a week range as a human-readable label.
 *
 * @param {string} weekStartStr - Week start date in YYYY-MM-DD format
 * @returns {string} Formatted week label (e.g., "Jan 8 – Jan 14")
 *
 * @example
 * formatWeekLabel('2024-01-08') // "Jan 8 – Jan 14"
 */
export function formatWeekLabel(weekStartStr) {
    const start = new Date(weekStartStr + 'T00:00:00');
    const end = new Date(weekStartStr + 'T00:00:00');
    end.setDate(end.getDate() + 6);
    const opts = { month: 'short', day: 'numeric' };
    return start.toLocaleDateString('en-US', opts) + ' \u2013 ' + end.toLocaleDateString('en-US', opts);
}
```

## File: `js/utils/formatters.js`
```javascript
/**
 * Formatters Module
 *
 * Number and value formatting utilities.
 * Used throughout the dashboard for consistent data presentation.
 */

/**
 * Format a number with K/M suffixes for large values.
 *
 * @param {number} num - The number to format
 * @returns {string} Formatted string (e.g., "1.5K", "2.3M", "42")
 *
 * @example
 * formatNumber(1234) // "1.2K"
 * formatNumber(1234567) // "1.2M"
 * formatNumber(42) // "42"
 */
export function formatNumber(num) {
    if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
    if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
    return num.toString();
}

/**
 * Format a number with commas for thousands separators.
 *
 * @param {number} value - The number to format
 * @param {number} decimals - Number of decimal places to show
 * @returns {string} Formatted string with commas (e.g., "1,234,567.89")
 *
 * @example
 * formatWithCommas(1234567.89, 2) // "1,234,567.89"
 * formatWithCommas(1234, 0) // "1,234"
 */
export function formatWithCommas(value, decimals) {
    const parts = value.toFixed(decimals).split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
}
```

## File: `js/utils/model-utils.js`
```javascript
/**
 * Model Utilities Module
 *
 * Model information, pricing lookups, and family classification.
 * Handles all model-specific logic for display and cost calculation.
 */

/**
 * Get pricing information for a specific model.
 * Returns per-million-token pricing for input, output, cache write, and cache read.
 *
 * @param {string} model - The model identifier string
 * @returns {{input: number, output: number, cacheWrite: number, cacheRead: number}}
 *   Pricing object with rates per million tokens
 *
 * @example
 * getPricingForModel('claude-opus-4-6')
 * // { input: 5, output: 25, cacheWrite: 6.25, cacheRead: 0.50 }
 *
 * getPricingForModel('claude-sonnet-3-5')
 * // { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 }
 */
export function getPricingForModel(model) {
    if (!model) return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
    const m = model.toLowerCase();

    // ============================================================
    // FUTURE MODELS (Claude 5.x and beyond - speculative pricing)
    // ============================================================
    // Note: These are projected prices based on historical pricing trends.
    // Update with actual pricing when models are released.

    // Claude 5.x Opus (future flagship - estimated higher than current Opus)
    if (m.includes('opus-5'))
        return { input: 20, output: 100, cacheWrite: 25, cacheRead: 2.0 };

    // Claude 5.x Sonnet (future mid-tier - estimated higher than Sonnet 4.5)
    if (m.includes('sonnet-5'))
        return { input: 5, output: 20, cacheWrite: 6.25, cacheRead: 0.50 };

    // Claude 5.x Haiku (future fast model - estimated higher than Haiku 4.5)
    if (m.includes('haiku-5'))
        return { input: 1.5, output: 7.5, cacheWrite: 1.875, cacheRead: 0.15 };

    // Claude 6.x and beyond (very speculative)
    if (m.includes('opus-6') || m.includes('opus-7') || m.includes('opus-8') || m.includes('opus-9'))
        return { input: 30, output: 150, cacheWrite: 37.5, cacheRead: 3.0 };
    if (m.includes('sonnet-6') || m.includes('sonnet-7') || m.includes('sonnet-8') || m.includes('sonnet-9'))
        return { input: 8, output: 40, cacheWrite: 10, cacheRead: 0.80 };
    if (m.includes('haiku-6') || m.includes('haiku-7') || m.includes('haiku-8') || m.includes('haiku-9'))
        return { input: 2, output: 10, cacheWrite: 2.5, cacheRead: 0.20 };

    // ============================================================
    // CURRENT MODELS (Claude 4.x)
    // ============================================================

    // Opus 4.6 and 4.5 (cheaper than older Opus)
    if (m.includes('opus-4-6') || m.includes('opus-4.6') || m.includes('opus-4-5') || m.includes('opus-4.5'))
        return { input: 5, output: 25, cacheWrite: 6.25, cacheRead: 0.50 };

    // Opus 4.1, 4.0 and Claude 3 Opus (more expensive)
    if (m.includes('opus-4-1') || m.includes('opus-4.1') || m.includes('opus-4-0') || m.includes('opus-4.0'))
        return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };

    // Generic Opus fallback (assume expensive)
    if (m.includes('opus'))
        return { input: 15, output: 75, cacheWrite: 18.75, cacheRead: 1.50 };

    // Sonnet 4.5 and 4.0 (same pricing)
    if (m.includes('sonnet-4') || m.includes('sonnet-3-7') || m.includes('sonnet-3.7') || m.includes('sonnet-3-5') || m.includes('sonnet-3.5'))
        return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };

    // Generic Sonnet fallback
    if (m.includes('sonnet'))
        return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };

    // Haiku 4.5 and 4.0 (newer, more expensive)
    if (m.includes('haiku-4-5') || m.includes('haiku-4.5') || m.includes('haiku-4-0') || m.includes('haiku-4.0'))
        return { input: 1, output: 5, cacheWrite: 1.25, cacheRead: 0.10 };

    // Haiku 3.5 and 3.0 (older, cheaper)
    if (m.includes('haiku-3') || m.includes('haiku'))
        return { input: 0.25, output: 1.25, cacheWrite: 0.30, cacheRead: 0.03 };

    // Default to Sonnet pricing
    return { input: 3, output: 15, cacheWrite: 3.75, cacheRead: 0.30 };
}

/**
 * Get model info (display name and CSS class) from a model string.
 *
 * @param {string} model - The model identifier string
 * @returns {{name: string, cls: string}} Object with display name and CSS class
 *
 * @example
 * getModelInfo('claude-opus-4-6') // { name: 'Opus 4.6', cls: 'model-opus' }
 * getModelInfo('claude-sonnet-3-5') // { name: 'Sonnet', cls: 'model-sonnet' }
 * getModelInfo('claude-haiku') // { name: 'Haiku', cls: 'model-haiku' }
 */
export function getModelInfo(model) {
    if (!model) return { name: 'Unknown', cls: 'model-sonnet' };
    const m = model.toLowerCase();

    // ============================================================
    // FUTURE MODELS (Claude 5.x and beyond)
    // ============================================================
    // Note: These are speculative and will need adjustment when released.
    // Check order carefully - most specific versions first.

    // Claude 5.x family (next generation)
    if (m.includes('opus-5-1') || m.includes('opus-5.1')) return { name: 'Opus 5.1', cls: 'model-opus' };
    if (m.includes('opus-5-0') || m.includes('opus-5.0') || m.includes('opus-5')) return { name: 'Opus 5', cls: 'model-opus' };

    if (m.includes('sonnet-5-1') || m.includes('sonnet-5.1')) return { name: 'Sonnet 5.1', cls: 'model-sonnet' };
    if (m.includes('sonnet-5-0') || m.includes('sonnet-5.0') || m.includes('sonnet-5')) return { name: 'Sonnet 5', cls: 'model-sonnet' };

    if (m.includes('haiku-5-1') || m.includes('haiku-5.1')) return { name: 'Haiku 5.1', cls: 'model-haiku' };
    if (m.includes('haiku-5-0') || m.includes('haiku-5.0') || m.includes('haiku-5')) return { name: 'Haiku 5', cls: 'model-haiku' };

    // Claude 6.x family (future)
    if (m.includes('opus-6-1') || m.includes('opus-6.1')) return { name: 'Opus 6.1', cls: 'model-opus' };
    if (m.includes('opus-6-0') || m.includes('opus-6.0') || m.includes('opus-6')) return { name: 'Opus 6', cls: 'model-opus' };

    if (m.includes('sonnet-6-1') || m.includes('sonnet-6.1')) return { name: 'Sonnet 6.1', cls: 'model-sonnet' };
    if (m.includes('sonnet-6-0') || m.includes('sonnet-6.0') || m.includes('sonnet-6')) return { name: 'Sonnet 6', cls: 'model-sonnet' };

    if (m.includes('haiku-6-1') || m.includes('haiku-6.1')) return { name: 'Haiku 6.1', cls: 'model-haiku' };
    if (m.includes('haiku-6-0') || m.includes('haiku-6.0') || m.includes('haiku-6')) return { name: 'Haiku 6', cls: 'model-haiku' };

    // Claude 7.x, 8.x, 9.x (far future - generic)
    if (m.includes('opus-7') || m.includes('opus-8') || m.includes('opus-9')) return { name: m.match(/opus-(\d+)/)?.[0]?.toUpperCase() || 'Opus', cls: 'model-opus' };
    if (m.includes('sonnet-7') || m.includes('sonnet-8') || m.includes('sonnet-9')) return { name: m.match(/sonnet-(\d+)/)?.[0]?.toUpperCase() || 'Sonnet', cls: 'model-sonnet' };
    if (m.includes('haiku-7') || m.includes('haiku-8') || m.includes('haiku-9')) return { name: m.match(/haiku-(\d+)/)?.[0]?.toUpperCase() || 'Haiku', cls: 'model-haiku' };

    // ============================================================
    // CURRENT MODELS (Claude 4.x)
    // ============================================================

    // Opus 4.x versions (most recent first)
    if (m.includes('opus-4-6') || m.includes('opus-4.6')) return { name: 'Opus 4.6', cls: 'model-opus' };
    if (m.includes('opus-4-5') || m.includes('opus-4.5')) return { name: 'Opus 4.5', cls: 'model-opus' };
    if (m.includes('opus-4-1') || m.includes('opus-4.1')) return { name: 'Opus 4.1', cls: 'model-opus' };
    if (m.includes('opus-4-0') || m.includes('opus-4.0')) return { name: 'Opus 4.0', cls: 'model-opus' };

    // Sonnet 4.x versions
    if (m.includes('sonnet-4-6') || m.includes('sonnet-4.6')) return { name: 'Sonnet 4.6', cls: 'model-sonnet' };
    if (m.includes('sonnet-4-5') || m.includes('sonnet-4.5')) return { name: 'Sonnet 4.5', cls: 'model-sonnet' };
    if (m.includes('sonnet-4-0') || m.includes('sonnet-4.0') || m.includes('sonnet-4-20')) return { name: 'Sonnet 4', cls: 'model-sonnet' };

    // Haiku 4.x versions
    if (m.includes('haiku-4-5') || m.includes('haiku-4.5')) return { name: 'Haiku 4.5', cls: 'model-haiku' };
    if (m.includes('haiku-4-0') || m.includes('haiku-4.0')) return { name: 'Haiku 4', cls: 'model-haiku' };

    // ============================================================
    // LEGACY MODELS (Claude 3.x and older)
    // ============================================================

    // Claude 3.x versions
    if (m.includes('3-opus') || m.includes('3.5-opus') || m.includes('3.0-opus')) return { name: 'Opus 3', cls: 'model-opus' };
    if (m.includes('3-7-sonnet') || m.includes('3.7-sonnet')) return { name: 'Sonnet 3.7', cls: 'model-sonnet' };
    if (m.includes('3-5-sonnet') || m.includes('3.5-sonnet')) return { name: 'Sonnet 3.5', cls: 'model-sonnet' };
    if (m.includes('3-sonnet') || m.includes('3.0-sonnet')) return { name: 'Sonnet 3', cls: 'model-sonnet' };
    if (m.includes('3-5-haiku') || m.includes('3.5-haiku')) return { name: 'Haiku 3.5', cls: 'model-haiku' };
    if (m.includes('3-haiku') || m.includes('3.0-haiku')) return { name: 'Haiku 3', cls: 'model-haiku' };

    // Generic family fallbacks
    if (m.includes('opus')) return { name: 'Opus', cls: 'model-opus' };
    if (m.includes('sonnet')) return { name: 'Sonnet', cls: 'model-sonnet' };
    if (m.includes('haiku')) return { name: 'Haiku', cls: 'model-haiku' };

    // Claude 2.x and 1.x (very old, rarely used)
    if (m.includes('claude-2.1')) return { name: 'Claude 2.1', cls: 'model-sonnet' };
    if (m.includes('claude-2.0') || m.includes('claude-2')) return { name: 'Claude 2', cls: 'model-sonnet' };
    if (m.includes('claude-1')) return { name: 'Claude 1', cls: 'model-sonnet' };
    if (m.includes('instant')) return { name: 'Instant', cls: 'model-haiku' };

    return { name: model, cls: 'model-sonnet' };
}

/**
 * Get model family from a model string.
 *
 * @param {string} model - The model identifier string
 * @returns {string} Model family name ('Opus', 'Sonnet', 'Haiku', or 'Unknown')
 *
 * @example
 * getModelFamily('claude-opus-4-6') // "Opus"
 * getModelFamily('claude-sonnet-3-5') // "Sonnet"
 * getModelFamily('claude-haiku') // "Haiku"
 */
export function getModelFamily(model) {
    if (!model) return 'Unknown';
    if (model.includes('opus')) return 'Opus';
    if (model.includes('sonnet')) return 'Sonnet';
    if (model.includes('haiku')) return 'Haiku';
    return 'Unknown';
}
```


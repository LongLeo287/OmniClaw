---
id: migueldeicaza-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.143105
---

# KNOWLEDGE EXTRACT: migueldeicaza
> **Extracted on:** 2026-03-30 17:42:48
> **Source:** migueldeicaza

---

## File: `SwiftTerm.md`
```markdown
# 📦 migueldeicaza/SwiftTerm [🔖 PENDING/APPROVE]
🔗 https://github.com/migueldeicaza/SwiftTerm


## Meta
- **Stars:** ⭐ 1428 | **Forks:** 🍴 278
- **Language:** Swift | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Xterm/VT100 Terminal emulator in Swift

## README (trích đầu)
```

SwiftTerm
=========

SwiftTerm is a VT100/Xterm terminal emulator library for Swift applications that can be 
embedded into macOS, iOS applications, text-based, headless applications or other 
custom scenarios. It has been used in several commercially available SSH clients, including 
[Secure Shellfish](https://apps.apple.com/us/app/secure-shellfish-ssh-files/id1336634154), 
 [La Terminal](https://apps.apple.com/us/app/la-terminal-ssh-client/id1629902861) and [CodeEdit](https://github.com/CodeEditApp/CodeEdit)

Check the [API Documentation](https://migueldeicaza.github.io/SwiftTerm/documentation/swiftterm/)

This repository contains both a terminal emulator engine that is UI agnostic, as well as
front-ends for this engine for iOS using UIKit, and macOS using AppKit.   A curses-based
terminal emulator (to emulate an xterm inside a console application) is available as
part of the [TermKit](https://github.com/migueldeicaza/TermKit) library. 

**Sample Code** There are a couple of minimal sample apps for Mac and iOS showing how to 
use the library inside the `TerminalApp` directory.   

* The sample Mac app has much of the functionality of MacOS' Terminal.app, but without the configuration UI.   
* The sample iOS application uses an SSH library to connect to a remote system (as there is no native shell
on iOS to run) and includes a login UI to configure the connection. 

## Companion Apps

[SwiftTermApp](https://github.com/migueldeicaza/SwiftTermApp) builds
an actual iOS app that uses this library and is more complete than the
testing apps in this module and provides a proper configuration UI.
It is a proof of concept for what you would need to do.

[Pane](https://github.com/migueldeicaza/pane) is a terminal
multiplexor, similar to tmux.

## History

This is a port of my original
[XtermSharp](https://github.com/migueldeicaza/XtermSharp), which was itself
based on [xterm.js](https://xtermjs.org).  At this point, I consider SwiftTerm
to be a more advanced terminal emulator than both of those (modulo
Selection/Accessibility) as it handles UTF, Unicode and grapheme clusters better
than those and has a more complete coverage of terminal emulation.   XtermSharp
is generally attempting to keep up, but has lagged behind.

Plenty of test cases have been extracted from xterm.js and Ghostty and
this also relies extensively on `esctest` to ensure compatibility.

Features
========

* Pretty decent terminal emulation, on or better than XtermSharp and xterm.js (and more comprehensive in many ways)
* Unicode rendering (including Emoji, and combining characters and emoji)
* Reusable and pluggable engine allows multiple user interfaces to be built on top of it:
   *  Bundled MacOS and iOS
   *  Bundled Headless terminal.
   *  [TermKit](https://github.com/migueldeicaza/TermKit) contains a terminal-over-a-terminal
   *  [Pane](https://github.com/migueldeicaza/pane) implements a terminal multiplexor
* Selection engine (with macOS support in the view)
* Search support w
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


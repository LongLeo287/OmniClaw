---
id: ramzesenok-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:06.683472
---

# KNOWLEDGE EXTRACT: ramzesenok
> **Extracted on:** 2026-03-30 17:52:59
> **Source:** ramzesenok

---

## File: `iOS-Accessibility-Audit-Skill.md`
```markdown
# 📦 ramzesenok/iOS-Accessibility-Audit-Skill [🔖 PENDING/APPROVE]
🔗 https://github.com/ramzesenok/iOS-Accessibility-Audit-Skill


## Meta
- **Stars:** ⭐ 12 | **Forks:** 🍴 0
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Skill that will help agents audit your app or concrete features against accessibility norms

## README (trích đầu)
```
# iOS-Accessibility-Audit-Skill
A Skill that will help agents audit your app or concrete features against accessibility norms and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) in particular.

- Focuses on iOS and SwiftUI
- Provides an audit, not fixes
- Suggests follow-up human checks to perform

Audit includes a problem, WCAG paragraph and a suggested solution with a code snippet. All in a descending priority markdown list. Looks like this:
## Findings - P1
### 1. Gesture-based task rows do not expose reliable control semantics

**What:** Likely issue (confidence: high). Task rows are interactive via .onTapGesture / .onLongPressGesture on a non-control container, so role/action/state exposure is not reliably equivalent to a native control for VoiceOver, Switch Control, or keyboard-style navigation.

**Where:** HistoryView.swift

**Fix suggestion:** Use a semantic Button for toggle, expose done/not-done as accessibility value, and provide copy as an explicit accessibility action.

**WCAG:** 4.1.2 - Name, Role, Value (A); 2.1.1 - Keyboard (A)

```swift
ForEach(todosForDate) { todo in
    let title = todo.title ?? ""

    Button {
        if isTogglable { toggleTodo(todo) }
    } label: {
        HistoryTodoView(title: title, isDone: todo.isDone == true)
            .frame(maxWidth: .infinity, alignment: .leading)
    }
    .buttonStyle(.plain)
    .contentShape(.rect)
    .accessibilityLabel(title)
    .accessibilityValue(todo.isDone == true ? "Done" : "Not done")
    .accessibilityHint(isTogglable ? "Double tap to toggle completion." : "Read-only for this date.")
    .accessibilityAction(named: Text("Copy title")) {
        UIPasteboard.general.string = title
        toastToShow = Toast(text: "Copied to clipboard", style: .info)
    }
}
```
### 2. Copy feedback is shown visually/haptically but not announced as a status message
**What:** Copied to clipboard feedback is pushed through toast + haptic only; there is no UIAccessibility.post(.announcement, ...) on this feature path, so VoiceOver users may miss transient feedback.

**Where:** HistoryView.swift, ToastMessageOverlay.swift

**Fix suggestion:** Post an accessibility announcement when copy succeeds (or centralize this in the toast modifier for all feature toasts).

**WCAG:** 4.1.3 - Status Messages (AA)

```swift
.onLongPressGesture(
    minimumDuration: 1,
    perform: {
        UIPasteboard.general.string = todo.title
        toastToShow = Toast(text: "Copied to clipboard", style: .info)
        UIAccessibility.post(
            notification: .announcement,
            argument: NSLocalizedString("Copied to clipboard", comment: "History copy feedback")
        )
    },
    onPressingChanged: { isBeingPressed in
        longPressedTodoAndDate = isBeingPressed ? (todo, .now) : nil
    }
)
```

## Findings - P2
...

## Findings - P3
...

## Scope / Assumptions
Audited with Swiftui Wcag Accessibility Auditor as a code-only review (no app run).

In scope: HistoryView.swift, and ToastMessageOverlay.
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


# [Mechanic/System Name]

> **Status**: Draft | In Review | Approved | Implemented
> **Author**: [Agent or person]
> **Last Updated**: [Date]
> **Implements Pillar**: [Which game pillar this supports]

## Overview

[One paragraph that explains this mechanic to someone who knows nothing about
the project. What is it, what does the player do, and why does it exist?]

## Player Fantasy

[What should the player FEEL when engaging with this mechanic? What is the
emotional or power fantasy being served? This section guides all detail
decisions below.]

## Detailed Design

### Core Rules

[Precise, unambiguous rules. A programmer should be able to implement this
section without asking questions. Use numbered rules for sequential processes
and bullet points for properties.]

### States and Transitions

[If this system has states (e.g., weapon states, status effects, phases),
document every state and every valid transition between states.]

| State | Entry Condition | Exit Condition | Behavior |
|-------|----------------|----------------|----------|

### Interactions with Other Systems

[How does this system interact with combat? Inventory? Progression? UI?
For each interaction, specify the interface: what data flows in, what flows
out, and who is responsible for what.]

## Formulas

[Every mathematical formula used by this system. For each formula:]

### [Formula Name]

```
result = base_value * (1 + modifier_sum) * scaling_factor
```

| Variable | Type | Range | Source | Description |
|----------|------|-------|--------|-------------|
| base_value | float | 1-100 | data file | The base amount before modifiers |
| modifier_sum | float | -0.9 to 5.0 | calculated | Sum of all active modifiers |
| scaling_factor | float | 0.5-2.0 | data file | Level-based scaling |

**Expected output range**: [min] to [max]
**Edge case**: When modifier_sum < -0.9, clamp to -0.9 to prevent negative results.

## Edge Cases

[Explicitly document what happens in unusual situations. Each edge case
should have a clear resolution.]

| Scenario | Expected Behavior | Rationale |
|----------|------------------|-----------|
| [What if X is zero?] | [This happens] | [Because of this reason] |
| [What if both effects trigger?] | [Priority rule] | [Design reasoning] |

## Dependencies

[List every system this mechanic depends on or that depends on this mechanic.]

| System | Direction | Nature of Dependency |
|--------|-----------|---------------------|
| [Combat] | This depends on Combat | Needs damage calculation results |
| [Inventory] | Inventory depends on this | Provides item effect data |

## Tuning Knobs

[Every value that should be adjustable for balancing. Include the current
value, the safe range, and what happens at the extremes.]

| Parameter | Current Value | Safe Range | Effect of Increase | Effect of Decrease |
|-----------|--------------|------------|-------------------|-------------------|

## Visual/Audio Requirements

[What visual and audio feedback does this mechanic need?]

| Event | Visual Feedback | Audio Feedback | Priority |
|-------|----------------|---------------|----------|

## UI Requirements

[What information needs to be displayed to the player and when?]

| Information | Display Location | Update Frequency | Condition |
|-------------|-----------------|-----------------|-----------|

## Acceptance Criteria

[Testable criteria that confirm this mechanic is working as designed.]

- [ ] [Criterion 1: specific, measurable, testable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
- [ ] Performance: System update completes within [X]ms
- [ ] No hardcoded values in implementation

## Open Questions

[Anything not yet decided. Each question should have an owner and deadline.]

| Question | Owner | Deadline | Resolution |
|----------|-------|----------|-----------|

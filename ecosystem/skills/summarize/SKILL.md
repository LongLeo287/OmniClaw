---
description: Summarize text at different detail levels
argument-hint: "[brief|medium|detailed] [text or topic]"
context: inline
user_invocable: true
---

Summarize the following content. Adjust the level of detail based on the first argument:

- **brief**: 1-2 sentence summary capturing the key point.
- **medium**: 3-5 sentence summary covering main ideas.
- **detailed**: Comprehensive summary with all important points, organized with bullet points.

If no detail level is specified, default to **medium**.

Content to summarize:

$ARGUMENTS

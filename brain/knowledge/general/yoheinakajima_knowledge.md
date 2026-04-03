---
id: yoheinakajima-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.559547
---

# KNOWLEDGE EXTRACT: yoheinakajima
> **Extracted on:** 2026-03-30 18:01:25
> **Source:** yoheinakajima

---

## File: `babyagi.md`
```markdown
# 📦 yoheinakajima/babyagi [🔖 PENDING/APPROVE]
🔗 https://github.com/yoheinakajima/babyagi
🌐 https://babyagi.org/

## Meta
- **Stars:** ⭐ 22213 | **Forks:** 🍴 2849
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# BabyAGI

> [!NOTE]
> The original BabyAGI from March 2023 introduced task planning as a method for developing autonomous agents. This project has been archived and moved to the [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive) repo (September 2024 snapshot).

> [!CAUTION]
> This is a framework built by Yohei who has never held a job as a developer. The purpose of this repo is to share ideas and spark discussion and for experienced devs to play with. Not meant for production use. Use with cautioun.

---

This newest BabyAGI is an experimental framework for a self-building autonomous agent. Earlier efforts to expand BabyAGI have made it clear that the optimal way to build a general autonomous agent is to build the simplest thing that can build itself.

Check out [this introductory X/Twitter thread](https://x.com/yoheinakajima/status/1840678823681282228) for a simple overview.

The core is a new function framework (**functionz**) for storing, managing, and executing functions from a database. It offers a graph-based structure for tracking imports, dependent functions, and authentication secrets, with automatic loading and comprehensive logging capabilities. Additionally, it comes with a dashboard for managing functions, running updates, and viewing logs.

## Table of Contents

- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Function Metadata](#function-metadata)
- [Function Loading](#function-loading)
- [Key Dependencies](#key-dependencies)
- [Execution Environment](#execution-environment)
  - [Log](#log)
- [Dashboard](#dashboard)
- [Pre-loaded Functions](#pre-loaded-functions)
- [Future/Draft Features](#futuredraft-features)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

To quickly check out the dashboard and see how it works:

1. **Install BabyAGI:**

    ```bash
    pip install babyagi
    ```

2. **Import BabyAGI and load the dashboard:**

    ```python
    import babyagi

    if __name__ == "__main__":
        app = babyagi.create_app('/dashboard')
        app.run(host='0.0.0.0', port=8080)
    ```

3. **Navigate to the dashboard:**

    Open your browser and go to `http://localhost:8080/dashboard` to access the BabyAGI dashboard.
    
## Basic Usage

Start by importing `babyagi` and registering your functions. Here's how to register two functions, where one depends on the other:

```python
import babyagi

# Register a simple function
@babyagi.register_function()
def world():
    return "world"

# Register a function that depends on 'world'
@babyagi.register_function(dependencies=["world"])
def hello_world():
    x = world()
    return f"Hello {x}!"

# Execute the function
print(babyagi.hello_world())  # Output: Hello world!

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
```

## Function Metadata

Functions can be registered with metadata to enhance their capabilities and manage their relati
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


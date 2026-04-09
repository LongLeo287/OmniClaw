---
description: Testing workflow – run tests, check coverage, fix failures, add missing tests
---

# Testing Workflow

## Steps

1. **Run all tests**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml
```

2. **Check coverage**
// turbo
```bash
# Using cargo-tarpaulin
cargo tarpaulin --manifest-path crates/contribai-rs/Cargo.toml --out term

# Using cargo-llvm-cov (alternative)
cargo llvm-cov --manifest-path crates/contribai-rs/Cargo.toml
```

3. **Identify untested code**
Look at uncovered lines in the tarpaulin/llvm-cov output. Focus on public functions and error paths.

4. **Run specific module tests**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml analysis::skills
```

5. **Run tests with debug output**
// turbo
```bash
RUST_LOG=debug cargo test --manifest-path crates/contribai-rs/Cargo.toml -- --nocapture
```

6. **Write missing tests**
Tests are co-located in the same `.rs` file as the code under test:
```rust
// At the bottom of the module file (e.g. src/analysis/skills.rs)
#[cfg(test)]
mod tests {
    use super::*;

    // Synchronous test
    #[test]
    fn test_function_happy_path() {
        // Arrange
        let input = "some input";

        // Act
        let result = function_under_test(input);

        // Assert
        assert!(result.is_ok());
        assert_eq!(result.unwrap().status, "success");
    }

    // Async test (requires tokio)
    #[tokio::test]
    async fn test_async_function() {
        let result = async_function_under_test("input").await;
        assert!(result.is_ok());
    }

    // Parameterized-style: use a loop or separate test functions
    #[test]
    fn test_validation_valid() { assert!(validate("valid")); }
    #[test]
    fn test_validation_empty() { assert!(!validate("")); }
}
```

7. **Run only a specific test by name**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml test_name -- --exact
```

8. **Generate HTML coverage report**
// turbo
```bash
cargo llvm-cov --manifest-path crates/contribai-rs/Cargo.toml --html
```
Open `target/llvm-cov/html/index.html` to browse coverage visually.

## Test Categories

Tests live inside `#[cfg(test)] mod tests { ... }` blocks co-located in each `.rs` source file:

- `src/core/*.rs` – Config, model, event, error unit tests
- `src/analysis/*.rs` – Skill detection, analyzer, repo-map tests
- `src/github/*.rs` – GitHub client integration tests (requires token)
- `src/mcp/*.rs` – MCP tool dispatch tests

The project has **323 tests** total across all modules.

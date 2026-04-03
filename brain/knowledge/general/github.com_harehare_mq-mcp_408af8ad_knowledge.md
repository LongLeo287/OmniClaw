---
id: github.com-harehare-mq-mcp-408af8ad-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.643608
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-mcp_408af8ad
> **Extracted on:** 2026-04-01 14:15:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523815/github.com_harehare_mq-mcp_408af8ad

---

## File: `.gitignore`
```
work

book
dist
debug/
target/
.direnv/
result

**/*.rs.bk
*.pdb

logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*
.pnpm-debug.log*

pkg
pids
*.pid
*.seed
*.pid.lock

lib-cov

coverage
*.lcov

.nyc_output

.grunt

bower_components

.lock-wscript

build/Release

node_modules/
jspm_packages/

.npm

.node_repl_history

*.tgz

.env
.env.test
.env.development.local
.env.test.local
.env.production.local
.env.local

.cache/
.vscode-test
.intentionally-empty-file.o


# OS metadata
.DS_Store
Thumbs.db

# IDE files
.idea
*.code-workspace

*.tgz

# vscode
*.vsix

# docs
docs/assets
docs/toolsAssets
docs/playground.html
docs/logo.svg

*.so

settings.local.json

# claude
CLAUDE.local.md

example.html

.github/chatmodes

.serena
```

## File: `Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
categories = ["command-line-utilities", "text-processing"]
description = "Markdown Query - MCP server implementation"
edition = "2024"
homepage = "https://mqlang.org/"
keywords = ["markdown", "jq", "query", "mcp"]
license = "MIT"
name = "mq-mcp"
readme = "README.md"
repository = "https://github.com/harehare/mq"
version = "0.1.9"

[dependencies]
miette = {version = "7.6.0", features = ["fancy"]}
mq-hir = "0.5.24"
mq-lang = "0.5.24"
mq-markdown = "0.5.24"
rmcp = {version = "0.9.0", features = ["server"]}
serde = {version = "1.0", features = ["derive"]}
serde_json = {version = "1.0"}
tokio = {version = "1.48.0", features = ["macros", "rt-multi-thread", "io-std"]}
tracing = "0.1.43"
tracing-subscriber = {version = "0.3.22", features = ["env-filter"]}

[dev-dependencies]
rstest = "0.26.1"

[lib]
name = "mq_mcp"
path = "src/lib.rs"

```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Takahiro Sato

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
<h1 align="center">mq-mcp</h1>

[![ci](https://github.com/harehare/mq-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-mcp/actions/workflows/ci.yml)
[![mq language](https://img.shields.io/badge/mq-language-orange.svg)](https://github.com/harehare/mq)


Model Context Protocol (MCP) server implementation for [mq](https://github.com/harehare/mq). This crate provides an MCP server that allows AI assistants to process Markdown and HTML content using mq's query language.

## Installation

You can install mq-mcp using the installation script:

```bash
curl -fsSL https://raw.githubusercontent.com/harehare/mq-mcp/main/bin/install.sh | bash
```

Or clone this repository and run the install script:

```bash
git clone https://github.com/harehare/mq-mcp.git
cd mq-mcp
./bin/install.sh
```

The script will:
- Install the `mq` binary to `~/.mq/bin`
- Add `~/.mq/bin` to your PATH (if not already present)
- Support macOS, Linux, and Windows
- Verify checksums for security

After installation, restart your terminal or run:

```bash
source ~/.zshrc  # or ~/.bashrc for bash users
```

## Implementation

The server implements four MCP tools:

- `html_to_markdown`: Converts HTML to Markdown and executes mq queries
- `extract_markdown`: Executes mq queries on Markdown content
- `available_functions`: Returns available functions for mq queries
- `available_selectors`: Returns available selectors for mq queries

### Tool Parameters

#### html_to_markdown

- `html` (string): HTML content to process
- `query` (optional string): mq query to execute

#### extract_markdown

- `markdown` (string): Markdown content to process
- `query` (string): mq query to execute

#### available_functions

No parameters. Returns JSON with function names, descriptions, parameters, and example queries.

#### available_selectors

No parameters. Returns JSON with selector names, descriptions, and parameters.

## Configuration

### Claude Desktop

#### Using mq-mcp binary directly

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "/Users/YOUR_USERNAME/.mq/bin/mq-mcp",
      "args": []
    }
  }
}
```

Or simply use `mq-mcp` if `~/.mq/bin` is in your PATH:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "mq-mcp",
      "args": []
    }
  }
}
```

#### Using mq command

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "/Users/YOUR_USERNAME/.mq/bin/mq",
      "args": ["mcp"]
    }
  }
}
```

Or simply use `mq` if `~/.mq/bin` is in your PATH:

```json
{
  "mcpServers": {
    "mq-mcp": {
      "command": "mq",
      "args": ["mcp"]
    }
  }
}
```

### VS Code with MCP Extension

#### Using mq-mcp binary directly

Add to `.vscode/settings.json`:

```json
{
  "mcp": {
    "servers": {
      "mq-mcp": {
        "type": "stdio",
        "command": "mq-mcp",
        "args": []
      }
    }
  }
}
```

#### Using mq command

Add to `.vscode/settings.json`:

```json
{
  "mcp": {
    "servers": {
      "mq-mcp": {
        "type": "stdio",
        "command": "mq",
        "args": ["mcp"]
      }
    }
  }
}
```

## License

This project is licensed under the MIT License
```

## File: `src/lib.rs`
```rust
pub mod server;
pub use server::start;
```

## File: `src/main.rs`
```rust
pub mod server;

use tracing_subscriber::EnvFilter;

#[tokio::main]
async fn main() -> miette::Result<()> {
    tracing_subscriber::fmt()
        .with_env_filter(EnvFilter::from_default_env())
        .with_thread_names(true)
        .with_target(true)
        .with_line_number(true)
        .init();

    server::start().await
}
```

## File: `src/server.rs`
```rust
use miette::miette;
use rmcp::{
    ErrorData, ServerHandler, ServiceExt,
    handler::server::{tool::ToolRouter, wrapper::Parameters},
    model::{CallToolResult, Content, ProtocolVersion, ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
};
use tokio::io::{stdin, stdout};
type McpResult = Result<CallToolResult, ErrorData>;

#[derive(Debug, Clone, Default)]
pub struct Server {
    pub tool_router: ToolRouter<Self>,
}

#[derive(Debug, rmcp::serde::Deserialize, schemars::JsonSchema)]
struct QueryForHtml {
    #[schemars(description = "The HTML to process")]
    html: String,
    #[schemars(
        description = "The mq query to execute. Selectors and functions listed in the available_selectors and available_functions tools can be used."
    )]
    query: Option<String>,
}

#[derive(Debug, rmcp::serde::Deserialize, schemars::JsonSchema)]
struct QueryForMarkdown {
    #[schemars(description = "The markdown to process")]
    markdown: String,
    #[schemars(
        description = "The mq query to execute. Selectors and functions listed in the available_selectors and available_functions tools can be used ."
    )]
    query: String,
}

#[derive(Debug, rmcp::serde::Serialize, rmcp::serde::Deserialize, schemars::JsonSchema)]
struct FunctionInfo {
    #[schemars(description = "The function name")]
    name: String,
    #[schemars(description = "The function description")]
    description: String,
    #[schemars(description = "The function parameters")]
    params: Vec<String>,
    #[schemars(description = "Whether this is a built-in function")]
    is_builtin: bool,
}

#[derive(Debug, rmcp::serde::Serialize, rmcp::serde::Deserialize, schemars::JsonSchema)]
struct SelectorInfo {
    #[schemars(description = "The function name")]
    name: String,
    #[schemars(description = "The function description")]
    description: String,
    #[schemars(description = "The function parameters")]
    params: Vec<String>,
}

#[tool_router]
impl Server {
    pub fn new() -> Result<Self, Box<dyn std::error::Error>> {
        Ok(Self {
            tool_router: Self::tool_router(),
        })
    }

    #[tool(
        description = "Executes an mq query on the provided HTML content and returns the result as Markdown. Selectors and functions listed in the available_selectors and available_functions tools can be used."
    )]
    fn html_to_markdown(
        &self,
        Parameters(QueryForHtml { html, query }): Parameters<QueryForHtml>,
    ) -> McpResult {
        let mut engine = mq_lang::DefaultEngine::default();
        engine.load_builtin_module();

        let markdown = mq_markdown::Markdown::from_html_str(&html).map_err(|e| {
            ErrorData::parse_error(
                "Failed to parse html",
                Some(serde_json::Value::String(e.to_string())),
            )
        })?;
        let values = engine
            .eval(
                &query.unwrap_or("identity()".to_string()),
                markdown
                    .nodes
                    .clone()
                    .into_iter()
                    .map(mq_lang::RuntimeValue::from),
            )
            .map_err(|e| {
                ErrorData::invalid_request(
                    "Failed to query",
                    Some(serde_json::Value::String(e.to_string())),
                )
            })?;

        Ok(CallToolResult::success(
            values
                .into_iter()
                .filter_map(|value| {
                    if value.is_none() || value.is_empty() {
                        None
                    } else {
                        Some(Content::text(value.to_string()))
                    }
                })
                .collect::<Vec<_>>(),
        ))
    }

    #[tool(
        description = "Extract from markdown content. Selectors and functions listed in the available_selectors and available_functions tools can be used."
    )]
    fn extract_markdown(
        &self,
        Parameters(QueryForMarkdown { markdown, query }): Parameters<QueryForMarkdown>,
    ) -> Result<CallToolResult, ErrorData> {
        let mut engine = mq_lang::DefaultEngine::default();
        engine.load_builtin_module();

        let markdown = mq_markdown::Markdown::from_html_str(&markdown).map_err(|e| {
            ErrorData::parse_error(
                "Failed to parse markdown",
                Some(serde_json::Value::String(e.to_string())),
            )
        })?;
        let values = engine
            .eval(
                &query,
                markdown
                    .nodes
                    .clone()
                    .into_iter()
                    .map(mq_lang::RuntimeValue::from),
            )
            .map_err(|e| {
                ErrorData::invalid_request(
                    "Failed to query",
                    Some(serde_json::Value::String(e.to_string())),
                )
            })?;

        Ok(CallToolResult::success(
            values
                .into_iter()
                .filter_map(|value| {
                    if value.is_none() || value.is_empty() {
                        None
                    } else {
                        Some(Content::text(value.to_string()))
                    }
                })
                .collect::<Vec<_>>(),
        ))
    }

    #[tool(description = "Get available selectors that can be used in mq query.")]
    fn available_functions(&self) -> McpResult {
        let hir = mq_hir::Hir::default();
        let mut functions = Vec::with_capacity(256);

        // Get built-in functions
        for (name, builtin_doc) in hir.builtin.functions.iter() {
            functions.push(FunctionInfo {
                name: name.to_string(),
                description: builtin_doc.description.to_string(),
                params: builtin_doc.params.iter().map(|p| p.to_string()).collect(),
                is_builtin: true,
            });
        }

        // Get internal functions
        for (name, builtin_doc) in hir.builtin.internal_functions.iter() {
            functions.push(FunctionInfo {
                name: name.to_string(),
                description: builtin_doc.description.to_string(),
                params: builtin_doc.params.iter().map(|p| p.to_string()).collect(),
                is_builtin: true,
            });
        }

        let output = serde_json::json!({
            "functions": functions,
            "examples": vec![
                r#"select(or(.[], .code, .h)) | upcase() | add(" Hello World")"#.to_string(),
                r#"select(not(.code))"#.to_string(),
                r#"select(.code.lang == "js")"#.to_string(),
            ],
        });
        let functions_json = serde_json::to_string(&output).expect("Failed to serialize functions");

        Ok(CallToolResult::success(vec![Content::text(functions_json)]))
    }

    #[tool(description = "Get available selectors that can be used in mq query.")]
    fn available_selectors(&self) -> McpResult {
        let hir = mq_hir::Hir::default();
        let mut selectors = Vec::with_capacity(256);

        // Get selectors
        for (name, selector_doc) in hir.builtin.selectors.iter() {
            selectors.push(SelectorInfo {
                name: name.to_string(),
                description: selector_doc.description.to_string(),
                params: selector_doc.params.iter().map(|p| p.to_string()).collect(),
            });
        }

        let output = serde_json::json!({
            "selectors": selectors,
        });
        let selectors_json = serde_json::to_string(&output).expect("Failed to serialize selectors");

        Ok(CallToolResult::success(vec![Content::text(selectors_json)]))
    }
}

#[tool_handler]
impl ServerHandler for Server {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            protocol_version: ProtocolVersion::V_2025_06_18,
            instructions: Some(
                "mq is a tool for processing markdown content with a jq-like syntax.".into(),
            ),
            capabilities: ServerCapabilities::builder()
                .enable_logging()
                .enable_tools()
                .enable_tool_list_changed()
                .build(),
            ..Default::default()
        }
    }
}

pub async fn start() -> miette::Result<()> {
    let transport = (stdin(), stdout());
    let server = Server::new().expect("Failed to create server");

    let service = server.serve(transport).await.map_err(|e| miette!(e))?;
    service.waiting().await.map_err(|e| miette!(e))?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(
        QueryForHtml {
            html: "<h1>Test Heading</h1><p>This is a test paragraph.</p>".to_string(),
            query: Some(".h1".to_string()),
        },
        Ok("# Test Heading")
    )]
    #[case(
        QueryForHtml {
            html: "<h1>Test Heading</h1><p>This is a test paragraph.</p>".to_string(),
            query: Some(".text".to_string()),
        },
        Ok("Test Heading\n\nThis is a test paragraph.")
    )]
    #[case(
        QueryForHtml {
            html: "<h1>Test Heading</h1><p>This is a test paragraph.</p>".to_string(),
            query: None,
        },
        Ok("# Test Heading\n\nThis is a test paragraph.")
    )]
    #[case(
        QueryForHtml {
            html: "<h1>Test Heading".to_string(), // malformed HTML
            query: Some(".h1".to_string()),
        },
        Ok("# Test Heading")
    )]
    #[case(
        QueryForHtml {
            html: "<h1>Test Heading</h1>".to_string(),
            query: Some("not_a_function(".to_string()), // invalid query
        },
        Err("Failed to query")
    )]
    fn test_html_to_markdown(
        #[case] query: QueryForHtml,
        #[case] expected: Result<&'static str, &'static str>,
    ) {
        let server = Server::new().expect("Failed to create server");
        let result = server.html_to_markdown(Parameters(query));
        match expected {
            Ok(expected_text) => {
                let result = result.expect("Expected Ok result");
                assert!(!result.is_error.unwrap_or_default());
                let actual = result
                    .content
                    .into_iter()
                    .map(|c| c.as_text().map(|t| t.text.clone()).unwrap_or_default())
                    .collect::<Vec<_>>()
                    .join("\n\n");

                assert_eq!(actual, expected_text);
            }
            Err(expected_err) => {
                let err = result.expect_err("Expected error result");
                let msg = format!("{err}");
                assert!(
                    msg.contains(expected_err),
                    "Error message '{msg}' does not contain expected '{expected_err}'"
                );
            }
        }
    }

    #[rstest]
    #[case(
        QueryForMarkdown {
            markdown: "# Test Heading".to_string(),
            query: ".h1".to_string(),
        },
        Ok("# Test Heading")
    )]
    #[case(
        QueryForMarkdown {
            markdown: "# Test Heading\n\nThis is a test paragraph.".to_string(),
            query: ".text".to_string(),
        },
        Ok("Test Heading\n\nThis is a test paragraph.")
    )]
    #[case(
        QueryForMarkdown {
            markdown: "# Test Heading\n\nThis is a test paragraph.".to_string(),
            query: "identity()".to_string(),
        },
        Ok("# Test Heading\n\nThis is a test paragraph.")
    )]
    #[case(
        QueryForMarkdown {
            markdown: "# Test Heading".to_string(),
            query: "not_a_function(".to_string(), // invalid query
        },
        Err("Failed to query")
    )]
    #[case(
        QueryForMarkdown {
            markdown: "".to_string(),
            query: ".h1".to_string(),
        },
        Ok("")
    )]
    fn test_extract_markdown(
        #[case] query: QueryForMarkdown,
        #[case] expected: Result<&'static str, &'static str>,
    ) {
        let server = Server::new().expect("Failed to create server");
        let result = server.extract_markdown(Parameters(query));
        match expected {
            Ok(expected_text) => {
                let result = result.expect("Expected Ok result");
                assert!(!result.is_error.unwrap_or_default());
                let actual = result
                    .content
                    .into_iter()
                    .map(|c| c.as_text().map(|c| c.text.clone()).unwrap_or_default())
                    .collect::<Vec<_>>()
                    .join("\n\n");
                assert_eq!(actual, expected_text);
            }
            Err(expected_err) => {
                let err = result.expect_err("Expected error result");
                let msg = format!("{err}");
                assert!(
                    msg.contains(expected_err),
                    "Error message '{msg}' does not contain expected '{expected_err}'"
                );
            }
        }
    }

    #[test]
    fn test_available_functions() {
        let server = Server::new().expect("Failed to create server");
        let result = server.available_functions().unwrap();
        assert!(!result.is_error.unwrap_or_default());
        assert_eq!(result.content.into_iter().len(), 1);
    }

    #[test]
    fn test_available_selectors() {
        let server = Server::new().expect("Failed to create server");
        let result = server.available_selectors().unwrap();
        assert!(!result.is_error.unwrap_or_default());
        assert_eq!(result.content.into_iter().len(), 1);
    }

    #[test]
    fn test_get_info() {
        let server = Server::new().expect("Failed to create server");
        let info = server.get_info();
        assert_eq!(info.protocol_version, ProtocolVersion::V_2025_06_18);
        assert!(info.instructions.is_some());
        let instructions = info.instructions.unwrap();
        assert!(
            instructions.contains("mq is a tool for processing markdown content"),
            "Instructions should mention mq"
        );
    }
}
```


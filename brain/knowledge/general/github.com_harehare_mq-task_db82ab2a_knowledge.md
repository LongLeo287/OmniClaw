---
id: github.com-harehare-mq-task-db82ab2a-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.725775
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-task_db82ab2a
> **Extracted on:** 2026-04-01 14:39:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524041/github.com_harehare_mq-task_db82ab2a

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

work
```

## File: `Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
categories = ["command-line-utilities", "text-processing"]
description = "A task runner using Markdown"
edition = "2024"
homepage = "https://mqlang.org/"
keywords = ["markdown", "jq", "taskrunner"]
license = "MIT"
name = "mq-task"
readme = "README.md"
repository = "https://github.com/harehare/mq"
version = "0.1.8"

[[bin]]
name = "mq-task"
path = "src/main.rs"

[lib]
name = "mq_task"
path = "src/lib.rs"

[dependencies]
clap = {version = "4.6.0", features = ["derive"]}
colored = "3.1"
crossterm = "0.29"
miette = {version = "7.6.0", features = ["fancy"]}
mq-lang = "0.5.23"
mq-markdown = "0.5.23"
ratatui = "0.30"
serde = {version = "1.0", features = ["derive"]}
serde_json = "1.0"
thiserror = "2.0.18"
toml = "1.1.0"
which = "8.0.2"

[profile.release]
codegen-units = 1
lto = "fat"
opt-level = "z"
panic = "abort"
strip = true

[package.metadata.binstall]
pkg-fmt = "bin"
pkg-url = "{ repo }/releases/download/v{ version }/mq-task-{ target }{ binary-ext }"

```

## File: `README.md`
```markdown
<h1 align="center">mq-task</h1>

[![ci](https://github.com/harehare/mq-task/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq-task/actions/workflows/ci.yml)

`mq-task` is a task runner that executes code blocks in Markdown files based on section titles.
It is implemented using [mq](https://github.com/harehare/mq), a jq-like command-line tool for Markdown processing, to parse and extract sections from Markdown documents.

![demo](assets/demo.gif)

> [!WARNING]
> `mq-task` is currently under active development.

## Features

- Execute code blocks from specific sections in Markdown files
- Configurable runtimes for different programming languages
- Support for custom heading levels
- TOML-based configuration
- Built on top of the mq query language

## Installation

### Quick Install

```bash
curl -sSL https://raw.githubusercontent.com/harehare/mq-task/refs/heads/main/bin/install.sh | bash
```

The installer will:
- Download the latest mq binary for your platform
- Install it to `~/.mq/bin/`
- Update your shell profile to add mq to your PATH

### Cargo

```sh
$ cargo install --git https://github.com/harehare/mq-task.git
```

## Usage

### Run a task (shorthand)

```bash
# Run from README.md (default)
mq-task "Task Name"

# Run from a specific file
mq-task -f tasks.md "Task Name"
```

### Run a task (explicit)

```bash
mq-task run "Task Name"
mq-task run --file tasks.md "Task Name"
```

### Pass arguments to a task

You can pass arguments to your task using `--` separator:

```bash
# Pass arguments to a task
mq-task "Task Name" -- arg1 arg2 arg3

# With explicit run command
mq-task run "Task Name" -- arg1 arg2 arg3

# From a specific file
mq-task -f tasks.md "Task Name" -- arg1 arg2
```

Arguments are accessible via environment variables:
- `MX_ARGS`: All arguments joined by space (e.g., "arg1 arg2 arg3")
- `MX_ARG_0`, `MX_ARG_1`, ...: Individual arguments

Example in a Markdown task:

````markdown
## My Task

```bash
echo "All args: $MX_ARGS"
echo "First arg: $MX_ARG_0"
echo "Second arg: $MX_ARG_1"
```
````

### List available tasks

```bash
# List tasks from README.md (default)
mq-task

# List tasks from a specific file
mq-task -f tasks.md
mq-task list --file tasks.md
```

### Initialize configuration

```bash
mq-task init
```

This creates an `mq-task.toml` file with default runtime settings.

## Configuration

Create an `mq-task.toml` file to customize runtime behavior:

```toml
# Runtimes configuration
# Simple format: language = "command"
# The execution mode defaults to "stdin"
[runtimes]
bash = "bash"
sh = "sh"
python = "python3"
ruby = "ruby"
node = "node"
javascript = "node"
js = "node"
php = "php"
perl = "perl"
jq = "jq"

# Detailed format with execution mode
# Execution modes: "stdin" (default), "file", or "arg"
# - stdin: Pass code via standard input
# - file: Write code to a temporary file and pass it as an argument
# - arg: Pass code as a command-line argument

[runtimes.go]
command = "go run"
execution_mode = "file"  # Go requires file-based execution

[runtimes.golang]
command = "go run"
execution_mode = "file"

[runtimes.mq]
command = "mq"
execution_mode = "arg"  # mq uses query as argument
```

You can also mix both formats:

```toml
[runtimes]
python = "python3"  # Simple format, uses default stdin mode

[runtimes.go]       # Detailed format with custom execution mode
command = "go run"
execution_mode = "file"
```

```bash
# Using shorthand (from tasks.md by default)
mq-task Build

# From a specific file
mq-task -f tasks.md Build

# Using explicit run command
mq-task run Build
mq-task run --file tasks.md Build
```

## License

MIT
```

## File: `sections.mq`
```
# Extracts sections from markdown
# Returns an array where each element is a dict with:
# - title: the heading text
# - level: the heading level (1-6)
# - content: array of markdown nodes in that section (including the heading)

import "section"

|

def extract_sections(md_nodes):
  let section_list = section::sections(md_nodes)
  | map(section_list, fn(s):
    let heading = first(s[:header])
    | let title = to_text(heading)
    | let level = heading.level
    | {"title": title, "level": level, "content": s[:children]}
  end)
end

# Extracts code blocks from a section
def extract_code_blocks(section_content):
  let code_blocks = filter(section_content, is_code)
  | map(code_blocks, fn(code):
    let lang = attr(code, "lang")
    | let text = to_text(code)
    | {"lang": lang, "code": text}
  end)
end

# Extracts text from a section
def extract_description(section_content):
  filter(section_content, is_text)
  | first()
  | if (is_none()): None else: to_text()
end

# Main query to extract sections with their code blocks
def sections_with_code(md_nodes):
  let section_list = extract_sections(md_nodes)
  | map(section_list, fn(section):
    let title = section["title"]
    | let level = section["level"]
    | let content = section["content"]
    | let codes = extract_code_blocks(content)
    | let description = extract_description(content)
    | {"title": title, "level": level, "codes": codes, "description": description}
  end)
end

```

## File: `assets/README.md`
```markdown
# Example

## Bash

```bash
echo "Hello, world!"
```

## Python

```python
print("Hello, world!")
```

## Ruby

This code block runs with Ruby.

```ruby
puts "Hello, world!"
```

## JavaScript

This code block runs with Node.js.

```javascript
console.log("Hello, world!");
```

## Go

This code block runs with Go.

```go
package main
import "fmt"
func main() {
    fmt.Println("Hello, world!")
}
```

## Rust

```rust
fn main() {
    println!("Hello, world!");
}
```

## Perl

```perl
print "Hello, world!\n";
```

## mq

```mq
print("Hello, world!")
```
```

## File: `assets/demo.tape`
```
Output "demo.gif"

Require echo

Set Shell "zsh"
Set FontSize 24
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set FontFamily "Hack Nerd Font"
Set Padding 16
Set WindowBar Colorful
Set Framerate 20

Hide
Type "clear"
Enter
Show

Type `mq-task`
Enter
Sleep 1.5s

Type `mq-task JavaScript`
Enter
Sleep 1.5s

Type `mq-task Go`
Enter
Sleep 1.5s

Type `mq-task Python`
Enter
Sleep 1.5s

Type `mq-task mq`
Enter
Sleep 1.5s
```

## File: `src/config.rs`
```rust
//! Configuration for mq_task task runner

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::convert::TryFrom;
use std::fs;
use std::path::Path;

use crate::error::{Error, Result};

/// Execution mode for a runtime
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Default)]
#[serde(rename_all = "lowercase")]
pub enum ExecutionMode {
    /// Pass code via stdin
    #[default]
    Stdin,
    /// Write code to a temporary file and pass it as argument
    File,
    /// Pass code as a command argument
    Arg,
}

impl TryFrom<&str> for ExecutionMode {
    type Error = Error;

    fn try_from(s: &str) -> Result<Self> {
        match s.to_lowercase().as_str() {
            "stdin" => Ok(ExecutionMode::Stdin),
            "file" => Ok(ExecutionMode::File),
            "arg" => Ok(ExecutionMode::Arg),
            _ => Err(Error::Config(format!(
                "Invalid execution mode: '{}'. Valid options: stdin, file, arg",
                s
            ))),
        }
    }
}

/// Runtime configuration that can be either a simple string or a detailed config
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
#[serde(untagged)]
pub enum RuntimeConfig {
    /// Simple command string (execution_mode defaults to stdin)
    Simple(String),
    /// Detailed configuration with command and execution mode
    Detailed {
        command: String,
        #[serde(default)]
        execution_mode: ExecutionMode,
    },
}

impl RuntimeConfig {
    /// Get the command string from the runtime config
    pub fn command(&self) -> &str {
        match self {
            RuntimeConfig::Simple(cmd) => cmd,
            RuntimeConfig::Detailed { command, .. } => command,
        }
    }

    /// Get the execution mode from the runtime config
    pub fn execution_mode(&self) -> ExecutionMode {
        match self {
            RuntimeConfig::Simple(_) => ExecutionMode::default(),
            RuntimeConfig::Detailed { execution_mode, .. } => execution_mode.clone(),
        }
    }
}

/// Configuration for mq_task task runner
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Config {
    /// Runtime mappings: language -> command or detailed config
    #[serde(default = "default_runtimes")]
    pub runtimes: HashMap<String, RuntimeConfig>,
}

impl Default for Config {
    fn default() -> Self {
        Self {
            runtimes: default_runtimes(),
        }
    }
}

impl Config {
    /// Load configuration from a TOML file
    pub fn from_file<P: AsRef<Path>>(path: P) -> Result<Self> {
        let content = fs::read_to_string(path)?;
        let config: Config = toml::from_str(&content)?;
        Ok(config)
    }

    /// Get runtime command for a language
    pub fn get_runtime(&self, lang: &str) -> Option<&str> {
        self.runtimes.get(lang).map(|config| config.command())
    }

    /// Get execution mode for a language
    pub fn get_execution_mode(&self, lang: &str) -> ExecutionMode {
        self.runtimes
            .get(lang)
            .map(|config| config.execution_mode())
            .unwrap_or_default()
    }

    /// Check if runtime exists for a language
    pub fn has_runtime(&self, lang: &str) -> bool {
        self.runtimes.contains_key(lang)
    }

    /// Apply runtime overrides from CLI arguments
    /// Format: ["lang:command", "lang2:command2"]
    /// execution_mode: optional execution mode to apply to all overrides
    pub fn apply_runtime_overrides(
        &mut self,
        overrides: &[String],
        execution_mode: Option<ExecutionMode>,
    ) -> Result<()> {
        for override_str in overrides {
            let parts: Vec<&str> = override_str.splitn(2, ':').collect();
            if parts.len() != 2 {
                return Err(Error::Config(format!(
                    "Invalid runtime override format: '{}'. Expected format: 'lang:command'",
                    override_str
                )));
            }

            let lang = parts[0].to_string();
            let command = parts[1].to_string();

            let runtime_config = if let Some(ref mode) = execution_mode {
                RuntimeConfig::Detailed {
                    command,
                    execution_mode: mode.clone(),
                }
            } else {
                RuntimeConfig::Simple(command)
            };

            self.runtimes.insert(lang, runtime_config);
        }

        Ok(())
    }

    /// Validate that all configured runtimes are available in PATH
    pub fn validate_runtimes(&self) -> Result<()> {
        for (lang, config) in &self.runtimes {
            let cmd = config.command();
            let binary = cmd.split_whitespace().next().unwrap_or(cmd);
            if which::which(binary).is_err() {
                return Err(Error::Config(format!(
                    "Runtime '{}' for language '{}' not found in PATH",
                    binary, lang
                )));
            }
        }
        Ok(())
    }
}

/// Default runtime mappings
fn default_runtimes() -> HashMap<String, RuntimeConfig> {
    let mut runtimes = HashMap::new();

    // Languages with stdin execution mode (default)
    runtimes.insert(
        "bash".to_string(),
        RuntimeConfig::Simple("bash".to_string()),
    );
    runtimes.insert("sh".to_string(), RuntimeConfig::Simple("sh".to_string()));
    runtimes.insert(
        "python".to_string(),
        RuntimeConfig::Simple("python3".to_string()),
    );
    runtimes.insert(
        "ruby".to_string(),
        RuntimeConfig::Simple("ruby".to_string()),
    );
    runtimes.insert(
        "node".to_string(),
        RuntimeConfig::Simple("node".to_string()),
    );
    runtimes.insert(
        "javascript".to_string(),
        RuntimeConfig::Simple("node".to_string()),
    );
    runtimes.insert("js".to_string(), RuntimeConfig::Simple("node".to_string()));
    runtimes.insert("php".to_string(), RuntimeConfig::Simple("php".to_string()));
    runtimes.insert(
        "perl".to_string(),
        RuntimeConfig::Simple("perl".to_string()),
    );
    runtimes.insert("jq".to_string(), RuntimeConfig::Simple("jq".to_string()));

    // Go requires file-based execution
    runtimes.insert(
        "go".to_string(),
        RuntimeConfig::Detailed {
            command: "go run".to_string(),
            execution_mode: ExecutionMode::File,
        },
    );
    runtimes.insert(
        "golang".to_string(),
        RuntimeConfig::Detailed {
            command: "go run".to_string(),
            execution_mode: ExecutionMode::File,
        },
    );

    // mq requires argument-based execution
    runtimes.insert(
        "mq".to_string(),
        RuntimeConfig::Detailed {
            command: "mq".to_string(),
            execution_mode: ExecutionMode::Arg,
        },
    );

    runtimes
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_runtime() {
        let config = Config::default();
        assert_eq!(config.get_runtime("bash"), Some("bash"));
        assert_eq!(config.get_runtime("python"), Some("python3"));
        assert_eq!(config.get_runtime("unknown"), None);
    }

    #[test]
    fn test_execution_modes() {
        let config = Config::default();
        // Test default execution mode (stdin)
        assert_eq!(config.get_execution_mode("bash"), ExecutionMode::Stdin);
        assert_eq!(config.get_execution_mode("python"), ExecutionMode::Stdin);

        // Test file-based execution mode
        assert_eq!(config.get_execution_mode("go"), ExecutionMode::File);
        assert_eq!(config.get_execution_mode("golang"), ExecutionMode::File);

        // Test arg-based execution mode
        assert_eq!(config.get_execution_mode("mq"), ExecutionMode::Arg);
    }

    #[test]
    fn test_runtime_config_simple() {
        let config = RuntimeConfig::Simple("python3".to_string());
        assert_eq!(config.command(), "python3");
        assert_eq!(config.execution_mode(), ExecutionMode::Stdin);
    }

    #[test]
    fn test_runtime_config_detailed() {
        let config = RuntimeConfig::Detailed {
            command: "go run".to_string(),
            execution_mode: ExecutionMode::File,
        };
        assert_eq!(config.command(), "go run");
        assert_eq!(config.execution_mode(), ExecutionMode::File);
    }

    #[test]
    fn test_toml_deserialization_simple() {
        let toml = r#"
[runtimes]
python = "python3"
"#;
        let config: Config = toml::from_str(toml).unwrap();
        assert_eq!(config.get_runtime("python"), Some("python3"));
        assert_eq!(config.get_execution_mode("python"), ExecutionMode::Stdin);
    }

    #[test]
    fn test_toml_deserialization_detailed() {
        let toml = r#"
[runtimes.go]
command = "go run"
execution_mode = "file"
"#;
        let config: Config = toml::from_str(toml).unwrap();
        assert_eq!(config.get_runtime("go"), Some("go run"));
        assert_eq!(config.get_execution_mode("go"), ExecutionMode::File);
    }

    #[test]
    fn test_toml_deserialization_mixed() {
        let toml = r#"
[runtimes]
python = "python3"

[runtimes.go]
command = "go run"
execution_mode = "file"

[runtimes.mq]
command = "mq"
execution_mode = "arg"
"#;
        let config: Config = toml::from_str(toml).unwrap();

        // Simple config
        assert_eq!(config.get_runtime("python"), Some("python3"));
        assert_eq!(config.get_execution_mode("python"), ExecutionMode::Stdin);

        // Detailed config with file mode
        assert_eq!(config.get_runtime("go"), Some("go run"));
        assert_eq!(config.get_execution_mode("go"), ExecutionMode::File);

        // Detailed config with arg mode
        assert_eq!(config.get_runtime("mq"), Some("mq"));
        assert_eq!(config.get_execution_mode("mq"), ExecutionMode::Arg);
    }
}
```

## File: `src/error.rs`
```rust
//! Error types for mq_task

use thiserror::Error;

/// Result type for mq_task operations
pub type Result<T> = std::result::Result<T, Error>;

/// Error types for mq_task operations
#[derive(Error, Debug)]
pub enum Error {
    /// Error reading or parsing Markdown file
    #[error("Markdown error: {0}")]
    Markdown(String),

    /// Error executing mq query
    #[error("Query error: {0}")]
    Query(String),

    /// Error executing code block
    #[error("Execution error: {0}")]
    Execution(String),

    /// Configuration error
    #[error("Config error: {0}")]
    Config(String),

    /// IO error
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    /// TOML parsing error
    #[error("TOML parse error: {0}")]
    TomlParse(#[from] toml::de::Error),

    /// Section not found
    #[error("Section not found: {0}")]
    SectionNotFound(String),

    /// Runtime not found
    #[error("Runtime not found for language: {0}")]
    RuntimeNotFound(String),
}
```

## File: `src/lib.rs`
```rust
//! mq_task - Markdown-based task runner
//!
//! mq_task is a task runner that executes code blocks in Markdown files based on section titles.
//! It uses mq query language to parse and extract sections from Markdown documents.

pub mod config;
pub mod error;
pub mod runner;
pub mod tui;

pub use config::{Config, ExecutionMode};
pub use error::{Error, Result};
pub use runner::Runner;
```

## File: `src/main.rs`
```rust
//! mq_task - Markdown-based task runner CLI

use clap::{Parser, Subcommand};
use colored::*;
use miette::{IntoDiagnostic, Result};
use std::path::PathBuf;

use mq_task::{Config, ExecutionMode, Runner};

const DEFAULT_TASKS_FILE: &str = "README.md";

#[derive(Parser)]
#[command(name = "mq_task")]
#[command(about = "Markdown-based task runner", long_about = None)]
#[command(version)]
struct Cli {
    /// Task name to execute (shorthand for 'run' command)
    #[arg(value_name = "TASK")]
    task: Option<String>,

    /// Path to the markdown file
    #[arg(short, long, default_value = DEFAULT_TASKS_FILE)]
    file: PathBuf,

    /// Path to configuration file
    #[arg(short, long)]
    config: Option<PathBuf>,

    /// Override runtime for a language (format: lang:command, e.g., python:python3.11)
    #[arg(short, long, value_name = "LANG:COMMAND")]
    runtime: Vec<String>,

    /// Set execution mode for runtime overrides (stdin, file, arg)
    #[arg(short, long, value_name = "MODE")]
    execution_mode: Option<String>,

    /// Filter code blocks by language (e.g., bash, python, go)
    #[arg(long, value_name = "LANG")]
    lang: Option<String>,

    /// Show what would be executed without actually running it
    #[arg(long)]
    dry_run: bool,

    /// Arguments to pass to the task (use -- to separate: mq_task task -- arg1 arg2)
    #[arg(last = true)]
    args: Vec<String>,

    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Run a task from a markdown file
    Run {
        /// Task name (section title) to execute
        task: String,

        /// Path to the markdown file
        #[arg(short, long, default_value = DEFAULT_TASKS_FILE)]
        file: PathBuf,

        /// Path to configuration file
        #[arg(short, long)]
        config: Option<PathBuf>,

        /// Override runtime for a language (format: lang:command, e.g., python:python3.11)
        #[arg(short, long, value_name = "LANG:COMMAND")]
        runtime: Vec<String>,

        /// Set execution mode for runtime overrides (stdin, file, arg)
        #[arg(short, long, value_name = "MODE")]
        execution_mode: Option<String>,

        /// Filter code blocks by language (e.g., bash, python, go)
        #[arg(long, value_name = "LANG")]
        lang: Option<String>,

        /// Show what would be executed without actually running it
        #[arg(long)]
        dry_run: bool,

        /// Arguments to pass to the task (use -- to separate: mq_task run task -- arg1 arg2)
        #[arg(last = true)]
        args: Vec<String>,
    },

    /// List all available tasks in a markdown file
    List {
        /// Path to the markdown file
        #[arg(short, long, default_value = DEFAULT_TASKS_FILE)]
        file: PathBuf,

        /// Path to configuration file
        #[arg(short, long)]
        config: Option<PathBuf>,

        /// Filter code blocks by language (e.g., bash, python, go)
        #[arg(long, value_name = "LANG")]
        lang: Option<String>,
    },

    /// Interactively select and run a task using TUI
    Tui {
        /// Path to the markdown file
        #[arg(short, long, default_value = DEFAULT_TASKS_FILE)]
        file: PathBuf,

        /// Path to configuration file
        #[arg(short, long)]
        config: Option<PathBuf>,

        /// Filter code blocks by language (e.g., bash, python, go)
        #[arg(long, value_name = "LANG")]
        lang: Option<String>,

        /// Show what would be executed without actually running it
        #[arg(long)]
        dry_run: bool,
    },

    /// Generate a sample configuration file
    Init {
        /// Output path for configuration file
        #[arg(short, long, default_value = "mq_task.toml")]
        output: PathBuf,
    },
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        Some(Commands::Run {
            file,
            task,
            config,
            runtime,
            execution_mode,
            lang,
            dry_run,
            args,
        }) => run_task(file, task, config, runtime, execution_mode, lang, dry_run, args)?,
        Some(Commands::List { file, config, lang }) => list_tasks(file, config, lang)?,
        Some(Commands::Tui {
            file,
            config,
            lang,
            dry_run,
        }) => run_tui(file, config, lang, dry_run)?,
        Some(Commands::Init { output }) => init_config(output)?,
        None => {
            // If no subcommand, check if task is provided
            if let Some(task) = cli.task {
                run_task(
                    cli.file,
                    task,
                    cli.config,
                    cli.runtime,
                    cli.execution_mode,
                    cli.lang,
                    cli.dry_run,
                    cli.args,
                )?;
            } else {
                // No task provided, list available tasks
                list_tasks(cli.file, cli.config, cli.lang)?;
            }
        }
    }

    Ok(())
}

/// Run a specific task
#[allow(clippy::too_many_arguments)]
fn run_task(
    markdown_path: PathBuf,
    task_name: String,
    config_path: Option<PathBuf>,
    runtime_overrides: Vec<String>,
    execution_mode: Option<String>,
    lang_filter: Option<String>,
    dry_run: bool,
    args: Vec<String>,
) -> Result<()> {
    let mut config = load_config(config_path)?;

    // Parse execution mode if specified
    let exec_mode = if let Some(mode_str) = execution_mode {
        Some(ExecutionMode::try_from(mode_str.as_str()).into_diagnostic()?)
    } else {
        None
    };

    // Apply runtime overrides
    if !runtime_overrides.is_empty() {
        config
            .apply_runtime_overrides(&runtime_overrides, exec_mode)
            .into_diagnostic()?;
    }

    let mut runner = Runner::new(config);
    runner.set_dry_run(dry_run);

    println!("Running task: {}\n", task_name);

    runner
        .run_task_with_lang_filter(&markdown_path, &task_name, &args, lang_filter.as_deref())
        .into_diagnostic()?;

    Ok(())
}

/// Launch the interactive TUI for task selection
fn run_tui(
    markdown_path: PathBuf,
    config_path: Option<PathBuf>,
    lang_filter: Option<String>,
    dry_run: bool,
) -> Result<()> {
    let config = load_config(config_path)?;
    mq_task::tui::run_tui(markdown_path, config, lang_filter, dry_run).into_diagnostic()?;
    Ok(())
}

/// List all available tasks
fn list_tasks(
    markdown_path: PathBuf,
    config_path: Option<PathBuf>,
    lang_filter: Option<String>,
) -> Result<()> {
    let config = load_config(config_path)?;
    let mut runner = Runner::new(config);

    let sections = runner
        .list_task_sections(&markdown_path)
        .into_diagnostic()?;

    // Filter sections by language if specified
    let filtered_sections: Vec<_> = if let Some(ref lang) = lang_filter {
        sections
            .into_iter()
            .filter(|section| section.codes.iter().any(|code| code.lang == *lang))
            .collect()
    } else {
        sections
    };

    if filtered_sections.is_empty() {
        if let Some(ref lang) = lang_filter {
            println!(
                "{}",
                format!(
                    "No tasks found with language '{}' in {}",
                    lang,
                    markdown_path.display()
                )
                .yellow()
            );
        } else {
            println!(
                "{}",
                format!("No tasks found in {}", markdown_path.display()).yellow()
            );
        }
        return Ok(());
    }

    let mut output = String::new();
    output.push_str(&format!(
        "{} {}{}\n\n",
        "Available tasks in".bold(),
        markdown_path.display().to_string().cyan(),
        if let Some(ref lang) = lang_filter {
            format!(" {}", format!("(language: {})", lang).bright_black())
        } else {
            String::new()
        }
    ));

    for section in filtered_sections {
        // Show language information if filtering is active
        let lang_info = if lang_filter.is_some() {
            let langs: Vec<String> = section
                .codes
                .iter()
                .filter_map(|code| {
                    if let Some(ref filter) = lang_filter {
                        if code.lang == *filter {
                            Some(code.lang.clone())
                        } else {
                            None
                        }
                    } else {
                        Some(code.lang.clone())
                    }
                })
                .collect();

            if !langs.is_empty() {
                format!(" {}", format!("[{}]", langs.join(", ")).bright_black())
            } else {
                String::new()
            }
        } else {
            String::new()
        };

        if let Some(desc) = section.description {
            let trimmed = desc.trim();
            if !trimmed.is_empty() {
                output.push_str(&format!(
                    "  {}{} {}\n",
                    section.title.green().bold(),
                    lang_info,
                    format!("- {}", trimmed).bright_black()
                ));
            } else {
                output.push_str(&format!(
                    "  {}{}\n",
                    section.title.green().bold(),
                    lang_info
                ));
            }
        } else {
            output.push_str(&format!(
                "  {}{}\n",
                section.title.green().bold(),
                lang_info
            ));
        }
    }

    print!("{}", output);

    Ok(())
}

/// Initialize configuration file
fn init_config(output_path: PathBuf) -> Result<()> {
    if output_path.exists() {
        return Err(miette::miette!(
            "Configuration file already exists: {}",
            output_path.display()
        ));
    }

    let config = Config::default();
    let toml = toml::to_string_pretty(&config).into_diagnostic()?;

    std::fs::write(&output_path, toml).into_diagnostic()?;
    println!("Configuration file created: {}", output_path.display());

    Ok(())
}

/// Load configuration from file or use default
fn load_config(config_path: Option<PathBuf>) -> Result<Config> {
    let config = if let Some(path) = config_path {
        Config::from_file(&path).into_diagnostic()?
    } else {
        Config::default()
    };

    Ok(config)
}
```

## File: `src/runner.rs`
```rust
use std::collections::BTreeMap;
use std::fs;
use std::io::Write;
use std::path::Path;
use std::process::{Command, Stdio};

use mq_lang::{Engine, Ident, RuntimeValue, parse_markdown_input};
use serde::{Deserialize, Serialize};

use crate::config::{Config, ExecutionMode};
use crate::error::{Error, Result};

const SECTIONS_QUERY: &str = include_str!("../sections.mq");

/// Represents a code block in a section
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct CodeBlock {
    /// Language of the code block
    pub lang: String,
    /// Code content
    pub code: String,
}

/// Represents a section with its code blocks
#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Section {
    /// Section title
    pub title: String,
    /// Code blocks in this section
    pub codes: Vec<CodeBlock>,
    /// Optional description extracted from the section content
    pub description: Option<String>,
}

/// Task runner that executes code blocks in Markdown sections
pub struct Runner {
    config: Config,
    engine: Engine,
    dry_run: bool,
}

impl Runner {
    /// Create a new Runner with the given configuration
    pub fn new(config: Config) -> Self {
        let mut engine: Engine = Engine::default();
        engine.load_builtin_module();

        Self {
            config,
            engine,
            dry_run: false,
        }
    }

    /// Create a new Runner with default configuration
    pub fn with_default_config() -> Self {
        Self::new(Config::default())
    }

    /// Enable or disable dry-run mode
    pub fn set_dry_run(&mut self, dry_run: bool) {
        self.dry_run = dry_run;
    }

    /// Load and parse a Markdown file
    pub fn load_markdown<P: AsRef<Path>>(&self, path: P) -> Result<String> {
        fs::read_to_string(path).map_err(Error::Io)
    }

    /// Extract sections from Markdown content
    pub fn extract_sections(&mut self, markdown: &str) -> Result<Vec<Section>> {
        let input = parse_markdown_input(markdown)
            .map_err(|e| Error::Markdown(format!("Failed to parse markdown: {}", e)))?;

        let query = format!("{}\n | nodes | sections_with_code()", SECTIONS_QUERY);
        let result = self
            .engine
            .eval(&query, input.into_iter())
            .map_err(|e| Error::Query(format!("Failed to execute query: {}", e)))?;

        let sections = self.parse_sections(result)?;

        Ok(sections)
    }

    fn parse_sections(&self, result: mq_lang::RuntimeValues) -> Result<Vec<Section>> {
        let mut sections = Vec::new();

        for value in result.into_iter() {
            if let RuntimeValue::Dict(dict) = value {
                let section = self.parse_section(&dict)?;
                sections.push(section);
            }
        }

        Ok(sections)
    }

    fn parse_section(&self, dict: &BTreeMap<Ident, RuntimeValue>) -> Result<Section> {
        let title = dict
            .get(&Ident::from("title"))
            .and_then(|v| match v {
                RuntimeValue::String(s) => Some(s.to_string()),
                _ => None,
            })
            .unwrap_or_default();

        let codes = dict
            .get(&Ident::from("codes"))
            .and_then(|v| match v {
                RuntimeValue::Array(arr) => Some(self.parse_code_blocks(arr)),
                _ => None,
            })
            .unwrap_or_else(|| Ok(Vec::new()))?;

        let description = dict.get(&Ident::from("description")).and_then(|v| match v {
            RuntimeValue::String(s) => Some(s.to_string()),
            _ => None,
        });

        Ok(Section {
            title,
            codes,
            description,
        })
    }

    fn parse_code_blocks(&self, arr: &[RuntimeValue]) -> Result<Vec<CodeBlock>> {
        let mut blocks = Vec::new();

        for item in arr {
            if let RuntimeValue::Dict(dict) = item {
                let lang = dict
                    .get(&Ident::from("lang"))
                    .and_then(|v| match v {
                        RuntimeValue::String(s) => Some(s.to_string()),
                        _ => None,
                    })
                    .unwrap_or_default();

                let code = dict
                    .get(&Ident::from("code"))
                    .and_then(|v| match v {
                        RuntimeValue::String(s) => Some(s.to_string()),
                        _ => None,
                    })
                    .unwrap_or_default();

                blocks.push(CodeBlock { lang, code });
            }
        }

        Ok(blocks)
    }

    pub fn find_section<'a>(&self, sections: &'a [Section], title: &str) -> Option<&'a Section> {
        sections.iter().find(|s| s.title == title)
    }

    pub fn execute_section(&self, section: &Section) -> Result<()> {
        self.execute_section_with_args(section, &[])
    }

    pub fn execute_section_with_args(&self, section: &Section, args: &[String]) -> Result<()> {
        self.execute_section_with_lang_filter(section, args, None)
    }

    pub fn execute_section_with_lang_filter(
        &self,
        section: &Section,
        args: &[String],
        lang_filter: Option<&str>,
    ) -> Result<()> {
        for code_block in &section.codes {
            if code_block.lang.is_empty() {
                continue;
            }

            // Apply language filter if specified
            if let Some(filter) = lang_filter
                && code_block.lang != filter
            {
                continue;
            }

            self.execute_code_with_args(&code_block.lang, &code_block.code, args)?;
        }

        Ok(())
    }

    pub fn execute_code(&self, lang: &str, code: &str) -> Result<()> {
        self.execute_code_with_args(lang, code, &[])
    }

    pub fn execute_code_with_args(&self, lang: &str, code: &str, args: &[String]) -> Result<()> {
        let runtime = self
            .config
            .get_runtime(lang)
            .ok_or_else(|| Error::RuntimeNotFound(lang.to_string()))?;

        let parts: Vec<&str> = runtime.split_whitespace().collect();
        if parts.is_empty() {
            return Err(Error::RuntimeNotFound(lang.to_string()));
        }

        // Get execution mode from config
        let execution_mode = self.config.get_execution_mode(lang);

        if self.dry_run {
            let args_line = if !args.is_empty() {
                format!("\n[dry-run] args: {}", args.join(" "))
            } else {
                String::new()
            };
            println!(
                "[dry-run] lang: {}\n[dry-run] runtime: {}\n[dry-run] code:\n{}{}",
                lang, runtime, code, args_line
            );
            return Ok(());
        }

        match execution_mode {
            ExecutionMode::File => self.execute_code_with_file_and_args(lang, code, &parts, args),
            ExecutionMode::Arg => self.execute_code_with_arg_mode(code, &parts, args),
            ExecutionMode::Stdin => self.execute_code_with_stdin_and_args(code, &parts, args),
        }
    }

    fn execute_code_with_stdin_and_args(
        &self,
        code: &str,
        parts: &[&str],
        task_args: &[String],
    ) -> Result<()> {
        let cmd = parts[0];
        let args = &parts[1..];

        // Use inherit() for stdout/stderr to preserve TTY and colors
        let mut child = Command::new(cmd)
            .args(args)
            .stdin(Stdio::piped())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .envs(Self::prepare_env_vars(task_args))
            .spawn()
            .map_err(|e| Error::Execution(format!("Failed to spawn process: {}", e)))?;

        // Write code to stdin
        if let Some(mut stdin) = child.stdin.take() {
            stdin
                .write_all(code.as_bytes())
                .map_err(|e| Error::Execution(format!("Failed to write to stdin: {}", e)))?;
            drop(stdin);
        }

        // Wait for completion
        let status = child
            .wait()
            .map_err(|e| Error::Execution(format!("Failed to wait for process: {}", e)))?;

        if !status.success() {
            return Err(Error::Execution("Execution failed".to_string()));
        }

        Ok(())
    }

    fn execute_code_with_arg_mode(
        &self,
        code: &str,
        parts: &[&str],
        task_args: &[String],
    ) -> Result<()> {
        let cmd = parts[0];
        // Append code as an argument to the command
        let mut args: Vec<&str> = parts[1..].to_vec();
        args.push(code);

        // Use inherit() for stdout/stderr to preserve TTY and colors
        let mut child = Command::new(cmd)
            .args(args)
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .envs(Self::prepare_env_vars(task_args))
            .spawn()
            .map_err(|e| Error::Execution(format!("Failed to spawn process: {}", e)))?;

        // Write code to stdin
        if let Some(mut stdin) = child.stdin.take() {
            stdin
                .write_all(code.as_bytes())
                .map_err(|e| Error::Execution(format!("Failed to write to stdin: {}", e)))?;
            drop(stdin);
        }

        // Wait for completion
        let status = child
            .wait()
            .map_err(|e| Error::Execution(format!("Failed to wait for process: {}", e)))?;

        if !status.success() {
            return Err(Error::Execution("Execution failed".to_string()));
        }

        Ok(())
    }

    fn execute_code_with_file_and_args(
        &self,
        lang: &str,
        code: &str,
        parts: &[&str],
        task_args: &[String],
    ) -> Result<()> {
        use std::env;

        // Create temporary directory
        let temp_dir = env::temp_dir();

        // Use language name as file extension, or map known languages
        let file_ext = match lang {
            "go" | "golang" => "go",
            "python" => "py",
            "ruby" => "rb",
            "javascript" | "js" => "js",
            "typescript" | "ts" => "ts",
            _ => lang, // Use language name as extension for custom languages
        };

        // Generate unique file name
        let timestamp = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let file_name = format!("mx_temp_{}.{}", timestamp, file_ext);
        let temp_file = temp_dir.join(&file_name);

        // Write code to temporary file
        fs::write(&temp_file, code)
            .map_err(|e| Error::Execution(format!("Failed to write temp file: {}", e)))?;

        // Execute go run <file>
        let status = Command::new(parts[0])
            .args(&parts[1..])
            .arg(&temp_file)
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .envs(Self::prepare_env_vars(task_args))
            .status()
            .map_err(|e| Error::Execution(format!("Failed to execute {}: {}", lang, e)))?;

        // Clean up temporary file
        fs::remove_file(&temp_file).ok();

        if !status.success() {
            Err(Error::Execution(format!("{} execution failed", lang)))
        } else {
            Ok(())
        }
    }

    /// Prepare environment variables from task arguments
    fn prepare_env_vars(args: &[String]) -> Vec<(String, String)> {
        let mut env_vars = Vec::new();

        // Set MX_ARGS with all arguments joined by space
        if !args.is_empty() {
            env_vars.push(("MX_ARGS".to_string(), args.join(" ")));
        }

        // Set individual arguments as MX_ARG_0, MX_ARG_1, etc.
        for (i, arg) in args.iter().enumerate() {
            env_vars.push((format!("MX_ARG_{}", i), arg.clone()));
        }

        env_vars
    }

    /// Run a specific task by section title
    pub fn run_task<P: AsRef<Path>>(&mut self, markdown_path: P, task_name: &str) -> Result<()> {
        self.run_task_with_args(markdown_path, task_name, &[])
    }

    /// Run a specific task with arguments
    pub fn run_task_with_args<P: AsRef<Path>>(
        &mut self,
        markdown_path: P,
        task_name: &str,
        args: &[String],
    ) -> Result<()> {
        self.run_task_with_lang_filter(markdown_path, task_name, args, None)
    }

    /// Run a specific task with arguments and language filter
    pub fn run_task_with_lang_filter<P: AsRef<Path>>(
        &mut self,
        markdown_path: P,
        task_name: &str,
        args: &[String],
        lang_filter: Option<&str>,
    ) -> Result<()> {
        let markdown = self.load_markdown(markdown_path)?;
        let sections = self.extract_sections(&markdown)?;

        let section = self
            .find_section(&sections, task_name)
            .ok_or_else(|| Error::SectionNotFound(task_name.to_string()))?;

        self.execute_section_with_lang_filter(section, args, lang_filter)
    }

    /// List all available tasks (sections) in a Markdown file
    pub fn list_tasks<P: AsRef<Path>>(&mut self, markdown_path: P) -> Result<Vec<String>> {
        let markdown = self.load_markdown(markdown_path)?;
        let sections = self.extract_sections(&markdown)?;

        Ok(sections
            .into_iter()
            .map(|s| format!("{}: {}", s.title, s.description.unwrap_or_default()))
            .collect())
    }

    /// List all available task sections in a Markdown file with their details
    pub fn list_task_sections<P: AsRef<Path>>(&mut self, markdown_path: P) -> Result<Vec<Section>> {
        let markdown = self.load_markdown(markdown_path)?;
        self.extract_sections(&markdown)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_extract_sections() {
        let markdown = r#"# Title

## Task 1

```bash
echo "hello"
```

## Task 2

```python
print("world")
```
"#;

        let mut runner = Runner::with_default_config();
        let sections = runner.extract_sections(markdown).unwrap();

        assert_eq!(sections.len(), 3);
        assert_eq!(sections[1].title, "Task 1");
        assert_eq!(sections[1].codes.len(), 1);
        assert_eq!(sections[1].codes[0].lang, "bash");
    }

    #[test]
    fn test_find_section() {
        let sections = vec![
            Section {
                title: "Task 1".to_string(),
                ..Default::default()
            },
            Section {
                title: "Task 2".to_string(),
                ..Default::default()
            },
        ];

        let runner = Runner::with_default_config();
        let found = runner.find_section(&sections, "Task 1");
        assert!(found.is_some());
        assert_eq!(found.unwrap().title, "Task 1");

        let not_found = runner.find_section(&sections, "Task 3");
        assert!(not_found.is_none());
    }

    #[test]
    fn test_language_filter() {
        let section = Section {
            title: "Mixed Task".to_string(),
            codes: vec![
                CodeBlock {
                    lang: "bash".to_string(),
                    code: "echo 'bash code'".to_string(),
                },
                CodeBlock {
                    lang: "python".to_string(),
                    code: "print('python code')".to_string(),
                },
                CodeBlock {
                    lang: "bash".to_string(),
                    code: "echo 'more bash'".to_string(),
                },
            ],
            description: None,
        };

        let runner = Runner::with_default_config();

        // Test filtering for bash only - this will fail if bash is not available,
        // but demonstrates the filtering logic
        let result = runner.execute_section_with_lang_filter(&section, &[], Some("bash"));
        // We can't guarantee bash is available in test environment, so we just check
        // that the method runs without panicking
        let _ = result;
    }

    #[test]
    fn test_extract_sections_with_multiple_languages() {
        let markdown = r#"# Title

## Mixed Task

```bash
echo "bash code"
```

```python
print("python code")
```

```bash
echo "more bash"
```
"#;

        let mut runner = Runner::with_default_config();
        let sections = runner.extract_sections(markdown).unwrap();

        assert_eq!(sections.len(), 2);
        assert_eq!(sections[1].title, "Mixed Task");
        assert_eq!(sections[1].codes.len(), 3);
        assert_eq!(sections[1].codes[0].lang, "bash");
        assert_eq!(sections[1].codes[1].lang, "python");
        assert_eq!(sections[1].codes[2].lang, "bash");
    }
}
```

## File: `src/tui.rs`
```rust
//! Interactive TUI for task selection and execution

use std::io;
use std::path::PathBuf;

use crossterm::{
    event::{self, DisableMouseCapture, EnableMouseCapture, Event, KeyCode, KeyEventKind},
    execute,
    terminal::{EnterAlternateScreen, LeaveAlternateScreen, disable_raw_mode, enable_raw_mode},
};
use ratatui::{
    Terminal,
    backend::CrosstermBackend,
    layout::{Constraint, Direction, Layout},
    style::{Color, Modifier, Style},
    text::{Line, Span},
    widgets::{Block, Borders, List, ListItem, ListState, Paragraph},
};

use crate::runner::Section;
use crate::{Config, Runner};

struct App {
    sections: Vec<Section>,
    list_state: ListState,
}

impl App {
    fn new(sections: Vec<Section>) -> Self {
        let mut list_state = ListState::default();
        if !sections.is_empty() {
            list_state.select(Some(0));
        }
        Self {
            sections,
            list_state,
        }
    }

    fn next(&mut self) {
        if self.sections.is_empty() {
            return;
        }
        let i = match self.list_state.selected() {
            Some(i) => (i + 1) % self.sections.len(),
            None => 0,
        };
        self.list_state.select(Some(i));
    }

    fn previous(&mut self) {
        if self.sections.is_empty() {
            return;
        }
        let i = match self.list_state.selected() {
            Some(i) => {
                if i == 0 {
                    self.sections.len() - 1
                } else {
                    i - 1
                }
            }
            None => 0,
        };
        self.list_state.select(Some(i));
    }

    fn selected_section(&self) -> Option<&Section> {
        self.list_state
            .selected()
            .and_then(|i| self.sections.get(i))
    }
}

/// Run the interactive TUI for task selection
pub fn run_tui(
    markdown_path: PathBuf,
    config: Config,
    lang_filter: Option<String>,
    dry_run: bool,
) -> crate::error::Result<()> {
    let mut runner = Runner::new(config.clone());
    runner.set_dry_run(dry_run);

    let sections = {
        let mut r = Runner::new(config);
        let raw_sections = r.list_task_sections(&markdown_path)?;

        // Apply language filter if specified
        if let Some(ref lang) = lang_filter {
            raw_sections
                .into_iter()
                .filter(|s| s.codes.iter().any(|c| c.lang == *lang))
                .collect()
        } else {
            raw_sections
        }
    };

    // Setup terminal
    enable_raw_mode().map_err(crate::error::Error::Io)?;
    let mut stdout = io::stdout();
    execute!(stdout, EnterAlternateScreen, EnableMouseCapture).map_err(crate::error::Error::Io)?;
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend).map_err(crate::error::Error::Io)?;

    let mut app = App::new(sections);
    let result = run_app(&mut terminal, &mut app);

    // Restore terminal
    disable_raw_mode().map_err(crate::error::Error::Io)?;
    execute!(
        terminal.backend_mut(),
        LeaveAlternateScreen,
        DisableMouseCapture
    )
    .map_err(crate::error::Error::Io)?;
    terminal.show_cursor().map_err(crate::error::Error::Io)?;

    // Execute selected task if any
    if let Some(task_name) = result? {
        println!("Running task: {}\n", task_name);
        runner.run_task_with_lang_filter(
            &markdown_path,
            &task_name,
            &[],
            lang_filter.as_deref(),
        )?;
    }

    Ok(())
}

fn run_app<B: ratatui::backend::Backend>(
    terminal: &mut Terminal<B>,
    app: &mut App,
) -> crate::error::Result<Option<String>> {
    loop {
        terminal.draw(|f| ui(f, app)).expect("Failed to draw TUI");

        if let Event::Key(key) = event::read().map_err(crate::error::Error::Io)? {
            if key.kind != KeyEventKind::Press {
                continue;
            }
            match key.code {
                KeyCode::Char('q') | KeyCode::Esc => return Ok(None),
                KeyCode::Down | KeyCode::Char('j') => app.next(),
                KeyCode::Up | KeyCode::Char('k') => app.previous(),
                KeyCode::Enter => {
                    if let Some(section) = app.selected_section() {
                        return Ok(Some(section.title.clone()));
                    }
                }
                _ => {}
            }
        }
    }
}

fn ui(f: &mut ratatui::Frame, app: &mut App) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Min(3), Constraint::Length(3)])
        .split(f.area());

    let items: Vec<ListItem> = app
        .sections
        .iter()
        .map(|s| {
            let content = if let Some(ref desc) = s.description {
                let trimmed = desc.trim();
                if !trimmed.is_empty() {
                    Line::from(vec![
                        Span::styled(
                            s.title.clone(),
                            Style::default()
                                .fg(Color::Green)
                                .add_modifier(Modifier::BOLD),
                        ),
                        Span::raw(" - "),
                        Span::styled(trimmed.to_string(), Style::default().fg(Color::DarkGray)),
                    ])
                } else {
                    Line::from(Span::styled(
                        s.title.clone(),
                        Style::default()
                            .fg(Color::Green)
                            .add_modifier(Modifier::BOLD),
                    ))
                }
            } else {
                Line::from(Span::styled(
                    s.title.clone(),
                    Style::default()
                        .fg(Color::Green)
                        .add_modifier(Modifier::BOLD),
                ))
            };
            ListItem::new(content)
        })
        .collect();

    let list = List::new(items)
        .block(Block::default().borders(Borders::ALL).title(" Tasks "))
        .highlight_style(
            Style::default()
                .bg(Color::DarkGray)
                .add_modifier(Modifier::BOLD),
        )
        .highlight_symbol("▶ ");

    f.render_stateful_widget(list, chunks[0], &mut app.list_state);

    let help = Paragraph::new("↑/↓ or j/k: navigate   Enter: run   q/Esc: quit")
        .style(Style::default().fg(Color::DarkGray))
        .block(Block::default().borders(Borders::ALL).title(" Help "));

    f.render_widget(help, chunks[1]);
}
```

## File: `tests/integration_test.rs`
```rust
use mq_task::{Config, Runner};
use std::fs;

#[test]
fn test_list_tasks() {
    let markdown = r#"# Test Document

## Task 1

```bash
echo "hello"
```

## Task 2

```python
print("world")
```
"#;

    let temp_dir = std::env::temp_dir();
    let test_file = temp_dir.join("test_list_tasks.md");
    fs::write(&test_file, markdown).unwrap();

    let config = Config::default();
    let mut runner = Runner::new(config);

    let tasks = runner.list_tasks(&test_file).unwrap();

    assert_eq!(tasks.len(), 3);
    assert_eq!(tasks[0], "Test Document: ");
    assert_eq!(tasks[1], "Task 1: ");
    assert_eq!(tasks[2], "Task 2: ");

    fs::remove_file(test_file).unwrap();
}

#[test]
fn test_extract_sections() {
    let markdown = r#"# Test Document

## Build

```bash
echo "building..."
```

## Test

```bash
echo "testing..."
```
"#;

    let config = Config::default();
    let mut runner = Runner::new(config);

    let sections = runner.extract_sections(markdown).unwrap();

    assert_eq!(sections.len(), 3);
    assert_eq!(sections[0].title, "Test Document");
    assert_eq!(sections[1].title, "Build");
    assert_eq!(sections[2].title, "Test");
}

#[test]
fn test_execute_bash() {
    let config = Config::default();
    let runner = Runner::new(config);

    let code = r#"echo "hello from bash""#;
    // Output is displayed in real-time, so we just check that execution succeeds
    runner.execute_code("bash", code).unwrap();
}
```


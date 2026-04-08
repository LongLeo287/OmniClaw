# Deep Matrix Profile: FETCHED_agent-skills_043028

# Deep Knowledge Report for ClickHouse Best Practices Repository

## Overview

This repository provides 'Agent Skills' to enhance AI coding agents with domain-specific best practices for using ClickHouse databases. The skills are packaged as rules that help LLMs and agents write optimized queries, design schemas, and manage data ingestion according to ClickHouse best practices.

### Core Components

1. **Build Script (`build.ts`)**: Compiles individual rule files into a single `AGENTS.md` document.
2. **Link Validation Scripts**:
   - **Internal Links Check (`check-links.ts`)**: Ensures internal links within the rules are valid and point to existing files.
   - **External Link Validation (`check-external-links.ts`)**: Validates external HTTP/HTTPS links in skill files for broken or invalid URLs.
3. **SQL Syntax Validation (`validate-sql.ts`)**: Uses ClickHouse binary to validate SQL syntax in rule examples.
4. **Rule Parsing and Validation (`parser.ts`, `validate.ts`)**: Parses rule markdown files into structured objects, validates the structure of rules, and ensures compliance with best practices.

## Architectural Patterns

### Modular Design
The repository is designed using a modular approach, where each script handles specific tasks:
- **Build Script**: Compiles all rules into a single document.
- **Link Validation Scripts**: Ensure that links within the documents are valid.
- **SQL Syntax Validation**: Validates SQL syntax in examples.

### Dependency Injection and Configuration Management
Configuration settings such as paths to rule files, metadata file, and output file are managed through `config.ts`. This allows for easy modification of paths without changing the core logic.

## Core Algorithms

### Build Process (`build.ts`)
1. **Read Rule Files**: Uses `fs/promises` to read all `.md` files in the rules directory.
2. **Parse Rules**: Utilizes a custom parser to extract metadata and rule content from each file.
3. **Generate Markdown**: Constructs a structured markdown document by iterating through sections, rules, and their respective impacts.

### Link Validation (`check-links.ts`, `check-external-links.ts`)
1. **Internal Links Check**:
   - Extracts links using regular expressions.
   - Checks if the referenced files exist in the directory.
2. **External Link Validation**:
   - Uses `fs/promises` to read and validate external URLs asynchronously with retry logic.

### SQL Syntax Validation (`validate-sql.ts`)
1. **Download ClickHouse Binary**: Ensures the binary is available for validation, downloading it if necessary.
2. **Validate Examples**: Executes each example using the ClickHouse binary and checks for syntax errors or dangerous patterns.

## Primary Mechanisms

### Rule Parsing
- **Parser Functionality**:
  - Reads rule files and extracts metadata such as version, organization, date, etc.
  - Parses rules into structured objects with fields like `id`, `title`, `impact`, `explanation`, `examples`, `references`.
- **Validation Rules**:
  - Ensures each rule has a title, explanation, and at least one example.
  - Validates the impact level to ensure it is one of predefined values.

### Link Validation
- **Internal Links**: Checks if referenced files exist in the directory.
- **External Links**: Uses HTTP requests with retry logic to validate external URLs.

### SQL Syntax Validation
- **Binary Download**: Ensures ClickHouse binary is available for validation.
- **Syntax Check**: Executes each example using the ClickHouse binary and checks for syntax errors or dangerous patterns.

## Conclusion

The repository's architecture is modular, making it easy to extend or modify individual components. The use of configuration management ensures flexibility in path settings, while core algorithms ensure robustness in rule parsing, link validation, and SQL syntax checking. This structure supports the development of high-quality ClickHouse best practices for AI-driven coding agents.

---
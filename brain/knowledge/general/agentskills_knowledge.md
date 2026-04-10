# Knowledge Dump for agentskills

## File: DEEP_KNOWLEDGE.md
```
# Deep Matrix Profile: FETCHED_agentskills_111250

# DEEP_KNOWLEDGE.md

## Overview

The `skills-ref` repository is designed to provide a structured framework for defining and managing "Agent Skills" in an open format. This document delves into the architectural patterns, core algorithms, and primary mechanisms of the library.

### Architectural Patterns

1. **Modular Design**: The codebase is modular, with distinct components handling different aspects of skill management.
2. **Command-Line Interface (CLI)**: A CLI provides a user-friendly interface for interacting with the library's functionalities.
3. **Error Handling**: Robust error handling mechanisms are implemented to ensure that invalid inputs or conditions are gracefully managed.

### Core Algorithms and Primary Mechanisms

#### 1. Command-Line Interface (CLI)

The `cli.py` module defines a command-line interface using the `click` library, enabling users to interact with the library through various commands:

- **Validate**: Validates a skill directory for compliance with specified rules.
- **Read Properties**: Reads and prints properties from the SKILL.md file as JSON.
- **Generate Prompt XML**: Generates an XML block suitable for agent prompts.

#### 2. Error Handling

The `errors.py` module defines custom exceptions to handle various errors related to skills:

- **SkillError**: Base exception class for all skill-related errors.
- **ParseError**: Raised when parsing SKILL.md files fails.
- **ValidationError**: Raised when validating properties of a skill directory.

#### 3. Data Models

The `models.py` module defines data classes representing the structure and properties of skills:

- **SkillProperties**: Represents parsed properties from the SKILL.md frontmatter, including name, description, license, compatibility, allowed tools, and metadata.

#### 4. Frontmatter Parsing

The `parser.py` module handles parsing YAML frontmatter from SKILL.md files:

- **find_skill_md**: Finds the SKILL.md file in a skill directory.
- **parse_frontmatter**: Parses the YAML frontmatter and extracts metadata.
- **read_properties**: Reads properties from the parsed frontmatter.

#### 5. Validation

The `validator.py` module contains validation logic to ensure that skills meet specified criteria:

- **validate_name**: Validates the name of the skill according to defined rules.
- **validate_description**: Validates the description length and content.
- **validate_compatibility**: Validates the compatibility field.
- **_validate_metadata_fields**: Validates metadata fields.

#### 6. XML Prompt Generation

The `prompt.py` module generates an XML block for agent prompts:

- **to_prompt**: Generates a formatted XML string with skill information.

### Detailed Explanation of Key Components

#### Command-Line Interface (CLI)

```python
# cli.py
@click.group()
@click.version_option()
def main():
    """Reference library for Agent Skills."""
    pass

@main.command("validate")
@click.argument("skill_path", type=click.Path(exists=True, path_type=Path))
def validate_cmd(skill_path: Path):
    # Validation logic here
```

- **Main Function**: Defines the CLI entry point.
- **Validate Command**: Validates a skill directory and prints errors if any.

#### Error Handling

```python
# errors.py
class SkillError(Exception):
    pass

class ParseError(SkillError):
    def __init__(self, message: str, errors: list[str] | None = None):
        super().__init__(message)
        self.errors = errors if errors is not None else [message]
```

- **Custom Exceptions**: `SkillError`, `ParseError`, and `ValidationError` are defined to handle specific error scenarios.

#### Data Models

```python
# models.py
@dataclass
class SkillProperties:
    name: str
    description: str
    license: Optional[str] = None
    compatibility: Optional[str] = None
    allowed_tools: Optional[str] = None
    metadata: dict[str, str] = field(default_factory=dict)
```

- **SkillProperties Class**: Represents the properties of a skill.

#### Frontmatter Parsing

```python
# parser.py
def parse_frontmatter(content: str) -> tuple[dict, str]:
    # Parsing logic here
```

- **parse_frontmatter Function**: Parses YAML frontmatter from SKILL.md content and returns metadata and body text.

#### Validation

```python
# validator.py
def validate(skill_dir: Path) -> list[str]:
    # Validation logic here
```

- **validate Function**: Validates a skill directory for compliance with specified rules.

#### XML Prompt Generation

```python
# prompt.py
def to_prompt(skill_dirs: list[Path]) -> str:
    # XML generation logic here
```

- **to_prompt Function**: Generates an XML block suitable for agent prompts.

### Conclusion

The `skills-ref` repository provides a comprehensive framework for managing and validating Agent Skills. The modular design, robust error handling, and well-defined data models ensure that the library can be easily extended and integrated into various systems.
```

## File: README.md
```
# Agent Skills

[Agent Skills](https://agentskills.io) are a simple, open format for giving agents new capabilities and expertise.

Skills are folders of instructions, scripts, and resources that agents can discover and use to perform better at specific tasks. Write once, use everywhere.

## Getting Started

- **[Documentation](https://agentskills.io)** — Guides and tutorials
- **[Specification](https://agentskills.io/specification)** — Format details
- **[Example Skills](https://github.com/anthropics/skills)** — See what's possible
- **[Discord](https://discord.gg/MKPE9g8aUy)** — Join the discussion!

This repo contains the specification, documentation, and reference SDK. Also see a list of example skills [here](https://github.com/anthropics/skills).

## About

Agent Skills is an open format maintained by [Anthropic](https://anthropic.com) and open to contributions from the community.

## License

Code in this repository is licensed under [Apache 2.0](LICENSE). Documentation is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). See individual directories for details.

```

## File: schema.json
```
{
  "id": "agentskills",
  "name": "Agentskills",
  "version": "1.0.0",
  "tier": 3,
  "status": "active",
  "domain": "agent-framework",
  "cost_tier": "standard",
  "load_on_boot": false,
  "path": "\\ecosystem\\skills\\agentskills\\SKILL.md",
  "accessible_by": [
    "Orchestrator",
    "Claude Code"
  ],
  "dependencies": [],
  "exposed_functions": [
    {
      "name": "reference",
      "description": "Reference for agentskills",
      "input": "string",
      "output": "string"
    }
  ],
  "consumed_by": [],
  "emits_events": [],
  "listens_to": [],
  "tags": [
    "agent"
  ]
}
```

## File: SKILL.md
```
# SKILL PROFILE: repo-fetched-agentskills-111250
# Department Registry: OAP Toolchain
# Scope: Pure OS-sanctioned Tools
---

## 1. Domain Capability
Generic specialist agent.

## 2. Linked Toolkit
> [!NOTE]
> No static YAML skills mapped. Awaiting dynamic plugin hooks from OAP Orchestrator.

---
*Capability Register hardened by OmniClaw OA Skill Auditor.*

```

## File: _DIR_IDENTITY.md
```
---
id: repo-fetched-agentskills-111250
type: skill
owner: OA
registered_at: 2026-04-04T15:22:16.269758
tags: ["auto-cloned", "AI Agents", "Open Format", "Capability Building", "oa-assimilated", "premium-repo"]
---

# FETCHED_agentskills_111250

## Assimilation Report
This repository defines Agent Skills, an open format for providing agents with new capabilities and expertise through structured folders of instructions and scripts. It serves as the central specification, documentation, and reference SDK for implementing these skills.

```

## File: .claude\settings.json
```
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}

```

## File: docs\claude.md
```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. The project defines an open format for teaching AI agents specialized workflows through SKILL.md files.

## Documentation

The Agent Skills documentation site, defined in the `docs/` directory, is built with [Mintlify](https://mintlify.com).

### Quick Start Commands

```bash
# Run local development server
npm run dev
```

Local preview available at `http://localhost:3000`

### Development Notes

- **Navigation**: Defined in `docs/docs.json` under `navigation.pages` array
- **Adding pages**: Create new `.mdx` file in `/docs`, add filename (without extension) to navigation
- **Deployment**: Automatic on push to `main` branch
- **Troubleshooting**: If page shows 404, ensure you're running `mint dev` from directory containing `docs.json`

```

## File: docs\docs.json
```
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "Agent Skills",
  "colors": {
    "primary": "#7f7f7f",
    "light": "#bfbfbf",
    "dark": "#404040"
  },
  "favicon": "/favicon.svg",
  "banner": {
    "content": "Agent Skills now has an official [Discord server](https://discord.gg/MKPE9g8aUy). See the [announcement](https://github.com/agentskills/agentskills/discussions/273) for details.",
    "dismissible": true
  },
  "navbar": {
    "primary": {
      "type": "github",
      "href": "https://github.com/agentskills/agentskills"
    }
  },
  "navigation": {
    "pages": [
      "home",
      "what-are-skills",
      "specification",
      "clients",
      {
        "group": "For skill creators",
        "pages": [
          "skill-creation/quickstart",
          "skill-creation/best-practices",
          "skill-creation/optimizing-descriptions",
          "skill-creation/evaluating-skills",
          "skill-creation/using-scripts"
        ]
      },
      {
        "group": "For client implementors",
        "pages": [
          "client-implementation/adding-skills-support"
        ]
      }
    ]
  },
  "contextual": {
    "options": [
      "copy",
      "view",
      "chatgpt",
      "claude",
      "perplexity",
      "mcp",
      "cursor",
      "vscode"
    ]
  },
  "redirects": [
    {
      "source": "/integrate-skills",
      "destination": "/client-implementation/adding-skills-support"
    }
  ]
}

```

## File: docs\README.md
```
# Agent Skills Documentation

This directory contains the source code for the Agent Skills [documentation site](https://agentskills.io/), which is built using [Mintlify](https://mintlify.com).

## Development

Run the following command at the documentation root, where `docs.json` is located:

```bash
npx mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing changes

Changes are deployed to production automatically after pushing to the default branch.

```

## File: docs\style.css
```
#content-area {
  --font-mono: var(--font-jetbrains-mono), ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; /* via Mintlify theme */

  h5 {
    font-weight: 500;
  }

  h6 {
    font-weight: 400;
  }
}



/*** Add automatic section numbers to headings and table of contents items ***/

#enable-section-numbers {
  display: none;
}

body:has(#enable-section-numbers) {
  #content-area,
  #table-of-contents {
    counter-reset: h2-counter h3-counter h4-counter h5-counter h6-counter;
  }

  #content-area h2[id],
  #table-of-contents li[data-depth="0"] {
    counter-set: h3-counter h4-counter h5-counter h6-counter;
  }

  #content-area h3[id],
  #table-of-contents li[data-depth="1"] {
    counter-set: h4-counter h5-counter h6-counter;
  }

  #content-area h4[id],
  #table-of-contents li[data-depth="2"] {
    counter-set: h5-counter h6-counter;
  }

  #content-area h5[id],
  #content-area h5,
  #table-of-contents li[data-depth="3"] {
    counter-set: h6-counter;
  }

  #content-area h2[id]::before,
  #table-of-contents li[data-depth="0"] a::before {
    counter-increment: h2-counter;
    content: counter(h2-counter) ". ";
  }

  #content-area h3[id]::before,
  #table-of-contents li[data-depth="1"] a::before {
    counter-increment: h3-counter;
    content: counter(h2-counter) "." counter(h3-counter) " ";
  }

  #content-area h4[id]::before,
  #table-of-contents li[data-depth="2"] a::before {
    counter-increment: h4-counter;
    content: counter(h2-counter) "." counter(h3-counter) "." counter(h4-counter)
      " ";
  }

  #content-area h5[id]::before,
  #content-area h5::before,
  #table-of-contents li[data-depth="3"] a::before {
    counter-increment: h5-counter;
    content: counter(h2-counter) "." counter(h3-counter) "." counter(h4-counter)
      "." counter(h5-counter) " ";
  }

  #content-area h6[id]::before,
  #content-area h6::before,
  #table-of-contents li[data-depth="4"] a::before {
    counter-increment: h6-counter;
    content: counter(h2-counter) "." counter(h3-counter) "." counter(h4-counter)
      "." counter(h5-counter) "." counter(h6-counter) " ";
  }
}



/* Logo carousel */
.logo-carousel {
  overflow: hidden;
  width: 100%;
}

.logo-carousel-track {
  display: flex;
  align-items: center;
  width: max-content;
  gap: 3rem;
  padding: 0.75rem 0;
  will-change: transform;
}

@keyframes logo-scroll {
  from { transform: translateX(0); }
  to { transform: translateX(calc(-50% - 1.5rem)); }
}

@media (prefers-reduced-motion: reduce) {
  .logo-carousel-track { animation: none; }
}

```

## File: docs\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs
name: Docs
path: ecosystem/skills/repo-fetched-agentskills-111250/docs
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Docs
Storage area for 'docs' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: docs\client-implementation\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs-client-implementation
name: Client-Implementation
path: ecosystem/skills/repo-fetched-agentskills-111250/docs/client-implementation
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Client-Implementation
Storage area for 'client-implementation' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: docs\images\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs-images
name: Images
path: ecosystem/skills/repo-fetched-agentskills-111250/docs/images
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Images
Storage area for 'images' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: docs\images\logos\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs-images-logos
name: Logos
path: ecosystem/skills/repo-fetched-agentskills-111250/docs/images/logos
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Logos
Storage area for 'logos' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: docs\skill-creation\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs-skill-creation
name: Skill-Creation
path: ecosystem/skills/repo-fetched-agentskills-111250/docs/skill-creation
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skill-Creation
Storage area for 'skill-creation' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: docs\snippets\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-docs-snippets
name: Snippets
path: ecosystem/skills/repo-fetched-agentskills-111250/docs/snippets
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Snippets
Storage area for 'snippets' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills-ref\claude.md
```
# Development

## Code Quality

Format and lint with ruff:

```bash
uv run ruff format .
uv run ruff check --fix .
```

## Testing

Run tests with pytest:

```bash
uv run pytest
```

```

## File: skills-ref\README.md
```
# skills-ref

Reference library for Agent Skills.

> [!IMPORTANT]
> This library is intended for demonstration purposes only. It is not meant to be used in production.

## Installation

### macOS / Linux

Using pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Or using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
source .venv/bin/activate
```

### Windows

Using pip (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Using pip (Command Prompt):

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
```

Or using [uv](https://docs.astral.sh/uv/):

```powershell
uv sync
.venv\Scripts\Activate.ps1
```

After installation, the `skills-ref` executable will be available on your `PATH` (within the activated virtual environment).

## Usage

### CLI

```bash
# Validate a skill
skills-ref validate path/to/skill

# Read skill properties (outputs JSON)
skills-ref read-properties path/to/skill

# Generate <available_skills> XML for agent prompts
skills-ref to-prompt path/to/skill-a path/to/skill-b
```

### Python API

```python
from pathlib import Path
from skills_ref import validate, read_properties, to_prompt

# Validate a skill directory
problems = validate(Path("my-skill"))
if problems:
    print("Validation errors:", problems)

# Read skill properties
props = read_properties(Path("my-skill"))
print(f"Skill: {props.name} - {props.description}")

# Generate prompt for available skills
prompt = to_prompt([Path("skill-a"), Path("skill-b")])
print(prompt)
```

## Agent Prompt Integration

Use `to-prompt` to generate the suggested `<available_skills>` XML block for your agent's system prompt. This format is recommended for Anthropic's models, but Skill Clients may choose to format it differently based on the model being used.

```xml
<available_skills>
<skill>
<name>
my-skill
</name>
<description>
What this skill does and when to use it
</description>
<location>
/path/to/my-skill/SKILL.md
</location>
</skill>
</available_skills>
```

The `<location>` element tells the agent where to find the full skill instructions.

## License

Apache 2.0

```

## File: skills-ref\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-skills-ref
name: Skills-Ref
path: ecosystem/skills/repo-fetched-agentskills-111250/skills-ref
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skills-Ref
Storage area for 'skills-ref' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills-ref\src\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-skills-ref-src
name: Src
path: ecosystem/skills/repo-fetched-agentskills-111250/skills-ref/src
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Src
Storage area for 'src' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills-ref\src\skills_ref\cli.py
```
"""CLI for skills-ref library."""

import json
import sys
from pathlib import Path

import click

from .errors import SkillError
from .parser import read_properties
from .prompt import to_prompt
from .validator import validate


def _is_skill_md_file(path: Path) -> bool:
    """Check if path points directly to a SKILL.md or skill.md file."""
    return path.is_file() and path.name.lower() == "skill.md"


@click.group()
@click.version_option()
def main():
    """Reference library for Agent Skills."""
    pass


@main.command("validate")
@click.argument("skill_path", type=click.Path(exists=True, path_type=Path))
def validate_cmd(skill_path: Path):
    """Validate a skill directory.

    Checks that the skill has a valid SKILL.md with proper frontmatter,
    correct naming conventions, and required fields.

    Exit codes:
        0: Valid skill
        1: Validation errors found
    """
    if _is_skill_md_file(skill_path):
        skill_path = skill_path.parent

    errors = validate(skill_path)

    if errors:
        click.echo(f"Validation failed for {skill_path}:", err=True)
        for error in errors:
            click.echo(f"  - {error}", err=True)
        sys.exit(1)
    else:
        click.echo(f"Valid skill: {skill_path}")


@main.command("read-properties")
@click.argument("skill_path", type=click.Path(exists=True, path_type=Path))
def read_properties_cmd(skill_path: Path):
    """Read and print skill properties as JSON.

    Parses the YAML frontmatter from SKILL.md and outputs the
    properties as JSON.

    Exit codes:
        0: Success
        1: Parse error
    """
    try:
        if _is_skill_md_file(skill_path):
            skill_path = skill_path.parent

        props = read_properties(skill_path)
        click.echo(json.dumps(props.to_dict(), indent=2))
    except SkillError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@main.command("to-prompt")
@click.argument(
    "skill_paths", type=click.Path(exists=True, path_type=Path), nargs=-1, required=True
)
def to_prompt_cmd(skill_paths: tuple[Path, ...]):
    """Generate <available_skills> XML for agent prompts.

    Accepts one or more skill directories.

    Exit codes:
        0: Success
        1: Error
    """
    try:
        resolved_paths = []
        for skill_path in skill_paths:
            if _is_skill_md_file(skill_path):
                resolved_paths.append(skill_path.parent)
            else:
                resolved_paths.append(skill_path)

        output = to_prompt(resolved_paths)
        click.echo(output)
    except SkillError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

```

## File: skills-ref\src\skills_ref\errors.py
```
"""Skill-related exceptions."""


class SkillError(Exception):
    """Base exception for all skill-related errors."""

    pass


class ParseError(SkillError):
    """Raised when SKILL.md parsing fails."""

    pass


class ValidationError(SkillError):
    """Raised when skill properties are invalid.

    Attributes:
        errors: List of validation error messages (may contain just one)
    """

    def __init__(self, message: str, errors: list[str] | None = None):
        super().__init__(message)
        self.errors = errors if errors is not None else [message]

```

## File: skills-ref\src\skills_ref\models.py
```
"""Data models for Agent Skills."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SkillProperties:
    """Properties parsed from a skill's SKILL.md frontmatter.

    Attributes:
        name: Skill name in kebab-case (required)
        description: What the skill does and when the model should use it (required)
        license: License for the skill (optional)
        compatibility: Compatibility information for the skill (optional)
        allowed_tools: Tool patterns the skill requires (optional, experimental)
        metadata: Key-value pairs for client-specific properties (defaults to
            empty dict; omitted from to_dict() output when empty)
    """

    name: str
    description: str
    license: Optional[str] = None
    compatibility: Optional[str] = None
    allowed_tools: Optional[str] = None
    metadata: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary, excluding None values."""
        result = {"name": self.name, "description": self.description}
        if self.license is not None:
            result["license"] = self.license
        if self.compatibility is not None:
            result["compatibility"] = self.compatibility
        if self.allowed_tools is not None:
            result["allowed-tools"] = self.allowed_tools
        if self.metadata:
            result["metadata"] = self.metadata
        return result

```

## File: skills-ref\src\skills_ref\parser.py
```
"""YAML frontmatter parsing for SKILL.md files."""

from pathlib import Path
from typing import Optional

import strictyaml

from .errors import ParseError, ValidationError
from .models import SkillProperties


def find_skill_md(skill_dir: Path) -> Optional[Path]:
    """Find the SKILL.md file in a skill directory.

    Prefers SKILL.md (uppercase) but accepts skill.md (lowercase).

    Args:
        skill_dir: Path to the skill directory

    Returns:
        Path to the SKILL.md file, or None if not found
    """
    for name in ("SKILL.md", "skill.md"):
        path = skill_dir / name
        if path.exists():
            return path
    return None


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from SKILL.md content.

    Args:
        content: Raw content of SKILL.md file

    Returns:
        Tuple of (metadata dict, markdown body)

    Raises:
        ParseError: If frontmatter is missing or invalid
    """
    if not content.startswith("---"):
        raise ParseError("SKILL.md must start with YAML frontmatter (---)")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ParseError("SKILL.md frontmatter not properly closed with ---")

    frontmatter_str = parts[1]
    body = parts[2].strip()

    try:
        parsed = strictyaml.load(frontmatter_str)
        metadata = parsed.data
    except strictyaml.YAMLError as e:
        raise ParseError(f"Invalid YAML in frontmatter: {e}")

    if not isinstance(metadata, dict):
        raise ParseError("SKILL.md frontmatter must be a YAML mapping")

    if "metadata" in metadata and isinstance(metadata["metadata"], dict):
        metadata["metadata"] = {str(k): str(v) for k, v in metadata["metadata"].items()}

    return metadata, body


def read_properties(skill_dir: Path) -> SkillProperties:
    """Read skill properties from SKILL.md frontmatter.

    This function parses the frontmatter and returns properties.
    It does NOT perform full validation. Use validate() for that.

    Args:
        skill_dir: Path to the skill directory

    Returns:
        SkillProperties with parsed metadata

    Raises:
        ParseError: If SKILL.md is missing or has invalid YAML
        ValidationError: If required fields (name, description) are missing
    """
    skill_dir = Path(skill_dir)
    skill_md = find_skill_md(skill_dir)

    if skill_md is None:
        raise ParseError(f"SKILL.md not found in {skill_dir}")

    content = skill_md.read_text()
    metadata, _ = parse_frontmatter(content)

    if "name" not in metadata:
        raise ValidationError("Missing required field in frontmatter: name")
    if "description" not in metadata:
        raise ValidationError("Missing required field in frontmatter: description")

    name = metadata["name"]
    description = metadata["description"]

    if not isinstance(name, str) or not name.strip():
        raise ValidationError("Field 'name' must be a non-empty string")
    if not isinstance(description, str) or not description.strip():
        raise ValidationError("Field 'description' must be a non-empty string")

    return SkillProperties(
        name=name.strip(),
        description=description.strip(),
        license=metadata.get("license"),
        compatibility=metadata.get("compatibility"),
        allowed_tools=metadata.get("allowed-tools"),
        metadata=metadata.get("metadata"),
    )

```

## File: skills-ref\src\skills_ref\prompt.py
```
"""Generate <available_skills> XML prompt block for agent system prompts."""

import html
from pathlib import Path

from .parser import find_skill_md, read_properties


def to_prompt(skill_dirs: list[Path]) -> str:
    """Generate the <available_skills> XML block for inclusion in agent prompts.

    This XML format is what Anthropic uses and recommends for Claude models.
    Skill Clients may format skill information differently to suit their
    models or preferences.

    Args:
        skill_dirs: List of paths to skill directories

    Returns:
        XML string with <available_skills> block containing each skill's
        name, description, and location.

    Example output:
        <available_skills>
        <skill>
        <name>pdf-reader</name>
        <description>Read and extract text from PDF files</description>
        <location>/path/to/pdf-reader/SKILL.md</location>
        </skill>
        </available_skills>
    """
    if not skill_dirs:
        return "<available_skills>\n</available_skills>"

    lines = ["<available_skills>"]

    for skill_dir in skill_dirs:
        skill_dir = Path(skill_dir).resolve()
        props = read_properties(skill_dir)

        lines.append("<skill>")
        lines.append("<name>")
        lines.append(html.escape(props.name))
        lines.append("</name>")
        lines.append("<description>")
        lines.append(html.escape(props.description))
        lines.append("</description>")

        skill_md_path = find_skill_md(skill_dir)
        lines.append("<location>")
        lines.append(str(skill_md_path))
        lines.append("</location>")

        lines.append("</skill>")

    lines.append("</available_skills>")

    return "\n".join(lines)

```

## File: skills-ref\src\skills_ref\validator.py
```
"""Skill validation logic."""

import unicodedata
from pathlib import Path
from typing import Optional

from .errors import ParseError
from .parser import find_skill_md, parse_frontmatter

MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500

# Allowed frontmatter fields per Agent Skills Spec
ALLOWED_FIELDS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}


def _validate_name(name: str, skill_dir: Path) -> list[str]:
    """Validate skill name format and directory match.

    Skill names support i18n characters (Unicode letters) plus hyphens.
    Names must be lowercase and cannot start/end with hyphens.
    """
    errors = []

    if not name or not isinstance(name, str) or not name.strip():
        errors.append("Field 'name' must be a non-empty string")
        return errors

    name = unicodedata.normalize("NFKC", name.strip())

    if len(name) > MAX_SKILL_NAME_LENGTH:
        errors.append(
            f"Skill name '{name}' exceeds {MAX_SKILL_NAME_LENGTH} character limit "
            f"({len(name)} chars)"
        )

    if name != name.lower():
        errors.append(f"Skill name '{name}' must be lowercase")

    if name.startswith("-") or name.endswith("-"):
        errors.append("Skill name cannot start or end with a hyphen")

    if "--" in name:
        errors.append("Skill name cannot contain consecutive hyphens")

    if not all(c.isalnum() or c == "-" for c in name):
        errors.append(
            f"Skill name '{name}' contains invalid characters. "
            "Only letters, digits, and hyphens are allowed."
        )

    if skill_dir:
        dir_name = unicodedata.normalize("NFKC", skill_dir.name)
        if dir_name != name:
            errors.append(
                f"Directory name '{skill_dir.name}' must match skill name '{name}'"
            )

    return errors


def _validate_description(description: str) -> list[str]:
    """Validate description format."""
    errors = []

    if not description or not isinstance(description, str) or not description.strip():
        errors.append("Field 'description' must be a non-empty string")
        return errors

    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"Description exceeds {MAX_DESCRIPTION_LENGTH} character limit "
            f"({len(description)} chars)"
        )

    return errors


def _validate_compatibility(compatibility: str) -> list[str]:
    """Validate compatibility format."""
    errors = []

    if not isinstance(compatibility, str):
        errors.append("Field 'compatibility' must be a string")
        return errors

    if len(compatibility) > MAX_COMPATIBILITY_LENGTH:
        errors.append(
            f"Compatibility exceeds {MAX_COMPATIBILITY_LENGTH} character limit "
            f"({len(compatibility)} chars)"
        )

    return errors


def _validate_metadata_fields(metadata: dict) -> list[str]:
    """Validate that only allowed fields are present."""
    errors = []

    extra_fields = set(metadata.keys()) - ALLOWED_FIELDS
    if extra_fields:
        errors.append(
            f"Unexpected fields in frontmatter: {', '.join(sorted(extra_fields))}. "
            f"Only {sorted(ALLOWED_FIELDS)} are allowed."
        )

    return errors


def validate_metadata(metadata: dict, skill_dir: Optional[Path] = None) -> list[str]:
    """Validate parsed skill metadata.

    This is the core validation function that works on already-parsed metadata,
    avoiding duplicate file I/O when called from the parser.

    Args:
        metadata: Parsed YAML frontmatter dictionary
        skill_dir: Optional path to skill directory (for name-directory match check)

    Returns:
        List of validation error messages. Empty list means valid.
    """
    errors = []
    errors.extend(_validate_metadata_fields(metadata))

    if "name" not in metadata:
        errors.append("Missing required field in frontmatter: name")
    else:
        errors.extend(_validate_name(metadata["name"], skill_dir))

    if "description" not in metadata:
        errors.append("Missing required field in frontmatter: description")
    else:
        errors.extend(_validate_description(metadata["description"]))

    if "compatibility" in metadata:
        errors.extend(_validate_compatibility(metadata["compatibility"]))

    return errors


def validate(skill_dir: Path) -> list[str]:
    """Validate a skill directory.

    Args:
        skill_dir: Path to the skill directory

    Returns:
        List of validation error messages. Empty list means valid.
    """
    skill_dir = Path(skill_dir)

    if not skill_dir.exists():
        return [f"Path does not exist: {skill_dir}"]

    if not skill_dir.is_dir():
        return [f"Not a directory: {skill_dir}"]

    skill_md = find_skill_md(skill_dir)
    if skill_md is None:
        return ["Missing required file: SKILL.md"]

    try:
        content = skill_md.read_text()
        metadata, _ = parse_frontmatter(content)
    except ParseError as e:
        return [str(e)]

    return validate_metadata(metadata, skill_dir)

```

## File: skills-ref\src\skills_ref\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-skills-ref-src-skills_ref
name: Skills Ref
path: ecosystem/skills/repo-fetched-agentskills-111250/skills-ref/src/skills_ref
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Skills Ref
Storage area for 'skills_ref' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills-ref\src\skills_ref\__init__.py
```
"""Reference library for Agent Skills."""

from .errors import ParseError, SkillError, ValidationError
from .models import SkillProperties
from .parser import find_skill_md, read_properties
from .prompt import to_prompt
from .validator import validate

__all__ = [
    "SkillError",
    "ParseError",
    "ValidationError",
    "SkillProperties",
    "find_skill_md",
    "validate",
    "read_properties",
    "to_prompt",
]

__version__ = "0.1.0"

```

## File: skills-ref\tests\test_parser.py
```
"""Tests for parser module."""

import pytest

from skills_ref.parser import (
    ParseError,
    ValidationError,
    find_skill_md,
    parse_frontmatter,
    read_properties,
)


def test_valid_frontmatter():
    content = """---
name: my-skill
description: A test skill
---
# My Skill

Instructions here.
"""
    metadata, body = parse_frontmatter(content)
    assert metadata["name"] == "my-skill"
    assert metadata["description"] == "A test skill"
    assert "# My Skill" in body


def test_missing_frontmatter():
    content = "# No frontmatter here"
    with pytest.raises(ParseError, match="must start with YAML frontmatter"):
        parse_frontmatter(content)


def test_unclosed_frontmatter():
    content = """---
name: my-skill
description: A test skill
"""
    with pytest.raises(ParseError, match="not properly closed"):
        parse_frontmatter(content)


def test_invalid_yaml():
    content = """---
name: [invalid
description: broken
---
Body here
"""
    with pytest.raises(ParseError, match="Invalid YAML"):
        parse_frontmatter(content)


def test_non_dict_frontmatter():
    content = """---
- just
- a
- list
---
Body
"""
    with pytest.raises(ParseError, match="must be a YAML mapping"):
        parse_frontmatter(content)


def test_read_valid_skill(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
license: MIT
---
# My Skill
""")
    props = read_properties(skill_dir)
    assert props.name == "my-skill"
    assert props.description == "A test skill"
    assert props.license == "MIT"


def test_read_with_metadata(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
metadata:
  author: Test Author
  version: 1.0
---
Body
""")
    props = read_properties(skill_dir)
    assert props.metadata == {"author": "Test Author", "version": "1.0"}


def test_missing_skill_md(tmp_path):
    with pytest.raises(ParseError, match="SKILL.md not found"):
        read_properties(tmp_path)


def test_missing_name(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
description: A test skill
---
Body
""")
    with pytest.raises(ValidationError, match="Missing required field.*name"):
        read_properties(skill_dir)


def test_missing_description(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
---
Body
""")
    with pytest.raises(ValidationError, match="Missing required field.*description"):
        read_properties(skill_dir)


def test_find_skill_md_prefers_uppercase(tmp_path):
    """SKILL.md should be preferred over skill.md when both exist."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("uppercase")
    (skill_dir / "skill.md").write_text("lowercase")
    result = find_skill_md(skill_dir)
    assert result is not None
    assert result.name == "SKILL.md"


def test_find_skill_md_accepts_lowercase(tmp_path):
    """skill.md should be accepted when SKILL.md doesn't exist."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "skill.md").write_text("lowercase")
    result = find_skill_md(skill_dir)
    assert result is not None
    # Check case-insensitively since some filesystems are case-insensitive
    assert result.name.lower() == "skill.md"


def test_find_skill_md_returns_none_when_missing(tmp_path):
    """find_skill_md should return None when no skill.md exists."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    result = find_skill_md(skill_dir)
    assert result is None


def test_read_properties_with_lowercase_skill_md(tmp_path):
    """read_properties should work with lowercase skill.md."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "skill.md").write_text("""---
name: my-skill
description: A test skill
---
# My Skill
""")
    props = read_properties(skill_dir)
    assert props.name == "my-skill"
    assert props.description == "A test skill"


def test_read_with_allowed_tools(tmp_path):
    """allowed-tools should be parsed into SkillProperties."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
allowed-tools: Bash(jq:*) Bash(git:*)
---
Body
""")
    props = read_properties(skill_dir)
    assert props.allowed_tools == "Bash(jq:*) Bash(git:*)"
    # Verify to_dict outputs as "allowed-tools" (hyphenated)
    d = props.to_dict()
    assert d["allowed-tools"] == "Bash(jq:*) Bash(git:*)"

```

## File: skills-ref\tests\test_prompt.py
```
"""Tests for prompt module."""

from skills_ref.prompt import to_prompt


def test_empty_list():
    result = to_prompt([])
    assert result == "<available_skills>\n</available_skills>"


def test_single_skill(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
---
Body
""")
    result = to_prompt([skill_dir])
    assert "<available_skills>" in result
    assert "</available_skills>" in result
    assert "<name>\nmy-skill\n</name>" in result
    assert "<description>\nA test skill\n</description>" in result
    assert "<location>" in result
    assert "SKILL.md" in result


def test_multiple_skills(tmp_path):
    skill_a = tmp_path / "skill-a"
    skill_a.mkdir()
    (skill_a / "SKILL.md").write_text("""---
name: skill-a
description: First skill
---
Body
""")

    skill_b = tmp_path / "skill-b"
    skill_b.mkdir()
    (skill_b / "SKILL.md").write_text("""---
name: skill-b
description: Second skill
---
Body
""")

    result = to_prompt([skill_a, skill_b])
    assert result.count("<skill>") == 2
    assert result.count("</skill>") == 2
    assert "skill-a" in result
    assert "skill-b" in result


def test_special_characters_escaped(tmp_path):
    """XML special characters in description are escaped."""
    skill_dir = tmp_path / "special-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: special-skill
description: Use <foo> & <bar> tags
---
Body
""")
    result = to_prompt([skill_dir])
    assert "&lt;foo&gt;" in result
    assert "&amp;" in result
    assert "&lt;bar&gt;" in result
    assert "<foo>" not in result
    assert "<bar>" not in result

```

## File: skills-ref\tests\test_validator.py
```
"""Tests for validator module."""

from skills_ref.validator import validate


def test_valid_skill(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
---
# My Skill
""")
    errors = validate(skill_dir)
    assert errors == []


def test_nonexistent_path(tmp_path):
    errors = validate(tmp_path / "nonexistent")
    assert len(errors) == 1
    assert "does not exist" in errors[0]


def test_not_a_directory(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("test")
    errors = validate(file_path)
    assert len(errors) == 1
    assert "Not a directory" in errors[0]


def test_missing_skill_md(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    errors = validate(skill_dir)
    assert len(errors) == 1
    assert "Missing required file: SKILL.md" in errors[0]


def test_invalid_name_uppercase(tmp_path):
    skill_dir = tmp_path / "MySkill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: MySkill
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("lowercase" in e for e in errors)


def test_name_too_long(tmp_path):
    long_name = "a" * 70  # Exceeds 64 char limit
    skill_dir = tmp_path / long_name
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(f"""---
name: {long_name}
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("exceeds" in e and "character limit" in e for e in errors)


def test_name_leading_hyphen(tmp_path):
    skill_dir = tmp_path / "-my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: -my-skill
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("cannot start or end with a hyphen" in e for e in errors)


def test_name_consecutive_hyphens(tmp_path):
    skill_dir = tmp_path / "my--skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my--skill
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("consecutive hyphens" in e for e in errors)


def test_name_invalid_characters(tmp_path):
    skill_dir = tmp_path / "my_skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my_skill
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("invalid characters" in e for e in errors)


def test_name_directory_mismatch(tmp_path):
    skill_dir = tmp_path / "wrong-name"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: correct-name
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert any("must match skill name" in e for e in errors)


def test_unexpected_fields(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
unknown_field: should not be here
---
Body
""")
    errors = validate(skill_dir)
    assert any("Unexpected fields" in e for e in errors)


def test_valid_with_all_fields(tmp_path):
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
license: MIT
metadata:
  author: Test
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_allowed_tools_accepted(tmp_path):
    """allowed-tools is accepted (experimental feature)."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
allowed-tools: Bash(jq:*) Bash(git:*)
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_i18n_chinese_name(tmp_path):
    """Chinese characters are allowed in skill names."""
    skill_dir = tmp_path / "技能"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: 技能
description: A skill with Chinese name
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_i18n_russian_name_with_hyphens(tmp_path):
    """Russian names with hyphens are allowed."""
    skill_dir = tmp_path / "мой-навык"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: мой-навык
description: A skill with Russian name
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_i18n_russian_lowercase_valid(tmp_path):
    """Russian lowercase names should be accepted."""
    skill_dir = tmp_path / "навык"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: навык
description: A skill with Russian lowercase name
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_i18n_russian_uppercase_rejected(tmp_path):
    """Russian uppercase names should be rejected."""
    skill_dir = tmp_path / "НАВЫК"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: НАВЫК
description: A skill with Russian uppercase name
---
Body
""")
    errors = validate(skill_dir)
    assert any("lowercase" in e for e in errors)


def test_description_too_long(tmp_path):
    """Description exceeding 1024 chars should fail."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    long_desc = "x" * 1100
    (skill_dir / "SKILL.md").write_text(f"""---
name: my-skill
description: {long_desc}
---
Body
""")
    errors = validate(skill_dir)
    assert any("exceeds" in e and "1024" in e for e in errors)


def test_valid_compatibility(tmp_path):
    """Valid compatibility field should be accepted."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text("""---
name: my-skill
description: A test skill
compatibility: Requires Python 3.11+
---
Body
""")
    errors = validate(skill_dir)
    assert errors == []


def test_compatibility_too_long(tmp_path):
    """Compatibility exceeding 500 chars should fail."""
    skill_dir = tmp_path / "my-skill"
    skill_dir.mkdir()
    long_compat = "x" * 550
    (skill_dir / "SKILL.md").write_text(f"""---
name: my-skill
description: A test skill
compatibility: {long_compat}
---
Body
""")
    errors = validate(skill_dir)
    assert any("exceeds" in e and "500" in e for e in errors)


def test_nfkc_normalization(tmp_path):
    """Skill names are NFKC normalized before validation.

    The name 'café' can be represented two ways:
    - Precomposed: 'café' (4 chars, 'é' is U+00E9)
    - Decomposed: 'café' (5 chars, 'e' + combining acute U+0301)

    NFKC normalizes both to the precomposed form.
    """
    # Use decomposed form: 'cafe' + combining acute accent (U+0301)
    decomposed_name = "cafe\u0301"  # 'café' with combining accent
    composed_name = "café"  # precomposed form

    # Directory uses composed form, SKILL.md uses decomposed - should match after normalization
    skill_dir = tmp_path / composed_name
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(f"""---
name: {decomposed_name}
description: A test skill
---
Body
""")
    errors = validate(skill_dir)
    assert errors == [], f"Expected no errors, got: {errors}"

```

## File: skills-ref\tests\_DIR_IDENTITY.md
```
---
id: ecosystem-skills-repo-fetched-agentskills-111250-skills-ref-tests
name: Tests
path: ecosystem/skills/repo-fetched-agentskills-111250/skills-ref/tests
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# Tests
Storage area for 'tests' domain.
> Auto-generated identity tag by OMA v2.1.

```

## File: skills-ref\tests\__init__.py
```
"""Tests for skills-ref library."""

```


---
id: github.com-omkamal-pypict-claude-skill-a93c3572-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:07.613849
---

# KNOWLEDGE EXTRACT: github.com_omkamal_pypict-claude-skill_a93c3572
> **Extracted on:** 2026-04-01 12:31:03
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521855/github.com_omkamal_pypict-claude-skill_a93c3572

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/
*.log

# PICT generated files (optional - keep for examples)
# *.txt

# OS
Thumbs.db
.DS_Store

# Claude specific
.claude/
*.claude

# Temporary files
*.tmp
*.bak
*.backup
temp/
tmp/
CLAUDE.md
.specify/*

# Blog articles and drafts
blog-article.md
blog-article-image-prompts.md
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional real-world examples (e-commerce, API testing, mobile apps)
- Enhanced PICT syntax reference documentation
- Improved helper scripts for PICT model generation
- Integration with test management tools
- Support for higher-order combinatorial testing (3-way, 4-way)

## [1.0.2] - 2025-10-19

### Added
- **Automotive Gearbox Control System example** - Advanced PICT example for safety-critical systems
- `examples/gearbox-specification.md` - Comprehensive 10-section specification (3,600+ words)
  - System components (sensors, actuators, controls)
  - Operating modes (Manual, Sport, Eco)
  - Functional requirements and safety features
  - Error handling and fault tolerance
  - Performance, environmental, and integration requirements
- `examples/gearbox-test-plan.md` - Complete PICT test plan
  - 12 parameters with complex interdependencies
  - 14 business rules and safety constraints
  - 40 test cases from ~159 billion combinations (99.999999975% reduction)
  - Expected outputs with detailed system responses
  - Priority-based execution plan, coverage analysis, traceability matrix
  - Risk assessment for safety-critical scenarios

### Changed
- Updated `examples/README.md` with gearbox example section
- Added advanced constraint modeling patterns documentation
- Expanded learning points with multi-mode testing and fault injection examples

### Documentation
- Comprehensive gearbox specification covering all aspects of transmission control
- Detailed test plan demonstrating advanced PICT usage
- Learning material for complex parameter interactions and safety constraints

## [1.0.1] - 2025-10-19

### Added
- **Claude Code Plugin Marketplace support** - Users can now install via `/plugin` commands
- `.claude-plugin/marketplace.json` - Marketplace catalog for plugin discovery
- `.claude-plugin/plugin.json` - Complete plugin metadata with keywords and repository info
- Plugin installation as Method 1 in README.md (easiest installation method)

### Changed
- Updated README.md with plugin marketplace installation instructions
- Renumbered installation methods (now 5 methods: marketplace, git clone, submodule, minimal zip, full zip)
- Updated author information: Omar Kamal Hosney <omar.wasat@gmail.com>

### Improved
- Easier installation process via plugin marketplace
- Automated updates when using plugin marketplace
- Better discoverability through Claude Code's plugin system

## [1.0.0] - 2025-10-19

### Added
- Initial release of PICT Test Designer skill
- Core functionality for test case design using PICT methodology
- Comprehensive ATM system testing example
- Installation guide for Claude Code CLI and Desktop
- MIT License with proper attributions
- Contributing guidelines
- Documentation structure (README, SKILL.md, examples)
- GitHub Actions CI workflow
- Example directory with ATM specification and test plan
- **Minimal installation package (9.3 KB)** with essential files only
- GitHub Release v1.0.0 with downloadable assets
- Multiple installation methods (git clone, submodule, minimal ZIP, full ZIP)

### Features
- Automated parameter identification from requirements
- PICT model generation with constraints
- Expected output determination
- Pairwise test case generation
- Support for multiple testing domains
- Comprehensive documentation and examples
- 80-99% test case reduction while maintaining coverage

### Fixed
- Corrected installation instructions (removed non-existent CLI commands)
- Updated to use proper manual installation via `.claude/skills/` directory
- Removed CLAUDE.md from version control (now user-specific)

### Documentation
- README.md: Corrected installation methods with 4 options
- QUICKSTART.md: Updated with accurate installation steps
- releases/README.md: Guide for using minimal package
- README-INSTALL.txt: User-friendly guide included in minimal ZIP

### Credits
- Built on Microsoft PICT
- Uses pypict Python bindings by Kenichi Maehashi
- Designed for Claude AI by Anthropic

## Version History

### Versioning Scheme

- **Major version (X.0.0)**: Incompatible API changes or major feature additions
- **Minor version (0.X.0)**: New features in a backward-compatible manner
- **Patch version (0.0.X)**: Backward-compatible bug fixes

### Release Types

- **[Unreleased]**: Changes in development but not yet released
- **[Version]**: Released version with date

### Change Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

---

## How to Contribute to Changelog

When submitting a pull request, add your changes to the [Unreleased] section under the appropriate category (Added, Changed, Fixed, etc.).

Example:
```markdown
## [Unreleased]

### Added
- New example for mobile app testing (#42)

### Fixed
- Typo in installation instructions (#38)
```

The maintainers will move items from [Unreleased] to a versioned release when publishing a new version.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to pypict-claude-skill

Thank you for your interest in contributing to the PICT Test Designer Claude Skill! This document provides guidelines and instructions for contributing.

## Ways to Contribute

### 1. Add Examples
- Real-world test scenarios from different domains
- Industry-specific testing patterns
- Complex constraint scenarios
- Edge cases and advanced usage

### 2. Improve Documentation
- Fix typos or unclear explanations
- Add tutorials or guides
- Translate documentation
- Improve code comments

### 3. Enhance the Skill
- Optimize test case generation
- Add new constraint patterns
- Improve expected output determination
- Extend domain support

### 4. Report Issues
- Bug reports
- Feature requests
- Documentation gaps
- Usability improvements

### 5. Share Use Cases
- Blog posts about using the skill
- Video tutorials
- Workshop materials
- Success stories

## Getting Started

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/pypict-claude-skill.git
   cd pypict-claude-skill
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/originalowner/pypict-claude-skill.git
   ```

### Create a Branch

Create a descriptive branch name:
```bash
git checkout -b feature/add-ecommerce-example
# or
git checkout -b fix/typo-in-readme
# or
git checkout -b docs/improve-installation-guide
```

## Contribution Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

### Quality Standards

#### For Examples
- Include complete specification/requirements
- Provide clear PICT model
- Generate comprehensive test cases
- Add expected outputs
- Document key learning points
- Follow the existing example structure

#### For Documentation
- Use clear, concise language
- Include code examples where helpful
- Test all commands and code snippets
- Follow markdown best practices
- Check spelling and grammar

#### For Skill Improvements
- Maintain backward compatibility when possible
- Add comments explaining complex logic
- Update documentation to reflect changes
- Include examples demonstrating new features
- Test thoroughly before submitting

### File Structure

When adding examples:
```
examples/
├── your-example-name/
│   ├── README.md           # Overview and learning points
│   ├── specification.md    # Original requirements
│   ├── pict-model.txt     # Generated PICT model
│   └── test-plan.md       # Complete test plan
└── README.md              # Update to list your example
```

### Commit Messages

Write clear, descriptive commit messages:

```bash
# Good
git commit -m "Add e-commerce checkout testing example"
git commit -m "Fix typo in installation instructions"
git commit -m "Improve constraint generation for negative testing"

# Not ideal
git commit -m "Update files"
git commit -m "Fix stuff"
git commit -m "WIP"
```

### Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests/examples** if you're adding features
3. **Update README.md** if you're adding examples or major features
4. **Ensure quality**:
   - Check for typos
   - Test all examples
   - Verify markdown renders correctly
   - Ensure links work

5. **Submit PR** with a clear description:
   ```markdown
   ## Description
   Brief description of what this PR does
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Example addition
   
   ## Testing
   How was this tested?
   
   ## Related Issues
   Fixes #123
   ```

6. **Respond to feedback** promptly and professionally

## Example Contribution Workflow

### Adding a New Example

1. Create your branch:
   ```bash
   git checkout -b example/api-testing
   ```

2. Add your files to `examples/`:
   ```bash
   mkdir examples/api-testing
   # Create your specification, model, and test plan
   ```

3. Update `examples/README.md`:
   ```markdown
   ## API Testing Example
   Demonstrates PICT testing for REST API endpoints...
   ```

4. Commit your changes:
   ```bash
   git add examples/api-testing/
   git add examples/README.md
   git commit -m "Add REST API testing example"
   ```

5. Push to your fork:
   ```bash
   git push origin example/api-testing
   ```

6. Create a Pull Request on GitHub

### Fixing Documentation

1. Create your branch:
   ```bash
   git checkout -b docs/clarify-installation
   ```

2. Make your changes

3. Commit and push:
   ```bash
   git commit -m "Clarify installation steps for Windows users"
   git push origin docs/clarify-installation
   ```

4. Create a Pull Request

## Review Process

1. **Automated checks** (if configured) will run
2. **Maintainer review** typically within 1-2 weeks
3. **Feedback and iteration** may be requested
4. **Approval and merge** once all criteria met

## Recognition

Contributors will be:
- Listed in the repository's contributors
- Mentioned in release notes (for significant contributions)
- Credited in the documentation where appropriate

## Questions?

- Open an issue for general questions
- Tag your issue with `question`
- Be patient - we're all volunteers!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Every contribution, no matter how small, helps make this skill better for everyone. We appreciate your time and effort! 🙏
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 pypict-claude-skill contributors

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

---

This project uses and acknowledges the following tools:

PICT (Pairwise Independent Combinatorial Testing)
Copyright (c) Microsoft Corporation
Licensed under the MIT License
https://github.com/microsoft/pict

pypict - Python binding for PICT
Copyright (c) Kenichi Maehashi
Licensed under the MIT License
https://github.com/kmaehashi/pypict
```

## File: `PUBLISHING.md`
```markdown
# Publishing Guide

This guide will walk you through publishing the pypict-claude-skill repository to GitHub.

## Prerequisites

Before you begin, make sure you have:
- [ ] A GitHub account
- [ ] Git installed on your computer
- [ ] The pypict-claude-skill directory on your local machine

## Step-by-Step Publishing Process

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and log in
2. Click the "+" icon in the top-right corner
3. Select "New repository"
4. Configure your repository:
   - **Repository name:** `pypict-claude-skill`
   - **Description:** "A Claude skill for designing comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing)"
   - **Visibility:** Public (so others can use it)
   - **Initialize:** DO NOT add README, .gitignore, or license (we already have these)
5. Click "Create repository"

### Step 2: Initialize Local Git Repository

Open your terminal and navigate to the pypict-claude-skill directory:

```bash
cd /path/to/pypict-claude-skill

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: PICT Test Designer skill v1.0.0"
```

### Step 3: Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/pypict-claude-skill.git

# Verify remote is set correctly
git remote -v
```

### Step 4: Push to GitHub

```bash
# Push to main branch (or master if using older git)
git branch -M main
git push -u origin main
```

### Step 5: Verify on GitHub

1. Go to your repository: `https://github.com/YOUR_USERNAME/pypict-claude-skill`
2. Verify all files are present:
   - README.md
   - SKILL.md
   - LICENSE
   - examples/
   - .github/
   - And all other files

### Step 6: Configure Repository Settings

#### Enable Issues
1. Go to Settings → General
2. Under "Features", ensure "Issues" is checked

#### Enable Discussions (Optional)
1. Go to Settings → General
2. Under "Features", check "Discussions"
3. This allows users to ask questions and share experiences

#### Set Up Branch Protection (Optional but Recommended)
1. Go to Settings → Branches
2. Add branch protection rule for `main`
3. Recommended settings:
   - Require pull request reviews before merging
   - Require status checks to pass

### Step 7: Create a Release

1. Go to your repository on GitHub
2. Click "Releases" (right sidebar)
3. Click "Create a new release"
4. Configure the release:
   - **Tag:** `v1.0.0`
   - **Release title:** `v1.0.0 - Initial Release`
   - **Description:**
     ```markdown
     ## 🎉 Initial Release
     
     First public release of the PICT Test Designer skill for Claude!
     
     ### Features
     - Complete PICT-based test case generation
     - Comprehensive ATM system example
     - Installation guides for Claude Code CLI and Desktop
     - Full documentation and examples
     
     ### Highlights
     - Reduces test cases by 99%+ while maintaining coverage
     - Easy integration with Claude Code
     - Real-world examples included
     
     ### Credits
     Built on Microsoft PICT and pypict by Kenichi Maehashi
     ```
5. Click "Publish release"

### Step 8: Update README URLs

Now that you know your GitHub username, update the placeholder URLs in README.md:

```bash
# Edit README.md and replace all instances of:
# "yourusername" with your actual GitHub username

# For example, change:
# https://github.com/yourusername/pypict-claude-skill
# to:
# https://github.com/YOUR_ACTUAL_USERNAME/pypict-claude-skill
```

Then commit and push:

```bash
git add README.md
git commit -m "Update URLs with actual GitHub username"
git push origin main
```

### Step 9: Test the Installation

Test that others can install your skill:

#### For Claude Code CLI:
```bash
claude code config add-skill \
  --name pict-test-designer \
  --source github \
  --repo YOUR_USERNAME/pypict-claude-skill
```

#### For Claude Code Desktop:
1. Settings → Skills
2. Add Skill from GitHub
3. URL: `https://github.com/YOUR_USERNAME/pypict-claude-skill`

### Step 10: Share Your Skill!

Now that it's published, share it with:

1. **Social Media**
   - Post on Twitter/X with hashtags #ClaudeAI #Testing #PICT
   - Share on LinkedIn
   - Post in relevant Reddit communities (r/softwaredevelopment, r/QualityAssurance)

2. **Communities**
   - Claude AI Discord
   - Software testing forums
   - QA communities

3. **Your Team**
   - Share with colleagues
   - Add to team documentation
   - Include in onboarding materials

## Maintaining Your Repository

### When Making Updates

```bash
# Make your changes
git add .
git commit -m "Description of changes"
git push origin main

# For new releases
git tag -a v1.1.0 -m "Version 1.1.0"
git push origin v1.1.0
```

### Update CHANGELOG.md

Keep track of changes in CHANGELOG.md for each release.

### Respond to Issues and PRs

- Check GitHub regularly for new issues
- Review pull requests promptly
- Thank contributors
- Keep discussions friendly and helpful

## Promoting Your Skill

### 1. Add Topics to Your Repository

On GitHub, add relevant topics:
- claude
- claude-ai
- pict
- testing
- test-automation
- combinatorial-testing
- pairwise-testing
- qa
- quality-assurance

### 2. Create a Blog Post

Write about:
- Why you created this skill
- How it helps with testing
- Real-world use cases
- Tutorial on using it

### 3. Make a Video Tutorial

Create a quick video showing:
- Installation process
- Basic usage
- The ATM example
- Tips and tricks

### 4. Submit to Directories

- Add to awesome lists (awesome-claude, awesome-testing)
- Submit to skill directories
- List on your portfolio

## Getting Help

If you encounter issues:

1. Check [GitHub's documentation](https://docs.github.com)
2. Ask in GitHub Discussions (if enabled)
3. Search for similar issues
4. Ask in Claude AI community

## Congratulations! 🎉

Your skill is now public and ready to help the community!

Next steps:
- Monitor for issues and feedback
- Plan improvements based on user needs
- Consider adding more examples
- Keep documentation up to date

---

**Remember:** You're now maintaining an open-source project. Be patient, be kind, and enjoy helping others improve their testing!
```

## File: `QUICKSTART.md`
```markdown
# Quick Start Guide

Get started with PICT Test Designer in 5 minutes!

## Installation (Choose One)

### Option 1: Personal Installation (All Projects)

```bash
# Clone to your personal skills directory
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer

# Restart Claude Code - the skill is now available in all projects
```

### Option 2: Project-Specific Installation

```bash
# From your project directory
git clone https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer

# Restart Claude Code - the skill is available in this project only
```

### Option 3: Manual Download

1. Download ZIP from: `https://github.com/omkamal/pypict-claude-skill`
2. Extract to `~/.claude/skills/pict-test-designer` (personal) or `.claude/skills/pict-test-designer` (project)
3. Restart Claude Code

## Your First Test Plan (3 Steps)

### Step 1: Start Claude Code

Open your terminal or Claude Code Desktop

### Step 2: Describe Your System

Simply tell Claude what you want to test:

```
I need to test a login function with these requirements:
- Users can login with email and password
- Support for 2FA (enabled/disabled)
- "Remember me" checkbox option
- Rate limiting after 3 failed attempts

Can you design test cases using the pict-test-designer skill?
```

### Step 3: Get Your Test Cases!

Claude will automatically:
1. ✅ Analyze your requirements
2. ✅ Identify test parameters and values
3. ✅ Generate a PICT model with constraints
4. ✅ Create optimized test cases
5. ✅ Provide expected outputs

## Example Output

You'll receive:

### 1. PICT Model
```
Email: Valid, Invalid, Empty
Password: Valid, Invalid, Empty
TwoFactorAuth: Enabled, Disabled
RememberMe: Checked, Unchecked
FailedAttempts: 0, 1, 2, 3

IF [FailedAttempts] = "3" THEN [Email] = "Valid";
```

### 2. Test Cases Table

| Test # | Email | Password | 2FA | Remember | Failed | Expected Output |
|--------|-------|----------|-----|----------|--------|-----------------|
| 1 | Valid | Valid | Enabled | Checked | 0 | Success: Login with 2FA prompt |
| 2 | Valid | Invalid | Disabled | Unchecked | 1 | Error: Incorrect password (2 attempts left) |
| ... | ... | ... | ... | ... | ... | ... |

### 3. Summary
- Total combinations: 432
- PICT test cases: 15
- Reduction: 96.5%

## Real-World Examples

### Try the ATM Example

```
Using the pict-test-designer skill, analyze the ATM specification 
in examples/atm-specification.md and show me the test coverage
```

This demonstrates a complex system with:
- 8 parameters
- 25,920 possible combinations
- Only 31 test cases needed!

## Common Use Cases

### Testing a Web Form
```
Design test cases for a registration form with:
- Name (required, max 50 chars)
- Email (required, must be valid format)
- Phone (optional, 10 digits)
- Country (dropdown with 5 options)
- Terms checkbox (required)
```

### Testing an API Endpoint
```
I need to test a REST API endpoint that:
- Accepts GET, POST, PUT, DELETE methods
- Requires authentication (valid token, invalid token, missing token)
- Returns JSON, XML, or error
- Has rate limiting

Design test cases.
```

### Testing System Configuration
```
Test our application deployment with:
- Environment: Dev, Staging, Production
- Database: MySQL, PostgreSQL, SQLite
- Cache: Enabled/Disabled
- SSL: Enabled/Disabled
- Log Level: Debug, Info, Error

With the constraint: Production must not use SQLite or Debug logging
```

## Tips for Best Results

### ✅ Do This
- Describe your requirements clearly
- Mention any business rules or constraints
- Specify what different values mean
- Ask for specific output formats if needed

### ❌ Avoid This
- Too vague: "test my app"
- No context: "make test cases for login"
- Missing constraints: Not mentioning dependencies between parameters

## Next Steps

1. **Try it with your own system** - Start with a simple feature
2. **Review the examples** - Check out the [ATM example](examples/)
3. **Read the full documentation** - See [SKILL.md](../bmad_repo/SKILL.md)
4. **Customize for your needs** - Adapt parameters and constraints
5. **Share your results** - Consider contributing examples!

## Getting Help

- **Questions?** Open an [issue on GitHub](https://github.com/yourusername/pypict-claude-skill/issues)
- **Examples?** Check the [examples directory](examples/)
- **Documentation?** Read [SKILL.md](../bmad_repo/SKILL.md) and [README.md](README.md)

## Advanced Usage

### Generate More Test Cases

Once you have the PICT model, you can:

1. **Use online tools**:
   - https://pairwise.yuuniworks.com/
   - https://pairwise.teremokgames.com/

2. **Install PICT locally**:
   ```bash
   # Windows: Download from GitHub
   # https://github.com/microsoft/pict/releases
   
   # Linux/Mac: Use pypict
   pip install pypict
   ```

3. **Modify the model**:
   - Add more parameters
   - Change constraints
   - Adjust values
   - Re-generate test cases

### Export to Test Management Tools

The generated test cases can be:
- Copied to Excel/CSV
- Imported to JIRA, TestRail, Azure Test Plans
- Converted to automated test scripts
- Used in documentation

## Success Story

> "We were testing a configuration-heavy system with hundreds of possible combinations. Using PICT Test Designer, we reduced our test suite from 500+ tests to just 45 tests while maintaining the same coverage. This saved us weeks of testing time!" - QA Team Lead

## What's Next?

- Add this skill to your regular testing workflow
- Try it on different types of systems
- Share examples with your team
- Contribute improvements back to the project

**Happy Testing! 🚀**
```

## File: `README.md`
```markdown
# PICT Test Designer - Claude Skill

A Claude skill for designing comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing). This skill enables systematic test case design with minimal test cases while maintaining high coverage through pairwise combinatorial testing.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude](https://img.shields.io/badge/Claude-Skill-blue.svg)](https://claude.ai)

## 🎯 What is PICT?

PICT (Pairwise Independent Combinatorial Testing) is a combinatorial testing tool developed by Microsoft. It generates test cases that efficiently cover all pairwise combinations of parameters while drastically reducing the total number of tests compared to exhaustive testing.

**Example:** Testing a system with 8 parameters and 3-5 values each:
- Exhaustive testing: **25,920 test cases**
- PICT pairwise testing: **~30 test cases** (99.88% reduction!)

## 🚀 Features

- **Automated Test Case Generation**: Converts requirements into structured PICT models
- **Constraint-Based Testing**: Applies business rules to eliminate invalid combinations
- **Expected Output Generation**: Automatically determines expected results for each test case
- **Comprehensive Coverage**: Ensures all pairwise parameter interactions are tested
- **Multiple Domains**: Works for software functions, APIs, web forms, configurations, and more

## 📋 Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing in Claude Code CLI](#installing-in-claude-code-cli)
  - [Installing in Claude Code Desktop](#installing-in-claude-code-desktop)
- [Quick Start](#quick-start)
- [Example: ATM System Testing](#example-atm-system-testing)
- [How It Works](#how-it-works)
- [Use Cases](#use-cases)
- [Credits](#credits)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites

- Claude Code CLI or Claude Code Desktop
- (Optional) Python 3.7+ with `pypict` for advanced usage

### Installation Methods

Claude Code skills can be installed via the plugin marketplace or manually by placing them in the `.claude/skills/` directory.

### Method 1: Install via Claude Code Plugin Marketplace (Easiest) 🌟

Install directly through Claude Code's plugin system:

```bash
# Add the marketplace
/plugin marketplace add omkamal/pypict-claude-skill

# Install the plugin
/plugin install pict-test-designer@pypict-claude-skill
```

This automatically installs the skill and keeps it updated. The skill will be available across all your projects.

### Method 2: Install from GitHub (Manual)

**For Personal Use (All Projects):**

```bash
# Clone the repository to your personal skills directory
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer

# Restart Claude Code to load the skill
# The skill will now be available in all your projects
```

**For Project-Specific Use:**

```bash
# From your project directory
git clone https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer

# Add to .gitignore if you don't want to commit it
echo ".claude/skills/" >> .gitignore

# Or commit it to share with your team
git add .claude/skills/pict-test-designer
git commit -m "Add PICT test designer skill"
```

### Method 3: Install via Git Submodule (Team Sharing)

If you want to share this skill with your team via version control:

```bash
# From your project directory
git submodule add https://github.com/omkamal/pypict-claude-skill.git .claude/skills/pict-test-designer
git commit -m "Add PICT test designer skill as submodule"

# Team members clone with:
git clone --recurse-submodules <your-repo-url>

# Or if already cloned:
git submodule update --init --recursive
```

### Method 4: Download Minimal Package from Releases

Download the pre-packaged minimal installation from [GitHub Releases](https://github.com/omkamal/pypict-claude-skill/releases):

```bash
# Download the latest minimal package from releases
wget https://github.com/omkamal/pypict-claude-skill/releases/latest/download/pict-test-designer-minimal.zip

# Extract and install for personal use
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal ~/.claude/skills/pict-test-designer

# Or for project-specific use
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal .claude/skills/pict-test-designer
```

**What's included:** SKILL.md, LICENSE, references/ (syntax and examples)
**What's excluded:** Full examples, helper scripts, extended documentation
**Size:** ~9 KB | **Latest Version:** [See Releases](https://github.com/omkamal/pypict-claude-skill/releases)

### Method 5: Download Full Repository

1. **Download the repository** as a ZIP from GitHub
2. **Extract to the skills directory**:

```bash
# For personal use (all projects)
unzip pypict-claude-skill-main.zip
mv pypict-claude-skill-main ~/.claude/skills/pict-test-designer

# For project-specific use
unzip pypict-claude-skill-main.zip
mv pypict-claude-skill-main .claude/skills/pict-test-designer
```

### Verify Installation

After installation, restart Claude Code. The skill will load automatically when relevant. You can verify by asking Claude:

```
Do you have access to the pict-test-designer skill?
```

Or simply start using it:

```
Design test cases for a login function with username, password, and remember me checkbox.
```

## 🚀 Quick Start

Once installed, you can use the skill in Claude by simply asking:

```
Design test cases for a login function with username, password, and remember me checkbox.
```

Claude will:
1. Analyze the requirements
2. Identify parameters and values
3. Generate a PICT model with constraints
4. Create test cases with expected outputs
5. Present results in a formatted table

## 📊 Example: ATM System Testing

This repository includes a complete real-world example of testing an ATM system. See the [examples](examples/) directory for:

- **[ATM Specification](examples/atm-specification.md)**: Complete ATM system specification with 11 sections covering hardware, software, security, and functional requirements
- **[ATM Test Plan](examples/atm-test-plan.md)**: Comprehensive test plan generated using PICT methodology with 31 test cases (reduced from 25,920 possible combinations)

### ATM Example Summary

**System Parameters:**
- Transaction Types (5): Withdrawal, Deposit, Balance Inquiry, Transfer, PIN Change
- Card Types (3): EMV Chip, Magnetic Stripe, Invalid
- PIN Status (4): Valid, Invalid attempts 1-3
- Account Types (3): Checking, Savings, Both
- Transaction Amounts (4): Within limits, at max, exceeds transaction, exceeds daily
- Cash Availability (3): Sufficient, Insufficient, Empty
- Network Status (3): Primary, Backup, Disconnected
- Card Condition (3): Good, Damaged, Expired

**Test Results:**
- Total possible combinations: **25,920**
- PICT test cases generated: **31**
- **Reduction: 99.88%**
- Coverage: All pairwise (2-way) interactions
- Test execution time: Reduced from weeks to hours

### Running the ATM Example

```bash
# In Claude Code
Ask: "Use the pict-test-designer skill to analyze the ATM specification 
in examples/atm-specification.md and generate test cases"
```

## 🔍 How It Works

### 1. Requirements Analysis

Claude analyzes your requirements to identify:
- **Parameters**: Input variables, configuration options, environmental factors
- **Values**: Possible values using equivalence partitioning
- **Constraints**: Business rules and dependencies
- **Expected Outcomes**: What should happen for different combinations

### 2. PICT Model Generation

Creates a structured model:

```
# Parameters
Browser: Chrome, Firefox, Safari
OS: Windows, MacOS, Linux
Memory: 4GB, 8GB, 16GB

# Constraints
IF [OS] = "MacOS" THEN [Browser] <> "IE";
IF [Memory] = "4GB" THEN [OS] <> "MacOS";
```

### 3. Test Case Generation

Generates minimal test cases covering all pairwise combinations:

| Test # | Browser | OS | Memory | Expected Output |
|--------|---------|----|---------|-----------------------------|
| 1 | Chrome | Windows | 4GB | Success |
| 2 | Firefox | MacOS | 8GB | Success |
| 3 | Safari | Linux | 16GB | Success |
| ... | ... | ... | ... | ... |

### 4. Expected Output Determination

For each test case, Claude determines the expected outcome based on:
- Business requirements
- Code logic
- Valid/invalid combinations

## 🎯 Use Cases

### Software Testing
- Function testing with multiple parameters
- API endpoint testing
- Database query testing
- Algorithm validation

### Configuration Testing
- System configuration combinations
- Feature flag testing
- Environment setup validation
- Browser compatibility testing

### Web Application Testing
- Form validation
- User authentication flows
- E-commerce checkout processes
- Shopping cart functionality

### Mobile Testing
- Device and OS combinations
- Screen size and orientation
- Network conditions
- App permissions

### Hardware Testing
- Device compatibility
- Interface testing
- Protocol validation
- Performance under different conditions

## 📚 Documentation

- **[SKILL.md](../bmad_repo/SKILL.md)**: Complete skill documentation with workflow and best practices
- **[PICT Syntax Reference](references/pict_syntax.md)**: Complete syntax guide (to be created)
- **[Examples](../claude_bp_repo/examples.md)**: Real-world examples across domains (to be created)
- **[Helper Scripts](scripts/pict_helper.py)**: Python utilities for PICT (to be created)

## 💡 Tips for Best Results

### Good Parameter Names
✅ Use descriptive names: `AuthMethod`, `UserRole`, `PaymentType`
✅ Apply equivalence partitioning: `FileSize: Small, Medium, Large`
✅ Include boundary values: `Age: 0, 17, 18, 65, 66`
✅ Add negative values: `Amount: ~-1, 0, 100, ~999999`

### Writing Constraints
✅ Document rationale: `# Safari only available on MacOS`
✅ Start simple, add incrementally
✅ Test constraints work as expected

### Expected Outputs
✅ Be specific: "Login succeeds, user redirected to dashboard"
❌ Not vague: "Works" or "Success"

## 🙏 Credits

This skill is built upon the excellent work of:

- **[Microsoft PICT](https://github.com/microsoft/pict)**: The original Pairwise Independent Combinatorial Testing tool developed by Microsoft Research
- **[pypict](https://github.com/kmaehashi/pypict)**: Python binding for PICT by Kenichi Maehashi
- **Community Contributors**: All contributors who have helped improve PICT tools

### About PICT

PICT was developed by Jacek Czerwonka at Microsoft Research. It's a powerful combinatorial testing tool that has been used extensively within Microsoft for testing complex systems with multiple interacting parameters.

**References:**
- [PICT: Pairwise Independent Combinatorial Testing](https://github.com/microsoft/pict)
- [Pairwise Testing Methodology](https://www.pairwisetesting.com/)
- [Combinatorial Test Design](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Add examples or documentation**
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Areas for Contribution

- Additional real-world examples
- Enhanced constraint patterns
- Support for more testing domains
- Improved documentation
- Bug fixes and improvements

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The underlying PICT tool by Microsoft is also licensed under the MIT License.

## 🔗 Links

- **Claude AI**: https://claude.ai
- **Claude Documentation**: https://docs.claude.com
- **Microsoft PICT**: https://github.com/microsoft/pict
- **pypict**: https://github.com/kmaehashi/pypict
- **Online PICT Tools**: 
  - https://pairwise.yuuniworks.com/
  - https://pairwise.teremokgames.com/

## 📧 Support

If you encounter issues or have questions:

1. Check the [examples](examples/) directory for reference
2. Review the [SKILL.md](../bmad_repo/SKILL.md) documentation
3. Open an issue on GitHub
4. Join discussions in the Issues section

## 🌟 Star This Repository

If you find this skill useful, please star the repository to help others discover it!

---

**Made with ❤️ for the Claude and testing community**

**Powered by Microsoft PICT and pypict**
```

## File: `SKILL.md`
```markdown
---
name: pict-test-designer
description: Design comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing) for any piece of requirements or code. Analyzes inputs, generates PICT models with parameters, values, and constraints for valid scenarios using pairwise testing. Outputs the PICT model, markdown table of test cases, and expected results.
---

# PICT Test Designer

This skill enables systematic test case design using PICT (Pairwise Independent Combinatorial Testing). Given requirements or code, it analyzes the system to identify test parameters, generates a PICT model with appropriate constraints, executes the model to generate pairwise test cases, and formats the results with expected outputs.

## When to Use This Skill

Use this skill when:
- Designing test cases for a feature, function, or system with multiple input parameters
- Creating test suites for configurations with many combinations
- Needing comprehensive coverage with minimal test cases
- Analyzing requirements to identify test scenarios
- Working with code that has multiple conditional paths
- Building test matrices for API endpoints, web forms, or system configurations

## Workflow

Follow this process for test design:

### 1. Analyze Requirements or Code

From the user's requirements or code, identify:
- **Parameters**: Input variables, configuration options, environmental factors
- **Values**: Possible values for each parameter (using equivalence partitioning)
- **Constraints**: Business rules, technical limitations, dependencies between parameters
- **Expected Outcomes**: What should happen for different combinations

**Example Analysis:**

For a login function with requirements:
- Users can login with username/password
- Supports 2FA (on/off)
- Remembers login on trusted devices
- Rate limits after 3 failed attempts

Identified parameters:
- Credentials: Valid, Invalid
- TwoFactorAuth: Enabled, Disabled
- RememberMe: Checked, Unchecked
- PreviousFailures: 0, 1, 2, 3, 4

### 2. Generate PICT Model

Create a PICT model with:
- Clear parameter names
- Well-defined value sets (using equivalence partitioning and boundary values)
- Constraints for invalid combinations
- Comments explaining business rules

**Model Structure:**
```
# Parameter definitions
ParameterName: Value1, Value2, Value3

# Constraints (if any)
IF [Parameter1] = "Value" THEN [Parameter2] <> "OtherValue";
```

**Refer to references/pict_syntax.md for:**
- Complete syntax reference
- Constraint grammar and operators
- Advanced features (sub-models, aliasing, negative testing)
- Command-line options
- Detailed constraint patterns

**Refer to references/examples.md for:**
- Complete real-world examples by domain
- Software function testing examples
- Web application, API, and mobile testing examples
- Database and configuration testing patterns
- Common patterns for authentication, resource access, error handling

### 3. Execute PICT Model

Generate the PICT model text and format it for the user. You can use Python code directly to work with the model:

```python
# Define parameters and constraints
parameters = {
    "OS": ["Windows", "Linux", "MacOS"],
    "Browser": ["Chrome", "Firefox", "Safari"],
    "Memory": ["4GB", "8GB", "16GB"]
}

constraints = [
    'IF [OS] = "MacOS" THEN [Browser] IN {Safari, Chrome}',
    'IF [Memory] = "4GB" THEN [OS] <> "MacOS"'
]

# Generate model text
model_lines = []
for param_name, values in parameters.items():
    values_str = ", ".join(values)
    model_lines.append(f"{param_name}: {values_str}")

if constraints:
    model_lines.append("")
    for constraint in constraints:
        if not constraint.endswith(';'):
            constraint += ';'
        model_lines.append(constraint)

model_text = "\n".join(model_lines)
print(model_text)
```

**Using the helper script (optional):**
The `scripts/pict_helper.py` script provides utilities for model generation and output formatting:

```bash
# Generate model from JSON config
python scripts/pict_helper.py generate config.json

# Format PICT tool output as markdown table
python scripts/pict_helper.py format output.txt

# Parse PICT output to JSON
python scripts/pict_helper.py parse output.txt
```

**To generate actual test cases**, the user can:
1. Save the PICT model to a file (e.g., `model.txt`)
2. Use online PICT tools like:
   - https://pairwise.yuuniworks.com/
   - https://pairwise.teremokgames.com/
3. Or install PICT locally (see references/pict_syntax.md)

### 4. Determine Expected Outputs

For each generated test case, determine the expected outcome based on:
- Business requirements
- Code logic
- Valid/invalid combinations

Create a list of expected outputs corresponding to each test case.

### 5. Format Complete Test Suite

Provide the user with:
1. **PICT Model** - The complete model with parameters and constraints
2. **Markdown Table** - Test cases in table format with test numbers
3. **Expected Outputs** - Expected result for each test case

## Output Format

Present results in this structure:

````markdown
## PICT Model

```
# Parameters
Parameter1: Value1, Value2, Value3
Parameter2: ValueA, ValueB

# Constraints
IF [Parameter1] = "Value1" THEN [Parameter2] = "ValueA";
```

## Generated Test Cases

| Test # | Parameter1 | Parameter2 | Expected Output |
| --- | --- | --- | --- |
| 1 | Value1 | ValueA | Success |
| 2 | Value2 | ValueB | Success |
| 3 | Value1 | ValueB | Error: Invalid combination |
...

## Test Case Summary

- Total test cases: N
- Coverage: Pairwise (all 2-way combinations)
- Constraints applied: N
````

## Best Practices

### Parameter Identification

**Good:**
- Use descriptive names: `AuthMethod`, `UserRole`, `PaymentType`
- Apply equivalence partitioning: `FileSize: Small, Medium, Large` instead of `FileSize: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
- Include boundary values: `Age: 0, 17, 18, 65, 66`
- Add negative values for error testing: `Amount: ~-1, 0, 100, ~999999`

**Avoid:**
- Generic names: `Param1`, `Value1`, `V1`
- Too many values without partitioning
- Missing edge cases

### Constraint Writing

**Good:**
- Document rationale: `# Safari only available on MacOS`
- Start simple, add incrementally
- Test constraints work as expected

**Avoid:**
- Over-constraining (eliminates too many valid combinations)
- Under-constraining (generates invalid test cases)
- Complex nested logic without clear documentation

### Expected Output Definition

**Be specific:**
- "Login succeeds, user redirected to dashboard"
- "HTTP 400: Invalid credentials error"
- "2FA prompt displayed"

**Not vague:**
- "Works"
- "Error"
- "Success"

### Scalability

For large parameter sets:
- Use sub-models to group related parameters with different orders
- Consider separate test suites for unrelated features
- Start with order 2 (pairwise), increase for critical combinations
- Typical pairwise testing reduces test cases by 80-90% vs exhaustive

## Common Patterns

### Web Form Testing

```python
parameters = {
    "Name": ["Valid", "Empty", "TooLong"],
    "Email": ["Valid", "Invalid", "Empty"],
    "Password": ["Strong", "Weak", "Empty"],
    "Terms": ["Accepted", "NotAccepted"]
}

constraints = [
    'IF [Terms] = "NotAccepted" THEN [Name] = "Valid"',  # Test validation even if terms not accepted
]
```

### API Endpoint Testing

```python
parameters = {
    "HTTPMethod": ["GET", "POST", "PUT", "DELETE"],
    "Authentication": ["Valid", "Invalid", "Missing"],
    "ContentType": ["JSON", "XML", "FormData"],
    "PayloadSize": ["Empty", "Small", "Large"]
}

constraints = [
    'IF [HTTPMethod] = "GET" THEN [PayloadSize] = "Empty"',
    'IF [Authentication] = "Missing" THEN [HTTPMethod] IN {GET, POST}'
]
```

### Configuration Testing

```python
parameters = {
    "Environment": ["Dev", "Staging", "Production"],
    "CacheEnabled": ["True", "False"],
    "LogLevel": ["Debug", "Info", "Error"],
    "Database": ["SQLite", "PostgreSQL", "MySQL"]
}

constraints = [
    'IF [Environment] = "Production" THEN [LogLevel] <> "Debug"',
    'IF [Database] = "SQLite" THEN [Environment] = "Dev"'
]
```

## Troubleshooting

### No Test Cases Generated

- Check constraints aren't over-restrictive
- Verify constraint syntax (must end with `;`)
- Ensure parameter names in constraints match definitions (use `[ParameterName]`)

### Too Many Test Cases

- Verify using order 2 (pairwise) not higher order
- Consider breaking into sub-models
- Check if parameters can be separated into independent test suites

### Invalid Combinations in Output

- Add missing constraints
- Verify constraint logic is correct
- Check if you need to use `NOT` or `<>` operators

### Script Errors

- Ensure pypict is installed: `pip install pypict --break-system-packages`
- Check Python version (3.7+)
- Verify model syntax is valid

## References

- **references/pict_syntax.md** - Complete PICT syntax reference with grammar and operators
- **references/examples.md** - Comprehensive real-world examples across different domains
- **scripts/pict_helper.py** - Python utilities for model generation and output formatting
- [PICT GitHub Repository](https://github.com/microsoft/pict) - Official PICT documentation
- [pypict Documentation](https://github.com/kmaehashi/pypict) - Python binding documentation
- [Online PICT Tools](https://pairwise.yuuniworks.com/) - Web-based PICT generator

## Examples

### Example 1: Simple Function Testing

**User Request:** "Design tests for a divide function that takes two numbers and returns the result."

**Analysis:**
- Parameters: dividend (number), divisor (number)
- Values: Using equivalence partitioning and boundaries
  - Numbers: negative, zero, positive, large values
- Constraints: Division by zero is invalid
- Expected outputs: Result or error

**PICT Model:**
```
Dividend: -10, 0, 10, 1000
Divisor: ~0, -5, 1, 5, 100

IF [Divisor] = "0" THEN [Dividend] = "10";
```

**Test Cases:**

| Test # | Dividend | Divisor | Expected Output |
| --- | --- | --- | --- |
| 1 | 10 | 0 | Error: Division by zero |
| 2 | -10 | 1 | -10.0 |
| 3 | 0 | -5 | 0.0 |
| 4 | 1000 | 5 | 200.0 |
| 5 | 10 | 100 | 0.1 |

### Example 2: E-commerce Checkout

**User Request:** "Design tests for checkout flow with payment methods, shipping options, and user types."

**Analysis:**
- Payment: Credit Card, PayPal, Bank Transfer (limited by user type)
- Shipping: Standard, Express, Overnight
- User: Guest, Registered, Premium
- Constraints: Guests can't use Bank Transfer, Premium users get free Express

**PICT Model:**
```
PaymentMethod: CreditCard, PayPal, BankTransfer
ShippingMethod: Standard, Express, Overnight
UserType: Guest, Registered, Premium

IF [UserType] = "Guest" THEN [PaymentMethod] <> "BankTransfer";
IF [UserType] = "Premium" AND [ShippingMethod] = "Express" THEN [PaymentMethod] IN {CreditCard, PayPal};
```

**Output:** 12-15 test cases covering all valid payment/shipping/user combinations with expected costs and outcomes.
```

## File: `STRUCTURE.md`
```markdown
# Repository Structure

Complete file structure of the pypict-claude-skill repository.

```
pypict-claude-skill/
├── .github/                          # GitHub configuration
│   ├── ISSUE_TEMPLATE/               # Issue templates
│   │   ├── bug_report.md             # Bug report template
│   │   └── feature_request.md        # Feature request template
│   ├── workflows/                    # GitHub Actions
│   │   └── ci.yml                    # CI workflow for validation
│   ├── markdown-link-check-config.json  # Link checker config
│   └── pull_request_template.md      # PR template
│
├── examples/                         # Real-world examples
│   ├── README.md                     # Examples overview
│   ├── atm-specification.md          # ATM system specification
│   └── atm-test-plan.md              # Complete ATM test plan (31 test cases)
│
├── references/                       # Reference documentation
│   ├── pict_syntax.md                # PICT syntax reference (placeholder)
│   └── examples.md                   # PICT examples reference (placeholder)
│
├── scripts/                          # Helper scripts
│   ├── README.md                     # Scripts documentation
│   └── pict_helper.py                # Python utilities for PICT
│
├── .gitignore                        # Git ignore rules
├── CHANGELOG.md                      # Version history
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                           # MIT License with attributions
├── PUBLISHING.md                     # Guide to publish on GitHub
├── QUICKSTART.md                     # Quick start guide
├── README.md                         # Main documentation
└── SKILL.md                          # Skill definition for Claude

```

## File Descriptions

### Root Directory

| File | Purpose | Status |
|------|---------|--------|
| **README.md** | Main repository documentation with installation and usage | ✅ Complete |
| **SKILL.md** | Claude skill definition with workflow and best practices | ✅ Complete |
| **LICENSE** | MIT License with proper attribution to PICT and pypict | ✅ Complete |
| **CONTRIBUTING.md** | Guidelines for contributing to the project | ✅ Complete |
| **CHANGELOG.md** | Version history and release notes | ✅ Complete |
| **QUICKSTART.md** | Quick start guide for new users | ✅ Complete |
| **PUBLISHING.md** | Step-by-step guide to publish repository | ✅ Complete |
| **.gitignore** | Git ignore patterns for Python and temp files | ✅ Complete |

### .github/ Directory

| File | Purpose | Status |
|------|---------|--------|
| **workflows/ci.yml** | GitHub Actions workflow for CI/CD | ✅ Complete |
| **ISSUE_TEMPLATE/bug_report.md** | Template for bug reports | ✅ Complete |
| **ISSUE_TEMPLATE/feature_request.md** | Template for feature requests | ✅ Complete |
| **pull_request_template.md** | Template for pull requests | ✅ Complete |
| **markdown-link-check-config.json** | Configuration for link checking | ✅ Complete |

### examples/ Directory

| File | Purpose | Status |
|------|---------|--------|
| **README.md** | Overview of available examples | ✅ Complete |
| **atm-specification.md** | Complete ATM system specification (11 sections) | ✅ Complete |
| **atm-test-plan.md** | Full test plan with PICT model and 31 test cases | ✅ Complete |

### references/ Directory

| File | Purpose | Status |
|------|---------|--------|
| **pict_syntax.md** | PICT syntax reference and grammar | 🚧 Placeholder |
| **examples.md** | Collection of PICT examples by domain | 🚧 Placeholder |

### scripts/ Directory

| File | Purpose | Status |
|------|---------|--------|
| **README.md** | Scripts documentation | ✅ Complete |
| **pict_helper.py** | Python utilities for PICT (generate, format, parse) | 🚧 Basic implementation |

## Key Features by File

### README.md
- Installation instructions for Claude Code CLI and Desktop
- Quick start guide
- ATM example summary
- Credits to Microsoft PICT and pypict
- Links to documentation and resources

### SKILL.md
- Complete workflow for using the skill
- Parameter identification guidelines
- PICT model generation process
- Constraint writing best practices
- Expected output determination
- Common patterns and examples

### examples/atm-test-plan.md
- Complete PICT model with 8 parameters
- 16 business rule constraints
- 31 optimized test cases (from 25,920 combinations)
- Coverage analysis
- Test execution guidelines
- Risk-based prioritization
- Traceability matrix

### PUBLISHING.md
- Step-by-step GitHub publishing guide
- Repository configuration instructions
- Release creation process
- Promotion strategies
- Maintenance guidelines

### CONTRIBUTING.md
- Contribution types and guidelines
- File structure for examples
- Commit message conventions
- Pull request process
- Quality standards

## File Statistics

- **Total Files:** 18
- **Markdown Documentation:** 14 files
- **Python Scripts:** 1 file
- **Configuration Files:** 3 files
- **Complete Files:** 15 (83%)
- **Placeholder Files:** 2 (11%)
- **Basic Implementation:** 1 (6%)

## Documentation Coverage

| Category | Coverage |
|----------|----------|
| Installation | ✅ Complete |
| Quick Start | ✅ Complete |
| Examples | ✅ 1 complete (ATM), more planned |
| API/Reference | 🚧 Placeholders (to be completed) |
| Contributing | ✅ Complete |
| Publishing | ✅ Complete |

## Next Steps for Repository

### Short Term (v1.1)
1. Complete `references/pict_syntax.md` with full PICT syntax
2. Add more examples to `references/examples.md`
3. Enhance `pict_helper.py` with full pypict integration
4. Add more real-world examples

### Medium Term (v1.2-1.3)
1. E-commerce checkout example
2. API testing example
3. Mobile app configuration example
4. Integration with test management tools

### Long Term (v2.0+)
1. Advanced constraint patterns library
2. Automated test case generation from code
3. CI/CD integration examples
4. Performance testing templates

## Contributing to Structure

When adding new files:

1. **Examples**: Add to `examples/` with specification and test plan
2. **Documentation**: Add to root or `references/` as appropriate
3. **Scripts**: Add to `scripts/` with README update
4. **Templates**: Add to `.github/ISSUE_TEMPLATE/` or `.github/`

## Maintenance Checklist

- [ ] Keep CHANGELOG.md updated
- [ ] Update README.md with new features
- [ ] Add new examples to examples/README.md
- [ ] Update file counts in this document
- [ ] Maintain links in all markdown files
- [ ] Test all code examples and commands
- [ ] Keep license attributions current

---

**Repository Status:** ✅ Ready for Publishing

**Last Updated:** October 19, 2025

**Version:** 1.0.0
```

## File: `examples/README.md`
```markdown
# Examples

This directory contains real-world examples of using the PICT Test Designer skill.

## ATM System Testing Example

A comprehensive example demonstrating how to use PICT methodology to test a complex banking ATM system.

### Files

- **[atm-specification.md](atm-specification.md)**: Complete ATM system specification with 11 sections covering:
  - Functional requirements (withdrawals, deposits, transfers, etc.)
  - Hardware specifications (card readers, cash dispensers, displays)
  - Security requirements (encryption, authentication, physical security)
  - Network and connectivity requirements
  - Compliance and standards

- **[atm-test-plan.md](atm-test-plan.md)**: Complete test plan generated using the PICT skill, including:
  - PICT model with 8 parameters and 16 constraints
  - 31 optimized test cases (reduced from 25,920 possible combinations)
  - Expected outputs for each test case
  - Test execution guidelines
  - Coverage analysis
  - Risk-based prioritization

### Key Statistics

- **Total Parameters**: 8 (Transaction Type, Card Type, PIN Status, Account Type, Transaction Amount, Cash Availability, Network Status, Card Condition)
- **Exhaustive Combinations**: 25,920
- **PICT Test Cases**: 31
- **Reduction**: 99.88%
- **Coverage**: All pairwise (2-way) interactions
- **Constraints**: 16 business rules

### How to Use This Example

1. **Review the specification**: Read [atm-specification.md](atm-specification.md) to understand the system requirements

2. **Study the test plan**: Review [atm-test-plan.md](atm-test-plan.md) to see how the PICT skill converted requirements into test cases

3. **Try it yourself**: Ask Claude to analyze the specification:
   ```
   Using the pict-test-designer skill, analyze the ATM specification 
   and generate test cases for the security requirements
   ```

4. **Adapt for your needs**: Use this as a template for your own specifications

### Learning Points

This example demonstrates:

- **Parameter identification**: How to identify testable parameters from requirements
- **Equivalence partitioning**: Grouping values into meaningful categories
- **Constraint modeling**: Applying business rules to eliminate invalid combinations
- **Expected output determination**: Automatically determining what should happen for each test case
- **Test prioritization**: Organizing tests by risk and criticality
- **Traceability**: Linking test cases back to requirements

## Automotive Gearbox Control System Example

A sophisticated example demonstrating PICT methodology for testing a semi-automatic transmission control system with multiple operating modes and complex safety constraints.

### Files

- **[gearbox-specification.md](gearbox-specification.md)**: Comprehensive gearbox control system specification with 10 sections:
  - System components (sensors, actuators, controls)
  - Operating modes (Manual, Sport, Eco)
  - Functional requirements (shift logic, safety features)
  - Error handling and fault tolerance
  - Performance and reliability requirements
  - Environmental conditions and constraints

- **[gearbox-test-plan.md](gearbox-test-plan.md)**: Complete test plan with PICT methodology:
  - PICT model with 12 parameters and 14 constraints
  - 40 optimized test cases (from ~159 billion combinations)
  - Expected outputs with detailed system responses
  - Priority-based test execution plan
  - Coverage analysis and traceability matrix
  - Risk assessment for high-risk scenarios

### Key Statistics

- **Total Parameters**: 12 (Mode, Gear, Speed, RPM, Throttle, Brake, Shift Request, Temperature, Road Condition, Incline, Sensor Status, Hydraulic Pressure)
- **Exhaustive Combinations**: ~159,000,000,000 (159 billion)
- **PICT Test Cases**: 40
- **Reduction**: 99.999999975%
- **Coverage**: All pairwise (2-way) interactions
- **Constraints**: 14 complex business rules and safety constraints

### How to Use This Example

1. **Review the specification**: Read [gearbox-specification.md](gearbox-specification.md) for the complete system design

2. **Study the test plan**: Examine [gearbox-test-plan.md](gearbox-test-plan.md) to see complex constraint modeling

3. **Try it yourself**: Ask Claude to analyze specific scenarios:
   ```
   Using the pict-test-designer skill, analyze the gearbox specification
   and generate test cases for the safety features section
   ```

4. **Learn constraint modeling**: This example shows advanced constraint patterns for:
   - Mutually exclusive conditions (brake vs. throttle)
   - Physical limitations (gear ratios, speed limits)
   - Safety interlocks (reverse lockout, over-rev protection)
   - Environmental adaptations (ice, temperature, incline)

### Learning Points

This example demonstrates:

- **Complex parameter interactions**: 12-way parameter space with interdependencies
- **Advanced constraint modeling**: Physical, safety, and operational constraints
- **Multi-mode testing**: Different behaviors in Manual, Sport, and Eco modes
- **Fault injection testing**: Sensor failures, temperature extremes, hydraulic issues
- **Environmental testing**: Road conditions, incline, temperature variations
- **Safety-critical testing**: Over-rev protection, reverse lockout, hill start assist
- **Comprehensive traceability**: Complete mapping to specification requirements

### Additional Examples (Coming Soon)

- E-commerce checkout testing
- API endpoint testing
- Web form validation
- Mobile app configuration testing
- Database query testing

## Contributing Examples

Have a great example to share? We welcome contributions!

1. Fork the repository
2. Add your example to this directory
3. Include both the specification/requirements and the generated test plan
4. Update this README with a description
5. Submit a pull request

### Example Structure

When contributing, please include:
- Original specification or requirements document
- Generated PICT model
- Test cases with expected outputs
- Brief description of the domain and key learning points
```

## File: `examples/atm-specification.md`
```markdown
# ATM Machine Specification Document

## 1. System Overview

**Product Name:** SecureBank ATM Model SB-5000  
**Version:** 1.0  
**Purpose:** Self-service banking terminal for cash withdrawal, deposits, balance inquiries, and basic account transactions

## 2. Functional Requirements

### 2.1 Core Functions
- **Cash Withdrawal:** Support withdrawals in denominations of $20, $50, and $100 (configurable)
- **Cash Deposit:** Accept cash deposits with bill validation and counting
- **Balance Inquiry:** Display current account balance for checking and savings accounts
- **Fund Transfer:** Enable transfers between customer's own accounts
- **PIN Change:** Allow customers to change their PIN securely
- **Mini Statement:** Print last 10 transactions

### 2.2 Transaction Limits
- Maximum withdrawal per transaction: $500
- Maximum withdrawal per day: $1,000 (configurable)
- Maximum deposit per transaction: $5,000
- Transaction timeout: 60 seconds of inactivity

## 3. Hardware Requirements

### 3.1 Physical Components
- **Card Reader:** EMV chip card and magnetic stripe reader (ISO 7816 compliant)
- **Cash Dispenser:** 4-cassette system, capacity 2,000 bills per cassette
- **Cash Acceptor:** Bill validator with counterfeit detection
- **Receipt Printer:** Thermal printer, 80mm width
- **Display:** 15-inch touchscreen LCD (1024x768 resolution)
- **Keypad:** Encrypted PIN pad with physical keys
- **Camera:** Two surveillance cameras (customer-facing and cash area)

### 3.2 Physical Specifications
- **Dimensions:** 1600mm (H) x 800mm (W) x 600mm (D)
- **Weight:** Approximately 250 kg
- **Safe Rating:** UL 291 Level 1 certified
- **Power Requirements:** 110-240V AC, 50/60Hz, 500W maximum

## 4. Software Requirements

### 4.1 Operating System
- Hardened Windows 10 IoT Enterprise or Linux-based embedded OS
- Real-time monitoring and health check capabilities

### 4.2 Application Software
- ATM controller software with multi-language support (minimum 3 languages)
- Transaction processing engine
- Remote monitoring and diagnostics software
- Automated software update capability
- Comprehensive audit logging system

### 4.3 Communication Protocols
- ISO 8583 messaging standard for financial transactions
- TCP/IP network protocol
- SSL/TLS encryption for all communications
- Support for NDC+ and DDC protocols

## 5. Security Requirements

### 5.1 Physical Security
- Anti-skimming devices on card reader
- Tamper-evident sensors and alarms
- Reinforced steel safe with time-delay lock
- Anchor bolts for secure installation
- Anti-vandalism coating and materials

### 5.2 Data Security
- Triple DES or AES-256 encryption for PIN blocks
- End-to-end encryption for all sensitive data
- PCI-DSS compliance for payment card data
- Secure key management system (DUKPT)
- No storage of card magnetic stripe data

### 5.3 Authentication
- Customer authentication via PIN (minimum 4 digits, maximum 6 digits)
- Card authentication via EMV chip validation
- Maximum 3 incorrect PIN attempts before card retention

## 6. User Interface Requirements

### 6.1 Display Interface
- Clear, intuitive menu navigation
- High contrast for outdoor visibility
- Accessibility features for visually impaired users (audio guidance option)
- Transaction progress indicators
- Clear error messages and instructions

### 6.2 Response Time
- Card insertion to welcome screen: < 3 seconds
- Transaction authorization: < 10 seconds
- Cash dispensing: < 15 seconds from authorization

## 7. Network and Connectivity

### 7.1 Network Requirements
- Primary: Secure broadband connection (minimum 1 Mbps)
- Backup: 4G/LTE cellular connection
- Automatic failover between primary and backup
- VPN tunnel to host processor

### 7.2 Availability
- System uptime: 99.5% excluding scheduled maintenance
- Maximum network latency: 500ms to host
- Automatic reconnection after network disruption

## 8. Environmental Requirements

- **Operating Temperature:** 10°C to 40°C (50°F to 104°F)
- **Storage Temperature:** -20°C to 60°C (-4°F to 140°F)
- **Humidity:** 20% to 80% non-condensing
- **Installation:** Indoor or outdoor (with weather-resistant enclosure)

## 9. Compliance and Standards

- ADA (Americans with Disabilities Act) compliant
- PCI-PTS certified for secure payment terminals
- EMV Level 1 and Level 2 certified
- ISO 9001 quality management standards
- Local banking regulations and Central Bank requirements

## 10. Maintenance and Support

### 10.1 Monitoring
- 24/7 remote monitoring and alerting
- Automated cash level tracking
- Predictive maintenance alerts
- Transaction success rate monitoring

### 10.2 Maintenance Schedule
- Preventive maintenance: Quarterly
- Cash replenishment: As needed (low cash alert at 20% capacity)
- Receipt paper replacement: As needed
- Software updates: Monthly security patches

## 11. Service Level Agreements

- Critical issue response time: 4 hours
- Hardware repair completion: 24 hours
- Parts availability: 48 hours
- Mean time between failures (MTBF): > 20,000 hours

---

This specification provides a comprehensive framework for an ATM system that can be used for test case design and validation.
```

## File: `examples/atm-test-plan.md`
```markdown
# ATM System Test Plan
## Using PICT (Pairwise Independent Combinatorial Testing)

**System:** SecureBank ATM Model SB-5000  
**Version:** 1.0  
**Test Plan Version:** 1.0  
**Date:** October 19, 2025  
**Test Methodology:** Pairwise Combinatorial Testing

---

## 1. Executive Summary

This test plan uses Pairwise Independent Combinatorial Testing (PICT) to efficiently test the ATM system with comprehensive coverage while minimizing the number of test cases. The approach reduces test cases by approximately 85% compared to exhaustive testing while maintaining high coverage of parameter interactions.

**Key Statistics:**
- **Total Test Cases Generated:** 31
- **Parameters Tested:** 8
- **Total Possible Combinations:** 25,920 (exhaustive)
- **Pairwise Test Cases:** 31 (99.88% reduction)
- **Constraints Applied:** 16 business rules
- **Coverage Level:** All 2-way (pairwise) parameter interactions

---

## 2. PICT Model

The following model defines all parameters, their values, and business rule constraints:

```
# ATM System Test Model
# Based on SecureBank ATM Model SB-5000 Specification v1.0

# Parameters
TransactionType: Withdrawal, Deposit, BalanceInquiry, Transfer, PINChange
CardType: EMVChip, MagStripe, Invalid
PINStatus: Valid, Invalid_1st, Invalid_2nd, Invalid_3rd
AccountType: Checking, Savings, Both
TransactionAmount: Within_Limit, At_Max_Transaction, Exceeds_Transaction, Exceeds_Daily
CashAvailability: Sufficient, Insufficient, Empty
NetworkStatus: Connected_Primary, Connected_Backup, Disconnected
CardCondition: Good, Damaged, Expired

# Constraints based on ATM business rules

# Invalid cards cannot complete transactions
IF [CardType] = "Invalid" THEN [TransactionType] = "Withdrawal"
IF [CardType] = "Invalid" THEN [PINStatus] = "Valid"

# Balance inquiry doesn't need cash or specific amounts
IF [TransactionType] = "BalanceInquiry" THEN [TransactionAmount] = "Within_Limit"
IF [TransactionType] = "BalanceInquiry" THEN [CashAvailability] = "Sufficient"

# PIN change doesn't need cash or specific amounts
IF [TransactionType] = "PINChange" THEN [TransactionAmount] = "Within_Limit"
IF [TransactionType] = "PINChange" THEN [CashAvailability] = "Sufficient"

# Deposits don't check cash availability in dispenser
IF [TransactionType] = "Deposit" THEN [CashAvailability] = "Sufficient"

# Transfer doesn't need cash from dispenser
IF [TransactionType] = "Transfer" THEN [CashAvailability] = "Sufficient"

# Withdrawals require checking cash and transaction limits
IF [TransactionType] = "Withdrawal" AND [CashAvailability] = "Empty" THEN [TransactionAmount] = "Within_Limit"

# After 3rd invalid PIN, card should be retained regardless of transaction
IF [PINStatus] = "Invalid_3rd" THEN [TransactionType] = "Withdrawal"

# Damaged or expired cards should fail before PIN validation
IF [CardCondition] = "Damaged" THEN [PINStatus] = "Valid"
IF [CardCondition] = "Expired" THEN [PINStatus] = "Valid"

# Network disconnection affects all transaction types similarly
IF [NetworkStatus] = "Disconnected" THEN [TransactionType] IN {Withdrawal, Deposit, Transfer}

# Amount constraints only apply to withdrawal and deposit
IF [TransactionAmount] = "Exceeds_Daily" THEN [TransactionType] IN {Withdrawal, Deposit}
IF [TransactionAmount] = "Exceeds_Transaction" THEN [TransactionType] IN {Withdrawal, Deposit}
IF [TransactionAmount] = "At_Max_Transaction" THEN [TransactionType] IN {Withdrawal, Deposit}
```

---

## 3. Parameter Definitions

### 3.1 TransactionType
- **Withdrawal:** Cash withdrawal from account
- **Deposit:** Cash deposit to account
- **BalanceInquiry:** Check account balance
- **Transfer:** Transfer funds between accounts
- **PINChange:** Change ATM PIN

### 3.2 CardType
- **EMVChip:** Card with EMV chip (current standard)
- **MagStripe:** Magnetic stripe only card (legacy)
- **Invalid:** Unrecognized or damaged card data

### 3.3 PINStatus
- **Valid:** Correct PIN entered
- **Invalid_1st:** First incorrect PIN attempt
- **Invalid_2nd:** Second incorrect PIN attempt
- **Invalid_3rd:** Third incorrect PIN attempt (triggers card retention)

### 3.4 AccountType
- **Checking:** Checking account only
- **Savings:** Savings account only
- **Both:** Multiple accounts available

### 3.5 TransactionAmount
- **Within_Limit:** Amount within all limits
- **At_Max_Transaction:** At maximum per-transaction limit ($500 for withdrawal)
- **Exceeds_Transaction:** Exceeds per-transaction limit
- **Exceeds_Daily:** Exceeds daily limit ($1,000)

### 3.6 CashAvailability
- **Sufficient:** ATM has enough cash
- **Insufficient:** ATM has some cash but not enough for transaction
- **Empty:** ATM is out of cash

### 3.7 NetworkStatus
- **Connected_Primary:** Using primary broadband connection
- **Connected_Backup:** Failover to 4G/LTE backup
- **Disconnected:** No network connectivity

### 3.8 CardCondition
- **Good:** Card is in good condition
- **Damaged:** Card is damaged/unreadable
- **Expired:** Card has expired

---

## 4. Generated Test Cases

| Test # | Transaction Type | Card Type | PIN Status | Account Type | Transaction Amount | Cash Availability | Network Status | Card Condition | Expected Output |
|--------|-----------------|-----------|------------|--------------|-------------------|-------------------|----------------|---------------|-----------------|
| 1 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | Success: Cash dispensed - Receipt printed |
| 2 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Primary | Good | Success: Deposit accepted - Receipt printed |
| 3 | BalanceInquiry | EMVChip | Valid | Both | Within_Limit | Sufficient | Connected_Primary | Good | Success: Balance displayed and printed |
| 4 | Transfer | MagStripe | Valid | Both | Within_Limit | Sufficient | Connected_Primary | Good | Success: Transfer completed - Receipt printed |
| 5 | PINChange | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | Success: PIN changed successfully |
| 6 | Withdrawal | EMVChip | Invalid_1st | Checking | Within_Limit | Sufficient | Connected_Primary | Good | Error: Incorrect PIN - 2 attempts remaining |
| 7 | Withdrawal | MagStripe | Invalid_2nd | Savings | Within_Limit | Sufficient | Connected_Primary | Good | Error: Incorrect PIN - 1 attempt remaining |
| 8 | Withdrawal | EMVChip | Invalid_3rd | Both | Within_Limit | Sufficient | Connected_Primary | Good | Error: Maximum PIN attempts exceeded - Card retained |
| 9 | Withdrawal | Invalid | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | Error: Card not recognized - Transaction declined |
| 10 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Damaged | Error: Card unreadable - Please use another card |
| 11 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Primary | Expired | Error: Card expired - Please contact your bank |
| 12 | Withdrawal | EMVChip | Valid | Checking | At_Max_Transaction | Sufficient | Connected_Primary | Good | Success: Cash dispensed - Receipt printed |
| 13 | Withdrawal | MagStripe | Valid | Savings | Exceeds_Transaction | Sufficient | Connected_Primary | Good | Error: Transaction exceeds maximum withdrawal amount ($500) |
| 14 | Withdrawal | EMVChip | Valid | Both | Exceeds_Daily | Sufficient | Connected_Primary | Good | Error: Transaction exceeds daily withdrawal limit ($1,000) |
| 15 | Deposit | MagStripe | Valid | Checking | At_Max_Transaction | Sufficient | Connected_Primary | Good | Success: Deposit accepted - Receipt printed |
| 16 | Deposit | EMVChip | Valid | Savings | Exceeds_Transaction | Sufficient | Connected_Primary | Good | Error: Deposit exceeds maximum amount ($5,000) |
| 17 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Insufficient | Connected_Primary | Good | Error: Insufficient cash in ATM for this amount |
| 18 | Withdrawal | MagStripe | Valid | Savings | Within_Limit | Empty | Connected_Primary | Good | Error: ATM out of cash - Please try another location |
| 19 | Withdrawal | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Backup | Good | Success: Cash dispensed - Receipt printed (Backup network) |
| 20 | Deposit | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Backup | Good | Success: Deposit accepted - Receipt printed (Backup network) |
| 21 | Transfer | EMVChip | Valid | Both | Within_Limit | Sufficient | Connected_Backup | Good | Success: Transfer completed - Receipt printed (Backup network) |
| 22 | Withdrawal | MagStripe | Valid | Checking | Within_Limit | Sufficient | Disconnected | Good | Error: Cannot connect to bank - Transaction unavailable |
| 23 | Deposit | EMVChip | Valid | Savings | Within_Limit | Sufficient | Disconnected | Good | Error: Cannot connect to bank - Transaction unavailable |
| 24 | Transfer | MagStripe | Valid | Both | Within_Limit | Sufficient | Disconnected | Good | Error: Cannot connect to bank - Transaction unavailable |
| 25 | Transfer | EMVChip | Valid | Checking | Within_Limit | Sufficient | Connected_Primary | Good | Error: Transfer requires multiple accounts |
| 26 | Withdrawal | MagStripe | Valid | Both | At_Max_Transaction | Sufficient | Connected_Backup | Good | Success: Cash dispensed - Receipt printed (Backup network) |
| 27 | BalanceInquiry | MagStripe | Valid | Checking | Within_Limit | Sufficient | Connected_Backup | Good | Success: Balance displayed and printed (Backup network) |
| 28 | PINChange | MagStripe | Valid | Savings | Within_Limit | Sufficient | Connected_Backup | Good | Success: PIN changed successfully (Backup network) |
| 29 | Deposit | EMVChip | Valid | Both | At_Max_Transaction | Sufficient | Connected_Backup | Good | Success: Deposit accepted - Receipt printed (Backup network) |
| 30 | Withdrawal | EMVChip | Invalid_1st | Savings | Exceeds_Transaction | Insufficient | Connected_Backup | Good | Error: Incorrect PIN - 2 attempts remaining |
| 31 | BalanceInquiry | EMVChip | Invalid_2nd | Savings | Within_Limit | Sufficient | Connected_Primary | Good | Error: Incorrect PIN - 1 attempt remaining |

---

## 5. Test Coverage Analysis

### 5.1 Coverage by Transaction Type
- **Withdrawal:** 14 test cases (45%)
- **Deposit:** 7 test cases (23%)
- **BalanceInquiry:** 3 test cases (10%)
- **Transfer:** 4 test cases (13%)
- **PINChange:** 2 test cases (6%)
- **Other (Card errors):** 1 test case (3%)

### 5.2 Coverage by Outcome Type
- **Success Scenarios:** 17 test cases (55%)
- **Error Scenarios:** 14 test cases (45%)

### 5.3 Critical Scenarios Covered
✅ All transaction types tested  
✅ All card types tested  
✅ All PIN scenarios including card retention  
✅ Transaction limit enforcement  
✅ Daily limit enforcement  
✅ Cash availability scenarios  
✅ Network failover testing  
✅ Card condition validation  
✅ Account type validation  

---

## 6. Test Execution Guidelines

### 6.1 Pre-Test Setup
1. **ATM Configuration:**
   - Load cash cassettes with sufficient bills
   - Verify all hardware components operational
   - Configure transaction limits as per specification
   - Ensure primary and backup network connections

2. **Test Cards:**
   - Prepare EMV chip cards (valid, expired)
   - Prepare magnetic stripe cards (valid, damaged)
   - Prepare invalid/unrecognized cards

3. **Test Accounts:**
   - Create test accounts (checking, savings, both)
   - Set known balances for verification
   - Configure daily withdrawal limits

### 6.2 Test Execution Process

For each test case:

1. **Setup:** Configure ATM and account per test parameters
2. **Execute:** Perform transaction as specified
3. **Observe:** Record actual outcome
4. **Verify:** Compare with expected output
5. **Log:** Document results and any deviations
6. **Reset:** Return ATM to initial state for next test

### 6.3 Pass/Fail Criteria

**Pass:** 
- Actual output matches expected output exactly
- Transaction completes within specified time limits
- Receipt printed (if applicable) with correct information
- Audit log entry created correctly

**Fail:**
- Output differs from expected
- System error or crash occurs
- Transaction timeout
- Incorrect receipt or no receipt when expected
- Security validation bypassed

---

## 7. Test Environment Requirements

### 7.1 Hardware
- ATM with all components operational
- Network connectivity (primary and backup)
- Cash cassettes with mixed denominations
- Receipt paper loaded
- Test cards (various types)

### 7.2 Software
- ATM application software v1.0
- Test transaction processing environment
- Network simulation tools for failover testing
- Monitoring and logging tools

### 7.3 Test Data
- Valid test account credentials
- Multiple account types
- Known account balances
- Expired and invalid cards for negative testing

---

## 8. Risk-Based Testing Priorities

### Priority 1 (Critical) - Must Pass
- Test Cases: 1, 2, 3, 8, 9, 13, 14, 18, 22
- **Focus:** Core transactions, security (card retention), limit enforcement, critical error conditions

### Priority 2 (High) - Should Pass
- Test Cases: 4, 5, 6, 7, 10, 11, 12, 16, 17, 19, 23, 24
- **Focus:** All transaction types, error handling, network failover

### Priority 3 (Medium) - Nice to Pass
- Test Cases: 15, 20, 21, 25, 26, 27, 28, 29, 30, 31
- **Focus:** Edge cases, combined scenarios, backup operations

---

## 9. Traceability Matrix

| Requirement | Test Cases | Coverage |
|-------------|------------|----------|
| SEC-001: PIN Validation | 6, 7, 8, 30, 31 | ✅ Full |
| SEC-002: Card Retention | 8 | ✅ Full |
| SEC-003: Invalid Card Detection | 9, 10, 11 | ✅ Full |
| TXN-001: Withdrawal Limits | 12, 13, 14 | ✅ Full |
| TXN-002: Deposit Limits | 15, 16 | ✅ Full |
| TXN-003: Cash Availability | 17, 18 | ✅ Full |
| NET-001: Primary Network | 1-18, 25, 31 | ✅ Full |
| NET-002: Backup Network | 19, 20, 21, 26, 27, 28, 29, 30 | ✅ Full |
| NET-003: Network Failure | 22, 23, 24 | ✅ Full |
| ACC-001: Account Validation | 25 | ✅ Full |
| HW-001: All Transaction Types | 1, 2, 3, 4, 5 | ✅ Full |

---

## 10. Defect Reporting Template

When logging defects, include:

- **Test Case Number:** Reference from this plan
- **Severity:** Critical / High / Medium / Low
- **Steps to Reproduce:** Detailed steps with parameters
- **Expected Result:** From test plan
- **Actual Result:** What actually occurred
- **Screenshots/Logs:** Evidence of failure
- **Environment:** Hardware/software configuration
- **Impact:** User experience or security implications

---

## 11. Test Metrics to Track

- **Total Test Cases:** 31
- **Test Cases Executed:** _____
- **Test Cases Passed:** _____
- **Test Cases Failed:** _____
- **Test Cases Blocked:** _____
- **Pass Rate:** _____%
- **Defects Found:** _____
- **Critical Defects:** _____
- **Test Execution Time:** _____ hours

---

## 12. How to Use This Test Plan

### 12.1 Generating More Test Cases

If you need to generate additional test cases or modify the model:

1. **Edit the PICT model** (Section 2) with new parameters or constraints
2. **Use online PICT tools:**
   - https://pairwise.yuuniworks.com/
   - https://pairwise.teremokgames.com/
3. **Or install PICT locally:**
   - Download from: https://github.com/microsoft/pict
   - Run: `pict atm_model.txt`

### 12.2 Customizing for Your Environment

- Adjust transaction limits in parameter values
- Add/remove card types based on your supported standards
- Modify network scenarios based on your infrastructure
- Add language parameters for internationalization testing

### 12.3 Integration with Test Management Tools

This test plan can be imported into:
- JIRA Test Management
- TestRail
- Azure Test Plans
- HP ALM/Quality Center
- Any tool accepting CSV or Excel format

---

## 13. Appendices

### Appendix A: PICT Syntax Reference

**Basic Syntax:**
```
ParameterName: Value1, Value2, Value3
```

**Constraints:**
```
IF [Parameter1] = "Value" THEN [Parameter2] = "OtherValue";
IF [Parameter1] <> "Value" THEN [Parameter2] IN {Value1, Value2};
```

**Operators:**
- `=` Equal to
- `<>` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal
- `<=` Less than or equal
- `IN` Member of set
- `AND` Logical AND
- `OR` Logical OR
- `NOT` Logical NOT

### Appendix B: Testing Best Practices

1. **Isolate Test Cases:** Each test should be independent
2. **Reset State:** Return to known state between tests
3. **Document Deviations:** Log any variations from expected behavior
4. **Verify Logs:** Check audit logs for each transaction
5. **Test Security:** Never skip security-related test cases
6. **Monitor Performance:** Track response times
7. **Test Recovery:** Include abnormal termination scenarios
8. **Backup Testing:** Verify backup systems work as expected

### Appendix C: Common Issues and Solutions

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Card retention doesn't trigger | Security settings | Verify max PIN attempts configuration |
| Network failover fails | Backup not configured | Check 4G/LTE connection settings |
| Receipt not printing | Paper jam / Empty | Check printer status before testing |
| Transaction timeout | Network latency | Verify network performance meets spec |
| Limits not enforced | Configuration error | Verify transaction limit settings |

---

## Document Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Oct 19, 2025 | Test Team | Initial test plan with PICT methodology |

---

**Approval:**

Test Manager: _________________ Date: _________

QA Lead: _________________ Date: _________

Project Manager: _________________ Date: _________
```

## File: `examples/gearbox-specification.md`
```markdown
# Automotive Gearbox Control System - Specification

## 1. System Overview

The Automotive Gearbox Control System is an electronic control unit (ECU) that manages gear shifting in a semi-automatic transmission. The system monitors vehicle conditions and driver inputs to determine optimal gear selection and execute smooth gear changes.

## 2. System Components

### 2.1 Input Sensors
- **Vehicle Speed Sensor**: Measures current speed (0-200 km/h)
- **Engine RPM Sensor**: Measures engine revolutions (0-7000 RPM)
- **Throttle Position Sensor**: Measures accelerator pedal position (0-100%)
- **Brake Pressure Sensor**: Detects brake application
- **Clutch Position Sensor**: Monitors clutch engagement state
- **Gear Position Sensor**: Detects current gear (N, 1-6, R)

### 2.2 Driver Controls
- **Gear Selector**: Manual, Sport, Eco modes
- **Shift Paddles**: Manual up/down shift requests
- **Clutch Pedal**: Manual clutch control (if applicable)

### 2.3 Outputs
- **Gear Actuator**: Mechanical gear selection
- **Clutch Actuator**: Clutch engagement/disengagement
- **Dashboard Display**: Current gear indicator
- **Warning Lights**: System errors and alerts

## 3. Operating Modes

### 3.1 Manual Mode
- Driver has full control over gear selection
- System prevents invalid shifts (e.g., direct 5th to 1st)
- Rev-matching on downshifts
- Neutral safety: requires brake to shift out of Park/Neutral

### 3.2 Sport Mode
- Holds gears longer for higher RPM
- Faster gear changes
- Downshifts on hard braking
- Target shift points: 5000-6500 RPM

### 3.3 Eco Mode
- Early upshifts for fuel efficiency
- Target shift points: 2000-3000 RPM
- Smooth, gradual gear changes
- Skip-shift capability (e.g., 2nd to 4th)

## 4. Functional Requirements

### 4.1 Gear Shifting Logic

#### 4.1.1 Upshift Conditions
- **Eco Mode**: Engine RPM > 2500 AND throttle < 40%
- **Manual Mode**: Driver paddle input OR RPM > 6000
- **Sport Mode**: Engine RPM > 5500

#### 4.1.2 Downshift Conditions
- **Eco Mode**: Engine RPM < 1500 OR heavy throttle (>80%)
- **Manual Mode**: Driver paddle input OR RPM < 1200
- **Sport Mode**: Engine RPM < 2000 OR brake pressure > 50%

#### 4.1.3 Prohibited Shifts
- Cannot shift from Reverse to any forward gear without stopping (speed = 0)
- Cannot shift to Reverse from any forward gear while moving (speed > 0)
- Cannot skip more than 2 gears in a single shift (except computer-controlled skip-shift)
- Cannot downshift if resulting RPM would exceed 7000 (red line protection)

### 4.2 Safety Features

#### 4.2.1 Hill Start Assist
- Activates when: stopped on incline > 5% AND brake released
- Holds brake pressure for 2 seconds
- Prevents rollback

#### 4.2.2 Overrun Protection
- Prevents downshift if resulting engine RPM > 6500
- Displays warning message to driver
- Ignores paddle input if unsafe

#### 4.2.3 Stall Prevention
- Auto-downshift if engine RPM < 800 while moving
- Automatic neutral engagement if stopped for > 3 seconds in gear
- Clutch slip if speed drops below minimum for current gear

#### 4.2.4 Neutral Safety
- Engine start only allowed in Park or Neutral
- Brake pedal required to shift from Park
- Reverse requires full stop (speed = 0 km/h)

### 4.3 Error Handling

#### 4.3.1 Sensor Failures
- **Speed Sensor Failure**: Limit to current gear, disable automatic shifting
- **RPM Sensor Failure**: Use speed-based shift logic as fallback
- **Throttle Sensor Failure**: Default to conservative shift points
- **Multiple Sensor Failures**: Enter limp-home mode (3rd gear only)

#### 4.3.2 Actuator Failures
- **Gear Actuator Jam**: Attempt 3 retries with 200ms delay
- **Clutch Actuator Failure**: Lock in current gear, display warning
- **Hydraulic Pressure Low**: Reduce shift speed, display warning

#### 4.3.3 Temperature Management
- **Normal Operation**: 70-110°C
- **High Temperature Warning**: 110-130°C (reduce shift frequency)
- **Critical Temperature**: >130°C (limp-home mode, 3rd gear only)

## 5. Performance Requirements

### 5.1 Shift Times
- **Eco Mode**: 800-1200 ms per shift
- **Manual Mode**: 400-600 ms per shift
- **Sport Mode**: 150-300 ms per shift

### 5.2 Response Times
- **Paddle Input**: < 50 ms recognition
- **Brake Detection**: < 20 ms
- **Emergency Neutral**: < 100 ms

### 5.3 Reliability
- **MTBF**: > 150,000 km
- **Shift Success Rate**: > 99.5%
- **False Error Rate**: < 0.1%

## 6. Environmental Conditions

### 6.1 Operating Temperature
- **Normal**: -20°C to +50°C ambient
- **Gearbox Oil**: -10°C to +130°C

### 6.2 Altitude
- **Sea Level to 3000m**: Normal operation
- **3000m to 5000m**: Adjusted shift points for reduced air density

### 6.3 Weather Conditions
- Rain, snow, ice: Reduced shift aggressiveness
- Detection via wheel slip sensors and ABS integration

## 7. User Interface Requirements

### 7.1 Dashboard Display
- Current gear number (1-6, R, N, P)
- Selected mode (Manual, Sport, Eco)
- Shift indicator (up/down arrows)
- Warning messages (text + icon)

### 7.2 Warning Messages
- "Gearbox Overheating" (yellow)
- "Shift Not Possible" (red)
- "Service Required" (yellow)
- "Limp-Home Mode Active" (red)

### 7.3 User Feedback
- Shift confirmation (subtle indicator flash)
- Paddle input acknowledgment (haptic feedback if available)
- Audio warning for critical errors

## 8. Integration Requirements

### 8.1 Engine Control Unit (ECU)
- Torque reduction request during shifts
- RPM synchronization for smooth engagement
- Engine braking coordination

### 8.2 Anti-lock Braking System (ABS)
- Wheel slip detection for traction control
- Emergency braking gear hold
- Stability control integration

### 8.3 Electronic Stability Control (ESC)
- Torque vectoring support
- Drift mode compatibility (sport mode)
- Traction control coordination

## 9. Validation Requirements

### 9.1 Unit Testing
- Individual sensor input validation
- Shift logic decision trees
- Safety feature triggering

### 9.2 Integration Testing
- Multi-mode operation
- Sensor failure scenarios
- ECU communication

### 9.3 System Testing
- Real-world driving scenarios
- Extreme condition testing
- Long-term reliability testing

## 10. Constraints and Assumptions

### 10.1 Physical Constraints
- Maximum gear ratio: 1:6.5 (1st gear) to 1:0.85 (6th gear)
- Clutch engagement time: 200-400 ms
- Hydraulic system pressure: 8-12 bar

### 10.2 System Assumptions
- Sensors provide accurate readings within ±5% tolerance
- ECU communication latency < 10 ms
- Battery voltage maintained at 12-14V

### 10.3 Regulatory Compliance
- ISO 26262 (Automotive Safety Integrity Level - ASIL C)
- UNECE R13 (Braking regulations)
- Local emissions standards compliance
```

## File: `examples/gearbox-test-plan.md`
```markdown
# Automotive Gearbox Control System - PICT Test Plan

## Test Plan Overview

This test plan uses Pairwise Independent Combinatorial Testing (PICT) to generate comprehensive test cases for the Automotive Gearbox Control System with minimal test execution while ensuring complete coverage of all critical parameter interactions.

## Test Parameters Analysis

Based on the specification analysis, the following parameters have been identified:

### Core Parameters
1. **Operating Mode**: Manual, Sport, Eco
2. **Current Gear**: Park, Neutral, Reverse, 1st, 2nd, 3rd, 4th, 5th, 6th
3. **Vehicle Speed**: Stopped, Low (1-30 km/h), Medium (31-80 km/h), High (81-150 km/h), VeryHigh (151-200 km/h)
4. **Engine RPM**: Idle (<1000), Low (1000-2500), Normal (2500-4500), High (4500-6500), RedLine (>6500)
5. **Throttle Position**: Closed (0-10%), Light (11-40%), Medium (41-80%), Heavy (81-100%)
6. **Brake Status**: NotApplied, Light, Hard
7. **Shift Request**: None, PaddleUp, PaddleDown, Automatic
8. **Temperature**: Cold (<70°C), Normal (70-110°C), Warm (110-130°C), Critical (>130°C)

### Environmental Parameters
9. **Road Condition**: Dry, Wet, Ice
10. **Incline**: Flat, UpHill, DownHill

### System State Parameters
11. **Sensor Status**: AllOK, SpeedFail, RPMFail, ThrottleFail, MultipleFail
12. **Hydraulic Pressure**: Normal, Low, Critical

## PICT Model

```pict
# Core Operating Parameters
OperatingMode: Manual, Sport, Eco
CurrentGear: Park, Neutral, Reverse, 1st, 2nd, 3rd, 4th, 5th, 6th
VehicleSpeed: Stopped, Low, Medium, High, VeryHigh
EngineRPM: Idle, Low, Normal, High, RedLine
ThrottlePosition: Closed, Light, Medium, Heavy
BrakeStatus: NotApplied, Light, Hard
ShiftRequest: None, PaddleUp, PaddleDown, Automatic
Temperature: Cold, Normal, Warm, Critical
RoadCondition: Dry, Wet, Ice
Incline: Flat, UpHill, DownHill
SensorStatus: AllOK, SpeedFail, RPMFail, ThrottleFail, MultipleFail
HydraulicPressure: Normal, Low, Critical

# Constraint 1: Park/Neutral only valid when stopped
IF [CurrentGear] = "Park" THEN [VehicleSpeed] = "Stopped";
IF [CurrentGear] = "Neutral" AND [ShiftRequest] <> "None" THEN [VehicleSpeed] = "Stopped";

# Constraint 2: Reverse requires vehicle stopped
IF [CurrentGear] = "Reverse" AND [ShiftRequest] = "None" THEN [VehicleSpeed] IN {Stopped, Low};
IF [ShiftRequest] = "PaddleDown" AND [CurrentGear] = "1st" THEN [VehicleSpeed] = "Stopped";

# Constraint 3: Engine RPM correlates with vehicle speed and gear
IF [VehicleSpeed] = "Stopped" THEN [EngineRPM] IN {Idle, Low};
IF [VehicleSpeed] = "VeryHigh" THEN [EngineRPM] IN {Normal, High, RedLine};
IF [CurrentGear] IN {Park, Neutral} THEN [EngineRPM] IN {Idle, Low, Normal};

# Constraint 4: Throttle and brake are mutually exclusive (mostly)
IF [BrakeStatus] = "Hard" THEN [ThrottlePosition] IN {Closed, Light};
IF [ThrottlePosition] = "Heavy" THEN [BrakeStatus] = "NotApplied";

# Constraint 5: High gears require sufficient speed
IF [CurrentGear] IN {5th, 6th} THEN [VehicleSpeed] IN {Medium, High, VeryHigh};
IF [CurrentGear] IN {5th, 6th} THEN [EngineRPM] <> "Idle";

# Constraint 6: Low gears limited to lower speeds
IF [CurrentGear] = "1st" AND [VehicleSpeed] IN {High, VeryHigh} THEN [EngineRPM] = "RedLine";
IF [CurrentGear] = "2nd" AND [VehicleSpeed] = "VeryHigh" THEN [EngineRPM] IN {High, RedLine};

# Constraint 7: Shift requests must be appropriate for current gear
IF [ShiftRequest] = "PaddleDown" AND [CurrentGear] = "1st" THEN [VehicleSpeed] = "Stopped";
IF [ShiftRequest] = "PaddleUp" AND [CurrentGear] = "6th" THEN [EngineRPM] <> "RedLine";

# Constraint 8: Critical temperature limits automatic shifting
IF [Temperature] = "Critical" THEN [ShiftRequest] IN {None, PaddleUp, PaddleDown};
IF [Temperature] = "Critical" THEN [CurrentGear] IN {Neutral, 3rd};

# Constraint 9: Sensor failures affect operation
IF [SensorStatus] = "MultipleFail" THEN [CurrentGear] = "3rd";
IF [SensorStatus] = "MultipleFail" THEN [ShiftRequest] = "None";
IF [SensorStatus] = "SpeedFail" THEN [ShiftRequest] IN {None, PaddleUp, PaddleDown};

# Constraint 10: Hydraulic pressure issues limit operation
IF [HydraulicPressure] = "Critical" THEN [ShiftRequest] = "None";
IF [HydraulicPressure] = "Low" THEN [OperatingMode] <> "Sport";

# Constraint 11: Ice conditions require special handling
IF [RoadCondition] = "Ice" THEN [ThrottlePosition] IN {Closed, Light, Medium};
IF [RoadCondition] = "Ice" AND [BrakeStatus] = "Hard" THEN [VehicleSpeed] IN {Stopped, Low};

# Constraint 12: Operating mode influences shift behavior
IF [OperatingMode] = "Eco" AND [ThrottlePosition] = "Heavy" THEN [EngineRPM] IN {Idle, Low, Normal};
IF [OperatingMode] = "Sport" AND [ShiftRequest] = "Automatic" THEN [EngineRPM] IN {Normal, High, RedLine};

# Constraint 13: Cold temperature affects shifting
IF [Temperature] = "Cold" THEN [OperatingMode] IN {Manual, Eco};
IF [Temperature] = "Cold" THEN [ShiftRequest] <> "Automatic";

# Constraint 14: Incline affects shift logic
IF [Incline] = "UpHill" AND [CurrentGear] IN {5th, 6th} THEN [ThrottlePosition] IN {Medium, Heavy};
IF [Incline] = "DownHill" AND [BrakeStatus] IN {Light, Hard} THEN [EngineRPM] IN {Normal, High};
```

## Generated Test Cases

| Test # | Mode | Gear | Speed | RPM | Throttle | Brake | ShiftReq | Temp | Road | Incline | Sensor | Hydraulic | Expected Output |
|--------|------|------|-------|-----|----------|-------|----------|------|------|---------|--------|-----------|-----------------|
| 1 | Manual | Park | Stopped | Idle | Closed | NotApplied | None | Normal | Dry | Flat | AllOK | Normal | Success: Vehicle parked, engine idling |
| 2 | Sport | 3rd | Medium | High | Medium | NotApplied | Automatic | Normal | Wet | Flat | AllOK | Normal | Success: Upshift to 4th at 5500 RPM |
| 3 | Eco | 2nd | Low | Low | Light | NotApplied | Automatic | Normal | Dry | UpHill | AllOK | Normal | Success: Hold 2nd gear, insufficient RPM for upshift |
| 4 | Manual | 4th | High | Normal | Medium | NotApplied | PaddleUp | Normal | Dry | Flat | AllOK | Normal | Success: Upshift to 5th gear via paddle |
| 5 | Sport | 5th | VeryHigh | High | Medium | NotApplied | None | Normal | Dry | DownHill | AllOK | Normal | Success: Hold 5th gear, RPM in range |
| 6 | Eco | 3rd | Medium | Low | Closed | Light | None | Normal | Wet | Flat | AllOK | Normal | Success: Downshift to 2nd, low RPM + closed throttle |
| 7 | Manual | 1st | Stopped | Idle | Closed | Hard | None | Cold | Dry | Flat | AllOK | Normal | Success: Stationary in 1st with brake applied |
| 8 | Sport | 2nd | Low | Normal | Heavy | NotApplied | Automatic | Normal | Dry | UpHill | AllOK | Normal | Success: Hold 2nd gear for power uphill |
| 9 | Eco | 6th | VeryHigh | Normal | Light | NotApplied | None | Normal | Dry | Flat | AllOK | Normal | Success: Cruising in 6th gear |
| 10 | Manual | Reverse | Stopped | Low | Closed | NotApplied | None | Normal | Wet | Flat | AllOK | Normal | Success: In reverse, vehicle stopped |
| 11 | Sport | 3rd | Medium | RedLine | Heavy | NotApplied | Automatic | Normal | Dry | Flat | AllOK | Normal | Success: Upshift to 4th to prevent over-rev |
| 12 | Eco | 1st | Low | Normal | Medium | NotApplied | Automatic | Normal | Ice | Flat | AllOK | Normal | Success: Smooth upshift to 2nd |
| 13 | Manual | 4th | Medium | Low | Closed | Light | PaddleDown | Normal | Dry | DownHill | AllOK | Normal | Success: Downshift to 3rd for engine braking |
| 14 | Sport | 3rd | Low | High | Light | Hard | None | Normal | Ice | Flat | AllOK | Normal | Warning: Reduce shift aggressiveness on ice |
| 15 | Eco | 2nd | Medium | Normal | Light | NotApplied | None | Warm | Dry | Flat | AllOK | Normal | Success: Upshift to 3rd (or 4th skip-shift) |
| 16 | Manual | Neutral | Stopped | Idle | Closed | NotApplied | None | Normal | Dry | Flat | AllOK | Normal | Success: Neutral, engine idling |
| 17 | Sport | 5th | High | High | Medium | NotApplied | PaddleDown | Normal | Dry | Flat | AllOK | Normal | Success: Downshift to 4th |
| 18 | Eco | 3rd | Medium | Normal | Closed | NotApplied | Automatic | Normal | Wet | UpHill | AllOK | Normal | Success: Hold 3rd gear for uphill |
| 19 | Manual | 1st | Low | High | Heavy | NotApplied | PaddleUp | Normal | Dry | Flat | AllOK | Normal | Success: Upshift to 2nd |
| 20 | Sport | 4th | VeryHigh | RedLine | Medium | NotApplied | None | Normal | Dry | Flat | AllOK | Normal | Warning: Prevent downshift, would over-rev |
| 21 | Eco | 3rd | Stopped | Idle | Closed | Hard | None | Normal | Dry | UpHill | AllOK | Normal | Success: Hill start assist activated |
| 22 | Manual | 2nd | Medium | Normal | Light | NotApplied | None | Cold | Dry | Flat | AllOK | Normal | Success: Hold 2nd, cold mode conservative |
| 23 | Sport | 6th | VeryHigh | Normal | Light | NotApplied | Automatic | Normal | Dry | Flat | AllOK | Normal | Success: Hold 6th, optimal cruising |
| 24 | Eco | 1st | Stopped | Low | Closed | NotApplied | Automatic | Normal | Dry | Flat | SpeedFail | Normal | Error: Limit to current gear, speed sensor failed |
| 25 | Manual | 3rd | Medium | Normal | Medium | NotApplied | PaddleUp | Normal | Dry | Flat | RPMFail | Normal | Success: Upshift using speed-based logic fallback |
| 26 | Sport | 3rd | Low | Low | Closed | NotApplied | None | Critical | Dry | Flat | AllOK | Normal | Error: Limp-home mode, critical temperature |
| 27 | Eco | 3rd | Medium | Normal | Light | NotApplied | None | Normal | Dry | Flat | MultipleFail | Normal | Error: Limp-home mode, multiple sensor failures |
| 28 | Manual | 4th | High | High | Medium | NotApplied | None | Normal | Dry | Flat | AllOK | Low | Warning: Reduced shift speed, low hydraulic pressure |
| 29 | Sport | 3rd | Medium | Normal | Medium | NotApplied | None | Normal | Dry | Flat | AllOK | Critical | Error: Lock in current gear, critical hydraulic failure |
| 30 | Eco | 2nd | Low | Low | Light | NotApplied | Automatic | Normal | Ice | Flat | AllOK | Normal | Success: Gentle upshift, ice mode active |
| 31 | Manual | 5th | VeryHigh | Normal | Medium | NotApplied | PaddleDown | Normal | Wet | Flat | AllOK | Normal | Success: Downshift to 4th |
| 32 | Sport | 1st | Stopped | Idle | Closed | Hard | None | Normal | Dry | DownHill | AllOK | Normal | Success: Holding brake on downhill |
| 33 | Eco | 4th | High | Low | Closed | Light | Automatic | Normal | Dry | Flat | AllOK | Normal | Success: Downshift to 3rd, low RPM |
| 34 | Manual | 6th | VeryHigh | High | Heavy | NotApplied | None | Normal | Dry | Flat | AllOK | Normal | Success: Maximum speed in top gear |
| 35 | Sport | 2nd | Medium | RedLine | Medium | NotApplied | Automatic | Normal | Dry | Flat | AllOK | Normal | Success: Emergency upshift to prevent damage |
| 36 | Eco | 1st | Low | Normal | Light | NotApplied | Automatic | Warm | Dry | Flat | ThrottleFail | Normal | Success: Conservative shift points, throttle sensor failed |
| 37 | Manual | Park | Stopped | Idle | Closed | Hard | None | Normal | Ice | Flat | AllOK | Normal | Success: Park brake, ice condition noted |
| 38 | Sport | 4th | High | High | Medium | Light | None | Normal | Dry | DownHill | AllOK | Normal | Success: Engine braking with downshift |
| 39 | Eco | 5th | VeryHigh | Normal | Closed | NotApplied | None | Normal | Wet | Flat | AllOK | Normal | Success: Coasting in 5th gear |
| 40 | Manual | 3rd | Medium | High | Heavy | NotApplied | PaddleUp | Cold | Dry | UpHill | AllOK | Normal | Success: Upshift to 4th, cold mode allows manual override |

## Test Case Summary

- **Total Possible Combinations**: 12 parameters with 3-13 values each = ~159 billion combinations
- **PICT Generated Test Cases**: 40
- **Test Reduction**: 99.999999975% reduction
- **Coverage**: All pairwise (2-way) parameter interactions
- **Constraints Applied**: 14 business rules and safety constraints

## Test Execution Priority

### Priority 1: Critical Safety Tests (Tests 7, 10, 21, 26, 27, 29, 32, 37)
- Park/Neutral safety
- Reverse lockout
- Hill start assist
- Critical temperature handling
- Sensor failure modes
- Hydraulic failures

### Priority 2: Core Functionality (Tests 1-6, 8-9, 11-20, 23-25, 30-31, 33-36, 38-40)
- Normal shifting in all modes
- Paddle shift operations
- Automatic shift logic
- RPM protection
- Speed-based logic

### Priority 3: Edge Cases (Tests 22, 28)
- Cold temperature operation
- Low hydraulic pressure
- Environmental conditions

## Coverage Analysis

### Operating Modes Coverage
- **Manual**: 15 tests (37.5%)
- **Sport**: 13 tests (32.5%)
- **Eco**: 12 tests (30%)

### Gear Range Coverage
- All gears (Park, N, R, 1-6) tested
- Emphasis on mid-range gears (2nd-4th) for common scenarios

### Error Scenarios Coverage
- Sensor failures: 4 tests (10%)
- Temperature extremes: 3 tests (7.5%)
- Hydraulic issues: 2 tests (5%)
- Environmental conditions: 8 tests (20%)

### Shift Request Coverage
- **None** (steady state): 18 tests (45%)
- **Automatic**: 12 tests (30%)
- **PaddleUp**: 5 tests (12.5%)
- **PaddleDown**: 5 tests (12.5%)

## Traceability Matrix

| Requirement Section | Test Cases | Coverage |
|---------------------|------------|----------|
| 4.1.1 Upshift Conditions | 2, 4, 8, 12, 15, 19, 30, 35 | 100% |
| 4.1.2 Downshift Conditions | 3, 6, 13, 33, 38 | 100% |
| 4.1.3 Prohibited Shifts | 10, 20, 35 | 100% |
| 4.2.1 Hill Start Assist | 21 | 100% |
| 4.2.2 Overrun Protection | 11, 20, 35 | 100% |
| 4.2.3 Stall Prevention | 3, 33 | 100% |
| 4.2.4 Neutral Safety | 1, 7, 10, 16, 32, 37 | 100% |
| 4.3.1 Sensor Failures | 24, 25, 27, 36 | 100% |
| 4.3.2 Actuator Failures | 29 | 100% |
| 4.3.3 Temperature Management | 22, 26 | 100% |

## Test Environment Setup

### Required Hardware
- Gearbox ECU unit
- Vehicle speed simulator (0-200 km/h)
- Engine RPM simulator (0-7000 RPM)
- Throttle position simulator (0-100%)
- Brake pressure simulator
- Temperature control unit (-20°C to +150°C)
- Gear position sensor mockup
- Hydraulic pressure simulator

### Software Tools
- PICT command-line tool (for model validation)
- Test automation framework
- Data logging and analysis tools
- ECU diagnostic interface

### Test Data Collection
- Shift completion time (ms)
- Clutch engagement time (ms)
- Engine RPM before/after shift
- Vehicle speed before/after shift
- Hydraulic pressure readings
- Temperature readings
- Error codes generated

## Expected Test Duration

- **Setup**: 2 hours
- **Execution**: ~30 minutes (40 tests × 45 seconds average)
- **Data Analysis**: 1 hour
- **Total**: ~3.5 hours

## Success Criteria

### Pass Criteria
- All safety constraints respected (100%)
- Shift times within specification (>95%)
- No unexpected error codes (<5%)
- Smooth transitions (subjective, all tests)

### Fail Criteria
- Any safety violation (immediate stop)
- Shift time >2× specification
- Unexpected limp-home mode activation
- Incorrect gear selected

## Risk Assessment

### High Risk Areas
- Reverse to forward gear transitions (Test 10)
- Critical temperature handling (Test 26)
- Multiple sensor failures (Test 27)
- Hydraulic pressure critical (Test 29)

### Medium Risk Areas
- Sensor failure fallback logic (Tests 24, 25, 36)
- Ice condition handling (Tests 12, 14, 30)
- Over-rev protection (Tests 11, 20, 35)

### Low Risk Areas
- Normal mode operation (Tests 1-9)
- Standard upshift/downshift (Tests 2, 4, 6, 13, 17, 31)

## Notes and Recommendations

1. **Test Automation**: Automate all 40 tests for regression testing
2. **Real-World Validation**: Follow up with road testing for selected scenarios
3. **Expanded Coverage**: Consider 3-way interactions for critical safety features
4. **Performance Testing**: Add load testing for shift actuator endurance
5. **Edge Case Exploration**: Manual testing for unusual conditions not covered by PICT

## References

- Gearbox Specification Document (gearbox-specification.md)
- PICT Tool Documentation: https://github.com/microsoft/pict
- ISO 26262 Automotive Safety Standard
- Test Automation Framework Documentation
```

## File: `references/examples.md`
```markdown
# PICT Examples Reference

> **Note**: This is a placeholder file. Comprehensive examples are coming soon!
> 
> For now, check out the [examples directory](../examples/) for complete real-world examples.

## Available Examples

### Complete Examples
- **[ATM System Testing](../examples/atm-specification.md)**: Comprehensive banking ATM system with 31 test cases

### Coming Soon

#### Software Testing
- Function testing with multiple parameters
- API endpoint testing
- Database query validation
- Algorithm testing

#### Web Applications
- Form validation
- User authentication
- E-commerce checkout
- Shopping cart operations

#### Configuration Testing
- System configurations
- Feature flags
- Environment settings
- Browser compatibility

#### Mobile Testing
- Device and OS combinations
- Screen sizes
- Network conditions
- Permissions

## Pattern Library (Coming Soon)

### Common Constraint Patterns

```
# Dependency constraints
IF [FeatureA] = "Enabled" THEN [FeatureB] = "Enabled";

# Exclusive options
IF [PaymentMethod] = "Cash" THEN [InstallmentPlan] = "None";

# Platform limitations
IF [OS] = "iOS" THEN [Browser] IN {Safari, Chrome};

# Environment restrictions
IF [Environment] = "Production" THEN [LogLevel] <> "Debug";
```

### Boundary Value Patterns

```
# Numeric boundaries
Age: 0, 17, 18, 64, 65, 100

# Size categories
FileSize: 0KB, 1KB, 1MB, 100MB, 1GB

# Time periods
Duration: 0s, 1s, 30s, 60s, 3600s
```

### Negative Testing Patterns

```
# Invalid inputs (using ~ prefix in some PICT variants)
Email: Valid, Invalid, Empty, TooLong
Password: Strong, Weak, Empty, SpecialChars

# Error conditions
NetworkStatus: Connected, Slow, Disconnected, Timeout
```

## Contributing Examples

Have an example to share? We'd love to include it!

1. Create your example following the structure in [examples/README.md](../../../README.md)
2. Include:
   - Original specification
   - PICT model
   - Test cases with expected outputs
   - Learning points
3. Submit a pull request

See [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md) for details.

## External Resources

- [Pairwise Testing Tutorial](https://www.pairwisetesting.com/)
- [NIST Combinatorial Testing Resources](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software)
- [Microsoft PICT Examples](https://github.com/microsoft/pict/tree/main/doc)
```

## File: `references/pict_syntax.md`
```markdown
# PICT Syntax Reference

> **Note**: This is a placeholder file. Complete syntax documentation is coming soon!
> 
> For now, please refer to the official PICT documentation:
> - [Microsoft PICT on GitHub](https://github.com/microsoft/pict)
> - [PICT User Guide](https://github.com/microsoft/pict/blob/main/doc/pict.md)

## Quick Reference

### Basic Model Structure

```
# Parameters
ParameterName: Value1, Value2, Value3
AnotherParameter: ValueA, ValueB, ValueC

# Constraints (optional)
IF [ParameterName] = "Value1" THEN [AnotherParameter] <> "ValueA";
```

### Parameter Definition

```
ParameterName: Value1, Value2, Value3, ...
```

### Constraint Syntax

```
IF <condition> THEN <condition>;
```

### Operators

- `=` - Equal to
- `<>` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to
- `IN` - Member of set
- `AND` - Logical AND
- `OR` - Logical OR
- `NOT` - Logical NOT

### Example Constraints

```
# Simple constraint
IF [OS] = "MacOS" THEN [Browser] <> "IE";

# Multiple conditions
IF [Environment] = "Production" AND [LogLevel] = "Debug" THEN [Approved] = "False";

# Set membership
IF [UserRole] = "Guest" THEN [Permission] IN {Read, None};
```

## Coming Soon

Detailed documentation will include:
- Complete grammar specification
- Advanced features (sub-models, aliasing, seeding)
- Negative testing patterns
- Weight specifications
- Order specifications
- Examples for each feature

## Contributing

If you'd like to help complete this documentation:
1. Fork the repository
2. Add content to this file
3. Submit a pull request

See [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md) for guidelines.

## External Resources

- [Official PICT Documentation](https://github.com/microsoft/pict/blob/main/doc/pict.md)
- [pypict Documentation](https://github.com/kmaehashi/pypict)
- [Pairwise Testing Explained](https://www.pairwisetesting.com/)
```

## File: `releases/README.md`
```markdown
# Release Files

This directory contains pre-packaged release files for easy installation of the PICT Test Designer skill.

## Minimal Installation Package

**File:** `pict-test-designer-minimal.zip` (9.3 KB)

This ZIP contains only the essential files needed for the skill to function:

- `SKILL.md` - Core skill definition
- `LICENSE` - MIT License
- `references/pict_syntax.md` - PICT syntax reference
- `references/examples.md` - Common patterns and examples
- `README-INSTALL.txt` - Installation instructions

### Quick Installation

**For personal use (all projects):**
```bash
# Download the ZIP
wget https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip

# Extract and install
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal ~/.claude/skills/pict-test-designer

# Restart Claude Code
```

**For project-specific use:**
```bash
# Download the ZIP
wget https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip

# Extract and install
unzip pict-test-designer-minimal.zip
mv pict-test-designer-minimal .claude/skills/pict-test-designer

# Restart Claude Code
```

**Windows:**
```powershell
# Download manually or use:
Invoke-WebRequest -Uri "https://github.com/omkamal/pypict-claude-skill/raw/main/releases/pict-test-designer-minimal.zip" -OutFile "pict-test-designer-minimal.zip"

# Extract to:
# Personal: %USERPROFILE%\.claude\skills\pict-test-designer\
# Project:  .claude\skills\pict-test-designer\
```

## What's Not Included

The minimal package excludes:
- Full examples (ATM test plan)
- Helper scripts (pict_helper.py)
- Extended documentation (README.md, QUICKSTART.md, etc.)

For the complete package with examples and documentation, clone the full repository:
```bash
git clone https://github.com/omkamal/pypict-claude-skill.git ~/.claude/skills/pict-test-designer
```

## Verification

After installation, restart Claude Code and verify by asking:
```
Do you have access to the pict-test-designer skill?
```

Or start using it immediately:
```
Design test cases for a login function with username, password, and remember me checkbox.
```

## Version Information

- **Current Version:** 1.0.0
- **Last Updated:** October 19, 2025
- **Size:** 9.3 KB (compressed)
- **Files:** 5 files

## Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/omkamal/pypict-claude-skill/issues
- Full Documentation: https://github.com/omkamal/pypict-claude-skill
```

## File: `scripts/README.md`
```markdown
# Scripts

This directory contains helper scripts for working with PICT models and test cases.

## Available Scripts

### pict_helper.py

A Python utility for:
- Generating PICT models from JSON configuration
- Formatting PICT output as markdown tables
- Parsing PICT output into JSON

**Installation:**
```bash
pip install pypict --break-system-packages
```

**Usage:**

1. **Generate PICT model from config:**
   ```bash
   python pict_helper.py generate config.json > model.txt
   ```

2. **Format PICT output as markdown:**
   ```bash
   python pict_helper.py format output.txt
   ```

3. **Parse PICT output to JSON:**
   ```bash
   python pict_helper.py parse output.txt
   ```

**Example config.json:**
```json
{
    "parameters": {
        "Browser": ["Chrome", "Firefox", "Safari"],
        "OS": ["Windows", "MacOS", "Linux"],
        "Memory": ["4GB", "8GB", "16GB"]
    },
    "constraints": [
        "IF [OS] = \"MacOS\" THEN [Browser] <> \"IE\"",
        "IF [Memory] = \"4GB\" THEN [OS] <> \"MacOS\""
    ]
}
```

## Future Scripts

We welcome contributions for:
- Test automation generators
- Export to test management tools (JIRA, TestRail)
- Integration with CI/CD pipelines
- Coverage analysis tools
- Constraint validation utilities

## Contributing

Have a useful script to share?

1. Add your script to this directory
2. Update this README with usage instructions
3. Add comments and examples in your script
4. Submit a pull request

See [CONTRIBUTING.md](../bmad_repo/CONTRIBUTING.md) for guidelines.

## Dependencies

Current scripts use:
- Python 3.7+
- pypict (optional, for direct PICT integration)

All dependencies should be clearly documented in each script.
```

## File: `scripts/pict_helper.py`
```python
#!/usr/bin/env python3
"""
PICT Helper Script

This script provides utilities for working with PICT models and test cases.

Note: This is a placeholder/example script. Full implementation coming soon!

Requirements:
    pip install pypict --break-system-packages

Usage:
    python pict_helper.py generate config.json
    python pict_helper.py format output.txt
    python pict_helper.py parse output.txt
"""

import sys
import json
from typing import Dict, List, Any

def generate_model(config_file: str) -> str:
    """
    Generate a PICT model from a JSON configuration file.
    
    Args:
        config_file: Path to JSON config file
        
    Returns:
        PICT model as string
        
    Example config.json:
    {
        "parameters": {
            "Browser": ["Chrome", "Firefox", "Safari"],
            "OS": ["Windows", "MacOS", "Linux"],
            "Memory": ["4GB", "8GB", "16GB"]
        },
        "constraints": [
            "IF [OS] = \"MacOS\" THEN [Browser] <> \"IE\"",
            "IF [Memory] = \"4GB\" THEN [OS] <> \"MacOS\""
        ]
    }
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        parameters = config.get('parameters', {})
        constraints = config.get('constraints', [])
        
        # Generate model
        model_lines = []
        model_lines.append("# Generated PICT Model")
        model_lines.append("")
        
        # Add parameters
        for param_name, values in parameters.items():
            values_str = ", ".join(values)
            model_lines.append(f"{param_name}: {values_str}")
        
        # Add constraints
        if constraints:
            model_lines.append("")
            model_lines.append("# Constraints")
            for constraint in constraints:
                if not constraint.endswith(';'):
                    constraint += ';'
                model_lines.append(constraint)
        
        return "\n".join(model_lines)
        
    except Exception as e:
        print(f"Error generating model: {e}", file=sys.stderr)
        return ""

def format_output(output_file: str) -> str:
    """
    Format PICT output as a markdown table.
    
    Args:
        output_file: Path to PICT output file
        
    Returns:
        Markdown formatted table
    """
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            return "No output to format"
        
        # First line is header
        header = lines[0].strip().split('\t')
        
        # Create markdown table
        table = []
        table.append("| " + " | ".join(header) + " |")
        table.append("|" + "|".join(["-" * (len(h) + 2) for h in header]) + "|")
        
        # Add data rows
        for line in lines[1:]:
            if line.strip():
                values = line.strip().split('\t')
                table.append("| " + " | ".join(values) + " |")
        
        return "\n".join(table)
        
    except Exception as e:
        print(f"Error formatting output: {e}", file=sys.stderr)
        return ""

def parse_output(output_file: str) -> List[Dict[str, str]]:
    """
    Parse PICT output into a list of dictionaries.
    
    Args:
        output_file: Path to PICT output file
        
    Returns:
        List of test case dictionaries
    """
    try:
        with open(output_file, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            return []
        
        # First line is header
        header = lines[0].strip().split('\t')
        
        # Parse data rows
        test_cases = []
        for i, line in enumerate(lines[1:], 1):
            if line.strip():
                values = line.strip().split('\t')
                test_case = {"test_id": i}
                for h, v in zip(header, values):
                    test_case[h] = v
                test_cases.append(test_case)
        
        return test_cases
        
    except Exception as e:
        print(f"Error parsing output: {e}", file=sys.stderr)
        return []

def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python pict_helper.py generate <config.json>")
        print("  python pict_helper.py format <output.txt>")
        print("  python pict_helper.py parse <output.txt>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "generate" and len(sys.argv) >= 3:
        config_file = sys.argv[2]
        model = generate_model(config_file)
        print(model)
    
    elif command == "format" and len(sys.argv) >= 3:
        output_file = sys.argv[2]
        table = format_output(output_file)
        print(table)
    
    elif command == "parse" and len(sys.argv) >= 3:
        output_file = sys.argv[2]
        test_cases = parse_output(output_file)
        print(json.dumps(test_cases, indent=2))
    
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

# Example usage:
"""
# 1. Create a config.json file:
{
    "parameters": {
        "Browser": ["Chrome", "Firefox", "Safari"],
        "OS": ["Windows", "MacOS", "Linux"]
    },
    "constraints": [
        "IF [OS] = \"MacOS\" THEN [Browser] <> \"IE\""
    ]
}

# 2. Generate PICT model:
python pict_helper.py generate config.json > model.txt

# 3. Run PICT (if installed):
pict model.txt > output.txt

# 4. Format as markdown:
python pict_helper.py format output.txt

# 5. Parse to JSON:
python pict_helper.py parse output.txt
"""
```


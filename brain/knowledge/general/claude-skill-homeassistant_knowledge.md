---
id: claude-skill-homeassistant-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:05.265533
---

# KNOWLEDGE EXTRACT: claude-skill-homeassistant
> **Extracted on:** 2026-03-30 13:16:39
> **Source:** claude-skill-homeassistant

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2024 Home Assistant Claude Skill Contributors

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
# Home Assistant Manager - Claude Code Skill

> Expert-level Home Assistant configuration management with efficient deployment workflows, remote CLI access, automation verification, and comprehensive Lovelace dashboard development.

[![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2)](https://github.com/anthropics/claude-code)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatible-41BDF5)](https://www.home-assistant.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![Tablet Dashboard Example](dashboard.png)
*Example tablet-optimized dashboard built using this skill - touch-friendly controls, color-coded status, and responsive grid layout*

## 🎬 See It In Action

### Quick Skill Check
Verify Claude can see and use this skill:

https://github.com/user-attachments/assets/a215df83-ce84-4ed2-bb93-f3a3ee0c43e8

*Shows Claude recognizing the skill and loading Home Assistant expertise*

### Full Workflow Demo
Watch the complete workflow in action - end to end (3x speed):


https://github.com/user-attachments/assets/eab53b18-ae2b-4d43-b1e4-e45bf9357099

*Complete automation development cycle including deployment, testing, log analysis, and git workflow*

## 🚀 What This Skill Does

This Claude Code skill transforms Claude into a **Home Assistant expert** that helps you:

### Configuration Management
- **Rapid Development Workflow**: Deploy changes via `scp` for instant testing, commit to git when stable
- **Smart Reload vs Restart**: Automatically determines whether to reload or restart based on change type
- **Configuration Validation**: Always validates before applying changes to prevent downtime
- **Remote CLI Access**: Seamlessly manages HA instances via SSH and `hass-cli`

### Automation Development
- **Complete Verification Protocol**: Automatically tests automations by triggering manually and checking logs
- **Error Detection**: Identifies template errors, type mismatches, and execution failures
- **Log Analysis Patterns**: Knows what success and error indicators to look for
- **Iterative Fix Workflow**: Guides through debugging and re-testing cycles

### Lovelace Dashboard Development
- **Tablet Optimization**: Creates touch-friendly dashboards optimized for specific screen sizes (7", 11", 13")
- **Card Type Expertise**: Knows when to use Mushroom cards, Tile cards, Panel vs Sections views
- **Template Patterns**: Provides ready-to-use Jinja2 templates for common use cases:
  - Door/window counting with color coding
  - Conditional display based on time/state
  - Multi-condition status indicators
- **Common Pitfall Solutions**: Solves dashboard registration, auto-entities failures, template type errors
- **Real-World Examples**: Includes working examples from production tablet dashboards

### Workflow Optimization
- **Git + scp Hybrid**: Uses git for version control, scp for rapid iteration
- **No Restart for Dashboards**: Deploys dashboard changes with just browser refresh
- **Context7 Integration**: Leverages official HA documentation via MCP when available
- **Deployment Decision Tree**: Guides through the optimal workflow based on change type

## 📦 Installation

### Prerequisites

1. **Claude Code** installed and configured
2. **Home Assistant** instance with:
   - SSH access enabled
   - Git repository connected to `/config` directory
3. **Local tools**:
   - `hass-cli` installed (`pipx install homeassistant-cli`)
   - SSH key authentication configured
   - Environment variables set: `HASS_SERVER`, `HASS_TOKEN`

### Install the Skill

#### Option 1: Clone into your Home Assistant config repository

```bash
cd /path/to/your/homeassistant/config
mkdir -p .claude/skills
cd .claude/skills
git clone git@github.com:komal-SkyNET/claude-skill-homeassistant.git home-assistant-manager
```

#### Option 2: Download and extract

```bash
cd /path/to/your/homeassistant/config
mkdir -p .claude/skills/home-assistant-manager
cd .claude/skills/home-assistant-manager
curl -L https://github.com/komal-SkyNET/claude-skill-homeassistant/archive/main.tar.gz | tar xz --strip-components=1
```

### Verify Installation

The skill should appear when you start Claude Code in your Home Assistant repository. Claude will automatically load the skill and apply the expertise.

## 🎯 Usage Examples

### Example 1: Create a New Automation

```
User: "Create an automation that sends a notification when the front door
       is left open for more than 5 minutes"

Claude: [Uses skill to]:
1. Create automation YAML with proper syntax
2. Deploy via scp for testing
3. Reload automations (no restart needed)
4. Manually trigger to test
5. Check logs for execution
6. Verify notification received
7. Commit to git when working
```

### Example 2: Build a Tablet Dashboard

```
User: "Create a dashboard for my 11-inch tablet in the living room
       with lights, thermostat, and door status"

Claude: [Uses skill to]:
1. Create new dashboard file in .vault/
2. Register in lovelace_dashboards
3. Use 3-column grid layout (optimal for 11")
4. Add Mushroom cards for touch-friendly controls
5. Create template card with door counting
6. Deploy via scp for instant preview
7. Iterate on layout based on feedback
8. Commit when finalized
```

### Example 3: Debug a Template Error

```
User: "My automation has a TypeError about comparing str and int"

Claude: [Uses skill to]:
1. Check logs for exact error message
2. Identify template needs | int filter
3. Fix the template syntax
4. Deploy via scp
5. Trigger manually to verify
6. Check logs confirm no errors
7. Commit the fix
```

## 🏗️ Skill Architecture

This skill provides expertise in three core areas:

### 1. Remote Access Patterns
- `hass-cli` commands with environment variables
- SSH-based `ha` CLI commands
- Log analysis and error detection
- State verification

### 2. Deployment Workflows
- **Git workflow**: For final, tested changes
- **scp workflow**: For rapid iteration (dashboards, testing)
- **Reload vs Restart**: Smart decision making
- **Verification protocols**: Always check outcomes

### 3. Dashboard Development
- **View types**: Panel (full-screen) vs Sections (organized)
- **Card types**: Mushroom, Tile, Template, Auto-entities
- **Template patterns**: Jinja2 snippets for common use cases
- **Debugging**: JSON validation, template testing, entity verification

## 🤝 Contributing

We welcome contributions from the Home Assistant community! This skill has been developed through real-world usage and we want to keep improving it.

### What to Contribute

**🎯 Focus on Home Assistant-specific expertise:**

✅ **GOOD contributions:**
- New template patterns for common use cases
- Solutions to specific HA configuration pitfalls
- Dashboard card examples for different devices
- Integration-specific deployment workflows
- Automation verification patterns
- Log analysis patterns for specific errors

❌ **AVOID generic contributions:**
- General git workflows (unless HA-specific)
- Generic Python/YAML best practices
- Non-HA development workflows

### Contribution Guidelines

#### 1. Template Pattern Contributions

Add to the "Common Template Patterns" section:

```markdown
**Your Pattern Name:**
```jinja2
{% set entities = [...] %}
{{ your_template_logic }}
```

**Use case:** Explain when to use this
**Example output:** Show what it produces
```

#### 2. Dashboard Card Examples

Add to "Real-World Examples":

```markdown
### Your Card Name
```json
{
  "type": "...",
  ...
}
```

**Best for:** Device type, use case
**Features:** What makes this example useful
```

#### 3. Pitfall Solutions

Add to "Common Pitfalls":

```markdown
**Problem X: Brief description**
- **Symptom:** What the user sees
- **Cause:** Root cause explanation
- **Fix:** Step-by-step solution
```

#### 4. Workflow Improvements

If proposing workflow changes:
- Explain the problem with current workflow
- Provide specific HA scenario where it applies
- Show before/after comparison
- Include verification steps

### How to Submit

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-contribution-name`
3. **Make your changes** to `SKILL.md`
4. **Test thoroughly** in your own HA environment
5. **Update README.md** if adding new capabilities
6. **Submit a Pull Request** with:
   - Clear description of what you're adding
   - Example usage scenario
   - Verification that it works in real HA setup

### Contribution Review Process

PRs are reviewed for:
- ✅ **HA-specific value**: Does it solve a real HA problem?
- ✅ **Accuracy**: Is the information correct and up-to-date?
- ✅ **Clarity**: Is it well-documented and easy to understand?
- ✅ **Tested**: Has it been verified in a real HA environment?

## 📚 Skill Structure

```
home-assistant-manager/
├── SKILL.md          # Main skill content with YAML frontmatter
├── README.md         # This file
└── LICENSE           # MIT License
```

The skill follows the [official Claude skills specification](https://github.com/anthropics/skills):
- `SKILL.md` contains YAML frontmatter with `name` and `description`
- Content organized in logical sections
- Includes examples, patterns, and workflows
- Focused on actionable expertise

## 🔧 Environment Setup

For the skill to work optimally, ensure your environment has:

### SSH Access
```bash
# Test SSH access
ssh root@homeassistant.local "ha core info"
```

### hass-cli Setup
```bash
# Install hass-cli
pipx install homeassistant-cli

# Set environment variables (add to ~/.bashrc or ~/.zshrc)
export HASS_SERVER=http://homeassistant.local:8123
export HASS_TOKEN=your_long_lived_access_token

# Test hass-cli
hass-cli state list
```

### Git Repository
```bash
# Your HA config should be a git repository
cd /config
git init
git remote add origin your-repo-url

# Claude should be run from this directory
```

### Context7 MCP (Optional but Recommended)
```bash
# Add Context7 for official HA documentation
claude mcp add --transport http context7 https://mcp.context7.com/mcp \
  --header "CONTEXT7_API_KEY: your_api_key"
```

## 🎨 Use Cases

### DevOps & Configuration Management
- Rapid automation development and testing
- Safe configuration changes with validation
- Remote HA instance management
- Git-based version control workflow

### Dashboard Development
- Tablet-optimized control panels
- Wall-mounted dashboard displays
- Mobile-responsive layouts
- Touch-friendly interface design

### Template Development
- Jinja2 template creation and debugging
- Dynamic sensor calculations
- Conditional automation logic
- Custom card configurations

### Troubleshooting
- Log analysis and error detection
- Template type error resolution
- Dashboard debugging
- Integration configuration issues

## 📖 Related Resources

- [Official Claude Skills Repository](https://github.com/anthropics/skills)
- [Home Assistant Documentation](https://www.home-assistant.io/brain/knowledge/docs_legacy/)
- [Lovelace UI Documentation](https://www.home-assistant.io/lovelace/)
- [Home Assistant Community](https://community.home-assistant.io/)

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 👤 Author

**Komal Venkatesh Ganesan**

If you find this skill helpful for managing your Home Assistant setup, consider supporting its development:

<a href="https://www.buymeacoffee.com/komalvenkag" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50"></a>

## 💬 Support & Discussion

- **Issues**: [GitHub Issues](https://github.com/komal-SkyNET/claude-skill-homeassistant/issues)
- **Discussions**: [GitHub Discussions](https://github.com/komal-SkyNET/claude-skill-homeassistant/discussions)
- **Home Assistant Community**: Tag contributions with `claude-skill`

---

**Made with ❤️ for the Home Assistant community**
```

## File: `SKILL.md`
```markdown
---
name: home-assistant-manager
description: Expert-level Home Assistant configuration management with efficient deployment workflows (git and rapid scp iteration), remote CLI access via SSH and hass-cli, automation verification protocols, log analysis, reload vs restart optimization, and comprehensive Lovelace dashboard management for tablet-optimized UIs. Includes template patterns, card types, debugging strategies, and real-world examples.
---

# Home Assistant Manager

Expert-level Home Assistant configuration management with efficient workflows, remote CLI access, and verification protocols.

## Core Capabilities

- Remote Home Assistant instance management via SSH and hass-cli
- Smart deployment workflows (git-based and rapid iteration)
- Configuration validation and safety checks
- Automation testing and verification
- Log analysis and error detection
- Reload vs restart optimization
- Lovelace dashboard development and optimization
- Template syntax patterns and debugging
- Tablet-optimized UI design

## Prerequisites

Before starting, verify the environment has:
1. SSH access to Home Assistant instance (`root@homeassistant.local`)
2. `hass-cli` installed locally
3. Environment variables loaded (HASS_SERVER, HASS_TOKEN)
4. Git repository connected to HA `/config` directory
5. Context7 MCP server with Home Assistant docs (recommended)

## Remote Access Patterns

### Using hass-cli (Local, via REST API)

All `hass-cli` commands use environment variables automatically:

```bash
# List entities
hass-cli state list

# Get specific state
hass-cli state get sensor.entity_name

# Call services
hass-cli service call automation.reload
hass-cli service call automation.trigger --arguments entity_id=automation.name
```

### Using SSH for HA CLI

```bash
# Check configuration validity
ssh root@homeassistant.local "ha core check"

# Restart Home Assistant
ssh root@homeassistant.local "ha core restart"

# View logs
ssh root@homeassistant.local "ha core logs"

# Tail logs with grep
ssh root@homeassistant.local "ha core logs | grep -i error | tail -20"
```

## Deployment Workflows

### Standard Git Workflow (Final Changes)

Use for changes you want in version control:

```bash
# 1. Make changes locally
# 2. Check validity
ssh root@homeassistant.local "ha core check"

# 3. Commit and push
git add file.yaml
git commit -m "Description"
git push

# 4. CRITICAL: Pull to HA instance
ssh root@homeassistant.local "cd /config && git pull"

# 5. Reload or restart
hass-cli service call automation.reload  # if reload sufficient
# OR
ssh root@homeassistant.local "ha core restart"  # if restart needed

# 6. Verify
hass-cli state get sensor.new_entity
ssh root@homeassistant.local "ha core logs | grep -i error | tail -20"
```

### Rapid Development Workflow (Testing/Iteration)

Use `scp` for quick testing before committing:

```bash
# 1. Make changes locally
# 2. Quick deploy
scp automations.yaml root@homeassistant.local:/config/

# 3. Reload/restart
hass-cli service call automation.reload

# 4. Test and iterate (repeat 1-3 as needed)

# 5. Once finalized, commit to git
git add automations.yaml
git commit -m "Final tested changes"
git push
```

**When to use scp:**
- 🚀 Rapid iteration and testing
- 🔄 Frequent small adjustments
- 🧪 Experimental changes
- 🎨 UI/Dashboard work

**When to use git:**
- ✅ Final tested changes
- 📦 Version control tracking
- 🔒 Important configs
- 👥 Changes to document

## Reload vs Restart Decision Making

**ALWAYS assess if reload is sufficient before requiring a full restart.**

### Can be reloaded (fast, preferred):
- ✅ Automations: `hass-cli service call automation.reload`
- ✅ Scripts: `hass-cli service call script.reload`
- ✅ Scenes: `hass-cli service call scene.reload`
- ✅ Template entities: `hass-cli service call template.reload`
- ✅ Groups: `hass-cli service call group.reload`
- ✅ Themes: `hass-cli service call frontend.reload_themes`

### Require full restart:
- ❌ Min/Max sensors and platform-based sensors
- ❌ New integrations in configuration.yaml
- ❌ Core configuration changes
- ❌ MQTT sensor/binary_sensor platforms

## Automation Verification Workflow

**ALWAYS verify automations after deployment:**

### Step 1: Deploy
```bash
git add automations.yaml && git commit -m "..." && git push
ssh root@homeassistant.local "cd /config && git pull"
```

### Step 2: Check Configuration
```bash
ssh root@homeassistant.local "ha core check"
```

### Step 3: Reload
```bash
hass-cli service call automation.reload
```

### Step 4: Manually Trigger
```bash
hass-cli service call automation.trigger --arguments entity_id=automation.name
```

**Why trigger manually?**
- Instant feedback (don't wait for scheduled triggers)
- Verify logic before production
- Catch errors immediately

### Step 5: Check Logs
```bash
sleep 3
ssh root@homeassistant.local "ha core logs | grep -i 'automation_name' | tail -20"
```

**Success indicators:**
- `Initialized trigger AutomationName`
- `Running automation actions`
- `Executing step ...`
- No ERROR or WARNING messages

**Error indicators:**
- `Error executing script`
- `Invalid data for call_service`
- `TypeError`, `Template variable warning`

### Step 6: Verify Outcome

**For notifications:**
- Ask user if they received it
- Check logs for mobile_app messages

**For device control:**
```bash
hass-cli state get switch.device_name
```

**For sensors:**
```bash
hass-cli state get sensor.new_sensor
```

### Step 7: Fix and Re-test if Needed
If errors found:
1. Identify root cause from error messages
2. Fix the issue
3. Re-deploy (steps 1-2)
4. Re-verify (steps 3-6)

## Dashboard Management

### Dashboard Fundamentals

**What are Lovelace Dashboards?**
- JSON files in `.vault/` directory (e.g., `.vault/lovelace.control_center`)
- UI configuration for Home Assistant frontend
- Optimizable for different devices (mobile, tablet, wall panels)

**Critical Understanding:**
- Creating dashboard file is NOT enough - must register in `.vault/lovelace_dashboards`
- Dashboard changes don't require HA restart (just browser refresh)
- Use panel view for full-screen content (maps, cameras)
- Use sections view for organized multi-card layouts

### Dashboard Development Workflow

**Rapid Iteration with scp (Recommended for dashboards):**

```bash
# 1. Make changes locally
vim .vault/lovelace.control_center

# 2. Deploy immediately (no git commit yet)
scp .vault/lovelace.control_center root@homeassistant.local:/config/.vault/

# 3. Refresh browser (Ctrl+F5 or Cmd+Shift+R)
# No HA restart needed!

# 4. Iterate: Repeat 1-3 until perfect

# 5. Commit when stable
git add .vault/lovelace.control_center
git commit -m "Update dashboard layout"
git push
ssh root@homeassistant.local "cd /config && git pull"
```

**Why scp for dashboards:**
- Instant feedback (no HA restart)
- Iterate quickly on visual changes
- Commit only stable versions

### Creating New Dashboard

**Complete workflow:**

```bash
# Step 1: Create dashboard file
cp .vault/lovelace.my_home .vault/lovelace.new_dashboard

# Step 2: Register in lovelace_dashboards
# Edit .vault/lovelace_dashboards to add:
{
  "id": "new_dashboard",
  "show_in_sidebar": true,
  "icon": "mdi:tablet-dashboard",
  "title": "New Dashboard",
  "require_admin": false,
  "mode": "storage",
  "url_path": "new-dashboard"
}

# Step 3: Deploy both files
scp .vault/lovelace.new_dashboard root@homeassistant.local:/config/.vault/
scp .vault/lovelace_dashboards root@homeassistant.local:/config/.vault/

# Step 4: Restart HA (required for registry changes)
ssh root@homeassistant.local "ha core restart"
sleep 30

# Step 5: Verify appears in sidebar
```

**Update .gitignore to track:**
```gitignore
# Exclude .vault/ by default
.vault/

# Include dashboard files
!.vault/lovelace.new_dashboard
!.vault/lovelace_dashboards
```

### View Types Decision Matrix

**Use Panel View when:**
- Displaying full-screen map (vacuum, cameras)
- Single large card needs full width
- Want zero margins/padding
- Minimize scrolling

**Use Sections View when:**
- Organizing multiple cards
- Need responsive grid layout
- Building multi-section dashboards

**Layout Example:**
```json
// Panel view - full width, no margins
{
  "type": "panel",
  "title": "Vacuum Map",
  "path": "map",
  "cards": [
    {
      "type": "custom:xiaomi-vacuum-map-card",
      "entity": "vacuum.dusty"
    }
  ]
}

// Sections view - organized, has ~10% margins
{
  "type": "sections",
  "title": "Home",
  "sections": [
    {
      "type": "grid",
      "cards": [...]
    }
  ]
}
```

### Card Types Quick Reference

**Mushroom Cards (Modern, Touch-Optimized):**
```json
{
  "type": "custom:mushroom-light-card",
  "entity": "light.living_room",
  "use_light_color": true,
  "show_brightness_control": true,
  "collapsible_controls": true,
  "fill_container": true
}
```
- Best for tablets and touch screens
- Animated, colorful icons
- Built-in slider controls

**Mushroom Template Card (Dynamic Content):**
```json
{
  "type": "custom:mushroom-template-card",
  "primary": "All Doors",
  "secondary": "{% set sensors = ['binary_sensor.front_door'] %}\n{% set open = sensors | select('is_state', 'on') | list | length %}\n{{ open }} / {{ sensors | length }} open",
  "icon": "mdi:door",
  "icon_color": "{% if open > 0 %}red{% else %}green{% endif %}"
}
```
- Use Jinja2 templates for dynamic content
- Color-code status with icon_color
- Multi-line templates use `\n` in JSON

**Tile Card (Built-in, Modern):**
```json
{
  "type": "tile",
  "entity": "climate.thermostat",
  "features": [
    {"type": "climate-hvac-modes", "hvac_modes": ["heat", "cool", "fan_only", "off"]},
    {"type": "target-temperature"}
  ]
}
```
- No custom cards required
- Built-in features for controls

### Common Template Patterns

**Counting Open Doors:**
```jinja2
{% set door_sensors = [
  'binary_sensor.front_door',
  'binary_sensor.back_door'
] %}
{% set open = door_sensors | select('is_state', 'on') | list | length %}
{{ open }} / {{ door_sensors | length }} open
```

**Color-Coded Days Until:**
```jinja2
{% set days = state_attr('sensor.bin_collection', 'daysTo') | int %}
{% if days <= 1 %}red
{% elif days <= 3 %}amber
{% elif days <= 7 %}yellow
{% else %}grey
{% endif %}
```

**Conditional Display:**
```jinja2
{% set bins = [] %}
{% if days and days | int <= 7 %}
  {% set bins = bins + ['Recycling'] %}
{% endif %}
{% if bins %}This week: {{ bins | join(', ') }}{% else %}None this week{% endif %}
```

**IMPORTANT:** Always use `| int` or `| float` to avoid type errors when comparing

### Tablet Optimization

**Screen-specific layouts:**
- 11-inch tablets: 3-4 columns
- Touch targets: minimum 44x44px
- Minimize scrolling: Use panel view for full-screen
- Visual feedback: Color-coded status (red/green/amber)

**Grid Layout for Tablets:**
```json
{
  "type": "grid",
  "columns": 3,
  "square": false,
  "cards": [
    {"type": "custom:mushroom-light-card", "entity": "light.living_room"},
    {"type": "custom:mushroom-light-card", "entity": "light.bedroom"}
  ]
}
```

### Common Dashboard Pitfalls

**Problem 1: Dashboard Not in Sidebar**
- **Cause:** File created but not registered
- **Fix:** Add to `.vault/lovelace_dashboards` and restart HA

**Problem 2: "Configuration Error" in Card**
- **Cause:** Custom card not installed, wrong syntax, template error
- **Fix:**
  - Check HACS for card installation
  - Check browser console (F12) for details
  - Test templates in Developer Tools → Template

**Problem 3: Auto-Entities Fails**
- **Cause:** `card_param` not supported by card type
- **Fix:** Use cards that accept `entities` parameter:
  - ✅ Works: `entities`, `vertical-stack`, `horizontal-stack`
  - ❌ Doesn't work: `grid`, `glance` (without specific syntax)

**Problem 4: Vacuum Map Has Margins/Scrolling**
- **Cause:** Using sections view (has margins)
- **Fix:** Use panel view for full-width, no scrolling

**Problem 5: Template Type Errors**
- **Error:** `TypeError: '<' not supported between instances of 'str' and 'int'`
- **Fix:** Use type filters: `states('sensor.days') | int < 7`

### Dashboard Debugging

**1. Browser Console (F12):**
- Check for red errors when loading dashboard
- Common: "Custom element doesn't exist" → Card not installed

**2. Validate JSON Syntax:**
```bash
python3 -m json.tool .vault/lovelace.control_center > /dev/null
```

**3. Test Templates:**
```
Home Assistant → Developer Tools → Template
Paste template to test before adding to dashboard
```

**4. Verify Entities:**
```bash
hass-cli state get binary_sensor.front_door
```

**5. Clear Browser Cache:**
- Hard refresh: Ctrl+F5 or Cmd+Shift+R
- Try incognito window

## Real-World Examples

### Quick Controls Dashboard Section
```json
{
  "type": "grid",
  "title": "Quick Controls",
  "cards": [
    {
      "type": "custom:mushroom-template-card",
      "primary": "All Doors",
      "secondary": "{% set doors = ['binary_sensor.front_door', 'binary_sensor.back_door'] %}\n{% set open = doors | select('is_state', 'on') | list | length %}\n{{ open }} / {{ doors | length }} open",
      "icon": "mdi:door",
      "icon_color": "{% if open > 0 %}red{% else %}green{% endif %}"
    },
    {
      "type": "tile",
      "entity": "climate.thermostat",
      "features": [
        {"type": "climate-hvac-modes", "hvac_modes": ["heat", "cool", "fan_only", "off"]},
        {"type": "target-temperature"}
      ]
    }
  ]
}
```

### Individual Light Cards (Touch-Friendly)
```json
{
  "type": "grid",
  "title": "Lights",
  "columns": 3,
  "cards": [
    {
      "type": "custom:mushroom-light-card",
      "entity": "light.office_studio",
      "name": "Office",
      "use_light_color": true,
      "show_brightness_control": true,
      "collapsible_controls": true
    }
  ]
}
```

### Full-Screen Vacuum Map
```json
{
  "type": "panel",
  "title": "Vacuum",
  "path": "vacuum-map",
  "cards": [
    {
      "type": "custom:xiaomi-vacuum-map-card",
      "vacuum_platform": "Tasshack/dreame-vacuum",
      "entity": "vacuum.dusty"
    }
  ]
}
```

## Common Commands Quick Reference

```bash
# Configuration
ssh root@homeassistant.local "ha core check"
ssh root@homeassistant.local "ha core restart"

# Logs
ssh root@homeassistant.local "ha core logs | tail -50"
ssh root@homeassistant.local "ha core logs | grep -i error | tail -20"

# State/Services
hass-cli state list
hass-cli state get entity.name
hass-cli service call automation.reload
hass-cli service call automation.trigger --arguments entity_id=automation.name

# Deployment
git add . && git commit -m "..." && git push
ssh root@homeassistant.local "cd /config && git pull"
scp file.yaml root@homeassistant.local:/config/

# Dashboard deployment
scp .vault/lovelace.my_dashboard root@homeassistant.local:/config/.vault/
python3 -m json.tool .vault/lovelace.my_dashboard > /dev/null  # Validate JSON

# Quick test cycle
scp automations.yaml root@homeassistant.local:/config/
hass-cli service call automation.reload
hass-cli service call automation.trigger --arguments entity_id=automation.name
ssh root@homeassistant.local "ha core logs | grep -i 'automation' | tail -10"
```

## Best Practices Summary

1. **Always check configuration** before restart: `ha core check`
2. **Prefer reload over restart** when possible
3. **Test automations manually** after deployment
4. **Check logs** for errors after every change
5. **Use scp for rapid iteration**, git for final changes
6. **Verify outcomes** - don't assume it worked
7. **Use Context7** for current documentation
8. **Test templates in Dev Tools** before adding to dashboards
9. **Validate JSON syntax** before deploying dashboards
10. **Test on actual device** for tablet dashboards
11. **Color-code status** for visual feedback (red/green/amber)
12. **Commit only stable versions** - test with scp first

## Workflow Decision Tree

```
Configuration Change Needed
├─ Is this final/tested?
│  ├─ YES → Use git workflow
│  └─ NO → Use scp workflow
├─ Check configuration valid
├─ Deploy (git pull or scp)
├─ Needs restart?
│  ├─ YES → ha core restart
│  └─ NO → Use appropriate reload
├─ Verify in logs
└─ Test outcome

Dashboard Change Needed
├─ Make changes locally
├─ Deploy via scp for testing
├─ Refresh browser (Ctrl+F5)
├─ Test on target device
├─ Iterate until perfect
└─ Commit to git when stable
```

---

This skill encapsulates efficient Home Assistant management workflows developed through iterative optimization and real-world dashboard development. Apply these patterns to any Home Assistant instance for reliable, fast, and safe configuration management.
```


# 📝 Pull Request Description

Please provide a clear and concise description of what this PR changes and why it's needed.

## 🔄 Changes Made

### 📊 CSV Format Changes (if applicable)

- [ ] Added new fields to CSV format
- [ ] Modified existing field structure
- [ ] Maintained backward compatibility

### 💻 CLI Changes (if applicable)

- [ ] Added new CLI commands
- [ ] Modified existing commands
- [ ] Updated help text

### 🧪 Core Logic Changes (if applicable)

- [ ] Updated CSV parsing logic
- [ ] Modified search/filter functionality
- [ ] Enhanced logging utilities

### 📚 Documentation Updates

- [ ] Updated README.md
- [ ] Added/updated code comments
- [ ] Updated CLI help text

## 🧪 Testing

### Manual Testing

Please describe the manual testing you performed:

```bash
# Example commands you tested
bun cli list
bun cli add "Test log" --tags=test --problem="Testing" --solution="Fixed"
bun cli search "test"
bun cli stats
```

### Test Scenarios

- [ ] Tested with existing CSV logs
- [ ] Tested with new CSV format (if applicable)
- [ ] Tested CLI commands work correctly
- [ ] Tested error handling
- [ ] Tested edge cases (empty logs, malformed CSV, etc.)

## 📊 CSV Format Validation (if applicable)

If this PR changes the CSV format, please provide examples:

**Before:**

```csv
name,tags,problem,solution,created-at,updated-at
```

**After:**

```csv
name,tags,problem,solution,created-at,updated-at,new-field
```

## 🎯 LLM Token Optimization

Consider the impact on LLM token usage:

- [ ] Changes maintain or improve token efficiency
- [ ] New fields add minimal token overhead
- [ ] Format remains simple and predictable for LLMs

## 📋 Checklist

### Code Quality

- [ ] Code follows the project's coding standards
- [ ] Added appropriate comments for new functions
- [ ] Used functional programming approach (no classes/OOP)
- [ ] Code is formatted with Biome

### Testing & Validation

- [ ] All existing tests still pass
- [ ] Added new tests for new functionality
- [ ] Manual testing completed successfully
- [ ] Edge cases considered and handled

### Documentation

- [ ] README.md updated if needed
- [ ] CLI help text updated if commands changed
- [ ] Code comments added for new/modified functions

### Project Standards

- [ ] Changes align with LLM-optimized logging goals
- [ ] CSV format remains simple and efficient
- [ ] No breaking changes without proper justification
- [ ] Dependencies updated appropriately

## 🔗 Related Issues

Closes #(issue number)
Related to #(issue number)

## 📸 Screenshots (if applicable)

If this PR includes UI/CLI changes, please add screenshots:

**Before:**
[Add screenshot here]

**After:**
[Add screenshot here]

## 💬 Additional Notes

Any additional context, notes, or considerations for the reviewers.

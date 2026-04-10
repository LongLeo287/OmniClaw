---
description: Code review workflow – systematic PR review process following the Code Reviewer agent standards
---

# Code Review Workflow

## Steps

1. **Read PR description and linked issue**
Understand the context: what problem is being solved and why.

2. **Check CI status**
// turbo
```bash
git fetch origin
git log origin/main..HEAD --oneline
```
CI must be green before review starts.

3. **Pull the PR branch locally**
```bash
git fetch origin <branch-name>
git checkout <branch-name>
```

4. **Run tests locally**
// turbo
```bash
pytest tests/ -v --tb=short
```

5. **Run lint check**
// turbo
```bash
ruff check contribai/
```

6. **Review code changes**
Go through the Code Reviewer checklist:
- [ ] Functionality: code does what PR says, edge cases handled
- [ ] Architecture: correct module, no circular imports
- [ ] Code quality: functions < 50 lines, files < 400 lines, no duplication
- [ ] Documentation: docstrings, README updated if needed
- [ ] Testing: new code has tests, edge cases covered
- [ ] Security: no secrets, inputs validated, LLM output untrusted
- [ ] Performance: no N+1, async for I/O

7. **Check for breaking changes**
Review `contribai/core/models.py` and `contribai/core/config.py` for any model changes that could break existing configs or data.

8. **Leave review comments**
Use severity labels:
- `nit:` – Style preference, non-blocking
- `suggestion:` – Improvement idea, non-blocking
- `issue:` – Must fix before merge
- `question:` – Need clarification
- `blocker:` – Critical, blocks merge

9. **Write summary comment**
Overall assessment of the PR quality and any blocking issues.

10. **Approve or request changes**
- **Approve**: All checks pass, code is clean
- **Request Changes**: Has blocking issues
- **Comment**: Non-blocking suggestions only

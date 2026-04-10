---
description: Security audit workflow – scan for vulnerabilities, review dependencies, check for secrets
---

# Security Audit Workflow

## Steps

1. **Check for hardcoded secrets**
// turbo
```bash
ruff check contribai/ --select S105,S106,S107
```
Also manually search for common patterns:
// turbo
```bash
python -c "import pathlib; files = list(pathlib.Path('contribai').rglob('*.py')); [print(f'{f}:{i+1}: {line.strip()}') for f in files for i, line in enumerate(f.read_text().splitlines()) if any(kw in line.lower() for kw in ['password', 'secret', 'api_key', 'token'] if 'config' not in str(f))]"
```

2. **Check dependencies for known vulnerabilities**
```bash
pip audit
```

3. **Review security-sensitive files**
Manually inspect these critical files:
- `contribai/core/config.py` – Token/key handling
- `contribai/github/client.py` – API authentication
- `contribai/llm/provider.py` – API key handling
- `contribai/pr/manager.py` – Git operations
- `contribai/analysis/analyzer.py` – LLM output parsing

4. **Check for unsafe deserialization**
// turbo
```bash
python -c "import pathlib; files = list(pathlib.Path('contribai').rglob('*.py')); [print(f'{f}:{i+1}: {line.strip()}') for f in files for i, line in enumerate(f.read_text().splitlines()) if 'yaml.load(' in line and 'safe_load' not in line]"
```

5. **Check .gitignore covers sensitive files**
// turbo
```bash
python -c "required = ['config.yaml', '.env', '*.db', '*.sqlite']; import pathlib; gi = pathlib.Path('.gitignore').read_text(); [print(f'✅ {r}' if r in gi else f'❌ MISSING: {r}') for r in required]"
```

6. **Verify LLM output sanitization**
Check that all LLM responses are treated as untrusted:
- JSON parsing uses try/except
- No `eval()` or `exec()` on LLM output
- File paths from LLM are validated
- No shell commands constructed from LLM output

7. **Create security report**
Document findings in `docs/security-audit-YYYY-MM-DD.md`

8. **Fix critical issues immediately**
Any critical finding should be fixed on a `fix/security-*` branch with priority review.

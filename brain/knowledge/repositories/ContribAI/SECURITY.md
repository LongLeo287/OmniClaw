# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.4.x   | ✅ Active |
| 2.3.x   | ✅        |
| 2.0.x – 2.2.x | ⚠️ Security fixes only |
| < 2.0   | ❌        |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Create a [GitHub Issue](https://github.com/tang-vu/ContribAI/issues/new)** with the `security` label
2. For critical vulnerabilities, use [GitHub Security Advisories](https://github.com/tang-vu/ContribAI/security/advisories) instead
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Response Timeline
- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 1 week
- **Fix & Release**: Within 2 weeks for critical issues

## Security Considerations

ContribAI handles sensitive data:
- **GitHub Tokens** – Stored in `config.yaml` (gitignored)
- **LLM API Keys** – Stored in `config.yaml` (gitignored)
- **LLM Outputs** – Treated as untrusted data, sanitized before use
- **Repository Code** – Fetched via API, processed in memory
- **PR Outcomes** – Stored locally in SQLite database

### What We Do
- Config files with secrets are in `.gitignore`
- Only `yaml.safe_load()` is used (no unsafe deserialization)
- LLM output is parsed with try/except, never `eval()`'d
- GitHub tokens use minimal required scopes
- Rate limiting prevents API abuse
- DCO signoff on all commits via GitHub API
- Middleware chain validates and gates every pipeline action

### Architecture Security (v2.4.0)
- **Middleware chain** — RateLimit and Validation middlewares run before any processing
- **Quality gate** — QualityGateMiddleware blocks low-scoring contributions
- **Retry with backoff** — RetryMiddleware prevents retry-based abuse
- **Outcome memory** — Learns from rejected PRs to avoid repeating mistakes
- **Tool protocol** — All external interactions go through typed Tool interface

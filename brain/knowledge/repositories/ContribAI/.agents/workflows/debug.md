---
description: Debugging workflow – systematic approach to finding and fixing bugs
---

# Debug Workflow

## Steps

1. **Reproduce the issue**
Run the failing command with verbose logging:
```bash
contribai <command> -v
```

2. **Check the error traceback**
Read the full traceback. Identify:
- Which module threw the error
- The exception type (from `contribai.core.exceptions`?)
- The root cause vs. symptom

3. **Enable debug logging**
// turbo
```bash
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
# Then run the problematic code
"
```

4. **Run specific test in debug mode**
// turbo
```bash
pytest tests/ -v -s --log-cli-level=DEBUG -k "test_name"
```

5. **Common debugging patterns**

### GitHub API issues
```python
# Check rate limit
import asyncio
from contribai.github.client import GitHubClient
async def check():
    client = GitHubClient(token="ghp_...")
    rl = await client.check_rate_limit()
    print(rl)
    await client.close()
asyncio.run(check())
```

### LLM issues
```python
# Test LLM directly
import asyncio
from contribai.core.config import load_config
from contribai.llm.provider import create_llm_provider
async def test():
    config = load_config()
    llm = create_llm_provider(config.llm)
    response = await llm.complete("Hello, respond with 'OK'")
    print(f"Response: {response}")
    await llm.close()
asyncio.run(test())
```

### Memory/DB issues
```python
# Check memory DB
import asyncio
from contribai.orchestrator.memory import Memory
async def check():
    mem = Memory("~/.contribai/memory.db")
    await mem.init()
    stats = await mem.get_stats()
    print(stats)
    prs = await mem.get_prs()
    print(f"PRs: {len(prs)}")
    await mem.close()
asyncio.run(check())
```

6. **Fix the bug**
- Create a `fix/` branch
- Write a failing test first (TDD)
- Implement the fix
- Verify the test passes

7. **Verify no regressions**
// turbo
```bash
pytest tests/ -v --tb=short
```

8. **Commit the fix**
```bash
git add -A
git commit -m "fix(<module>): <description of fix>"
```

## Common Issues & Solutions

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| `RateLimitError` | GitHub API quota exceeded | Wait for reset, reduce `max_repos_per_run` |
| `LLMRateLimitError` | LLM API quota exceeded | Switch provider, wait, or reduce requests |
| `ConfigError` | Invalid config.yaml | Check YAML syntax, compare with `config.example.yaml` |
| `GitHubAPIError 404` | Repo not found or private | Verify URL, check token permissions |
| `LLMError` | API key invalid or wrong model | Verify API key and model name in config |

---
description: Testing workflow – run tests, check coverage, fix failures, add missing tests
---

# Testing Workflow

## Steps

1. **Run all tests**
// turbo
```bash
pytest tests/ -v --tb=short
```

2. **Check coverage**
// turbo
```bash
pytest tests/ --cov=contribai --cov-report=term-missing --cov-fail-under=50
```

3. **Identify untested code**
Look at the `Missing` column in the coverage report to find uncovered lines.

4. **Run specific module tests**
// turbo
```bash
pytest tests/unit/test_config.py -v -s
```

5. **Run tests with debug output**
// turbo
```bash
pytest tests/ -v -s --log-cli-level=DEBUG
```

6. **Write missing tests**
Follow the QA Engineer standards:
```python
# File: tests/unit/test_<module>.py
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

# Arrange-Act-Assert pattern
async def test_function_happy_path():
    # Arrange
    mock_dep = AsyncMock()
    sut = SystemUnderTest(mock_dep)
    
    # Act
    result = await sut.do_thing(input_data)
    
    # Assert
    assert result.status == "success"
    mock_dep.called_method.assert_called_once()

# Parametrize for edge cases
@pytest.mark.parametrize("input,expected", [
    ("valid", True),
    ("", False),
    (None, False),
])
def test_validation(input, expected):
    assert validate(input) == expected
```

7. **Run only failing tests**
// turbo
```bash
pytest tests/ -v --lf
```

8. **Generate HTML coverage report**
// turbo
```bash
pytest tests/ --cov=contribai --cov-report=html
```
Open `htmlcov/index.html` to browse coverage visually.

## Test Categories
- `tests/unit/` – Isolated module tests with mocked dependencies
- `tests/integration/` – Multi-module tests
- `tests/fixtures/` – Canned responses and sample data

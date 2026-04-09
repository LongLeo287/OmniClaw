.PHONY: install test lint format build clean docker help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install package with dev dependencies
	pip install -e ".[dev]"

test: ## Run tests with coverage
	pytest tests/ -v --tb=short --cov=contribai --cov-report=term-missing

test-quick: ## Run tests without coverage
	pytest tests/ -v --tb=short

lint: ## Lint and format code
	ruff check contribai/ --fix
	ruff format contribai/ tests/

lint-check: ## Check lint without fixing
	ruff check contribai/
	ruff format --check contribai/ tests/

build: ## Build Python package
	python -m build

docker: ## Build Docker image
	docker build -t contribai:latest .

docker-run: ## Run with Docker (dry run)
	docker run --rm -v $(PWD)/config.yaml:/home/contribai/config.yaml:ro contribai:latest run --dry-run

clean: ## Clean build artifacts
	rm -rf dist/ build/ *.egg-info .pytest_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

stats: ## Show project statistics
	@echo "📁 Python files:"
	@find contribai -name "*.py" | wc -l
	@echo "📝 Lines of code:"
	@find contribai -name "*.py" -exec cat {} + | wc -l
	@echo "🧪 Test files:"
	@find tests -name "*.py" 2>/dev/null | wc -l || echo "0"

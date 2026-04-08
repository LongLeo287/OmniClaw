"""Custom exception hierarchy for ContribAI."""


class ContribAIError(Exception):
    """Base exception for all ContribAI errors."""

    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.details = details or {}


class ConfigError(ContribAIError):
    """Configuration loading or validation error."""


class GitHubAPIError(ContribAIError):
    """GitHub API request failure."""

    def __init__(self, message: str, status_code: int | None = None, **kwargs):
        super().__init__(message, **kwargs)
        self.status_code = status_code


class RateLimitError(GitHubAPIError):
    """GitHub API rate limit exceeded."""

    def __init__(self, reset_at: int | None = None, **kwargs):
        super().__init__("GitHub API rate limit exceeded", **kwargs)
        self.reset_at = reset_at


class LLMError(ContribAIError):
    """LLM provider error."""


class LLMRateLimitError(LLMError):
    """LLM rate limit exceeded."""


class AnalysisError(ContribAIError):
    """Code analysis failure."""


class ContributionError(ContribAIError):
    """Contribution generation failure."""


class PRCreationError(ContribAIError):
    """Pull request creation failure."""

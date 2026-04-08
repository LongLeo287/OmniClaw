"""Message formatter abstraction for multi-provider LLM support.

Decouples message formatting from provider logic — each provider
uses a formatter to translate generic messages into provider-specific format.

Inspired by AgentScope's FormatterBase pattern.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

logger = logging.getLogger(__name__)


class FormatterBase(ABC):
    """Abstract base for message formatters.

    Translates a list of generic chat messages into provider-specific format.
    """

    @abstractmethod
    def format_messages(
        self,
        messages: list[dict[str, str]],
        *,
        system: str | None = None,
    ) -> Any:
        """Format messages for a specific LLM provider.

        Args:
            messages: List of {"role": "user"|"assistant"|"system", "content": "..."}.
            system: Optional system prompt (some providers handle this separately).

        Returns:
            Provider-specific formatted messages.
        """

    @abstractmethod
    def format_prompt(self, prompt: str, *, system: str | None = None) -> Any:
        """Format a single prompt string for completion.

        Args:
            prompt: User prompt text.
            system: Optional system prompt.

        Returns:
            Provider-specific formatted input.
        """


class GeminiFormatter(FormatterBase):
    """Formatter for Google Gemini API.

    Converts standard messages to Gemini's Content/Part format.
    """

    def format_messages(
        self,
        messages: list[dict[str, str]],
        *,
        system: str | None = None,
    ) -> dict[str, Any]:
        """Format messages for Gemini.

        Returns:
            Dict with 'contents' (list of Content) and 'system_instruction' (str|None).
        """
        try:
            from google.genai import types
        except ImportError:
            # Fallback: return raw dicts if google-genai not installed
            return {"contents": messages, "system_instruction": system}

        contents = []
        for msg in messages:
            role = "model" if msg["role"] == "assistant" else "user"
            contents.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))

        return {"contents": contents, "system_instruction": system}

    def format_prompt(self, prompt: str, *, system: str | None = None) -> dict[str, Any]:
        return {"contents": prompt, "system_instruction": system}


class OpenAIFormatter(FormatterBase):
    """Formatter for OpenAI-compatible APIs (GPT-4, etc.)."""

    def format_messages(
        self,
        messages: list[dict[str, str]],
        *,
        system: str | None = None,
    ) -> list[dict[str, str]]:
        """Format messages for OpenAI chat completion.

        Returns:
            List of {"role": ..., "content": ...} with system prepended.
        """
        formatted: list[dict[str, str]] = []
        if system:
            formatted.append({"role": "system", "content": system})
        formatted.extend(messages)
        return formatted

    def format_prompt(self, prompt: str, *, system: str | None = None) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        return messages


class AnthropicFormatter(FormatterBase):
    """Formatter for Anthropic Claude API."""

    def format_messages(
        self,
        messages: list[dict[str, str]],
        *,
        system: str | None = None,
    ) -> dict[str, Any]:
        """Format messages for Anthropic.

        Returns:
            Dict with 'messages' (filtered, no system role) and 'system' prompt.
        """
        # Anthropic handles system separately, not in messages list
        filtered = [m for m in messages if m["role"] != "system"]
        return {"messages": filtered, "system": system or ""}

    def format_prompt(self, prompt: str, *, system: str | None = None) -> dict[str, Any]:
        return {
            "messages": [{"role": "user", "content": prompt}],
            "system": system or "",
        }


class OllamaFormatter(FormatterBase):
    """Formatter for Ollama local models."""

    def format_messages(
        self,
        messages: list[dict[str, str]],
        *,
        system: str | None = None,
    ) -> list[dict[str, str]]:
        """Format messages for Ollama (OpenAI-compatible)."""
        formatted: list[dict[str, str]] = []
        if system:
            formatted.append({"role": "system", "content": system})
        formatted.extend(messages)
        return formatted

    def format_prompt(self, prompt: str, *, system: str | None = None) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        return messages


# Provider → Formatter mapping
PROVIDER_FORMATTERS: dict[str, type[FormatterBase]] = {
    "gemini": GeminiFormatter,
    "openai": OpenAIFormatter,
    "anthropic": AnthropicFormatter,
    "ollama": OllamaFormatter,
}


def get_formatter(provider: str) -> FormatterBase:
    """Get the appropriate formatter for a provider.

    Args:
        provider: Provider name (gemini, openai, anthropic, ollama).

    Returns:
        Formatter instance.
    """
    formatter_cls = PROVIDER_FORMATTERS.get(provider, OpenAIFormatter)
    return formatter_cls()

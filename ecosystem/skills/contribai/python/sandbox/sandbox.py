"""Sandbox execution for validating generated code.

Inspired by DeerFlow and SWE-agent — runs code in isolated Docker
containers to verify syntax and basic correctness before creating PRs.
"""

from __future__ import annotations

import asyncio
import logging
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class SandboxResult:
    """Result of sandbox code execution.

    Attributes:
        success: Whether the code passed validation.
        output: Stdout from execution.
        errors: Stderr or error messages.
        language: Language that was validated.
        duration_sec: Execution duration.
    """

    success: bool = False
    output: str = ""
    errors: str = ""
    language: str = ""
    duration_sec: float = 0.0


# Language → Docker image mapping
LANGUAGE_IMAGES: dict[str, str] = {
    "python": "python:3.12-slim",
    "javascript": "node:20-slim",
    "typescript": "node:20-slim",
    "go": "golang:1.22-alpine",
    "rust": "rust:1.77-slim",
}

# Language → syntax check command (validates without executing)
SYNTAX_CHECK_COMMANDS: dict[str, str] = {
    "python": 'python -c "import ast, sys; ast.parse(sys.stdin.read())"',
    "javascript": "node --check /tmp/code.js",
    "typescript": "node --check /tmp/code.ts",
    "go": "gofmt -e /tmp/code.go",
    "rust": "rustfmt --check /tmp/code.rs",
}


class Sandbox:
    """Validates generated code in isolated Docker containers.

    Performs syntax checking without full execution to catch obvious
    errors before submitting PRs.

    Usage:
        sandbox = Sandbox(enabled=True, timeout=30)
        result = await sandbox.validate("print('hello')", "python")
        if not result.success:
            logger.error("Code failed validation: %s", result.errors)
    """

    def __init__(
        self,
        enabled: bool = False,
        timeout: int = 30,
        docker_image: str = "",
    ):
        self._enabled = enabled
        self._timeout = timeout
        self._docker_image_override = docker_image

    @property
    def enabled(self) -> bool:
        """Whether sandbox validation is enabled."""
        return self._enabled

    @property
    def available(self) -> bool:
        """Whether Docker is available on this system."""
        return shutil.which("docker") is not None

    async def validate(self, code: str, language: str) -> SandboxResult:
        """Validate code syntax in a Docker container.

        Args:
            code: Source code to validate.
            language: Programming language.

        Returns:
            SandboxResult with success status and any errors.
        """
        if not self._enabled:
            return SandboxResult(success=True, output="Sandbox disabled", language=language)

        if not self.available:
            logger.warning("Docker not found, falling back to local validation")
            return await self._validate_local(code, language)

        return await self._validate_docker(code, language)

    async def validate_batch(
        self,
        files: dict[str, str],
        language: str,
    ) -> dict[str, SandboxResult]:
        """Validate multiple files.

        Args:
            files: Mapping of {path: content}.
            language: Programming language.

        Returns:
            Mapping of {path: SandboxResult}.
        """
        results: dict[str, SandboxResult] = {}
        for path, content in files.items():
            results[path] = await self.validate(content, language)
        return results

    async def _validate_docker(self, code: str, language: str) -> SandboxResult:
        """Run syntax check inside Docker container."""
        import time

        image = self._docker_image_override or LANGUAGE_IMAGES.get(language)
        if not image:
            return SandboxResult(
                success=True,
                output=f"No Docker image for {language}, skipping",
                language=language,
            )

        # Write code to temp file
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=self._get_extension(language), delete=False
        ) as f:
            f.write(code)
            temp_path = f.name

        try:
            start = time.monotonic()
            cmd = self._build_docker_command(image, temp_path, language)
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(),
                timeout=self._timeout,
            )
            duration = time.monotonic() - start

            return SandboxResult(
                success=proc.returncode == 0,
                output=stdout.decode()[:2000],
                errors=stderr.decode()[:2000],
                language=language,
                duration_sec=round(duration, 2),
            )
        except TimeoutError:
            return SandboxResult(
                success=False,
                errors=f"Timeout after {self._timeout}s",
                language=language,
                duration_sec=float(self._timeout),
            )
        except Exception as e:
            return SandboxResult(
                success=False,
                errors=str(e),
                language=language,
            )
        finally:
            Path(temp_path).unlink(missing_ok=True)

    async def _validate_local(self, code: str, language: str) -> SandboxResult:
        """Fallback: validate locally without Docker."""

        if language == "python":
            return self._validate_python_local(code)

        # For other languages, just return success (can't validate without Docker)
        return SandboxResult(
            success=True,
            output=f"No local validator for {language}",
            language=language,
        )

    @staticmethod
    def _validate_python_local(code: str) -> SandboxResult:
        """Validate Python syntax using ast.parse."""
        import ast
        import time

        start = time.monotonic()
        try:
            ast.parse(code)
            return SandboxResult(
                success=True,
                output="Syntax OK",
                language="python",
                duration_sec=round(time.monotonic() - start, 4),
            )
        except SyntaxError as e:
            return SandboxResult(
                success=False,
                errors=f"SyntaxError at line {e.lineno}: {e.msg}",
                language="python",
                duration_sec=round(time.monotonic() - start, 4),
            )

    @staticmethod
    def _build_docker_command(image: str, file_path: str, language: str) -> str:
        """Build docker run command for syntax checking."""
        ext = Sandbox._get_extension(language)
        container_path = f"/tmp/code{ext}"
        check_cmd = SYNTAX_CHECK_COMMANDS.get(language, f"cat {container_path}")

        return (
            f"docker run --rm --network none "
            f"-v {file_path}:{container_path}:ro "
            f"--memory 128m --cpus 0.5 "
            f"{image} sh -c '{check_cmd}'"
        )

    @staticmethod
    def _get_extension(language: str) -> str:
        """Get file extension for a language."""
        return {
            "python": ".py",
            "javascript": ".js",
            "typescript": ".ts",
            "go": ".go",
            "rust": ".rs",
        }.get(language, ".txt")

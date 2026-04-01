"""
CUSTOMS CHECKPOINT
CEO Rule: "Those with pass go easier but ARE STILL CHECKED. No pass gets strict checks."
Log ALL requests (PASS and FAIL) for audit trail.
"""
from __future__ import annotations

import json
import logging
import os
import uuid
from pathlib import Path
from fastapi import Request, HTTPException

# ── Logging setup ──────────────────────────────────────────────────────────────
_ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
LOG_DIR = _ROOT / "system" / "ops" / "telemetry" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("BorderSecurity")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    fh = logging.FileHandler(LOG_DIR / "border_security.log", encoding='utf-8')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(fh)

# ── Bad keyword list (prompt injection + code injection) ───────────────────────
_BAD_KEYWORDS = [
    "DROP TABLE", "DELETE FROM", "INSERT INTO", "SELECT *",  # SQL injection
    "<script>", "javascript:", "onerror=",                   # XSS
    "/bin/bash", "/bin/sh", "sudo rm", "cmd.exe",            # Shell injection
    "ignore all previous instructions",                       # Prompt injection
    "ignore previous", "disregard your instructions",
    "you are now", "act as DAN", "jailbreak",
    "../../../", "..\\..\\",                                  # Path traversal
]

_GUEST_SIZE_LIMIT = 10 * 1024       # 10 KB
_VIP_SIZE_LIMIT   = 50 * 1024 * 1024  # 50 MB
_VALID_PLATFORMS  = {"zalo", "telegram", "facebook", "discord", "line", "whatsapp"}


# ── Scan functions ─────────────────────────────────────────────────────────────

async def strict_payload_scan(payload: str, request_id: str) -> bool:
    """Strict byte check: SQL/XSS/shell injection, prompt injection, size."""
    if len(payload) > _GUEST_SIZE_LIMIT:
        logger.warning(f"[{request_id}] OVERSIZE: {len(payload)} bytes > {_GUEST_SIZE_LIMIT}B limit (GUEST)")
        return False

    payload_lower = payload.lower()
    for kw in _BAD_KEYWORDS:
        if kw.lower() in payload_lower:
            logger.error(f"[{request_id}] MALICIOUS KEYWORD: '{kw}'")
            return False

    return True


async def vip_payload_scan(payload: str, request_id: str) -> bool:
    """Light check for VIP/HQ: only size and path traversal."""
    if len(payload) > _VIP_SIZE_LIMIT:
        logger.warning(f"[{request_id}] VIP OVERSIZE: {len(payload)} bytes > {_VIP_SIZE_LIMIT}B")
        return False

    # Path traversal is still blocked even for VIP
    for kw in ["../../../", "..\\..\\", "/etc/passwd", "/etc/shadow"]:
        if kw in payload:
            logger.error(f"[{request_id}] VIP PATH TRAVERSAL attempt: '{kw}'")
            return False

    return True


async def inspect_cargo(request: Request, passport_status: dict) -> bool:
    """
    Inspect cargo (body) passing checkpoint.
    Log ALL requests (PASS and FAIL) for audit.
    Return True if passed, raise HTTPException otherwise.
    """
    level = passport_status.get("level", "UNKNOWN")
    owner = passport_status.get("owner", "UNKNOWN")
    client_ip = request.client.host if request.client else "UNKNOWN_IP"
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
    endpoint = str(request.url.path)

    try:
        body_bytes = await request.body()
        payload_str = body_bytes.decode('utf-8', errors='replace')
    except Exception as e:
        logger.error(f"[{request_id}] DECODE ERROR from {client_ip}: {e}")
        raise HTTPException(status_code=400, detail="Payload encoding error.")

    is_vip = level in {"VIP", "OMNICLAW_HQ", "SYSTEM_BOT"}
    is_safe = await (vip_payload_scan(payload_str, request_id) if is_vip
                     else strict_payload_scan(payload_str, request_id))

    if is_safe:
        logger.info(f"[{request_id}] PASS | {level} | {owner} | {client_ip} | {endpoint} | {len(payload_str)}B")
    else:
        logger.critical(f"[{request_id}] BLOCK | {level} | {owner} | {client_ip} | {endpoint}")
        detail = ("Payload oversize or VIP standard violation."
                  if is_vip else "Malicious / Sabotage from unknown guest. DROP.")
        raise HTTPException(status_code=403, detail=detail)

    return True


def validate_platform(platform: str) -> str:
    """Validate bot platform name. Return normalized platform, raise HTTPException if invalid."""
    normalized = platform.lower().strip()
    if normalized not in _VALID_PLATFORMS:
        raise HTTPException(
            status_code=400,
            detail=f"Platform '{platform}' not supported. Supported: {sorted(_VALID_PLATFORMS)}"
        )
    return normalized
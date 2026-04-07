"""
CUSTOMS CHECKPOINT (OSF Upgraded)
CEO Rule: "Those with pass go easier but ARE STILL CHECKED. No pass gets strict checks."
OSF Additions: Rate Limiting & Regex WAF & Log Rotation
"""
from __future__ import annotations

import json
import logging
import os
import re
import time
import uuid
from pathlib import Path
from fastapi import Request, HTTPException
from logging.handlers import RotatingFileHandler

# ── Logging setup ──────────────────────────────────────────────────────────────
_ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
LOG_DIR = _ROOT / "core" / "ops" / "telemetry" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("BorderSecurity")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    fh = RotatingFileHandler(LOG_DIR / "border_security.log", maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(fh)

# ── WAF Regex Patterns (OSF Standard) ──────────────────────────────────────────
_BAD_PATTERNS = [
    re.compile(r"(?i)(drop|delete|insert|update|select).*?(from|table|into)"), # SQLi
    re.compile(r"(?i)<script.*?>|javascript:|onerror="),                         # XSS
    re.compile(r"(?i)(/bin/bash|/bin/sh|sudo\s+rm|cmd\.exe)"),                   # Shell
    re.compile(r"(?i)(ignore.*previous|disregard.*instructions|jailbreak)"),     # Prompt Injection
    re.compile(r"(?i)(\.\./\.\./|\.\.\\\.\.\\|/etc/passwd)"),                    # Path Traversal
]

_GUEST_SIZE_LIMIT = 10 * 1024       # 10 KB
_VIP_SIZE_LIMIT   = 50 * 1024 * 1024  # 50 MB
_VALID_PLATFORMS  = {"zalo", "telegram", "facebook", "discord", "line", "whatsapp"}

# ── Rate Limiter State ─────────────────────────────────────────────────────────
_rate_limit_cache: dict[str, list[float]] = {}
GUEST_RATE_LIMIT = 5  # reqs / sec
VIP_RATE_LIMIT = 100  # reqs / sec

def _check_rate_limit(client_id: str, is_vip: bool) -> bool:
    """Returns True if allowed, False if limit exceeded."""
    limit = VIP_RATE_LIMIT if is_vip else GUEST_RATE_LIMIT
    now = time.time()
    
    # Prune old timestamps efficiently
    history = _rate_limit_cache.get(client_id, [])
    # Keep only requests within the last 1.0 second
    history = [ts for ts in history if now - ts < 1.0]
    
    if len(history) >= limit:
        # Update cache to keep latest state anyway
        _rate_limit_cache[client_id] = history
        return False
        
    history.append(now)
    _rate_limit_cache[client_id] = history
    return True


# ── Scan functions ─────────────────────────────────────────────────────────────

async def strict_payload_scan(payload: str, request_id: str) -> bool:
    """Strict check: Regex WAF & size limit."""
    if len(payload) > _GUEST_SIZE_LIMIT:
        logger.warning(f"[{request_id}] OVERSIZE: {len(payload)} bytes > {_GUEST_SIZE_LIMIT}B limit (GUEST)")
        return False

    for pattern in _BAD_PATTERNS:
        if pattern.search(payload):
            logger.error(f"[{request_id}] WAF MALICIOUS MATCH: {pattern.pattern}")
            return False

    return True


async def vip_payload_scan(payload: str, request_id: str) -> bool:
    """Light check for VIP/HQ: only size and path traversal."""
    if len(payload) > _VIP_SIZE_LIMIT:
        logger.warning(f"[{request_id}] VIP OVERSIZE: {len(payload)} bytes > {_VIP_SIZE_LIMIT}B")
        return False

    path_traversal_pattern = _BAD_PATTERNS[4] # The path traversal regex
    if path_traversal_pattern.search(payload):
        logger.error(f"[{request_id}] VIP WAF MATCH (Path Traversal): {path_traversal_pattern.pattern}")
        return False

    return True


async def inspect_cargo(request: Request, passport_status: dict) -> bool:
    """
    Inspect cargo (body) passing checkpoint.
    OSF Adds: In-Memory Rate Limiting
    """
    level = passport_status.get("level", "UNKNOWN")
    owner = passport_status.get("owner", "UNKNOWN")
    client_ip = request.client.host if request.client else "UNKNOWN_IP"
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
    endpoint = str(request.url.path)

    is_vip = level in {"VIP", "OMNICLAW_HQ", "SYSTEM_BOT"}

    # 1. OSF Rate Limiting Gate
    if not _check_rate_limit(client_ip, is_vip):
        logger.warning(f"[{request_id}] RATE LIMIT EXCEEDED | IP: {client_ip} | Level: {level}")
        raise HTTPException(status_code=429, detail="Too Many Requests. OSF Shield active.")

    # 2. Payload Inspection
    try:
        body_bytes = await request.body()
        payload_str = body_bytes.decode('utf-8', errors='replace')
    except Exception as e:
        logger.error(f"[{request_id}] DECODE ERROR from {client_ip}: {e}")
        raise HTTPException(status_code=400, detail="Payload encoding error.")

    is_safe = await (vip_payload_scan(payload_str, request_id) if is_vip
                     else strict_payload_scan(payload_str, request_id))

    if is_safe:
        logger.info(f"[{request_id}] PASS | {level} | {owner} | {client_ip} | {endpoint} | {len(payload_str)}B")
    else:
        logger.critical(f"[{request_id}] BLOCK | {level} | {owner} | {client_ip} | {endpoint}")
        detail = ("Payload oversize or VIP standard violation."
                  if is_vip else "Malicious / Sabotage from unknown guest. OSF DROP.")
        raise HTTPException(status_code=403, detail=detail)

    return True


def validate_platform(platform: str) -> str:
    """Validate bot platform name."""
    normalized = platform.lower().strip()
    if normalized not in _VALID_PLATFORMS:
        raise HTTPException(
            status_code=400,
            detail=f"Platform '{platform}' not supported. Supported: {sorted(_VALID_PLATFORMS)}"
        )
    return normalized
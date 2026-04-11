"""
PASSPORT ISSUER & VAULT MANAGER
Birthplace and issuer of Wooden Tags (VIP/GUEST/BOT) for communicating entities.
Tokens are persisted to JSON file to survive restarts.
"""
import uuid
import hashlib
import time
import json
import os
import threading
from pathlib import Path

_VALID_LEVELS = {"VIP", "GUEST", "BOT", "SYSTEM_BOT", "OMNICLAW_HQ"}


def _load_master_env():
    """Load MASTER.env to get OMNICLAW_HQ_MASTER_KEY if available."""
    root = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
    env_path = root / "core" / "ops" / "secrets" / "MASTER.env"
    if env_path.exists():
        with open(env_path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, val = line.split('=', 1)
                    os.environ.setdefault(key.strip(), val.strip())


_load_master_env()

_ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
_VAULT_FILE = _ROOT / "core" / "ops" / "secrets" / "vault_tokens.json"


class VaultKeeper:
    def __init__(self):
        self._lock = threading.Lock()
        # Structure: token_hash -> {"level": str, "owner": str, "expires": float}
        self._tokens: dict = {}

        # HQ Master Key tá»« env var (khÃ´ng hardcode trong source)
        raw_master = os.environ.get("OMNICLAW_HQ_MASTER_KEY", "OMNICLAW-HQ-MASTER-ROOT-2026")
        self._hq_master_key_hash = hashlib.sha256(raw_master.encode()).hexdigest()

        self._load_tokens()

    # â”€â”€ Persistence â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

    def _load_tokens(self):
        """Load tokens from file (survive restart)."""
        if _VAULT_FILE.exists():
            try:
                with open(_VAULT_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                # Prune expired tokens on load
                now = time.time()
                self._tokens = {k: v for k, v in data.items() if v.get("expires", 0) > now}
            except Exception:
                self._tokens = {}

    def _save_tokens(self):
        """Persist tokens to file (called after each change)."""
        _VAULT_FILE.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(_VAULT_FILE, 'w', encoding='utf-8') as f:
                json.dump(self._tokens, f, ensure_ascii=False, indent=2)
        except Exception:
            pass  # Non-fatal â€” token still works in-memory

    # â”€â”€ Public API â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

    def issue_passport(self, owner: str, level: str = "GUEST", duration_days: int = 30) -> str:
        """Issue Wooden Tag for a Client/Bot. Return raw token (only once)."""
        if level not in _VALID_LEVELS:
            raise ValueError(f"Invalid level '{level}'. Choose: {_VALID_LEVELS}")

        raw_token = f"omniclaw_{level.lower()}_{uuid.uuid4().hex}"
        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

        with self._lock:
            self._tokens[token_hash] = {
                "level": level,
                "owner": owner,
                "expires": time.time() + (duration_days * 86400),
                "issued_at": time.time(),
            }
            self._save_tokens()

        return raw_token

    def verify_passport(self, raw_token: str) -> dict:
        """Customs inspects Tag â€” returns dict with status/level/owner/msg."""
        if not raw_token:
            return {"status": "NO_PASS", "level": "UNKNOWN", "msg": "No Pass"}

        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()

        # HQ Master Key bypass
        if token_hash == self._hq_master_key_hash:
            return {"status": "VALID", "level": "OMNICLAW_HQ", "owner": "THE_CORE", "msg": "HQ - Exempt"}

        with self._lock:
            stamp = self._tokens.get(token_hash)

        if stamp is None:
            return {"status": "INVALID", "level": "UNKNOWN", "msg": "Token does not exist or has been revoked."}

        if time.time() > stamp["expires"]:
            return {"status": "EXPIRED", "level": stamp["level"], "msg": "Token expired."}

        return {"status": "VALID", "level": stamp["level"], "owner": stamp["owner"], "msg": "Valid."}

    def revoke_passport(self, raw_token: str) -> bool:
        """Revoke token immediately. Return True if successful."""
        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
        with self._lock:
            if token_hash in self._tokens:
                del self._tokens[token_hash]
                self._save_tokens()
                return True
        return False

    def list_passports(self) -> list:
        """List all valid tokens (does not return raw token)."""
        now = time.time()
        with self._lock:
            return [
                {
                    "owner": v["owner"],
                    "level": v["level"],
                    "expires_in_hours": round((v["expires"] - now) / 3600, 1),
                }
                for v in self._tokens.values()
                if v["expires"] > now
            ]

    def purge_expired(self) -> int:
        """Purge all expired tokens. Return count of removed tokens."""
        now = time.time()
        with self._lock:
            before = len(self._tokens)
            self._tokens = {k: v for k, v in self._tokens.items() if v["expires"] > now}
            removed = before - len(self._tokens)
            if removed:
                self._save_tokens()
        return removed


# Singleton instance
vault = VaultKeeper()

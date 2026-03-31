"""
PASSPORT ISSUER & VAULT MANAGER
Nơi sinh ra và cấp phát Thẻ Mộc (VIP) và Passport cho các thành phần giao tiếp.
"""
import uuid
import hashlib
import time
import os
from pathlib import Path

def _load_master_env():
    """Load MASTER.env để lấy OMNICLAW_HQ_MASTER_KEY nếu có."""
    root = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
    env_path = root / "system" / "ops" / "secrets" / "MASTER.env"
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

class VaultKeeper:
    def __init__(self):
        # Database giả lập lưu các Ticket/Token đã đúc
        # Structure: token_hash -> {"level": "VIP"|"GUEST", "owner": "...", "expires": float}
        self._tokens = {}
        
        # OmniClaw HQ Master Key — load từ OMNICLAW_HQ_MASTER_KEY trong MASTER.env
        # Fallback về giá trị mặc định nếu chưa config (cần đổi trong production)
        raw_master = os.environ.get("OMNICLAW_HQ_MASTER_KEY", "OMNICLAW-HQ-MASTER-ROOT-2026")
        self._hq_master_key_hash = hashlib.sha256(raw_master.encode()).hexdigest()

    def issue_passport(self, owner: str, level: str = "GUEST", duration_days: int = 30) -> str:
        """Cấp Thẻ Mộc hoặc Passport cho một Client/Bot."""
        raw_token = f"omniclaw_{level.lower()}_{uuid.uuid4().hex}"
        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
        
        self._tokens[token_hash] = {
            "level": level,       # VIP, GUEST, BOT
            "owner": owner,
            "expires": time.time() + (duration_days * 86400)
        }
        return raw_token # Chỉ trả raw 1 lần duy nhất

    def verify_passport(self, raw_token: str) -> dict:
        """Hải quan dùng hàm này để soi Thẻ."""
        if not raw_token:
            return {"status": "NO_PASS", "level": "UNKNOWN", "msg": "Khách vãng lai / Không có Pass"}

        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
        
        # Soi hàng của HQ
        if token_hash == self._hq_master_key_hash:
            return {"status": "VALID", "level": "OMNICLAW_HQ", "owner": "THE_CORE", "msg": "Tuyệt mật - Miễn kiểm siêu tốc"}

        if token_hash not in self._tokens:
            return {"status": "INVALID", "level": "UNKNOWN", "msg": "Thẻ giả hoặc mộc giả."}

        stamp = self._tokens[token_hash]
        if time.time() > stamp["expires"]:
            return {"status": "EXPIRED", "level": stamp["level"], "msg": "Thẻ đã hết hạn."}
            
        return {"status": "VALID", "level": stamp["level"], "owner": stamp["owner"], "msg": "Hợp lệ."}

# Khởi tạo Lão giữ kho (Singlton instance cho bộ nhớ Cảng)
vault = VaultKeeper()

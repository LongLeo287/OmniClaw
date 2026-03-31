"""
PASSPORT ISSUER & VAULT MANAGER
Nơi sinh ra và cấp phát Thẻ Mộc (VIP) và Passport cho các thành phần giao tiếp.
"""
import uuid
import hashlib
import time

class VaultKeeper:
    def __init__(self):
        # Database giả lập lưu các Ticket/Token đã đúc
        # Structure: token_hash -> {"level": "VIP"|"GUEST", "owner": "...", "expires": float}
        self._tokens = {}
        
        # Hardcode OmniClaw HQ Master Key (Thượng phương bảo kiếm)
        # Chỉ Admin nội bộ mới sở hữu key này
        self._hq_master_key_hash = hashlib.sha256(b"OMNICLAW-HQ-MASTER-ROOT-2026").hexdigest()

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

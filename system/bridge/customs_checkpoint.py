"""
CUSTOMS CHECKPOINT (TRẠM KIỂM SOÁT HẢI QUAN)
Áp dụng Luật Thép từ CEO: "Ai có thẻ sẽ đi dễ hơn nhưng VẪN BỊ KIỂM TRA. Chưa có thẻ thì kiểm tra gắt gao".
ĐƯỢC GẮN CAMERA GIÁM SÁT: Luôn report (ghi log) khi có biến.
"""
from fastapi import Request, HTTPException
import json
import logging
import os

# Thiết lập hệ thống Báo động (Telemetry)
LOG_DIR = r"d:\LongLeo\AI OS CORP\AI OS\system\ops\telemetry\logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("BorderSecurity")
logger.setLevel(logging.WARNING)
if not logger.handlers:
    fh = logging.FileHandler(os.path.join(LOG_DIR, "border_security.log"), encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

async def strict_payload_scan(payload: str) -> bool:
    """Kiểm tra khắt khe từng byte mã độc, prompt injection, DDoS..."""
    bad_keywords = ["DROP TABLE", "<script>", "/bin/bash", "sudo rm", "ignore all previous instructions"]
    for kw in bad_keywords:
        if kw.lower() in payload.lower():
            logger.error(f"🚨 CƯỚP BIỂN (MÃ ĐỘC): Phát hiện từ khóa '{kw}' trong khoang hàng.")
            return False
            
    if len(payload) > 10240:
        logger.warning(f"🚨 TẢI TRỌNG LẠ: Vượt 10KB (Khách Lạ). Kích thước: {len(payload)} bytes.")
        return False
        
    return True

async def vip_payload_scan(payload: str) -> bool:
    """Xét duyệt nhanh gọn (Log lưu vết nhưng không soi từng ngóc ngách)"""
    if len(payload) > 52428800: # 50MB
        logger.warning(f"🚨 TẢI TRỌNG VIP QUÁ KHỔ: Vượt 50MB. Kích thước: {len(payload)} bytes.")
        return False
    return True

async def inspect_cargo(request: Request, passport_status: dict):
    """Tiến hành kiểm duyệt hàng hóa (Body Request) khi qua trạm."""
    
    level = passport_status.get("level", "UNKNOWN")
    client_ip = request.client.host if request.client else "UNKNOWN_IP"
    
    try:
        body_bytes = await request.body()
        payload_str = body_bytes.decode('utf-8')
    except Exception:
        logger.error(f"❌ CUSTOMS ERROR: Lỗi định dạng gói hàng từ IP {client_ip}")
        raise HTTPException(status_code=400, detail="Customs Error: Hàng hóa (Payload) bọc sai quy cách.")

    if level in ["VIP", "OMNICLAW_HQ", "SYSTEM_BOT"]:
        is_safe = await vip_payload_scan(payload_str)
        if not is_safe:
            raise HTTPException(status_code=403, detail="Customs Error: Khối hàng cực tiêu hoặc vi phạm chuẩn VIP.")
    else:
        is_safe = await strict_payload_scan(payload_str)
        if not is_safe:
            # Ghi danh sách đen vào sổ
            logger.critical(f"🛑 BÁO ĐỘNG ĐỎ: Đuổi cổ IP {client_ip} vì nghi ngờ phá hoại (No_Pass/GUEST).")
            raise HTTPException(status_code=403, detail="Customs Alert: Báo động mã độc / Phá hoại từ khách lạ. Lệnh DROP ngay lập tức.")
            
    return True

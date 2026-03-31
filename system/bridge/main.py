"""
OMNICLAW REMOTE BRIDGE - API GATEWAY
Trạm Gác Cửa Khẩu (Massive Port) đón mọi lưu lượng từ OmniClaw Remote.
Hierarchy: OmniClaw HQ (Lõi) > Bridge Gateway.
"""

from fastapi import FastAPI, Request, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from passport_issuer import vault
from customs_checkpoint import inspect_cargo

app = FastAPI(
    title="OmniClaw Remote Bridge",
    description="Siêu Bến Cảng Local đón/xử lý requests từ OmniClaw Remote và External Bots.",
    version="1.0.0"
)

# CORS Policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Yêu cầu siết lại VPN CIDR ở Production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY_NAME = "X-OMNICLAW-HQ-TOKEN"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def check_passport(request: Request, api_key: str = Security(api_key_header)) -> dict:
    """Hải Quan kiểm tra Hộ chiếu/Thẻ Mộc P2A."""
    from customs_checkpoint import logger # Import chung cái còi báo động
    
    status = vault.verify_passport(api_key)
    if status["status"] in ["INVALID", "EXPIRED"]:
        client_ip = request.client.host if request.client else "UNKNOWN_IP"
        logger.warning(f"🚫 THẺ GIẢ / HẾT HẠN: Chặn kẻ mạo danh từ IP {client_ip} - Lý do: {status['msg']}")
        raise HTTPException(status_code=403, detail=f"Hải quan chặn: {status['msg']}")
    return status

# =========================================================================
# PHÂN KHU 1: BOT DOCK (Zalo, Telegram, Facebook, Discord)
# =========================================================================
@app.post("/dock/bots/{platform}")
async def bot_webhook_receiver(platform: str, request: Request, passport: dict = Security(check_passport)):
    """Rốn nhận tín hiệu các platform Social Bot do OmniClaw Remote đẩy về."""
    await inspect_cargo(request, passport_status=passport) # Trạm Kiểm Dịch
    try:
        payload = await request.json()
    except Exception:
         raise HTTPException(status_code=400, detail="Hải Quan: Lỗi bung gói hàng JSON")
    
    # bridge-commander-agent sẽ triệu hồi Agent Lõi để reply Bot tương ứng
    return {"status": "CLEARED_CUSTOMS", "target": f"bot_handler_{platform}", "lane": passport["level"]}

# =========================================================================
# PHÂN KHU 2: AGENTIC AI & MCP (OpenClaw, Third-party Agents, MCP Tools)
# =========================================================================
@app.post("/dock/mcp/dispatch")
async def mcp_server_gateway(request: Request, passport: dict = Security(check_passport)):
    """Cổng dành riêng cho các Tool Agents bên ngoài gọi vào MCP Local."""
    await inspect_cargo(request, passport_status=passport)
    return {"status": "CLEARED_CUSTOMS", "target": "local_mcp_event_bus"}

@app.post("/dock/agentic_ai/sync")
async def openclaw_sync(request: Request, passport: dict = Security(check_passport)):
    """Cảng đồng bộ hóa nhận thức giữa Local và OpenClaw (Remote AI)."""
    await inspect_cargo(request, passport_status=passport)
    return {"status": "SYNC_AUTHORIZED"}

# =========================================================================
# PHÂN KHU 3: CLOUD & DASHBOARD (Supabase, Google Cloud, Mobile App)
# =========================================================================
@app.post("/dock/cloud/webhook")
async def cloud_webhook_sync(request: Request, passport: dict = Security(check_passport)):
    """Tiếp nhận update Database từ Supabase & GCloud bắn về Local."""
    await inspect_cargo(request, passport_status=passport)
    return {"status": "DATABASE_SYNC_QUEUED"}

@app.post("/dock/dashboard/ui_command")
async def master_dashboard_command(request: Request, passport: dict = Security(check_passport)):
    """Nhận tín hiệu Controller từ giao diện Web/Mobile Quản Trị."""
    await inspect_cargo(request, passport_status=passport)
    return {"status": "HQ_COMMAND_DISPATCHED"}

# =========================================================================
# PHÂN KHU 4: VAULT KEEPING (Quản lý P2A, Master Account, Keys)
# =========================================================================
@app.get("/vault/auth/issue_temp_pass")
async def issue_p2a_token(master_key: str = Security(api_key_header)):
    """Endpoint cấp phát thẻ P2A tạm thời (Yêu cầu Master Key Local)."""
    # Soi Master Key
    if vault.verify_passport(master_key).get("level") != "OMNICLAW_HQ":
         raise HTTPException(status_code=403, detail="Chỉ OmniClaw Lõi mới được đúc thẻ mới.")
    
    new_pass = vault.issue_passport(owner="Remote_Slave", level="GUEST", duration_days=1)
    return {"issued_pass": new_pass, "valid_for_days": 1}

# =========================================================================
# PORT HEALTH
# =========================================================================
@app.get("/health")
async def harbor_health_check():
    """Ping xem Cảng có hoạt động không."""
    return {"status": "PORT_OPEN", "commander": "bridge-commander-agent", "terminals": 5}

if __name__ == "__main__":
    import uvicorn
    # Khai mở bến cảng ở Local 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)


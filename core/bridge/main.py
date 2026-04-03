"""
OMNICLAW REMOTE BRIDGE - API GATEWAY
Border Patrol Checkpoint receives all traffic from OmniClaw Remote.
Dispatch thực sự tới agent_bus (SQLite pub/sub) + blackboard.json.

Endpoints:
  POST /dock/bots/{platform}      — Social bot webhooks
  POST /dock/mcp/dispatch         — MCP tool agent calls
  POST /dock/agentic_ai/sync      — OmniClaw AI sync
  POST /dock/cloud/webhook        — Supabase / GCloud updates
  POST /dock/dashboard/ui_command — Web/Mobile UI commands
  POST /vault/auth/issue_temp_pass — Issue temp token (HQ key required)
  POST /vault/auth/revoke         — Revoke token
  GET  /vault/auth/list           — List valid tokens (HQ only)
  GET  /health                    — Health check
"""

from __future__ import annotations

import json
import logging
import os
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, Request, HTTPException, Security, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader

from .passport_issuer import vault
from .customs_checkpoint import inspect_cargo, validate_platform

# ── Config ─────────────────────────────────────────────────────────────────────
_ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[2])))
_BLACKBOARD = _ROOT / "brain" / "shared-context" / "blackboard.json"
_BRIDGE_LOG = _ROOT / "system" / "ops" / "telemetry" / "logs" / "bridge_gateway.log"
_BRIDGE_LOG.parent.mkdir(parents=True, exist_ok=True)

# CORS: read from env var, fallback wildcard for dev
_ALLOWED_ORIGINS = os.environ.get("BRIDGE_ALLOWED_ORIGINS", "*").split(",")

# ── Logging ────────────────────────────────────────────────────────────────────
gw_logger = logging.getLogger("BridgeGateway")
gw_logger.setLevel(logging.INFO)
if not gw_logger.handlers:
    fh = logging.FileHandler(_BRIDGE_LOG, encoding='utf-8')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    gw_logger.addHandler(fh)

# ── Agent Bus (graceful fallback nếu chưa init) ────────────────────────────────
_agent_bus = None
try:
    import sys
    if str(_ROOT) not in sys.path:
        sys.path.insert(0, str(_ROOT))
    from core.ops.scripts.agent_bus import AgentBus
    _agent_bus = AgentBus()
    gw_logger.info("AgentBus connected.")
except Exception as _e:
    gw_logger.warning(f"AgentBus unavailable — using blackboard fallback. ({_e})")


def _publish_event(topic: str, payload: dict) -> Optional[int]:
    """Fire event to AgentBus if available, fallback write to blackboard.json."""
    if _agent_bus:
        try:
            return _agent_bus.publish(topic, payload)
        except Exception as e:
            gw_logger.error(f"AgentBus publish failed: {e}")

    # Blackboard fallback — append to inbound_queue list
    try:
        bb: dict = {}
        if _BLACKBOARD.exists():
            bb = json.loads(_BLACKBOARD.read_text(encoding='utf-8-sig'))
        queue = bb.setdefault("inbound_queue", [])
        queue.append({"topic": topic, "payload": payload,
                      "ts": datetime.utcnow().isoformat()})
        _BLACKBOARD.write_text(json.dumps(bb, ensure_ascii=False, indent=2), encoding='utf-8')
    except Exception as e:
        gw_logger.error(f"Blackboard fallback failed: {e}")
    return None


# ── Lifespan ───────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    gw_logger.info("OmniClaw Bridge Gateway starting on port 8000.")
    expired = vault.purge_expired()
    if expired:
        gw_logger.info(f"Purged {expired} expired token(s) on startup.")
    yield
    gw_logger.info("OmniClaw Bridge Gateway shutting down.")


# ── App ────────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="OmniClaw Remote Bridge",
    description="Local Super Harbor receiving/processing requests from OmniClaw Remote and External Bots.",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Auth ───────────────────────────────────────────────────────────────────────
API_KEY_NAME = "X-OMNICLAW-HQ-TOKEN"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def check_passport(request: Request, api_key: str = Security(api_key_header)) -> dict:
    """Check Passport / P2A Wooden Tag."""
    from .customs_checkpoint import logger as border_logger

    status = vault.verify_passport(api_key)
    if status["status"] in ("INVALID", "EXPIRED", "NO_PASS"):
        client_ip = request.client.host if request.client else "UNKNOWN"
        border_logger.warning(f"BLOCKED {client_ip}: {status['msg']}")
        raise HTTPException(status_code=403, detail=f"Customs blocked: {status['msg']}")
    return status


# ── Middleware: inject X-Request-ID ───────────────────────────────────────────
@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    req_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())[:12]
    request.state.request_id = req_id
    response: Response = await call_next(request)
    response.headers["X-Request-ID"] = req_id
    return response


# ── PHÂN KHU 1: BOT DOCK ──────────────────────────────────────────────────────
@app.post("/dock/bots/{platform}")
async def bot_webhook_receiver(
    platform: str,
    request: Request,
    passport: dict = Security(check_passport),
):
    """Receive webhook from Social Bots (Zalo/Telegram/Facebook/Discord/Line)."""
    platform = validate_platform(platform)
    await inspect_cargo(request, passport_status=passport)

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Error parse JSON body.")

    event_id = _publish_event(
        topic=f"bot.inbound.{platform}",
        payload={
            "platform": platform,
            "data": payload,
            "passport_level": passport["level"],
            "request_id": request.state.request_id,
        },
    )

    gw_logger.info(f"Bot webhook [{platform}] queued. event_id={event_id} req={request.state.request_id}")
    return {
        "status": "CLEARED_CUSTOMS",
        "platform": platform,
        "event_id": event_id,
        "lane": passport["level"],
    }


# ── PHÂN KHU 2: AGENTIC AI & MCP ─────────────────────────────────────────────
@app.post("/dock/mcp/dispatch")
async def mcp_server_gateway(
    request: Request,
    passport: dict = Security(check_passport),
):
    """Port for external Tool Agents calling into Local MCP."""
    await inspect_cargo(request, passport_status=passport)

    try:
        payload = await request.json()
    except Exception:
        payload = {}

    event_id = _publish_event(
        topic="mcp.dispatch",
        payload={
            "data": payload,
            "passport_level": passport["level"],
            "request_id": request.state.request_id,
        },
    )

    return {"status": "CLEARED_CUSTOMS", "target": "local_mcp_event_bus", "event_id": event_id}


@app.post("/dock/agentic_ai/sync")
async def openclaw_sync(
    request: Request,
    passport: dict = Security(check_passport),
):
    """Synchronize context between Local and OmniClaw (Remote AI)."""
    await inspect_cargo(request, passport_status=passport)

    try:
        payload = await request.json()
    except Exception:
        payload = {}

    event_id = _publish_event(
        topic="agentic_ai.sync",
        payload={
            "data": payload,
            "passport_level": passport["level"],
            "request_id": request.state.request_id,
        },
    )

    return {"status": "SYNC_AUTHORIZED", "event_id": event_id}


# ── PHÂN KHU 3: CLOUD & DASHBOARD ────────────────────────────────────────────
@app.post("/dock/cloud/webhook")
async def cloud_webhook_sync(
    request: Request,
    passport: dict = Security(check_passport),
):
    """Receive Database update from Supabase/GCloud."""
    await inspect_cargo(request, passport_status=passport)

    try:
        payload = await request.json()
    except Exception:
        payload = {}

    event_id = _publish_event(
        topic="cloud.webhook",
        payload={
            "data": payload,
            "passport_level": passport["level"],
            "request_id": request.state.request_id,
        },
    )

    return {"status": "DATABASE_SYNC_QUEUED", "event_id": event_id}


@app.post("/dock/dashboard/ui_command")
async def master_dashboard_command(
    request: Request,
    passport: dict = Security(check_passport),
):
    """Receive Controller signal from Web/Mobile UI."""
    await inspect_cargo(request, passport_status=passport)

    try:
        payload = await request.json()
    except Exception:
        payload = {}

    event_id = _publish_event(
        topic="dashboard.ui_command",
        payload={
            "data": payload,
            "passport_level": passport["level"],
            "request_id": request.state.request_id,
        },
    )

    return {"status": "HQ_COMMAND_DISPATCHED", "event_id": event_id}


# ── PHÂN KHU 4: VAULT KEEPING ────────────────────────────────────────────────
@app.post("/vault/auth/issue_temp_pass")
async def issue_p2a_token(
    request: Request,
    master_key: str = Security(api_key_header),
):
    """Issue temporary P2A token (requires Master Key)."""
    status = vault.verify_passport(master_key)
    if status.get("level") != "OMNICLAW_HQ":
        raise HTTPException(status_code=403, detail="Only OmniClaw Core can mint new tokens.")

    try:
        body = await request.json()
    except Exception:
        body = {}

    owner = body.get("owner", "Remote_Slave")
    level = body.get("level", "GUEST")
    duration = int(body.get("duration_days", 1))

    try:
        new_pass = vault.issue_passport(owner=owner, level=level, duration_days=duration)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    gw_logger.info(f"Token issued: owner={owner} level={level} days={duration}")
    return {"issued_pass": new_pass, "owner": owner, "level": level, "valid_for_days": duration}


@app.post("/vault/auth/revoke")
async def revoke_token(
    request: Request,
    passport: dict = Security(check_passport),
):
    """Revoke a token. Only OMNICLAW_HQ can revoke others' tokens."""
    if passport.get("level") != "OMNICLAW_HQ":
        raise HTTPException(status_code=403, detail="Only OMNICLAW_HQ can revoke tokens.")

    try:
        body = await request.json()
        token_to_revoke = body.get("token")
    except Exception:
        token_to_revoke = None

    if not token_to_revoke:
        raise HTTPException(status_code=400, detail="Missing 'token' field in body.")

    revoked = vault.revoke_passport(token_to_revoke)
    gw_logger.info(f"Token revoke: {'SUCCESS' if revoked else 'NOT_FOUND'} by {passport.get('owner')}")
    return {"status": "REVOKED" if revoked else "NOT_FOUND"}


@app.get("/vault/auth/list")
async def list_tokens(passport: dict = Security(check_passport)):
    """List valid tokens (OMNICLAW_HQ only)."""
    if passport.get("level") != "OMNICLAW_HQ":
        raise HTTPException(status_code=403, detail="OMNICLAW_HQ only.")
    return {"tokens": vault.list_passports()}


# ── HEALTH ─────────────────────────────────────────────────────────────────────
@app.get("/health")
async def harbor_health_check():
    """Ping to see if Harbor is active."""
    return {
        "status": "PORT_OPEN",
        "version": "2.0.0",
        "agent_bus": "connected" if _agent_bus else "fallback_blackboard",
        "commander": "bridge-commander-agent",
        "terminals": {
            "bot_dock": "/dock/bots/{platform}",
            "mcp_dispatch": "/dock/mcp/dispatch",
            "agentic_ai": "/dock/agentic_ai/sync",
            "cloud": "/dock/cloud/webhook",
            "dashboard": "/dock/dashboard/ui_command",
        },
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
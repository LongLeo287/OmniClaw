"""
oid/triage.py — OID Security Gate & Classification Engine
Owner: strix-agent + knowledge_navigator (Dept: Security GRC + Knowledge)
Role: Phase 2-3 of OID pipeline.
    1. Security scan — blocks malicious/suspicious sources (Strix Gate)
    2. Deduplication check — rejects already-known sources
    3. Domain classification + scoring — routes to ACCEPTED/PENDING/REJECTED

STRICT RULE: 100% English only. No other language in code, comments, or output.
"""

import hashlib
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Tuple, Dict, Any
import os

OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[4])
STATE_DIR = Path(OMNICLAW_ROOT) / "storage" / "vault" / "OID_STATE"
PROCESSED_DB = STATE_DIR / "processed_hashes.json"

# ── Strix: Known bad patterns ─────────────────────────────────────────────────
MALICIOUS_PATTERNS = [
    r"prompt[_\-]?leak", r"jailbreak", r"bypass[_\-]?filter",
    r"malware", r"rat\b", r"keylogger", r"xpfarm", r"phish",
    r"credential[_\-]?dump", r"exploit[_\-]?kit",
]

# ── Navigator: Domain keyword mapping ─────────────────────────────────────────
DOMAIN_MAP = {
    "ai_ml":       ["llm", "rag", "embedding", "agent", "model", "transformer", "fine-tun"],
    "backend":     ["fastapi", "django", "flask", "express", "api", "rest", "graphql", "python", "node"],
    "frontend":    ["react", "vue", "nextjs", "svelte", "html", "css", "tailwind", "ui", "ux"],
    "devops":      ["docker", "kubernetes", "k8s", "ci/cd", "terraform", "ansible", "github-action"],
    "cybersecurity": ["cve", "pentest", "owasp", "security", "firewall", "siem", "vuln"],
    "data":        ["pandas", "spark", "database", "sql", "etl", "pipeline", "warehouse"],
    "mobile":      ["android", "ios", "react-native", "flutter", "swift", "kotlin"],
    "knowledge":   ["memory", "knowledge", "graph", "ontology", "lightrag", "vector", "qdrant"],
}


def _log(msg: str):
    ts = datetime.now().strftime('%H:%M:%S')
    print(f"[{ts}] [strix-agent / navigator] {msg}")


# ── Deduplication ─────────────────────────────────────────────────────────────

def _load_processed_db() -> Dict[str, Any]:
    if not PROCESSED_DB.exists():
        return {}
    try:
        return json.loads(PROCESSED_DB.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_processed_db(db: Dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DB.write_text(json.dumps(db, indent=2), encoding="utf-8")


def is_duplicate(source: str) -> bool:
    """Return True if source has already been processed (hash match)."""
    db = _load_processed_db()
    key = hashlib.md5(source.strip().lower().encode()).hexdigest()
    return key in db


def mark_as_processed(source: str, ticket_id: str) -> None:
    """Record source hash in the processed DB to prevent future duplicates."""
    db = _load_processed_db()
    key = hashlib.md5(source.strip().lower().encode()).hexdigest()
    db[key] = {"ticket_id": ticket_id, "processed_at": datetime.now().isoformat()}
    _save_processed_db(db)


# ── Strix Security Gate ───────────────────────────────────────────────────────

def security_scan(source: str) -> Tuple[bool, str]:
    """
    Strix-agent security check: scan source URL/path for malicious patterns.

    Returns:
        (passed: bool, reason: str)
    """
    src_lower = source.lower()
    for pattern in MALICIOUS_PATTERNS:
        if re.search(pattern, src_lower):
            reason = f"Blocked by Strix gate — matched threat pattern: '{pattern}'"
            _log(f"[SECURITY_FAIL] {reason}")
            return False, reason
    _log(f"[SECURITY_PASS] Source cleared: {source[:80]}")
    return True, "Clean — no threat patterns detected"


# ── Navigator: Domain Classification & Scoring ───────────────────────────────

def classify_and_score(source: str, content_snippet: str = "") -> Dict[str, Any]:
    """
    knowledge_navigator: classify domain and generate a quality confidence score.

    Args:
        source:          Original URL or file path.
        content_snippet: First 2000 chars of scraped content for domain hints.

    Returns:
        {
            "domain": str,
            "confidence": float,   # 0.0 – 1.0
            "verdict":   str,       # ACCEPTED | PENDING | REJECTED
            "reason":    str
        }
    """
    text = (source + " " + content_snippet).lower()
    scores: Dict[str, int] = {}

    for domain, keywords in DOMAIN_MAP.items():
        hits = sum(1 for kw in keywords if kw in text)
        if hits:
            scores[domain] = hits

    if not scores:
        return {
            "domain": "general",
            "confidence": 0.3,
            "verdict": "PENDING",
            "reason": "No domain keywords matched — escalate to CEO for routing"
        }

    best_domain = max(scores, key=scores.__getitem__)
    total_keywords = len(DOMAIN_MAP[best_domain])
    confidence = min(scores[best_domain] / max(total_keywords * 0.5, 1), 1.0)

    if confidence >= 0.7:
        verdict = "ACCEPTED"
        reason = f"High confidence match ({confidence:.0%}) for domain: {best_domain}"
    elif confidence >= 0.4:
        verdict = "PENDING"
        reason = f"Moderate confidence ({confidence:.0%}) — CEO review recommended"
    else:
        verdict = "PENDING"
        reason = f"Low confidence ({confidence:.0%}) — insufficient domain signal"

    _log(f"[CLASSIFY] domain={best_domain} confidence={confidence:.0%} verdict={verdict}")

    return {
        "domain": best_domain,
        "confidence": round(confidence, 2),
        "verdict": verdict,
        "reason": reason
    }


# ── Combined Triage Entry Point ───────────────────────────────────────────────

def triage(source: str, ticket_id: str, content_snippet: str = "") -> Dict[str, Any]:
    """
    Full triage run for a single intake source.
    Runs: dedup → security scan → domain classification.

    Returns triage result dict with final verdict.
    """
    # Step 0: Deduplication
    if is_duplicate(source):
        _log(f"[DEDUP] Source already processed — skipping: {source[:80]}")
        return {
            "domain": "N/A",
            "confidence": 1.0,
            "verdict": "REJECTED",
            "reason": "Duplicate — source already exists in processed knowledge base"
        }

    # Step 1: Strix Security Gate
    passed, sec_reason = security_scan(source)
    if not passed:
        return {
            "domain": "N/A",
            "confidence": 0.0,
            "verdict": "REJECTED",
            "reason": sec_reason
        }

    # Step 2: Domain Classification
    result = classify_and_score(source, content_snippet)

    return result

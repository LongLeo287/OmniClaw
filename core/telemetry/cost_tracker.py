#!/usr/bin/env python3
"""
[OER] Core Cost Tracker
======================================================
Mission: 
  1. Parse telemetry receipts across the ecosystem.
  2. Map token usage to USD fixed pricing (Pillar 1).
  3. Generate alerts for anomalies and baseline breaches.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
RECEIPTS_DIR = REPO_ROOT / "core" / "telemetry" / "receipts"
SUMMARY_PATH = REPO_ROOT / "core" / "telemetry" / "logs" / "cost_tracker_summary.json"
DEFAULT_BASELINE_USD = 0.50
DEFAULT_TOKEN_ALERT = 200_000

# Fixed pricing table in USD / 1M tokens.
MODEL_PRICING_USD_PER_1M: dict[str, tuple[float, float]] = {
    "gpt-4o": (5.00, 15.00),
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4.1": (2.00, 8.00),
    "gpt-4.1-mini": (0.40, 1.60),
    "gpt-5": (1.25, 10.00),
    "gpt-5-mini": (0.25, 2.00),
    "claude-3-5-sonnet": (3.00, 15.00),
    "claude-3-7-sonnet": (3.00, 15.00),
    "claude-sonnet-4": (3.00, 15.00),
    "gemini-2.0-flash": (0.10, 0.40),
    "gemini-2.5-pro": (1.25, 10.00),
    "deepseek-chat": (0.27, 1.10),
    "deepseek-reasoner": (0.55, 2.19),
    "qwen2.5-coder": (0.20, 0.80),
    "default": (0.50, 1.50),
}

KEY_ALIASES = {
    "agent": {"agent", "agent_id", "worker", "owner", "picked_by"},
    "project": {"project", "project_name", "project_id", "task_id", "ticket"},
    "model": {"model", "model_name", "model_id", "llm", "provider_model"},
    "input_tokens": {"input_tokens", "prompt_tokens", "input_token", "prompt_token"},
    "output_tokens": {"output_tokens", "completion_tokens", "output_token", "completion_token"},
    "total_tokens": {"total_tokens", "tokens"},
    "timestamp": {"timestamp", "created_at", "time", "date"},
}

LINE_PATTERNS = {
    "agent": re.compile(r"(?im)^(?:agent|owner)\s*[:=]\s*(.+)$"),
    "project": re.compile(r"(?im)^(?:project|project_name|task_id|ticket)\s*[:=]\s*(.+)$"),
    "model": re.compile(r"(?im)^(?:model|model_name|llm)\s*[:=]\s*(.+)$"),
    "input_tokens": re.compile(r"(?im)^(?:input_tokens|prompt_tokens)\s*[:=]\s*([0-9_]+)$"),
    "output_tokens": re.compile(r"(?im)^(?:output_tokens|completion_tokens)\s*[:=]\s*([0-9_]+)$"),
    "total_tokens": re.compile(r"(?im)^(?:total_tokens|tokens)\s*[:=]\s*([0-9_]+)$"),
}


@dataclass
class NormalizedReceipt:
    source_file: str
    timestamp: str
    agent_id: str
    project_name: str
    model_name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    usd_cost: float
    warnings: list[str] = field(default_factory=list)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _safe_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        cleaned = value.replace("_", "").replace(",", "").strip()
        if cleaned.isdigit():
            return int(cleaned)
    return None


def _iter_key_values(payload: Any) -> Iterable[tuple[str, Any]]:
    if isinstance(payload, dict):
        for key, value in payload.items():
            yield key, value
            yield from _iter_key_values(value)
    elif isinstance(payload, list):
        for item in payload:
            yield from _iter_key_values(item)


def _first_matching_text(payload: Any, aliases: set[str]) -> str | None:
    for key, value in _iter_key_values(payload):
        if key in aliases and isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _sum_matching_ints(payload: Any, aliases: set[str]) -> int:
    total = 0
    for key, value in _iter_key_values(payload):
        if key in aliases:
            parsed = _safe_int(value)
            if parsed is not None:
                total += parsed
    return total


def _parse_markdown_receipt(raw_text: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {}
    for field_name, pattern in LINE_PATTERNS.items():
        match = pattern.search(raw_text)
        if not match:
            continue
        value = match.group(1).strip()
        parsed[field_name] = _safe_int(value) if "tokens" in field_name else value
    return parsed


def _load_receipt(path: Path) -> tuple[Any, list[str]]:
    warnings: list[str] = []
    if path.suffix.lower() == ".json":
        try:
            return json.loads(path.read_text(encoding="utf-8")), warnings
        except json.JSONDecodeError as exc:
            warnings.append(f"invalid_json:{exc}")
            return {}, warnings

    raw_text = path.read_text(encoding="utf-8", errors="ignore")
    warnings.append("non_json_receipt")
    return _parse_markdown_receipt(raw_text), warnings


def _canonical_model_name(raw_model: str | None) -> str:
    if not raw_model:
        return "default"
    lowered = raw_model.strip().lower()
    for known in MODEL_PRICING_USD_PER_1M:
        if known != "default" and known in lowered:
            return known
    return lowered


def _pricing_for_model(model_name: str) -> tuple[float, float]:
    if model_name in MODEL_PRICING_USD_PER_1M:
        return MODEL_PRICING_USD_PER_1M[model_name]
    return MODEL_PRICING_USD_PER_1M["default"]


def normalize_receipt(path: Path) -> NormalizedReceipt:
    payload, warnings = _load_receipt(path)
    input_tokens = _sum_matching_ints(payload, KEY_ALIASES["input_tokens"])
    output_tokens = _sum_matching_ints(payload, KEY_ALIASES["output_tokens"])
    total_tokens = _sum_matching_ints(payload, KEY_ALIASES["total_tokens"])

    if total_tokens == 0:
        total_tokens = input_tokens + output_tokens
    elif input_tokens == 0 and output_tokens == 0:
        input_tokens = total_tokens

    model_name = _canonical_model_name(_first_matching_text(payload, KEY_ALIASES["model"]))
    agent_id = _first_matching_text(payload, KEY_ALIASES["agent"]) or path.stem
    project_name = _first_matching_text(payload, KEY_ALIASES["project"]) or "unknown-project"
    timestamp = _first_matching_text(payload, KEY_ALIASES["timestamp"]) or _utc_now()

    if input_tokens == 0 and output_tokens == 0:
        warnings.append("missing_token_metrics")
    if model_name == "default":
        warnings.append("default_pricing_used")

    input_price, output_price = _pricing_for_model(model_name)
    usd_cost = round((input_tokens / 1_000_000 * input_price) + (output_tokens / 1_000_000 * output_price), 6)

    return NormalizedReceipt(
        source_file=str(path.relative_to(REPO_ROOT)),
        timestamp=timestamp,
        agent_id=agent_id,
        project_name=project_name,
        model_name=model_name,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        usd_cost=usd_cost,
        warnings=warnings,
    )


def collect_receipts(receipts_dir: Path = RECEIPTS_DIR) -> list[NormalizedReceipt]:
    receipts: list[NormalizedReceipt] = []
    for path in sorted(receipts_dir.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        if path.suffix.lower() not in {".json", ".md"}:
            continue
        receipts.append(normalize_receipt(path))
    return receipts


def _baseline_for_agent(history: list[NormalizedReceipt]) -> float:
    nonzero_costs = [receipt.usd_cost for receipt in history if receipt.usd_cost > 0]
    if not nonzero_costs:
        return DEFAULT_BASELINE_USD
    return max(DEFAULT_BASELINE_USD, sum(nonzero_costs) / len(nonzero_costs))


def build_summary(receipts: list[NormalizedReceipt]) -> dict[str, Any]:
    by_agent: dict[str, list[NormalizedReceipt]] = defaultdict(list)
    by_project: dict[str, dict[str, Any]] = defaultdict(lambda: {"usd_cost": 0.0, "tokens": 0})
    by_model: dict[str, dict[str, Any]] = defaultdict(lambda: {"usd_cost": 0.0, "tokens": 0})
    alerts: list[str] = []

    for receipt in receipts:
        by_agent[receipt.agent_id].append(receipt)
        by_project[receipt.project_name]["usd_cost"] += receipt.usd_cost
        by_project[receipt.project_name]["tokens"] += receipt.total_tokens
        by_model[receipt.model_name]["usd_cost"] += receipt.usd_cost
        by_model[receipt.model_name]["tokens"] += receipt.total_tokens

    agent_summary: dict[str, dict[str, Any]] = {}
    for agent_id, items in sorted(by_agent.items()):
        total_cost = round(sum(item.usd_cost for item in items), 6)
        total_tokens = sum(item.total_tokens for item in items)
        baseline = round(_baseline_for_agent(items), 6)
        agent_alerts: list[str] = []

        if total_cost >= baseline * 3:
            agent_alerts.append(f"ALERT: {agent_id} exceeded 3x baseline spend ({total_cost:.4f} USD vs {baseline:.4f} USD)")
        if total_tokens >= DEFAULT_TOKEN_ALERT:
            agent_alerts.append(f"ALERT: {agent_id} exceeded token baseline ({total_tokens} tokens)")

        alerts.extend(agent_alerts)
        agent_summary[agent_id] = {
            "receipt_count": len(items),
            "usd_cost": total_cost,
            "tokens": total_tokens,
            "baseline_usd": baseline,
            "alerts": agent_alerts,
        }

    return {
        "generated_at": _utc_now(),
        "receipts_scanned": len(receipts),
        "totals": {
            "usd_cost": round(sum(item.usd_cost for item in receipts), 6),
            "input_tokens": sum(item.input_tokens for item in receipts),
            "output_tokens": sum(item.output_tokens for item in receipts),
            "tokens": sum(item.total_tokens for item in receipts),
        },
        "alerts": alerts,
        "by_agent": agent_summary,
        "by_project": {name: {"usd_cost": round(data["usd_cost"], 6), "tokens": data["tokens"]} for name, data in sorted(by_project.items())},
        "by_model": {name: {"usd_cost": round(data["usd_cost"], 6), "tokens": data["tokens"]} for name, data in sorted(by_model.items())},
        "receipts": [asdict(receipt) for receipt in receipts],
    }


def write_summary(summary: dict[str, Any], output_path: Path = SUMMARY_PATH) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Aggregate telemetry receipts into fixed-price cost reports.")
    parser.add_argument("--receipts-dir", default=str(RECEIPTS_DIR), help="Directory containing receipt logs.")
    parser.add_argument("--output", default=str(SUMMARY_PATH), help="Path to write summary JSON.")
    parser.add_argument("--print-alerts", action="store_true", help="Print all generated alerts to stdout.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    receipts = collect_receipts(Path(args.receipts_dir))
    summary = build_summary(receipts)
    write_summary(summary, Path(args.output))

    if args.print_alerts:
        for alert in summary["alerts"]:
            print(alert)

    print(
        f"Cost tracker complete: {summary['receipts_scanned']} receipt(s), "
        f"{summary['totals']['tokens']} tokens, {summary['totals']['usd_cost']:.6f} USD"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add gateway_border_security department to org_chart.yaml."""
import os
import yaml
from pathlib import Path

ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
ORG_CHART = ROOT / "brain" / "corp" / "org_chart.yaml"

with open(ORG_CHART, "r", encoding="utf-8") as f:
    org = yaml.safe_load(f)

if "gateway_border_security" not in org.get("departments", {}):
    org.setdefault("departments", {})["gateway_border_security"] = {
        "head": "bridge-commander-agent",
        "workers": []
    }

with open(ORG_CHART, "w", encoding="utf-8") as f:
    yaml.dump(org, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print("Updated org_chart.yaml with gateway_border_security department.")
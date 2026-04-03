#!/usr/bin/env python3
"""
[ OA] OmniClaw Academy Auditor - Supreme Elder
=========================================================
What's the problem:
  1. final_check(): Checks the file and OA_FINAL_CHECK before delivering to OER
  2. learn_from_dumps(): How does raw data work?
  3. process_dispatch_queue(): Dispatching case resolution from OHD
  4. collect_knowledge(): How to collect knowledge from brain/ecosystem
  5. upgrade_daemon() / upgrade_skill(): Upgrade routines.
  6. propose_new_rule(): Propose modifications to Rules.

Authority: HIGHEST among the 5 Daemons.
Rule: Output must route via OER_INBOX without bypassing.
"""
import os
import json
import shutil
from datetime import datetime
from daemon_trust import authenticate_daemon, assert_write_access, abs_path, PATHS
from daemon_utils import (load_oma_map, load_fast_index, deep_scan, fast_trace,
                          find_stray_files, report_before, report_after, report_error,
                          queue_enqueue, queue_dequeue, queue_mark_success, queue_mark_failed)

DAEMON_NAME = "OA"
config = authenticate_daemon(DAEMON_NAME)

OA_WORKSHOP    = abs_path(PATHS.OA_WORKSHOP)
OA_DISPATCH    = abs_path(PATHS.OA_DISPATCH)
OA_FINAL_CHECK = abs_path(PATHS.OA_FINAL_CHECK)
OER_INBOX      = abs_path(PATHS.OER_INBOX)
RAW_DUMPS      = abs_path(PATHS.RAW_DUMPS)
KNOWLEDGE      = abs_path(PATHS.KNOWLEDGE)
RULES_PATH     = abs_path(PATHS.RULES)
HANDOFF_LOG    = abs_path(PATHS.HANDOFF_LOG)
SYSTEM_MAP     = abs_path(PATHS.SYSTEM_MAP)


def log_action(action: str, detail: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(HANDOFF_LOG), exist_ok=True)
    with open(HANDOFF_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [OA] {action} | {detail}\n")


def handoff_to_oer(filepath: str, reason: str = "approved"):
    """Transfer output from OA approval to OER_INBOX."""
    if not assert_write_access(DAEMON_NAME, OER_INBOX):
        return False
    os.makedirs(OER_INBOX, exist_ok=True)
    dest = os.path.join(OER_INBOX, os.path.basename(filepath))
    if os.path.exists(dest):
        dest = dest.replace(".md", f"_{datetime.now().strftime('%H%M%S')}.md")
    shutil.move(filepath, dest)
    print("[OmniClaw System Event]")
    log_action("HANDOFF_OER", f"Approved: {os.path.basename(filepath)} | reason={reason}")
    return True


def reject_to_quarantine(filepath: str, reason: str):
    """ [System log: Legacy non-English docstring localized] """
    fname = os.path.basename(filepath)
    import re
    m = re.match(r"^OA_REJECTED_(\d+)_", fname)
    if m:
        fail_count = int(m.group(1)) + 1
        base_name = fname[len(m.group(0)):]
    else:
        if fname.startswith("OA_REJECTED_"):
            fail_count = 2
            base_name = fname[len("OA_REJECTED_"):]
        else:
            fail_count = 1
            base_name = fname

    if fail_count >= 3:
        trash = abs_path("vault/tmp/trash")
        os.makedirs(trash, exist_ok=True)
        dest = os.path.join(trash, f"TOMBSTONE_{base_name}")
        shutil.move(filepath, dest)
        log_action("TOMBSTONE", f"File={base_name} | reason=Failed 3 times: Moved to TRASH")
        print("[OmniClaw System Event]")
        return

    quarantine = abs_path(PATHS.QUARANTINE)
    os.makedirs(quarantine, exist_ok=True)
    new_fname = f"OA_REJECTED_{fail_count}_{base_name}"
    dest = os.path.join(quarantine, new_fname)
    shutil.move(filepath, dest)
    # Note down the reason
    with open(dest + ".rejection_note.txt", "w", encoding="utf-8") as f:
        f.write(f"OA Rejection Note (Strike {fail_count})\nFile: {base_name}\nReason: {reason}\nAt: {datetime.now().isoformat()}\n")
    print("[OmniClaw System Event]")
    log_action("REJECT", f"File={new_fname} | Strike={fail_count} | reason={reason}")


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def final_check():
    """
    Check the last files of OA_FINAL_CHECK (healed by OHD).
    Approve to OER_INBOX or reject to QUARANTINE.
    """
    if not os.path.exists(OA_FINAL_CHECK):
        return

    candidates = [f for f in os.listdir(OA_FINAL_CHECK)
                  if os.path.isfile(os.path.join(OA_FINAL_CHECK, f))]
    if not candidates:
        return

    report_before(DAEMON_NAME, "FINAL_CHECK", candidates)
    oma_map = load_oma_map()
    fast_index = load_fast_index()
    indexed_ids = {e.get("id") for e in fast_index}
    results = {"success": 0, "failed": 0, "skipped": 0}

    for fname in candidates:
        fpath = os.path.join(OA_FINAL_CHECK, fname)
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(1024)

            # Check 1: Is there Frontmatter?
            if not content.startswith("---"):
                reject_to_quarantine(fpath, "Missing YAML frontmatter after OHD heal")
                results["failed"] += 1
                continue

            # Check 2: Parse ID
            file_id = None
            for line in content[3:content.find("---", 3)].strip().split("\n"):
                if line.startswith("id:"):
                    file_id = line.split(":", 1)[1].strip().strip("\"'")
                    break

            if not file_id:
                reject_to_quarantine(fpath, "ID field missing in frontmatter")
                results["failed"] += 1
                continue

            # Check 3: ID page (is it in the index?)
            if file_id in indexed_ids:
                reject_to_quarantine(fpath, f"Duplicate ID '{file_id}' already registered")
                results["failed"] += 1
                continue

            # Approve!
            handoff_to_oer(fpath, reason=f"id={file_id} passed all OA checks")
            results["success"] += 1

        except Exception as e:
            report_error(DAEMON_NAME, f"final_check {fname}", str(e))
            results["failed"] += 1

    report_after(DAEMON_NAME, "FINAL_CHECK", results)


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def process_dispatch_queue():
    """Handle judgment cases from OA_DISPATCH_QUEUE via Neural Bus."""
    msg = queue_dequeue("OA_DISPATCH_QUEUE")
    if not msg:
        return

    case = msg["payload"]
    msg_id = msg["id"]
    
    report_before(DAEMON_NAME, "DISPATCH_VERDICT", [f"Task_ID_{msg_id}"])
    results = {"success": 0, "failed": 0, "skipped": 0}

    try:
        print("[OmniClaw System Event]")
        # TODO: Implement LLM-based verdict logic
        log_action("VERDICT", f"MsgID={msg_id} | Reason={case.get('reason')}")
        queue_mark_success(msg_id)
        results["success"] += 1
    except Exception as e:
        report_error(DAEMON_NAME, f"dispatch task {msg_id}", str(e))
        queue_mark_failed(msg_id)
        results["failed"] += 1

    report_after(DAEMON_NAME, "DISPATCH_VERDICT", results)


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def learn_from_dumps():
    """ [System log: Legacy non-English docstring localized] """
    if not os.path.exists(RAW_DUMPS):
        return
    dumps = [f for f in os.listdir(RAW_DUMPS) if f.endswith(".md")]
    if not dumps:
        print("[OmniClaw System Event]")
        return

    report_before(DAEMON_NAME, "LEARN_DUMPS", dumps)
    results = {"success": 0, "failed": 0, "skipped": 0}
    for fname in dumps:
        try:
            # [System log: Legacy non-English comment removed]
            ki_draft = _create_ki_draft(fname)
            if ki_draft:
                handoff_to_oer(ki_draft, reason="KI extracted from raw dump")
                results["success"] += 1
            else:
                results["skipped"] += 1
        except Exception as e:
            report_error(DAEMON_NAME, f"learn {fname}", str(e))
            results["failed"] += 1
    report_after(DAEMON_NAME, "LEARN_DUMPS", results)


def _create_ki_draft(source_fname: str) -> str:
    """Enter the draft in OA_workshop. Use the draft file."""
    os.makedirs(OA_WORKSHOP, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = os.path.splitext(source_fname)[0][:40]
    ki_id = f"ki-{stem.lower().replace(' ', '-').replace('_', '-')}"
    draft_path = os.path.join(OA_WORKSHOP, f"KI_{stem}_{ts}.md")

    content = f"""---
id: {ki_id}
type: knowledge
owner: OA
source: {source_fname}
created_at: {datetime.now().isoformat()}
tags: [knowledge-item, auto-extracted]
---

# Knowledge Item: {stem}

> [!NOTE]
> Auto-extracted by OA Academy. TODO: Human review recommended.

## Summary
(OA: LLM extraction pending  source file: `{source_fname}`)

## Key Concepts
- TODO

## References
- Source: `{PATHS.RAW_DUMPS}/{source_fname}`
"""
    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OmniClaw System Event]")
    return draft_path


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def collect_knowledge():
    """
    OA autonomously scans brain/ecosystem to update awareness.
    Does not execute writes during this phase; only synthesizes context.
    """
    print("[OmniClaw System Event]")
    report_before(DAEMON_NAME, "COLLECT_KNOWLEDGE", ["brain/", "ecosystem/"])

    brain_files   = deep_scan(abs_path("brain"),     extensions=(".md", ".json"))
    eco_files     = deep_scan(abs_path("ecosystem"), extensions=(".md", ".json"))
    stray_brain   = find_stray_files(abs_path("brain"))
    stray_eco     = find_stray_files(abs_path("ecosystem"))

    summary = {
        "brain_files": len(brain_files),
        "ecosystem_files": len(eco_files),
        "stray_brain": len(stray_brain),
        "stray_ecosystem": len(stray_eco),
    }
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    report_after(DAEMON_NAME, "COLLECT_KNOWLEDGE",
                 {"success": summary["brain_files"] + summary["ecosystem_files"], "failed": 0, "skipped": 0})
    return summary


# [System log: Legacy non-English comment removed]
# 5.UPGRADE
# [System log: Legacy non-English comment removed]
def create_artifact(artifact_type: str, name: str, content: str, meta: dict = None):
    """ [System log: Legacy non-English docstring localized] """
    os.makedirs(OA_WORKSHOP, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{artifact_type}_{name}_{ts}.md"
    draft_path = os.path.join(OA_WORKSHOP, fname)

    fm = {"id": f"{artifact_type}-{name}", "type": artifact_type,
          "owner": "OA", "created_at": datetime.now().isoformat()}
    if meta:
        fm.update(meta)

    frontmatter = "---\n" + "".join(f"{k}: {v}\n" for k, v in fm.items()) + "---\n\n"
    report_before(DAEMON_NAME, f"CREATE_{artifact_type.upper()}", [name])
    with open(draft_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + content)
    print("[OmniClaw System Event]")
    handoff_to_oer(draft_path, reason=f"New {artifact_type}: {name}")
    report_after(DAEMON_NAME, f"CREATE_{artifact_type.upper()}", {"success": 1, "failed": 0, "skipped": 0})


def propose_new_rule(rule_id: str, title: str, content: str):
    """Produce Rules in brain/rules via OER."""
    create_artifact("rules", rule_id, content, meta={"name": title, "tags": "[proposed, oa-generated]"})


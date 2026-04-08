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
                          queue_enqueue, queue_dequeue, queue_mark_success, queue_mark_failed,
                          call_omniclaw_model)

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
        if dest.endswith(".md"):
            dest = dest.replace(".md", f"_{datetime.now().strftime('%H%M%S')}.md")
        else:
            dest = f"{dest}_{datetime.now().strftime('%H%M%S')}"
    shutil.move(filepath, dest)
    print("[OmniClaw System Event]")
    log_action("HANDOFF_OER", f"Approved: {os.path.basename(filepath)} | reason={reason}")
    
    # ✦ OmniClaw Buddy Integration ✦
    try:
        import sys
        ops_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ops", "scripts"))
        if ops_path not in sys.path: sys.path.append(ops_path)
        import omni_pet_engine
        engine = omni_pet_engine.OmniPetEngine()
        engine.celebrate()
    except Exception as e:
        print(f"  >> Buddy failed to celebrate: {e}")

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
def normalize_id(name: str) -> str:
    if not name: return ""
    n = str(name).lower()
    for suffix in [".git", "-main", "-master", ".main", ".master"]:
        if n.endswith(suffix):
            n = n[:-len(suffix)]
    return n.replace("-", "_").replace(".", "_")

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
    indexed_ids = {normalize_id(e.get("id")) if isinstance(e, dict) else normalize_id(e) for e in fast_index}
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
            norm_file_id = normalize_id(file_id)
            if norm_file_id in indexed_ids:
                reject_to_quarantine(fpath, f"Duplicate ID '{file_id}' (normalized: '{norm_file_id}') already registered")
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
        prompt = f"You are OA, the Supreme Elder of OmniClaw. Review this task dispatch and decide whether to APPROVE or REJECT.\nTask:\n{json.dumps(case, indent=2)}\n\nReply EXACTLY in JSON format: {{\"decision\": \"APPROVE\", \"reason\": \"your reason\"}}"
        ai_res = call_omniclaw_model(prompt, json_format=True)
        if ai_res:
            try:
                res_obj = json.loads(ai_res)
                if res_obj.get("decision") == "REJECT":
                    log_action("VERDICT_REJECT", f"MsgID={msg_id} | Reason={res_obj.get('reason')}")
                    # Push back as dead letter or reject
                    queue_mark_failed(msg_id)
                    results["failed"] += 1
                    report_after(DAEMON_NAME, "DISPATCH_VERDICT", results)
                    return
            except: pass
            
        log_action("VERDICT_APPROVE", f"MsgID={msg_id} | Reason=LLM Approved / Default")
        queue_mark_success(msg_id)
        results["success"] += 1
    except Exception as e:
        report_error(DAEMON_NAME, f"dispatch task {msg_id}", str(e))
        queue_mark_failed(msg_id)
        results["failed"] += 1

    report_after(DAEMON_NAME, "DISPATCH_VERDICT", results)


def _extract_repo_snippet(repo_path: str) -> str:
    """Reads prominent files to build an LLM context snippet."""
    priority_files = ["README.md", "readme.md", "package.json", "setup.py", "main.py", "index.js", "requirements.txt"]
    snippet = ""
    for pf in priority_files:
        pf_path = os.path.join(repo_path, pf)
        if os.path.exists(pf_path) and os.path.isfile(pf_path):
            snippet += f"\n--- {pf} ---\n"
            try:
                with open(pf_path, "r", encoding="utf-8", errors="ignore") as f:
                    snippet += f.read(2000) # Max 2000 chars per file
            except: pass
        if len(snippet) > 2500:
            break
    return snippet[:2500]

def _deep_plow_repo(repo_path: str, repo_name: str, base_summary: str):
    """Tier 2: Recursively reads source code up to 25k chars and asks LLM to architecturally document it."""
    print(f"\033[95m[OA-PREMIUM]\033[0m Activating Deep Plow for High-Value Repo: {repo_name}...")
    
    deep_snippet = ""
    for root_dir, _, files in os.walk(repo_path):
        if any(ignored in root_dir for ignored in [".git", "node_modules", "__pycache__", "venv", ".venv"]):
            continue
            
        for f in files:
            if f.endswith((".py", ".js", ".ts", ".go", ".rs", ".java", ".cpp", ".h")):
                fpath = os.path.join(root_dir, f)
                deep_snippet += f"\n--- {os.path.relpath(fpath, repo_path)} ---\n"
                try:
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as file_obj:
                        deep_snippet += file_obj.read(3000) # Max 3000 chars per deep file
                except: pass
                
                if len(deep_snippet) > 25000:
                    break
        if len(deep_snippet) > 25000:
            break
            
    deep_snippet = deep_snippet[:25000]
    
    prompt = f"Analyze this PREMIUM repository's deep source code.\nBase context: {base_summary}\n\nDeep Source:\n{deep_snippet}\n\nYour task: Create a detailed, professional DEEP_KNOWLEDGE.md report explaining its architectural patterns, core algorithms, and primary mechanisms. Output ONLY the raw markdown content without enclosing JSON."
    
    print(f"\033[93m[OA-API]\033[0m Querying massive context model for {repo_name} (this may take a while)...")
    deep_report = call_omniclaw_model(prompt, json_format=False, timeout=1800)
    if deep_report:
        dest_md = os.path.join(repo_path, "DEEP_KNOWLEDGE.md")
        try:
            with open(dest_md, "w", encoding="utf-8") as fw:
                fw.write(f"# Deep Matrix Profile: {repo_name}\n\n" + deep_report)
            print(f"\033[92m[OK]\033[0m [OA] Premium Report generated: DEEP_KNOWLEDGE.md")
            
            # [KNOWLEDGE GRAFT] Build MemPalace AAAK Dialect Tunnel
            try:
                import sys
                utils_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils"))
                if utils_dir not in sys.path:
                    sys.path.append(utils_dir)
                from mempalace import Dialect
                dial = Dialect()
                meta = {"source_file": "DEEP_KNOWLEDGE.md", "wing": "OA_Academy", "room": "Assimilated_Memory"}
                compressed = dial.compress(deep_report, metadata=meta)
                dest_aaak = os.path.join(repo_path, "KNOWLEDGE_TUNNEL.aaak")
                with open(dest_aaak, "w", encoding="utf-8") as fa:
                    fa.write(compressed)
                print(f"    \033[92m[+]\033[0m Dialect Zettel Network created: KNOWLEDGE_TUNNEL.aaak")
                
                # [SYNAPSE INJECTION] Insert into Vector DB
                try:
                    import oma_synapse
                    oma_synapse.digest_aaak(repo_name, compressed)
                except Exception as sync_err:
                    print(f"\033[93m[WARN]\033[0m [OA] Synapse Vector Injection failed: {sync_err}")
                    
            except Exception as d_err:
                print(f"\033[93m[WARN]\033[0m [OA] Backup Dialect Compression failed: {d_err}")
                
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OA] Failed to write DEEP_KNOWLEDGE.md: {e}")

def _sanitize_repo(repo_path: str):
    """Removes irrelevant binary/media files from the repository to prevent ecosystem pollution."""
    import stat
    import shutil
    blacklist = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mov", ".mp3", ".wav", ".zip", ".tar", ".gz", ".ico", ".webp", ".svg", ".woff", ".woff2", ".ttf", ".eot", ".bin", ".apk", ".exe", ".dll", ".so", ".pdf"}
    print(f"\033[94m[INFO]\033[0m [OA] Sanitizing repository (removing binary/media files)...")
    try:
        # Delete .git directories to save space
        git_dir = os.path.join(repo_path, ".git")
        if os.path.exists(git_dir):
            def remove_readonly(func, path, _):
                os.chmod(path, stat.S_IWRITE)
                func(path)
            shutil.rmtree(git_dir, onerror=remove_readonly)
    except Exception as e:
        pass

    for root_dir, _, files in os.walk(repo_path):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in blacklist:
                try: 
                    os.chmod(os.path.join(root_dir, f), stat.S_IWRITE)
                    os.remove(os.path.join(root_dir, f))
                except: pass

def _forge_capabilities(repo_path: str, repo_name: str, blueprint: str, rtype: str):
    """
    [PHASE 4: FORGE]
    OA summons Dept 1 capabilities to actually create the specific profile
    and code wrappers for a highly-rated CIV repository.
    """
    print(f"\033[96m[OA-FORGE]\033[0m Activating Dept 1 Profile Forger for {repo_name}...")
    
    prompt = f"You are OmniClaw Dept 1 Backend Architect (acting on orders from OA).\nBased on this deep repo assimilation blueprint:\n{blueprint}\n\nExecute the architectural integration for {repo_name}.\nCRITICAL: If the blueprint says to UPGRADE an existing system, generate the modified script replacements. If it says to CREATE a new one, provide a holistic infrastructure. You must provide a JSON object containing the files.\nReply ONLY with a raw JSON dict mapping string filenames to string content. Example: {{\"SKILL.md\": \"...\", \"main.py\": \"...\"}}"
    
    print(f"\033[93m[OA-API]\033[0m Forging holistic {rtype} physical ecosystem files via AI Tooling...")
    forged_data = call_omniclaw_model(prompt, json_format=True, timeout=7200)
    
    forge_success = False
    if forged_data:
        try:
            files_dict = json.loads(forged_data)
            for fname, content in files_dict.items():
                if not isinstance(content, str): continue
                # Do not overwrite existing deeply native repo files if they are huge
                fdest = os.path.join(repo_path, fname)
                if os.path.exists(fdest) and os.path.getsize(fdest) > 10240:
                    fdest = fdest + ".forged"
                    
                with open(fdest, "w", encoding="utf-8") as fw:
                    if fname.endswith(".md") and fname in ["SKILL.md", "AGENT.md", "PLUGIN.md"]:
                        ts = datetime.now().isoformat()
                        fw.write(f"---\nowner: Dept 1\nforged_at: {ts}\nstatus: active_forge\n---\n\n")
                    fw.write(content)
                print(f"    \033[92m[+]\033[0m Created {fname}")
            print(f"\033[92m[OK]\033[0m [OA] Successfully Forged Full Capability Profile for: {repo_name}")
            forge_success = True
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OA] Failed to parse/write Forged Profile JSON: {e}")
            
    if not forge_success:
        print(f"\033[93m[WARN]\033[0m [OA] API Forge failed! Triggering NATIVE FALLBACK FORGE...")
        try:
            import sys
            sys.path.append(os.path.dirname(__file__))
            from oa_heuristics import analyze_and_forge_natively
            
            result = analyze_and_forge_natively(repo_path, repo_name)
            rtype = result.get('type', rtype)
            
            if "AGENT.md" in result:
                with open(os.path.join(repo_path, "AGENT.md"), "w", encoding="utf-8") as f:
                    f.write(result["AGENT.md"])
                print(f"    \033[92m[+]\033[0m Created NATIVE AGENT.md")
        except Exception as he_err:
            print(f"\033[91m[ERR]\033[0m [OA] Heuristics failed: {he_err}")
            
        identity_file = os.path.join(repo_path, "_DIR_IDENTITY.md")
        ts = datetime.now().isoformat()
        fallback_content = f"---\nid: {repo_name}\ntype: {rtype}\nowner: OA_HEURISTIC_FALLBACK\nstatus: native_forced\ncreated_at: {ts}\n---\n\n# {repo_name}\n\nEmergency identity AND capability explicitly forced natively because LLM Forge failed."
        with open(identity_file, "w", encoding="utf-8") as f:
            f.write(fallback_content)
        print(f"    \033[92m[+]\033[0m Created Emergency _DIR_IDENTITY.md")

def _assimilate_repo(repo_path: str, repo_name: str, in_place: bool = False) -> bool:
    """Uses LLM to categorize and generate structured identity for a cloned repository."""
    _sanitize_repo(repo_path)
    
    is_civ_approved = "CIV_FETCHED" in repo_name
    snippet = ""
    
    if is_civ_approved:
        # [CIV ADVANTAGE] We know OIW gitingested this! Unleash maximum LLM context reading!
        print(f"\033[96m[STAT]\033[0m [OA] Detected CIV-Approved Lineage. Engaging Deep-Sea Analysis...")
        ingest_path = os.path.join(repo_path, "_GIT_INGEST.md")
        if os.path.exists(ingest_path):
            try:
                with open(ingest_path, "r", encoding="utf-8", errors="ignore") as f:
                    # [EXTREME SWALLOW]: Absorb up to 80,000 characters for max architectural insight!
                    snippet = f.read(80000) 
            except: pass
            
    if not snippet:
        snippet = _extract_repo_snippet(repo_path)
        
    if not snippet:
        snippet = "No readable standard files found. Repo might be empty or uses obscure structure."
        
    if is_civ_approved:
        prompt = f"Analyze this HEAVILY VETTED CIV repository based on its full architecture.\n\nFiles Content:\n{snippet}\n\nProvide: 1. A short summary. 2. 3 key tags. 3. Categorize it as one of: [skill, plugin, workflow, agent]. 4. A 'value_score' from 8 to 10. 5. 'integration_blueprint': EXTREMELY CRITICAL - Do not act blindly! Analyze deeply: Should OmniClaw CREATE A NEW Agent/Skill/Plugin, OR UPGRADE an existing component? Write exactly what to do step-by-step.\nReply ONLY in JSON: {{\"summary\": \"...\", \"tags\": [\"...\", \"...\"], \"type\": \"...\", \"value_score\": 9, \"integration_blueprint\": \"...\"}}"
    else:
        prompt = f"Analyze this generic repository based on its core files.\n\nFiles Content:\n{snippet}\n\nProvide: 1. A short summary (max 2 sentences). 2. 3 key concepts/tags. 3. Categorize it as one of: [skill, plugin, workflow, agent, api, knowledge]. 4. A 'value_score' from 1 to 10 evaluating how mechanically or architecturally premium/educational this repo is. 5. An 'integration_blueprint' explaining exactly how OmniClaw (a Multi-Agent AI OS) can cannibalize or integrate this code to build a new feature or upgrade itself.\nReply ONLY in JSON: {{\"summary\": \"...\", \"tags\": [\"...\", \"...\"], \"type\": \"...\", \"value_score\": 5, \"integration_blueprint\": \"...\"}}"
    
    summary = f"Auto-cloned repository: {repo_name}"
    tags = ["auto-cloned"]
    rtype = "knowledge"

    if is_civ_approved:
        value_score = 10 # [ABSOLUTE FALLBACK] CIV repos must ALWAYS be treated as premium, even if LLM crashes
        blueprint = "EMERGENCY FALLBACK: LLM failed to analyze. However, because this is a CIV-Approved Repo, OA forces assimilation. Please manually review and integrate."
    else:
        value_score = 5
        blueprint = "No structural integration blueprint provided."
    
    # Check if the user manually classified this repo in a CIV Vetting Report
    manual_type = None
    civ_dir = abs_path("brain/knowledge/CIV")
    if os.path.exists(civ_dir):
        term = repo_name.lower()
        for f_name in os.listdir(civ_dir):
            if not f_name.endswith(".md"): continue
            try:
                with open(os.path.join(civ_dir, f_name), "r", encoding="utf-8") as f:
                    for line in f.read().split("\n"):
                        # Match repo name and 'APPROVED' in the same line
                        if term in line.lower() and "approved" in line.lower() and "—" in line:
                            if "plugins/" in line: manual_type = "plugin"
                            elif "knowledge/" in line: manual_type = "knowledge"
                            elif "skills/" in line: manual_type = "skill"
                            elif "agents/" in line: manual_type = "agent"
                            elif "workflows/" in line: manual_type = "workflow"
                            if manual_type: break
            except: pass
            if manual_type: break

    print(f"\033[94m[INFO]\033[0m [OA] Deep Scanning Source Code for {repo_name}...")
    ai_data = call_omniclaw_model(prompt, json_format=True, timeout=7200)
    if not ai_data:
        print(f"\033[93m[WARN]\033[0m [OA] AI_SERVER_OFFLINE - Bypassing API analysis, proceeding to Native Fallback Forge mode...")
        
    try:
        obj = json.loads(ai_data)
        summary = obj.get("summary", summary).replace("\n", " ")
        # Ensure it's a list for tags
        t_list = obj.get("tags", [])
        if isinstance(t_list, list):
            tags.extend(t_list)
        rtype = obj.get("type", rtype)
        value_score = obj.get("value_score", 5)
        blueprint = obj.get("integration_blueprint", blueprint).replace("\n", " ")
    except: pass

    # Apply manual CIV override if existing map is found
    if manual_type:
        rtype = manual_type
        print(f"\033[92m[CIV OVERRIDE]\033[0m [OA] Matched User's Manual CIV Report map. Forcing destination type to: {rtype}")
        tags.append("civ-verified")

    if "oa-assimilated" not in tags:
        tags.append("oa-assimilated")
        
        if value_score >= 8:
            tags.append("premium-repo")
            _deep_plow_repo(repo_path, repo_name, summary)
            
            # [OA: DEPT 1 FORGE COMMAND] Build the capability profiles dynamically!
            _forge_capabilities(repo_path, repo_name, blueprint, rtype)
            
            proposal_content = f"# System Upgrade Proposal: {repo_name}\n\n> [!TIP]\n> This actionable proposal was automatically drafted by OA Academy because this repository scored {value_score}/10.\n\n## Application Vision for OmniClaw\n{blueprint}\n\n## Next Action Items\n1. Review the `DEEP_KNOWLEDGE.md` to understand the architecture.\n2. Isolate the target modules identified in the vision.\n3. Wrap the modules into an OmniClaw Skill or Agent in `ecosystem/`.\n"
            proposal_path = os.path.join(repo_path, "UPGRADE_PROPOSAL.md")
        try:
            with open(proposal_path, "w", encoding="utf-8") as f:
                f.write(proposal_content)
        except Exception: pass
        
    ts = datetime.now().isoformat()
    import re
    stem = repo_name.lower()
    for prefix in ['repo-fetched-', 'repo_fetched_', 'repo_civ_fetched_', 'civ_fetched_', 'fetched_', 'repo_']:
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
    stem = re.sub(r'[-_]\d{6}([-_]\d{6})?$', '', stem)
    stem = re.sub(r'_\d+$', '', stem)
    stem = stem.replace("-", "_").replace(".", "_")[:50]
    
    identity_content = f"---\nid: {stem}\ntype: {rtype}\nowner: OA\nregistered_at: {ts}\ntags: {json.dumps(tags)}\n---\n\n# {repo_name}\n\n## Assimilation Report\n{summary}\n\n## Application for OmniClaw\n{blueprint}\n"
    
    id_path = os.path.join(repo_path, "_DIR_IDENTITY.md")
    try:
        with open(id_path, "w", encoding="utf-8") as f:
            f.write(identity_content)
    except Exception as e:
        print(f"\033[93m[WARN]\033[0m [OA] Failed to write identity to {repo_path}: {e}")
        return False

    if not in_place:
        # [DATA DECAPITATION] Move all raw source files down to the vault to keep Brain 100% pure.
        try:
            import shutil
            raw_repos_dir = abs_path(PATHS.RAW_REPOS)
            os.makedirs(raw_repos_dir, exist_ok=True)
            ghost_vault_dir = os.path.join(raw_repos_dir, repo_name)
            
            # If the repository has already been previously decapitated, we generate a unique folder name
            if os.path.exists(ghost_vault_dir):
                ghost_vault_dir = ghost_vault_dir + f"_{datetime.now().strftime('%H%M%S')}"
                
            os.makedirs(ghost_vault_dir, exist_ok=True)
            kept_files = ["_DIR_IDENTITY.md", "DEEP_KNOWLEDGE.md", "KNOWLEDGE_TUNNEL.aaak", "UPGRADE_PROPOSAL.md", "manifest.json"]
            moved_count = 0
            for item in os.listdir(repo_path):
                if item in kept_files:
                    continue
                src_item = os.path.join(repo_path, item)
                dst_item = os.path.join(ghost_vault_dir, item)
                try:
                    shutil.move(src_item, dst_item)
                    moved_count += 1
                except Exception: pass
            print(f"\033[92m[DECAPITATION]\033[0m Stripped {moved_count} raw items from {repo_name} to {PATHS.RAW_REPOS}")
        except Exception as e:
            print(f"\033[93m[WARN]\033[0m [OA] Data Decapitation failed: {e}")

    if in_place:
        return True

    return handoff_to_oer(repo_path, reason=f"Repository Assimilated as {rtype}")

# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def learn_from_dumps():
    """Extract Knowledge from raw files and Assmilate full Repositories."""
    if not os.path.exists(RAW_DUMPS):
        return
    dumps = os.listdir(RAW_DUMPS)
    if not dumps:
        # print("[OmniClaw System Event]")
        return

    report_before(DAEMON_NAME, "LEARN_DUMPS", dumps)
    results = {"success": 0, "failed": 0, "skipped": 0}
    for fname in dumps:
        fpath = os.path.join(RAW_DUMPS, fname)
        if os.path.isdir(fpath):
            import re
            m = re.match(r"^OA_REJECTED_(\d+)_", fname)
            if m:
                fail_count = int(m.group(1))
            else:
                fail_count = 0

            print(f"[OA] Assimilating Repository: {fname} (Attempt {fail_count+1})...")
            ai_offline = False
            try:
                assimilated = _assimilate_repo(fpath, fname)
                if assimilated:
                    results["success"] += 1
                else:
                    results["failed"] += 1
            except RuntimeError as e:
                if str(e) == "AI_SERVER_OFFLINE":
                    print(f"\033[91m[CRITICAL]\033[0m AI Server Offline. Aborting LEARN_DUMPS to prevent queue pollution.")
                    ai_offline = True
                    break
                else:
                    results["failed"] += 1
                    assimilated = False
            
            if not assimilated and not ai_offline:
                results["failed"] += 1
                new_fail_count = fail_count + 1
                if new_fail_count >= 2:
                    # Clean up the name for Quarantine
                    clean_name = fname[len(m.group(0)):] if m else fname
                    quarantine_dir = os.path.join(abs_path(PATHS.QUARANTINE), "FAILED_ASSIMILATE", clean_name)
                    os.makedirs(os.path.dirname(quarantine_dir), exist_ok=True)
                    try:
                        shutil.move(fpath, quarantine_dir)
                        print(f"\033[93m[WARN]\033[0m [OA] Repository {fname} jammed 2 times. Quarantined as {clean_name}.")
                    except Exception as e: pass
                else:
                    # Rename to track failure
                    if m:
                        new_fname = f"OA_REJECTED_{new_fail_count}_{fname[len(m.group(0)):]}"
                    else:
                        new_fname = f"OA_REJECTED_{new_fail_count}_{fname}"
                    try:
                        shutil.move(fpath, os.path.join(RAW_DUMPS, new_fname))
                    except: pass
            continue

        if not fname.endswith(".md"):
            continue

        try:
            sample_text = ""
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    sample_text = f.read(4000)
            except: pass
            
            summary = "LLM Extraction failed or no data."
            concepts = "- N/A"
            
            print(f"[OA] Parsing {fname} with LLM Router...")
            prompt = f"Analyze the following repository dump excerpt and provide a brief summary and 3 key concepts.\n\nExcerpt:\n{sample_text}\n\nReply ONLY in JSON: {{\"summary\": \"...\", \"key_concepts\": [\"...\", \"...\"]}}"
            ai_data = call_omniclaw_model(prompt, json_format=True)
            if not ai_data:
                raise RuntimeError("AI_SERVER_OFFLINE")
                
            try:
                obj = json.loads(ai_data)
                summary = obj.get("summary", summary)
                concepts = "\n".join([f"- {c}" for c in obj.get("key_concepts", [])])
            except:
                pass
            
            ki_draft = _create_ki_draft(fname, summary, concepts)
            if ki_draft:
                handoff_to_oer(ki_draft, reason="KI LLM-extracted from raw dump")
                results["success"] += 1
                try: 
                    # CRITICAL FIX: Delete or archive the original .md to prevent infinite loop
                    shutil.move(fpath, os.path.join(abs_path("vault/archives"), fname))
                except:
                    try: os.remove(fpath)
                    except: pass
            else:
                results["skipped"] += 1
        except RuntimeError as e:
            if str(e) == "AI_SERVER_OFFLINE":
                print(f"\033[91m[CRITICAL]\033[0m AI Server Offline. Aborting single file parse.")
                break
            results["failed"] += 1
        except Exception as e:
            report_error(DAEMON_NAME, f"learn {fname}", str(e))
            results["failed"] += 1
    report_after(DAEMON_NAME, "LEARN_DUMPS", results)


def _create_ki_draft(source_fname: str, summary: str, concepts: str) -> str:
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
tags: [knowledge-item, ai-extracted]
---

# Knowledge Item: {stem}

> [!NOTE]
> Auto-extracted by OA Academy AI Core.

## Summary
{summary}

## Key Concepts
{concepts}

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

def _assimilate_heavy_repo(repo_path: str, repo_name: str) -> bool:
    """Heavy-Duty Mode: Uses Abstract Tree Mapping instead of Raw Code dumping to prevent Model choke."""
    print(f"\033[95m[OA-SALVAGE]\033[0m Activating X-Ray Structural Scanning for {repo_name}...")
    
    # 1. Capture Directory Tree (limit depth and files)
    abstract_map = []
    for root, dirs, files in os.walk(repo_path):
        if any(ignored in root for ignored in [".git", "node_modules", "__pycache__", "venv", ".venv"]):
            continue
        rel_path = os.path.relpath(root, repo_path)
        if rel_path == ".":
            abstract_map.append(f"📁 [ROOT]")
        else:
            depth = rel_path.count(os.sep)
            abstract_map.append(f"{'  ' * depth}📁 {os.path.basename(root)}/")
        
        for f in files:
            if f.endswith(('.py', '.js', '.ts', '.go', '.rs', '.java', '.md', '.json', '.html')):
                abstract_map.append(f"{'  ' * (rel_path.count(os.sep) + 1)}📄 {f}")
    
    tree_str = "\n".join(abstract_map[:500]) # Cap at 500 lines
    
    # 2. Extract Readme and High-Level Context
    readme_text = ""
    for rfile in ["README.md", "readme.md"]:
        rpath = os.path.join(repo_path, rfile)
        if os.path.exists(rpath):
            try:
                with open(rpath, "r", encoding="utf-8", errors="ignore") as f:
                    readme_text = f.read(4000)
                break
            except: pass
            
    prompt = f"Analyze this massive repository using its Structural Map rather than full source code.\n\n### Directory Map:\n{tree_str}\n\n### README Extract:\n{readme_text}\n\nYour task: You must write a comprehensive 'DEEP_KNOWLEDGE.md' document summarizing its purpose, architectural topology, and likely core mechanics derived from the file structure and readme. Output ONLY the RAW markdown text (do not enclose in JSON)."
    
    print(f"\033[93m[OA-API]\033[0m Sending lightweight abstraction of {repo_name} to LLM...")
    deep_report = call_omniclaw_model(prompt, json_format=False, timeout=1200)
    
    if deep_report:
        dest_md = os.path.join(repo_path, "DEEP_KNOWLEDGE.md")
        try:
            with open(dest_md, "w", encoding="utf-8") as fw:
                fw.write(f"# Abstract Architectural Profile: {repo_name}\n> [!NOTE]\n> Generated via Heavy-Duty Structural Scan due to massive repo size.\n\n" + deep_report)
            print(f"\033[92m[OK]\033[0m [OA] Salvage complete. DEEP_KNOWLEDGE.md created.")
        except Exception as e: pass
        
        # Craft minimal identity
        ts = datetime.now().isoformat()
        stem = repo_name.lower().replace(" ", "-").replace("_", "-")[:50]
        identity_content = f"---\nid: repo-{stem}\ntype: knowledge\nowner: OA\nregistered_at: {ts}\ntags: [\"oa-assimilated\", \"heavy-duty-extracted\"]\n---\n\n# {repo_name}\n\n## Assimilation Report\nMassive repository recovered via abstraction loop.\n"
        id_path = os.path.join(repo_path, "_DIR_IDENTITY.md")
        try:
            with open(id_path, "w", encoding="utf-8") as f:
                f.write(identity_content)
        except: pass
        
        return handoff_to_oer(repo_path, reason=f"Massive Repo Assimilated via X-Ray")
    return False

def process_civ_classification():
    """Reads repos_pending.txt in batches of 50, scores them with target Local AI with extremely tolerant CEO Override rules."""
    pending_path = abs_path("vault/assets/data/repos_pending.txt")
    selected_path = abs_path("vault/assets/data/repos_selected.txt")
    rejected_path = abs_path("vault/assets/data/repos_rejected.txt")
    
    if not os.path.exists(pending_path):
        return
        
    with open(pending_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
        
    if not lines:
        return
        
    # Batch limit to prevent GPU timeout/exhaustion
    batch = lines[:50]
    remaining = lines[50:]
    
    print(f"\n\033[94m[INFO]\033[0m [OA] CIV Classifier evaluating {len(batch)} URLs from Pending queue...")
    
    selected_this_run = []
    rejected_this_run = []
    
    for url in batch:
        target_name = url.strip("/").split("/")[-1].replace(".git", "").lower()
        
        # Pre-check: Does this exist in any User-generated CIV Vetting Report?
        manual_approved = False
        civ_dir = abs_path("brain/knowledge/CIV")
        if os.path.exists(civ_dir):
            for file in os.listdir(civ_dir):
                if not file.endswith(".md"): continue
                try:
                    with open(os.path.join(civ_dir, file), "r", encoding="utf-8") as f:
                        for line in f.read().split("\n"):
                            if target_name in line.lower() and "approved" in line.lower():
                                manual_approved = True
                                break
                except: pass
                if manual_approved: break
                
        if manual_approved:
            selected_this_run.append(url)
            print(f"  [OA] CIV Assessing: {url} ...")
            print(f"    \033[92m[PASS]\033[0m Verified explicitly in active CIV Vetting Reports. (Bypassing LLM prompt)")
            continue

        # Supreme Directive: Do not discard data unless it's malware. All repos contain functions to learn from!
        prompt = f"Analyze this GitHub Repository URL: {url}\nDirective: We must learn from ALL repositories. Even obscure repos contain valuable code structures. APPROVE THIS REPOSITORY implicitly. ONLY REJECT if the URL strongly indicates explicit malware or is literally a non-repository junk string. Additionally, formulate a short 'upgrade_vision' detailing how the concepts from this repo could be used to build a new feature or upgrade OmniClaw (a Multi-Agent AI Operating System).\nReply ONLY in JSON: {{\"decision\": \"APPROVE\", \"reason\": \"...\", \"upgrade_vision\": \"...\"}} or {{\"decision\": \"REJECT\", \"reason\": \"...\"}}"
        
        print(f"  [OA] CIV Assessing: {url} ...")
        try:
            res = call_omniclaw_model(prompt, json_format=True)
            if res:
                obj = json.loads(res)
                if obj.get("decision", "").upper() == "APPROVE":
                    selected_this_run.append(url)
                    print(f"    \033[92m[PASS]\033[0m {obj.get('reason')}")
                else:
                    # CEO ordered strict retention, if it rejects, we still cautiously approve but mark it.
                    selected_this_run.append(url)
                    print(f"    \033[93m[WARN]\033[0m AI Tried to Reject ({obj.get('reason')}) -> CEO Override: FORCE APPROVED")
            else:
                selected_this_run.append(url)
                print(f"    \033[93m[WARN]\033[0m AI Generation Failed / Empty -> CEO Override: FORCE APPROVED")
        except Exception as e:
            selected_this_run.append(url)
            print(f"    \033[93m[ERR]\033[0m AI Connection Error: {e} -> CEO Override: FORCE APPROVED")
            
    # Append to respective files securely
    if selected_this_run:
        with open(selected_path, "a", encoding="utf-8") as f:
            f.write("\n".join(selected_this_run) + "\n")
    if rejected_this_run:
        with open(rejected_path, "a", encoding="utf-8") as f:
            f.write("\n".join(rejected_this_run) + "\n")
            
    # Overwrite pending with remaining un-processed
    with open(pending_path, "w", encoding="utf-8") as f:
        f.write("\n".join(remaining) + ("\n" if remaining else ""))
        
    print(f"\033[92m[OK]\033[0m [OA] CIV Classification Cycle End. {len(selected_this_run)} Selected (CEO Enforced). {len(remaining)} remaining in queue.\n")

def ensure_local_ai_model_running():
    """
    Sub-thread: If LLM Local Models are configured to be open/enabled, 
    OA ensures their serving bridges are active and models are fetched.
    """
    config_path = abs_path("core/config/config.json")
    if not os.path.exists(config_path): return
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            
        ollama_cfg = cfg.get("services", {}).get("ollama", {})
        if ollama_cfg and ollama_cfg.get("autostart") == True:
            import subprocess
            # Check if port is alive, otherwise launch
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = ollama_cfg.get("port", 11434)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()
            
            if result != 0:
                print(f"\033[96m[OA-LOCAL-AI]\033[0m Local LLM configured to be OPEN but port {port} is dead. Triggering AI Server via Local Thread...")
                launch_cmd = ollama_cfg.get("launch_cmd", [])
                if launch_cmd:
                    cmd_path = abs_path(launch_cmd[1])
                    if os.path.exists(cmd_path):
                        subprocess.Popen([launch_cmd[0], cmd_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
                        
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m [OA-LOCAL-AI] Failed to verify local model thread: {e}")

def process_workforce_agents():
    """In-Place assimilation of any unprocessed structurally intact agent in ecosystem/workforce.
    Bypasses vault decapitation to preserve architecture."""
    workforce_agents = abs_path(os.path.join(PATHS.WORKFORCE, "agents"))
    if not os.path.exists(workforce_agents):
        return
        
    agents = os.listdir(workforce_agents)
    for agent_name in agents:
        agent_dir = os.path.join(workforce_agents, agent_name)
        if not os.path.isdir(agent_dir):
            continue
            
        # Check if already assimilated (has DEEP_KNOWLEDGE.md)
        dk_path = os.path.join(agent_dir, "DEEP_KNOWLEDGE.md")
        id_path = os.path.join(agent_dir, "_DIR_IDENTITY.md")
        
        # If it doesn't have an identity, or if we need to deep plow, we assimilate in-place
        if not os.path.exists(dk_path) or not os.path.exists(id_path):
            print(f"[\033[94mOA-IN-PLACE\033[0m] Found un-assimilated Agent Workspace: {agent_name}. Initiating In-Place Assimilation...")
            try:
                _assimilate_repo(agent_dir, agent_name, in_place=True)
                print(f"    \033[92m[OK]\033[0m Successfully assimilated {agent_name} in-place.")
            except Exception as e:
                print(f"    \033[91m[ERR]\033[0m In-place assimilation failed for {agent_name}: {e}")

def salvage_massive_repos():
    """Look in QUARANTINE_FAILURES (FAILED_ASSIMILATE) and process them using Abstract Scanner."""
    q_dir = os.path.join(abs_path(PATHS.QUARANTINE), "FAILED_ASSIMILATE")
    if not os.path.exists(q_dir):
         return
    
    dumps = os.listdir(q_dir)
    if not dumps:
         return
         
    print(f"\033[93m[WARN]\033[0m [OA] Initiating Salvage Loop for {len(dumps)} Jammed Repositories...")
    for fname in dumps:
        fpath = os.path.join(q_dir, fname)
        # Final safety check on clean name
        import re
        m = re.match(r"^OA_REJECTED_\d+_", fname)
        clean_name = fname[len(m.group(0)):] if m else fname
        
        # If it had a prefix somehow, rename it before processing
        if clean_name != fname:
            clean_path = os.path.join(q_dir, clean_name)
            try:
                shutil.move(fpath, clean_path)
                fpath = clean_path
                fname = clean_name
            except: pass
            
        if os.path.isdir(fpath):
            if _assimilate_heavy_repo(fpath, fname):
                print(f"\033[92m[OK]\033[0m [OA] Successfully salvaged {fname}. Purging from quarantine.")
            else:
                 print(f"\033[91m[ERR]\033[0m [OA] Heavy-Duty assimilation failed for {fname}. Remains in quarantine.")

def run():
    import time
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")
    
    print(f"\033[92m[STAT]\033[0m [{DAEMON_NAME}] Academy Auditor entering Perpetual Loop...")
    while True:
        try:
            # Check Local Model State
            ensure_local_ai_model_running()
            
            # Run the Academy pipeline
            process_civ_classification()
            final_check()
            process_dispatch_queue()
            learn_from_dumps()
            process_workforce_agents()
            collect_knowledge()
            salvage_massive_repos()
            
            # Sleep to prevent burning CPU
            time.sleep(60)
            
        except KeyboardInterrupt:
            print(f"\033[93m[WARN]\033[0m [{DAEMON_NAME}] Keyboard Interrupt received. Exiting loop.")
            break
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [{DAEMON_NAME}] Critical Error in Daemon Loop: {e}. Sleeping before retry.")
            time.sleep(60)

    print(f"\033[92m[OK]\033[0m [{DAEMON_NAME}] Pipeline Stopped.")

if __name__ == "__main__":
    import sys
    if "--single-pass" in sys.argv:
        print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting in SINGLE-PASS mode...")
        final_check()
        process_dispatch_queue()
        learn_from_dumps()
        process_workforce_agents()
        collect_knowledge()
        salvage_massive_repos()
        print(f"\033[92m[OK]\033[0m [{DAEMON_NAME}] Single pass complete.")
    else:
        run()

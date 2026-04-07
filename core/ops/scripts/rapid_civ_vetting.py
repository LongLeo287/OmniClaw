import os
import sys
import json
from datetime import datetime

# Adjust path to find daemon_utils
ops_dir = os.path.dirname(os.path.abspath(__file__))
ops_parent = os.path.dirname(ops_dir)
core_dir = os.path.dirname(ops_parent)
daemons_dir = os.path.join(core_dir, "daemons")
if daemons_dir not in sys.path:
    sys.path.append(daemons_dir)

from daemon_utils import call_omniclaw_model

root_dir = os.path.dirname(core_dir)
RAW_DUMPS = os.path.join(root_dir, "vault", "tmp", "raw_knowledge_dumps")
CIV_DIR = os.path.join(root_dir, "brain", "knowledge", "CIV")

def get_candidates():
    candidates = []
    keywords = ["agent", "rag", "mcp", "ui", "llm", "framework", "skill", "workflow", "core", "omni", "claude", "qwen", "ai", "vision", "audio"]
    if not os.path.exists(RAW_DUMPS):
        return []
        
    for d in os.listdir(RAW_DUMPS):
        d_path = os.path.join(RAW_DUMPS, d)
        if os.path.isdir(d_path):
            name = d.lower()
            score = 0
            for kw in keywords:
                if kw in name:
                    score += 1
            if "fetched_" in name.lower():
                score += 1 # prioritize the recently pushed ones
            
            # Additional heuristic: size
            try:
                # Just check count of files briefly to filter out empty ghosts
                fcount = len(os.listdir(d_path))
                if fcount > 2:
                    score += 0.5
                else:
                    score -= 5 # Empty
            except: pass
            
            candidates.append((d, d_path, score))
            
    # Sort and pick top 15
    candidates.sort(key=lambda x: x[2], reverse=True)
    return candidates[:6]

def extract_readme(path):
    for rm in ["README.md", "readme.md", "README"]:
        fp = os.path.join(path, rm)
        if os.path.exists(fp):
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read(1500) # limit to 1500 chars to save tokens
            except: pass
    return "No README available."

def generate_report():
    print(f"\033[94m[INFO]\033[0m Activating Rapid Vetting Batch 06...")
    cands = get_candidates()
    if not cands:
        print(f"\033[93m[WARN]\033[0m No candidates found in RAW_DUMPS.")
        return

    print(f"\033[94m[INFO]\033[0m Filtered top {len(cands)} candidates heuristically. Extracting Context...")
    
    context_blob = ""
    for idx, (name, d_path, score) in enumerate(cands):
        blob = extract_readme(d_path)
        context_blob += f"\n\n=======================\nREPO NUMBER {idx+1}: {name}\nHEURISTIC SCORE: {score}\nREADME EXCERPT:\n{blob}\n=======================\n"
        
    prompt = f"""You are the Content-Analyst-Agent (Dept 06) for OmniClaw OS.
I have heuristically selected {len(cands)} fetched repositories that currently reside in the unprocessed queue.
Your task is to review all of them based on their names and README excerpts, and select the TOP 5 absolute best / most strategic / coolest repositories that OmniClaw should integrate as skills/frameworks.

Input Repositories (1 to {len(cands)}):
{context_blob}

Task:
Write a Vetting Report matching the structure of 'vetting_report_batch_05.md'.
Include:
1. Executive Summary
2. Scan Results (Table mapping repo name, Focus Area, License, Score out of 100, and Decision)
   -> The top 5 must have decision "✅ APPROVED"
   -> The rest should be "⏳ HEAVY EXTRACT REQUIRED" or "❌ NOISE"
3. Detailed Assessments (Only for the Top 5 APPROVED). Explain why it is incredibly cool and what it provides.

Return ONLY the markdown document content (from --- frontmatter to the end). Do not wrap in JSON or ```markdown."""

    print(f"\033[93m[OA-API]\033[0m Sending massive batch prompt to LLM...")
    report_md = call_omniclaw_model(prompt, json_format=False, timeout=600)
    
    if not report_md:
        print("\033[91m[ERR]\033[0m Failed to generate Vetting Report.")
        return
        
    os.makedirs(CIV_DIR, exist_ok=True)
    report_path = os.path.join(CIV_DIR, "vetting_report_batch_06.md")
    
    if "---" not in report_md[:100]:
        fm = f"---\nid: vetting-report-batch-06\ntype: document\nowner: SYSTEM\ntags: [auto-vetting, batch-06]\nhealed_at: {datetime.now().isoformat()}\n---\n\n"
        report_md = fm + report_md
        
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_md)
        print(f"\033[92m[DONE]\033[0m Vetting Report generated at: {report_path}")
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m Cannot write report: {e}")

if __name__ == "__main__":
    generate_report()

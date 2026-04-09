"""HTML dashboard generator for ContribAI.

Generates a single-page dashboard with embedded CSS and JS.
No external dependencies required.
"""

from __future__ import annotations


def render_dashboard(
    stats: dict,
    repos: list[dict],
    prs: list[dict],
) -> str:
    """Render the HTML dashboard page."""
    repo_rows = ""
    for r in repos[:20]:
        repo_rows += (
            f"<tr>"
            f"<td>{_esc(r.get('full_name', ''))}</td>"
            f"<td>{r.get('language', '-')}</td>"
            f"<td>{r.get('stars', 0):,}</td>"
            f"<td>{r.get('findings', 0)}</td>"
            f"<td>{_esc(r.get('analyzed_at', '')[:10])}</td>"
            f"</tr>"
        )

    pr_rows = ""
    no_prs = '<tr><td colspan="5" style="color:var(--muted)">No PRs yet</td></tr>'
    no_repos = '<tr><td colspan="5" style="color:var(--muted)">No repos analyzed yet</td></tr>'
    for p in prs[:20]:
        status_cls = p.get("status", "open")
        pr_rows += (
            f"<tr>"
            f"<td>{_esc(p.get('repo', ''))}</td>"
            f'<td><a href="{_esc(p.get("pr_url", "#"))}" '
            f'target="_blank">#{p.get("pr_number", 0)}</a></td>'
            f"<td>{_esc(p.get('title', ''))}</td>"
            f'<td><span class="badge {status_cls}">'
            f"{status_cls}</span></td>"
            f"<td>{p.get('type', '-')}</td>"
            f"</tr>"
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ContribAI Dashboard</title>
<style>
:root {{
  --bg: #0f172a; --surface: #1e293b; --border: #334155;
  --text: #e2e8f0; --muted: #94a3b8; --accent: #38bdf8;
  --green: #22c55e; --amber: #f59e0b; --red: #ef4444;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg); color: var(--text);
  min-height: 100vh;
}}
.container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
h1 {{
  font-size: 1.75rem; margin-bottom: 2rem;
  background: linear-gradient(135deg, var(--accent), #a78bfa);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
.stats {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem; margin-bottom: 2rem;
}}
.stat-card {{
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.5rem;
  transition: transform 0.2s;
}}
.stat-card:hover {{ transform: translateY(-2px); }}
.stat-card .label {{ color: var(--muted); font-size: 0.875rem; }}
.stat-card .value {{
  font-size: 2rem; font-weight: 700; margin-top: 0.25rem;
}}
.section {{
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem;
}}
.section h2 {{
  font-size: 1.125rem; margin-bottom: 1rem;
  color: var(--accent);
}}
table {{ width: 100%; border-collapse: collapse; }}
th, td {{
  padding: 0.75rem 1rem; text-align: left;
  border-bottom: 1px solid var(--border);
}}
th {{ color: var(--muted); font-size: 0.75rem; text-transform: uppercase; }}
td {{ font-size: 0.875rem; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.badge {{
  display: inline-block; padding: 0.25rem 0.5rem;
  border-radius: 6px; font-size: 0.75rem; font-weight: 600;
}}
.badge.open {{ background: #164e63; color: var(--accent); }}
.badge.merged {{ background: #14532d; color: var(--green); }}
.badge.closed {{ background: #451a03; color: var(--amber); }}
.actions {{ margin-bottom: 2rem; display: flex; gap: 0.5rem; }}
.btn {{
  padding: 0.5rem 1rem; border: none; border-radius: 8px;
  font-size: 0.875rem; cursor: pointer; font-weight: 600;
  transition: opacity 0.2s;
}}
.btn:hover {{ opacity: 0.85; }}
.btn-primary {{ background: var(--accent); color: var(--bg); }}
.btn-secondary {{ background: var(--border); color: var(--text); }}
#status {{ color: var(--muted); font-size: 0.875rem; margin-left: 1rem; }}
</style>
</head>
<body>
<div class="container">
  <h1>ContribAI Dashboard</h1>

  <div class="stats">
    <div class="stat-card">
      <div class="label">Repos Analyzed</div>
      <div class="value">{stats.get("total_repos_analyzed", 0)}</div>
    </div>
    <div class="stat-card">
      <div class="label">PRs Submitted</div>
      <div class="value">{stats.get("total_prs_submitted", 0)}</div>
    </div>
    <div class="stat-card">
      <div class="label">PRs Merged</div>
      <div class="value">{stats.get("prs_merged", 0)}</div>
    </div>
    <div class="stat-card">
      <div class="label">Total Runs</div>
      <div class="value">{stats.get("total_runs", 0)}</div>
    </div>
  </div>

  <div class="actions">
    <button class="btn btn-primary" onclick="triggerRun(false)">
      Run Pipeline
    </button>
    <button class="btn btn-secondary" onclick="triggerRun(true)">
      Dry Run
    </button>
    <span id="status"></span>
  </div>

  <div class="section">
    <h2>Recent PRs</h2>
    <table>
      <thead>
        <tr><th>Repo</th><th>PR</th><th>Title</th>
            <th>Status</th><th>Type</th></tr>
      </thead>
      <tbody>{pr_rows if pr_rows else no_prs}</tbody>
    </table>
  </div>

  <div class="section">
    <h2>Analyzed Repos</h2>
    <table>
      <thead>
        <tr><th>Repository</th><th>Language</th><th>Stars</th>
            <th>Findings</th><th>Analyzed</th></tr>
      </thead>
      <tbody>{repo_rows if repo_rows else no_repos}</tbody>
    </table>
  </div>
</div>

<script>
async function triggerRun(dryRun) {{
  const el = document.getElementById('status');
  el.textContent = 'Starting...';
  try {{
    const res = await fetch('/api/run', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{dry_run: dryRun}})
    }});
    const data = await res.json();
    el.textContent = dryRun ? 'Dry run started' : 'Pipeline started';
    setTimeout(() => el.textContent = '', 5000);
  }} catch (e) {{
    el.textContent = 'Error: ' + e.message;
  }}
}}
</script>
</body>
</html>"""


def _esc(text: str) -> str:
    """Escape HTML special characters."""
    return (
        text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    )

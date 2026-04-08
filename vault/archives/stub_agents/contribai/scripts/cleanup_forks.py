"""
Fork Cleanup Script for ContribAI
Lists all forks, checks PR status, and deletes forks that are safe to remove.

Safe to delete: forks where all associated PRs are merged or closed.
NOT safe: forks with open PRs (deleting would break them).
"""

import subprocess

import httpx

token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
}


def get_all_forks():
    """Get all forked repos from the authenticated user."""
    forks = []
    page = 1
    while True:
        r = httpx.get(
            "https://api.github.com/user/repos",
            headers=headers,
            params={"type": "forks", "per_page": 100, "page": page},
            timeout=30,
        )
        data = r.json()
        if not data:
            break
        forks.extend(data)
        page += 1
    return forks


def get_prs_from_fork(fork_owner, parent_owner, parent_name):
    """Get all PRs from this fork to the parent repo."""
    try:
        r = httpx.get(
            f"https://api.github.com/repos/{parent_owner}/{parent_name}/pulls",
            headers=headers,
            params={"state": "all", "head": f"{fork_owner}:", "per_page": 100},
            timeout=30,
        )
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return []


def main():
    print("🔍 Fetching all forks...\n")
    forks = get_all_forks()

    if not forks:
        print("No forks found!")
        return

    print(f"Found {len(forks)} fork(s)\n")
    print("=" * 80)

    safe_to_delete = []
    has_open_prs = []
    no_prs = []

    for fork in forks:
        fork_full = fork["full_name"]
        fork_owner = fork["owner"]["login"]

        # Fetch detailed repo info to get parent
        try:
            detail = httpx.get(
                f"https://api.github.com/repos/{fork_full}",
                headers=headers,
                timeout=30,
            ).json()
            parent = detail.get("parent", {})
        except Exception:
            parent = {}

        parent_owner = parent.get("owner", {}).get("login", "?")
        parent_name = parent.get("name", "?")
        parent_full = f"{parent_owner}/{parent_name}"

        print(f"\n📁 {fork_full} (fork of {parent_full})")

        if not parent or parent_owner == "?":
            print("   ⚠️  No parent info, skipping")
            continue

        prs = get_prs_from_fork(fork_owner, parent_owner, parent_name)

        if not prs:
            print("   📭 No PRs found")
            no_prs.append({"fork": fork_full, "parent": parent_full})
        else:
            open_prs = [p for p in prs if p["state"] == "open"]
            merged_prs = [p for p in prs if p.get("merged_at")]
            closed_prs = [p for p in prs if p["state"] == "closed" and not p.get("merged_at")]

            for p in prs:
                if p.get("merged_at"):
                    state = "🟢 merged"
                elif p["state"] == "open":
                    state = "🟡 open"
                else:
                    state = "🔴 closed"
                print(f"   PR #{p['number']}: {p['title'][:60]} [{state}]")

            if open_prs:
                print(f"   ⚠️  {len(open_prs)} open PR(s) — DO NOT DELETE")
                has_open_prs.append(
                    {"fork": fork_full, "parent": parent_full, "open": len(open_prs)}
                )
            else:
                print(
                    f"   ✅ All PRs resolved ({len(merged_prs)} merged, {len(closed_prs)} closed)"
                )
                safe_to_delete.append({"fork": fork_full, "parent": parent_full})

    # Summary
    print("\n" + "=" * 80)
    print("\n📊 SUMMARY\n")

    if has_open_prs:
        print(f"⚠️  {len(has_open_prs)} fork(s) with OPEN PRs (keep these):")
        for f in has_open_prs:
            print(f"   - {f['fork']} → {f['parent']} ({f['open']} open)")

    deletable = safe_to_delete + no_prs
    if deletable:
        print(f"\n✅ {len(deletable)} fork(s) safe to delete:")
        for f in deletable:
            print(f"   - {f['fork']} → {f['parent']}")

        print(f"\n🗑️  Delete {len(deletable)} fork(s)? [y/N] ", end="")
        answer = input().strip().lower()
        if answer == "y":
            for f in deletable:
                fork_name = f["fork"]
                print(f"   Deleting {fork_name}...", end=" ")
                r = httpx.delete(
                    f"https://api.github.com/repos/{fork_name}",
                    headers=headers,
                    timeout=30,
                )
                if r.status_code == 204:
                    print("✅ deleted")
                else:
                    print(f"❌ error {r.status_code}: {r.text[:100]}")
            print("\n🎉 Done!")
        else:
            print("Cancelled.")
    else:
        print("No forks to delete.")


if __name__ == "__main__":
    main()

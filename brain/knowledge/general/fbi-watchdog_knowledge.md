---
id: fbi-watchdog-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.896837
---

# KNOWLEDGE EXTRACT: fbi-watchdog
> **Extracted on:** 2026-03-30 17:36:59
> **Source:** fbi-watchdog

---

## File: `.gitignore`
```
# Environment and credentials
.env

# State files
fbi_watchdog_results.json
onion_watchdog_results.json
http_watchdog_results.json
whois_watchdog_results.json
ip_watchdog_results.json
event_feed.json

# Monitored sites (user-specific)
monitored_sites.json

# Screenshots
screenshots/

# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.venv/
venv/
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `env.example`
```
# FBI Watchdog - Environment Configuration
# Copy this file to .env and fill in your values:
#   cp .env.example .env
#   chmod 600 .env
#
# All notification channels are optional. Configure Discord, Telegram,
# both, or neither. Without any configured, alerts appear in console
# and event feed only.

# Discord webhook URL (optional)
# Create one in Discord: Server Settings > Integrations > Webhooks
WEBHOOKFBIWATCHDOG=

# Telegram bot token (optional)
# Create a bot via @BotFather on Telegram
TELEGRAM_BOT_TOKEN=

# Telegram chat or channel ID (optional)
# Use @userinfobot or @getidsbot to find your chat ID
TELEGRAM_CHAT_ID=

# SOCKS5 proxy for clearnet requests (optional)
# Routes HTTP, WHOIS, and screenshot requests through the proxy
# Can also be set via --proxy CLI flag
CLEARNET_PROXY=
```

## File: `fbi_watchdog.py`
```python
import sys
import os
import time
import json
import signal
import hashlib
import argparse
import tempfile
import random
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

import dns.resolver
import requests
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from rich.console import Console
from rich.padding import Padding

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import logging
logging.getLogger("whois").setLevel(logging.CRITICAL)
logging.getLogger("whois.whois").setLevel(logging.CRITICAL)


console = Console()

VERSION = "3.0.0"
STATE_FILE = Path("fbi_watchdog_results.json")
ONION_STATE_FILE = Path("onion_watchdog_results.json")
HTTP_STATE_FILE = Path("http_watchdog_results.json")
WHOIS_STATE_FILE = Path("whois_watchdog_results.json")
IP_STATE_FILE = Path("ip_watchdog_results.json")
SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

DNS_RECORDS = ["A", "AAAA", "CNAME", "MX", "NS", "TXT"]
DNS_TIMEOUT = 5
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0",
]

REQUEST_TIMEOUT = 15
ONION_TIMEOUT = 30
SCAN_INTERVAL = 15
DNS_DOMAIN_DELAY = 0.5
DNS_RECORD_DELAY = 0.15
ONION_SITE_DELAY = 1.0
HTTP_CONCURRENCY = 10
WHOIS_CONCURRENCY = 5
IP_CONCURRENCY = 10

TRACKED_HEADERS = [
    "server", "x-powered-by",
    "x-frame-options", "strict-transport-security", "x-content-type-options", "x-xss-protection",
    "via", "x-cdn", "x-origin-server",
]

WHOIS_SEIZURE_INDICATORS = [
    "department of justice", "u.s. government", "united states government",
    "law enforcement", "seized", "europol", "interpol",
    "national crime agency", "fbi", "ice homeland security",
    "markmonitor", "namecheap special", "fbi seized", "seized gov",
    "forfeiture", "usdoj", "justice gov", "usssdomainseizure",
]

WHOIS_PRIVACY_ORGS = [
    "withheld for privacy", "privacy service", "whoisguard", "domains by proxy",
    "contact privacy", "redacted for privacy", "data protected",
    "privacy protect", "perfect privacy", "identity protection",
    "privacydotlink", "domain privacy",
]

REGISTRAR_ALIASES = {
    "tucows com co": "tucows",
    "tucows domains inc": "tucows",
    "tucows inc": "tucows",
    "namecheap inc": "namecheap",
    "namecheap": "namecheap",
    "godaddy com llc": "godaddy",
    "godaddy com inc": "godaddy",
    "godaddy llc": "godaddy",
    "network solutions llc": "network solutions",
    "network solutions inc": "network solutions",
    "cloudflare inc": "cloudflare",
    "cloudflare": "cloudflare",
    "porkbun llc": "porkbun",
    "porkbun inc": "porkbun",
    "gandi sas": "gandi",
    "gandi": "gandi",
    "dynadot llc": "dynadot",
    "dynadot inc": "dynadot",
    "enom llc": "enom",
    "enom inc": "enom",
    "google llc": "google",
    "google inc": "google",
    "google domains": "google",
    "squarespace domains llc": "squarespace",
    "immaterialism limited": "immaterialism",
    "immaterialism": "immaterialism",
}

SEIZURE_KEYWORDS = [
    "this hidden site has been seized", "this domain has been seized",
    "this site has been seized", "this website has been seized",
    "this website has been shut down",
    "seized by the fbi", "seized by the united states", "seized by law enforcement",
    "seized as part of a law enforcement", "department of justice",
    "seized pursuant to", "this domain name has been seized by ice",
    "warrant issued", "forfeiture order", "seized pursuant to a warrant",
    "seized by europol", "seized by interpol", "national crime agency",
    "operation conducted by", "operation conducted jointly",
    "seized by bka", "bundeskriminalamt", "politie nederland",
    "seized by afp", "australian federal police",
    "seized by garda", "an garda síochána", "seized by rcmp",
    "polisen sverige", "seized by polisen",
    "seized by the finnish", "seized by the danish",
    "law enforcement operation", "international law enforcement",
    "joint law enforcement operation",
    "this website is now under the control of", "seized and shut down",
]

CHALLENGE_KEYWORDS = [
    "checking your browser", "just a moment", "cf-challenge", "cf_chl_opt",
    "attention required", "verify you are human",
    "ddos protection by cloudflare", "please wait while we verify",
    "enable javascript and cookies", "ray id:",
    "ddos-guard", "ddosguard", "ddos protection by ddos-guard",
    "checking your connection", "please allow up to 5 seconds",
    "bot verification", "managed challenge",
    "hcaptcha", "recaptcha", "turnstile",
]

SITES_FILE = Path("monitored_sites.json")
EVENT_FEED_FILE = Path("event_feed.json")
EVENT_FEED_MAX = 500


def _atomic_write_json(filepath: Path, data: dict):
    dir_path = filepath.parent
    tmp_path = None
    try:
        fd, tmp_path = tempfile.mkstemp(dir=str(dir_path), suffix='.tmp')
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, str(filepath))
    except Exception:
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        raise


class EventFeed:
    
    def __init__(self, feed_file: Path = EVENT_FEED_FILE, site_manager=None):
        self.feed_file = feed_file
        self.site_manager = site_manager
        self.events: List[dict] = []
        self._load()
    
    def _load(self):
        try:
            if self.feed_file.exists():
                with open(self.feed_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    events = data.get("events", [])
                    if isinstance(events, list):
                        self.events = events
                        return
                self.events = []
        except Exception:
            self.events = []
    
    def _save(self):
        try:
            feed = {
                "feed_version": "1.0",
                "generator": f"FBI Watchdog v{VERSION}",
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "event_count": len(self.events),
                "events": self.events
            }
            if self.site_manager:
                feed["total_monitored"] = {
                    "clearnet": len(self.site_manager.domains),
                    "onion": len(self.site_manager.onion_sites)
                }
            _atomic_write_json(self.feed_file, feed)
        except Exception:
            pass
    
    def add_event(self, event_type: str, domain: str, details: dict):
        event = {
            **details,
            "id": secrets.token_hex(8),
            "type": event_type,
            "domain": domain,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        
        self.events.insert(0, event)
        
        if len(self.events) > EVENT_FEED_MAX:
            self.events = self.events[:EVENT_FEED_MAX]
        
        self._save()


class SiteManager:
    
    def __init__(self, sites_file: Path = SITES_FILE):
        self.sites_file = sites_file
        self.domains: List[str] = []
        self.onion_sites: List[str] = []
        self._load()
    
    def _load(self):
        if self.sites_file.exists():
            try:
                with open(self.sites_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if not isinstance(data, dict):
                    raise ValueError("Invalid sites file format")
                domains = data.get("domains", [])
                onion_sites = data.get("onion_sites", [])
                if not isinstance(domains, list) or not isinstance(onion_sites, list):
                    raise ValueError("Invalid sites file format")
                self.domains = [d for d in domains if isinstance(d, str)]
                self.onion_sites = [o for o in onion_sites if isinstance(o, str)]
                return
            except Exception:
                pass
        
        self.domains = []
        self.onion_sites = []
        self._save()
        console.print(Padding(
            f"[bold yellow]→ Created empty {self.sites_file} - add sites via menu or --add flag[/bold yellow]",
            (0, 0, 0, 4)
        ))
    
    def _save(self):
        try:
            _atomic_write_json(self.sites_file, {
                "domains": self.domains,
                "onion_sites": self.onion_sites
            })
        except Exception:
            pass
    
    @staticmethod
    def _clean_site(site: str) -> str:
        site = site.strip().lower()
        for prefix in ["http://", "https://", "www."]:
            if site.startswith(prefix):
                site = site[len(prefix):]
        site = site.rstrip("/")
        if not re.match(r'^[a-z0-9][a-z0-9.\-]{1,253}[a-z0-9]$', site):
            return ""
        if '..' in site:
            return ""
        return site
    
    def add_site(self, site: str) -> Tuple[str, bool]:
        site = self._clean_site(site)
        if not site:
            return ("invalid", False)
        
        if site.endswith(".onion"):
            if site in self.onion_sites:
                return ("onion", False)
            self.onion_sites.insert(0, site)
            self._save()
            return ("onion", True)
        else:
            if site in self.domains:
                return ("clearnet", False)
            self.domains.insert(0, site)
            self._save()
            return ("clearnet", True)
    
    def remove_site(self, site: str) -> Tuple[str, bool]:
        site = self._clean_site(site)
        if not site:
            return ("invalid", False)
        
        if site.endswith(".onion"):
            if site not in self.onion_sites:
                return ("onion", False)
            self.onion_sites.remove(site)
            self._save()
            return ("onion", True)
        else:
            if site not in self.domains:
                return ("clearnet", False)
            self.domains.remove(site)
            self._save()
            return ("clearnet", True)
    
    def reload(self) -> Tuple[int, int]:
        """Re-read monitored_sites.json and update lists in-place so global
        references (DOMAINS, ONION_SITES) stay valid without reassignment."""
        if not self.sites_file.exists():
            return (0, 0)
        try:
            with open(self.sites_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if not isinstance(data, dict):
                return (len(self.domains), len(self.onion_sites))
            new_domains = [self._clean_site(d) for d in data.get("domains", []) if isinstance(d, str)]
            new_onion = [self._clean_site(o) for o in data.get("onion_sites", []) if isinstance(o, str)]
            new_domains = [d for d in new_domains if d]
            new_onion = [o for o in new_onion if o]
            self.domains[:] = new_domains
            self.onion_sites[:] = new_onion
            return (len(self.domains), len(self.onion_sites))
        except Exception:
            return (len(self.domains), len(self.onion_sites))


site_manager = SiteManager()
DOMAINS = site_manager.domains
ONION_SITES = site_manager.onion_sites


class DWIConfig:
    def __init__(self):
        load_dotenv()
        
        env_path = Path(".env")
        if env_path.exists():
            env_stat = env_path.stat()
            if env_stat.st_mode & 0o077:
                console.print(Padding(
                    "[bold red]→ WARNING: .env file is readable by other users. Run: chmod 600 .env[/bold red]",
                    (0, 0, 0, 4)
                ))
        
        self.webhook_url = os.getenv("WEBHOOKFBIWATCHDOG")
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.clearnet_proxy = os.getenv("CLEARNET_PROXY")
        
        self.validate()
    
    def validate(self):
        if self.webhook_url and not self.webhook_url.startswith("https://discord.com/api/webhooks/"):
            console.print(Padding(
                "[red]→ WEBHOOKFBIWATCHDOG must be a valid Discord webhook URL (https://discord.com/api/webhooks/...)[/red]",
                (0, 0, 0, 4)
            ))
            sys.exit(1)
        
        if not self.webhook_url:
            console.print(Padding(
                "[yellow]→ Discord webhook not configured - Discord notifications will be skipped[/yellow]",
                (0, 0, 0, 4)
            ))
        
        self.proxy_ip = None
        self.real_ip = None
        if self.clearnet_proxy:
            if not re.match(r'^socks5h?://([\w.\-]+:[\w.\-]+@)?[\w.\-]+:\d+$', self.clearnet_proxy):
                console.print(Padding(
                    "[red]→ CLEARNET_PROXY must be a valid SOCKS5 URL (e.g. socks5h://127.0.0.1:1080)[/red]",
                    (0, 0, 0, 4)
                ))
                sys.exit(1)
            
            console.print(Padding(
                f"[bold cyan]→ Testing proxy connection...[/bold cyan]",
                (0, 0, 0, 4)
            ))
            proxy_dict = {"http": self.clearnet_proxy, "https": self.clearnet_proxy}
            try:
                console.print(Padding(
                    "[dim]    Checking proxy exit IP...[/dim]",
                    (0, 0, 0, 4)
                ))
                proxy_resp = requests.get(
                    "https://api.ipify.org?format=json",
                    proxies=proxy_dict, timeout=10
                )
                self.proxy_ip = proxy_resp.json().get("ip", "unknown")
                
                console.print(Padding(
                    "[dim]    Checking real IP...[/dim]",
                    (0, 0, 0, 4)
                ))
                real_resp = requests.get(
                    "https://api.ipify.org?format=json",
                    timeout=10
                )
                self.real_ip = real_resp.json().get("ip", "unknown")
                
                if self.proxy_ip == self.real_ip:
                    console.print(Padding(
                        f"[bold yellow]⚠ Proxy IP matches real IP ({self.proxy_ip}) - proxy may not be working[/bold yellow]",
                        (0, 0, 0, 4)
                    ))
            except Exception as e:
                console.print(Padding(
                    f"[bold red]✗ Proxy test failed: {str(e)[:60]}[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    "[bold red]  Check that your proxy is running and the address is correct[/bold red]",
                    (0, 0, 0, 4)
                ))
                sys.exit(1)

        if not self.telegram_bot_token or not self.telegram_chat_id:
            console.print(Padding(
                "[yellow]→ Telegram credentials not configured - Telegram notifications will be skipped[/yellow]",
                (0, 0, 0, 4)
            ))
        else:
            if not re.match(r'^\d+:[A-Za-z0-9_\-]+$', self.telegram_bot_token):
                console.print(Padding(
                    "[red]→ TELEGRAM_BOT_TOKEN has invalid format[/red]",
                    (0, 0, 0, 4)
                ))
                self.telegram_bot_token = None
            if self.telegram_chat_id and not re.match(r'^-?\d+$', self.telegram_chat_id):
                console.print(Padding(
                    "[red]→ TELEGRAM_CHAT_ID has invalid format[/red]",
                    (0, 0, 0, 4)
                ))
                self.telegram_chat_id = None
        
        has_discord = bool(self.webhook_url)
        has_telegram = bool(self.telegram_bot_token and self.telegram_chat_id)
        if not has_discord and not has_telegram:
            console.print(Padding(
                "[bold yellow]⚠ No notification channels configured - alerts will only appear in console and event feed[/bold yellow]",
                (0, 0, 0, 4)
            ))


class StateManager:
    
    def __init__(self, state_file: Path):
        self.state_file = state_file
        self.data: Dict = {}
    
    def load(self) -> Dict:
        try:
            if self.state_file.exists():
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                if not isinstance(loaded, dict):
                    self.data = {}
                else:
                    self.data = loaded
            else:
                self.data = {}
        except json.JSONDecodeError:
            self.data = {}
        except Exception:
            self.data = {}
        return self.data
    
    def save(self):
        try:
            _atomic_write_json(self.state_file, self.data)
        except Exception:
            pass
    
    def get(self, key: str, default=None):
        return self.data.get(key, default)
    
    def set(self, key: str, value):
        self.data[key] = value


class Notifier:
    
    def __init__(self, config: DWIConfig):
        self.config = config
        self.session = requests.Session()
        self.session.max_redirects = 5
        self.session.headers.update({"User-Agent": random.choice(USER_AGENTS)})
    
    def _send_request(self, url: str, data: dict = None, use_tor: bool = False) -> Optional[str]:
        proxies = None
        if use_tor:
            proxies = {
                "http": "socks5h://127.0.0.1:9050",
                "https": "socks5h://127.0.0.1:9050"
            }
        
        try:
            if data:
                response = self.session.post(url, json=data, proxies=proxies, 
                                             timeout=REQUEST_TIMEOUT)
            else:
                response = self.session.get(url, proxies=proxies, 
                                            timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.text
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.ProxyError:
            pass
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.RequestException:
            pass
        return None
    
    def notify_telegram(self, domain: str, record_type: str, records: List[str], 
                       previous_records: List[str], seizure_capture: str = None):
        if not self.config.telegram_bot_token or not self.config.telegram_chat_id:
            return

        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        
        prev_fmt = "\n".join(previous_records) if previous_records else "None"
        new_fmt = "\n".join(records) if records else "None"
        
        message = (
            f"⚠️ *FBI Watchdog - {record_type}* ⚠️\n"
            "🔗 *DarkWebInformer.com - Cyber Threat Intelligence*\n\n"
            f"*Domain:* {domain}\n"
            f"*Record Type:* {record_type}\n"
            f"*Time Detected:* {ts}\n\n"
            f"*Previous Records:*\n```\n{prev_fmt}\n```\n"
            f"*New Records:*\n```\n{new_fmt}\n```"
        )
        
        if seizure_capture and Path(seizure_capture).exists():
            try:
                cap = message[:1024] if len(message) > 1024 else message
                
                tg_url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendPhoto"
                with open(seizure_capture, 'rb') as photo:
                    resp = self.session.post(
                        tg_url,
                        data={
                            "chat_id": self.config.telegram_chat_id,
                            "caption": cap,
                            "parse_mode": "Markdown"
                        },
                        files={"photo": photo},
                        timeout=REQUEST_TIMEOUT,
                    )
                    resp.raise_for_status()
                    return
            except Exception:
                pass
        
        self._send_request(
            f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendMessage",
            data={"chat_id": self.config.telegram_chat_id, "text": message[:4096], "parse_mode": "Markdown"}
        )
    
    def notify_discord(self, domain: str, record_type: str, records: List[str], 
                      prev_records: List[str], screenshot_path: str = None):
        if not self.config.webhook_url:
            return
        ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        
        prev_fmt = '\n'.join(prev_records) if prev_records else 'None'
        new_fmt = '\n'.join(records) if records else 'None'
        
        fields = [
            {"name": "Domain", "value": f"`{domain}`", "inline": True},
            {"name": "Record Type", "value": f"`{record_type}`", "inline": True},
            {"name": "Previous Records", "value": f"```\n{prev_fmt}\n```", "inline": False},
            {"name": "New Records", "value": f"```\n{new_fmt}\n```", "inline": False},
        ]
        
        if len(records) > 1:
            fields.append({"name": "Records Changed", "value": str(len(records)), "inline": True})
        
        embed = {
            "title": f"⚠️ FBI Watchdog - {record_type} ⚠️",
            "description": "🔗 **DarkWebInformer.com - Cyber Threat Intelligence**",
            "fields": fields,
            "color": 16711680,
            "footer": {"text": f"FBI Watchdog v{VERSION} • {ts}"},
        }
        
        if screenshot_path and Path(screenshot_path).exists():
            try:
                embed["image"] = {"url": "attachment://seizure.png"}
                payload = {"embeds": [embed]}
                
                with open(screenshot_path, 'rb') as img:
                    files = {
                        "file": ("seizure.png", img, "image/png")
                    }
                    response = self.session.post(
                        self.config.webhook_url,
                        data={"payload_json": json.dumps(payload)},
                        files=files,
                        timeout=REQUEST_TIMEOUT,
                    )
                    response.raise_for_status()
                    return
            except Exception:
                pass
        
        self._send_request(self.config.webhook_url, data={"embeds": [embed]})
    
    def notify_seizure_escalation_telegram(self, domain: str, evidence: dict, 
                                            seizure_capture: str = None):
        if not self.config.telegram_bot_token or not self.config.telegram_chat_id:
            return
        
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        trigger = evidence.get("trigger", "Unknown")
        
        sections = [
            "🚨 *FBI Watchdog - SEIZURE ESCALATION ALERT* 🚨",
            "🔗 *DarkWebInformer.com - Cyber Threat Intelligence*\n",
            f"*Domain:* `{domain}`",
            f"*Triggered By:* {trigger}",
            f"*Time Detected:* {ts}\n",
        ]
        
        http_ev = evidence.get("http", {})
        if http_ev:
            http_lines = []
            for item in http_ev.get("changes", []):
                http_lines.append(f"  {item}")
            if http_lines:
                sections.append("*🔍 HTTP Fingerprint Changes:*")
                sections.append("```\n" + "\n".join(http_lines) + "\n```")
        
        whois_ev = evidence.get("whois", {})
        if whois_ev:
            whois_lines = []
            for item in whois_ev.get("changes", []):
                whois_lines.append(f"  {item}")
            indicators = whois_ev.get("seizure_indicators", [])
            if whois_lines:
                sections.append("*📋 WHOIS Changes:*")
                sections.append("```\n" + "\n".join(whois_lines) + "\n```")
            if indicators:
                sections.append(f"*⚠️ Seizure Indicators:* {', '.join(indicators)}")
        
        dns_ev = evidence.get("dns", {})
        if dns_ev:
            dns_lines = []
            for rtype, info in dns_ev.items():
                prev = ", ".join(info.get("previous", [])) or "None"
                curr = ", ".join(info.get("current", [])) or "None"
                dns_lines.append(f"  {rtype}: {prev} → {curr}")
            if dns_lines:
                sections.append("*🌐 DNS Records:*")
                sections.append("```\n" + "\n".join(dns_lines) + "\n```")
        
        msg = "\n".join(sections)
        
        if seizure_capture and Path(seizure_capture).exists():
            try:
                cap = msg[:1024] if len(msg) > 1024 else msg
                tg_url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendPhoto"
                with open(seizure_capture, 'rb') as photo:
                    resp = self.session.post(
                        tg_url,
                        data={
                            "chat_id": self.config.telegram_chat_id,
                            "caption": cap,
                            "parse_mode": "Markdown"
                        },
                        files={"photo": photo},
                        timeout=REQUEST_TIMEOUT,
                    )
                    resp.raise_for_status()
                    return
            except Exception:
                pass
        
        self._send_request(
            f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendMessage",
            data={"chat_id": self.config.telegram_chat_id, "text": msg[:4096], "parse_mode": "Markdown"}
        )
    
    def notify_seizure_escalation_discord(self, domain: str, evidence: dict,
                                           screenshot_path: str = None):
        if not self.config.webhook_url:
            return
        ts = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        trigger = evidence.get("trigger", "Unknown")
        
        fields = [
            {"name": "Domain", "value": f"`{domain}`", "inline": True},
            {"name": "Triggered By", "value": f"`{trigger}`", "inline": True},
        ]
        
        http_ev = evidence.get("http", {})
        if http_ev:
            lines = [f"  {item}" for item in http_ev.get("changes", [])]
            if lines:
                fields.append({"name": "🔍 HTTP Fingerprint Changes", "value": "```\n" + "\n".join(lines) + "\n```", "inline": False})
        
        whois_ev = evidence.get("whois", {})
        if whois_ev:
            wlines = [f"  {item}" for item in whois_ev.get("changes", [])]
            indicators = whois_ev.get("seizure_indicators", [])
            if wlines:
                fields.append({"name": "📋 WHOIS Changes", "value": "```\n" + "\n".join(wlines) + "\n```", "inline": False})
            if indicators:
                fields.append({"name": "⚠️ Seizure Indicators", "value": ", ".join(indicators), "inline": False})
        
        dns_ev = evidence.get("dns", {})
        if dns_ev:
            dlines = []
            for rtype, info in dns_ev.items():
                prev = ", ".join(info.get("previous", [])) or "None"
                curr = ", ".join(info.get("current", [])) or "None"
                dlines.append(f"  {rtype}: {prev} → {curr}")
            if dlines:
                fields.append({"name": "🌐 DNS Records", "value": "```\n" + "\n".join(dlines) + "\n```", "inline": False})
        
        evidence_sources = sum(1 for k in ("http", "whois", "dns") if evidence.get(k))
        
        embed = {
            "title": "🚨 FBI Watchdog - SEIZURE ESCALATION ALERT 🚨",
            "description": f"🔗 **DarkWebInformer.com - Cyber Threat Intelligence**\nCorroborated across **{evidence_sources}** monitor(s)",
            "fields": fields,
            "color": 16711680,
            "footer": {"text": f"FBI Watchdog v{VERSION} • {ts}"},
        }
        
        if screenshot_path and Path(screenshot_path).exists():
            try:
                embed["image"] = {"url": "attachment://seizure.png"}
                payload = {"embeds": [embed]}
                with open(screenshot_path, 'rb') as img:
                    files = {"file": ("seizure.png", img, "image/png")}
                    response = self.session.post(
                        self.config.webhook_url,
                        data={"payload_json": json.dumps(payload)},
                        files=files,
                        timeout=REQUEST_TIMEOUT,
                    )
                    response.raise_for_status()
                    return
            except Exception:
                pass
        
        self._send_request(self.config.webhook_url, data={"embeds": [embed]})


class TorChecker:
    
    TOR_CHECK_TTL = 300
    TOR_CONTROL_PORT = 9051
    
    def __init__(self):
        self.is_running = False
        self.ports = [9050, 9150]
        self._last_check_time = 0
    
    def renew_circuit(self) -> bool:
        """Send NEWNYM signal to Tor control port to get a fresh circuit."""
        import socket
        try:
            with socket.create_connection(('127.0.0.1', self.TOR_CONTROL_PORT), timeout=5) as sock:
                sock.sendall(b'AUTHENTICATE ""\r\n')
                resp = sock.recv(256)
                if b'250' not in resp:
                    return False
                sock.sendall(b'SIGNAL NEWNYM\r\n')
                resp = sock.recv(256)
                return b'250' in resp
        except Exception:
            return False
    
    def check(self) -> bool:
        if self.is_running and (time.time() - self._last_check_time < self.TOR_CHECK_TTL):
            return True
        
        for port in self.ports:
            try:
                proxies = {
                    "http": f"socks5h://127.0.0.1:{port}",
                    "https": f"socks5h://127.0.0.1:{port}"
                }
                response = requests.get(
                    "https://check.torproject.org/",
                    proxies=proxies,
                    timeout=10
                )
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                
                if "Congratulations" in soup.get_text(" ", strip=True):
                    self.is_running = True
                    self._last_check_time = time.time()
                    return True
            except requests.exceptions.RequestException:
                continue
        
        self.is_running = False
        return False


class DWIScreenshot:
    
    @classmethod
    def capture(cls, url: str, use_tor: bool = False, proxy_url: str = None) -> Optional[Path]:
        domain = url.replace("http://", "").replace("https://", "")
        safe_domain = re.sub(r'[^a-zA-Z0-9._\-]', '_', domain)[:200]
        screenshot_path = SCREENSHOT_DIR / f"{safe_domain}_seizure.png"
        
        if not screenshot_path.resolve().parent == SCREENSHOT_DIR.resolve():
            console.print(Padding(
                f"[bold red]  ✗ Invalid screenshot path for: {domain[:60]}[/bold red]",
                (0, 0, 0, 6)
            ))
            return None
        
        
        try:
            with sync_playwright() as p:
                launch_args = ["--no-sandbox"]
                
                proxy_settings = None
                if use_tor:
                    proxy_settings = {"server": "socks5://127.0.0.1:9050"}
                elif proxy_url:
                    proxy_match = re.match(
                        r'^(socks5h?)://(?:([^:]+):([^@]+)@)?(.+)$', proxy_url
                    )
                    if proxy_match:
                        scheme, username, password, host_port = proxy_match.groups()
                        proxy_settings = {"server": f"socks5://{host_port}"}
                        if username and password:
                            proxy_settings["username"] = username
                            proxy_settings["password"] = password
                    else:
                        proxy_settings = {"server": proxy_url}
                
                try:
                    browser = p.chromium.launch(
                        headless=True,
                        args=launch_args,
                        proxy=proxy_settings
                    )
                except Exception as proxy_err:
                    if proxy_settings and "authentication" in str(proxy_err).lower():
                        console.print(Padding(
                            "[bold yellow]  ⚠ Proxy auth not supported for screenshots - falling back to direct[/bold yellow]",
                            (0, 0, 0, 6)
                        ))
                        browser = p.chromium.launch(
                            headless=True,
                            args=launch_args
                        )
                    else:
                        raise
                
                context = browser.new_context(
                    viewport={"width": 1920, "height": 1080},
                    ignore_https_errors=use_tor,
                    accept_downloads=False,
                    java_script_enabled=False
                )
                
                page = context.new_page()
                
                full_url = url if url.startswith("http") else f"http://{url}"
                
                try:
                    page.goto(full_url, timeout=60000, wait_until="load")
                    page.wait_for_timeout(3000)
                except PlaywrightTimeout:
                    pass
                except Exception:
                    pass
                
                page.screenshot(path=str(screenshot_path), full_page=True)
                
                context.close()
                browser.close()
                
                console.print(Padding(
                    f"[bold green]  ✓ Screenshot saved: {screenshot_path.name}[/bold green]",
                    (0, 0, 0, 6)
                ))
                return screenshot_path
                
        except Exception as e:
            err_msg = re.sub(r'://[^:]+:[^@]+@', '://***:***@', str(e))
            console.print(Padding(
                f"[bold yellow]  ⚠ Screenshot capture failed: {err_msg[:80]}[/bold yellow]",
                (0, 0, 0, 6)
            ))
        
        return None


class EscalationEngine:
    
    def __init__(self, dns_state: StateManager, notifier: 'Notifier', 
                 event_feed: EventFeed = None, proxy_url: str = None):
        self.dns_state = dns_state
        self.notifier = notifier
        self.event_feed = event_feed
        self.proxy_url = proxy_url
    
    def _quick_dns_check(self, domain: str) -> dict:
        evidence = {}
        sei_indicators = ['fbi.seized', 'seized.gov', 'europol', 'interpol', 'seized',
                          'forfeiture', 'usdoj', 'justice.gov', 'usssdomainseizure']
        
        for rtype in DNS_RECORDS:
            try:
                answers = dns.resolver.resolve(domain, rtype, lifetime=DNS_TIMEOUT)
                current = sorted([r.to_text() for r in answers])
            except Exception:
                current = []
            
            dstate = self.dns_state.get(domain, {})
            rstate = dstate.get(rtype, {})
            if isinstance(rstate, dict):
                hist = rstate.get("history", [])
                prev = hist[-1] if hist else []
            else:
                prev = []
            
            rstr = str(current).lower()
            hits = [ind for ind in sei_indicators if ind in rstr]
            
            if current != prev or hits:
                entry = {"previous": prev, "current": current}
                if hits:
                    entry["seizure_indicators"] = hits
                evidence[rtype] = entry
            
            time.sleep(DNS_RECORD_DELAY)
        
        return evidence
    
    def escalate(self, domain: str, trigger: str, http_evidence: dict = None,
                 whois_evidence: dict = None):
        console.print("")
        console.print(Padding("█" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold red]🚨 SEIZURE ESCALATION - FULL DOMAIN AUDIT 🚨[/bold red]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold yellow]Domain: {domain}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold yellow]Triggered by: {trigger}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding("█" * 80, (0, 0, 0, 4)))
        console.print("")
        
        console.print(Padding(
            "[bold cyan]→ Step 1/3: Running immediate DNS audit...[/bold cyan]",
            (0, 0, 0, 4)
        ))
        dns_evidence = self._quick_dns_check(domain)
        
        if dns_evidence:
            dns_seizure_found = any(
                "seizure_indicators" in info for info in dns_evidence.values()
            )
            if dns_seizure_found:
                console.print(Padding(
                    f"[bold red]  🚨 DNS SEIZURE RECORDS FOUND across {len(dns_evidence)} record type(s)[/bold red]",
                    (0, 0, 0, 4)
                ))
            else:
                console.print(Padding(
                    f"[bold red]  DNS changes found across {len(dns_evidence)} record type(s)[/bold red]",
                    (0, 0, 0, 4)
                ))
            for rtype, info in dns_evidence.items():
                prev = ", ".join(info["previous"]) or "None"
                curr = ", ".join(info["current"]) or "None"
                indicators = info.get("seizure_indicators", [])
                indicator_str = f"  ← SEIZURE: {', '.join(indicators)}" if indicators else ""
                console.print(Padding(
                    f"[bold white]    {rtype}: {prev} → {curr}{indicator_str}[/bold white]",
                    (0, 0, 0, 4)
                ))
        else:
            console.print(Padding(
                "[bold green]  No DNS changes detected (yet - may propagate later)[/bold green]",
                (0, 0, 0, 4)
            ))
        
        console.print(Padding(
            "[bold cyan]→ Step 2/3: Capturing screenshot...[/bold cyan]",
            (0, 0, 0, 4)
        ))
        screenshot_path = DWIScreenshot.capture(domain, use_tor=False, proxy_url=self.proxy_url)
        screenshot_str = str(screenshot_path) if screenshot_path else None
        
        console.print(Padding(
            "[bold cyan]→ Step 3/3: Sending consolidated seizure alert...[/bold cyan]",
            (0, 0, 0, 4)
        ))
        
        evidence = {
            "trigger": trigger,
            "http": http_evidence or {},
            "whois": whois_evidence or {},
            "dns": dns_evidence,
        }
        
        self.notifier.notify_seizure_escalation_discord(
            domain, evidence, screenshot_path=screenshot_str
        )
        self.notifier.notify_seizure_escalation_telegram(
            domain, evidence, seizure_capture=screenshot_str
        )
        
        if self.event_feed:
            self.event_feed.add_event("seizure_escalation", domain, {
                "trigger": trigger,
                "http_evidence": http_evidence,
                "whois_evidence": whois_evidence,
                "dns_changes": {k: v for k, v in dns_evidence.items()},
                "screenshot": screenshot_str,
                "site_type": "clearnet"
            })
        
        console.print("")
        console.print(Padding("█" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            "[bold green]✓ Seizure escalation complete - all evidence bundled and sent[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print(Padding("█" * 80, (0, 0, 0, 4)))
        console.print("")


class OnionMonitor:
    
    def __init__(self, state_manager: StateManager, tor_checker: TorChecker, 
                 notifier: Notifier, event_feed: EventFeed = None):
        self.state = state_manager
        self.tor = tor_checker
        self.notifier = notifier
        self.event_feed = event_feed
        self.silent = False
    
    def check_site(self, onion_url: str) -> bool:
        if not self.tor.check():
            return False
        
        proxies = {
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050"
        }
        
        last_status = self.state.get(onion_url, {}).get("status", "unknown")
        is_first_run = (last_status == "unknown")
        
        console.print(Padding(
            f"  [bold cyan]→ Connecting via Tor...[/bold cyan]",
            (0, 0, 0, 6)
        ))
        
        try:
            url = onion_url if onion_url.startswith("http") else f"http://{onion_url}"
            response = requests.get(url, proxies=proxies, timeout=ONION_TIMEOUT, 
                                   stream=True)
            max_size = 5 * 1024 * 1024
            chunks = []
            bytes_read = 0
            for chunk in response.iter_content(chunk_size=65536, decode_unicode=False):
                bytes_read += len(chunk)
                if bytes_read > max_size:
                    response.close()
                    console.print(Padding(
                        f"  [bold yellow]⚠ {onion_url} - Response too large, skipping[/bold yellow]",
                        (0, 0, 0, 6)
                    ))
                    return False
                chunks.append(chunk)
            html_content = b"".join(chunks).decode("utf-8", errors="replace").lower()
            
            is_seized = any(keyword in html_content for keyword in SEIZURE_KEYWORDS)
            new_status = "seized" if is_seized else "active"
            
            if is_first_run:
                console.print("")
                console.print(Padding("+" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    f"[bold magenta]📡 NEW ONION SITE ADDED TO MONITORING[/bold magenta]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("+" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    f"[bold yellow]Site: {onion_url}[/bold yellow]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold green]Initial Status: {new_status.upper()}[/bold green]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("+" * 80, (0, 0, 0, 4)))
                console.print("")
                
                
                self.state.set(onion_url, {
                    "status": new_status,
                    "last_checked": datetime.now(timezone.utc).isoformat()
                })
                self.state.save()
                
                if not self.silent:
                    screenshot_path = None
                    if is_seized:
                        console.print(Padding(
                            "[bold cyan]→ Capturing seizure screenshot...[/bold cyan]",
                            (0, 0, 0, 4)
                        ))
                        screenshot_path = DWIScreenshot.capture(onion_url, use_tor=True)
                    
                    console.print(Padding(
                        "[bold cyan]→ Sending new onion site notifications...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    
                    status_records = [new_status.upper()]
                    prev_status = ["NEW SITE"]
                    screenshot_str = str(screenshot_path) if screenshot_path else None
                    
                    self.notifier.notify_telegram(onion_url, "New Onion Site", status_records, prev_status, seizure_capture=screenshot_str)
                    self.notifier.notify_discord(onion_url, "New Onion Site", status_records, prev_status, screenshot_path=screenshot_str)
                    
                    if self.event_feed:
                        self.event_feed.add_event("new_onion_site", onion_url, {
                            "status": new_status,
                            "site_type": "onion",
                            "screenshot": screenshot_str
                        })
                    
                    console.print(Padding(
                        "[bold green]✓ New onion site notifications sent[/bold green]",
                        (0, 0, 0, 4)
                    ))
                    console.print("")
                else:
                    console.print(Padding(
                        "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                        (0, 0, 0, 4)
                    ))
                
                return False
            
            if last_status == new_status or (last_status == "unreachable" and new_status == "seized"):
                if last_status == "unreachable" and new_status == "seized":
                    self.state.set(onion_url, {
                        "status": new_status,
                        "last_checked": datetime.now(timezone.utc).isoformat()
                    })
                    self.state.save()
                console.print(Padding(
                    f"  [bold green]✓ {onion_url} - {new_status.capitalize()} (no change)[/bold green]",
                    (0, 0, 0, 6)
                ))

                if self.event_feed and not self.silent:
                    found_keywords = [kw for kw in SEIZURE_KEYWORDS if kw in html_content] if is_seized else []
                    self.event_feed.add_event("http_baseline", onion_url, {
                        "fingerprint": {
                            "_status_code": response.status_code,
                            "_final_url": url,
                            "_body_hash": hashlib.sha256(b"".join(chunks)).hexdigest(),
                            "_body_size": bytes_read,
                            "_scheme": "http" if url.startswith("http://") else "https",
                            "_seizure_keywords": found_keywords,
                            "_is_challenge_page": False,
                            "server": response.headers.get("server", ""),
                        },
                        "site_type": "onion"
                    })

                return False
            
            if is_seized:
                console.print("")
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    "[bold red]🚨 ONION SITE SEIZURE DETECTED! 🚨[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    f"[bold yellow]Site: {onion_url}[/bold yellow]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold red]Previous Status: Online[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold red]Current Status: SEIZED BY LAW ENFORCEMENT[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print("")
                
                
                self.state.set(onion_url, {
                    "status": new_status,
                    "last_checked": datetime.now(timezone.utc).isoformat()
                })
                self.state.save()
                
                if not self.silent:
                    console.print(Padding(
                        "[bold cyan]→ Capturing seizure screenshot...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    screenshot_path = DWIScreenshot.capture(onion_url, use_tor=True)
                    
                    console.print(Padding(
                        "[bold cyan]→ Sending seizure notifications...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    screenshot_str = str(screenshot_path) if screenshot_path else None
                    self.notifier.notify_telegram(onion_url, "Onion Seized", ["Seized"], ["Online"], seizure_capture=screenshot_str)
                    self.notifier.notify_discord(onion_url, "Onion Seized", ["Seized"], ["Online"], screenshot_path=screenshot_str)
                    
                    if self.event_feed:
                        self.event_feed.add_event("seizure", onion_url, {
                            "previous_status": "online",
                            "new_status": "seized",
                            "site_type": "onion",
                            "screenshot": screenshot_str
                        })
                    
                    console.print(Padding(
                        "[bold green]✓ Seizure notifications sent[/bold green]",
                        (0, 0, 0, 4)
                    ))
                    console.print("")
                else:
                    console.print(Padding(
                        "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                        (0, 0, 0, 4)
                    ))
            else:
                console.print(Padding(
                    f"  [bold green]✓ {onion_url} - Active[/bold green]",
                    (0, 0, 0, 6)
                ))
                self.state.set(onion_url, {
                    "status": new_status,
                    "last_checked": datetime.now(timezone.utc).isoformat()
                })
                self.state.save()
            
            return is_seized
            
        except requests.exceptions.ConnectionError:
            new_status = "unreachable"
            console.print(Padding(
                f"  [bold yellow]⚠ {onion_url} - Unreachable (Connection refused) - retrying with new circuit...[/bold yellow]",
                (0, 0, 0, 6)
            ))
            retry_result = self._retry_with_new_circuit(onion_url, proxies)
            if retry_result is not None:
                return retry_result
        except requests.exceptions.Timeout:
            new_status = "unreachable"
            console.print(Padding(
                f"  [bold yellow]⚠ {onion_url} - Timeout - retrying with new circuit...[/bold yellow]",
                (0, 0, 0, 6)
            ))
            retry_result = self._retry_with_new_circuit(onion_url, proxies)
            if retry_result is not None:
                return retry_result
        except requests.exceptions.RequestException as e:
            new_status = "unreachable"
            console.print(Padding(
                f"  [bold yellow]⚠ {onion_url} - Error: {str(e)[:30]}[/bold yellow]",
                (0, 0, 0, 6)
            ))
        
        if last_status != new_status and last_status != "seized":
            self.state.set(onion_url, {
                "status": new_status,
                "last_checked": datetime.now(timezone.utc).isoformat()
            })
            self.state.save()
        
        return False
    
    def _retry_with_new_circuit(self, onion_url: str, proxies: dict):
        """Rotate Tor circuit and retry a failed onion check once. Returns result or None on failure."""
        if self.tor.renew_circuit():
            console.print(Padding(
                f"  [bold cyan]↻ Circuit rotated, waiting for new circuit...[/bold cyan]",
                (0, 0, 0, 6)
            ))
            time.sleep(5)
            try:
                url = onion_url if onion_url.startswith("http") else f"http://{onion_url}"
                response = requests.get(url, proxies=proxies, timeout=ONION_TIMEOUT, stream=True)
                max_size = 5 * 1024 * 1024
                chunks = []
                bytes_read = 0
                for chunk in response.iter_content(chunk_size=65536, decode_unicode=False):
                    bytes_read += len(chunk)
                    if bytes_read > max_size:
                        response.close()
                        break
                    chunks.append(chunk)
                html_content = b"".join(chunks).decode("utf-8", errors="replace").lower()
                is_seized = any(keyword in html_content for keyword in SEIZURE_KEYWORDS)
                new_status = "seized" if is_seized else "active"
                
                console.print(Padding(
                    f"  [bold green]✓ Retry successful - {onion_url} is {new_status}[/bold green]",
                    (0, 0, 0, 6)
                ))
                
                self.state.set(onion_url, {
                    "status": new_status,
                    "last_checked": datetime.now(timezone.utc).isoformat()
                })
                self.state.save()
                
                if self.event_feed and not self.silent:
                    found_keywords = [kw for kw in SEIZURE_KEYWORDS if kw in html_content] if is_seized else []
                    self.event_feed.add_event("http_baseline", onion_url, {
                        "fingerprint": {
                            "_status_code": response.status_code,
                            "_final_url": url,
                            "_body_hash": hashlib.sha256(b"".join(chunks)).hexdigest(),
                            "_body_size": bytes_read,
                            "_scheme": "http" if url.startswith("http://") else "https",
                            "_seizure_keywords": found_keywords,
                            "_is_challenge_page": False,
                            "server": response.headers.get("server", ""),
                        },
                        "site_type": "onion"
                    })
                
                return is_seized
            except Exception:
                console.print(Padding(
                    f"  [bold yellow]⚠ Retry also failed for {onion_url}[/bold yellow]",
                    (0, 0, 0, 6)
                ))
        else:
            console.print(Padding(
                f"  [bold yellow]⚠ Could not rotate circuit (is Tor ControlPort enabled?)[/bold yellow]",
                (0, 0, 0, 6)
            ))
        return None
    
    def scan_all(self):
        if not self.tor.check():
            console.print("")
            console.print(Padding(
                "[bold yellow]⚠ Skipping onion site scans: Tor is not running or not configured[/bold yellow]",
                (0, 0, 0, 4)
            ))
            console.print("")
            return
        
        total = len(ONION_SITES)
        start_time = time.time()
        seized_count = 0
        reachable_count = 0
        unreachable_count = 0
        
        console.print("")
        console.print(Padding(
            "[bold magenta]═══════════════════════════════════════════════════════════[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold magenta]→ Starting Onion Site Seizure Scan - {total} sites[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold magenta]═══════════════════════════════════════════════════════════[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        for i, onion_site in enumerate(ONION_SITES, 1):
            console.print(Padding(
                f"[bold yellow]→ [{i}/{total}] {onion_site}[/bold yellow]",
                (0, 0, 0, 4)
            ))
            
            result = self.check_site(onion_site)
            
            site_status = self.state.get(onion_site, {}).get("status", "unknown")
            if site_status == "seized":
                seized_count += 1
            elif site_status == "active":
                reachable_count += 1
            else:
                unreachable_count += 1
            
            console.print("")
            
            if i < total:
                time.sleep(ONION_SITE_DELAY)
        
        elapsed = time.time() - start_time
        console.print(Padding(
            "[bold magenta]───────────────────────────────────────────────────────────[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold magenta]→ Onion scan finished in {elapsed:.1f}s[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold green]  Active: {reachable_count}[/bold green]  [bold yellow]Unreachable: {unreachable_count}[/bold yellow]  [bold red]Seized: {seized_count}[/bold red]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold magenta]───────────────────────────────────────────────────────────[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print("")


class DNSMonitor:
    
    def __init__(self, state_manager: StateManager, notifier: Notifier, 
                 event_feed: EventFeed = None, proxy_url: str = None):
        self.state = state_manager
        self.notifier = notifier
        self.event_feed = event_feed
        self.silent = False
        self.proxy_url = proxy_url
    
    def check_domain(self, domain: str, record_type: str) -> bool:
        try:
            answers = dns.resolver.resolve(domain, record_type, lifetime=DNS_TIMEOUT)
            records = sorted([r.to_text() for r in answers])
        except dns.resolver.NXDOMAIN:
            return False
        except dns.resolver.Timeout:
            return False
        except dns.resolver.NoAnswer:
            return False
        except Exception as e:
            return False
        
        domain_state = self.state.get(domain, {})
        record_state = domain_state.get(record_type, {"records": [], "history": []})
        
        if not isinstance(record_state, dict):
            record_state = {"records": [], "history": []}
        
        history = record_state.get("history", [])
        
        if records in history:
            return False
        
        is_first_run = len(history) == 0
        
        if is_first_run:
            seizure_indicators = ['fbi.seized', 'seized.gov', 'europol', 'interpol', 'seized', 'usssdomainseizure']
            is_seized = any(indicator in str(records).lower() for indicator in seizure_indicators)
            
            if is_seized:
                console.print("")
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    f"[bold red]🚨 NEW DOMAIN DETECTED - ALREADY SEIZED![/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print(Padding(
                    f"[bold yellow]Domain: {domain}[/bold yellow]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold yellow]Record Type: {record_type}[/bold yellow]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold red]Seizure Indicators: {', '.join(records)}[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding("!" * 80, (0, 0, 0, 4)))
                console.print("")
                
                
                if domain not in self.state.data:
                    self.state.data[domain] = {}
                
                self.state.data[domain][record_type] = {
                    "records": records,
                    "history": [records]
                }
                
                if not self.silent:
                    console.print(Padding(
                        "[bold cyan]→ Capturing seizure screenshot...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    screenshot_path = DWIScreenshot.capture(domain, use_tor=False, proxy_url=self.proxy_url)
                    
                    console.print(Padding(
                        "[bold cyan]→ Sending SEIZURE notifications...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    
                    screenshot_str = str(screenshot_path) if screenshot_path else None
                    self.notifier.notify_discord(domain, f"DNS Seizure ({record_type})", records, ["Previously active"], screenshot_path=screenshot_str)
                    self.notifier.notify_telegram(domain, f"DNS Seizure ({record_type})", records, ["Previously active"], seizure_capture=screenshot_str)
                    
                    if self.event_feed:
                        self.event_feed.add_event("seizure", domain, {
                            "record_type": record_type,
                            "records": records,
                            "site_type": "clearnet",
                            "screenshot": screenshot_str
                        })
                    
                    console.print(Padding(
                        "[bold green]✓ Seizure notifications sent[/bold green]",
                        (0, 0, 0, 4)
                    ))
                    console.print("")
                else:
                    console.print(Padding(
                        "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                        (0, 0, 0, 4)
                    ))
                
                return True
            
            console.print("")
            console.print(Padding("+" * 80, (0, 0, 0, 4)))
            console.print(Padding(
                f"[bold cyan]📡 NEW DOMAIN ADDED TO MONITORING[/bold cyan]",
                (0, 0, 0, 4)
            ))
            console.print(Padding("+" * 80, (0, 0, 0, 4)))
            console.print(Padding(
                f"[bold yellow]Domain: {domain}[/bold yellow]",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[bold yellow]Record Type: {record_type}[/bold yellow]",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[bold green]Initial Records: {', '.join(records)}[/bold green]",
                (0, 0, 0, 4)
            ))
            console.print(Padding("+" * 80, (0, 0, 0, 4)))
            console.print("")
            
            
            if domain not in self.state.data:
                self.state.data[domain] = {}
            
            self.state.data[domain][record_type] = {
                "records": records,
                "history": [records]
            }
            
            
            if not self.silent:
                console.print(Padding(
                    "[bold cyan]→ Sending new domain notifications...[/bold cyan]",
                    (0, 0, 0, 4)
                ))
                
                self.notifier.notify_discord(domain, f"DNS New Domain ({record_type})", records, [])
                self.notifier.notify_telegram(domain, f"DNS New Domain ({record_type})", records, [])
                
                if self.event_feed:
                    self.event_feed.add_event("new_domain", domain, {
                        "record_type": record_type,
                        "records": records,
                        "site_type": "clearnet"
                    })
                
                console.print(Padding(
                    "[bold green]✓ New domain notifications sent[/bold green]",
                    (0, 0, 0, 4)
                ))
                console.print("")
            else:
                console.print(Padding(
                    "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                    (0, 0, 0, 4)
                ))
            
            return True
        
        prev_records = history[-1]
        
        console.print("")
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold red]🚨 DNS CHANGE DETECTED![/bold red]",
            (0, 0, 0, 4)
        ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold yellow]Domain: {domain}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold yellow]Record Type: {record_type}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold red]Previous: {', '.join(prev_records)}[/bold red]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold green]New: {', '.join(records)}[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print("")
        
        
        history.append(records)
        if domain not in self.state.data:
            self.state.data[domain] = {}
        
        self.state.data[domain][record_type] = {
            "records": records,
            "history": history[-10:]
        }
        
        
        if not self.silent:
            console.print(Padding(
                "[bold cyan]→ Sending notifications (Discord, Telegram)...[/bold cyan]",
                (0, 0, 0, 4)
            ))
            self.notifier.notify_discord(domain, f"DNS Change ({record_type})", records, prev_records)
            self.notifier.notify_telegram(domain, f"DNS Change ({record_type})", records, prev_records)
            
            if self.event_feed:
                self.event_feed.add_event("dns_change", domain, {
                    "record_type": record_type,
                    "previous_records": prev_records,
                    "new_records": records,
                    "site_type": "clearnet"
                })
            
            console.print(Padding(
                "[bold green]✓ Notifications sent[/bold green]",
                (0, 0, 0, 4)
            ))
            console.print("")
        else:
            console.print(Padding(
                "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                (0, 0, 0, 4)
            ))
        
        return True
    
    def scan_all(self) -> Dict[str, int]:
        stats = {"scanned": 0, "changes": 0}
        
        total = len(DOMAINS)
        start_time = time.time()
        
        console.print("")
        console.print(Padding(
            "[bold cyan]═══════════════════════════════════════════════════════════[/bold cyan]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold cyan]→ Starting DNS Scan - {total} domains × {len(DNS_RECORDS)} record types[/bold cyan]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold cyan]═══════════════════════════════════════════════════════════[/bold cyan]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        for i, domain in enumerate(DOMAINS, 1):
            console.print(Padding(
                f"[bold white]┌─ [{i}/{total}] {domain}[/bold white]",
                (0, 0, 0, 4)
            ))
            
            domain_changes = 0
            
            for j, record_type in enumerate(DNS_RECORDS):
                stats["scanned"] += 1
                
                console.print(Padding(
                    f"[dim]│  Checking {record_type:<6}[/dim]",
                    (0, 0, 0, 4)
                ))
                
                if self.check_domain(domain, record_type):
                    stats["changes"] += 1
                    domain_changes += 1
                
                if j < len(DNS_RECORDS) - 1:
                    time.sleep(DNS_RECORD_DELAY)
            
            if domain_changes > 0:
                console.print(Padding(
                    f"[bold yellow]└─ {domain_changes} change(s) detected[/bold yellow]",
                    (0, 0, 0, 4)
                ))
            else:
                console.print(Padding(
                    f"[bold green]└─ No changes[/bold green]",
                    (0, 0, 0, 4)
                ))
            
            console.print("")
            
            if i < total:
                time.sleep(DNS_DOMAIN_DELAY)
        
        elapsed = time.time() - start_time
        console.print(Padding(
            f"[bold cyan]→ DNS scan finished in {elapsed:.1f}s - {stats['scanned']} records checked, {stats['changes']} changes[/bold cyan]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        return stats


class HTTPMonitor:
    
    MAX_BODY_SIZE = 5 * 1024 * 1024
    
    SEIZURE_REDIRECT_PATTERNS = [
        ".gov", ".mil", "seized", "justice.gov", "europol.europa.eu",
        "ice.gov", "fbi.gov",
    ]
    
    def __init__(self, state_manager: StateManager, notifier: 'Notifier', 
                 event_feed: EventFeed = None, escalation: 'EscalationEngine' = None,
                 proxies: dict = None):
        self.state = state_manager
        self.notifier = notifier
        self.event_feed = event_feed
        self.silent = False
        self.escalation = escalation
        self.proxies = proxies
        self.scan_count = 0
    
    def _fetch_fingerprint(self, domain: str) -> Optional[dict]:
        hdrs = {"User-Agent": random.choice(USER_AGENTS)}
        
        for scheme in ["https", "http"]:
            try:
                resp = requests.get(
                    f"{scheme}://{domain}",
                    timeout=REQUEST_TIMEOUT,
                    headers=hdrs,
                    allow_redirects=True,
                    stream=True,
                    verify=(scheme == "https"),
                    proxies=self.proxies
                )
                
                fingerprint = {}
                for header in TRACKED_HEADERS:
                    val = resp.headers.get(header)
                    if val:
                        fingerprint[header] = val
                
                fingerprint["_status_code"] = resp.status_code
                fingerprint["_final_url"] = resp.url
                
                hasher = hashlib.sha256()
                chunks = []
                bytes_read = 0
                keyword_scan_limit = 1 * 1024 * 1024
                for chunk in resp.iter_content(chunk_size=65536):
                    bytes_read += len(chunk)
                    if bytes_read > self.MAX_BODY_SIZE:
                        resp.close()
                        break
                    hasher.update(chunk)
                    if bytes_read <= keyword_scan_limit:
                        chunks.append(chunk)
                
                fingerprint["_body_hash"] = hasher.hexdigest()
                fingerprint["_body_size"] = bytes_read
                fingerprint["_scheme"] = scheme
                
                body_text = b"".join(chunks).decode("utf-8", errors="replace").lower()
                seizure_hits = [kw for kw in SEIZURE_KEYWORDS if kw in body_text]
                fingerprint["_seizure_keywords"] = seizure_hits
                
                challenge_hits = [kw for kw in CHALLENGE_KEYWORDS if kw in body_text]
                fingerprint["_is_challenge_page"] = bool(challenge_hits)
                
                return fingerprint
                
            except requests.exceptions.SSLError:
                if scheme == "https":
                    continue
                return None
            except requests.exceptions.ConnectionError:
                if scheme == "https":
                    continue
                return None
            except requests.exceptions.Timeout:
                return None
            except requests.exceptions.RequestException:
                return None
        
        return None
    
    def _check_domain_with_fingerprint(self, domain: str, fingerprint: Optional[dict]) -> bool:
        if fingerprint is None:
            console.print(Padding(
                f"  [bold yellow]⚠ HTTP unreachable: {domain[:60]}[/bold yellow]",
                (0, 0, 0, 6)
            ))
            return False
        
        prev_state = self.state.get(domain, {})
        prev_fingerprint = prev_state.get("fingerprint", {})
        is_first_run = not prev_fingerprint
        
        transient_codes = {502, 503, 504, 520, 521, 522, 523, 524}
        is_transient_response = fingerprint.get("_status_code") in transient_codes
        is_challenge_response = fingerprint.get("_is_challenge_page", False)
        
        if not is_transient_response and not is_challenge_response:
            self.state.set(domain, {
                "fingerprint": fingerprint,
                "last_checked": datetime.now(timezone.utc).isoformat()
            })
        elif not is_first_run:
            return False
        
        if is_first_run:
            server = fingerprint.get("server", "Unknown")
            body_hash = fingerprint.get("_body_hash", "")[:12]
            seizure_kw = fingerprint.get("_seizure_keywords", [])
            
            console.print(Padding(
                f"  [bold green]✓ HTTP baseline: {domain[:50]} - {server} - body:{body_hash}[/bold green]",
                (0, 0, 0, 6)
            ))
            
            if seizure_kw and not self.silent and self.scan_count <= 2:
                console.print(Padding(
                    f"  [bold red]⚠ SEIZURE KEYWORDS in initial HTTP: {', '.join(seizure_kw[:3])}[/bold red]",
                    (0, 0, 0, 6)
                ))
                
                if self.escalation:
                    console.print(Padding(
                        "[bold red]→ Seizure keywords on first scan - triggering cross-monitor escalation...[/bold red]",
                        (0, 0, 0, 4)
                    ))
                    self.escalation.escalate(
                        domain,
                        trigger=f"HTTP Initial ({', '.join(seizure_kw[:3])})",
                        http_evidence={"changes": [f"Seizure keywords: {', '.join(seizure_kw)}"]}
                    )
                else:
                    alert_records = [f"Keyword: {kw}" for kw in seizure_kw]
                    self.notifier.notify_discord(domain, "HTTP Seizure Keywords (Initial)", alert_records, ["New domain"])
                    self.notifier.notify_telegram(domain, "HTTP Seizure Keywords (Initial)", alert_records, ["New domain"])
                
                if self.event_feed:
                    self.event_feed.add_event("http_seizure_initial", domain, {
                        "seizure_keywords": seizure_kw,
                        "server": server,
                        "site_type": "clearnet"
                    })
            elif not self.silent and self.event_feed:
                self.event_feed.add_event("http_baseline", domain, {
                    "fingerprint": fingerprint,
                    "site_type": "clearnet"
                })
            
            return True
        
        header_changes = {}
        body_changed = False
        
        all_headers = set(list(prev_fingerprint.keys()) + list(fingerprint.keys()))
        meta_fields = {"_body_hash", "_body_size", "_scheme", "_status_code", "_final_url", "_seizure_keywords", "_is_challenge_page"}
        
        for key in all_headers:
            if key in meta_fields:
                continue
            old_val = prev_fingerprint.get(key)
            new_val = fingerprint.get(key)
            if old_val != new_val:
                header_changes[key] = {"old": old_val, "new": new_val}
        
        old_status = prev_fingerprint.get("_status_code")
        new_status = fingerprint.get("_status_code")
        is_transient = new_status in transient_codes or old_status in transient_codes
        status_changed = old_status != new_status and not is_transient
        
        old_hash = prev_fingerprint.get("_body_hash")
        new_hash = fingerprint.get("_body_hash")
        old_size = prev_fingerprint.get("_body_size", 0)
        new_size = fingerprint.get("_body_size", 0)
        
        body_hash_differs = old_hash != new_hash
        body_changed = False
        
        is_challenge = fingerprint.get("_is_challenge_page", False)
        was_challenge = prev_fingerprint.get("_is_challenge_page", False)
        skip_body = is_challenge or was_challenge or is_transient
        
        if body_hash_differs and not skip_body and old_size > 0:
            size_ratio = abs(new_size - old_size) / old_size
            body_changed = size_ratio > 0.35
        elif body_hash_differs and not skip_body and old_size == 0:
            body_changed = True
        
        old_url = prev_fingerprint.get("_final_url", "")
        new_url = fingerprint.get("_final_url", "")
        old_url_stripped = re.sub(r'^https?://', '', old_url).rstrip('/')
        new_url_stripped = re.sub(r'^https?://', '', new_url).rstrip('/')
        redirect_changed = old_url_stripped != new_url_stripped
        
        current_seizure_kw = fingerprint.get("_seizure_keywords", [])
        prev_seizure_kw = prev_fingerprint.get("_seizure_keywords", [])
        new_seizure_kw = [kw for kw in current_seizure_kw if kw not in prev_seizure_kw]
        has_new_seizure_keywords = bool(new_seizure_kw)
        
        if not header_changes and not body_changed and not status_changed and not redirect_changed and not has_new_seizure_keywords:
            return False
        
        changes_summary = []
        if status_changed:
            changes_summary.append(f"Status: {old_status} → {new_status}")
        if redirect_changed:
            changes_summary.append(f"Redirect: {old_url[:60]} → {new_url[:60]}")
        if header_changes:
            for h, diff in header_changes.items():
                changes_summary.append(f"{h}: {diff['old'] or 'None'} → {diff['new'] or 'None'}")
        if body_changed:
            changes_summary.append(f"Body hash: {old_hash[:12]} → {new_hash[:12]} (size: {old_size:,} → {new_size:,})")
        if has_new_seizure_keywords and not body_changed:
            changes_summary.append(f"Body hash: {old_hash[:12]} → {new_hash[:12]} (seizure keywords detected)")
        
        is_seizure_signal = False
        seizure_reasons = []
        
        if has_new_seizure_keywords:
            is_seizure_signal = True
            seizure_reasons.append(f"Seizure keywords found in page: {', '.join(new_seizure_kw[:3])}")
        
        if redirect_changed and new_url:
            for pattern in self.SEIZURE_REDIRECT_PATTERNS:
                if pattern in new_url.lower():
                    is_seizure_signal = True
                    seizure_reasons.append(f"Redirect to {pattern}")
                    break
        
        if body_changed and "server" in header_changes:
            is_seizure_signal = True
            seizure_reasons.append("Server header + body content changed simultaneously")
        
        if status_changed and new_status in (403, 451):
            is_seizure_signal = True
            seizure_reasons.append(f"Status code changed to {new_status}")
        
        console.print("")
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        if is_seizure_signal:
            console.print(Padding(
                f"[bold red]🚨 HTTP SEIZURE SIGNAL DETECTED! 🚨[/bold red]",
                (0, 0, 0, 4)
            ))
        else:
            console.print(Padding(
                f"[bold red]🔍 HTTP FINGERPRINT CHANGE DETECTED![/bold red]",
                (0, 0, 0, 4)
            ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold yellow]Domain: {domain}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        for line in changes_summary:
            console.print(Padding(
                f"[bold white]  {line}[/bold white]",
                (0, 0, 0, 4)
            ))
        if seizure_reasons:
            for reason in seizure_reasons:
                console.print(Padding(
                    f"[bold red]  ⚠ {reason}[/bold red]",
                    (0, 0, 0, 4)
                ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print("")
        
        if not self.silent:
            if is_seizure_signal and self.escalation:
                console.print(Padding(
                    "[bold red]→ Seizure signal detected - triggering cross-monitor escalation...[/bold red]",
                    (0, 0, 0, 4)
                ))
                self.escalation.escalate(
                    domain, 
                    trigger=f"HTTP ({', '.join(seizure_reasons)})",
                    http_evidence={"changes": changes_summary}
                )
            else:
                change_records = changes_summary
                prev_records = [f"Status: {old_status}", f"Body: {old_hash[:12]}"]
                
                self.notifier.notify_discord(domain, "HTTP Fingerprint Change", change_records, prev_records)
                self.notifier.notify_telegram(domain, "HTTP Fingerprint Change", change_records, prev_records)
            
            if self.event_feed:
                self.event_feed.add_event("http_change", domain, {
                    "header_changes": header_changes,
                    "body_changed": body_changed,
                    "status_changed": status_changed,
                    "redirect_changed": redirect_changed,
                    "old_status": old_status,
                    "new_status": new_status,
                    "old_body_hash": old_hash,
                    "new_body_hash": new_hash,
                    "seizure_signal": is_seizure_signal,
                    "seizure_reasons": seizure_reasons,
                    "site_type": "clearnet"
                })
            
            console.print(Padding(
                "[bold green]✓ HTTP change notifications sent[/bold green]",
                (0, 0, 0, 4)
            ))
            console.print("")
        else:
            console.print(Padding(
                "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                (0, 0, 0, 4)
            ))
        
        return True
    
    def scan_all(self) -> Dict[str, int]:
        self.scan_count += 1
        stats = {"scanned": 0, "changes": 0}
        total = len(DOMAINS)
        start_time = time.time()
        
        console.print("")
        console.print(Padding(
            "[bold white]═══════════════════════════════════════════════════════════[/bold white]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold white]→ Starting HTTP Fingerprint Scan - {total} domains (×{HTTP_CONCURRENCY} parallel)[/bold white]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold white]═══════════════════════════════════════════════════════════[/bold white]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        fingerprints = {}
        fetched = 0
        with ThreadPoolExecutor(max_workers=HTTP_CONCURRENCY) as executor:
            future_to_domain = {
                executor.submit(self._fetch_fingerprint, domain): domain 
                for domain in DOMAINS
            }
            for future in as_completed(future_to_domain):
                domain = future_to_domain[future]
                fetched += 1
                try:
                    fingerprints[domain] = future.result()
                except Exception:
                    fingerprints[domain] = None
                console.print(Padding(
                    f"[dim]    Fetched {fetched}/{total}: {domain}[/dim]",
                    (0, 0, 0, 4)
                ))
        
        console.print("")
        
        for i, domain in enumerate(DOMAINS, 1):
            stats["scanned"] += 1
            
            console.print(Padding(
                f"[bold white]  [{i}/{total}] {domain}[/bold white]",
                (0, 0, 0, 4)
            ))
            
            fingerprint = fingerprints.get(domain)
            if self._check_domain_with_fingerprint(domain, fingerprint):
                stats["changes"] += 1
        
        elapsed = time.time() - start_time
        console.print(Padding(
            f"[bold white]→ HTTP scan finished in {elapsed:.1f}s - {stats['scanned']} domains, {stats['changes']} changes[/bold white]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        return stats


class WHOISMonitor:
    
    def __init__(self, state_manager: StateManager, notifier: 'Notifier', 
                 event_feed: EventFeed = None, escalation: 'EscalationEngine' = None,
                 proxies: dict = None, proxy_url: str = None):
        self.state = state_manager
        self.notifier = notifier
        self.event_feed = event_feed
        self.silent = False
        self._whois_available = None
        self.escalation = escalation
        self.proxies = proxies
        self.proxy_url = proxy_url
        self.scan_count = 0
    
    def _check_whois_available(self) -> bool:
        if self._whois_available is not None:
            return self._whois_available
        try:
            import whois
            self._whois_available = True
        except ImportError:
            self._whois_available = False
            console.print(Padding(
                "[bold yellow]⚠ python-whois not installed - WHOIS monitoring disabled[/bold yellow]",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                "[dim]    Install with: pip install python-whois[/dim]",
                (0, 0, 0, 4)
            ))
        return self._whois_available
    
    @staticmethod
    def _migrate_stored_record(record: dict) -> dict:
        """Re-normalize a stored WHOIS record so old state matches current normalization.
        Fixes false positives when normalization logic changes between versions."""
        if not record or not isinstance(record, dict):
            return record
        
        migrated = dict(record)
        
        status = migrated.get("status")
        if status is not None:
            if isinstance(status, str):
                status = status.split()
            if isinstance(status, list):
                known_epp = {
                    'clienthold', 'clienttransferprohibited', 'clientupdateprohibited',
                    'clientdeleteprohibited', 'clientrenewprohibited',
                    'serverhold', 'servertransferprohibited', 'serverupdateprohibited',
                    'serverdeleteprohibited', 'serverrenewprohibited',
                    'ok', 'active', 'inactive',
                }
                transient_statuses = {'addperiod', 'autorenewperiod', 'renewperiod',
                                      'transferperiod', 'redemptionperiod', 'pendingdelete',
                                      'pendingupdate', 'pendingtransfer'}
                flat = set()
                for v in status:
                    s = str(v).lower().strip()
                    s = re.sub(r'https?://(www\.)?icann\.org/epp#', '', s)
                    for part in s.split():
                        part = part.strip().rstrip('.')
                        if part and part not in transient_statuses:
                            flat.add(part)
                expanded = set()
                for token in flat:
                    if token in known_epp:
                        expanded.add(token)
                    else:
                        matched = False
                        for epp in known_epp:
                            stripped = token.replace(epp, '', 1)
                            if stripped == '' or stripped == epp or stripped in known_epp:
                                expanded.add(epp)
                                if stripped and stripped in known_epp:
                                    expanded.add(stripped)
                                matched = True
                                break
                        if not matched:
                            expanded.add(token)
                final = set()
                for s in expanded:
                    is_fragment = False
                    if s not in known_epp:
                        for candidate in expanded:
                            if candidate != s and candidate in known_epp and s in candidate:
                                is_fragment = True
                                break
                    if not is_fragment:
                        final.add(s)
                migrated["status"] = sorted(final)
        
        for date_key in ("creation_date", "expiration_date", "updated_date"):
            val = migrated.get(date_key)
            if isinstance(val, str) and '.' in val:
                migrated[date_key] = val.split('.')[0]
        
        return migrated
    
    def _fetch_whois(self, domain: str) -> Optional[dict]:
        if not self._check_whois_available():
            return None
        
        try:
            import whois
            w = whois.whois(domain)
            
            if w.status is None and w.registrar is None:
                return None
            
            def _normalize_registrar(val):
                if val is None:
                    return None
                s = str(val).lower().strip()
                s = re.sub(r'[.,;:\s]+', ' ', s).strip().rstrip('.')
                if s in REGISTRAR_ALIASES:
                    return REGISTRAR_ALIASES[s]
                stripped = re.sub(r'\s+(limited|ltd|inc|llc|corp|co|sas|gmbh|ag|bv|pty|oy|ab)$', '', s).strip()
                if stripped in REGISTRAR_ALIASES:
                    return REGISTRAR_ALIASES[stripped]
                return stripped
            
            def _normalize(val):
                if val is None:
                    return None
                if isinstance(val, list):
                    normalized = []
                    for v in val:
                        if not v:
                            continue
                        s = str(v).lower().strip()
                        s = re.sub(r'https?://(www\.)?icann\.org/epp#', '', s)
                        s = re.sub(r'[.,;:\s]+', ' ', s).strip().rstrip('.')
                        normalized.append(s)
                    return sorted(set(normalized))
                if isinstance(val, datetime):
                    if val.tzinfo is not None:
                        val = val.replace(tzinfo=None)
                    return val.strftime('%Y-%m-%dT%H:%M:%S')
                s = str(val).lower().strip()
                s = re.sub(r'https?://(www\.)?icann\.org/epp#', '', s)
                return re.sub(r'[.,;:\s]+', ' ', s).strip().rstrip('.')
            
            def _is_privacy_value(val) -> bool:
                if val is None:
                    return False
                val_str = str(val).lower()
                return any(p in val_str for p in WHOIS_PRIVACY_ORGS)
            
            def _normalize_status(val):
                if val is None:
                    return []
                if not isinstance(val, list):
                    val = [val]
                transient_statuses = {'addperiod', 'autorenewperiod', 'renewperiod',
                                      'transferperiod', 'redemptionperiod', 'pendingdelete',
                                      'pendingupdate', 'pendingtransfer'}
                known_epp = {
                    'clienthold', 'clienttransferprohibited', 'clientupdateprohibited',
                    'clientdeleteprohibited', 'clientrenewprohibited',
                    'serverhold', 'servertransferprohibited', 'serverupdateprohibited',
                    'serverdeleteprohibited', 'serverrenewprohibited',
                    'ok', 'active', 'inactive',
                }
                statuses = set()
                for v in val:
                    if not v:
                        continue
                    s = str(v).lower().strip()
                    s = re.sub(r'https?://(www\.)?icann\.org/epp#', '', s)
                    for part in s.split():
                        part = part.strip().rstrip('.')
                        if part and part not in transient_statuses:
                            statuses.add(part)
                final = set()
                for s in statuses:
                    is_fragment = False
                    if s not in known_epp:
                        for candidate in statuses:
                            if candidate != s and candidate in known_epp and s in candidate:
                                is_fragment = True
                                break
                    if not is_fragment:
                        final.add(s)
                return sorted(final)
            
            record = {
                "registrar": _normalize_registrar(w.registrar),
                "whois_server": _normalize(w.whois_server),
                "name_servers": _normalize(w.name_servers if isinstance(w.name_servers, list) else [w.name_servers] if w.name_servers else []),
                "status": _normalize_status(w.status),
                "registrant_org": _normalize(getattr(w, 'org', None)),
                "registrant_country": _normalize(getattr(w, 'country', None)),
                "creation_date": _normalize(w.creation_date[0] if isinstance(w.creation_date, list) and w.creation_date else w.creation_date),
                "expiration_date": _normalize(w.expiration_date[0] if isinstance(w.expiration_date, list) and w.expiration_date else w.expiration_date),
                "updated_date": _normalize(w.updated_date[0] if isinstance(w.updated_date, list) and w.updated_date else w.updated_date),
            }
            
            record["_has_privacy_org"] = _is_privacy_value(getattr(w, 'org', None))
            
            return record
            
        except Exception:
            return None
    
    def _check_seizure_indicators(self, record: dict) -> List[str]:
        indicators_found = []
        searchable = json.dumps(record).lower()
        
        for indicator in WHOIS_SEIZURE_INDICATORS:
            if indicator in searchable:
                indicators_found.append(indicator)
        
        LE_CLOUDFLARE_NS = [
            "jocelyn.ns.cloudflare.com", "plato.ns.cloudflare.com",
        ]
        SERVER_PROHIBITIONS = [
            "servertransferprohibited", "serverdeleteprohibited",
            "serverupdateprohibited", "serverholdprohibited",
        ]
        
        name_servers = record.get("name_servers", []) or []
        status = record.get("status", []) or []
        
        ns_str = " ".join(str(ns) for ns in name_servers).lower().replace(" ", "")
        has_le_cloudflare = any(
            ns.replace(".", "").replace(" ", "") in ns_str 
            for ns in LE_CLOUDFLARE_NS
        )
        
        if has_le_cloudflare:
            status_str = " ".join(str(s) for s in status).lower().replace(" ", "")
            prohibition_count = sum(1 for p in SERVER_PROHIBITIONS if p in status_str)
            if prohibition_count >= 3:
                indicators_found.append(f"le cloudflare ns + {prohibition_count} server prohibitions")
        
        return indicators_found
    
    def _check_domain_with_record(self, domain: str, record: Optional[dict]) -> bool:
        if record is None:
            console.print(Padding(
                f"  [bold yellow]⚠ WHOIS lookup failed: {domain[:60]}[/bold yellow]",
                (0, 0, 0, 6)
            ))
            return False
        
        prev_state = self.state.get(domain, {})
        prev_record = self._migrate_stored_record(prev_state.get("whois", {}))
        is_first_run = not prev_record
        
        seizure_hits = self._check_seizure_indicators(record)
        
        self.state.set(domain, {
            "whois": record,
            "seizure_indicators": seizure_hits,
            "last_checked": datetime.now(timezone.utc).isoformat()
        })
        
        if is_first_run:
            registrar = record.get("registrar", "Unknown")
            console.print(Padding(
                f"  [bold green]✓ WHOIS baseline: {domain[:50]} - {registrar}[/bold green]",
                (0, 0, 0, 6)
            ))
            
            if seizure_hits:
                console.print(Padding(
                    f"  [bold red]⚠ SEIZURE INDICATORS in initial WHOIS: {', '.join(seizure_hits)}[/bold red]",
                    (0, 0, 0, 6)
                ))
                
                if not self.silent and self.scan_count <= 2:
                    console.print(Padding(
                        "[bold cyan]→ Capturing screenshot...[/bold cyan]",
                        (0, 0, 0, 6)
                    ))
                    screenshot_path = DWIScreenshot.capture(domain, use_tor=False, proxy_url=self.proxy_url)
                    screenshot_str = str(screenshot_path) if screenshot_path else None
                    
                    alert_records = [f"Indicator: {h}" for h in seizure_hits]
                    self.notifier.notify_discord(domain, "WHOIS Seizure Indicators (Initial)", alert_records, ["New domain"], screenshot_path=screenshot_str)
                    self.notifier.notify_telegram(domain, "WHOIS Seizure Indicators (Initial)", alert_records, ["New domain"], seizure_capture=screenshot_str)
                    
                    if self.event_feed:
                        self.event_feed.add_event("whois_seizure_initial", domain, {
                            "seizure_indicators": seizure_hits,
                            "registrar": record.get("registrar"),
                            "screenshot": screenshot_str,
                            "site_type": "clearnet"
                        })
            
            if not self.silent and self.event_feed:
                self.event_feed.add_event("whois_baseline", domain, {
                    "registrar": record.get("registrar"),
                    "name_servers": record.get("name_servers"),
                    "site_type": "clearnet"
                })
            
            return True
        
        changes = {}
        whois_meta_fields = {"_has_privacy_org"}
        whois_noisy_fields = {"updated_date", "expiration_date", "whois_server"}
        
        all_keys = set(list(prev_record.keys()) + list(record.keys()))
        
        for key in all_keys:
            if key in whois_meta_fields or key in whois_noisy_fields:
                continue
            old_val = prev_record.get(key)
            new_val = record.get(key)
            if old_val != new_val:
                if key == "registrant_org":
                    old_is_privacy = old_val is None or any(
                        p in str(old_val).lower() for p in WHOIS_PRIVACY_ORGS
                    )
                    new_is_privacy = new_val is None or any(
                        p in str(new_val).lower() for p in WHOIS_PRIVACY_ORGS
                    )
                    if old_is_privacy or new_is_privacy:
                        continue
                
                if key == "registrant_country" and (old_val is None or new_val is None):
                    continue
                
                changes[key] = {"old": old_val, "new": new_val}
        
        if not changes:
            return False
        
        changes_summary = []
        for field, diff in changes.items():
            old_str = str(diff['old']) if diff['old'] else "None"
            new_str = str(diff['new']) if diff['new'] else "None"
            if len(old_str) > 80:
                old_str = old_str[:77] + "..."
            if len(new_str) > 80:
                new_str = new_str[:77] + "..."
            changes_summary.append(f"{field}: {old_str} → {new_str}")
        
        prev_seizure = prev_state.get("seizure_indicators", [])
        new_seizure_hits = [h for h in seizure_hits if h not in prev_seizure]
        was_already_seized = bool(prev_seizure)
        
        high_value_fields = {"registrar", "name_servers", "registrant_org", "status"}
        changed_high_value = set(changes.keys()) & high_value_fields
        
        if was_already_seized:
            lost_indicators = [h for h in prev_seizure if h not in seizure_hits]
            if lost_indicators:
                is_seizure_alert = True
            else:
                return False
        else:
            is_seizure_alert = bool(new_seizure_hits) or (bool(seizure_hits) and bool(changed_high_value))
        
        console.print("")
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        if is_seizure_alert:
            console.print(Padding(
                f"[bold red]🚨 WHOIS SEIZURE INDICATORS DETECTED! 🚨[/bold red]",
                (0, 0, 0, 4)
            ))
        else:
            console.print(Padding(
                f"[bold red]📋 WHOIS CHANGE DETECTED![/bold red]",
                (0, 0, 0, 4)
            ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold yellow]Domain: {domain}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        for line in changes_summary:
            console.print(Padding(
                f"[bold white]  {line}[/bold white]",
                (0, 0, 0, 4)
            ))
        if new_seizure_hits:
            console.print(Padding(
                f"[bold red]  Seizure indicators: {', '.join(new_seizure_hits)}[/bold red]",
                (0, 0, 0, 4)
            ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print("")
        
        if not self.silent:
            if is_seizure_alert and self.escalation:
                console.print(Padding(
                    "[bold red]→ WHOIS seizure indicators detected - triggering cross-monitor escalation...[/bold red]",
                    (0, 0, 0, 4)
                ))
                trigger_indicators = new_seizure_hits if new_seizure_hits else seizure_hits
                self.escalation.escalate(
                    domain,
                    trigger=f"WHOIS ({', '.join(trigger_indicators)})",
                    whois_evidence={
                        "changes": changes_summary,
                        "seizure_indicators": trigger_indicators
                    }
                )
            else:
                screenshot_str = None
                if is_seizure_alert:
                    console.print(Padding(
                        "[bold cyan]→ Capturing screenshot...[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                    screenshot_path = DWIScreenshot.capture(domain, use_tor=False, proxy_url=self.proxy_url)
                    screenshot_str = str(screenshot_path) if screenshot_path else None
                
                record_type = "WHOIS Seizure Alert" if is_seizure_alert else "WHOIS Change"
                prev_summary = [f"{k}: {str(v.get('old', 'None'))[:60]}" for k, v in changes.items()]
                
                self.notifier.notify_discord(domain, record_type, changes_summary, prev_summary, screenshot_path=screenshot_str)
                self.notifier.notify_telegram(domain, record_type, changes_summary, prev_summary, seizure_capture=screenshot_str)
            
            if self.event_feed:
                event_type = "whois_seizure" if is_seizure_alert else "whois_change"
                self.event_feed.add_event(event_type, domain, {
                    "changes": {k: {"old": str(v.get("old", "")), "new": str(v.get("new", ""))} for k, v in changes.items()},
                    "seizure_indicators": seizure_hits,
                    "new_seizure_indicators": new_seizure_hits,
                    "escalated": is_seizure_alert and self.escalation is not None,
                    "site_type": "clearnet"
                })
            
            console.print(Padding(
                "[bold green]✓ WHOIS change notifications sent[/bold green]",
                (0, 0, 0, 4)
            ))
            console.print("")
        else:
            console.print(Padding(
                "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                (0, 0, 0, 4)
            ))
        
        return True
    
    def scan_all(self) -> Dict[str, int]:
        if not self._check_whois_available():
            return {"scanned": 0, "changes": 0}
        
        self.scan_count += 1
        stats = {"scanned": 0, "changes": 0}
        total = len(DOMAINS)
        start_time = time.time()
        
        console.print("")
        console.print(Padding(
            "[bold green]═══════════════════════════════════════════════════════════[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold green]→ Starting WHOIS Scan - {total} domains (×{WHOIS_CONCURRENCY} parallel)[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold green]═══════════════════════════════════════════════════════════[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        whois_records = {}
        fetched = 0
        fetchable = [d for d in DOMAINS if not d.endswith(".onion")]
        fetch_total = len(fetchable)
        with ThreadPoolExecutor(max_workers=WHOIS_CONCURRENCY) as executor:
            future_to_domain = {
                executor.submit(self._fetch_whois, domain): domain
                for domain in fetchable
            }
            for future in as_completed(future_to_domain):
                domain = future_to_domain[future]
                fetched += 1
                try:
                    whois_records[domain] = future.result()
                except Exception:
                    whois_records[domain] = None
                console.print(Padding(
                    f"[dim]    Fetched {fetched}/{fetch_total}: {domain}[/dim]",
                    (0, 0, 0, 4)
                ))
        
        console.print("")
        
        for i, domain in enumerate(DOMAINS, 1):
            if domain.endswith(".onion"):
                continue
            stats["scanned"] += 1
            
            console.print(Padding(
                f"[bold white]  [{i}/{total}] {domain}[/bold white]",
                (0, 0, 0, 4)
            ))
            
            record = whois_records.get(domain)
            if self._check_domain_with_record(domain, record):
                stats["changes"] += 1
        
        elapsed = time.time() - start_time
        console.print(Padding(
            f"[bold green]→ WHOIS scan finished in {elapsed:.1f}s - {stats['scanned']} domains, {stats['changes']} changes[/bold green]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        return stats


class IPMonitor:
    """Monitors A/AAAA record IP addresses for changes across scan cycles.
    
    Unlike the DNS monitor which tracks full record-set history and fires on 
    never-before-seen combinations, the IP monitor focuses specifically on IP 
    address changes with richer context: reverse DNS, provider identification,
    and classification of change type (CDN rotation, hosting migration, 
    potential seizure infrastructure, origin IP leak).
    """
    
    KNOWN_CDN_KEYWORDS = [
        "cloudflare", "akamai", "fastly", "cloudfront", "incapsula", "imperva",
        "sucuri", "stackpath", "cdn77", "bunnycdn", "ddos-guard", "ddosguard",
        "quic.cloud", "section.io", "edgecast", "limelight", "keycdn",
    ]
    
    KNOWN_LE_INDICATORS = [
        "fbi.gov", "justice.gov", "usdoj", "europol", "interpol",
        "ice.gov", "dhs.gov", "seized", "ncsc.gov", "nca.gov",
        "bka.de", "bmi.bund", "polisen.se", "politie.nl",
    ]
    
    GOVERNMENT_ASN_KEYWORDS = [
        "department of justice", "u.s. government", "federal bureau",
        "united states department", "us-doj", "european police",
        "government communications", "ministry of defence",
    ]
    
    def __init__(self, state_manager: StateManager, notifier: 'Notifier',
                 event_feed: EventFeed = None, escalation: 'EscalationEngine' = None,
                 proxy_url: str = None):
        self.state = state_manager
        self.notifier = notifier
        self.event_feed = event_feed
        self.escalation = escalation
        self.silent = False
        self.proxy_url = proxy_url
        self.scan_count = 0
    
    def _resolve_ips(self, domain: str) -> dict:
        """Resolve A and AAAA records for a domain. Returns {'A': [...], 'AAAA': [...]}."""
        result = {"A": [], "AAAA": []}
        for rtype in ("A", "AAAA"):
            try:
                answers = dns.resolver.resolve(domain, rtype, lifetime=DNS_TIMEOUT)
                result[rtype] = sorted([r.to_text() for r in answers])
            except Exception:
                pass
        return result
    
    def _reverse_dns(self, ip: str) -> Optional[str]:
        """Attempt reverse DNS lookup for an IP address."""
        try:
            from dns.reversename import from_address
            rev_name = from_address(ip)
            answers = dns.resolver.resolve(rev_name, "PTR", lifetime=DNS_TIMEOUT)
            ptrs = [r.to_text().rstrip('.') for r in answers]
            return ptrs[0] if ptrs else None
        except Exception:
            return None
    
    def _classify_ip_change(self, domain: str, old_ips: list, new_ips: list,
                            rdns_results: dict) -> dict:
        """Classify what kind of IP change this is.
        
        Returns dict with:
            - change_type: 'cdn_rotation' | 'hosting_migration' | 'seizure_signal' | 
                           'provider_change' | 'new_ips_added' | 'ips_removed' | 'ip_change'
            - is_seizure_signal: bool
            - details: str
            - rdns: dict of ip -> rdns
        """
        classification = {
            "change_type": "ip_change",
            "is_seizure_signal": False,
            "details": "",
            "seizure_reasons": [],
            "rdns": rdns_results,
        }
        
        added = [ip for ip in new_ips if ip not in old_ips]
        removed = [ip for ip in old_ips if ip not in new_ips]
        
        for ip in new_ips:
            rdns = rdns_results.get(ip, "")
            if rdns:
                rdns_lower = rdns.lower()
                for indicator in self.KNOWN_LE_INDICATORS:
                    if indicator in rdns_lower:
                        classification["is_seizure_signal"] = True
                        classification["change_type"] = "seizure_signal"
                        classification["seizure_reasons"].append(
                            f"rDNS for {ip} → {rdns} (matches LE indicator: {indicator})"
                        )
        
        if not classification["is_seizure_signal"]:
            old_cdns = set()
            new_cdns = set()
            
            for ip in old_ips:
                rdns = rdns_results.get(ip, "")
                for cdn in self.KNOWN_CDN_KEYWORDS:
                    if cdn in (rdns or "").lower():
                        old_cdns.add(cdn)
            
            for ip in new_ips:
                rdns = rdns_results.get(ip, "")
                for cdn in self.KNOWN_CDN_KEYWORDS:
                    if cdn in (rdns or "").lower():
                        new_cdns.add(cdn)
            
            if old_cdns and new_cdns and old_cdns == new_cdns:
                classification["change_type"] = "cdn_rotation"
                classification["details"] = f"Same CDN provider ({', '.join(old_cdns)}), IP pool rotation"
            elif old_cdns and new_cdns and old_cdns != new_cdns:
                classification["change_type"] = "provider_change"
                classification["details"] = f"CDN change: {', '.join(old_cdns)} → {', '.join(new_cdns)}"
            elif old_cdns and not new_cdns and added:
                classification["change_type"] = "provider_change"
                classification["details"] = f"CDN ({', '.join(old_cdns)}) removed - possible origin IP exposure"
            elif not old_cdns and new_cdns:
                classification["change_type"] = "provider_change"
                classification["details"] = f"Moved behind CDN: {', '.join(new_cdns)}"
            elif added and not removed:
                classification["change_type"] = "new_ips_added"
                classification["details"] = f"{len(added)} new IP(s) added"
            elif removed and not added:
                classification["change_type"] = "ips_removed"
                classification["details"] = f"{len(removed)} IP(s) removed"
            else:
                total_changed = len(added) + len(removed)
                if total_changed == len(old_ips) + len(new_ips):
                    classification["change_type"] = "hosting_migration"
                    classification["details"] = "Complete IP replacement - likely hosting migration"
                else:
                    classification["change_type"] = "ip_change"
                    classification["details"] = f"{len(added)} added, {len(removed)} removed"
        
        return classification
    
    def _check_domain(self, domain: str, resolved: dict) -> bool:
        """Check a single domain for IP changes given pre-resolved IPs."""
        all_ips = resolved.get("A", []) + resolved.get("AAAA", [])
        
        if not all_ips:
            console.print(Padding(
                f"  [bold yellow]⚠ IP resolve failed: {domain[:60]}[/bold yellow]",
                (0, 0, 0, 6)
            ))
            return False
        
        prev_state = self.state.get(domain, {})
        prev_a = prev_state.get("A", [])
        prev_aaaa = prev_state.get("AAAA", [])
        prev_all = prev_a + prev_aaaa
        is_first_run = not prev_state
        
        new_a = resolved.get("A", [])
        new_aaaa = resolved.get("AAAA", [])
        
        self.state.set(domain, {
            "A": new_a,
            "AAAA": new_aaaa,
            "last_checked": datetime.now(timezone.utc).isoformat(),
        })
        
        if is_first_run:
            console.print(Padding(
                f"  [bold green]✓ IP baseline: {domain[:50]} → {', '.join(all_ips[:4])}{'...' if len(all_ips) > 4 else ''}[/bold green]",
                (0, 0, 0, 6)
            ))
            
            if not self.silent and self.event_feed:
                self.event_feed.add_event("ip_baseline", domain, {
                    "A": new_a,
                    "AAAA": new_aaaa,
                    "site_type": "clearnet"
                })
            return True
        
        a_changed = prev_a != new_a
        aaaa_changed = prev_aaaa != new_aaaa
        
        if not a_changed and not aaaa_changed:
            return False
        
        rdns_results = {}
        changed_ips = set(all_ips) - set(prev_all)
        for ip in changed_ips:
            rdns = self._reverse_dns(ip)
            if rdns:
                rdns_results[ip] = rdns
        
        if len(all_ips) <= 4:
            for ip in all_ips:
                if ip not in rdns_results:
                    rdns = self._reverse_dns(ip)
                    if rdns:
                        rdns_results[ip] = rdns
        
        classification = self._classify_ip_change(
            domain, prev_all, all_ips, rdns_results
        )
        
        is_seizure = classification["is_seizure_signal"]
        change_type = classification["change_type"]
        
        changes_summary = []
        if a_changed:
            changes_summary.append(f"A: {', '.join(prev_a) or 'None'} → {', '.join(new_a) or 'None'}")
        if aaaa_changed:
            changes_summary.append(f"AAAA: {', '.join(prev_aaaa) or 'None'} → {', '.join(new_aaaa) or 'None'}")
        if rdns_results:
            for ip, rdns in rdns_results.items():
                changes_summary.append(f"rDNS: {ip} → {rdns}")
        if classification["details"]:
            changes_summary.append(f"Classification: {classification['details']}")
        
        console.print("")
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        if is_seizure:
            console.print(Padding(
                "[bold red]🚨 IP CHANGE - SEIZURE SIGNAL! 🚨[/bold red]",
                (0, 0, 0, 4)
            ))
        else:
            console.print(Padding(
                f"[bold red]🔍 IP CHANGE DETECTED ({change_type.upper()})![/bold red]",
                (0, 0, 0, 4)
            ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold yellow]Domain: {domain}[/bold yellow]",
            (0, 0, 0, 4)
        ))
        for line in changes_summary:
            console.print(Padding(
                f"[bold white]  {line}[/bold white]",
                (0, 0, 0, 4)
            ))
        if classification["seizure_reasons"]:
            for reason in classification["seizure_reasons"]:
                console.print(Padding(
                    f"[bold red]  ⚠ {reason}[/bold red]",
                    (0, 0, 0, 4)
                ))
        console.print(Padding("!" * 80, (0, 0, 0, 4)))
        console.print("")
        
        if not self.silent:
            if is_seizure and self.escalation:
                console.print(Padding(
                    "[bold red]→ IP seizure signal - triggering cross-monitor escalation...[/bold red]",
                    (0, 0, 0, 4)
                ))
                self.escalation.escalate(
                    domain,
                    trigger=f"IP ({', '.join(classification['seizure_reasons'][:2])})",
                    http_evidence={"changes": changes_summary}
                )
            else:
                record_type_label = f"IP Change ({change_type.replace('_', ' ')})"
                prev_records = [f"A: {', '.join(prev_a)}", f"AAAA: {', '.join(prev_aaaa)}"]
                new_records = changes_summary
                
                self.notifier.notify_discord(domain, record_type_label, new_records, prev_records)
                self.notifier.notify_telegram(domain, record_type_label, new_records, prev_records)
            
            if self.event_feed:
                self.event_feed.add_event("ip_change", domain, {
                    "previous_A": prev_a,
                    "previous_AAAA": prev_aaaa,
                    "new_A": new_a,
                    "new_AAAA": new_aaaa,
                    "change_type": change_type,
                    "classification": classification["details"],
                    "is_seizure_signal": is_seizure,
                    "seizure_reasons": classification["seizure_reasons"],
                    "rdns": rdns_results,
                    "site_type": "clearnet"
                })
            
            console.print(Padding(
                "[bold green]✓ IP change notifications sent[/bold green]",
                (0, 0, 0, 4)
            ))
            console.print("")
        else:
            console.print(Padding(
                "[dim]  ↳ Silent mode - state saved, notifications skipped[/dim]",
                (0, 0, 0, 4)
            ))
        
        return True
    
    def scan_all(self) -> Dict[str, int]:
        self.scan_count += 1
        stats = {"scanned": 0, "changes": 0}
        total = len(DOMAINS)
        start_time = time.time()
        
        console.print("")
        console.print(Padding(
            "[bold yellow]═══════════════════════════════════════════════════════════[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold yellow]→ Starting IP Change Scan - {total} domains (×{IP_CONCURRENCY} parallel)[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            "[bold yellow]═══════════════════════════════════════════════════════════[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        resolved_map = {}
        fetched = 0
        with ThreadPoolExecutor(max_workers=IP_CONCURRENCY) as executor:
            future_to_domain = {
                executor.submit(self._resolve_ips, domain): domain
                for domain in DOMAINS
            }
            for future in as_completed(future_to_domain):
                domain = future_to_domain[future]
                fetched += 1
                try:
                    resolved_map[domain] = future.result()
                except Exception:
                    resolved_map[domain] = {"A": [], "AAAA": []}
                console.print(Padding(
                    f"[dim]    Resolved {fetched}/{total}: {domain}[/dim]",
                    (0, 0, 0, 4)
                ))
        
        console.print("")
        
        for i, domain in enumerate(DOMAINS, 1):
            stats["scanned"] += 1
            
            console.print(Padding(
                f"[bold white]  [{i}/{total}] {domain}[/bold white]",
                (0, 0, 0, 4)
            ))
            
            resolved = resolved_map.get(domain, {"A": [], "AAAA": []})
            if self._check_domain(domain, resolved):
                stats["changes"] += 1
        
        elapsed = time.time() - start_time
        console.print(Padding(
            f"[bold yellow]→ IP scan finished in {elapsed:.1f}s - {stats['scanned']} domains, {stats['changes']} changes[/bold yellow]",
            (0, 0, 0, 4)
        ))
        console.print("")
        
        return stats


class DWIWatchdog:
    
    def __init__(self, enable_dns=True, enable_http=True, enable_whois=True, enable_onion=True, enable_ip=True):
        self.config = DWIConfig()
        self.enable_dns = enable_dns
        self.enable_http = enable_http
        self.enable_whois = enable_whois
        self.enable_onion = enable_onion
        self.enable_ip = enable_ip
        
        self.clearnet_proxies = None
        if self.config.clearnet_proxy:
            self.clearnet_proxies = {
                "http": self.config.clearnet_proxy,
                "https": self.config.clearnet_proxy,
            }
        
        self.dns_state = StateManager(STATE_FILE)
        self.onion_state = StateManager(ONION_STATE_FILE)
        self.http_state = StateManager(HTTP_STATE_FILE)
        self.whois_state = StateManager(WHOIS_STATE_FILE)
        self.ip_state = StateManager(IP_STATE_FILE)
        self.tor_checker = TorChecker()
        self.notifier = Notifier(self.config)
        self.event_feed = EventFeed(site_manager=site_manager)
        
        self.dns_monitor = DNSMonitor(self.dns_state, self.notifier, self.event_feed,
                                      proxy_url=self.config.clearnet_proxy)
        self.onion_monitor = OnionMonitor(
            self.onion_state, self.tor_checker, 
            self.notifier, self.event_feed
        )
        
        self.seizure_escalation = EscalationEngine(
            self.dns_state, self.notifier, self.event_feed,
            proxy_url=self.config.clearnet_proxy
        )
        
        self.http_monitor = HTTPMonitor(
            self.http_state, self.notifier, self.event_feed, 
            escalation=self.seizure_escalation,
            proxies=self.clearnet_proxies
        )
        self.whois_monitor = WHOISMonitor(
            self.whois_state, self.notifier, self.event_feed,
            escalation=self.seizure_escalation,
            proxies=self.clearnet_proxies,
            proxy_url=self.config.clearnet_proxy
        )
        self.ip_monitor = IPMonitor(
            self.ip_state, self.notifier, self.event_feed,
            escalation=self.seizure_escalation,
            proxy_url=self.config.clearnet_proxy
        )
        
        self.running = True
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, sig, frame):
        console.print(Padding(
            "[bold red]→ Shutting down...[/bold red]",
            (0, 0, 0, 4)
        ))
        self.running = False
        try:
            self.dns_state.save()
            self.onion_state.save()
            self.http_state.save()
            self.whois_state.save()
            self.ip_state.save()
            console.print(Padding(
                "[bold green]✓ All state files saved. Goodbye.[/bold green]",
                (0, 0, 0, 4)
            ))
        except Exception:
            console.print(Padding(
                "[bold yellow]⚠ Some state files may not have saved.[/bold yellow]",
                (0, 0, 0, 4)
            ))
        sys.exit(0)
    
    def _print_banner(self):
        banner = r"""
 ______ ____ _____  __          __   _       _         _             
|  ____|  _ \_   _| \ \        / /  | |     | |       | |            
| |__  | |_) || |    \ \  /\  / /_ _| |_ ___| |__   __| | ___   __ _  
|  __| |  _ < | |     \ \/  \/ / _` | __/ __| '_ \ / _` |/ _ \ / _` |
| |    | |_) || |_     \  /\  / (_| | || (__| | | | (_| | (_) | (_| |
|_|    |____/_____|     \/  \/ \__,_|\__\___|_| |_|\__,_|\___/ \__, |
                                                                __/ |
                                                               |___/  

           / \__                Catching seizure banners...
          (    @\___            before law enforcement...
          /         O           even realizes they exist.
         /   (_____/
        /_____/   U
"""
        console.print(Padding(f"[bold blue]{banner}[/bold blue]", (0, 0, 0, 4)))
        console.print(Padding(
            f"    [bold blue]FBI Watchdog v{VERSION} by [link=https://darkwebinformer.com]Dark Web Informer[/link][/bold blue]",
            (0, 0, 0, 4)
        ))
        console.print("")
        console.print(Padding("─" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold white]System Status[/bold white]",
            (0, 0, 0, 4)
        ))
        console.print(Padding("─" * 80, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold cyan]→ Monitoring {len(DOMAINS)} clearnet domains (DNS + HTTP + WHOIS)[/bold cyan]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold magenta]→ Monitoring {len(ONION_SITES)} .onion sites[/bold magenta]",
            (0, 0, 0, 4)
        ))
        
        monitors = []
        if self.enable_dns:
            monitors.append("[bold green]DNS ✓[/bold green]")
        else:
            monitors.append("[bold red]DNS ✗[/bold red]")
        if self.enable_http:
            monitors.append("[bold green]HTTP ✓[/bold green]")
        else:
            monitors.append("[bold red]HTTP ✗[/bold red]")
        if self.enable_whois:
            monitors.append("[bold green]WHOIS ✓[/bold green]")
        else:
            monitors.append("[bold red]WHOIS ✗[/bold red]")
        if self.enable_ip:
            monitors.append("[bold green]IP ✓[/bold green]")
        else:
            monitors.append("[bold red]IP ✗[/bold red]")
        if self.enable_onion:
            monitors.append("[bold green]Onion ✓[/bold green]")
        else:
            monitors.append("[bold red]Onion ✗[/bold red]")
        console.print(Padding(
            f"→ Monitors: {' | '.join(monitors)}",
            (0, 0, 0, 4)
        ))
        console.print(Padding(
            f"[bold yellow]→ Scan interval: {SCAN_INTERVAL} seconds[/bold yellow]",
            (0, 0, 0, 4)
        ))
        if self.clearnet_proxies:
            if self.config.proxy_ip and self.config.real_ip and self.config.proxy_ip != self.config.real_ip:
                console.print(Padding(
                    f"[bold green]→ Clearnet proxy: ✓ exit IP {self.config.proxy_ip} (real IP: {self.config.real_ip})[/bold green]",
                    (0, 0, 0, 4)
                ))
            elif self.config.proxy_ip and self.config.proxy_ip == self.config.real_ip:
                console.print(Padding(
                    f"[bold yellow]→ Clearnet proxy: ⚠ exit IP {self.config.proxy_ip} matches real IP[/bold yellow]",
                    (0, 0, 0, 4)
                ))
            else:
                console.print(Padding(
                    f"[bold cyan]→ Clearnet proxy: {self.config.clearnet_proxy}[/bold cyan]",
                    (0, 0, 0, 4)
                ))
        console.print(Padding("─" * 80, (0, 0, 0, 4)))
        console.print("")
    
    def run(self, silent_cycles: int = 1):
        self.dns_state.load()
        self.onion_state.load()
        self.http_state.load()
        self.whois_state.load()
        self.ip_state.load()
        
        self._print_banner()
        
        
        console.print("")
        console.print(Padding(
            "[bold green]✓ FBI Watchdog is now active and monitoring...[/bold green]",
            (0, 0, 0, 4)
        ))
        if silent_cycles > 0:
            cycle_word = "cycle" if silent_cycles == 1 else "cycles"
            console.print(Padding(
                f"[bold yellow]→ First {silent_cycles} {cycle_word} will run silent (state rebuild, no notifications)[/bold yellow]",
                (0, 0, 0, 4)
            ))
        console.print("")
        
        scan_count = 0
        
        while self.running:
            try:
                scan_count += 1
                is_silent = scan_count <= silent_cycles
                
                prev_d, prev_o = len(DOMAINS), len(ONION_SITES)
                new_d, new_o = site_manager.reload()
                if new_d != prev_d or new_o != prev_o:
                    console.print(Padding(
                        f"[bold cyan]↻ Sites reloaded: {new_d} clearnet ({new_d - prev_d:+d}), {new_o} onion ({new_o - prev_o:+d})[/bold cyan]",
                        (0, 0, 0, 4)
                    ))
                
                self.dns_monitor.silent = is_silent
                self.onion_monitor.silent = is_silent
                self.http_monitor.silent = is_silent
                self.whois_monitor.silent = is_silent
                self.ip_monitor.silent = is_silent
                
                console.print(Padding(
                    "━" * 80,
                    (0, 0, 0, 4)
                ))
                if is_silent:
                    console.print(Padding(
                        f"[bold yellow]Scan Cycle #{scan_count} (Silent {scan_count}/{silent_cycles}) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/bold yellow]",
                        (0, 0, 0, 4)
                    ))
                    console.print(Padding(
                        f"[dim]    Rebuilding state - notifications suppressed until cycle #{silent_cycles + 1}[/dim]",
                        (0, 0, 0, 4)
                    ))
                else:
                    console.print(Padding(
                        f"[bold white]Scan Cycle #{scan_count} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/bold white]",
                        (0, 0, 0, 4)
                    ))
                console.print(Padding(
                    "━" * 80,
                    (0, 0, 0, 4)
                ))
                console.print("")
                
                if self.enable_dns:
                    stats = self.dns_monitor.scan_all()
                    self.dns_state.save()
                
                if self.enable_http:
                    console.print(Padding(
                        "[dim]    Transitioning to HTTP fingerprint monitoring...[/dim]",
                        (0, 0, 0, 4)
                    ))
                    time.sleep(1)
                    
                    http_stats = self.http_monitor.scan_all()
                    self.http_state.save()
                
                if self.enable_whois:
                    console.print(Padding(
                        "[dim]    Transitioning to WHOIS monitoring...[/dim]",
                        (0, 0, 0, 4)
                    ))
                    time.sleep(1)
                    
                    whois_stats = self.whois_monitor.scan_all()
                    self.whois_state.save()
                
                if self.enable_ip:
                    console.print(Padding(
                        "[dim]    Transitioning to IP change monitoring...[/dim]",
                        (0, 0, 0, 4)
                    ))
                    time.sleep(1)
                    
                    ip_stats = self.ip_monitor.scan_all()
                    self.ip_state.save()
                
                if self.enable_onion:
                    console.print(Padding(
                        "[dim]    Transitioning to onion monitoring...[/dim]",
                        (0, 0, 0, 4)
                    ))
                    time.sleep(2)
                    
                    if self.tor_checker.check():
                        self.onion_monitor.scan_all()
                        self.onion_state.save()
                    else:
                        console.print(Padding(
                            "[bold yellow]⚠ Skipping onion monitoring: Tor not available[/bold yellow]",
                            (0, 0, 0, 4)
                        ))
                        console.print("")
                
                console.print(Padding(
                    f"[bold green]✓ Scan cycle complete.[/bold green]",
                    (0, 0, 0, 4)
                ))
                console.print("")
                console.print(Padding(
                    f"[bold green]→ Sleeping for {SCAN_INTERVAL} seconds...[/bold green]",
                    (0, 0, 0, 4)
                ))
                console.print("")
                time.sleep(SCAN_INTERVAL)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(Padding(
                    f"[bold red]✗ Error in scan cycle: {e}[/bold red]",
                    (0, 0, 0, 4)
                ))
                console.print(Padding(
                    f"[bold yellow]→ Retrying in {SCAN_INTERVAL} seconds...[/bold yellow]",
                    (0, 0, 0, 4)
                ))
                time.sleep(SCAN_INTERVAL)


def show_startup_menu() -> dict:
    banner = r"""
 ______ ____ _____  __          __   _       _         _             
|  ____|  _ \_   _| \ \        / /  | |     | |       | |            
| |__  | |_) || |    \ \  /\  / /_ _| |_ ___| |__   __| | ___   __ _  
|  __| |  _ < | |     \ \/  \/ / _` | __/ __| '_ \ / _` |/ _ \ / _` |
| |    | |_) || |_     \  /\  / (_| | || (__| | | | (_| | (_) | (_| |
|_|    |____/_____|     \/  \/ \__,_|\__\___|_| |_|\__,_|\___/ \__, |
                                                                __/ |
                                                               |___/  

           / \__                Catching seizure banners...
          (    @\___            before law enforcement...
          /         O           even realizes they exist.
         /   (_____/
        /_____/   U
"""
    console.print(Padding(f"[bold blue]{banner}[/bold blue]", (0, 0, 0, 4)))
    console.print(Padding("─" * 60, (0, 0, 0, 4)))
    console.print(Padding(
        f"[bold white]FBI Watchdog v{VERSION} - Startup Menu[/bold white]",
        (0, 0, 0, 4)
    ))
    console.print(Padding(
        f"    [bold blue]by [link=https://darkwebinformer.com]Dark Web Informer[/link][/bold blue]",
        (0, 0, 0, 4)
    ))
    console.print(Padding("─" * 60, (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold white]  1.[/bold white] [green]Start normally[/green]                (notifications active immediately)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  2.[/bold white] [yellow]Start in silent mode[/yellow]          (first cycle rebuilds state, no alerts)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  3.[/bold white] [cyan]Reset state & start silent[/cyan]    (wipe state files, fresh baseline)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  4.[/bold white] [magenta]View current state stats[/magenta]      (show what's tracked, then return)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  5.[/bold white] [blue]Manage monitored sites[/blue]        (add, remove, or list sites)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  6.[/bold white] [white]Toggle monitors[/white]               (enable/disable DNS, HTTP, WHOIS, IP, Onion)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  7.[/bold white] [white]CLI flags reference[/white]           (show command line options for PM2/scripts)", (0, 0, 0, 4)))
    console.print(Padding("[bold white]  8.[/bold white] [red]Exit[/red]", (0, 0, 0, 4)))
    console.print("")
    
    while True:
        try:
            choice = input("    Select [1-8]: ").strip()
        except (EOFError, KeyboardInterrupt):
            return {"action": "exit"}
        
        if choice == "1":
            return {"action": "run", "silent_cycles": 0}
        elif choice == "2":
            try:
                count = input("    How many silent cycles? [1]: ").strip()
                silent_cycles = int(count) if count else 1
                if silent_cycles < 1:
                    silent_cycles = 1
            except (ValueError, EOFError, KeyboardInterrupt):
                silent_cycles = 1
            return {"action": "run", "silent_cycles": silent_cycles}
        elif choice == "3":
            return {"action": "reset_and_run"}
        elif choice == "4":
            return {"action": "view_stats"}
        elif choice == "5":
            return {"action": "manage_sites"}
        elif choice == "6":
            return {"action": "toggle_monitors"}
        elif choice == "7":
            return {"action": "cli_reference"}
        elif choice == "8":
            return {"action": "exit"}
        else:
            console.print(Padding("[red]    Invalid choice, try again[/red]", (0, 0, 0, 4)))


def manage_sites_menu():
    global DOMAINS, ONION_SITES
    
    while True:
        console.print("")
        console.print(Padding("─" * 60, (0, 0, 0, 4)))
        console.print(Padding("[bold white]Manage Monitored Sites[/bold white]", (0, 0, 0, 4)))
        console.print(Padding("─" * 60, (0, 0, 0, 4)))
        console.print(Padding(
            f"[bold cyan]  Clearnet: {len(DOMAINS)} domains[/bold cyan]  [bold magenta]Onion: {len(ONION_SITES)} sites[/bold magenta]",
            (0, 0, 0, 4)
        ))
        console.print(Padding(f"[dim]  Source: {SITES_FILE}[/dim]", (0, 0, 0, 4)))
        console.print("")
        console.print(Padding("[bold white]  1.[/bold white] [green]Add a site[/green]", (0, 0, 0, 4)))
        console.print(Padding("[bold white]  2.[/bold white] [red]Remove a site[/red]", (0, 0, 0, 4)))
        console.print(Padding("[bold white]  3.[/bold white] [cyan]List all clearnet domains[/cyan]", (0, 0, 0, 4)))
        console.print(Padding("[bold white]  4.[/bold white] [magenta]List all onion sites[/magenta]", (0, 0, 0, 4)))
        console.print(Padding("[bold white]  5.[/bold white] [dim]Back to main menu[/dim]", (0, 0, 0, 4)))
        console.print("")
        
        try:
            choice = input("    Select [1-5]: ").strip()
        except (EOFError, KeyboardInterrupt):
            return
        
        if choice == "1":
            _add_site_prompt()
        elif choice == "2":
            _remove_site_prompt()
        elif choice == "3":
            _list_sites(DOMAINS, "Clearnet Domains", "cyan")
        elif choice == "4":
            _list_sites(ONION_SITES, "Onion Sites", "magenta")
        elif choice == "5":
            return
        else:
            console.print(Padding("[red]    Invalid choice[/red]", (0, 0, 0, 4)))


def toggle_monitors_menu(monitor_flags: dict) -> dict:
    labels = {
        "enable_dns": "DNS",
        "enable_http": "HTTP Fingerprint",
        "enable_whois": "WHOIS",
        "enable_ip": "IP Changes",
        "enable_onion": "Onion Sites",
    }
    
    while True:
        console.print("")
        console.print(Padding("─" * 60, (0, 0, 0, 4)))
        console.print(Padding("[bold white]Toggle Monitors[/bold white]", (0, 0, 0, 4)))
        console.print(Padding("─" * 60, (0, 0, 0, 4)))
        console.print("")
        
        for i, (key, label) in enumerate(labels.items(), 1):
            enabled = monitor_flags[key]
            status = "[bold green]ON[/bold green]" if enabled else "[bold red]OFF[/bold red]"
            console.print(Padding(
                f"[bold white]  {i}.[/bold white] {label:<20} {status}",
                (0, 0, 0, 4)
            ))
        
        console.print(Padding(f"[bold white]  6.[/bold white] [dim]Back to main menu[/dim]", (0, 0, 0, 4)))
        console.print("")
        
        try:
            choice = input("    Toggle [1-6]: ").strip()
        except (EOFError, KeyboardInterrupt):
            return monitor_flags
        
        keys = list(labels.keys())
        if choice in ("1", "2", "3", "4", "5"):
            idx = int(choice) - 1
            key = keys[idx]
            monitor_flags[key] = not monitor_flags[key]
            label = labels[key]
            new_state = "ON" if monitor_flags[key] else "OFF"
            console.print(Padding(
                f"[bold yellow]    → {label} is now {new_state}[/bold yellow]",
                (0, 0, 0, 4)
            ))
        elif choice == "6":
            return monitor_flags
        else:
            console.print(Padding("[red]    Invalid choice[/red]", (0, 0, 0, 4)))


def _add_site_prompt():
    global DOMAINS, ONION_SITES
    
    console.print("")
    console.print(Padding(
        "[dim]    Enter domain or .onion address (or 'q' to cancel)[/dim]",
        (0, 0, 0, 4)
    ))
    console.print(Padding(
        "[dim]    Tip: paste multiple sites separated by commas[/dim]",
        (0, 0, 0, 4)
    ))
    console.print("")
    
    try:
        raw = input("    Site(s): ").strip()
    except (EOFError, KeyboardInterrupt):
        return
    
    if raw.lower() == 'q' or not raw:
        return
    
    sites = [s.strip() for s in raw.replace(",", " ").split() if s.strip()]
    
    for site in sites:
        site_type, success = site_manager.add_site(site)
        if site_type == "invalid":
            console.print(Padding(f"[red]    ✗ Invalid input: '{site}'[/red]", (0, 0, 0, 4)))
        elif success:
            label = "onion" if site_type == "onion" else "clearnet"
            console.print(Padding(f"[bold green]    ✓ Added {label} site: {site}[/bold green]", (0, 0, 0, 4)))
        else:
            console.print(Padding(f"[yellow]    ⚠ Already monitored: {site}[/yellow]", (0, 0, 0, 4)))
    
    DOMAINS = site_manager.domains
    ONION_SITES = site_manager.onion_sites


def _remove_site_prompt():
    global DOMAINS, ONION_SITES
    
    console.print("")
    console.print(Padding(
        "[dim]    Enter domain or .onion address to remove (or 'q' to cancel)[/dim]",
        (0, 0, 0, 4)
    ))
    console.print("")
    
    try:
        raw = input("    Site(s): ").strip()
    except (EOFError, KeyboardInterrupt):
        return
    
    if raw.lower() == 'q' or not raw:
        return
    
    sites = [s.strip() for s in raw.replace(",", " ").split() if s.strip()]
    
    for site in sites:
        site_type, success = site_manager.remove_site(site)
        if site_type == "invalid":
            console.print(Padding(f"[red]    ✗ Invalid input: '{site}'[/red]", (0, 0, 0, 4)))
        elif success:
            label = "onion" if site_type == "onion" else "clearnet"
            console.print(Padding(f"[bold red]    ✓ Removed {label} site: {site}[/bold red]", (0, 0, 0, 4)))
        else:
            console.print(Padding(f"[yellow]    ⚠ Not found in monitored sites: {site}[/yellow]", (0, 0, 0, 4)))
    
    DOMAINS = site_manager.domains
    ONION_SITES = site_manager.onion_sites


def _list_sites(sites: list, title: str, color: str):
    console.print("")
    console.print(Padding(f"[bold {color}]  {title} ({len(sites)} total)[/bold {color}]", (0, 0, 0, 4)))
    console.print(Padding(f"[{color}]  {'─' * 55}[/{color}]", (0, 0, 0, 4)))
    
    for i, site in enumerate(sites, 1):
        console.print(Padding(f"[dim]  {i:>3}.[/dim] {site}", (0, 0, 0, 4)))
    
    console.print(Padding(f"[dim]  Source: {SITES_FILE}[/dim]", (0, 0, 0, 4)))
    console.print("")


def show_cli_reference():
    console.print("")
    console.print(Padding("─" * 65, (0, 0, 0, 4)))
    console.print(Padding("[bold white]CLI Flags Reference[/bold white]", (0, 0, 0, 4)))
    console.print(Padding(
        f"    [bold blue]by [link=https://darkwebinformer.com]Dark Web Informer[/link][/bold blue]",
        (0, 0, 0, 4)
    ))
    console.print(Padding("─" * 65, (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold cyan]Startup Modes[/bold cyan]", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--silent[/bold white]       First cycle rebuilds state, no notifications", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--loud[/bold white]         Notifications active from cycle 1", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-menu[/bold white]      Skip interactive menu (for PM2/systemd)", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--reset[/bold white]        Wipe state files before starting (implies --silent)", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold cyan]Site Management[/bold cyan]", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--add SITE ...[/bold white] Add one or more sites (clearnet or .onion)", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--remove SITE ...[/bold white] Remove one or more sites", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--list-sites[/bold white]   List all monitored sites and exit", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold cyan]Monitor Toggles[/bold cyan]", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-dns[/bold white]       Disable DNS monitoring", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-http[/bold white]      Disable HTTP fingerprint monitoring", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-whois[/bold white]     Disable WHOIS monitoring", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-ip[/bold white]        Disable IP change monitoring", (0, 0, 0, 4)))
    console.print(Padding("  [bold white]--no-onion[/bold white]     Disable onion site monitoring", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold cyan]PM2 Examples[/bold cyan]", (0, 0, 0, 4)))
    console.print(Padding("[dim]  # Start with silent first cycle (default for PM2)[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --silent", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # Start with notifications hot from cycle 1[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --loud", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # Full reset and restart[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --reset", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[bold cyan]Quick Commands (run without starting the watchdog)[/bold cyan]", (0, 0, 0, 4)))
    console.print(Padding("[dim]  # Add sites[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  python3 fbi_watchdog.py --add newsite.cc somemarket.onion", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # Remove sites[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  python3 fbi_watchdog.py --remove oldsite.cc", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # List everything[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  python3 fbi_watchdog.py --list-sites", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # Add and immediately start[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  python3 fbi_watchdog.py --add newsite.cc --no-menu --loud", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("[dim]  # Start with only DNS and onion monitoring[/dim]", (0, 0, 0, 4)))
    console.print(Padding("  pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --silent --no-http --no-whois --no-ip", (0, 0, 0, 4)))
    console.print("")
    console.print(Padding("─" * 65, (0, 0, 0, 4)))
    console.print("")
    try:
        input("    Press Enter to return to menu...")
    except (EOFError, KeyboardInterrupt):
        pass


def show_state_stats():
    console.print("")
    console.print(Padding("─" * 60, (0, 0, 0, 4)))
    console.print(Padding("[bold white]Current State[/bold white]", (0, 0, 0, 4)))
    console.print(Padding("─" * 60, (0, 0, 0, 4)))
    
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                dns_data = json.load(f)
            domain_count = len(dns_data)
            record_count = sum(len(v) for v in dns_data.values() if isinstance(v, dict))
            console.print(Padding(
                f"[bold cyan]  DNS State:[/bold cyan] {domain_count} domains, {record_count} record sets tracked",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[dim]  File: {STATE_FILE} ({STATE_FILE.stat().st_size:,} bytes)[/dim]",
                (0, 0, 0, 4)
            ))
        except Exception as e:
            console.print(Padding(f"[red]  DNS State: Error reading - {e}[/red]", (0, 0, 0, 4)))
    else:
        console.print(Padding("[yellow]  DNS State: No state file found (first run)[/yellow]", (0, 0, 0, 4)))
    
    if ONION_STATE_FILE.exists():
        try:
            with open(ONION_STATE_FILE, 'r', encoding='utf-8') as f:
                onion_data = json.load(f)
            total = len(onion_data)
            statuses = defaultdict(int)
            for site_data in onion_data.values():
                if isinstance(site_data, dict):
                    statuses[site_data.get("status", "unknown")] += 1
            status_str = "  ".join(f"{k}: {v}" for k, v in sorted(statuses.items()))
            console.print(Padding(
                f"[bold magenta]  Onion State:[/bold magenta] {total} sites - {status_str}",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[dim]  File: {ONION_STATE_FILE} ({ONION_STATE_FILE.stat().st_size:,} bytes)[/dim]",
                (0, 0, 0, 4)
            ))
        except Exception as e:
            console.print(Padding(f"[red]  Onion State: Error reading - {e}[/red]", (0, 0, 0, 4)))
    else:
        console.print(Padding("[yellow]  Onion State: No state file found (first run)[/yellow]", (0, 0, 0, 4)))
    
    if HTTP_STATE_FILE.exists():
        try:
            with open(HTTP_STATE_FILE, 'r', encoding='utf-8') as f:
                http_data = json.load(f)
            http_count = len(http_data)
            console.print(Padding(
                f"[bold white]  HTTP State:[/bold white] {http_count} domains fingerprinted",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[dim]  File: {HTTP_STATE_FILE} ({HTTP_STATE_FILE.stat().st_size:,} bytes)[/dim]",
                (0, 0, 0, 4)
            ))
        except Exception as e:
            console.print(Padding(f"[red]  HTTP State: Error reading - {e}[/red]", (0, 0, 0, 4)))
    else:
        console.print(Padding("[yellow]  HTTP State: No state file found (first run)[/yellow]", (0, 0, 0, 4)))
    
    if WHOIS_STATE_FILE.exists():
        try:
            with open(WHOIS_STATE_FILE, 'r', encoding='utf-8') as f:
                whois_data = json.load(f)
            whois_count = len(whois_data)
            seizure_count = sum(
                1 for v in whois_data.values()
                if isinstance(v, dict) and v.get("seizure_indicators")
            )
            seizure_info = f"  ({seizure_count} with seizure indicators)" if seizure_count else ""
            console.print(Padding(
                f"[bold green]  WHOIS State:[/bold green] {whois_count} domains tracked{seizure_info}",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[dim]  File: {WHOIS_STATE_FILE} ({WHOIS_STATE_FILE.stat().st_size:,} bytes)[/dim]",
                (0, 0, 0, 4)
            ))
        except Exception as e:
            console.print(Padding(f"[red]  WHOIS State: Error reading - {e}[/red]", (0, 0, 0, 4)))
    else:
        console.print(Padding("[yellow]  WHOIS State: No state file found (first run)[/yellow]", (0, 0, 0, 4)))
    
    if IP_STATE_FILE.exists():
        try:
            with open(IP_STATE_FILE, 'r', encoding='utf-8') as f:
                ip_data = json.load(f)
            ip_count = len(ip_data)
            console.print(Padding(
                f"[bold yellow]  IP State:[/bold yellow] {ip_count} domains tracked",
                (0, 0, 0, 4)
            ))
            console.print(Padding(
                f"[dim]  File: {IP_STATE_FILE} ({IP_STATE_FILE.stat().st_size:,} bytes)[/dim]",
                (0, 0, 0, 4)
            ))
        except Exception as e:
            console.print(Padding(f"[red]  IP State: Error reading - {e}[/red]", (0, 0, 0, 4)))
    else:
        console.print(Padding("[yellow]  IP State: No state file found (first run)[/yellow]", (0, 0, 0, 4)))
    
    console.print(Padding("─" * 60, (0, 0, 0, 4)))
    console.print("")
    try:
        input("    Press Enter to return to menu...")
    except (EOFError, KeyboardInterrupt):
        pass


def reset_state_files():
    for f in [STATE_FILE, ONION_STATE_FILE, HTTP_STATE_FILE, WHOIS_STATE_FILE, IP_STATE_FILE]:
        if f.exists():
            f.unlink()
            console.print(Padding(f"[yellow]  Deleted {f}[/yellow]", (0, 0, 0, 4)))
        else:
            console.print(Padding(f"[dim]  {f} - already clean[/dim]", (0, 0, 0, 4)))


def parse_args():
    parser = argparse.ArgumentParser(description=f"FBI Watchdog v{VERSION}")
    parser.add_argument(
        "--silent", nargs="?", const=1, type=int, default=0, metavar="N",
        help="Run N silent cycles before enabling notifications (default: 1 if flag used)"
    )
    parser.add_argument(
        "--loud", action="store_true",
        help="Start with notifications active immediately (no silent first cycle)"
    )
    parser.add_argument(
        "--reset", action="store_true",
        help="Reset state files before starting (implies --silent)"
    )
    parser.add_argument(
        "--no-menu", action="store_true",
        help="Skip interactive menu (for PM2/daemon usage). Defaults to --silent if neither --silent nor --loud specified"
    )
    parser.add_argument(
        "--add", nargs="+", metavar="SITE",
        help="Add one or more sites to monitoring (clearnet or .onion)"
    )
    parser.add_argument(
        "--remove", nargs="+", metavar="SITE",
        help="Remove one or more sites from monitoring"
    )
    parser.add_argument(
        "--list-sites", action="store_true",
        help="List all monitored sites and exit"
    )
    parser.add_argument(
        "--no-dns", action="store_true",
        help="Disable DNS monitoring"
    )
    parser.add_argument(
        "--no-http", action="store_true",
        help="Disable HTTP fingerprint monitoring"
    )
    parser.add_argument(
        "--no-whois", action="store_true",
        help="Disable WHOIS monitoring"
    )
    parser.add_argument(
        "--no-ip", action="store_true",
        help="Disable IP change monitoring"
    )
    parser.add_argument(
        "--no-onion", action="store_true",
        help="Disable onion site monitoring"
    )
    parser.add_argument(
        "--proxy", metavar="URL",
        help="SOCKS5 proxy for clearnet requests (e.g. socks5h://127.0.0.1:1080). Overrides CLEARNET_PROXY env var"
    )
    return parser.parse_args()


def main():
    global DOMAINS, ONION_SITES
    
    try:
        args = parse_args()
        
        if args.list_sites:
            console.print("")
            _list_sites(DOMAINS, "Clearnet Domains", "cyan")
            _list_sites(ONION_SITES, "Onion Sites", "magenta")
            sys.exit(0)
        
        if args.add:
            console.print("")
            for site in args.add:
                site_type, success = site_manager.add_site(site)
                if site_type == "invalid":
                    console.print(Padding(f"[red]  ✗ Invalid: '{site}'[/red]", (0, 0, 0, 4)))
                elif success:
                    label = "onion" if site_type == "onion" else "clearnet"
                    console.print(Padding(f"[bold green]  ✓ Added {label}: {site}[/bold green]", (0, 0, 0, 4)))
                else:
                    console.print(Padding(f"[yellow]  ⚠ Already monitored: {site}[/yellow]", (0, 0, 0, 4)))
            DOMAINS = site_manager.domains
            ONION_SITES = site_manager.onion_sites
            console.print("")
            if not args.no_menu and not args.loud and not args.silent and not args.reset:
                sys.exit(0)
        
        if args.remove:
            console.print("")
            for site in args.remove:
                site_type, success = site_manager.remove_site(site)
                if site_type == "invalid":
                    console.print(Padding(f"[red]  ✗ Invalid: '{site}'[/red]", (0, 0, 0, 4)))
                elif success:
                    label = "onion" if site_type == "onion" else "clearnet"
                    console.print(Padding(f"[bold red]  ✓ Removed {label}: {site}[/bold red]", (0, 0, 0, 4)))
                else:
                    console.print(Padding(f"[yellow]  ⚠ Not found: {site}[/yellow]", (0, 0, 0, 4)))
            DOMAINS = site_manager.domains
            ONION_SITES = site_manager.onion_sites
            console.print("")
            if not args.no_menu and not args.loud and not args.silent and not args.reset:
                sys.exit(0)
        
        monitor_flags = {
            "enable_dns": not args.no_dns,
            "enable_http": not args.no_http,
            "enable_whois": not args.no_whois,
            "enable_ip": not args.no_ip,
            "enable_onion": not args.no_onion,
        }
        
        if args.proxy:
            os.environ["CLEARNET_PROXY"] = args.proxy
        
        if args.no_menu or not sys.stdin.isatty():
            if args.reset:
                reset_state_files()
            
            if args.loud:
                silent_cycles = 0
            elif args.silent:
                silent_cycles = args.silent
            else:
                silent_cycles = 1
            
            watchdog = DWIWatchdog(**monitor_flags)
            watchdog.run(silent_cycles=silent_cycles)
            return
        
        while True:
            result = show_startup_menu()
            
            if result["action"] == "exit":
                console.print(Padding("[bold red]→ Exiting.[/bold red]", (0, 0, 0, 4)))
                sys.exit(0)
            
            elif result["action"] == "view_stats":
                show_state_stats()
                continue
            
            elif result["action"] == "manage_sites":
                manage_sites_menu()
                continue
            
            elif result["action"] == "cli_reference":
                show_cli_reference()
                continue
            
            elif result["action"] == "toggle_monitors":
                monitor_flags = toggle_monitors_menu(monitor_flags)
                continue
            
            elif result["action"] == "reset_and_run":
                console.print("")
                reset_state_files()
                console.print("")
                watchdog = DWIWatchdog(**monitor_flags)
                watchdog.run(silent_cycles=1)
                return
            
            elif result["action"] == "run":
                watchdog = DWIWatchdog(**monitor_flags)
                watchdog.run(silent_cycles=result["silent_cycles"])
                return
        
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Dark Web Informer - Cyber Threat Intelligence

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `monitored_sites.example.json`
```json
{
  "domains": [
    "example.com",
    "anotherdomain.org"
  ],
  "onion_sites": [
    "exampleonion1234abcdef5678.onion"
  ]
}
```

## File: `README.md`
```markdown
<p align="center">
  <img src="screenshots/fbi_watchdog_banner.png" alt="FBI Watchdog Banner" width="700">
</p>

<h1 align="center">FBI Watchdog</h1>

<p align="center">
  <strong>Domain seizure detection and monitoring tool for cyber threat intelligence</strong>
</p>

<p align="center">
  <a href="https://darkwebinformer.com">DarkWebInformer.com</a> ·
  <a href="https://x.com/DarkWebInformer">@DarkWebInformer</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/python-3.9+-yellow" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

---

FBI Watchdog is a multi-layered domain monitoring tool that detects law enforcement seizures, DNS changes, HTTP fingerprint shifts, WHOIS record mutations, and IP address changes across clearnet domains and Tor onion sites. Built for threat intelligence analysts, security researchers, and anyone tracking domain infrastructure changes in real time.

When a seizure signal is detected across any monitor, the tool triggers a cross-monitor escalation audit, captures a screenshot of the seized page, and sends consolidated alerts to Discord and Telegram with full evidence.

<p align="center">
  <img src="screenshots/scan_cycle.png" alt="Scan Cycle">
</p>

---

## Features

- **DNS Monitoring** - Tracks A, AAAA, CNAME, MX, NS, and TXT records across all monitored domains. Detects never-before-seen record combinations and flags seizure-related DNS entries (e.g., `fbi.seized`, `seized.gov`, `usssdomainseizure`). SOA was taken out during testing because it was loud. Add it back in the script if you need it.

- **HTTP Fingerprint Monitoring** - Fingerprints server headers, status codes, body content hashes, redirect chains, and page size. Detects seizure keywords in page content, redirect-to-government patterns, and simultaneous server + body changes that indicate infrastructure takeover.

- **WHOIS Monitoring** - Tracks registrar, nameservers, registrant organization, status codes (EPP), and creation/expiration dates. Detects seizure indicators in WHOIS data including law enforcement registrar changes, server prohibition flags, and known LE Cloudflare nameservers.

- **IP Change Monitoring** - Monitors A and AAAA record IP addresses with reverse DNS lookups. Classifies changes as CDN rotation, hosting migration, provider change, or seizure signal based on rDNS matching against known law enforcement infrastructure.

- **Onion Site Monitoring** - Connects via Tor to monitor `.onion` sites for seizure banners. Supports automatic Tor circuit rotation on connection failures. Detects seizure keywords from FBI, Europol, BKA, AFP, Garda, RCMP, Polisen, and other international law enforcement agencies.

- **Cross-Monitor Seizure Escalation** - When any single monitor detects a seizure signal, an escalation engine triggers a full audit across all monitors, captures a screenshot, and sends a consolidated multi-evidence alert.

- **Automated Screenshot Capture** - Uses headless Chromium via Playwright to capture full-page screenshots of seized domains, attached to Discord and Telegram notifications.

- **Discord & Telegram Alerts** - Real-time notifications with rich embeds (Discord) and formatted messages (Telegram). Screenshots are attached directly to seizure alerts.

- **Silent Mode** - First scan cycle(s) can run silent to build a baseline state without triggering notifications. Prevents alert floods on first run or after a state reset.

- **Event Feed** - Maintains a rolling JSON event feed of all detected changes, baselines, and seizure events for external consumption or dashboard integration.

- **Hot Reload** - Monitored sites list is re-read from disk every scan cycle. Add or remove sites without restarting the watchdog.

- **SOCKS5 Proxy Support** - Route all clearnet HTTP/WHOIS requests through a SOCKS5 proxy. Proxy exit IP is validated against your real IP on startup. Note: screenshot capture via Playwright does not support SOCKS5 proxies with authentication and will fall back to a direct connection if proxy auth is configured. All other requests (HTTP, WHOIS, DNS, IP) work normally with authenticated proxies.

<table>
  <tr>
    <td><img src="screenshots/discord_alert.png" alt="Discord Alert" width="400"></td>
    <td><img src="screenshots/telegram_alert.png" alt="Telegram Alert" width="400"></td>
  </tr>
</table>

<p align="center">Real notifications captured during the LeakBase domain forum seizure by law enforcement.</p>

---

## FBI Watchdog Live Feed

A live, continuously updated feed powered by this tool is available at [darkwebinformer.com/fbi-watchdog-feed](https://darkwebinformer.com/fbi-watchdog-feed). The feed displays real-time seizure detections, DNS changes, HTTP fingerprint shifts, WHOIS mutations, and IP changes as they are detected across monitored domains and onion sites.

The live feed is available exclusively to paying subscribers of [Dark Web Informer](https://darkwebinformer.com/pricing).

---

## Architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│                          FBI Watchdog v3.0.0                          │
├─────────────┬──────────────┬───────────────┬───────────┬──────────────┤
│ DNS Monitor │ HTTP Monitor │ WHOIS Monitor │IP Monitor │Onion Monitor │
│ (dnspython) │  (requests)  │(python-whois) │(dnspython)│ (Tor SOCKS)  │
├─────────────┴──────────────┴───────────────┴───────────┴──────────────┤
│                           Escalation Engine                           │
│              (Cross-monitor audit + screenshot capture)               │
├───────────────────────────────────┬───────────────────────────────────┤
│         Discord Webhooks          │         Telegram Bot API          │
├─────────────────────┬─────────────┴─────────────┬─────────────────────┤
│ State Files (JSON)  │     Event Feed (JSON)     │  Screenshots (PNG)  │
└─────────────────────┴───────────────────────────┴─────────────────────┘
```

---

## Requirements

- Python 3.9+
- Tor (for onion site monitoring)
- Chromium (installed via Playwright for screenshot capture)

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/DarkWebInformer/FBIWatchdog.git
cd FBIWatchdog
```

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**3. Install Playwright browsers**

```bash
playwright install chromium
```

**4. Configure environment variables**

```bash
cp .env.example .env
chmod 600 .env
```

Edit `.env` and add your Discord webhook URL, Telegram credentials, or both. All notification channels are optional - the watchdog runs without any configured.

**5. Add sites to monitor**

```bash
python3 fbi_watchdog.py --add example.com anothersite.org somehiddenservice.onion
```

Or edit `monitored_sites.json` directly (see `monitored_sites.example.json` for format).

**6. Run**

```bash
python3 fbi_watchdog.py
```

---

## Configuration

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `WEBHOOKFBIWATCHDOG` | No | Discord webhook URL (`https://discord.com/api/webhooks/...`) |
| `TELEGRAM_BOT_TOKEN` | No | Telegram bot token for alert delivery |
| `TELEGRAM_CHAT_ID` | No | Telegram chat/channel ID for alerts |
| `CLEARNET_PROXY` | No | SOCKS5 proxy for clearnet requests (e.g., `socks5h://127.0.0.1:1080`). When configured, startup validation makes two requests to `api.ipify.org` to verify the proxy exit IP differs from your real IP. |

All notification channels are optional. Configure Discord, Telegram, both, or neither. Without any notification channels, the watchdog still runs and logs all detections to the console and event feed JSON.

### Monitored Sites

Sites are stored in `monitored_sites.json` and can be managed via CLI flags or the interactive menu:

```json
{
  "domains": [
    "example.com",
    "anotherdomain.org"
  ],
  "onion_sites": [
    "exampleonion1234.onion"
  ]
}
```

Sites are validated on add and reload. Invalid entries (malformed domains, path traversal attempts) are rejected.

The sites file is hot-reloaded every scan cycle - you can edit it while the watchdog is running.

---

## Usage

### Interactive Menu

```bash
python3 fbi_watchdog.py
```

Launches an interactive menu where you can start monitoring, manage sites, toggle individual monitors, view state stats, reset state files, and see the CLI reference.

![Menu](screenshots/startup_menu.png)

### Headless / PM2

```bash
# Start with 1 silent baseline cycle (default)
python3 fbi_watchdog.py --no-menu --silent

# Start with notifications active from cycle 1
python3 fbi_watchdog.py --no-menu --loud

# Reset all state and start fresh
python3 fbi_watchdog.py --no-menu --reset

# Disable specific monitors
python3 fbi_watchdog.py --no-menu --silent --no-whois --no-ip

# Route clearnet requests through a proxy
python3 fbi_watchdog.py --no-menu --silent --proxy socks5h://127.0.0.1:1080
```

### PM2 Examples

```bash
# Standard deployment
pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --silent

# Notifications hot from cycle 1
pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --loud

# Full reset and restart
pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --reset

# DNS and onion monitoring only
pm2 start fbi_watchdog.py --interpreter python3 -- --no-menu --silent --no-http --no-whois --no-ip
```

### Site Management (CLI)

```bash
# Add sites
python3 fbi_watchdog.py --add newsite.cc somemarket.onion

# Remove sites
python3 fbi_watchdog.py --remove oldsite.cc

# List all monitored sites
python3 fbi_watchdog.py --list-sites
```

### CLI Flags Reference

| Flag | Description |
|---|---|
| `--silent [N]` | Run N silent cycles before enabling notifications (default: 1) |
| `--loud` | Start with notifications active immediately |
| `--no-menu` | Skip interactive menu (for PM2/systemd/daemon usage) |
| `--reset` | Wipe all state files before starting (implies `--silent`) |
| `--add SITE [...]` | Add one or more sites to monitoring |
| `--remove SITE [...]` | Remove one or more sites from monitoring |
| `--list-sites` | List all monitored sites and exit |
| `--no-dns` | Disable DNS monitoring |
| `--no-http` | Disable HTTP fingerprint monitoring |
| `--no-whois` | Disable WHOIS monitoring |
| `--no-ip` | Disable IP change monitoring |
| `--no-onion` | Disable onion site monitoring |
| `--proxy URL` | SOCKS5 proxy for clearnet requests (overrides `CLEARNET_PROXY` env var) |

---

## Monitors

### DNS Monitor

Queries A, AAAA, CNAME, MX, NS, and TXT records for each clearnet domain. Maintains a history of up to 10 unique record sets per domain/record type. Fires an alert when a never-before-seen record combination appears.

Seizure-specific DNS indicators (e.g., `fbi.seized`, `seized.gov`, `europol`, `usssdomainseizure`) trigger immediate seizure alerts with screenshot capture.

### HTTP Fingerprint Monitor

Fetches each domain over HTTPS (falling back to HTTP) and fingerprints tracked response headers (`server`, `x-powered-by`, `strict-transport-security`, `via`, `x-cdn`, etc.), status code, final URL after redirects, and a SHA-256 hash of the response body.

Change detection filters out noise from transient HTTP errors (502-524), Cloudflare/DDoS-Guard challenge pages, and minor body fluctuations (under 35% size change). Runs fetches in parallel (10 concurrent by default).

Seizure signals include government domain redirects, seizure keywords in page content, simultaneous server header + body changes, and status code changes to 403/451.

### WHOIS Monitor

Queries WHOIS data for each clearnet domain and tracks registrar, nameservers, registrant organization, registrant country, EPP status codes, and key dates. Runs lookups in parallel (5 concurrent by default).

Normalizes registrar names (e.g., "Tucows Domains Inc." → "tucows"), strips ICANN EPP URL prefixes from status codes, deduplicates compound EPP tokens, and filters out privacy-service org changes to reduce false positives. Includes a state migration system that re-normalizes stored records when normalization logic changes between versions.

Seizure indicators include law enforcement keywords in WHOIS data, known LE Cloudflare nameservers paired with server prohibition flags, and registrar changes to government entities.

### IP Monitor

Resolves A and AAAA records and tracks IP address changes across scan cycles. Performs reverse DNS on new IPs and classifies changes into categories: CDN rotation (same provider, different IP pool), hosting migration (complete IP replacement), provider change (CDN swap or CDN removal), and seizure signal (rDNS matching known law enforcement infrastructure like `fbi.gov`, `justice.gov`, `europol`, etc.).

### Onion Monitor

Connects to each `.onion` site via Tor SOCKS proxy, downloads page content (capped at 5MB), and scans for seizure keywords from international law enforcement agencies. Supports automatic Tor circuit rotation on connection failures or timeouts, with a single retry on a fresh circuit.

### Seizure Escalation Engine

When any monitor detects a seizure signal (not just a change - a signal with seizure-specific indicators), the escalation engine triggers a full cross-monitor audit:

1. Immediate DNS audit across all record types
2. Screenshot capture via headless Chromium
3. Consolidated alert sent to Discord and Telegram with evidence from all monitors

This ensures that a single seizure indicator triggers comprehensive evidence collection rather than a piecemeal alert.

---

## State Files

The watchdog maintains separate state files for each monitor:

| File | Contents |
|---|---|
| `fbi_watchdog_results.json` | DNS record history per domain |
| `http_watchdog_results.json` | HTTP fingerprints per domain |
| `whois_watchdog_results.json` | WHOIS records and seizure indicators |
| `ip_watchdog_results.json` | Current A/AAAA records per domain |
| `onion_watchdog_results.json` | Onion site status (active/seized/unreachable) |
| `event_feed.json` | Rolling event feed (last 500 events) |
| `monitored_sites.json` | List of monitored clearnet and onion sites |

All state files use atomic writes (write to temp file, then `os.replace`) to prevent corruption on crash or power loss.

State can be reset via `--reset` flag or the interactive menu.

---

## Tor Setup

Onion site monitoring requires a running Tor instance with SOCKS proxy on port 9050 (default) or 9150 (Tor Browser).

**Install Tor:**

```bash
# Debian/Ubuntu
sudo apt install tor

# Start the service
sudo systemctl start tor
sudo systemctl enable tor
```

**Optional: Enable circuit rotation**

To allow the watchdog to rotate Tor circuits on connection failures, enable the control port in `/etc/tor/torrc`:

```
ControlPort 9051
CookieAuthentication 0
```

Then restart Tor:

```bash
sudo systemctl restart tor
```

For shared servers, use `HashedControlPassword` instead of disabling cookie authentication:

```bash
tor --hash-password "your_password"
```

Add the output to `torrc` as `HashedControlPassword`.

The watchdog verifies Tor connectivity by checking `https://check.torproject.org/` through the SOCKS proxy before starting onion scans. If Tor is not running, onion monitoring is skipped gracefully.

![Onion Scan Cycle](screenshots/onion_scan.png)

---

## Security

- All credentials are loaded from environment variables via `.env` - nothing is hardcoded
- The `.env` file permission is checked on startup and warns if it is readable by other users
- Discord webhook URL is validated against `https://discord.com/api/webhooks/` prefix
- Telegram bot token and chat ID are format-validated before use
- SOCKS5 proxy URL is regex-validated and exit IP is tested against your real IP on startup
- Site input is validated with a strict regex, rejects path traversal and malformed domains
- Screenshot paths are validated against the screenshots directory to prevent path traversal
- HTTP responses are streamed with a 5MB cap to prevent memory exhaustion
- Onion responses are capped at 5MB
- Keyword scanning is limited to the first 1MB of body content
- All state files use atomic writes to prevent corruption
- Proxy credentials are sanitized from error messages before console output
- Playwright runs headless with JavaScript disabled, downloads disabled, and `--no-sandbox`
- Event IDs use `secrets.token_hex()` (cryptographically secure)
- Signal handlers ensure graceful shutdown with state file saves on SIGINT/SIGTERM

### External Network Calls

When `CLEARNET_PROXY` is configured, the watchdog makes two requests to `https://api.ipify.org` on startup: one through the proxy and one direct. This is used solely to verify the proxy is working by comparing exit IPs. No data is sent to `api.ipify.org` beyond a standard GET request. These calls only occur once at startup and only when a proxy is configured. During normal monitoring, the only external calls are DNS queries, HTTP requests to monitored domains, WHOIS lookups, Tor connectivity checks via `check.torproject.org`, and notification delivery to Discord/Telegram APIs.

---

## Support FBI Watchdog & Dark Web Informer

FBI Watchdog is an open-source project dedicated to cyber threat intelligence, monitoring seizure banners, and providing real-time insights. Your support helps keep this project running!

You can also get access to premium cyber threat intelligence on **[Dark Web Informer](https://darkwebinformer.com)**.

### Subscription Options:  
- **Standard and Crypto Subscription:** [Sign up here](https://darkwebinformer.com/pricing)

Stay ahead of the latest cyber threats with real-time intelligence.

### ❤️ Donate to Support Dark Web Informer's Work
If you find Dark Web Informer and/or FBI Watchdog valuable, consider making a **donation** to help future development, research, and cyber threat intelligence.
[Donate here](https://darkwebinformer.com/donations)

### Advertise With Dark Web Informer
Looking to **promote your cybersecurity services** or **reach the right audience**?
Check out the **advertising options** here: [Advertising Rates](https://darkwebinformer.com/advertising-rates)

Your support helps keep **FBI Watchdog** and **Dark Web Informer** independent and continuously improving. Thank you!

---

## Star History

<a href="https://star-history.com/#DarkWebInformer/FBI_Watchdog&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=DarkWebInformer/FBI_Watchdog&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=DarkWebInformer/FBI_Watchdog&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=DarkWebInformer/FBI_Watchdog&type=Date" />
 </picture>
</a>

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
  Built by <a href="https://darkwebinformer.com">Dark Web Informer</a>
</p>
```

## File: `requirements.txt`
```
dnspython
requests
python-dotenv
playwright
rich
python-whois
beautifulsoup4
PySocks
urllib3
```

## File: `_VET_REPORT.md`
```markdown
﻿# Strix Vet Report: fbi-watchdog
**Date:** 2026-03-17 11:06:36
**Status:** PASS
**Critical Findings:** 0
**Warnings:** 1

## Verdict

PASS - Repo passed all security checks. Safe to extract specific files into AI OS.

## Findings

| Level | Category | Detail | File |
|-------|----------|--------|------|
| WARN | SENSITIVE_ACCESS | .env file access | `D:\Project\QUARANTINE\fbi-watchdog\fbi_watchdog.py` |


## Next Step

Proceed to content extraction. Copy only needed files into D:\APP\AI OS\knowledge\ or relevant skill folder.
```

## File: `screenshots/.gitignore`
```

```


import json
import socket
import logging
from urllib.request import Request, urlopen
from urllib.error import URLError

import os

AI_OS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

class DualStreamRouter:
    """
    Implements 2-Stream architecture for Harbor endpoints:
    Luồng 1 (Local First): Checks Network port.
    Luồng 2 (Cloud Fallback): Resolves to Cloud API if local is dead or offline_mode=False.
    """
    def __init__(self):
        self.config_path = os.path.join(AI_OS_ROOT, "core", "ops", "scripts", "config.json")
        self.config = self._load_config()

    def _load_config(self) -> dict:
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                return json.load(f).get("services", {})
        except Exception as e:
            logging.error(f"[ROUTER] Config error: {e}")
            return {}

    def _is_local_port_alive(self, port: int) -> bool:
        """Pings local port silently to check if Local Service is running."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1.0)
                return s.connect_ex(('127.0.0.1', port)) == 0
        except Exception:
            return False

    def resolve_endpoint(self, service_name: str) -> dict:
        """
        Dynamically returns the best endpoint for 2-stream routing.
        Returns -> {"url": URL, "stream": "local" | "cloud"}
        """
        service = self.config.get(service_name)
        if not service:
            return {"url": None, "stream": "none", "error": f"Service {service_name} not registered."}

        stream_mode = service.get("stream_mode", "local_first")
        local_url = service.get("url") or service.get("url_api")
        local_port = service.get("port") or service.get("port_api")
        cloud_url = service.get("fallback_cloud")

        if stream_mode == "cloud_only" and cloud_url:
            return {"url": cloud_url, "stream": "cloud"}

        if local_port and self._is_local_port_alive(local_port):
            return {"url": local_url, "stream": "local"}

        # Failover logic to Cloud!
        if cloud_url:
            logging.warning(f"[ROUTER] DUAL-STREAM FAILOVER: {service_name} Local (Port {local_port}) is DOWN. Pivoting to Cloud!")
            return {"url": cloud_url, "stream": "cloud_fallback"}
        
        logging.error(f"[ROUTER] FATAL 502: {service_name} Local is DOWN and NO Cloud Fallback defined!")
        return {"url": None, "stream": "dead", "error": "502 Bad Gateway"}

# Global Export
router = DualStreamRouter()

if __name__ == "__main__":
    import sys
    test_svc = sys.argv[1] if len(sys.argv) > 1 else "lightrag"
    print(f"Resolving '{test_svc}'...")
    res = router.resolve_endpoint(test_svc)
    print(json.dumps(res, indent=4))

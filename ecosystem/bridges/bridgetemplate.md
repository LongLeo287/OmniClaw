---
id: bridge_template
type: template
namespace: ecosystem.bridges.template
---

# 🌉 Bridge Construction Protocol

Standardized construction protocol for creating "Bridges" in the OmniClaw ecosystem.

Bridges act as the perimeter control layer, representing **OBD Harbor** to launch and manage satellites (Satellites/Skills/Servers) in isolated mode.

### 📜 Mandatory Bridge Standards:
1. **Dynamic Parameter Acquisition:** The Port must be dynamically retrieved via `sys.argv[1]` as delegated by OBD Harbor.
2. **Graceful Shutdown Inheritance:** The Bridge must intercept `KeyboardInterrupt` to safely clean up its child processes. Avoid leaving Zombie Processes.
3. **Port Spoofing/Mocking Mechanism:** If the target application only runs in the background (e.g., `system_pulse.py` or a desktop app) without opening a network Socket, the Bridge MUST manually bind a dummy Socket on the assigned port so OBD Harbor's Heartbeat Ping can scan and register the `ONLINE` status.
4. **No Unauthorized 0.0.0.0:** By default, if configuring host flags, always enforce `--host 127.0.0.1`. Only change to `0.0.0.0` if strictly authorized by overriding network policies.

*Reference `bridgetemplate.py` to copy the standard initialization boilerplate.*

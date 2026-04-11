# 🌉 OmniClaw Bridges Architecture

[🇻🇳 Xem bản Tiếng Việt (Vietnamese)](README-vn.md)

**Bridges** are the strict perimeter firewalls and local gateways of the OmniClaw Artificial Intelligence Operating System (`v5.0`). 

Everything within this directory serves as a **Harbor Launch Script** exclusively governed by the **OBD Harbor** (OmniClaw Bridge Daemon). This directory enforces isolation, ensuring that no external or background process can start and expose a network connection into OmniClaw without Explicit Authorization via the OBD Console.

---

## 🛑 The Core Golden Rules

1. **You Are Not in Control:** Bridges are NOT meant to be double-clicked or executed manually by users. They are orchestrated asynchronously by `obd_harbor.py`.
2. **Ports are Delegated:** Do not hardcode execution ports inside the Bridge script (unless spoofing). The target port MUST be requested from OBD's launch argument (`sys.argv[1]`), configured globally in `core/config/config.json`.
3. **Ghost Prevention (No Zombies):** 
   - A Bridge must intercept `KeyboardInterrupt` / SIGTERM to gracefully shut down whatever third-party node or executable it spawns. 
   - Never allow child processes to become orphaned in the background.
4. **Local Isolation:** If your underlying application allows you to configure its Host/Interface bind, ALWYAS default it to `--host 127.0.0.1`. **Do not use `0.0.0.0`** unless you explicitly intend to expose your node to the Entire LAN Network.

---

## 🛠️ How to Create a New Bridge

If you are writing a new integration to attach an external agent, LLM infrastructure, or scraper tool to OmniClaw:

1. **Register the Service:** First, declare your service and its expected API `port` inside `core/config/config.json`. Set `"autostart": false`.
2. **Create the Script:** Name it strictly as `launch_<service_name>.py`.
3. **Use the Boilerplate:** Copy the internal template:
   ```bash
   cp bridgetemplate.py launch_my_new_tool.py
   ```
4. **Inject Your Command:** Modify the `subprocess.Popen(...)` call inside your script to launch whatever custom environment (Node, Poetry, Cargo, Go) or server engine you are integrating.

### 🤫 The "Mock Port" Technique (For Daemons without HTTP/TCP bindings)
If your application is a silent background daemon (e.g., a Telegram Bot or file watcher) that *does not naturally open a network port*, OBD Harbor will constantly think it is `OFFLINE` (because OBD uses socket pinging).
To bypass this safely, your `launch_*.py` bridge must use Python's `socket` library to open a **Dummy Listener** on the designated port. Look at `launch_system_pulse.py` or the `bridgetemplate.py` for a working example.

---
*OmniClaw V5.0 Autonomous Core Documentation*

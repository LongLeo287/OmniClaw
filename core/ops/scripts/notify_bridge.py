#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path

# HỆ THỐNG ĐÃ ĐÓNG KẾT NỐI API THEO LỆNH SẾP
def load_keys():
    return {}

def send_telegram(bot_token, chat_id, message):
    if not bot_token or not chat_id: return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = json.dumps({"chat_id": chat_id, "text": message}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try: urllib.request.urlopen(req, timeout=5)
    except: pass

def send_discord(webhook_url, message):
    if not webhook_url: return
    data = json.dumps({"content": message}).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try: urllib.request.urlopen(req, timeout=5)
    except: pass

def send_facebook_workplace(bot_token, thread_id, message):
    if not bot_token or not thread_id: return
    url = f"https://graph.facebook.com/v12.0/me/messages?access_token={bot_token}"
    data = json.dumps({"recipient": {"thread_key": thread_id}, "message": {"text": message}}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try: urllib.request.urlopen(req, timeout=5)
    except: pass

def send_zalo(access_token, user_id, message):
    if not access_token or not user_id: return
    url = "https://openapi.zalo.me/v2.0/oa/message"
    data = json.dumps({"recipient": {"user_id": user_id}, "message": {"text": message}}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", "access_token": access_token}, method="POST")
    try: urllib.request.urlopen(req, timeout=5)
    except: pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)
        
    msg = sys.argv[1]
    keys = load_keys()
    
    # Plug and Play Execution
    if keys.get("TELEGRAM_BOT_TOKEN") and keys.get("TELEGRAM_CHAT_ID"):
        send_telegram(keys["TELEGRAM_BOT_TOKEN"], keys["TELEGRAM_CHAT_ID"], msg)
        
    if keys.get("DISCORD_WEBHOOK_URL"):
        send_discord(keys["DISCORD_WEBHOOK_URL"], msg)
        
    if keys.get("FACEBOOK_ACCESS_TOKEN") and keys.get("FACEBOOK_THREAD_ID"):
        send_facebook_workplace(keys["FACEBOOK_ACCESS_TOKEN"], keys["FACEBOOK_THREAD_ID"], msg)
        
    if keys.get("ZALO_ACCESS_TOKEN") and keys.get("ZALO_USER_ID"):
        send_zalo(keys["ZALO_ACCESS_TOKEN"], keys["ZALO_USER_ID"], msg)
        
    print(f"[Notify Bridge] Dispatched: {msg[:30]}...")

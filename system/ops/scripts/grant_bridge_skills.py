import json
import os

REGISTRY = r'd:\LongLeo\AI OS CORP\AI OS\brain\shared-context\SKILL_REGISTRY.json'

with open(REGISTRY, 'r', encoding='utf-8') as f:
    skills = json.load(f)

new_skills = {
    "api_routing": {
        "description": "Điều định tuyến Request và Webhook nhúng vào luồng hệ thống.",
        "filepath": "system/bridge/api_gateway/main.py",
        "granted_to": ["bridge-commander-agent"]
    },
    "passport_verify": {
        "description": "Xác minh chuẩn Thẻ/Token kết nối mảng Remote Bridge Vault.",
        "filepath": "system/bridge/secrets_manager/passport_issuer.py",
        "granted_to": ["bridge-commander-agent", "vault-keeper-agent"]
    }
}

for k, v in new_skills.items():
    if k not in skills:
        skills[k] = v
    else:
        for agent in v["granted_to"]:
            if agent not in skills[k].get("granted_to", []):
                skills[k].setdefault("granted_to", []).append(agent)

with open(REGISTRY, 'w', encoding='utf-8') as f:
    json.dump(skills, f, ensure_ascii=False, indent=4)

print("Đã Update Skill Registry cấp Chứng chỉ Kỹ năng cho Cục Trưởng!")

import yaml

ORG_CHART = r'd:\LongLeo\AI OS CORP\AI OS\brain\corp\org_chart.yaml'

with open(ORG_CHART, 'r', encoding='utf-8') as f:
    org = yaml.safe_load(f)

# Thêm phòng ban Cục Hải Quan
if 'gateway_border_security' not in org['departments']:
    org['departments']['gateway_border_security'] = {
        'head': 'bridge-commander-agent',
        'workers': []
    }

with open(ORG_CHART, 'w', encoding='utf-8') as f:
    yaml.dump(org, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print("Đã Update Sơ đồ tổ chức org_chart.yaml với Cục Hải Quan!")

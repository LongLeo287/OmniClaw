# OER_CHARTER-vn.md — Hien Chuong Cuc Dang Kiem Sinh Thai OmniClaw

**Tham Quyen:** CEO (LongLeo) | **Cap Bac Daemon:** Core Daemon So 4
**Dieu Hanh Boi:** Phong Ban 14 (`registry-manager-agent`)
**Hieu Luc Tu:** 2026-04-02

[**English Version**](OER_CHARTER.md) | [**Quay lai Muc Luc**](../README-vn.md)

---

## OER La Gi?

OER (OmniClaw Ecosystem Registry - Cuc Dang Kiem He Sinh Thai) la **Core Daemon Thu Tu** cua OmniClaw OS.
OIW di Thu Hoach, OHD di Chua Benh, OA di Xet Xu — **OER la Cuc Dang Kiem**.

OER la the luc DUY NHAT duoc uy quyen:
- Phat hanh ID duy nhat cho moi Skill, Plugin, Agent va Workflow.
- Viet va bao tri `SKILL_REGISTRY.json` (So cai He Sinh Thai).
- Di chuyen cac san pham da duoc duyet vao cac thu muc `ecosystem/`.
- Nam giu The Thinh Kinh (Free-Pass) vao `brain/knowledge/` de phoi hop nang luc.

Khong co agent, daemon hay quan chuc nao khac duoc phep thuc hien nhung hanh dong nay. Day la luat, khong phai goi y.

---

## Nhiem Vu Cot Loi

### 1. So Cai (SKILL_REGISTRY.json)
OER so huu va van hanh nguon su that duy nhat: `brain/registry/SKILL_REGISTRY.json`.
Moi Skill, Plugin, Agent, Workflow duoc dang ky vao OmniClaw deu phai co ID do OER phat hanh truoc khi Orchestrator co the su dung.

**Dinh Dang ID:**
| Loai Tai San | Dinh Dang ID | Vi Du |
|---|---|---|
| Skill | `SKILL-xxxx` | `SKILL-0104` |
| Plugin | `PLG-xxxx` | `PLG-0021` |
| Agent | `AGT-xxxx` | `AGT-0015` |
| Workflow | `WRK-xxxx` | `WRK-0008` |
| Department | `DEPT-xx` | `DEPT-22` |

### 2. Cong Kiem Tra Trung Lap (Gate 0)
Truoc khi bat ky pipeline nao bat dau, OER phai xac nhan tai san chua ton tai trong `SKILL_REGISTRY.json`. Neu phat hien trung lap, OER tu choi yeu cau va tra ve ID tai san hien co cho nguoi yeu cau.

### 3. Tiep Nhan Cuoi Cung (PHASE 5)
OER chi hanh dong **sau** khi TAN BO cac dieu kien duoi day deu duoc thoa man:
- Con dau `OHD_CLEAN` da co (chuan supply chain, khong IOC)
- Con dau `OA_APPROVED` da co (diem >=70, tat ca 8 Tru cot da duoc xem xet)
- `SKILL.md` hoac manifest tuong duong da duoc Phong 1 (Engineering) viet
- Nguon trong `storage/vault/quarantine/` dang cho chuyen khoan cuoi cung

Sau do OER se:
1. Tao ID duy nhat cho tai san.
2. Sao chep artifact tu `quarantine/` vao tang `ecosystem/` chinh xac.
3. Cap nhat `SKILL_REGISTRY.json` voi day du metadata.
4. Viet bien lai vao `telemetry/qa_receipts/gate_oer/`.
5. Thong bao cho Orchestrator bang tom tat co cau truc.

---

## Pipeline 5-Gate Tu Dong

```
[KHOI DONG: CEO / Orchestrator / Truong Phong]
        |
 [GATE 0: OER Kiem Tra Trung Lap]  -----> TU CHOI neu da ton tai
        |
 [PHASE 1: OIW — Thu Hoach & Gitingest]
   - Clone repo vao storage/vault/quarantine/
   - Nen thanh .md qua gitingest
        |
 [PHASE 2: OHD — Khu Trung & Quet Supply Chain]
   - Chay: system/security/supply_chain_scan.ps1
   - Chay: npm audit (neu JS), pip-audit (neu Python)
   - Dong dau: OHD_CLEAN | Timestamp
        |        \___THAT BAI__> OA Blacklist + Canh Bao
 [PHASE 3: OA — Kiem Toan & Tuan Thu]
   - Phong 9 (Strix): Diem bao mat >= 70
   - Phong 12 (Legal): Kiem tra bang quyen
   - Xem xet 8 Tru Cot
   - Dong dau: OA_APPROVED | Diem
        |        \___THAT BAI__> Bao Cao OA Faculty + Khoa
 [PHASE 4: Phong 1 (Engineering) — Ren]
   - Viet: SKILL.md / plugin manifest
   - Viet: unit tests
   - Dat trong: quarantine/ (da hoan thien, san sang)
        |
 [PHASE 5: OER — Dang Ky]
   - Phat ID duy nhat
   - Di chuyen vao ecosystem/[tang]/
   - Cap nhat: SKILL_REGISTRY.json
   - Viet: bien lai telemetry
   - Thong bao: Orchestrator "DA DANG KY"
```

---

## Kiem Soat Truy Cap

| The Luc | Doc `ecosystem/` | Ghi `ecosystem/` | Cap Nhat Registry |
|---|---|---|---|
| **OER (Phong 14)** | CO | **CO (DUY NHAT)** | **CO (DUY NHAT)** |
| OA | CO (kiem toan) | KHONG | KHONG |
| OHD | KHONG | KHONG | KHONG |
| OIW | KHONG | KHONG | KHONG |
| Orchestrator | CO | KHONG | KHONG |
| CTO / C-Suite | CO | KHONG | KHONG |
| Tat ca agent khac | KHONG | KHONG | KHONG |

---

## Quan He Voi Cac Core Daemon Khac

| Daemon | Vai Tro | Giao OER | Nhan Tu OER |
|---|---|---|---|
| OIW | Thu Hoach | Nguon tho da duoc cach ly | Xac nhan slot mo |
| OHD | Bac si | Con dau `OHD_CLEAN` | Yeu cau quet dinh ky |
| OA | Quan Toa | Con dau `OA_APPROVED` | Cap nhat Blacklist de thuc thi |

---

## Phan Quyen 4 Core Daemon (Ma Tran Toan Canh)

| Chuc nang | OIW | OHD | OA | OER |
|---|---|---|---|---|
| Hut Repo, Gitingest | YES | NO | NO | NO |
| Dat Repo vao Quarantine | YES | NO | NO | NO |
| Dang ky Agent/Dept moi | **NO** | NO | NO | **YES** |
| Quet Virus, IOC Supply Chain | NO | YES | NO | NO |
| Don rac npm, cache | NO | YES | NO | NO |
| Bao cao suc khoe he thong | NO | YES | NO | NO |
| Xet xu vi pham Kien Truc | NO | NO | YES | NO |
| Audit Ecosystem plugins | NO | NO | YES | NO |
| Nhap kho Skill vao `ecosystem/` | NO | NO | NO | YES |
| Cap nhat SKILL_REGISTRY.json | NO | NO | NO | YES |
| Cap ID, Bien so Tool/Plugin | NO | NO | NO | YES |
| Free-Pass vao `brain/knowledge` | NO | NO | NO | YES |
| Viet luat, Tru cot OA | NO | NO | YES | NO |

---

*OER Charter v1.0 — OmniClaw Corp — 2026-04-02*

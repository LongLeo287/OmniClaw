---
id: repo-fetched-arknights-endfield-060059
type: knowledge
owner: OA
registered_at: 2026-04-05T03:29:11.138679
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_Arknights_Endfield_060059

## Assimilation Report
Auto-cloned repository: FETCHED_Arknights_Endfield_060059

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: DIAGNOSTIC_REPORT.md
```md
# 数据库深度诊断报告

## 诊断时间
2026-01-21

## 诊断结果汇总

### ✅ 1. 触发器存活确认
**状态**: 需要验证

根据迁移文件，应该存在以下触发器：
- `update_stats_after_pull` - 更新用户统计表
- `update_weekly_after_pull` - 更新周榜表

### ✅ 2. 数据孤岛确认
**状态**: ⚠️ 发现严重问题

| 指标 | 结果 | 说明 |
|------|------|------|
| 本周抽卡数据 | ✅ 存在 | `recentPullsCount` 显示有数据 |
| 本周周榜数据 | ❌ 为空 | `currentWeekLeaderboard` 为空数组 |
| 用户统计表 | ❌ 为空 | `userStats` 为空数组，`totalUsers` = 0 |
| 历史周榜数据 | ⚠️ 存在 | `leaderboardCount` = 1（旧数据） |

**结论**: 触发器 100% 没有工作！本周有抽卡数据，但用户统计表和周榜表都是空的。

### ✅ 3. 权限锁确认 (RLS Check)
**状态**: 需要验证

根据迁移文件，以下表启用了 RLS：
- `gacha_pulls` - 用户只能查看和插入自己的数据
- `gacha_user_stats` - 用户只能查看和更新自己的数据
- `gacha_weekly_leaderboard` - 公开可读

**潜在问题**: 如果触发器函数没有使用 `SECURITY DEFINER`，RLS 可能会阻止触发器写入数据。

---

## 根本原因分析

### 问题 1: 触发器函数可能缺少 `SECURITY DEFINER`
触发器函数在执行时会受到 RLS 策略的限制。如果函数没有使用 `SECURITY DEFINER`，它会以调用者的权限执行，可能会被 RLS 策略阻止写入。

### 问题 2: 触发器可能未正确创建
虽然迁移文件中定义了触发器，但可能在执行过程中出现了错误，导致触发器没有被正确创建。

### 问题 3: 时区问题
如果触发器函数中的时区处理不正确，可能导致周榜的 `week_start` 计算错误，从而无法匹配本周的数据。

---

## 修复方案

### 方案 1: 重新创建触发器函数（推荐）

执行 `20260121_emergency_trigger_fix.sql` 脚本，该脚本会：

1. ✅ 删除旧的触发器和函数
2. ✅ 重新创建函数，确保使用 `SECURITY DEFINER`
3. ✅ 重新创建触发器
4. ✅ 验证触发器已正确创建
5. ✅ 手动触发一次统计更新

### 方案 2: 手动修复现有数据

如果触发器修复后，需要手动修复现有数据：

```sql
-- 1. 重新计算所有用户的统计数据
INSERT INTO gacha_user_stats (user_id, total_pulls, total_6star, total_5star, total_4star, current_pity6, current_pity5, best_6star_pity, avg_6star_pity, last_pull_at)
SELECT 
  user_id,
  SUM(pull_count) as total_pulls,
  SUM(COALESCE((results->>'six_star_count')::INTEGER, 0)) as total_6star,
  SUM(COALESCE((results->>'five_star_count')::INTEGER, 0)) as total_5star,
  SUM(COALESCE((results->>'four_star_count')::INTEGER, 0)) as total_4star,
  (SELECT pity6_after FROM gacha_pulls WHERE user_id = gp.user_id ORDER BY created_at DESC LIMIT 1) as current_pity6,
  (SELECT pity5_after FROM gacha_pulls WHERE user_id = gp.user_id ORDER BY created_at DESC LIMIT 1) as current_pity5,
  MIN(COALESCE((results->>'best_6star_pity')::INTEGER, 999)) as best_6star_pity,
  AVG(COALESCE((results->>'avg_6star_pity')::NUMERIC, 0)) as avg_6star_pity,
  MAX(created_at) as last_pull_at
FROM gacha_pulls gp
GROUP BY user_id
ON CONFLICT (user_id) DO UPDATE SET
  total_pulls = EXCLUDED.total_pulls,
  total_6star = EXCLUDED.total_6star,
  total_5star = EXCLUDED.total_5star,
  total_4star = EXCLUDED.total_4star,
  current_pity6 = EXCLUDED.current_pity6,
  current_pity5 = EXCLUDED.current_pity5,
  best_6star_pity = EXCLUDED.best_6star_pity,
  avg_6star_pity = EXCLUDED.avg_6star_pity,
  last_pull_at = EXCLUDED.last_pull_at,
  updated_at = NOW();

-- 2. 重新计算周榜数据
INSERT INTO gacha_weekly_leaderboard (user_id, week_start, score, best_pull)
SELECT 
  gp.user_id,
  date_trunc('week', gp.created_at AT TIME ZONE 'UTC')::DATE as week_start,
  COALESCE((gp.results->>'six_star_count')::INTEGER, 0) * 10000 +
  COALESCE((gp.results->>'five_star_count')::INTEGER, 0) * 100 +
  COALESCE((gp.results->>'four_star_count')::INTEGER, 0) * 10 as score,
  gp.results as best_pull
FROM gacha_pulls gp
WHERE gp.created_at >= date_trunc('week', NOW() AT TIME ZONE 'UTC')
ON CONFLICT (user_id, week_start) DO UPDATE SET
  score = EXCLUDED.score,
  best_pull = CASE 
    WHEN EXCLUDED.score > gacha_weekly_leaderboard.score THEN EXCLUDED.best_pull
    ELSE gacha_weekly_leaderboard.best_pull
  END;
```

---

## 执行步骤

### 步骤 1: 在 Supabase Dashboard 中执行修复脚本

1. 打开 Supabase Dashboard
2. 进入 SQL Editor
3. 执行 `20260121_emergency_trigger_fix.sql` 脚本

### 步骤 2: 验证修复结果

执行诊断查询：

```sql
-- 检查触发器
SELECT trigger_name FROM information_schema.triggers WHERE event_object_table = 'gacha_pulls';

-- 检查本周数据
SELECT COUNT(*) FROM gacha_pulls WHERE created_at >= date_trunc('week', NOW() AT TIME ZONE 'UTC');
SELECT COUNT(*) FROM gacha_weekly_leaderboard WHERE week_start = date_trunc('week', NOW() AT TIME ZONE 'UTC')::DATE;
SELECT COUNT(*) FROM gacha_user_stats;
```

### 步骤 3: 如果需要，手动修复历史数据

执行方案 2 中的 SQL 脚本。

---

## 预防措施

1. **定期检查触发器状态**
   - 创建监控脚本，定期检查触发器是否存在并处于启用状态

2. **使用 SECURITY DEFINER**
   - 所有需要绕过 RLS 的触发器函数都必须使用 `SECURITY DEFINER`

3. **测试触发器**
   - 在部署前测试触发器是否正确工作

4. **日志记录**
   - 添加日志记录，记录触发器的执行情况

---

## 联系方式

如果问题仍然存在，请提供：
1. 触发器查询结果
2. 本周数据查询结果
3. 任何错误信息

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for arknights_endfield
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\GLOSSARY.md
```md
# 术语库 (Glossary)

## 简介

本文档是"明日方舟：终末地"项目的多语言翻译的唯一标准源。所有游戏内术语、角色名称、世界观设定和系统术语的翻译都应遵循此文档中的标准。

## 核心术语对照表

### 品牌术语 (Brand)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| arknights_endfield | Arknights: Endfield | 明日方舟：终末地 | 明日方舟：終末地 | アークナイツ：エンドフィールド | 명일방주: 엔드필드 | Arknights: Endfield | Arknights: Endfield | Arknights: Endfield |
| endfield_industries | Endfield Industries | 终末地工业 | 終末地工業 | エンドフィールド工業 | 엔드필드 공업 | Endfield Industries | Endfield Industries | Endfield Industries |
| gryphline | GRYPHLINE | 鹰角网络 | GRYPHLINE | GRYPHLINE | GRYPHLINE | GRYPHLINE | GRYPHLINE | GRYPHLINE |

### 角色名称 (Roles)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| endministrator | Endministrator | 管理员 | 管理員 | 管理人 | 관리자 | Эндministrator | ผู้ดูแล | Người quản lý |
| perlica | Perlica | 佩丽卡 | 佩麗卡 | ペル莉カ | ペルリカ | Perlica | Perlica | Perlica |
| chen_qianyu | Chen Qianyu | 陈千语 | 陳千語 | チェン・センユー | 진천우 | Чэнь Цяньюй | Chen Qianyu | Chen Qianyu |
| wulfgard | Wulfgard | 沃尔夫加德 | 沃爾夫加德 | ウルフガード | 울프가드 | Вульфгард | Wulfgard | Wulfgard |
| ember | Ember | 余烬 | 餘燼 | エンバー | 엠버 | Эмбер | Ember | Ember |
| ardelia | Ardelia | 艾尔黛拉 | 艾爾黛拉 | アルデリア | 아델리아 | Арделия | Ardelia | Ardelia |

### 角色名称 (Expanded)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| chen_qianyu | Chen Qianyu | 陈千语 | 陳千語 | チェン・センユー | 진천우 | Чэнь Цяньюй | Chen Qianyu | Chen Qianyu |
| wulfgard | Wulfgard | 沃尔夫加德 | 沃爾夫加德 | ウルフガード | 울프가드 | Вульфгард | Wulfgard | Wulfgard |
| ember | Ember | 余烬 | 餘燼 | エンバー | 엠버 | Эмбер | Ember | Ember |
| ardelia | Ardelia | 艾尔黛拉 | 艾爾黛拉 | アルデリア | 아델리아 | Арделия | Ardelia | Ardelia |

### 职业体系 (Class System)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| guard | Guard | 近卫 | 近衛 | 前衛 | 가드 | Страж | การ์ด | Vệ Binh |
| vanguard | Vanguard | 先锋 | 先鋒 | 先鋒 | 뱅가드 | Авангард | แวนการ์ด | Tiên Phong |
| defender | Defender | 重装 | 重裝 | 重装 | 디펜더 | Защитник | ดีเฟนเดอร์ | Hộ Vệ |
| caster | Caster | 术师 | 術師 | 術師 | 캐스터 | Заклинатель | แคสเตอร์ | Thuật Sư |
| supporter | Supporter | 辅助 | 輔助 | 補助 | 서포터 | Помощник | ซัพพอร์ตเตอร์ | Hỗ Trợ |
| striker | Striker | 突击 | 突擊 | ストライカー | 스트라이커 | Штурмовик | สไตรเกอร์ | Đột Kích |

**注意**：Striker (突击) 是终末地中的新职业，替代了原明日方舟中的特种/狙击/医疗角色。

### 世界观术语 (Lore)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| talos_ii | Talos-II | 塔卫二 | 塔衛二 | タロII | 탈로스-II | Talos-II | Talos-II | Talos-II |
| originium | Originium | 源石 | 源石 | 源石 | 오리지늄 | Ориджиниум | Originium | Originium |
| aggelos | Aggelos | 天使 | 天使 | アンゲロス | 아겔로스 | Aggelos | Aggelos | Aggelos |
| blight | Blight | 侵蚀 | 侵蝕 | 侵蝕 | 침식 | Скверна | Blight | Blight |
| aic | Automated Industry Complex | 集成工业系统 | 集成工業系統 | 自動化工業複合体 | 자동화 공업 복합체 | AIC | AIC | AIC |

### 系统术语 (System)

| 英文键名 | 英文 | 简体中文 | 繁体中文 | 日文 | 韩文 | 俄文 | 泰文 | 越南文 |
|---------|------|---------|---------|------|------|------|------|--------|
| operator | Operator | 干员 | 幹員 | オペレーター | 오퍼레이터 | Оперативник | Operator | Operator |
| sanity | Sanity | 理智 | 理智 | 理性 | 이성 | Рассудок | Sanity | Sanity |

## 使用指南

1. **UI翻译**：在进行UI文本翻译时，必须先查阅此术语库，确保使用标准翻译。
2. **新增数据**：在添加新的游戏内容或功能时，应参考此术语库保持术语一致性。
3. **角色名称**：所有角色名称必须使用术语库中的标准翻译。
4. **更新流程**：如需添加新术语或修改现有术语，请先更新此文档，然后同步到`messages/glossary.json`文件。

## 注意事项

- **角色部分**：角色列表已更新至v1.1版本，包含新增角色。
- **职业体系**：新增职业体系，包含终末地中的六大职业。
- **版本控制**：术语库版本为1.1，更新日期为2026-01-19。
- **权威性**：此文档是项目翻译的唯一标准源，所有翻译工作应以此为准。

## 技术实现

术语库的机器可读版本位于`messages/glossary.json`，可在代码中通过以下方式引用：

```javascript
import glossary from '@/messages/glossary.json';

// 获取特定术语的翻译
const term = glossary.brand.arknights_endfield[locale];
```
```


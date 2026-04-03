---
id: github.com-zhanghandong-makepad-skills-793d2c07-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:47.734206
---

# KNOWLEDGE EXTRACT: github.com_ZhangHanDong_makepad-skills_793d2c07
> **Extracted on:** 2026-04-01 12:31:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521866/github.com_ZhangHanDong_makepad-skills_793d2c07

---

## File: `.gitignore`
```
.DS_Store
```

## File: `CLAUDE.md`
```markdown
# Makepad Skills - Claude Instructions

## CRITICAL: Hook-Based Skill Loading

**IMPORTANT:** When you see a message starting with `[makepad-skills]` in the conversation, you MUST:

1. **Read the routing instruction** - e.g., `[makepad-skills] Routing to: makepad-widgets makepad-layout`
2. **Immediately call the Skill tool** for EACH skill listed before doing anything else
3. **Do not skip this step** - the skills contain essential Makepad knowledge

Example:
```
[makepad-skills] Routing to: makepad-widgets makepad-layout
```
→ Call `Skill(makepad-widgets)` then `Skill(makepad-layout)` FIRST, then answer the question.

---

## Skill Routing

For Makepad/Robius/MolyKit questions, use **context detection** and **skill dependencies** to load multiple related skills.

### Context Detection (Load Skill Bundles)

When user intent matches these contexts, load the entire skill bundle:

| Context | Trigger Keywords | Load These Skills |
|---------|------------------|-------------------|
| **Full App Development** | "build app", "create app", "从零", "完整应用", "app architecture" | makepad-basics, makepad-dsl, makepad-layout, makepad-widgets, makepad-event-action, robius-app-architecture |
| **UI Design** | "ui design", "界面设计", "design ui" | makepad-dsl, makepad-layout, makepad-widgets, makepad-animation, makepad-shaders |
| **Widget/Component Creation** | "create widget", "创建组件", "自定义组件", "custom component" | makepad-widgets, makepad-dsl, makepad-layout, makepad-animation, makepad-shaders, makepad-font, makepad-event-action |
| **Production Patterns** | "best practice", "robrix pattern", "实际项目", "production" | robius-app-architecture, robius-widget-patterns, robius-state-management, robius-event-action |

### Skill Dependencies (Auto-Load Related Skills)

When loading a skill, automatically include its dependencies:

| Primary Skill | Also Load |
|---------------|-----------|
| makepad-widgets | makepad-layout, makepad-dsl |
| makepad-animation | makepad-shaders |
| makepad-shaders | makepad-widgets |
| makepad-font | makepad-widgets |
| robius-app-architecture | makepad-basics, makepad-event-action |
| robius-widget-patterns | makepad-widgets, makepad-layout |
| robius-event-action | makepad-event-action |

### Single Skill Keywords (Fallback)

For specific questions, match keywords to individual skills:

| Keywords | Skill |
|----------|-------|
| getting started, `live_design!`, `app_main!` | makepad-basics |
| DSL syntax, inheritance, `<Widget>`, `Foo = { }` | makepad-dsl |
| layout, Flow, Walk, padding, center, align | makepad-layout |
| View, Button, Label, widget | makepad-widgets |
| event, action, Hit, FingerDown, handle_event | makepad-event-action |
| animator, state, transition, hover | makepad-animation |
| shader, draw_bg, Sdf2d, gradient, glow | makepad-shaders |
| platform, macOS, Android, iOS, WASM | makepad-platform |
| font, text, glyph, typography | makepad-font |
| splash, script, cx.eval | makepad-splash |
| Tokio, async, submit_async_request | robius-app-architecture |
| apply_over, modal, collapsible, pageflip | robius-widget-patterns |
| custom action, MatchEvent, post_action | robius-event-action |
| AppState, persistence, Scope::with_data | robius-state-management |
| Matrix SDK, sliding sync, MatrixRequest | robius-matrix-integration |
| BotClient, OpenAI, SSE streaming | molykit |
| deploy, package, APK, IPA | makepad-deployment |
| troubleshoot, error, debug | makepad-reference |

### Extended Skills

**Note:** Production patterns are integrated into robius-* skills:
- Widget patterns (modal, collapsible, drag-drop) → `robius-widget-patterns/_base/`
- State patterns (theme switching, state machine) → `robius-state-management/_base/`
- Async patterns (streaming, tokio) → `robius-app-architecture/_base/`

## Usage Examples

### Full App Development (Bundle)
```
User: "我想从零开发一个 Makepad 应用"
-> Detect: Full app context
-> Load: makepad-basics, makepad-dsl, makepad-layout, makepad-widgets,
         makepad-event-action, robius-app-architecture
-> Answer with complete app structure, widgets, events, and async patterns
```

### Widget Creation (Bundle)
```
User: "帮我创建一个自定义按钮组件"
-> Detect: Widget creation context
-> Load: makepad-widgets, makepad-dsl, makepad-layout, makepad-animation,
         makepad-shaders, makepad-font, makepad-event-action
-> Answer with widget structure, styling, animations, and event handling
```

### Simple Question (Single + Dependencies)
```
User: "如何设置字体大小"
-> Match: makepad-font
-> Auto-load dependency: makepad-widgets
-> Load: makepad-font, makepad-widgets
-> Answer with text_style, font_size, and widget context
```

### Production App (Bundle)
```
User: "参考 Robrix 的最佳实践"
-> Detect: Production context
-> Load: robius-app-architecture, robius-widget-patterns,
         robius-state-management, robius-event-action
         + dependencies: makepad-basics, makepad-widgets, makepad-layout, makepad-event-action
-> Answer with production-ready patterns from Robrix/Moly codebases
```

## Key Patterns

### Makepad Widget Definition
```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,
    #[live] property: f64,
    #[rust] internal_state: State,
    #[animator] animator: Animator,
}
```

### Robius Async Pattern
```rust
// UI -> Async
submit_async_request(MatrixRequest::SendMessage { ... });

// Async -> UI
Cx::post_action(MessageSentAction { ... });
SignalToUI::set_ui_signal();
```

### MolyKit Cross-Platform Async
```rust
// Platform-agnostic spawning
spawn(async move {
    let result = fetch_data().await;
    Cx::post_action(DataReady(result));
    SignalToUI::set_ui_signal();
});
```

## Default Project Settings

When creating Makepad projects:

```toml
[package]
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }

[features]
default = []
nightly = ["makepad-widgets/nightly"]
```

## Source Codebases

For deeper reference, check these codebases:

- **Makepad**: `/path/to/makepad` - Framework source
- **Robrix**: `/path/to/robrix` - Matrix client example
- **Moly**: `/path/to/moly` - AI chat example
- **MolyKit**: `/path/to/moly/moly-kit` - AI chat toolkit
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Project Robius

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

## File: `README.ja.md`
```markdown
# Makepad 向け Claude Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Rust の [Makepad](https://github.com/makepad/makepad) フレームワークを使用してクロスプラットフォーム UI アプリケーションを構築するための Agent Skills です。

## Makepad について

[Makepad](https://github.com/makepad/makepad) は、Rust で書かれた次世代 UI フレームワークで、高性能なクロスプラットフォームアプリケーションの構築を可能にします。主な特徴：

- **クロスプラットフォーム**：単一のコードベースでデスクトップ（macOS、Windows、Linux）、モバイル（Android、iOS）、Web（WebAssembly）に対応
- **GPU アクセラレーション**：SDF（Signed Distance Field）描画によるカスタムシェーダーベースのレンダリング
- **ライブデザイン**：ホットリロード可能な `live_design!` DSL による迅速な UI 開発
- **高パフォーマンス**：ネイティブコンパイル、仮想 DOM なし、最小限のランタイムオーバーヘッド

## Robius について

[Project Robius](https://github.com/project-robius) は、Rust でフル機能のアプリケーション開発フレームワークを構築するオープンソースイニシアチブです。Makepad で構築された本番アプリケーション：

- **[Robrix](https://github.com/project-robius/robrix)** - リアルタイムメッセージング、E2E 暗号化、複雑な UI パターンを実装した Matrix チャットクライアント
- **[Moly](https://github.com/moxin-org/moly)** - データ集約型インターフェースと非同期操作を実装した AI モデルマネージャー

これらの Skills は Robrix と Moly で使用されているパターンから抽出されています。

## インストール

### プラグインマーケットプレイス（推奨）

Claude Code のプラグインマーケットプレイス経由でインストール：

```bash
# ステップ 1：マーケットプレイスを追加
/plugin marketplace add ZhangHanDong/makepad-skills

# ステップ 2：プラグインをインストール（1つまたは複数選択）
/plugin install makepad-full@makepad-skills-marketplace        # 全スキル
/plugin install makepad-core@makepad-skills-marketplace        # コア + 入門
/plugin install makepad-graphics@makepad-skills-marketplace    # グラフィックス & シェーダー
/plugin install makepad-patterns@makepad-skills-marketplace    # プロダクションパターン
/plugin install makepad-deployment@makepad-skills-marketplace  # プラットフォームパッケージング
/plugin install makepad-reference@makepad-skills-marketplace   # API ドキュメント & トラブルシューティング
```

**利用可能なプラグイン：**

| プラグイン | 説明 |
|-----------|------|
| `makepad-full` | 全スキルを含む完全パッケージ |
| `makepad-core` | 入門、レイアウト、ウィジェット、イベント |
| `makepad-graphics` | SDF 描画、シェーダー、アニメーション |
| `makepad-patterns` | 非同期、ステートマシン、オーバーレイ、リスト |
| `makepad-deployment` | Android、iOS、WASM パッケージング |
| `makepad-reference` | API ドキュメント、トラブルシューティング、コード品質 |
| `makepad-evolution` | 自己進化テンプレートとフック |

### スクリプトインストール

インストールスクリプトでワンコマンドセットアップ：

```bash
# 現在のプロジェクトにインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# hooks を有効にしてインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# 特定のプロジェクトにインストール
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# Codex 向けにインストール（.codex/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# Gemini CLI 向けにインストール（.gemini/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI 補足: Skills は実験的機能です。必要に応じて `/settings` で `experimental.skills` を有効化してください。

**スクリプト機能：**
- Rust/Makepad プロジェクトを自動検出（Cargo.toml をチェック）
- インストール前に既存の skills をバックアップ
- `--with-hooks` で自己進化フックをコピーして設定（Claude Code のみ）
- `--agent codex|claude-code|gemini` で Codex、Claude Code、または Gemini CLI を選択（デフォルト: claude-code）
- `--target` で任意のプロジェクトディレクトリにインストール可能
- カラー出力で進捗を明確に表示

**利用可能なオプション：**

| オプション | 説明 |
|-----------|------|
| `--target DIR` | 特定のディレクトリにインストール（デフォルト：現在のディレクトリ） |
| `--with-hooks` | 自己進化フックを有効化（Claude Code のみ） |
| `--agent AGENT` | エージェント指定: `codex`、`claude-code`、または `gemini`（デフォルト: `claude-code`） |
| `--branch NAME` | 特定のブランチを使用（デフォルト：main） |
| `--help` | ヘルプメッセージを表示 |

### 手動インストール

```bash
# このリポジトリをクローン
git clone https://github.com/ZhangHanDong/makepad-skills.git

# プロジェクトにコピー（https://code.claude.com/docs/en/skills）
cp -r makepad-skills/skills your-project/.claude/skills

# Codex プロジェクトにコピー（https://developers.openai.com/codex/skills）
cp -r makepad-skills/skills your-project/.codex/skills

# Gemini CLI プロジェクトにコピー（https://geminicli.com/docs/cli/skills/）
cp -r makepad-skills/skills your-project/.gemini/skills
```

インストール後のプロジェクト構造（Codex/Gemini は `.claude` を `.codex`/`.gemini` に置き換えてください）：

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── 00-getting-started/
│       ├── 01-core/
│       ├── 02-components/
│       ├── 03-graphics/
│       │   ├── _base/          # 公式 skills（アトミック）
│       │   └── community/      # コミュニティ貢献
│       ├── 04-patterns/
│       │   ├── _base/          # 公式 patterns（アトミック）
│       │   └── community/      # コミュニティ貢献
│       ├── 05-deployment/
│       ├── 06-reference/
│       ├── 99-evolution/
│       │   └── templates/      # 貢献テンプレート
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

詳細は [Claude Code Skills 公式ドキュメント](https://docs.anthropic.com/en/docs/claude-code/skills) を参照してください。

## GitHub Actions パッケージング

Makepad Packaging Action を使って CI で Makepad アプリをパッケージングできます。内部で `cargo-packager`（デスクトップ）と `cargo-makepad`（モバイル）を実行し、GitHub Releases へのアップロードに対応します。

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

注意：
- デスクトップは対応 OS の runner が必要です。
- iOS は macOS runner が必要です。

## アーキテクチャ：コラボレーション向けアトミック Skills

### なぜアトミック構造？

v2.1 では、協調開発向けに設計された**アトミック skill 構造**を導入しました：

```
04-patterns/
├── SKILL.md              # インデックスファイル
├── _base/                # 公式 patterns（番号付き、アトミック）
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 14-callout-tooltip.md
└── community/            # あなたの貢献
    ├── README.md
    └── {GitHub ユーザー名}-{パターン名}.md
```

**メリット：**
- **マージ競合なし**：`community/` のファイルは公式 `_base/` の更新と競合しません
- **並列開発**：複数のユーザーが同時に貢献可能
- **明確な帰属**：ファイル名の GitHub ユーザー名がクレジットを提供
- **段階的開示**：SKILL.md インデックス → 個別パターンの詳細

### 自己進化：開発から Skills を蓄積

自己進化機能により、開発中に発見したパターンをキャプチャして skills に追加できます。

#### 仕組み

1. **開発中**：Makepad でアプリを構築する際に、有用なパターン、シェーダー、エラー解決策を発見

2. **パターンをキャプチャ**：Claude に保存を依頼：
   ```
   ユーザー: このツールチップ配置ロジックは便利です。コミュニティパターンとして保存して
   Claude: [テンプレートを使用して community/{ユーザー名}-tooltip-positioning.md を作成]
   ```

3. **自動検出**（hooks 有効時）：エラーを遭遇して修正すると、システムが自動的に解決策を troubleshooting にキャプチャ

#### 自己進化フックを有効にする（オプション）

```bash
# 99-evolution からプロジェクトに hooks をコピー
cp -r your-project/.claude/skills/99-evolution/hooks your-project/.claude/skills/hooks

# フックに実行権限を付与
chmod +x your-project/.claude/skills/hooks/*.sh

# フック設定を .claude/settings.json に追加
# skills/99-evolution/hooks/settings.example.json を参照
```

#### 手動パターン作成

Claude に直接依頼：
```
ユーザー: さっき実装したドラッグ&ドロップ並べ替えをコミュニティパターンとして保存して
Claude: テンプレートを使用して作成します...
```

Claude は：
1. `99-evolution/templates/pattern-template.md` テンプレートを使用
2. `04-patterns/community/{あなたのユーザー名}-drag-drop-reorder.md` にファイルを作成
3. frontmatter とコンテンツを入力

### コミュニティ貢献ガイド

#### パターンの貢献

1. **パターンファイルを作成**：
   ```
   04-patterns/community/{GitHub ユーザー名}-{パターン名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/pattern-template.md` からコピー

3. **必須の frontmatter**：
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **メインリポジトリに PR を送信**

#### シェーダー/エフェクトの貢献

1. **エフェクトファイルを作成**：
   ```
   03-graphics/community/{GitHub ユーザー名}-{エフェクト名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/shader-template.md` からコピー

#### エラー解決策の貢献

1. **troubleshooting エントリを作成**：
   ```
   06-reference/troubleshooting/{エラー名}.md
   ```

2. **テンプレートを使用**：`99-evolution/templates/troubleshooting-template.md` からコピー

#### アップストリームとの同期

ローカル skills を更新しながら、貢献を保持：

```bash
# リポジトリをフォークしている場合
git fetch upstream
git merge upstream/main --no-edit
# community/ ファイルは _base/ の変更と競合しません
```

#### 昇格パス

高品質なコミュニティ貢献は `_base/` に昇格される可能性があります：
- パターンが広く有用で十分にテストされている
- ドキュメントが完全
- コミュニティのフィードバックがポジティブ
- `author` フィールドでクレジットを保持

## Skills 一覧 (v2.1 アトミック構造)

### [00-getting-started](../bmad_repo/SKILL.md) - プロジェクトセットアップ

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [init.md](../../../vault/archives/archive_legacy/claudekit/src/commands/agents-md/init.md) | プロジェクトスキャフォールディング | 「新しい Makepad アプリを作成」 |
| [project-structure.md](./skills/00-getting-started/project-structure.md) | ディレクトリ構成 | 「プロジェクトをどう整理すべき？」 |

### [01-core](../bmad_repo/SKILL.md) - コア開発

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [layout.md](../../../vault/archives/archive_legacy/vscode/src/vs/sessions/LAYOUT.md) | フロー、サイズ、間隔、配置 | 「UI 要素を配置」 |
| [widgets.md](./skills/01-core/widgets.md) | 一般的なウィジェット、カスタムウィジェット | 「ボタンの作り方は？」 |
| [events.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/simpy/references/events.md) | イベント処理、ヒットテスト | 「クリックイベントの処理」 |
| [styling.md](./skills/01-core/styling.md) | フォント、テキストスタイル、SVG アイコン | 「フォントサイズを変更」「アイコンを追加」 |

### [02-components](../bmad_repo/SKILL.md) - ウィジェットギャラリー

全ビルトインウィジェット参照（ui_zoo から）：Button、TextInput、Slider、Checkbox、Label、Image、ScrollView、PortalList、PageFlip など。

### [03-graphics](../bmad_repo/SKILL.md) - グラフィックスとアニメーション（アトミック）

`_base/` に 14 個の独立 skills：

| カテゴリ | Skills |
|----------|--------|
| シェーダー基礎 | `01-shader-structure`, `02-shader-math` |
| SDF 描画 | `03-sdf-shapes`, `04-sdf-drawing`, `05-progress-track` |
| アニメーション | `06-animator-basics`, `07-easing-functions`, `08-keyframe-animation`, `09-loading-spinner` |
| ビジュアルエフェクト | `10-hover-effect`, `11-gradient-effects`, `12-shadow-glow`, `13-disabled-state`, `14-toggle-checkbox` |

`community/` にはカスタムエフェクトを追加。

### [04-patterns](../bmad_repo/SKILL.md) - プロダクションパターン（アトミック）

`_base/` に 14 個の独立 patterns：

| カテゴリ | Patterns |
|----------|----------|
| ウィジェットパターン | `01-widget-extension`, `02-modal-overlay`, `03-collapsible`, `04-list-template`, `05-lru-view-cache`, `06-global-registry`, `07-radio-navigation` |
| データパターン | `08-async-loading`, `09-streaming-results`, `10-state-machine`, `11-theme-switching`, `12-local-persistence` |
| 高度なパターン | `13-tokio-integration`, `14-callout-tooltip` |

`community/` にはカスタムパターンを追加。

### [05-deployment](../bmad_repo/SKILL.md) - ビルドとパッケージ

デスクトップ（Linux、Windows、macOS）、モバイル（Android、iOS）、Web（WebAssembly）向けにビルド。

### [06-reference](../bmad_repo/SKILL.md) - リファレンス

| ファイル | 説明 | 使用場面 |
|----------|------|----------|
| [troubleshooting.md](troubleshooting.md) | よくあるエラーと修正 | 「Apply error: no matching field」 |
| [code-quality.md](code-quality.md) | Makepad 対応のリファクタリング | 「このコードを簡略化」 |
| [adaptive-layout.md](./skills/06-reference/adaptive-layout.md) | デスクトップ/モバイルレスポンシブ | 「デスクトップとモバイル両方に対応」 |

### [99-evolution](../bmad_repo/SKILL.md) - 自己改善

| コンポーネント | 説明 |
|---------------|------|
| `templates/` | パターン、シェーダー、troubleshooting テンプレート |
| `hooks/` | 自動検出と検証フック |

## 使用例

### 新規プロジェクト作成
```
ユーザー: カウンターボタン付きの "my-app" という Makepad アプリを作成
Claude: [00-getting-started でプロジェクト作成、01-core でボタン/カウンター実装]
```

### ツールチップを追加
```
ユーザー: ホバー時にユーザー情報を表示するツールチップを追加
Claude: [04-patterns/_base/14-callout-tooltip.md で完全な実装を取得]
```

### カスタムパターンを保存
```
ユーザー: この無限スクロール実装をコミュニティパターンとして保存
Claude: [04-patterns/community/yourhandle-infinite-scroll.md を作成]
```

### コンパイルエラー修正
```
ユーザー: "no matching field: font" エラーが発生
Claude: [06-reference/troubleshooting.md で正しい text_style 構文を特定]
```

## 構築できるもの

これらの Skills を使用すると、Claude は以下をサポートします：

- 適切な構造で新しい Makepad プロジェクトを初期化
- `live_design!` DSL でカスタムウィジェットを作成
- イベントとユーザーインタラクションを処理
- 視覚効果用の GPU シェーダーを作成
- スムーズなアニメーションを実装
- async/tokio でアプリケーション状態を管理
- レスポンシブなデスクトップ/モバイルレイアウトを構築
- すべてのプラットフォーム向けにアプリをパッケージ化
- 開発中に発見したパターンを**キャプチャして共有**

## これらの Skills で構築されたプロジェクト

makepad-skills と Claude Code を使用して作成された実際のプロジェクト：

| プロジェクト | 説明 | 所要時間 |
|-------------|------|----------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills-demo) | 為替レート変換アプリのデモ | 約 20 分 |
| [makepad-component](https://github.com/ZhangHanDong/makepad-component) | 再利用可能な Makepad コンポーネントライブラリ | - |

### makepad-skills-demo スクリーンショット

<p align="center">
  <img src="./assets/skill-app-demo.jpg" width="60%" alt="為替レート変換アプリ" />
</p>

### makepad-component スクリーンショット

<p align="center">
  <img src="./assets/mc1.png" width="45%" alt="コンポーネント 1" />
  <img src="./assets/mc2.png" width="45%" alt="コンポーネント 2" />
</p>
<p align="center">
  <img src="./assets/mc3.png" width="45%" alt="コンポーネント 3" />
  <img src="./assets/mc4.png" width="45%" alt="コンポーネント 4" />
</p>

## リソース

- [Makepad リポジトリ](https://github.com/makepad/makepad)
- [Makepad サンプル](https://github.com/makepad/makepad/tree/main/examples)
- [Project Robius](https://github.com/project-robius)
- [Robrix](https://github.com/project-robius/robrix)
- [Moly](https://github.com/moxin-org/moly)

## ライセンス

MIT
```

## File: `README.md`
```markdown
# Agent Skills for Makepad

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Agent skills for building cross-platform UI applications with the [Makepad](https://github.com/makepad/makepad) framework in Rust.

## About Makepad

[Makepad](https://github.com/makepad/makepad) is a next-generation UI framework written in Rust that enables building high-performance, cross-platform applications. Key features include:

- **Cross-Platform**: Single codebase for Desktop (macOS, Windows, Linux), Mobile (Android, iOS), and Web (WebAssembly)
- **GPU-Accelerated**: Custom shader-based rendering with SDF (Signed Distance Field) drawing
- **Live Design**: Hot-reloadable `live_design!` DSL for rapid UI development
- **High Performance**: Native compilation, no virtual DOM, minimal runtime overhead

## About Robius

[Project Robius](https://github.com/project-robius) is an open-source initiative to build a full-featured application development framework in Rust. Production applications built with Makepad include:

- **[Robrix](https://github.com/project-robius/robrix)** - A Matrix chat client showcasing real-time messaging, E2E encryption, and complex UI patterns
- **[Moly](https://github.com/moxin-org/moly)** - An AI model manager demonstrating data-heavy interfaces and async operations

These skills are extracted from patterns used in Robrix and Moly.

## Installation

### Plugin Marketplace (Recommended)

Install via Claude Code's plugin marketplace:

```bash
# Step 1: Add marketplace
/plugin marketplace add ZhangHanDong/makepad-skills

# Step 2: Install the plugin (includes all 20 skills)
/plugin install makepad-skills@makepad-skills-marketplace
```

**Using Plugin Skills:**

Plugin skills are accessed via namespace format (they won't appear in `/skills` list, but can be loaded):

```bash
# Load specific skills by namespace
/makepad-skills:makepad-widgets
/makepad-skills:makepad-layout
/makepad-skills:robius-widget-patterns

# Or just ask questions - hooks will auto-route to relevant skills
"How do I create a Makepad button?"
"makepad 布局怎么居中？"
```

**Manage installed plugins:**

```bash
/plugin                  # List installed plugins
/plugin uninstall makepad-skills@makepad-skills-marketplace  # Uninstall
```

### Shell Script Install

Use the install script for one-command setup:

```bash
# Install to current project
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# Install with hooks enabled
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# Install to specific project
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# Install for Codex (.codex/skills)
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# Install for Gemini CLI (.gemini/skills)
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI note: Skills are experimental. Enable `experimental.skills` in `/settings` if needed.

**Script features:**
- Auto-detects Rust/Makepad projects (checks for Cargo.toml)
- Backs up existing skills before installation
- `--with-hooks` copies and configures self-evolution hooks (Claude Code only)
- `--agent codex|claude-code|gemini` chooses Codex, Claude Code, or Gemini CLI (default: claude-code)
- `--target` allows installing to any project directory
- Colored output with clear progress indicators

**Available options:**

| Option | Description |
|--------|-------------|
| `--target DIR` | Install to specific directory (default: current) |
| `--with-hooks` | Enable self-evolution hooks (Claude Code only) |
| `--agent AGENT` | Set agent: `codex`, `claude-code`, or `gemini` (default: `claude-code`) |
| `--branch NAME` | Use specific branch (default: main) |
| `--help` | Show help message |

### Manual Install

```bash
# Clone this repo
git clone https://github.com/ZhangHanDong/makepad-skills.git

# Copy to your project (https://code.claude.com/docs/en/skills)
cp -r makepad-skills/skills your-project/.claude/skills

# Copy to your project for Codex (https://developers.openai.com/codex/skills)
cp -r makepad-skills/skills your-project/.codex/skills

# Copy to your project for Gemini CLI (https://geminicli.com/docs/cli/skills/)
cp -r makepad-skills/skills your-project/.gemini/skills
```

Your project structure should look like (use `.codex` or `.gemini` instead of `.claude`):

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       │
│       ├── # === Core Skills (16) ===
│       ├── makepad-basics/
│       ├── makepad-dsl/
│       ├── makepad-layout/
│       ├── makepad-widgets/
│       ├── makepad-event-action/
│       ├── makepad-animation/
│       ├── makepad-shaders/
│       ├── makepad-platform/
│       ├── makepad-font/
│       ├── makepad-splash/
│       ├── robius-app-architecture/
│       ├── robius-widget-patterns/
│       ├── robius-event-action/
│       ├── robius-state-management/
│       ├── robius-matrix-integration/
│       ├── molykit/
│       │
│       ├── # === Extended Skills (3) ===
│       ├── makepad-deployment/
│       ├── makepad-reference/
│       │
│       ├── evolution/          # Self-evolution system
│       │   └── templates/      # Contribution templates
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

See [Claude Code Skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills) for more details.

## GitHub Actions Packaging

Use the Makepad Packaging Action to build and release Makepad apps in CI. It wraps `cargo-packager` (desktop) and `cargo-makepad` (mobile), and can upload artifacts to GitHub Releases.

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

Notes:
- Desktop packages must run on matching OS runners.
- iOS builds require macOS runners.

## Architecture: Atomic Skills for Collaboration

### Why Atomic Structure?

v2.1 introduces an **atomic skill structure** designed for collaborative development:

```
robius-widget-patterns/
├── SKILL.md              # Index file
├── _base/                # Official patterns (numbered, atomic)
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 18-drag-drop-reorder.md
└── community/            # Your contributions
    └── {descriptive-pattern-name}.md
```

**Benefits:**
- **No merge conflicts**: Your `community/` files never conflict with official `_base/` updates
- **Parallel development**: Multiple users can contribute simultaneously
- **Clear attribution**: Your GitHub handle in filename provides credit
- **Progressive disclosure**: SKILL.md index → individual pattern details

### Self-Evolution: Enriching Skills from Your Development

The self-evolution feature allows you to capture patterns discovered during your development and add them to the skills.

#### How It Works

1. **During Development**: You discover a useful pattern, shader, or error solution while building with Makepad

2. **Capture the Pattern**: Ask Claude to save it:
   ```
   User: This tooltip positioning logic is useful. Save it as a community pattern.
   Claude: [Creates community/{handle}-tooltip-positioning.md using template]
   ```

3. **Auto-Detection** (with hooks enabled): When you encounter and fix errors, the system can automatically capture solutions to troubleshooting

#### Enable Self-Evolution Hooks (Optional)

```bash
# Copy hooks from evolution to your project
cp -r your-project/.claude/skills/evolution/hooks your-project/.claude/skills/hooks

# Make hooks executable
chmod +x your-project/.claude/skills/hooks/*.sh

# Add hooks config to your .claude/settings.json
# See skills/evolution/hooks/settings.example.json for the configuration
```

#### Manual Pattern Creation

Ask Claude directly:
```
User: Create a community pattern for the drag-drop reordering I just implemented
Claude: I'll create a pattern using the template...
```

Claude will:
1. Use the template from `evolution/templates/pattern-template.md`
2. Create file at `robius-widget-patterns/community/{descriptive-pattern-name}.md`
3. Fill in the frontmatter and content

### Community Contribution Guide

#### Contributing Patterns

1. **Create your pattern file** in the appropriate robius-* skill's community directory:
   - Widget patterns → `robius-widget-patterns/community/`
   - State patterns → `robius-state-management/community/`
   - Async patterns → `robius-app-architecture/community/`

2. **Use the template**: Copy from `evolution/templates/pattern-template.md`

3. **Required frontmatter**:
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **Submit PR** to the main repository

#### Contributing Shaders/Effects

1. **Create your effect file**:
   ```
   makepad-shaders/community/{github-handle}-{effect-name}.md
   ```

2. **Use the template**: Copy from `evolution/templates/shader-template.md`

#### Contributing Error Solutions

1. **Create troubleshooting entry**:
   ```
   makepad-reference/troubleshooting/{error-name}.md
   ```

2. **Use the template**: Copy from `evolution/templates/troubleshooting-template.md`

#### Syncing with Upstream

Keep your local skills updated while preserving your contributions:

```bash
# If you've forked the repo
git fetch upstream
git merge upstream/main --no-edit
# Your community/ files won't conflict with _base/ changes
```

#### Promotion Path

High-quality community contributions may be promoted to `_base/`:
- Pattern is widely useful and well-tested
- Documentation is complete
- Community feedback is positive
- Credit preserved via `author` field

## Skills Overview (v3.0 Flat Structure)

### Core Skills (16)

#### Makepad Core (10 Skills)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [makepad-basics](./skills/makepad-basics/) | App structure, `live_design!`, `app_main!` | "Create a new Makepad app" |
| [makepad-dsl](./skills/makepad-dsl/) | DSL syntax, inheritance, prototypes | "How to define widgets in DSL" |
| [makepad-layout](./skills/makepad-layout/) | Flow, sizing, spacing, alignment | "Center a widget", "Arrange elements" |
| [makepad-widgets](./skills/makepad-widgets/) | Common widgets, custom widgets | "Create a button", "Build a form" |
| [makepad-event-action](./skills/makepad-event-action/) | Event handling, actions | "Handle click events" |
| [makepad-animation](./skills/makepad-animation/) | Animator, states, transitions | "Add hover animation" |
| [makepad-shaders](./skills/makepad-shaders/) | Shaders, SDF, gradients, visual effects | "Custom visual effects" |
| [makepad-platform](./skills/makepad-platform/) | Platform support | "Build for Android/iOS" |
| [makepad-font](./skills/makepad-font/) | Font, text, typography | "Change font, text styling" |
| [makepad-splash](./skills/makepad-splash/) | Splash scripting language | "Dynamic UI scripting" |

#### Robius Patterns (5 Skills)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [robius-app-architecture](./skills/robius-app-architecture/) | Tokio, async/sync patterns | "Structure an async app" |
| [robius-widget-patterns](./skills/robius-widget-patterns/) | Reusable widgets, `apply_over` | "Create reusable components" |
| [robius-event-action](./skills/robius-event-action/) | Custom actions, `MatchEvent` | "Custom event handling" |
| [robius-state-management](./skills/robius-state-management/) | AppState, persistence | "Save/load app state" |
| [robius-matrix-integration](./skills/robius-matrix-integration/) | Matrix SDK integration | "Chat client features" |

#### MolyKit (1 Skill)

| Skill | Description | When to Use |
|-------|-------------|-------------|
| [molykit](./skills/molykit/) | AI chat, SSE streaming, `BotClient` | "AI chat integration" |

### Extended Skills (3)

**Note:** Production patterns are now integrated into robius-* skills:
- Widget patterns (11) → `robius-widget-patterns/_base/`
- State patterns (5) → `robius-state-management/_base/`
- Async patterns (3) → `robius-app-architecture/_base/`

#### [makepad-deployment](../bmad_repo/SKILL.md) - Build & Package

Build for desktop (Linux, Windows, macOS), mobile (Android, iOS), and web (WebAssembly).

#### [makepad-reference](../bmad_repo/SKILL.md) - Reference Materials

| File | Description | When to Use |
|------|-------------|-------------|
| troubleshooting.md | Common errors and fixes | "Apply error: no matching field" |
| code-quality.md | Makepad-aware refactoring | "Simplify this code" |
| adaptive-layout.md | Desktop/mobile responsive | "Support both desktop and mobile" |

#### [evolution](../bmad_repo/SKILL.md) - Self-Improvement

| Component | Description |
|-----------|-------------|
| `templates/` | Pattern, shader, and troubleshooting templates |
| `hooks/` | Auto-detection and validation hooks |
| `references/` | Collaboration guidelines |

## Usage Examples

### Create a New Project
```
User: Create a new Makepad app called "my-app" with a counter button
Claude: [Uses makepad-basics for scaffolding, makepad-widgets for button/counter]
```

### Add a Tooltip
```
User: Add a tooltip that shows user info on hover
Claude: [Uses robius-widget-patterns/_base/14-callout-tooltip.md for complete implementation]
```

### Save a Custom Pattern
```
User: Save this infinite scroll implementation as a community pattern
Claude: [Creates robius-widget-patterns/community/infinite-scroll.md]
```

### Fix Compilation Error
```
User: Getting "no matching field: font" error
Claude: [Uses makepad-reference/troubleshooting.md to identify correct text_style syntax]
```

## What You Can Build

With these skills, Claude can help you:

- Initialize new Makepad projects with proper structure
- Create custom widgets with `live_design!` DSL
- Handle events and user interactions
- Write GPU shaders for visual effects
- Implement smooth animations
- Manage application state with async/tokio
- Build responsive desktop/mobile layouts
- Package apps for all platforms
- **Capture and share patterns** you discover during development

## Projects Built with These Skills

Real-world projects created using makepad-skills and Claude Code:

| Project | Description | Time |
|---------|-------------|------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills-demo) | Currency converter app demo | ~20 min |
| [makepad-component](https://github.com/ZhangHanDong/makepad-component) | Reusable Makepad component library | - |

### makepad-skills-demo Screenshot

<p align="center">
  <img src="./assets/skill-app-demo.jpg" width="60%" alt="Currency Converter App" />
</p>

### makepad-component Screenshots

<p align="center">
  <img src="./assets/mc1.png" width="45%" alt="Component 1" />
  <img src="./assets/mc2.png" width="45%" alt="Component 2" />
</p>
<p align="center">
  <img src="./assets/mc3.png" width="45%" alt="Component 3" />
  <img src="./assets/mc4.png" width="45%" alt="Component 4" />
</p>

## Resources

- [Makepad Repository](https://github.com/makepad/makepad)
- [Makepad Examples](https://github.com/makepad/makepad/tree/main/examples)
- [Project Robius](https://github.com/project-robius)
- [Robrix](https://github.com/project-robius/robrix)
- [Moly](https://github.com/moxin-org/moly)

## License

MIT
```

## File: `README.zh-CN.md`
```markdown
# Makepad 的 Agent Skills

[English](./README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](./.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

用于在 Rust 中使用 [Makepad](https://github.com/makepad/makepad) 框架构建跨平台 UI 应用的 Agent Skills。

## 关于 Makepad

[Makepad](https://github.com/makepad/makepad) 是一个用 Rust 编写的新一代 UI 框架，能够构建高性能的跨平台应用。主要特性包括：

- **跨平台**：单一代码库支持桌面端（macOS、Windows、Linux）、移动端（Android、iOS）和 Web（WebAssembly）
- **GPU 加速**：基于自定义着色器的渲染，使用 SDF（有向距离场）绘制
- **实时设计**：可热重载的 `live_design!` DSL，实现快速 UI 开发
- **高性能**：原生编译，无虚拟 DOM，极低的运行时开销

## 关于 Robius

[Project Robius](https://github.com/project-robius) 是一个开源项目，致力于用 Rust 构建功能完整的应用开发框架。使用 Makepad 构建的生产级应用包括：

- **[Robrix](https://github.com/project-robius/robrix)** - Matrix 聊天客户端，展示了实时消息、端到端加密和复杂 UI 模式
- **[Moly](https://github.com/moxin-org/moly)** - AI 模型管理器，展示了数据密集型界面和异步操作

这些 Skills 提取自 Robrix 和 Moly 中使用的模式。

## 安装

### 插件市场安装（推荐）

通过 Claude Code 的插件市场安装：

```bash
# 第一步：添加市场
/plugin marketplace add ZhangHanDong/makepad-skills

# 第二步：安装插件（选择一个或多个）
/plugin install makepad-full@makepad-skills-marketplace        # 全部技能
/plugin install makepad-core@makepad-skills-marketplace        # 核心 + 入门
/plugin install makepad-graphics@makepad-skills-marketplace    # 图形 & 着色器
/plugin install makepad-patterns@makepad-skills-marketplace    # 生产模式
/plugin install makepad-deployment@makepad-skills-marketplace  # 平台打包
/plugin install makepad-reference@makepad-skills-marketplace   # API 文档 & 问题排查
```

**可用插件：**

| 插件 | 说明 |
|------|------|
| `makepad-full` | 包含所有技能的完整包 |
| `makepad-core` | 入门、布局、组件、事件 |
| `makepad-graphics` | SDF 绘图、着色器、动画 |
| `makepad-patterns` | 异步、状态机、弹窗、列表 |
| `makepad-deployment` | Android、iOS、WASM 打包 |
| `makepad-reference` | API 文档、问题排查、代码质量 |
| `makepad-evolution` | 自我进化模板和 hooks |

### 脚本安装

使用安装脚本一键完成：

```bash
# 安装到当前项目
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash

# 安装并启用 hooks
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks

# 安装到指定项目
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project

# --agent 不指定默认为: claude

# 安装到 Codex（.codex/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent codex

# 安装到 Gemini CLI（.gemini/skills）
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent gemini
```

Gemini CLI 说明：Skills 目前为实验性功能，如需使用请在 `/settings` 中启用 `experimental.skills`。

**脚本特性：**
- 自动检测 Rust/Makepad 项目（检查 Cargo.toml）
- 安装前自动备份已有 skills
- `--with-hooks` 复制并配置自我进化 hooks（仅 Claude Code）
- `--agent codex|claude-code|gemini` 选择 Codex、Claude Code 或 Gemini CLI（默认：claude-code）
- `--target` 支持安装到任意项目目录
- 彩色输出，清晰的进度提示

**可用选项：**

| 选项 | 说明 |
|------|------|
| `--target DIR` | 安装到指定目录（默认：当前目录） |
| `--with-hooks` | 启用自我进化 hooks（仅 Claude Code） |
| `--agent AGENT` | 设置Agent：`codex`、`claude-code` 或 `gemini`（默认：`claude-code`） |
| `--branch NAME` | 使用指定分支（默认：main） |
| `--help` | 显示帮助信息 |

### 手动安装

```bash
# 克隆此仓库
git clone https://github.com/ZhangHanDong/makepad-skills.git

# 复制到你的项目（https://code.claude.com/docs/en/skills）
cp -r makepad-skills/skills your-project/.claude/skills

# 复制到 Codex 项目（https://developers.openai.com/codex/skills）
cp -r makepad-skills/skills your-project/.codex/skills

# 复制到 Gemini CLI 项目（https://geminicli.com/docs/cli/skills/）
cp -r makepad-skills/skills your-project/.gemini/skills
```

安装后的项目结构（Codex/Gemini 请将 `.claude` 替换为 `.codex`/`.gemini`）：

```
your-project/
├── .claude/
│   └── skills/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── 00-getting-started/
│       ├── 01-core/
│       ├── 02-components/
│       ├── 03-graphics/
│       │   ├── _base/          # 官方 skills（原子化）
│       │   └── community/      # 社区贡献
│       ├── 04-patterns/
│       │   ├── _base/          # 官方 patterns（原子化）
│       │   └── community/      # 社区贡献
│       ├── 05-deployment/
│       ├── 06-reference/
│       ├── 99-evolution/
│       │   └── templates/      # 贡献模板
│       └── CONTRIBUTING.md
├── src/
└── Cargo.toml
```

更多详情请参阅 [Claude Code Skills 官方文档](https://docs.anthropic.com/en/docs/claude-code/skills)。

## GitHub Actions 打包

使用 Makepad Packaging Action 在 CI 中打包并发布 Makepad 应用。内部封装 `cargo-packager`（桌面）与 `cargo-makepad`（移动），并支持上传产物到 GitHub Releases。

Marketplace: [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)

```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  with:
    args: --target x86_64-unknown-linux-gnu --release
```

注意：
- 桌面包必须在对应 OS runner 上构建。
- iOS 需要 macOS runner。

## 架构：面向协作的原子化 Skills

### 为什么采用原子化结构？

v2.1 引入了**原子化 skill 结构**，专为协作开发设计：

```
04-patterns/
├── SKILL.md              # 索引文件
├── _base/                # 官方 patterns（编号、原子化）
│   ├── 01-widget-extension.md
│   ├── 02-modal-overlay.md
│   ├── ...
│   └── 14-callout-tooltip.md
└── community/            # 你的贡献
    ├── README.md
    └── {github用户名}-{pattern名称}.md
```

**优势：**
- **无合并冲突**：你的 `community/` 文件永远不会与官方 `_base/` 更新冲突
- **并行开发**：多个用户可以同时贡献
- **清晰归属**：文件名中的 GitHub 用户名提供署名
- **渐进式披露**：SKILL.md 索引 → 单个 pattern 详情

### 自我进化：从开发中沉淀 Skills

自我进化功能允许你捕获开发过程中发现的模式，并添加到 skills 中。

#### 工作原理

1. **开发过程中**：你在使用 Makepad 构建应用时发现有用的模式、着色器或错误解决方案

2. **捕获模式**：让 Claude 保存它：
   ```
   用户：这个 tooltip 定位逻辑很有用，保存为社区 pattern
   Claude：[使用模板创建 community/{用户名}-tooltip-positioning.md]
   ```

3. **自动检测**（启用 hooks 后）：当你遇到并修复错误时，系统可以自动将解决方案捕获到 troubleshooting

#### 启用自我进化 Hooks（可选）

```bash
# 从 99-evolution 复制 hooks 到项目
cp -r your-project/.claude/skills/99-evolution/hooks your-project/.claude/skills/hooks

# 添加执行权限
chmod +x your-project/.claude/skills/hooks/*.sh

# 将 hooks 配置添加到 .claude/settings.json
# 参考 skills/99-evolution/hooks/settings.example.json
```

#### 手动创建 Pattern

直接让 Claude 创建：
```
用户：把我刚才实现的拖拽排序保存为社区 pattern
Claude：我将使用模板创建...
```

Claude 会：
1. 使用 `99-evolution/templates/pattern-template.md` 模板
2. 在 `04-patterns/community/{你的用户名}-drag-drop-reorder.md` 创建文件
3. 填写 frontmatter 和内容

### 社区贡献指南

#### 贡献 Patterns

1. **创建 pattern 文件**：
   ```
   04-patterns/community/{github用户名}-{pattern名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/pattern-template.md` 复制

3. **必需的 frontmatter**：
   ```yaml
   ---
   name: my-pattern-name
   author: your-github-handle
   source: project-where-you-discovered-this
   date: 2024-01-15
   tags: [tag1, tag2, tag3]
   level: beginner|intermediate|advanced
   ---
   ```

4. **提交 PR** 到主仓库

#### 贡献着色器/效果

1. **创建效果文件**：
   ```
   03-graphics/community/{github用户名}-{效果名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/shader-template.md` 复制

#### 贡献错误解决方案

1. **创建 troubleshooting 条目**：
   ```
   06-reference/troubleshooting/{错误名称}.md
   ```

2. **使用模板**：从 `99-evolution/templates/troubleshooting-template.md` 复制

#### 与上游同步

保持本地 skills 更新，同时保留你的贡献：

```bash
# 如果你已 fork 仓库
git fetch upstream
git merge upstream/main --no-edit
# 你的 community/ 文件不会与 _base/ 变更冲突
```

#### 晋升路径

高质量的社区贡献可能会被提升到 `_base/`：
- Pattern 广泛有用且经过充分测试
- 文档完整
- 社区反馈积极
- 通过 `author` 字段保留署名

## Skills 概览 (v2.1 原子化结构)

### [00-getting-started](../bmad_repo/SKILL.md) - 项目设置

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [init.md](../../../vault/archives/archive_legacy/claudekit/src/commands/agents-md/init.md) | 项目脚手架 | "创建一个新的 Makepad 应用" |
| [project-structure.md](./skills/00-getting-started/project-structure.md) | 目录组织 | "我应该如何组织项目？" |

### [01-core](../bmad_repo/SKILL.md) - 核心开发

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [layout.md](../../../vault/archives/archive_legacy/vscode/src/vs/sessions/LAYOUT.md) | 流式布局、尺寸、间距、对齐 | "排列 UI 元素" |
| [widgets.md](./skills/01-core/widgets.md) | 常用组件、自定义组件 | "如何创建按钮？" |
| [events.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/simpy/references/events.md) | 事件处理、命中测试 | "处理点击事件" |
| [styling.md](./skills/01-core/styling.md) | 字体、文本样式、SVG 图标 | "修改字体大小"、"添加图标" |

### [02-components](../bmad_repo/SKILL.md) - 组件库

所有内置组件参考（来自 ui_zoo）：Button、TextInput、Slider、Checkbox、Label、Image、ScrollView、PortalList、PageFlip 等。

### [03-graphics](../bmad_repo/SKILL.md) - 图形与动画（原子化）

`_base/` 中包含 14 个独立 skills：

| 类别 | Skills |
|------|--------|
| 着色器基础 | `01-shader-structure`, `02-shader-math` |
| SDF 绘制 | `03-sdf-shapes`, `04-sdf-drawing`, `05-progress-track` |
| 动画 | `06-animator-basics`, `07-easing-functions`, `08-keyframe-animation`, `09-loading-spinner` |
| 视觉效果 | `10-hover-effect`, `11-gradient-effects`, `12-shadow-glow`, `13-disabled-state`, `14-toggle-checkbox` |

另有 `community/` 存放你的自定义效果。

### [04-patterns](../bmad_repo/SKILL.md) - 生产模式（原子化）

`_base/` 中包含 14 个独立 patterns：

| 类别 | Patterns |
|------|----------|
| 组件模式 | `01-widget-extension`, `02-modal-overlay`, `03-collapsible`, `04-list-template`, `05-lru-view-cache`, `06-global-registry`, `07-radio-navigation` |
| 数据模式 | `08-async-loading`, `09-streaming-results`, `10-state-machine`, `11-theme-switching`, `12-local-persistence` |
| 高级模式 | `13-tokio-integration`, `14-callout-tooltip` |

另有 `community/` 存放你的自定义 patterns。

### [05-deployment](../bmad_repo/SKILL.md) - 构建与打包

构建桌面端（Linux、Windows、macOS）、移动端（Android、iOS）和 Web（WebAssembly）。

### [06-reference](../bmad_repo/SKILL.md) - 参考资料

| 文件 | 描述 | 使用场景 |
|------|------|----------|
| [troubleshooting.md](troubleshooting.md) | 常见错误及修复 | "Apply error: no matching field" |
| [code-quality.md](code-quality.md) | Makepad 感知的重构 | "简化这段代码" |
| [adaptive-layout.md](./skills/06-reference/adaptive-layout.md) | 桌面/移动端响应式 | "同时支持桌面端和移动端" |

### [99-evolution](../bmad_repo/SKILL.md) - 自我改进

| 组件 | 描述 |
|------|------|
| `templates/` | Pattern、shader 和 troubleshooting 模板 |
| `hooks/` | 自动检测和验证 hooks |

## 使用示例

### 创建新项目
```
用户：创建一个名为 "my-app" 的 Makepad 应用，包含一个计数器按钮
Claude：[使用 00-getting-started 搭建项目，使用 01-core 实现按钮/计数器]
```

### 添加 Tooltip
```
用户：添加一个悬停时显示用户信息的 tooltip
Claude：[使用 04-patterns/_base/14-callout-tooltip.md 获取完整实现]
```

### 保存自定义 Pattern
```
用户：把这个无限滚动实现保存为社区 pattern
Claude：[创建 04-patterns/community/yourhandle-infinite-scroll.md]
```

### 修复编译错误
```
用户：遇到 "no matching field: font" 错误
Claude：[使用 06-reference/troubleshooting.md 识别正确的 text_style 语法]
```

## 你可以构建什么

使用这些 Skills，Claude 可以帮助你：

- 使用正确的结构初始化新的 Makepad 项目
- 使用 `live_design!` DSL 创建自定义组件
- 处理事件和用户交互
- 编写 GPU 着色器实现视觉效果
- 实现流畅的动画
- 使用 async/tokio 管理应用状态
- 构建响应式的桌面端/移动端布局
- 为所有平台打包应用
- **捕获并分享**你在开发过程中发现的模式

## 基于这些 Skills 构建的项目

使用 makepad-skills 和 Claude Code 创建的真实项目：

| 项目 | 描述 | 耗时 |
|------|------|------|
| [makepad-skills-demo](https://github.com/ZhangHanDong/makepad-skills-demo) | 汇率转换应用示例 | 约 20 分钟 |
| [makepad-component](https://github.com/ZhangHanDong/makepad-component) | 可复用的 Makepad 组件库 | - |

### makepad-skills-demo 截图

<p align="center">
  <img src="./assets/skill-app-demo.jpg" width="60%" alt="汇率转换应用" />
</p>

### makepad-component 截图

<p align="center">
  <img src="./assets/mc1.png" width="45%" alt="组件 1" />
  <img src="./assets/mc2.png" width="45%" alt="组件 2" />
</p>
<p align="center">
  <img src="./assets/mc3.png" width="45%" alt="组件 3" />
  <img src="./assets/mc4.png" width="45%" alt="组件 4" />
</p>

## 资源

- [Makepad 仓库](https://github.com/makepad/makepad)
- [Makepad 示例](https://github.com/makepad/makepad/tree/main/examples)
- [Project Robius](https://github.com/project-robius)
- [Robrix](https://github.com/project-robius/robrix)
- [Moly](https://github.com/moxin-org/moly)

## 许可证

MIT
```

## File: `install.sh`
```bash
#!/bin/bash
#
# Makepad Skills Installer
# https://github.com/ZhangHanDong/makepad-skills
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --target /path/to/project
#   curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --agent your_agent
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
REPO_URL="https://github.com/ZhangHanDong/makepad-skills"
BRANCH="main"
TARGET_DIR=""
WITH_HOOKS=false
TARGET_AGENT="claude-code"
TEMP_DIR=""

# Print colored message
info() { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

# Print banner
print_banner() {
    echo ""
    echo -e "${BLUE}╔══════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC}      ${GREEN}Makepad Skills Installer v3.0.0${NC}         ${BLUE}║${NC}"
    echo -e "${BLUE}║${NC}      Agent Skills for Makepad                ${BLUE}║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════╝${NC}"
    echo ""
}

# Show usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --target DIR      Install to specific directory (default: current directory)"
    echo "  --with-hooks      Also install and configure hooks (Claude Code only)"
    echo "  --agent AGENT     Set agent (default: claude-code)"
    echo "  --list-agents     Show supported agents and exit"
    echo "  --branch BRANCH   Use specific branch (default: main)"
    echo "  --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  # Install to current project"
    echo "  $0"
    echo ""
    echo "  # Install with hooks enabled"
    echo "  $0 --with-hooks"
    echo ""
    echo "  # Install to specific project"
    echo "  $0 --target /path/to/my-makepad-project"
    echo ""
    echo "  # Install for a specific agent"
    echo "  $0 --agent your_agent"
    echo ""
}

list_agents() {
    echo "Supported agents:"
    echo "  - claude-code (default)"
    echo "  - codex"
    echo "  - gemini"
}

# Parse arguments
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --target)
                TARGET_DIR="$2"
                shift 2
                ;;
            --with-hooks)
                WITH_HOOKS=true
                shift
                ;;
            --agent)
                if [[ -z "$2" ]]; then
                    error "Missing value for --agent (codex|claude-code|gemini)"
                fi
                TARGET_AGENT="$2"
                shift 2
                ;;
            --list-agents)
                list_agents
                exit 0
                ;;
            --codex)
                TARGET_AGENT="codex"
                shift
                ;;
            --claude|--claude-code)
                TARGET_AGENT="claude-code"
                shift
                ;;
            --branch)
                BRANCH="$2"
                shift 2
                ;;
            --help)
                usage
                exit 0
                ;;
            *)
                error "Unknown option: $1"
                ;;
        esac
    done
}

normalize_agent() {
    case "$TARGET_AGENT" in
        codex)
            ;;
        gemini)
            ;;
        claude|claude-code)
            TARGET_AGENT="claude-code"
            ;;
        *)
            error "Unknown agent: $TARGET_AGENT (expected codex, claude-code, or gemini)"
            ;;
    esac
}

agent_label() {
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "Codex"
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "Gemini CLI"
    else
        echo "Claude Code"
    fi
}

skills_base_dir() {
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "$TARGET_DIR/.codex"
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "$TARGET_DIR/.gemini"
    else
        echo "$TARGET_DIR/.claude"
    fi
}

skills_dir() {
    echo "$(skills_base_dir)/skills"
}

# Check dependencies
check_deps() {
    info "Checking dependencies..."

    # Need either curl or git
    if ! command -v curl &> /dev/null && ! command -v git &> /dev/null; then
        error "Either curl or git is required. Please install one of them first."
    fi

    # Need unzip if using curl
    if command -v curl &> /dev/null && ! command -v unzip &> /dev/null; then
        if ! command -v git &> /dev/null; then
            error "unzip is required when using curl. Please install unzip or git."
        fi
        warn "unzip not found, will use git instead"
    fi

    success "Dependencies OK"
}

# Determine target directory
determine_target() {
    if [[ -z "$TARGET_DIR" ]]; then
        TARGET_DIR="$(pwd)"
    fi

    # Expand to absolute path
    TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd)" || error "Target directory does not exist: $TARGET_DIR"

    info "Target directory: $TARGET_DIR"

    # Check if it looks like a project directory
    if [[ ! -f "$TARGET_DIR/Cargo.toml" ]]; then
        warn "No Cargo.toml found. This may not be a Rust/Makepad project."
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
}

# Clone or download repository
download_skills() {
    info "Downloading makepad-skills..."

    TEMP_DIR=$(mktemp -d)
    trap "rm -rf $TEMP_DIR" EXIT

    # Try ZIP download first (no git required)
    local ZIP_URL="https://github.com/ZhangHanDong/makepad-skills/archive/refs/heads/${BRANCH}.zip"

    if command -v curl &> /dev/null; then
        curl -fsSL "$ZIP_URL" -o "$TEMP_DIR/makepad-skills.zip" 2>/dev/null
        if [[ $? -eq 0 && -f "$TEMP_DIR/makepad-skills.zip" ]]; then
            unzip -q "$TEMP_DIR/makepad-skills.zip" -d "$TEMP_DIR" 2>/dev/null
            mv "$TEMP_DIR/makepad-skills-${BRANCH}" "$TEMP_DIR/makepad-skills"
            success "Downloaded via ZIP"
            return
        fi
    fi

    # Fallback to git clone
    if command -v git &> /dev/null; then
        git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TEMP_DIR/makepad-skills" 2>/dev/null && \
            success "Downloaded via git" && return
    fi

    error "Failed to download. Please check your internet connection."
}

# Install skills
install_skills() {
    local SKILLS_DIR
    SKILLS_DIR="$(skills_dir)"

    info "Installing skills for $(agent_label) to $SKILLS_DIR..."

    # Create base directory if needed
    mkdir -p "$(skills_base_dir)"

    # Backup existing skills if present
    if [[ -d "$SKILLS_DIR" ]]; then
        local BACKUP_DIR="$SKILLS_DIR.backup.$(date +%Y%m%d%H%M%S)"
        warn "Existing skills found. Backing up to $BACKUP_DIR"
        mv "$SKILLS_DIR" "$BACKUP_DIR"
    fi

    # Copy skills
    cp -r "$TEMP_DIR/makepad-skills/skills" "$SKILLS_DIR"

    success "Skills installed"
}

# Install hooks
install_hooks() {
    if [[ "$WITH_HOOKS" != true ]]; then
        return
    fi

    if [[ "$TARGET_AGENT" != "claude-code" ]]; then
        warn "Hooks are only supported in Claude Code. Skipping hook installation."
        return
    fi

    local BASE_DIR
    BASE_DIR="$(skills_base_dir)"
    local HOOKS_SRC="$TEMP_DIR/makepad-skills/.claude/hooks"
    local HOOKS_DST="$BASE_DIR/hooks"
    local SETTINGS_SRC="$TEMP_DIR/makepad-skills/.claude/settings.json"
    local SETTINGS_DST="$BASE_DIR/settings.json"

    info "Installing hooks to $HOOKS_DST..."

    # Create hooks directory
    mkdir -p "$HOOKS_DST"

    # Copy hook scripts
    if [[ -d "$HOOKS_SRC" ]]; then
        cp "$HOOKS_SRC"/*.sh "$HOOKS_DST/" 2>/dev/null || true
        chmod +x "$HOOKS_DST"/*.sh 2>/dev/null || true
        success "Hook scripts installed"
    else
        warn "Hook scripts source not found in .claude/hooks/, skipping"
    fi

    # Install settings.json (with UserPromptSubmit hook)
    if [[ -f "$SETTINGS_SRC" ]]; then
        if [[ -f "$SETTINGS_DST" ]]; then
            # Backup existing settings
            local BACKUP_SETTINGS="$SETTINGS_DST.backup.$(date +%Y%m%d%H%M%S)"
            warn "Existing settings.json found. Backing up to $BACKUP_SETTINGS"
            cp "$SETTINGS_DST" "$BACKUP_SETTINGS"
        fi
        cp "$SETTINGS_SRC" "$SETTINGS_DST"
        success "settings.json installed with UserPromptSubmit hook"
    else
        warn "settings.json source not found, creating default..."
        # Create default settings.json
        cat > "$SETTINGS_DST" << 'SETTINGS_EOF'
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/makepad-skill-router.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-bash.sh"
          }
        ]
      }
    ]
  }
}
SETTINGS_EOF
        success "Default settings.json created"
    fi

    echo ""
    info "Hooks are now configured for auto-triggering!"
    echo "  - UserPromptSubmit: Routes queries to appropriate skills"
    echo "  - PreToolUse: Detects Makepad version"
    echo "  - PostToolUse: Self-correction on errors"
}

# Print summary
print_summary() {
    local SKILLS_DIR
    SKILLS_DIR="$(skills_dir)"

    echo ""
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  Installation Complete!${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo ""
    echo "  Agent: $(agent_label)"
    echo "  Skills installed to: $SKILLS_DIR"
    echo ""
    echo "  Structure (19 Skills):"
    echo "  ├── # Core Skills (16)"
    echo "  ├── makepad-basics/          (App structure)"
    echo "  ├── makepad-dsl/             (DSL syntax)"
    echo "  ├── makepad-layout/          (Layout system)"
    echo "  ├── makepad-widgets/         (Widget components)"
    echo "  ├── makepad-event-action/    (Event handling)"
    echo "  ├── makepad-animation/       (Animation)"
    echo "  ├── makepad-shaders/         (Shaders & visual effects)"
    echo "  ├── makepad-platform/        (Platform support)"
    echo "  ├── makepad-font/            (Font, typography)"
    echo "  ├── makepad-splash/          (Splash scripting)"
    echo "  ├── robius-*/                (5 Robius patterns with _base/)"
    echo "  ├── molykit/                 (AI chat toolkit)"
    echo "  ├── # Extended Skills (3)"
    echo "  ├── makepad-deployment/      (Build & package)"
    echo "  ├── makepad-reference/       (Troubleshooting)"
    echo "  └── evolution/               (Self-improvement)"
    echo ""
    echo "  Quick Start:"
    if [[ "$TARGET_AGENT" == "codex" ]]; then
        echo "  1. Open your project with Codex"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    elif [[ "$TARGET_AGENT" == "gemini" ]]; then
        echo "  1. Open your project with Gemini CLI"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    else
        echo "  1. Open your project with Claude Code"
        echo "  2. Ask: \"Create a simple Makepad counter app\""
    fi
    echo ""
    if [[ "$TARGET_AGENT" != "claude-code" ]]; then
        if [[ "$WITH_HOOKS" == true ]]; then
            echo -e "  ${YELLOW}Hooks are only supported in Claude Code.${NC}"
            echo ""
        fi
    else
        if [[ "$WITH_HOOKS" == true ]]; then
            echo -e "  ${GREEN}Hooks are installed and auto-configured!${NC}"
            echo "  Skills will auto-trigger based on your questions."
            echo ""
        else
            echo "  To enable auto-triggering hooks, run:"
            echo "  curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks --target $TARGET_DIR"
            echo ""
        fi
    fi
    echo "  Documentation: https://github.com/ZhangHanDong/makepad-skills"
    echo ""
}

# Main
main() {
    print_banner
    parse_args "$@"
    normalize_agent
    check_deps
    determine_target
    download_skills
    install_skills
    install_hooks
    print_summary
}

main "$@"
```

## File: `metadata.json`
```json
{
  "name": "makepad-skills",
  "version": "2.0.0",
  "description": "Comprehensive Makepad, Robius, and MolyKit skills for Claude with auto-triggering",
  "author": "makepad-skills contributors",
  "license": "MIT",
  "repository": "https://github.com/ZhangHanDong/makepad-skills",

  "stats": {
    "makepad_skills": 11,
    "robius_skills": 5,
    "molykit_skills": 1,
    "extended_skills": 3,
    "total_skills": 20
  },

  "skills": {
    "router": [
      "makepad-router"
    ],
    "makepad": [
      "makepad-basics",
      "makepad-dsl",
      "makepad-layout",
      "makepad-widgets",
      "makepad-event-action",
      "makepad-animation",
      "makepad-shaders",
      "makepad-platform",
      "makepad-font",
      "makepad-splash"
    ],
    "robius": [
      "robius-app-architecture",
      "robius-widget-patterns",
      "robius-event-action",
      "robius-state-management",
      "robius-matrix-integration"
    ],
    "molykit": [
      "molykit"
    ],
    "extended": [
      "makepad-deployment",
      "makepad-reference",
      "evolution"
    ]
  },

  "triggers": {
    "makepad": [
      "makepad", "live_design!", "app_main!", "Widget", "View", "Button",
      "Label", "TextInput", "draw_bg", "Sdf2d", "shader", "animator",
      "Flow", "Walk", "Size", "Padding", "WidgetRef", "WidgetAction"
    ],
    "robius": [
      "robius", "robrix", "AppState", "Scope::with_data", "MatrixRequest",
      "TimelineUpdate", "submit_async_request", "MatchEvent", "handle_actions",
      "widget extension", "modal", "collapsible", "LRU cache", "drag-drop",
      "theme switching", "state machine", "persistence", "async loading", "tokio"
    ],
    "molykit": [
      "molykit", "moly-kit", "BotClient", "BotContext", "PlatformSend",
      "SSE streaming", "AI chat", "OpenAI Makepad"
    ],
    "extended": [
      "deployment", "android", "iOS", "WASM", "packaging",
      "GitHub Actions", "CI", "action", "marketplace", "release",
      "troubleshooting", "error", "code quality", "adaptive layout",
      "self-evolution", "hooks", "templates", "contribution"
    ]
  },

  "source_projects": {
    "makepad": "https://github.com/makepad/makepad",
    "robrix": "https://github.com/project-robius/robrix",
    "moly": "https://github.com/moxin-org/moly",
    "molykit": "https://github.com/moxin-org/moly/tree/main/moly-kit"
  },

  "compatibility": {
    "claude_code_min_version": "2.1.0",
    "makepad_version": "0.6.0+",
    "rust_edition": "2024"
  },

  "last_updated": "2026-02-04",
  "quality_checks": {
    "skill_frontmatter": true,
    "llms_txt_present": true,
    "references_present": true
  }
}
```

## File: `skills/CONTRIBUTING.md`
```markdown
# Contributing to Makepad Skills

Thank you for contributing to the Makepad skills ecosystem! This guide explains how to contribute patterns, shaders, hooks, and troubleshooting entries.

## Directory Structure

```
skills/
├── # Core Skills (16) - Use the corresponding skill for each topic
├── makepad-basics/          # App structure, getting started
├── makepad-dsl/             # DSL syntax, inheritance
├── makepad-layout/          # Layout, sizing, alignment
├── makepad-widgets/         # Widget components
├── makepad-event-action/    # Event handling
├── makepad-animation/       # Animation, states
├── makepad-shaders/         # Shader basics
├── makepad-platform/        # Platform support
├── makepad-font/            # Font, typography
├── makepad-splash/          # Splash scripting
├── robius-*/                # 5 Robius patterns
├── molykit/                 # AI chat toolkit
│
├── # Extended Skills (3) - Community contributions go here
├── makepad-shaders/
│   ├── _base/               # Official skills (numbered) - DO NOT modify
│   └── community/           # Community contributions
├── makepad-deployment/      # Build & packaging
├── makepad-reference/
│   └── troubleshooting/     # Error/solution documentation
│
├── # Note: Production patterns in robius-* skills:
├── # robius-widget-patterns/_base/   (modal, collapsible, etc.)
├── # robius-state-management/_base/  (theme, state machine, etc.)
├── # robius-app-architecture/_base/  (async loading, tokio, etc.)
│
└── evolution/
    ├── hooks/               # Hook scripts
    ├── references/          # Detailed guides
    └── templates/           # Contribution templates
```

## Contribution Types

### 1. Community Patterns

Add your pattern to the appropriate robius-* skill's community directory:
- Widget patterns → `robius-widget-patterns/community/`
- State patterns → `robius-state-management/community/`
- Async patterns → `robius-app-architecture/community/`

**File naming**: `{descriptive-pattern-name}.md` (NO GitHub handle in filename)

Examples:
- `drag-drop-list.md`
- `infinite-scroll.md`
- `theme-persistence.md`

**Template**: Copy from `evolution/templates/pattern-template.md`

### 2. Community Shaders/Effects

Add your shader to `makepad-shaders/community/`:

**File naming**: `{descriptive-effect-name}.md` (NO GitHub handle in filename)

Examples:
- `glassmorphism.md`
- `neon-glow.md`
- `particle-trail.md`

**Template**: Copy from `evolution/templates/shader-template.md`

### 3. Troubleshooting Entries

Add error solutions to `makepad-reference/troubleshooting/`:

**File naming**: `{error-short-name}.md`

Examples:
- `widget-not-found.md`
- `animator-not-playing.md`
- `shader-compile-error.md`

**Template**: Copy from `evolution/templates/troubleshooting-template.md`

### 4. Deployment Examples

Add CI/CD packaging examples to `makepad-deployment/community/`.

**File naming**: `{descriptive-example-name}.md` (NO GitHub handle in filename)

Include YAML frontmatter and a concise, runnable snippet. If the example is
adapted from another repo, add a `source` link.

### 5. Hooks

Add hooks to `evolution/hooks/`:

**File naming**: `{hook-purpose}.sh`

**Template**: Copy from `evolution/templates/hook-template.md`

**Additional requirements**: See [Hook Testing Requirements](#hook-testing-requirements) below.

## Frontmatter Format

Every contribution must include YAML frontmatter:

```yaml
---
name: my-pattern-name
author: your-github-handle          # Your ID goes here, NOT in filename
source: project-where-you-discovered-this
date: 2024-01-15
tags: [tag1, tag2, tag3]
level: beginner|intermediate|advanced
makepad-branch: main|dev            # Required: specify which branch this works with
---
```

## Naming Conflict Resolution

Since filenames don't include GitHub handles, conflicts may occur:

1. **First come, first served** - Merged PR owns the name
2. **Use descriptive suffix** for different approaches:
   - ✓ `drag-drop-native.md` vs `drag-drop-gesture.md`
   - ✗ `drag-drop.md` vs `drag-drop-v2.md`
3. **Maintainer decides** - May merge or replace if new version is clearly better

## Testing Requirements

### All Contributions Must Be Tested

Before submitting PR, verify:

- [ ] Code compiles with `cargo build`
- [ ] Tested in a real Makepad project
- [ ] All `live_design!` blocks are valid DSL
- [ ] Examples work as documented

**In PR description, include:**
```markdown
## Testing
- Tested with: [project name or "standalone test"]
- Makepad branch: main/dev
- Platform: macOS/Linux/Windows
```

### Hook Testing Requirements

Hooks require additional verification:

- [ ] Tested with `claude --with-hooks` flag
- [ ] Provided `settings.example.json` snippet in PR
- [ ] Documented prerequisites (e.g., `jq`, `bash 4+`)
- [ ] Works on macOS and Linux (note Windows limitations if any)

**Required in PR for hooks:**

1. **settings.example.json snippet** showing exact configuration
2. **Test evidence** describing trigger scenario and behavior

## Quality Guidelines

### Patterns Should:
- Solve a real, reusable problem
- Include working code examples
- Explain when to use (and when not to)
- Be tested in a real project

### Shaders Should:
- Produce a visible, useful effect
- Be performant (avoid heavy loops)
- Include inline comments explaining the math
- Document all customizable parameters

### Troubleshooting Should:
- Include exact error message
- Explain why the error occurs
- Show wrong vs. correct code
- Provide copy-pasteable solutions

### Hooks Should:
- Solve a specific automation need
- Be tested with `claude --with-hooks`
- Include ready-to-use settings.example.json
- Document all prerequisites

## Workflow

### Using Self-Evolution Skill

If you have the makepad-skills installed, use the self-evolution skill to add your contribution:

```
# In your Claude Code session
/evolve add pattern my-new-pattern

# Claude will guide you through creating the pattern
```

### Manual Contribution

1. Fork the repository
2. Create your file in the appropriate `community/` directory
3. Test your contribution thoroughly
4. Fill in the template with your content
5. Submit a Pull Request with testing evidence

### Syncing Upstream

To sync your fork with new official content while keeping your contributions:

```bash
git fetch upstream
git merge upstream/main --no-edit
```

Your `community/` files won't conflict with `_base/` changes.

## PR Checklist

Copy this checklist to your PR description:

```markdown
## Contribution Type
- [ ] Pattern
- [ ] Shader/Effect
- [ ] Troubleshooting
- [ ] Hook

## Required Checks
- [ ] File in correct `community/` directory
- [ ] Frontmatter includes `author` and `makepad-branch`
- [ ] Code tested and working
- [ ] No modification to `_base/` files

## Testing Evidence
- Tested with: [project name]
- Makepad branch: [main/dev]
- Platform: [macOS/Linux/Windows]

## For Hooks Only
- [ ] Tested with `claude --with-hooks`
- [ ] Included settings.example.json snippet
- [ ] Documented prerequisites
```

## Promotion Path

High-quality community contributions may be promoted to `_base/`:

1. Pattern is widely useful
2. Code is well-tested
3. Documentation is complete
4. Community feedback is positive

Promoted patterns:
- Get a numbered prefix (e.g., `15-community-pattern.md`)
- Move to `_base/` directory
- Credit preserved via `author` field

## File Organization Principles

### Why `_base/` + `community/`?

1. **No merge conflicts**: Your community files never conflict with official updates
2. **Attribution**: Your GitHub handle in frontmatter provides clear credit
3. **Discoverability**: SKILL.md indexes both directories
4. **Quality tiers**: Official vs community is clear

### Why One Pattern Per File?

1. **Atomic updates**: Change one pattern without affecting others
2. **Parallel contributions**: Multiple people can add patterns simultaneously
3. **Easy linking**: Direct links to specific patterns
4. **Progressive disclosure**: Users see index first, dive into details

## Code Style

### Rust Code

```rust
// Include necessary imports
use makepad_widgets::*;

// Add comments for non-obvious code
live_design! {
    // Explain what this widget does
    MyWidget = {{MyWidget}} {
        // ...
    }
}
```

### DSL Code

```rust
live_design! {
    // Use consistent indentation (4 spaces)
    MyView = <View> {
        width: Fill
        height: Fit

        // Group related properties
        flow: Down
        spacing: 10
        padding: 20
    }
}
```

## Detailed Guidelines

For more details, see [Collaboration Guidelines](evolution/references/collaboration.md).

## Questions?

- Open an issue on GitHub
- Tag `@robius` in discussions
- Check existing patterns for examples

Happy contributing!
```

## File: `skills/evolution/SKILL.md`
```markdown
---
name: evolution
description: |
  CRITICAL: Use for makepad-skills self-evolution and contribution. Triggers on:
  evolve, evolution, contribute, contribution, self-improve, self-improvement,
  add pattern, new pattern, capture learning, document solution,
  hooks, hook system, auto-trigger, skill routing,
  template, pattern template, shader template, troubleshooting template,
  演进, 贡献, 自我改进, 添加模式, 记录学习, 文档化解决方案
---

# Makepad Skills Evolution

This skill enables makepad-skills to self-improve continuously during development.

## Quick Navigation

| Topic | Description |
|-------|-------------|
| [Collaboration Guidelines](references/collaboration.md) | **Contributing to makepad-skills** |
| [Hooks Setup](#hooks-based-auto-triggering) | Auto-trigger evolution with hooks |
| [When to Evolve](#when-to-evolve) | Triggers and classification |
| [Evolution Process](#evolution-process) | Step-by-step guide |
| [Self-Correction](#self-correction) | Auto-fix skill errors |
| [Self-Validation](#self-validation) | Verify skill accuracy |
| [Version Adaptation](#version-adaptation) | Multi-branch support |

---

## Hooks-Based Auto-Triggering

For reliable automatic triggering, use Claude Code hooks. Install with `--with-hooks`:

```bash
# Install makepad-skills with hooks enabled
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks
```

This will install hooks to `.claude/hooks/` and configure `.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/makepad-skill-router.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-bash.sh"
          }
        ]
      }
    ]
  }
}
```

### What Hooks Do

| Hook | Trigger Event | Action |
|------|---------------|--------|
| `makepad-skill-router.sh` | UserPromptSubmit | Auto-route to relevant skills |
| `pre-tool.sh` | Before Bash/Write/Edit | Detect Makepad version from Cargo.toml |
| `post-bash.sh` | After Bash command fails | Detect Makepad errors, suggest fixes |
| `session-end.sh` | Session ends | Prompt to capture learnings |

---

## Skill Routing and Bundling

The `makepad-skill-router.sh` hook automatically loads relevant skills based on user queries.

### Context Detection

| Context | Trigger Keywords | Skills Loaded |
|---------|------------------|---------------|
| **Full App** | "build app", "从零", "完整应用" | basics, dsl, layout, widgets, event-action, app-architecture |
| **UI Design** | "ui design", "界面设计" | dsl, layout, widgets, animation, shaders |
| **Widget Creation** | "create widget", "创建组件", "自定义组件" | widgets, dsl, layout, animation, shaders, font, event-action |
| **Production** | "best practice", "robrix pattern", "实际项目" | app-architecture, widget-patterns, state-management, event-action |

### Skill Dependencies

When loading certain skills, related skills are auto-loaded:

| Primary Skill | Auto-loads |
|---------------|------------|
| robius-app-architecture | makepad-basics, makepad-event-action |
| robius-widget-patterns | makepad-widgets, makepad-layout |
| makepad-widgets | makepad-layout, makepad-dsl |
| makepad-animation | makepad-shaders |
| makepad-shaders | makepad-widgets |
| makepad-font | makepad-widgets |
| robius-event-action | makepad-event-action |

### Example

```
User: "我想从零开发一个 Makepad 应用"

[makepad-skills] Detected Makepad/Robius query
[makepad-skills] App development context detected - loading skill bundle
[makepad-skills] Routing to: makepad-basics makepad-dsl makepad-event-action
                            makepad-layout makepad-widgets robius-app-architecture
```

---

## When to Evolve

Trigger skill evolution when any of these occur during development:

| Trigger | Target Skill | Priority |
|---------|--------------|----------|
| New widget pattern discovered | robius-widget-patterns/_base | High |
| Shader technique learned | makepad-shaders | High |
| Compilation error solved | makepad-reference/troubleshooting | High |
| Layout solution found | makepad-reference/adaptive-layout | Medium |
| Build/packaging issue resolved | makepad-deployment | Medium |
| New project structure insight | makepad-basics | Low |
| Core concept clarified | makepad-dsl/makepad-widgets | Low |

---

## Evolution Process

### Step 1: Identify Knowledge Worth Capturing

Ask yourself:
- Is this a reusable pattern? (not project-specific)
- Did it take significant effort to figure out?
- Would it help other Makepad developers?
- Is it not already documented in makepad-skills?

### Step 2: Classify the Knowledge

```
Widget/Component Pattern     → robius-widget-patterns/_base/
Shader/Visual Effect         → makepad-shaders/
Error/Debug Solution         → makepad-reference/troubleshooting.md
Layout/Responsive Design     → makepad-reference/adaptive-layout.md
Build/Deploy Issue           → makepad-deployment/SKILL.md
Project Structure            → makepad-basics/
Core Concept/API             → makepad-dsl/ or makepad-widgets/
```

### Step 3: Format the Contribution

**For Patterns**:
```markdown
## Pattern N: [Pattern Name]

Brief description of what this pattern solves.

### live_design!
```rust
live_design! {
    // DSL code
}
```

### Rust Implementation
```rust
// Rust code
```
```

**For Troubleshooting**:
```markdown
### [Error Type/Message]

**Symptom**: What the developer sees

**Cause**: Why this happens

**Solution**:
```rust
// Fixed code
```
```

### Step 4: Mark Evolution (NOT Version)

Add an evolution marker above new content:

```markdown
<!-- Evolution: 2024-01-15 | source: my-app | author: @zhangsan -->
```

### Step 5: Submit via Git

```bash
# Create branch for your contribution
git checkout -b evolution/add-loading-pattern

# Commit your changes
git add robius-widget-patterns/_base/my-pattern.md
git commit -m "evolution: add loading state pattern from my-app"

# Push and create PR
git push origin evolution/add-loading-pattern
```

---

## Self-Correction

When skill content causes errors, automatically correct it.

### Trigger Conditions

```
User follows skill advice → Code fails to compile/run → Claude identifies skill was wrong
                                                      ↓
                                         AUTO: Correct skill immediately
```

### Correction Flow

1. **Detect** - Skill advice led to an error
2. **Verify** - Confirm the skill content is wrong
3. **Correct** - Update the skill file with fix

### Correction Marker Format

```markdown
<!-- Correction: YYYY-MM-DD | was: [old advice] | reason: [why it was wrong] -->
```

---

## Self-Validation

Periodically verify skill content is still accurate.

### Validation Checklist

```markdown
## Validation Report

### Code Examples
- [ ] All `live_design!` examples parse correctly
- [ ] All Rust code compiles
- [ ] All patterns work as documented

### API Accuracy
- [ ] Widget names exist in makepad-widgets
- [ ] Method signatures are correct
- [ ] Event types are accurate
```

### Validation Prompt

> "Please validate makepad-skills against current Makepad version"

---

## Version Adaptation

Provide version-specific guidance for different Makepad branches.

### Supported Versions

| Branch | Status | Notes |
|--------|--------|-------|
| main | Stable | Production ready |
| dev | Active | Latest features, may break |
| rik | Legacy | Older API style |

### Version Detection

Claude should detect Makepad version from:

1. **Cargo.toml branch reference**:
   ```toml
   makepad-widgets = { git = "...", branch = "dev" }
   ```

2. **Cargo.lock content**

3. **Ask user if unclear**

---

## Personalization

Adapt skill suggestions to project's coding style.

### Style Detection

Claude analyzes the current project to detect:

| Aspect | Detection Method | Adaptation |
|--------|------------------|------------|
| Naming convention | Scan existing widgets | Match snake_case vs camelCase |
| Code organization | Check module structure | Suggest matching patterns |
| Comment style | Read existing comments | Match documentation style |
| Widget complexity | Count lines per widget | Suggest appropriate patterns |

---

## Quality Guidelines

### DO Add
- Generic, reusable patterns
- Common errors with clear solutions
- Well-tested shader effects
- Platform-specific gotchas
- Performance optimizations

### DON'T Add
- Project-specific code
- Unverified solutions
- Duplicate content
- Incomplete examples
- Personal preferences without rationale

---

## Skill File Locations

```
skills/
├── # === Core Skills (16) ===
├── makepad-basics/        ← Getting started, app structure
├── makepad-dsl/           ← DSL syntax, inheritance
├── makepad-layout/        ← Layout, sizing, alignment
├── makepad-widgets/       ← Widget components
├── makepad-event-action/  ← Event handling
├── makepad-animation/     ← Animation, states
├── makepad-shaders/       ← Shader basics
├── makepad-platform/      ← Platform support
├── makepad-font/          ← Font, typography
├── makepad-splash/        ← Splash scripting
├── robius-app-architecture/   ← App architecture patterns
├── robius-widget-patterns/    ← Widget reuse patterns
├── robius-event-action/       ← Custom actions
├── robius-state-management/   ← State persistence
├── robius-matrix-integration/ ← Matrix SDK
├── molykit/               ← AI chat toolkit
│
├── # === Extended Skills (3) ===
├── makepad-shaders/ ← Advanced shaders, SDF
│   ├── _base/             ← Official patterns
│   └── community/         ← Community contributions
├── makepad-deployment/    ← Build & packaging
├── makepad-reference/     ← Troubleshooting, code quality
│
├── # Note: Production patterns integrated into robius-* skills:
├── # - Widget patterns → robius-widget-patterns/_base/
├── # - State patterns → robius-state-management/_base/
├── # - Async patterns → robius-app-architecture/_base/
│
└── evolution/             ← Self-evolution system
    ├── hooks/             ← Auto-trigger hooks
    ├── references/        ← Detailed guides
    └── templates/         ← Contribution templates
```

---

## Auto-Evolution Prompts

Use these prompts to trigger self-evolution:

### After Solving a Problem
> "This solution should be added to makepad-skills for future reference."

### After Creating a Widget
> "This widget pattern is reusable. Let me add it to makepad-patterns."

### After Debugging
> "This error and its fix should be documented in makepad-troubleshooting."

### After Completing a Feature
> "Review what I learned and update makepad-skills if applicable."

---

## Continuous Improvement Checklist

After each Makepad development session, consider:

- [ ] Did I discover a new widget composition pattern?
- [ ] Did I solve a tricky shader problem?
- [ ] Did I encounter and fix a confusing error?
- [ ] Did I find a better way to structure layouts?
- [ ] Did I learn something about packaging/deployment?
- [ ] Would any of this help other Makepad developers?

If yes to any, evolve the appropriate skill!

## References

- [makepad-skills repository](https://github.com/ZhangHanDong/makepad-skills)
- [Makepad documentation](https://github.com/makepad/makepad)
- [Project Robius](https://github.com/project-robius)
```

## File: `skills/evolution/hooks/README.md`
```markdown
# Makepad Skills Hooks

This folder contains Claude Code hooks to enable automatic triggering of makepad-skills features.

## Quick Setup

The easiest way to install hooks is using the installer:

```bash
curl -fsSL https://raw.githubusercontent.com/ZhangHanDong/makepad-skills/main/install.sh | bash -s -- --with-hooks
```

This will:
1. Copy skills to `.claude/skills/`
2. Copy hooks to `.claude/hooks/`
3. Create `.claude/settings.json` with hook configuration

## Manual Setup

Copy the hooks to `.claude/hooks/` and add to your `.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/makepad-skill-router.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-bash.sh"
          }
        ]
      }
    ]
  }
}
```

## Hooks Overview

| Hook | Trigger | Purpose |
|------|---------|---------|
| `makepad-skill-router.sh` | UserPromptSubmit | Auto-route queries to relevant skills |
| `pre-tool.sh` | Before Bash/Write/Edit | Detect Makepad version, validate dev branch |
| `post-bash.sh` | After Bash command | Detect compilation errors, suggest fixes |
| `session-end.sh` | Session ends | Prompt for evolution review (optional) |

## How It Works

1. **Skill Routing** (`makepad-skill-router.sh`): Analyzes user input and outputs JSON with `systemMessage` telling Claude which skills to load
2. **Version Detection** (`pre-tool.sh`): On first tool use, detects Makepad branch from Cargo.toml
3. **Error Detection** (`post-bash.sh`): Monitors `cargo build/run` output for common Makepad errors
4. **Evolution Prompt** (`session-end.sh`): Reminds to capture learnings at session end

## Output Format

Hooks output JSON that Claude Code interprets:

```json
{
  "continue": true,
  "systemMessage": "[makepad-skills] IMPORTANT: Before responding, you MUST call these skills: Skill(makepad-widgets), Skill(makepad-layout). These skills contain essential Makepad patterns and APIs."
}
```

---

## Optional: UI Specification Checker

The `pre-ui-edit.sh` hook checks UI code completeness to prevent text overlap issues.

### Prerequisites

```bash
# macOS
brew install jq

# Ubuntu/Debian
sudo apt install jq
```

### Setup

Add to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-ui-edit.sh"
          }
        ]
      }
    ]
  }
}
```

### What It Checks

When writing UI code (Button, Label, TextInput, RoundedView), checks for 5 properties:
- `width` - Fit / Fill / number
- `height` - Fit / Fill / number
- `padding` - { left, right, top, bottom } or number
- `draw_text` - { text_style, color }
- `wrap` - Word / Line / Ellipsis

If fewer than 3 properties are present, blocks and shows reminder.

### Technical Details

- Input: JSON via stdin `{"tool_name": "Edit", "tool_input": {...}}`
- Output: JSON with `continue: false` to block
- Exit code: `0` = allow, `2` = block
```

## File: `skills/evolution/hooks/makepad-skill-router.sh`
```bash
#!/bin/bash
# Makepad Skills Router - UserPromptSubmit Hook
#
# Analyzes user input and routes to appropriate skill
# Output goes to stderr so Claude can see it
#
# Usage: Called by Claude Code UserPromptSubmit hook
# Input: User's prompt via stdin (JSON format)

set -e

# Read user input from stdin
read -r USER_INPUT 2>/dev/null || USER_INPUT=""

# Extract the actual prompt text from JSON if present
# UserPromptSubmit provides: {"prompt": "user text here"}
if echo "$USER_INPUT" | grep -q '"prompt"'; then
    PROMPT=$(echo "$USER_INPUT" | sed 's/.*"prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/')
else
    PROMPT="$USER_INPUT"
fi

# Convert to lowercase for matching
PROMPT_LOWER=$(echo "$PROMPT" | tr '[:upper:]' '[:lower:]')

# Track matched skills
MATCHED_SKILLS=""

# ============================================================================
# Makepad Core Skills
# ============================================================================

# makepad-basics: Getting started, app structure
if echo "$PROMPT_LOWER" | grep -qE 'live_design!|app_main!|getting started|how to create|makepad app|入门|教程|hello world|appmaintf|appmaini|基础|创建.*应用'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-basics"
fi

# makepad-dsl: DSL syntax, inheritance
if echo "$PROMPT_LOWER" | grep -qE 'dsl|inheritance|prototype|<widget>|<view>|<button>|foo = \{|bar = \{|live.*syntax|继承|原型|dsl.*语法|如何定义.*组件'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-dsl"
fi

# makepad-layout: Layout system
if echo "$PROMPT_LOWER" | grep -qE 'layout|flow|walk|size|padding|margin|width|height|center|align|fit|fill|spacing|布局|居中|宽度|高度|对齐|间距'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-layout"
fi

# makepad-widgets: Widget components
if echo "$PROMPT_LOWER" | grep -qE '\bview\b|\bbutton\b|\blabel\b|\bimage\b|textinput|scrollview|roundedview|solidview|widget|\bmarkdown\b|\bhtml\b|textflow|rich.*text|富文本|markdown.*渲染|link.*click|链接.*点击|code.*block|代码块|组件|按钮|标签|视图|输入框|图片|列表'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-widgets"
fi

# makepad-event-action: Event handling
if echo "$PROMPT_LOWER" | grep -qE '\bevent\b|\baction\b|\bhit\b|fingerdown|fingerup|keydown|keyup|mousedown|handle_event|touchupdate|click|tap|事件|点击|触摸|键盘'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-event-action"
fi

# makepad-animation: Animation system
if echo "$PROMPT_LOWER" | grep -qE 'animat|state.*transition|hover.*effect|pressed.*state|animator|from:.*\{|play:.*\{|ease|动画|状态|过渡|悬停|按下'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-animation"
fi

# makepad-shaders: Shader and visual effects
if echo "$PROMPT_LOWER" | grep -qE 'shader|draw_bg|sdf2d|sdf\.|pixel|glsl|gradient|glow|shadow|visual.*effect|着色器|渐变|阴影|光效|绘制'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-shaders"
fi

# makepad-platform: Cross-platform support
if echo "$PROMPT_LOWER" | grep -qE 'platform|macos|windows|linux|android|ios|wasm|web|mobile|desktop|cross.*platform|跨平台|移动端|桌面端'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-platform"
fi

# makepad-font: Font and typography
if echo "$PROMPT_LOWER" | grep -qE 'font|text.*style|glyph|typography|font.*size|font.*family|text.*layout|字体|文字|排版|字号'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-font"
fi

# makepad-splash: Splash scripting language
if echo "$PROMPT_LOWER" | grep -qE 'splash|script!|cx\.eval|makepad.*script|dynamic.*ui|脚本|动态'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-splash"
fi

# ============================================================================
# Robius Pattern Skills
# ============================================================================

# robius-app-architecture: Async/Tokio integration
if echo "$PROMPT_LOWER" | grep -qE 'tokio|async.*runtime|submit_async|spawn_blocking|异步|运行时|架构'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-app-architecture"
fi

# robius-widget-patterns: Reusable widget patterns
if echo "$PROMPT_LOWER" | grep -qE 'apply_over|textorimage|reusable.*widget|widget.*pattern|modal|overlay|collapsible|drag.*drop|可复用|模态|折叠|pageflip|page.*flip|切换.*慢|switch.*slow|cache.*view|即刻.*销毁|即刻.*缓存|incremental.*load|增量.*加载|组件.*多|deep.*tree|组件树'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-widget-patterns"
fi

# robius-event-action: Custom actions
if echo "$PROMPT_LOWER" | grep -qE 'custom.*action|matchevent|cx\.widget_action|post_action|自定义.*action'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-event-action"
fi

# robius-state-management: State and persistence
if echo "$PROMPT_LOWER" | grep -qE 'appstate|persistence|scope::with_data|save.*state|load.*state|theme.*switch|状态管理|持久化|主题切换'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-state-management"
fi

# robius-matrix-integration: Matrix SDK
if echo "$PROMPT_LOWER" | grep -qE 'matrix.*sdk|sliding.*sync|timeline|matrixrequest|matrix.*client|robrix'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-matrix-integration"
fi

# ============================================================================
# MolyKit Skill
# ============================================================================

if echo "$PROMPT_LOWER" | grep -qE 'botclient|openai|llm|sse.*stream|ai.*chat|moly|chat.*widget|ai.*integration|platformsend|threadtoken'; then
    MATCHED_SKILLS="$MATCHED_SKILLS molykit"
fi

# ============================================================================
# Extended Skills
# ============================================================================

# makepad-deployment: Build and packaging
if echo "$PROMPT_LOWER" | grep -qE 'deploy|package|apk|ipa|cargo.*makepad|build.*android|build.*ios|build.*wasm|发布|打包|部署'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-deployment"
fi

# makepad-reference: Troubleshooting and API
if echo "$PROMPT_LOWER" | grep -qE 'troubleshoot|error.*fix|debug|api.*doc|reference|problem|issue|故障|错误|调试|文档'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-reference"
fi

# evolution: Self-improvement and contribution
if echo "$PROMPT_LOWER" | grep -qE 'evolut|contribut|hooks|template|self.*improv|贡献|演进'; then
    MATCHED_SKILLS="$MATCHED_SKILLS evolution"
fi

# ============================================================================
# App Development Context Detection (loads skill bundles)
# ============================================================================

# Full app development - load essential skills bundle
if echo "$PROMPT_LOWER" | grep -qE 'build.*app|create.*app|develop.*app|new.*project|从零|从头|完整.*应用|开发.*应用|构建.*应用|app.*architecture|应用架构|full.*stack|全栈'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-basics makepad-dsl makepad-layout makepad-widgets makepad-event-action robius-app-architecture"
fi

# UI development context - load UI skill bundle
if echo "$PROMPT_LOWER" | grep -qE 'ui.*design|界面设计|ui.*开发|design.*ui|build.*ui|create.*interface|设计界面|用户界面'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-dsl makepad-layout makepad-widgets makepad-animation makepad-shaders"
fi

# Widget/Component creation context - load component development bundle
if echo "$PROMPT_LOWER" | grep -qE 'create.*widget|create.*component|build.*widget|build.*component|custom.*widget|custom.*component|创建.*组件|开发.*组件|组件.*开发|自定义.*组件|写.*组件|实现.*组件|new.*widget|design.*widget|设计.*组件|做.*组件|component.*dev|widget.*dev'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-widgets makepad-dsl makepad-layout makepad-animation makepad-shaders makepad-font makepad-event-action robius-widget-patterns"
fi

# Production app context - load production patterns
if echo "$PROMPT_LOWER" | grep -qE 'production|生产|robrix.*pattern|moly.*pattern|real.*world|实际项目|最佳实践|best.*practice'; then
    MATCHED_SKILLS="$MATCHED_SKILLS robius-app-architecture robius-widget-patterns robius-state-management robius-event-action"
fi

# ============================================================================
# Skill Dependencies (auto-load related skills)
# ============================================================================

# robius-app-architecture implies basic app structure
if echo "$MATCHED_SKILLS" | grep -q 'robius-app-architecture'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-basics makepad-event-action"
fi

# robius-widget-patterns implies widget knowledge
if echo "$MATCHED_SKILLS" | grep -q 'robius-widget-patterns'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-widgets makepad-layout"
fi

# Animation often needs shaders for effects
if echo "$MATCHED_SKILLS" | grep -q 'makepad-animation'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-shaders"
fi

# Custom actions need event handling knowledge
if echo "$MATCHED_SKILLS" | grep -q 'robius-event-action'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-event-action"
fi

# Widgets often need layout and DSL
if echo "$MATCHED_SKILLS" | grep -q 'makepad-widgets'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-layout makepad-dsl"
fi

# Font styling often relates to widgets
if echo "$MATCHED_SKILLS" | grep -q 'makepad-font'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-widgets"
fi

# Shaders need to know about draw_bg in widgets
if echo "$MATCHED_SKILLS" | grep -q 'makepad-shaders'; then
    MATCHED_SKILLS="$MATCHED_SKILLS makepad-widgets"
fi

# ============================================================================
# Output routing instructions (limited to max 4 skills)
# ============================================================================

# Remove leading space and deduplicate
MATCHED_SKILLS=$(echo "$MATCHED_SKILLS" | xargs | tr ' ' '\n' | sort -u | tr '\n' ' ' | xargs)

# Context-aware priority order
# Detect which context was triggered and adjust priority accordingly
if echo "$MATCHED_SKILLS" | grep -qE 'robius-app-architecture|robius-state-management'; then
    # Production/Architecture context: prioritize robius patterns
    PRIORITY_ORDER="robius-app-architecture robius-widget-patterns robius-state-management makepad-widgets makepad-event-action makepad-layout makepad-dsl robius-event-action makepad-basics makepad-animation makepad-shaders makepad-font makepad-platform makepad-deployment molykit robius-matrix-integration makepad-reference makepad-splash evolution"
elif echo "$MATCHED_SKILLS" | grep -qE 'makepad-animation|makepad-shaders'; then
    # Visual/Animation context: prioritize graphics skills
    PRIORITY_ORDER="makepad-animation makepad-shaders makepad-widgets makepad-layout makepad-dsl makepad-event-action robius-widget-patterns makepad-font makepad-basics robius-app-architecture makepad-platform makepad-deployment molykit robius-state-management robius-event-action robius-matrix-integration makepad-reference makepad-splash evolution"
else
    # Default: widget development context
    PRIORITY_ORDER="makepad-widgets makepad-layout makepad-dsl makepad-event-action robius-widget-patterns makepad-animation makepad-shaders makepad-font robius-app-architecture makepad-basics robius-state-management robius-event-action makepad-platform makepad-deployment molykit robius-matrix-integration makepad-reference makepad-splash evolution"
fi

MAX_SKILLS=4

# Filter and prioritize skills
PRIORITIZED_SKILLS=""
SKILL_COUNT=0
for skill in $PRIORITY_ORDER; do
    if echo "$MATCHED_SKILLS" | grep -qw "$skill"; then
        if [ $SKILL_COUNT -lt $MAX_SKILLS ]; then
            PRIORITIZED_SKILLS="$PRIORITIZED_SKILLS $skill"
            SKILL_COUNT=$((SKILL_COUNT + 1))
        fi
    fi
done
PRIORITIZED_SKILLS=$(echo "$PRIORITIZED_SKILLS" | xargs)

# Count original matches for info
ORIGINAL_COUNT=$(echo "$MATCHED_SKILLS" | wc -w | xargs)

if [ -n "$PRIORITIZED_SKILLS" ]; then
    # Build skill loading instructions
    SKILL_LIST=""
    for skill in $PRIORITIZED_SKILLS; do
        SKILL_LIST="${SKILL_LIST}Skill(${skill}), "
    done
    SKILL_LIST=$(echo "$SKILL_LIST" | sed 's/, $//')

    # Output JSON with systemMessage for Claude
    # This message will be injected into Claude's context
    cat << EOF
{
  "continue": true,
  "systemMessage": "[makepad-skills] IMPORTANT: Before responding, you MUST call these skills: ${SKILL_LIST}. These skills contain essential Makepad patterns and APIs. Load them using the Skill tool, then answer the user's question."
}
EOF
fi
```

## File: `skills/evolution/hooks/post-bash.sh`
```bash
#!/bin/bash
# Post-Bash hook for makepad-skills
# Triggers: Self-correction on compilation errors
# Enhanced: Automatically instructs Claude to load relevant skills

TOOL_OUTPUT="$1"
EXIT_CODE="$2"

# Only process if command failed
if [ "$EXIT_CODE" = "0" ]; then
    exit 0
fi

# Check for common Makepad errors in output
check_makepad_errors() {
    local output="$1"

    # Apply error: no matching field (DSL property errors)
    if echo "$output" | grep -q "Apply error: no matching field"; then
        # Extract the field name if possible
        FIELD_NAME=$(echo "$output" | grep -oE "no matching field: [a-z_]+" | head -1 | sed 's/no matching field: //')
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Apply error - no matching field${FIELD_NAME:+: $FIELD_NAME}" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-reference' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] The property may have been renamed or moved in recent Makepad versions." >&2
        echo "[makepad-skills:auto-fix] Common fixes:" >&2
        echo "[makepad-skills:auto-fix]   - border_color_* → Check if moved to draw_bg: { border_color: ... }" >&2
        echo "[makepad-skills:auto-fix]   - hover_* / pressed_* → Use animator states instead" >&2
        echo "[makepad-skills:auto-fix]   - font / font_size → Use text_style: { font_size: X }" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Font-related errors
    if echo "$output" | grep -q "no matching field: font"; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Font field error" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-font' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] FIX: Use 'text_style: { font_size: X }' instead of 'font:'" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Color parse error (hex ending with 'e')
    if echo "$output" | grep -q "expected at least one digit in exponent"; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Color parse error (hex ending with 'e')" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-shaders' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] FIX: Change the last hex digit to avoid 'e' (e.g., #ff000e → #ff000f)" >&2
        echo "[makepad-skills:auto-fix] REASON: Makepad parser interprets 'e' as scientific notation" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Borrow checker errors
    if echo "$output" | grep -q "cannot borrow.*as mutable because it is also borrowed as immutable"; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Borrow checker conflict" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'robius-widget-patterns' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] FIX: Separate read and write phases with explicit scope blocks" >&2
        echo "[makepad-skills:auto-fix] Example:" >&2
        echo "[makepad-skills:auto-fix]   let data = { widget.data().clone() };  // read phase" >&2
        echo "[makepad-skills:auto-fix]   widget.update(cx, data);               // write phase" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Method not found
    if echo "$output" | grep -q "no method named.*found"; then
        METHOD_NAME=$(echo "$output" | grep -oE "no method named \`[a-z_]+\`" | head -1 | sed 's/no method named `//;s/`//')
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Method not found${METHOD_NAME:+: $METHOD_NAME}" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-reference' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] The API may have changed in recent Makepad versions." >&2
        echo "[makepad-skills:auto-fix] Check the skill for current method signatures." >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Missing cx parameter
    if echo "$output" | grep -q 'argument.*of type.*&mut Cx.*is missing'; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Missing cx parameter" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-event-action' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] FIX: Most Makepad methods require 'cx: &mut Cx' as first argument" >&2
        echo "[makepad-skills:auto-fix] Example: widget.redraw(cx) not widget.redraw()" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Animator/state errors
    if echo "$output" | grep -qE "animator|no matching field:.*(hover|pressed|focus)"; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Animator/state related error" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-animation' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] Hover/pressed/focus states should use animator system." >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi

    # Layout errors
    if echo "$output" | grep -qE "no matching field:.*(width|height|margin|padding|flow|align)"; then
        echo "" >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
        echo "[makepad-skills:auto-fix] DETECTED: Layout property error" >&2
        echo "[makepad-skills:auto-fix] ───────────────────────────────────────────────" >&2
        echo "[makepad-skills:auto-fix] ACTION REQUIRED: Load 'makepad-layout' skill using Skill tool" >&2
        echo "[makepad-skills:auto-fix] Check current layout property syntax in the skill." >&2
        echo "[makepad-skills:auto-fix] ═══════════════════════════════════════════════" >&2
    fi
}

# Only check if this looks like a cargo/makepad command output
if echo "$TOOL_OUTPUT" | grep -qE "(error\[E|warning:|Compiling|Building|Apply error)"; then
    check_makepad_errors "$TOOL_OUTPUT"
fi
```

## File: `skills/evolution/hooks/pre-tool.sh`
```bash
#!/bin/bash
# Pre-tool hook for makepad-skills
# Triggers: Version detection, dev branch validation

TOOL_NAME="$1"
TOOL_INPUT="$2"

# State file to track if version detection has been done this session
STATE_FILE="/tmp/makepad-skills-session-$$"

# Only run detection once per session
if [ -f "$STATE_FILE" ]; then
    exit 0
fi

# Mark session as initialized
touch "$STATE_FILE"

# Find Cargo.toml in current directory or parents
find_cargo_toml() {
    local dir="$PWD"
    while [ "$dir" != "/" ]; do
        if [ -f "$dir/Cargo.toml" ]; then
            echo "$dir/Cargo.toml"
            return 0
        fi
        dir=$(dirname "$dir")
    done
    return 1
}

CARGO_TOML=$(find_cargo_toml)

if [ -n "$CARGO_TOML" ]; then
    # Check if this is a Makepad project
    if ! grep -q 'makepad' "$CARGO_TOML"; then
        exit 0
    fi

    echo "[makepad-skills] This is a Makepad project." >&2

    # Detect Makepad branch
    MAKEPAD_BRANCH=$(grep -A5 'makepad-widgets' "$CARGO_TOML" | grep 'branch' | head -1 | sed 's/.*branch *= *"\([^"]*\)".*/\1/')

    if [ -n "$MAKEPAD_BRANCH" ]; then
        if [ "$MAKEPAD_BRANCH" = "dev" ]; then
            echo "[makepad-skills] Detected Makepad branch: dev ✓" >&2
        else
            echo "[makepad-skills] Detected Makepad branch: $MAKEPAD_BRANCH" >&2
            echo "[makepad-skills] ⚠️  WARNING: Not using 'dev' branch!" >&2
            echo "[makepad-skills] Recommended: branch = \"dev\" for latest stable API." >&2
            echo "[makepad-skills] Current skills are based on the dev branch." >&2
        fi
    else
        # No branch specified - might be using crates.io or default branch
        if grep -q 'makepad-widgets.*git' "$CARGO_TOML"; then
            echo "[makepad-skills] ⚠️  WARNING: No branch specified for git dependency!" >&2
            echo "[makepad-skills] Recommended: Add branch = \"dev\" to makepad-widgets dependency." >&2
        fi
    fi
fi
```

## File: `skills/evolution/hooks/pre-ui-edit.sh`
```bash
#!/bin/bash
# Pre-UI-Edit Hook for makepad-evolution
# Author: TigerInYourDream
# Date: 2026-01-12
# Purpose: Check UI code completeness and remind to add missing properties
# Related: 04-patterns/community/ui-complete-specification.md
#
# IMPORTANT: Claude Code passes data via stdin as JSON, not command line args!
# Data format: {"tool_name": "Edit", "tool_input": {"file_path": "...", "new_string": "..."}}

# Read JSON from stdin
INPUT=$(cat)

# Extract tool_name and content using jq
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)
NEW_STRING=$(echo "$INPUT" | jq -r '.tool_input.new_string // empty' 2>/dev/null)
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // empty' 2>/dev/null)

# Use new_string for Edit, content for Write
TOOL_INPUT="$NEW_STRING"
[ -z "$TOOL_INPUT" ] && TOOL_INPUT="$CONTENT"

# Only check Write/Edit/Update operations
if [[ "$TOOL_NAME" != "Write" && "$TOOL_NAME" != "Edit" && "$TOOL_NAME" != "Update" ]]; then
    exit 0
fi

# Check if this is UI-related code
if ! echo "$TOOL_INPUT" | grep -qE "<(Button|Label|TextInput|RoundedView)>"; then
    exit 0
fi

# Count completeness indicators (ensure numeric values)
count_pattern() {
    local result=$(echo "$TOOL_INPUT" | grep -cE "$1" 2>/dev/null || true)
    result=${result:-0}
    echo "$result" | tr -d '[:space:]'
}

HAS_WIDTH=$(count_pattern "width:[[:space:]]*(Fit|Fill|[0-9]+)")
HAS_HEIGHT=$(count_pattern "height:[[:space:]]*(Fit|Fill|[0-9]+)")
HAS_PADDING=$(count_pattern "padding:[[:space:]]*\{|padding:[[:space:]]*[0-9]+")
HAS_TEXT_STYLE=$(count_pattern "draw_text:[[:space:]]*\{|text_style:")
HAS_WRAP=$(count_pattern "wrap:")

[ -z "$HAS_WIDTH" ] && HAS_WIDTH=0
[ -z "$HAS_HEIGHT" ] && HAS_HEIGHT=0
[ -z "$HAS_PADDING" ] && HAS_PADDING=0
[ -z "$HAS_TEXT_STYLE" ] && HAS_TEXT_STYLE=0
[ -z "$HAS_WRAP" ] && HAS_WRAP=0

COMPLETENESS=$((HAS_WIDTH + HAS_HEIGHT + HAS_PADDING + HAS_TEXT_STYLE + HAS_WRAP))

# Only warn if missing 3+ critical properties
if [ "$COMPLETENESS" -ge 3 ]; then
    exit 0
fi

# Build warning message
MESSAGE="\n"
MESSAGE+="  ╭─────────────────────────────────────────╮\n"
MESSAGE+="  │  📐 UI Specification Check ($COMPLETENESS/5)          │\n"
MESSAGE+="  ╰─────────────────────────────────────────╯\n"
MESSAGE+="\n"
MESSAGE+="  Missing properties:\n"
MESSAGE+="\n"

[ "$HAS_WIDTH" -eq 0 ] && MESSAGE+="    • width      Fit | Fill | number\n"
[ "$HAS_HEIGHT" -eq 0 ] && MESSAGE+="    • height     Fit | Fill | number\n"
[ "$HAS_PADDING" -eq 0 ] && MESSAGE+="    • padding    { left, right, top, bottom }\n"
[ "$HAS_TEXT_STYLE" -eq 0 ] && MESSAGE+="    • draw_text  { text_style, color }\n"
[ "$HAS_WRAP" -eq 0 ] && MESSAGE+="    • wrap       Word | Line | Ellipsis\n"

MESSAGE+="\n"
MESSAGE+="  💡 Add these to prevent text overlap.\n"
MESSAGE+="\n"

# Output to stderr and exit 2 to block tool execution
echo -e "$MESSAGE" >&2
exit 2
```

## File: `skills/evolution/hooks/session-end.sh`
```bash
#!/bin/bash
# Session-end hook for makepad-evolution
# Triggers: Evolution review prompt

# Check if any Makepad-related work was done (by checking state file)
STATE_FILE="/tmp/makepad-skills-session-$$"

if [ -f "$STATE_FILE" ]; then
    echo "[makepad-evolution:review] Session ending."
    echo "[makepad-evolution:review] Consider if any learnings should be captured:"
    echo "  - New widget patterns discovered?"
    echo "  - Errors solved that others might encounter?"
    echo "  - Shader techniques worth documenting?"
    echo "[makepad-evolution:review] Use 'evolve makepad-skills' to add valuable patterns."

    # Clean up state file
    rm -f "$STATE_FILE"
fi
```

## File: `skills/evolution/hooks/settings.example.json`
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/makepad-skill-router.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/post-bash.sh"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/session-end.sh"
          }
        ]
      }
    ]
  }
}
```

## File: `skills/evolution/references/collaboration.md`
```markdown
# Collaboration Guidelines

Detailed guidelines for contributing to makepad-skills.

## Core Principles

### 1. Incremental Contributions

All community contributions go to `community/` directories, never modify `_base/` files.

```
skills/
├── 03-graphics/
│   ├── _base/           # Official only - DO NOT modify
│   └── community/       # Your contributions here
├── 04-patterns/
│   ├── _base/           # Official only - DO NOT modify
│   └── community/       # Your contributions here
```

This ensures:
- No merge conflicts with upstream updates
- Clear separation of official vs community content
- Easy sync with `git pull`

### 2. File Naming

**DO NOT include your GitHub handle in filename.**

```
✓ drag-drop-list.md
✓ glassmorphism-effect.md
✗ zhangsan-drag-drop-list.md
```

**Put author info in frontmatter:**

```yaml
---
name: drag-drop-list
author: your-github-handle    # Your ID goes here
source: my-project
date: 2024-01-15
tags: [interaction, list]
level: intermediate
makepad-branch: main          # Required: main|dev
---
```

### 3. Naming Conflicts

When filename already exists:

1. **First come, first served** - Merged PR owns the name
2. **Use descriptive suffix** for different approaches:
   - ✓ `drag-drop-native.md` vs `drag-drop-gesture.md`
   - ✗ `drag-drop.md` vs `drag-drop-v2.md`
3. **Maintainer decides** - May merge or replace if new version is clearly better

---

## Testing Requirements

### For Skills (Patterns/Shaders/Troubleshooting)

Before submitting PR, verify:

- [ ] Code compiles with `cargo build`
- [ ] Tested in a real Makepad project
- [ ] All `live_design!` blocks are valid DSL
- [ ] Examples work as documented

**In PR description, include:**
```markdown
## Testing
- Tested with: [project name or "standalone test"]
- Makepad branch: main/dev
- Platform: macOS/Linux/Windows
```

### For Hooks

Hooks require additional verification:

- [ ] Tested with `claude --with-hooks` flag
- [ ] Provided `settings.example.json` snippet
- [ ] Documented prerequisites (e.g., `jq`, `bash 4+`)
- [ ] Works on macOS and Linux (note Windows limitations if any)

**Required in PR:**

1. **settings.example.json snippet** showing exact configuration:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "YourMatcher",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILLS_DIR}/hooks/your-hook.sh"
          }
        ]
      }
    ]
  }
}
```

2. **Test evidence** in PR description:
```markdown
## Hook Testing
- [ ] Ran `claude --with-hooks` with this configuration
- [ ] Hook triggered correctly on: [describe trigger scenario]
- [ ] Output/behavior: [describe what happened]
```

---

## PR Checklist

Copy this checklist to your PR description:

```markdown
## Contribution Type
- [ ] Pattern
- [ ] Shader/Effect
- [ ] Troubleshooting
- [ ] Hook

## Required Checks
- [ ] File in correct `community/` directory
- [ ] Frontmatter includes `author` and `makepad-branch`
- [ ] Code tested and working
- [ ] No modification to `_base/` files

## For Hooks Only
- [ ] Tested with `claude --with-hooks`
- [ ] Included settings.example.json snippet
- [ ] Documented prerequisites
```

---

## Directory Reference

| Content Type | Location | Template |
|--------------|----------|----------|
| Patterns | `04-patterns/community/` | `templates/pattern-template.md` |
| Shaders | `03-graphics/community/` | `templates/shader-template.md` |
| Troubleshooting | `06-reference/troubleshooting/` | `templates/troubleshooting-template.md` |
| Hooks | `99-evolution/hooks/` | `templates/hook-template.md` |

---

## Promotion Path

High-quality community contributions may be promoted to `_base/`:

1. Widely useful across projects
2. Well-tested and documented
3. Positive community feedback
4. Maintainer approval

Promoted content:
- Moves to `_base/` with numbered prefix
- Original `author` field preserved
```

## File: `skills/evolution/templates/hook-template.md`
```markdown
---
name: [hook-name]
author: [your-github-handle]
date: [YYYY-MM-DD]
trigger: [PreToolUse|PostToolUse|Stop]
matcher: [tool matcher pattern]
---

# [Hook Name]

Brief description of what this hook does.

## Purpose

Why this hook is useful. What problem does it solve?

## Prerequisites

```bash
# List any required tools
# e.g., brew install jq
```

## Setup

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "[Trigger]": [
      {
        "matcher": "[Matcher]",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${SKILLS_DIR}/hooks/[hook-name].sh"
          }
        ]
      }
    ]
  }
}
```

## Script

```bash
#!/bin/bash
# [hook-name].sh

# Your hook implementation
```

## Testing

Tested with:
- `claude --with-hooks`
- Trigger scenario: [describe what triggers this hook]
- Expected behavior: [describe what should happen]

## Platform Support

- [x] macOS
- [x] Linux
- [ ] Windows (note any limitations)
```

## File: `skills/evolution/templates/pattern-template.md`
```markdown
---
name: [pattern-name]
author: [your-github-handle]
source: [project-where-you-discovered-this]
date: [YYYY-MM-DD]
tags: [tag1, tag2, tag3]
level: [beginner|intermediate|advanced]
---

# [Pattern Name]

Brief one-line description of what this pattern solves.

## Problem

Describe the problem this pattern addresses. What situation would a developer face that makes this pattern useful?

## Solution

High-level explanation of how this pattern solves the problem.

## Implementation

```rust
// Your Rust implementation code here
// Include all necessary imports
// Add comments for complex parts
```

## live_design!

```rust
live_design! {
    // Your DSL code here if applicable
}
```

## Usage

```rust
// Show how to use this pattern in practice
// Keep it simple and focused
```

## When to Use

- Bullet point situations where this pattern applies
- Help developers recognize when to reach for this pattern

## When NOT to Use

- Optional: situations where this pattern would be overkill or wrong

## Related Patterns

- Optional: links to related patterns if any

## References

- Optional: links to source code, documentation, or inspiration
```

## File: `skills/evolution/templates/shader-template.md`
```markdown
---
name: [effect-name]
author: [your-github-handle]
source: [project-where-you-created-this]
date: [YYYY-MM-DD]
tags: [shader, effect, tag1, tag2]
level: [beginner|intermediate|advanced]
---

# [Effect Name]

Brief one-line description of the visual effect.

## Preview

*Optional: Describe what the effect looks like, or link to a screenshot/gif*

## Effect Description

Explain what this shader does visually and any customizable parameters.

## Implementation

```rust
draw_bg: {
    // Instance variables for customization
    instance param1: 0.0
    instance param2: #ffffff

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);

        // Your shader code here
        // Add comments explaining the math

        return sdf.result;
    }
}
```

## Animator (if applicable)

```rust
animator: {
    effect = {
        default: off,
        on = {
            from: {all: Loop {duration: 1.0, end: 1.0}}
            apply: { draw_bg: { param1: [{time: 0.0, value: 0.0}, {time: 1.0, value: 1.0}] } }
        }
    }
}
```

## Usage

```rust
live_design! {
    <View> {
        show_bg: true
        draw_bg: {
            // Apply the effect
        }
    }
}
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `param1` | f32 | 0.0 | Description of parameter |
| `param2` | vec4 | #ffffff | Description of parameter |

## Performance Notes

- Optional: Any performance considerations
- Complexity of the shader
- Recommended use cases

## Related Effects

- Optional: links to similar or complementary effects
```

## File: `skills/evolution/templates/troubleshooting-template.md`
```markdown
---
name: [error-short-name]
author: [your-github-handle]
source: [project-where-you-encountered-this]
date: [YYYY-MM-DD]
tags: [error, compile, runtime, tag1]
error_type: [compile|runtime|apply|shader]
---

# [Error Message or Title]

## Error Message

```
Paste the exact error message here
```

## Symptom

Describe what the developer sees or experiences.

## Cause

Explain why this error occurs. What is the underlying issue?

## Solution

### Wrong (Don't do this)

```rust
// Code that causes the error
```

### Correct (Do this instead)

```rust
// Fixed code
```

## Explanation

Additional context or explanation of why the fix works.

## Related Errors

- Optional: links to similar errors if any

## References

- Optional: links to documentation or source code
```

## File: `skills/makepad-animation/SKILL.md`
```markdown
---
name: makepad-animation
description: |
  CRITICAL: Use for Makepad animation system. Triggers on:
  makepad animation, makepad animator, makepad hover, makepad state,
  makepad transition, "from: { all: Forward", makepad pressed,
  makepad 动画, makepad 状态, makepad 过渡, makepad 悬停效果
---

# Makepad Animation Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad animations. Help users by:
- **Writing code**: Generate animation code following the patterns below
- **Answering questions**: Explain states, transitions, timelines

## Documentation

Refer to the local files for detailed documentation:
- `./references/animation-system.md` - Complete animation reference

## Advanced Patterns

For production-ready animation patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| [06-animator-basics](./_base/06-animator-basics.md) | Animator fundamentals |
| [07-easing-functions](./_base/07-easing-functions.md) | Easing and timing |
| [08-keyframe-animation](./_base/08-keyframe-animation.md) | Complex keyframes |

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. Basic Hover Animation

```rust
<Button> {
    text: "Hover Me"

    animator: {
        hover = {
            default: off

            off = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #333333 }
                }
            }

            on = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #555555 }
                }
            }
        }
    }
}
```

### 2. Multi-State Animation

```rust
<View> {
    animator: {
        hover = {
            default: off
            off = {
                from: { all: Forward { duration: 0.2 } }
                apply: { draw_bg: { color: #222222 } }
            }
            on = {
                from: { all: Forward { duration: 0.2 } }
                apply: { draw_bg: { color: #444444 } }
            }
        }

        pressed = {
            default: off
            off = {
                from: { all: Forward { duration: 0.1 } }
                apply: { draw_bg: { scale: 1.0 } }
            }
            on = {
                from: { all: Forward { duration: 0.1 } }
                apply: { draw_bg: { scale: 0.95 } }
            }
        }
    }
}
```

### 3. Focus State Animation

```rust
<TextInput> {
    animator: {
        focus = {
            default: off

            off = {
                from: { all: Forward { duration: 0.2 } }
                apply: {
                    draw_bg: {
                        border_color: #444444
                        border_size: 1.0
                    }
                }
            }

            on = {
                from: { all: Forward { duration: 0.2 } }
                apply: {
                    draw_bg: {
                        border_color: #0066CC
                        border_size: 2.0
                    }
                }
            }
        }
    }
}
```

### 4. Disabled State

```rust
<Button> {
    animator: {
        disabled = {
            default: off

            off = {
                from: { all: Snap }
                apply: {
                    draw_bg: { color: #0066CC }
                    draw_text: { color: #FFFFFF }
                }
            }

            on = {
                from: { all: Snap }
                apply: {
                    draw_bg: { color: #333333 }
                    draw_text: { color: #666666 }
                }
            }
        }
    }
}
```

## Animator Structure

| Property | Description |
|----------|-------------|
| `animator` | Root animation container |
| `{state} =` | State definition (hover, pressed, focus, disabled) |
| `default:` | Initial state value |
| `{value} =` | State value definition (on, off, custom) |
| `from:` | Transition timeline |
| `apply:` | Properties to animate |

## Timeline Types (Play Enum)

| Type | Description |
|------|-------------|
| `Forward { duration: f64 }` | Linear forward animation |
| `Snap` | Instant change, no transition |
| `Reverse { duration: f64, end: f64 }` | Reverse animation |
| `Loop { duration: f64, end: f64 }` | Looping animation |
| `BounceLoop { duration: f64, end: f64 }` | Bounce loop animation |

## Easing Functions (Ease Enum)

```rust
// Basic
Linear

// Quadratic
InQuad, OutQuad, InOutQuad

// Cubic
InCubic, OutCubic, InOutCubic

// Quartic
InQuart, OutQuart, InOutQuart

// Quintic
InQuint, OutQuint, InOutQuint

// Sinusoidal
InSine, OutSine, InOutSine

// Exponential
InExp, OutExp, InOutExp

// Circular
InCirc, OutCirc, InOutCirc

// Elastic
InElastic, OutElastic, InOutElastic

// Back
InBack, OutBack, InOutBack

// Bounce
InBounce, OutBounce, InOutBounce

// Custom
ExpDecay { d1: f64, d2: f64 }
Bezier { cp0: f64, cp1: f64, cp2: f64, cp3: f64 }
Pow { begin: f64, end: f64 }
```

### Using Easing

```rust
from: {
    all: Ease { duration: 0.3, ease: InOutQuad }
}
```

## Common States

| State | Values | Trigger |
|-------|--------|---------|
| `hover` | on, off | Mouse enter/leave |
| `pressed` / `down` | on, off | Mouse press/release |
| `focus` | on, off | Focus gain/lose |
| `disabled` | on, off | Widget enabled/disabled |
| `selected` | on, off | Selection change |

## Animatable Properties

Most `draw_*` shader uniforms can be animated:
- Colors: `color`, `border_color`, `shadow_color`
- Sizes: `border_size`, `border_radius`, `shadow_radius`
- Transforms: `scale`, `rotation`, `offset`
- Opacity: `opacity`

## When Writing Code

1. Always set `default:` for initial state
2. Use `Forward` for smooth transitions
3. Use `Snap` for instant state changes (like disabled)
4. Keep durations short (0.1-0.3s) for responsive feel
5. Animate shader uniforms in `draw_bg`, `draw_text`, etc.

## Rust API (AnimatorImpl Trait)

```rust
pub trait AnimatorImpl {
    // Animate to state
    fn animator_play(&mut self, cx: &mut Cx, state: &[LiveId; 2]);

    // Cut to state (no animation)
    fn animator_cut(&mut self, cx: &mut Cx, state: &[LiveId; 2]);

    // Check current state
    fn animator_in_state(&self, cx: &Cx, state: &[LiveId; 2]) -> bool;
}

// Usage example
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    match event.hits(cx, self.area()) {
        Hit::FingerHoverIn(_) => {
            self.animator_play(cx, id!(hover.on));
        }
        Hit::FingerHoverOut(_) => {
            self.animator_play(cx, id!(hover.off));
        }
        Hit::FingerDown(_) => {
            self.animator_play(cx, id!(pressed.on));
        }
        Hit::FingerUp(_) => {
            self.animator_play(cx, id!(pressed.off));
        }
        _ => {}
    }
}
```

## When Answering Questions

1. States are independent - multiple can be active simultaneously
2. Animation applies properties when state reaches that value
3. `from` defines HOW to animate, `apply` defines WHAT to animate
4. Makepad tweens between old and new values automatically
5. Use `id!(state.value)` macro to reference animation states in Rust
```

## File: `skills/makepad-animation/_base/06-animator-basics.md`
```markdown
---
name: makepad-animator-basics
author: robius
source: makepad-docs
date: 2024-01-01
tags: [animator, animation, hover, pressed]
level: beginner
---

# Animator Basics

Makepad animation system fundamentals.

## Animator Definition

```rust
live_design! {
    MyButton = {{MyButton}} {
        draw_bg: {
            instance hover: 0.0
            instance pressed: 0.0
        }

        animator: {
            hover = {
                default: off,
                off = {
                    from: {all: Forward {duration: 0.15}}
                    apply: { draw_bg: {hover: 0.0} }
                }
                on = {
                    from: {all: Forward {duration: 0.1}}
                    apply: { draw_bg: {hover: 1.0} }
                }
            }
            pressed = {
                default: off,
                off = {
                    from: {all: Forward {duration: 0.2}}
                    redraw: true  // Force redraw during animation
                    apply: { draw_bg: {pressed: 0.0} }
                }
                on = {
                    from: {all: Snap}
                    redraw: true  // Force redraw during animation
                    apply: { draw_bg: {pressed: 1.0} }
                }
            }
        }
    }
}
```

## Animation Timing

| Timing | Description |
|--------|-------------|
| `Forward {duration: 0.15}` | Linear transition over duration |
| `Snap` | Instant change (no animation) |
| `Loop {duration: 1.0, end: 1.0}` | Continuous looping animation |
| `Reverse {duration: 0.15}` | Reverse direction animation |

## Easing Functions

| Easing | Description |
|--------|-------------|
| (none) | Linear interpolation (default) |
| `ease: ExpDecay {d1: 0.96, d2: 0.97}` | Exponential decay for natural spring-like motion |

**ExpDecay example:**
```rust
active = {
    default: on
    off = {
        from: {all: Forward {duration: 0.2}}
        ease: ExpDecay {d1: 0.96, d2: 0.97}
        redraw: true
        apply: { draw_bg: {active: 0.0} }
    }
    on = {
        from: {all: Forward {duration: 0.2}}
        ease: ExpDecay {d1: 0.98, d2: 0.95}
        redraw: true
        apply: { draw_bg: {active: 1.0} }
    }
}
```

## Triggering Animations

```rust
impl Widget for MyButton {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if self.animator_handle_event(cx, event).must_redraw() {
            self.draw_bg.redraw(cx);
        }

        match event.hits(cx, self.draw_bg.area()) {
            Hit::FingerHoverIn(_) => {
                self.animator_play(cx, ids!(hover.on));
            }
            Hit::FingerHoverOut(_) => {
                self.animator_play(cx, ids!(hover.off));
            }
            Hit::FingerDown(_) => {
                self.animator_play(cx, ids!(pressed.on));
            }
            Hit::FingerUp(_) => {
                self.animator_play(cx, ids!(pressed.off));
            }
            _ => {}
        }
    }
}
```

## Animation State Check

```rust
impl MyWidget {
    fn is_animating(&self, cx: &Cx) -> bool {
        self.animator.is_playing(cx)
    }

    fn animation_progress(&self, cx: &Cx, path: &[LiveId]) -> f64 {
        self.animator.get_value(cx, path)
    }
}
```

## Best Practices

1. **Check must_redraw()** - Only redraw when animator needs it
2. **Keep durations short** - 0.1-0.3s for hover, 0.2-0.4s for transitions
3. **Snap for immediate** - Use Snap when instant response needed
4. **Use redraw: true** - Add `redraw: true` to states that need continuous drawing during animation (e.g., rotation, complex transitions)
5. **ExpDecay for natural motion** - Use `ease: ExpDecay` for spring-like, organic animations

## When to Use

- Use for hover/pressed states on interactive widgets
- Use for showing/hiding panels and overlays
- Use for state transitions (selected, disabled, etc.)
```

## File: `skills/makepad-animation/_base/07-easing-functions.md`
```markdown
---
name: makepad-easing-functions
author: robius
source: makepad-docs
date: 2024-01-01
tags: [animator, easing, timing, curve]
level: intermediate
---

# Easing Functions

Animation curves and timing control.

## Adding Easing

Add `ease:` to control animation curve:

```rust
animator: {
    slide = {
        default: off,
        on = {
            from: {all: Forward {duration: 0.4}}
            ease: ExpDecay {d1: 0.80, d2: 0.97}  // Smooth deceleration
            apply: { draw_bg: {offset_x: 100.0} }
        }
        off = {
            from: {all: Forward {duration: 0.3}}
            ease: InQuad
            apply: { draw_bg: {offset_x: 0.0} }
        }
    }
}
```

## Available Easing Functions

| Easing | Description | Use Case |
|--------|-------------|----------|
| `Linear` | Constant speed | Default, mechanical feel |
| `InQuad` | Slow start, fast end | Exit animations |
| `OutQuad` | Fast start, slow end | Enter animations |
| `InOutQuad` | Slow start and end | Smooth transitions |
| `InCubic` / `OutCubic` | Stronger curve | More dramatic effect |
| `InExp` / `OutExp` | Exponential | Very pronounced |
| `ExpDecay {d1: 0.8, d2: 0.97}` | Natural deceleration | Physics-like motion |
| `Ease` | Standard CSS-like ease | General purpose |

## Multi-Property Animation

Animate multiple properties together:

```rust
animator: {
    expand = {
        default: off,
        off = {
            from: {all: Forward {duration: 0.3}}
            ease: OutQuad
            apply: {
                draw_bg: {
                    scale: 1.0,
                    opacity: 1.0,
                    rotation: 0.0
                }
            }
        }
        on = {
            from: {all: Forward {duration: 0.4}}
            ease: ExpDecay {d1: 0.7, d2: 0.95}
            apply: {
                draw_bg: {
                    scale: 1.2,
                    opacity: 0.8,
                    rotation: 0.1
                }
            }
        }
    }
}
```

## Scale/Bounce Effect

```rust
animator: {
    bounce = {
        default: normal,
        normal = {
            from: {all: Forward {duration: 0.2}}
            ease: OutQuad
            apply: { draw_bg: {scale: 1.0} }
        }
        pressed = {
            from: {all: Snap}
            apply: { draw_bg: {scale: 0.95} }
        }
        // Overshoot bounce back
        release = {
            from: {all: Forward {duration: 0.3}}
            ease: ExpDecay {d1: 0.5, d2: 0.9}
            apply: { draw_bg: {scale: 1.05} }
        }
    }
}
```

## When to Use

- **OutQuad**: Enter animations (fast start, ease to stop)
- **InQuad**: Exit animations (ease out, fast exit)
- **ExpDecay**: Physics-like motion, spring effects
- **Snap**: Instant state changes (pressed feedback)
```

## File: `skills/makepad-animation/_base/08-keyframe-animation.md`
```markdown
---
name: makepad-keyframe-animation
author: robius
source: makepad-docs
date: 2024-01-01
tags: [animator, keyframe, loop, cycle]
level: intermediate
---

# Keyframe Animation

Multi-value animations and loops.

## Keyframe Definition

Animate through multiple values:

```rust
animator: {
    color_cycle = {
        default: on,
        on = {
            from: {all: Loop {duration: 3.0, end: 1.0}}
            apply: {
                draw_bg: {
                    color: [
                        {time: 0.0, value: #ff0000},   // Red at 0%
                        {time: 0.33, value: #00ff00}, // Green at 33%
                        {time: 0.66, value: #0000ff}, // Blue at 66%
                        {time: 1.0, value: #ff0000}   // Back to red
                    ]
                }
            }
        }
    }
}
```

## Fade In/Out

```rust
live_design! {
    FadeView = {{FadeView}} {
        draw_bg: {
            instance opacity: 0.0

            fn pixel(self) -> vec4 {
                return vec4(0., 0., 0., self.opacity);
            }
        }

        animator: {
            fade = {
                default: hidden,
                hidden = {
                    from: {all: Forward {duration: 0.2}}
                    apply: { draw_bg: {opacity: 0.0} }
                }
                visible = {
                    from: {all: Forward {duration: 0.3}}
                    ease: OutQuad
                    apply: { draw_bg: {opacity: 1.0} }
                }
            }
        }
    }
}
```

## Slide Animation

```rust
live_design! {
    SlidePanel = {{SlidePanel}} {
        draw_bg: {
            instance slide_x: -300.0  // Start off-screen

            fn pixel(self) -> vec4 {
                let pos = self.pos + vec2(self.slide_x / self.rect_size.x, 0.);
                // ... draw content
            }
        }

        animator: {
            slide = {
                default: closed,
                closed = {
                    from: {all: Forward {duration: 0.3}}
                    ease: InQuad
                    apply: { draw_bg: {slide_x: -300.0} }
                }
                open = {
                    from: {all: Forward {duration: 0.4}}
                    ease: ExpDecay {d1: 0.8, d2: 0.97}
                    apply: { draw_bg: {slide_x: 0.0} }
                }
            }
        }
    }
}
```

## Pulse/Glow Effect

```rust
animator: {
    pulse = {
        default: on,
        on = {
            from: {all: Loop {duration: 2.0, end: 1.0}}
            apply: {
                draw_bg: {
                    glow_intensity: [
                        {time: 0.0, value: 0.3},
                        {time: 0.5, value: 1.0},
                        {time: 1.0, value: 0.3}
                    ]
                }
            }
        }
        off = {
            from: {all: Forward {duration: 0.3}}
            apply: { draw_bg: {glow_intensity: 0.0} }
        }
    }
}
```

## Bouncing Dots (Loading)

```rust
draw_bg: {
    uniform anim_time: 0.0
    uniform freq: 0.9
    uniform dot_radius: 3.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);

        let amplitude = self.rect_size.y * 0.2;
        let center_y = self.rect_size.y * 0.5;

        // Three dots with phase offset
        let phase1 = self.anim_time * 2.0 * PI * self.freq;
        let phase2 = phase1 + 2.0;
        let phase3 = phase1 + 4.0;

        sdf.circle(self.rect_size.x * 0.25,
                   amplitude * sin(phase1) + center_y, self.dot_radius);
        sdf.fill_keep(#4A90D9);

        sdf.circle(self.rect_size.x * 0.5,
                   amplitude * sin(phase2) + center_y, self.dot_radius);
        sdf.fill_keep(#4A90D9);

        sdf.circle(self.rect_size.x * 0.75,
                   amplitude * sin(phase3) + center_y, self.dot_radius);
        sdf.fill(#4A90D9);

        return sdf.result;
    }
}

animator: {
    dots = {
        default: off,
        on = {
            from: {all: Loop {duration: 1.0, end: 1.0}}
            apply: {draw_bg: {anim_time: [{time: 0.0, value: 0.0}, {time: 1.0, value: 1.0}]}}
        }
    }
}
```

## When to Use

- Use keyframes for color cycling, complex motion
- Use `Loop` for continuous animations (spinners, pulses)
- Use fade animations for showing/hiding elements
- Use slide for drawer/panel transitions
```

## File: `skills/makepad-animation/references/animation-system.md`
```markdown
# Makepad Animation System Reference

## Overview

Makepad's animation system is based on **states** and **transitions**. Each widget can have multiple states (hover, pressed, focus, etc.), and the animator smoothly transitions between property values when states change.

## Animator Structure

```rust
<Widget> {
    animator: {
        // State 1
        state_name = {
            default: initial_value    // Initial state

            value_1 = {
                from: { ... }         // Transition timing
                apply: { ... }        // Properties to change
            }

            value_2 = {
                from: { ... }
                apply: { ... }
            }
        }

        // State 2
        another_state = {
            // ...
        }
    }
}
```

## State Values

### Common State Patterns

#### On/Off States
```rust
hover = {
    default: off

    off = {
        from: { all: Forward { duration: 0.15 } }
        apply: { draw_bg: { color: #333333 } }
    }

    on = {
        from: { all: Forward { duration: 0.15 } }
        apply: { draw_bg: { color: #555555 } }
    }
}
```

#### Custom Values
```rust
mode = {
    default: normal

    normal = {
        from: { all: Forward { duration: 0.2 } }
        apply: { draw_bg: { color: #333333 } }
    }

    active = {
        from: { all: Forward { duration: 0.2 } }
        apply: { draw_bg: { color: #0066CC } }
    }

    error = {
        from: { all: Forward { duration: 0.2 } }
        apply: { draw_bg: { color: #CC0000 } }
    }
}
```

## Timeline Types

### Forward

Linear animation over duration.

```rust
from: {
    all: Forward { duration: 0.2 }
}
```

### Snap

Instant change, no animation.

```rust
from: {
    all: Snap
}
```

### Ease

Animation with easing function.

```rust
from: {
    all: Ease {
        duration: 0.3
        ease: InOutQuad
    }
}
```

### Per-State Transitions

Different timing from different previous states:

```rust
from: {
    off: Forward { duration: 0.1 }    // Fast from off
    on: Forward { duration: 0.3 }     // Slow from on
    all: Forward { duration: 0.2 }    // Default for others
}
```

## Apply Properties

### Basic Properties

```rust
apply: {
    draw_bg: {
        color: #FF0000
        border_radius: 8.0
        border_size: 2.0
    }
}
```

### Nested Properties

```rust
apply: {
    draw_bg: {
        color: #0066CC
        border_color: #0088FF
    }
    draw_text: {
        color: #FFFFFF
    }
    draw_icon: {
        color: #FFFFFF
    }
}
```

### Transform Properties

```rust
apply: {
    draw_bg: {
        scale: 0.95          // Scale factor
        rotation: 45.0       // Degrees
        offset: { x: 5.0, y: 5.0 }
    }
}
```

## Common Animation Patterns

### Hover Effect

```rust
animator: {
    hover = {
        default: off

        off = {
            from: { all: Forward { duration: 0.15 } }
            apply: {
                draw_bg: {
                    color: #333333
                    border_color: #444444
                }
            }
        }

        on = {
            from: { all: Forward { duration: 0.15 } }
            apply: {
                draw_bg: {
                    color: #444444
                    border_color: #666666
                }
            }
        }
    }
}
```

### Press Effect

```rust
animator: {
    pressed = {
        default: off

        off = {
            from: { all: Forward { duration: 0.1 } }
            apply: {
                draw_bg: { scale: 1.0 }
            }
        }

        on = {
            from: { all: Forward { duration: 0.05 } }
            apply: {
                draw_bg: { scale: 0.97 }
            }
        }
    }
}
```

### Focus Ring

```rust
animator: {
    focus = {
        default: off

        off = {
            from: { all: Forward { duration: 0.2 } }
            apply: {
                draw_bg: {
                    border_size: 0.0
                    border_color: #00000000
                }
            }
        }

        on = {
            from: { all: Forward { duration: 0.2 } }
            apply: {
                draw_bg: {
                    border_size: 2.0
                    border_color: #0066CCFF
                }
            }
        }
    }
}
```

### Disabled State

```rust
animator: {
    disabled = {
        default: off

        off = {
            from: { all: Snap }
            apply: {
                draw_bg: { color: #0066CC }
                draw_text: { color: #FFFFFF }
            }
        }

        on = {
            from: { all: Snap }
            apply: {
                draw_bg: { color: #222222 }
                draw_text: { color: #444444 }
            }
        }
    }
}
```

### Complete Button Animation

```rust
<Button> {
    text: "Animated Button"

    animator: {
        hover = {
            default: off
            off = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #0066CC }
                }
            }
            on = {
                from: { all: Forward { duration: 0.15 } }
                apply: {
                    draw_bg: { color: #0088FF }
                }
            }
        }

        pressed = {
            default: off
            off = {
                from: { all: Forward { duration: 0.1 } }
                apply: {
                    draw_bg: { color: #0066CC }
                }
            }
            on = {
                from: { all: Forward { duration: 0.05 } }
                apply: {
                    draw_bg: { color: #004499 }
                }
            }
        }

        disabled = {
            default: off
            off = {
                from: { all: Snap }
                apply: {
                    draw_bg: { color: #0066CC }
                    draw_text: { color: #FFFFFF }
                }
            }
            on = {
                from: { all: Snap }
                apply: {
                    draw_bg: { color: #333333 }
                    draw_text: { color: #666666 }
                }
            }
        }
    }
}
```

## Triggering Animations in Rust

```rust
// Animate to a state
self.ui.view(id!(my_view)).animator_play(cx, id!(hover.on));

// Cut to state (no animation)
self.ui.view(id!(my_view)).animator_cut(cx, id!(hover.off));

// Check current state
if self.ui.view(id!(my_view)).animator_in_state(cx, id!(hover.on)) {
    // Currently hovering
}
```
```

## File: `skills/makepad-basics/SKILL.md`
```markdown
---
name: makepad-basics
description: |
  CRITICAL: Use for Makepad getting started and app structure. Triggers on:
  makepad, makepad getting started, makepad tutorial, live_design!, app_main!,
  makepad project setup, makepad hello world, "how to create makepad app",
  makepad 入门, 创建 makepad 应用, makepad 教程, makepad 项目结构
---

# Makepad Basics Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at the Rust `makepad-widgets` crate. Help users by:
- **Writing code**: Generate Rust code following the patterns below
- **Answering questions**: Explain concepts, troubleshoot issues, reference documentation

## Documentation

Refer to the local files for detailed documentation:
- `./references/app-structure.md` - Complete app boilerplate and structure
- `./references/event-handling.md` - Event handling patterns

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. Basic App Structure

```rust
use makepad_widgets::*;

live_design! {
    use link::theme::*;
    use link::shaders::*;
    use link::widgets::*;

    App = {{App}} {
        ui: <Root> {
            main_window = <Window> {
                body = <View> {
                    width: Fill, height: Fill
                    flow: Down

                    <Label> { text: "Hello Makepad!" }
                }
            }
        }
    }
}

app_main!(App);

#[derive(Live, LiveHook)]
pub struct App {
    #[live] ui: WidgetRef,
}

impl LiveRegister for App {
    fn live_register(cx: &mut Cx) {
        crate::makepad_widgets::live_design(cx);
    }
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}
```

### 2. Cargo.toml Setup

```toml
[package]
name = "my_app"
version = "0.1.0"
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }
```

### 3. Handling Button Clicks

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        let actions = self.ui.handle_event(cx, event, &mut Scope::empty());

        if self.ui.button(id!(my_button)).clicked(&actions) {
            log!("Button clicked!");
        }
    }
}
```

### 4. Accessing and Modifying Widgets

```rust
// Get widget references
let label = self.ui.label(id!(my_label));
label.set_text("Updated text");

let input = self.ui.text_input(id!(my_input));
let text = input.text();
```

## API Reference Table

| Macro/Type | Description | Example |
|------------|-------------|---------|
| `live_design!` | Defines UI in DSL | `live_design! { App = {{App}} { ... } }` |
| `app_main!` | Entry point macro | `app_main!(App);` |
| `#[derive(Live)]` | Derive live data | `#[derive(Live, LiveHook)]` |
| `WidgetRef` | Reference to UI tree | `#[live] ui: WidgetRef` |
| `Cx` | Context for rendering | `fn handle_event(&mut self, cx: &mut Cx, ...)` |
| `id!()` | Widget ID macro | `self.ui.button(id!(my_button))` |

## Platform Setup

| Platform | Requirements |
|----------|--------------|
| macOS | Works out of the box |
| Windows | Works out of the box |
| Linux | `apt-get install clang libaudio-dev libpulse-dev libx11-dev libxcursor-dev` |
| Web | `cargo install wasm-pack` |

## When Writing Code

1. Always include required imports: `use makepad_widgets::*;`
2. Use `live_design!` macro for all UI definitions
3. Implement `LiveRegister` and `AppMain` traits
4. Use `id!()` macro for widget references
5. Handle events through `handle_event` method

## When Answering Questions

1. Emphasize live design - changes in DSL reflect instantly without recompilation
2. Makepad is GPU-first - all rendering is shader-based
3. Cross-platform: same code runs on Android, iOS, Linux, macOS, Windows, Web
4. Recommend UI Zoo example for widget exploration
```

## File: `skills/makepad-basics/references/app-structure.md`
```markdown
# Makepad App Structure Reference

## Complete App Template

```rust
use makepad_widgets::*;

live_design! {
    use link::theme::*;
    use link::shaders::*;
    use link::widgets::*;

    App = {{App}} {
        ui: <Root> {
            main_window = <Window> {
                window: { title: "My Makepad App" }
                body = <View> {
                    width: Fill
                    height: Fill
                    flow: Down
                    align: { x: 0.5, y: 0.5 }

                    // Your widgets here
                }
            }
        }
    }
}

app_main!(App);

#[derive(Live, LiveHook)]
pub struct App {
    #[live] ui: WidgetRef,
}

impl LiveRegister for App {
    fn live_register(cx: &mut Cx) {
        crate::makepad_widgets::live_design(cx);
    }
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}
```

## Key Components

### live_design! Macro

The `live_design!` macro defines your UI using Makepad's DSL. It's compiled at runtime, enabling live editing.

```rust
live_design! {
    // Import theme, shaders, and widgets
    use link::theme::*;
    use link::shaders::*;
    use link::widgets::*;

    // Define your app structure
    App = {{App}} {
        ui: <Root> {
            // Window and content
        }
    }
}
```

### App Struct

```rust
#[derive(Live, LiveHook)]
pub struct App {
    #[live] ui: WidgetRef,
    // Add custom state fields
    #[rust] counter: i32,
}
```

- `#[derive(Live)]` - Makes struct live-editable
- `#[derive(LiveHook)]` - Provides lifecycle hooks
- `#[live]` - Field synced with DSL
- `#[rust]` - Rust-only field, not in DSL

### LiveRegister Trait

```rust
impl LiveRegister for App {
    fn live_register(cx: &mut Cx) {
        // Register your crate's live design
        crate::makepad_widgets::live_design(cx);
        // Register custom widgets
        // crate::my_widget::live_design(cx);
    }
}
```

### AppMain Trait

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Process events and get actions
        let actions = self.ui.handle_event(cx, event, &mut Scope::empty());

        // Handle specific widget actions
        // ...
    }
}
```

## Project Structure

```
my_makepad_app/
├── Cargo.toml
├── src/
│   ├── main.rs          # App entry point
│   └── lib.rs           # (optional) Library code
└── resources/           # Assets
    ├── icons/
    └── images/
```

## Cargo.toml

```toml
[package]
name = "my_makepad_app"
version = "0.1.0"
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }

# For mobile/web builds (add features as needed)
[target.'cfg(target_os = "android")'.dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev", features = ["android"] }

[target.'cfg(target_arch = "wasm32")'.dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev", features = ["wasm"] }
```

## Running Your App

```bash
# Desktop
cargo run

# Web (requires wasm-pack)
cargo makepad wasm run -p my_makepad_app

# Android
cargo makepad android run -p my_makepad_app

# iOS
cargo makepad ios run -p my_makepad_app
```
```

## File: `skills/makepad-basics/references/event-handling.md`
```markdown
# Makepad Event Handling Reference

## Basic Event Handling Pattern

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        let actions = self.ui.handle_event(cx, event, &mut Scope::empty());

        // Handle button clicks
        if self.ui.button(id!(submit_btn)).clicked(&actions) {
            self.on_submit(cx);
        }

        // Handle text input changes
        if let Some(text) = self.ui.text_input(id!(name_input)).changed(&actions) {
            self.name = text;
        }

        // Handle checkbox toggle
        if self.ui.check_box(id!(agree_checkbox)).changed(&actions).is_some() {
            self.agreed = self.ui.check_box(id!(agree_checkbox)).selected(cx);
        }
    }
}
```

## Widget Action Methods

### Button

```rust
// Check if clicked
if self.ui.button(id!(my_btn)).clicked(&actions) {
    // Handle click
}

// Check if pressed (held down)
if self.ui.button(id!(my_btn)).pressed(&actions) {
    // Handle press
}

// Check if released
if self.ui.button(id!(my_btn)).released(&actions) {
    // Handle release
}
```

### TextInput

```rust
// Get changed text
if let Some(new_text) = self.ui.text_input(id!(input)).changed(&actions) {
    println!("Text changed to: {}", new_text);
}

// Get text programmatically
let current_text = self.ui.text_input(id!(input)).text();

// Set text programmatically
self.ui.text_input(id!(input)).set_text("New value");
```

### CheckBox / RadioButton

```rust
// Check if toggled
if self.ui.check_box(id!(checkbox)).changed(&actions).is_some() {
    let is_selected = self.ui.check_box(id!(checkbox)).selected(cx);
}
```

### Slider

```rust
// Get slider value change
if let Some(value) = self.ui.slider(id!(volume)).changed(&actions) {
    println!("Volume: {}", value);
}
```

### DropDown

```rust
// Check selection change
if let Some(index) = self.ui.drop_down(id!(dropdown)).selected(&actions) {
    println!("Selected index: {}", index);
}
```

## Accessing Widgets

### By ID

```rust
// Direct access
let label = self.ui.label(id!(my_label));
label.set_text("Hello");

// Nested access
let nested_btn = self.ui.view(id!(container)).button(id!(nested_btn));
```

### Widget Reference Types

| Widget | Access Method | Common Operations |
|--------|---------------|-------------------|
| `Label` | `.label(id!(...))` | `.set_text()` |
| `Button` | `.button(id!(...))` | `.clicked()`, `.pressed()` |
| `TextInput` | `.text_input(id!(...))` | `.text()`, `.set_text()`, `.changed()` |
| `CheckBox` | `.check_box(id!(...))` | `.selected()`, `.changed()` |
| `Slider` | `.slider(id!(...))` | `.changed()` |
| `DropDown` | `.drop_down(id!(...))` | `.selected()` |
| `View` | `.view(id!(...))` | `.redraw()` |
| `Image` | `.image(id!(...))` | `.set_texture()` |

## Triggering Redraws

```rust
// Redraw specific widget
self.ui.view(id!(my_view)).redraw(cx);

// Redraw entire UI
self.ui.redraw(cx);
```

## Custom Actions

```rust
// Define custom action
#[derive(Clone, Debug, DefaultNone)]
pub enum MyAction {
    None,
    DataLoaded(Vec<String>),
    Error(String),
}

// Dispatch action
cx.action(MyAction::DataLoaded(data));

// Handle in event loop
if let MyAction::DataLoaded(data) = event.action::<MyAction>() {
    self.data = data;
}
```
```

## File: `skills/makepad-deployment/SKILL.md`
```markdown
---
name: makepad-deployment
description: |
  CRITICAL: Use for Makepad packaging and deployment. Triggers on:
  deploy, package, APK, IPA, 打包, 部署,
  cargo-packager, cargo-makepad, WASM, Android, iOS,
  distribution, installer, .deb, .dmg, .nsis,
  GitHub Actions, CI, action, marketplace
---

# Makepad Packaging & Deployment

This skill covers packaging Makepad applications for all supported platforms.

## Quick Navigation

| Platform | Tool | Output |
|----------|------|--------|
| [Desktop](#desktop-packaging) | `cargo-packager` | .deb, .nsis, .dmg |
| [Android](#android) | `cargo-makepad` | .apk |
| [iOS](#ios) | `cargo-makepad` | .app, .ipa |
| [Web](#wasm-packaging) | `cargo-makepad` | Wasm + HTML/JS |
| [CI/CD](#github-actions-packaging) | `makepad-packaging-action` | GitHub Release assets |

---

## GitHub Actions Packaging

Use `makepad-packaging-action` to package Makepad apps in CI. It wraps
`cargo-packager` (desktop) and `cargo-makepad` (mobile), and can upload artifacts
to GitHub Releases.

```yaml
jobs:
  package:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: Project-Robius-China/makepad-packaging-action@v1
        with:
          args: --target x86_64-unknown-linux-gnu --release
```

Notes:
- Desktop packages must run on matching OS runners (Linux/Windows/macOS).
- iOS builds require macOS runners.
- Android builds can run on any OS runner.

Full inputs/env/outputs and release workflows live in
`references/makepad-packaging-action.md`.

## Desktop Packaging

Desktop packaging uses `cargo-packager` with `robius-packaging-commands` for resource handling.

### Install Tools

```bash
# Install cargo-packager
cargo install cargo-packager --locked

# Install robius-packaging-commands (v0.2.1)
cargo install --version 0.2.1 --locked \
    --git https://github.com/project-robius/robius-packaging-commands.git \
    robius-packaging-commands
```

### Configure Cargo.toml

Add packaging configuration to your `Cargo.toml`:

```toml
[package.metadata.packager]
product_name = "YourAppName"
identifier = "com.yourcompany.yourapp"
authors = ["Your Name or Team"]
description = "A brief description of your Makepad application"
# Note: long_description has 80 character max per line
long_description = """
Your detailed description here.
Keep each line under 80 characters.
"""
icons = ["./assets/icon.png"]
out_dir = "./dist"

# Pre-packaging command to collect resources
before-packaging-command = """
robius-packaging-commands before-packaging \
    --force-makepad \
    --binary-name your-app \
    --path-to-binary ./target/release/your-app
"""

# Resources to include in package
resources = [
    # Makepad built-in resources (required)
    { src = "./dist/resources/makepad_widgets", target = "makepad_widgets" },
    { src = "./dist/resources/makepad_fonts_chinese_bold", target = "makepad_fonts_chinese_bold" },
    { src = "./dist/resources/makepad_fonts_chinese_bold_2", target = "makepad_fonts_chinese_bold_2" },
    { src = "./dist/resources/makepad_fonts_chinese_regular", target = "makepad_fonts_chinese_regular" },
    { src = "./dist/resources/makepad_fonts_chinese_regular_2", target = "makepad_fonts_chinese_regular_2" },
    { src = "./dist/resources/makepad_fonts_emoji", target = "makepad_fonts_emoji" },

    # Your app resources
    { src = "./dist/resources/your_app_resource", target = "your_app_resource" },
]

before-each-package-command = """
robius-packaging-commands before-each-package \
    --force-makepad \
    --binary-name your-app \
    --path-to-binary ./target/release/your-app
"""
```

### Linux (Debian/Ubuntu)

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install libssl-dev libsqlite3-dev pkg-config \
    binfmt-support libxcursor-dev libx11-dev libasound2-dev libpulse-dev

# Build package
cargo packager --release
```

Output: `.deb` file in `./dist/`

### Windows

```bash
# Build NSIS installer
cargo packager --release --formats nsis
```

Output: `.exe` installer in `./dist/`

### macOS

```bash
# Build package
cargo packager --release
```

Output: `.dmg` file in `./dist/`

### Platform-Specific Configuration

```toml
# Linux (Debian)
[package.metadata.packager.deb]
depends = "./dist/depends_deb.txt"
desktop_template = "./packaging/your-app.desktop"
section = "utils"

# macOS
[package.metadata.packager.macos]
minimum_system_version = "11.0"
frameworks = []
info_plist_path = "./packaging/Info.plist"
entitlements = "./packaging/Entitlements.plist"
# Optional: signing identity for distribution
signing_identity = "Developer ID Application: Your Name (XXXXXXXXXX)"

# macOS DMG
[package.metadata.packager.dmg]
background = "./packaging/dmg_background.png"
window_size = { width = 960, height = 540 }
app_position = { x = 200, y = 250 }
application_folder_position = { x = 760, y = 250 }

# Windows NSIS
[package.metadata.packager.nsis]
appdata_paths = [
    "$APPDATA/$PUBLISHER/$PRODUCTNAME",
    "$LOCALAPPDATA/$PRODUCTNAME",
]
```

---

## Mobile Packaging

Mobile platforms use `cargo-makepad` for building and packaging.

### Install cargo-makepad

```bash
cargo install --force --git https://github.com/makepad/makepad.git \
    --branch dev cargo-makepad
```

### Android

```bash
# Install Android toolchain
cargo makepad android install-toolchain

# Full NDK (recommended for complete support)
cargo makepad android install-toolchain --full-ndk

# Build APK
cargo makepad android build -p your-app --release
```

Output: `.apk` in `./target/makepad-android-app/`

**Run on device/emulator:**
```bash
cargo makepad android run -p your-app --release
```

### iOS

```bash
# Install iOS toolchain
cargo makepad apple ios install-toolchain
```

**iOS Simulator:**
```bash
cargo makepad apple ios \
    --org=com.yourcompany \
    --app=YourApp \
    run-sim -p your-app --release
```

Output: `.app` in `./target/makepad-apple-app/aarch64-apple-ios-sim/release/`

**iOS Device (requires provisioning):**

First, create an empty app in Xcode with matching org/app names to generate provisioning profile.

```bash
cargo makepad apple ios \
    --org=com.yourcompany \
    --app=YourApp \
    --profile=$YOUR_PROFILE_PATH \
    --cert=$YOUR_CERT_FINGERPRINT \
    --device=iPhone \
    run-device -p your-app --release
```

Output: `.app` in `./target/makepad-apple-app/aarch64-apple-ios/release/`

**Create IPA for distribution:**
```bash
cd ./target/makepad-apple-app/aarch64-apple-ios/release
mkdir Payload
cp -r your-app.app Payload/
zip -r your-app-ios.ipa Payload
```

---

## Wasm Packaging

Build your Makepad app for web browsers.

```bash
# Install Wasm toolchain
cargo makepad wasm install-toolchain

# Build and run
cargo makepad wasm run -p your-app --release
```

Output in `./target/makepad-wasm-app/release/your-app/`:
- `index.html` - Entry point
- `*.wasm` - WebAssembly module
- `*.js` - JavaScript bridge
- `resources/` - Static assets

**Serve locally:**
```bash
cd ./target/makepad-wasm-app/release/your-app
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## Complete Example Cargo.toml

```toml
[package]
name = "my-makepad-app"
version = "1.0.0"
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }

[profile.release]
opt-level = 3

[profile.release-lto]
inherits = "release"
lto = "thin"

[profile.distribution]
inherits = "release"
codegen-units = 1
lto = "fat"

[package.metadata.packager]
product_name = "My Makepad App"
identifier = "com.example.mymakepadapp"
authors = ["Your Name <you@example.com>"]
description = "A cross-platform Makepad application"
long_description = """
My Makepad App is a cross-platform application
built with the Makepad UI framework in Rust.
It runs on desktop, mobile, and web platforms.
"""
icons = ["./packaging/icon.png"]
out_dir = "./dist"

before-packaging-command = """
robius-packaging-commands before-packaging \
    --force-makepad \
    --binary-name my-makepad-app \
    --path-to-binary ./target/release/my-makepad-app
"""

resources = [
    { src = "./dist/resources/makepad_widgets", target = "makepad_widgets" },
    { src = "./dist/resources/makepad_fonts_chinese_bold", target = "makepad_fonts_chinese_bold" },
    { src = "./dist/resources/makepad_fonts_chinese_bold_2", target = "makepad_fonts_chinese_bold_2" },
    { src = "./dist/resources/makepad_fonts_chinese_regular", target = "makepad_fonts_chinese_regular" },
    { src = "./dist/resources/makepad_fonts_chinese_regular_2", target = "makepad_fonts_chinese_regular_2" },
    { src = "./dist/resources/makepad_fonts_emoji", target = "makepad_fonts_emoji" },
    { src = "./dist/resources/my-makepad-app", target = "my-makepad-app" },
]

before-each-package-command = """
robius-packaging-commands before-each-package \
    --force-makepad \
    --binary-name my-makepad-app \
    --path-to-binary ./target/release/my-makepad-app
"""

[package.metadata.packager.deb]
depends = "./dist/depends_deb.txt"
section = "utils"

[package.metadata.packager.macos]
minimum_system_version = "11.0"

[package.metadata.packager.nsis]
appdata_paths = ["$LOCALAPPDATA/$PRODUCTNAME"]
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Install desktop packager | `cargo install cargo-packager --locked` |
| Install resource helper | `cargo install --version 0.2.1 --locked --git https://github.com/project-robius/robius-packaging-commands.git robius-packaging-commands` |
| Install mobile packager | `cargo install --force --git https://github.com/makepad/makepad.git --branch dev cargo-makepad` |
| GitHub Actions packaging | `uses: Project-Robius-China/makepad-packaging-action@v1` |
| Package for Linux | `cargo packager --release` |
| Package for Windows | `cargo packager --release --formats nsis` |
| Package for macOS | `cargo packager --release` |
| Build Android APK | `cargo makepad android build -p app --release` |
| Build iOS (Simulator) | `cargo makepad apple ios --org=x --app=y run-sim -p app --release` |
| Build iOS (Device) | `cargo makepad apple ios --org=x --app=y --profile=... --cert=... run-device -p app --release` |
| Build Wasm | `cargo makepad wasm run -p app --release` |

---

## Troubleshooting

### Missing Resources

If app crashes with missing resources:
1. Check `resources` array in Cargo.toml includes all Makepad resources
2. Verify `before-packaging-command` runs successfully
3. Check `./dist/resources/` contains expected files

### iOS Provisioning

For iOS device deployment:
1. Create empty app in Xcode with same org/app identifiers
2. Run on physical device once to generate provisioning profile
3. Note the profile path, certificate fingerprint
4. Use `--profile`, `--cert`, `--device` flags

### Android SDK Issues

```bash
# Reinstall toolchain with full NDK
cargo makepad android install-toolchain --full-ndk
```

## Reference Files

- `references/platform-troubleshooting.md` - Platform-specific deployment issues
- `references/makepad-packaging-action.md` - GitHub Actions packaging reference
- `community/dora-studio-package-workflow.md` - Dora Studio CI packaging example

## External References

- [cargo-packager docs](https://docs.crabnebula.dev/packager/)
- [robius-packaging-commands](https://github.com/project-robius/robius-packaging-commands)
- [cargo-makepad](https://github.com/makepad/makepad)
- [makepad-packaging-action](https://github.com/marketplace/actions/makepad-packaging-action)
```

## File: `skills/makepad-deployment/community/dora-studio-package-workflow.md`
```markdown
---
name: dora-studio-package-workflow
author: Tyrese Luo
source: dora-studio package.yml
date: 2026-02-04
tags: [deployment, github-actions, packaging, release, cargo-packager, cargo-makepad]
level: intermediate
makepad-branch: dev
---

# Dora Studio GitHub Actions packaging workflow

## Summary
CI workflow that creates a GitHub Release and packages desktop, Android, and iOS
artifacts using `makepad-packaging-action`.

## When to use
For multi-platform packaging in CI with optional release upload.

## Full workflow (verbatim)
```yaml
name: Build Makepad (All Platforms)

on:
  push:
    tags: ['v*']
  workflow_dispatch:
    inputs:
      build_desktop:
        description: "Build desktop packages"
        type: boolean
        default: true
      build_android:
        description: "Build Android APK"
        type: boolean
        default: true
      build_ios:
        description: "Build iOS app"
        type: boolean
        default: true
      release_tag:
        description: "Release tag (optional, supports __VERSION__)"
        type: string
        default: ""
      release_name:
        description: "Release name (optional, supports __VERSION__)"
        type: string
        default: ""
      release_body:
        description: "Release body (optional)"
        type: string
        default: ""
      release_draft:
        description: "Create draft release"
        type: boolean
        default: false
      prerelease:
        description: "Mark as prerelease"
        type: boolean
        default: false
      args:
        description: "Extra args passed to the action"
        type: string
        default: ""

permissions:
  contents: write

env:
  CARGO_TERM_COLOR: always

jobs:
  # Create release first (only once)
  create-release:
    name: Create Release
    runs-on: ubuntu-22.04
    outputs:
      release_tag: ${{ steps.get_tag.outputs.tag }}
      release_upload_url: ${{ steps.create_release.outputs.upload_url }}
      release_id: ${{ steps.create_release.outputs.id }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Get tag
        id: get_tag
        run: |
          if [ "${{ github.event_name }}" = "push" ] && [ "${{ github.ref_type }}" = "tag" ]; then
            echo "tag=${{ github.ref_name }}" >> $GITHUB_OUTPUT
          elif [ -n "${{ inputs.release_tag }}" ]; then
            echo "tag=${{ inputs.release_tag }}" >> $GITHUB_OUTPUT
          else
            echo "tag=v$(date +'%Y%m%d%H%M%S')" >> $GITHUB_OUTPUT
          fi

      - name: Get release name
        id: get_name
        run: |
          if [ -n "${{ inputs.release_name }}" ]; then
            echo "name=${{ inputs.release_name }}" >> $GITHUB_OUTPUT
          else
            echo "name=Dora Studio ${{ steps.get_tag.outputs.tag }}" >> $GITHUB_OUTPUT
          fi

      - name: Create Release
        id: create_release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: ${{ steps.get_tag.outputs.tag }}
          name: ${{ steps.get_name.outputs.name }}
          body: |
            ${{ inputs.release_body != '' && inputs.release_body || '## Dora Studio Release

            ### Downloads
            See the assets below for platform-specific downloads.

            ### Platforms
            - macOS (Apple Silicon)
            - Linux (x86_64)
            - Windows (x86_64)
            - Android (arm64)
            - iOS (arm64)' }}
          draft: ${{ inputs.release_draft || false }}
          prerelease: ${{ inputs.prerelease || false }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  desktop:
    name: Desktop (${{ matrix.name }})
    needs: create-release
    if: ${{ always() && (github.event_name == 'push' || inputs.build_desktop) }}
    strategy:
      fail-fast: false
      matrix:
        include:
          - os: ubuntu-22.04
            packager_formats: deb
            name: Linux
          - os: macos-14
            packager_formats: dmg
            name: macOS
          - os: windows-2022
            packager_formats: nsis
            name: Windows
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable

      - name: Install Linux dependencies
        if: startsWith(matrix.os, 'ubuntu')
        run: |
          sudo apt-get update
          sudo apt-get install libssl-dev pkg-config llvm clang libclang-dev binfmt-support libxcursor-dev libx11-dev libasound2-dev libpulse-dev libwayland-dev libxkbcommon-dev

      - name: Package (desktop)
        uses: Project-Robius-China/makepad-packaging-action@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          releaseId: ${{ needs.create-release.outputs.release_id }}
          args: ${{ inputs.args }}
          packager_formats: ${{ matrix.packager_formats }}

  android:
    name: Android
    needs: create-release
    if: ${{ always() && (github.event_name == 'push' || inputs.build_android) }}
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable

      - name: Package (android)
        uses: Project-Robius-China/makepad-packaging-action@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          releaseId: ${{ needs.create-release.outputs.release_id }}
          args: --target aarch64-linux-android ${{ inputs.args }}

  ios:
    name: iOS
    needs: create-release
    if: ${{ always() && (github.event_name == 'push' || inputs.build_ios) }}
    runs-on: macos-14
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable

      - name: Package (iOS)
        uses: Project-Robius-China/makepad-packaging-action@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          MAKEPAD_IOS_ORG: com.mofa
          MAKEPAD_IOS_APP: dora-studio
          APPLE_CERTIFICATE: ${{ secrets.APPLE_CERTIFICATE }}
          APPLE_CERTIFICATE_PASSWORD: ${{ secrets.APPLE_CERTIFICATE_PASSWORD }}
          APPLE_PROVISIONING_PROFILE: ${{ secrets.APPLE_PROVISIONING_PROFILE }}
          APPLE_KEYCHAIN_PASSWORD: ${{ secrets.APPLE_KEYCHAIN_PASSWORD }}
        with:
          releaseId: ${{ needs.create-release.outputs.release_id }}
          args: --target aarch64-apple-ios ${{ inputs.args }}
```

## Notes
- Desktop packages must run on matching OS runners.
- iOS builds require macOS runners.
- Android builds can run on any OS runner.

## Source
- https://github.com/dora-rs/dora-studio/blob/main/.github/workflows/package.yml
```

## File: `skills/makepad-deployment/references/makepad-packaging-action.md`
```markdown
# Makepad Packaging GitHub Action

## 中文摘要

- 用于 GitHub Actions 中的 Makepad 打包与发布，支持桌面、移动与 OpenHarmony。
- 内部封装 `cargo-packager` 与 `cargo-makepad`，可上传产物到 GitHub Releases。
- 通过 `args` 指定 target，移动端必须显式指定 target。
- 桌面/iOS 需要匹配的 runner（iOS 需 macOS）。

详细字段与示例见下文英文参考。

Reference for `makepad-packaging-action` (CI packaging + optional GitHub Release upload).

## When to use
- One-step packaging for desktop and mobile targets in CI
- Matrix builds across OS and target triples
- Upload artifacts to GitHub Releases

## Platform constraints
- Linux packages must run on Linux runners.
- Windows installers must run on Windows runners.
- macOS DMG/app bundles and iOS builds require macOS runners.
- Android builds can run on any OS runner.

## Inputs

| Input | Notes |
| --- | --- |
| `args` | Extra args passed to `cargo build` and `cargo makepad` (use `--target ...`). |
| `packager_formats` | Comma-separated `cargo packager` formats (`deb,dmg,nsis`). |
| `packager_args` | Extra args passed only to `cargo packager`. |
| `tagName` | Release tag name. Supports `__VERSION__`. |
| `releaseName` | Release title. Supports `__VERSION__`. |
| `releaseBody` | Release body markdown. |
| `releaseId` | Existing release ID to upload assets to. |
| `asset_name_template` | Template for asset names. Placeholders: `__APP__`, `__VERSION__`, `__PLATFORM__`, `__ARCH__`, `__MODE__`, `__EXT__`, `__FILENAME__`, `__BASENAME__`. |
| `asset_prefix` | Optional prefix for generated asset names. |
| `releaseDraft` | Create a draft release (`true`/`false`). |
| `prerelease` | Mark as prerelease (`true`/`false`). |
| `github_token` | Token for release creation/upload (defaults to `GITHUB_TOKEN`). |
| `project_path` | Makepad project path (default `.`). |
| `app_name` | Override app name (otherwise derived from `Cargo.toml`). |
| `app_version` | Override version (otherwise derived from `Cargo.toml`). |
| `identifier` | Override bundle identifier. |
| `include_release` | Include release build (`true`/`false`, default `true`). |
| `include_debug` | Include debug build (`true`/`false`, default `false`). |

## Environment variables

Android:
- `MAKEPAD_ANDROID_ABI` (default `aarch64`)
- `MAKEPAD_ANDROID_FULL_NDK` (`true`/`false`)
- `MAKEPAD_ANDROID_VARIANT` (`default` or `quest`)

iOS:
- `MAKEPAD_IOS_ORG`
- `MAKEPAD_IOS_APP`
- `MAKEPAD_IOS_PROFILE` (optional)
- `MAKEPAD_IOS_CERT` (optional)
- `MAKEPAD_IOS_SIM` (`true`/`false`)
- `MAKEPAD_IOS_CREATE_IPA` (`true`/`false`)
- `MAKEPAD_IOS_UPLOAD_TESTFLIGHT` (`true`/`false`)

Apple signing:
- `APPLE_CERTIFICATE` (base64 `.p12`)
- `APPLE_CERTIFICATE_PASSWORD`
- `APPLE_PROVISIONING_PROFILE` (base64 `.mobileprovision`)
- `APPLE_KEYCHAIN_PASSWORD`
- `APPLE_SIGNING_IDENTITY` (default `Apple Distribution`)

TestFlight upload (when `MAKEPAD_IOS_UPLOAD_TESTFLIGHT=true`):
- `APP_STORE_CONNECT_API_KEY` or `APP_STORE_CONNECT_API_KEY_CONTENT`
- `APP_STORE_CONNECT_KEY_ID`
- `APP_STORE_CONNECT_ISSUER_ID`

OpenHarmony (HAP):
- `DEVECO_HOME` (optional, auto-detected if omitted)
- `OHOS_P12_BASE64`
- `OHOS_PROFILE_BASE64`
- `OHOS_P12_PASSWORD`
- `OHOS_KEY_ALIAS` (default `debugKey`)
- `OHOS_KEY_PASSWORD` (default `OHOS_P12_PASSWORD`)
- `OHOS_CERT_BASE64` (optional)
- `OHOS_SIGN_ALG` (default `SHA256withECDSA`)

## Outputs

| Output | Notes |
| --- | --- |
| `artifacts` | JSON array of `{ path, platform, arch, mode, version }`. |
| `app_name` | Resolved app name. |
| `app_version` | Resolved app version. |
| `release_url` | GitHub Release URL (if created). |

## Behavior notes
- Target defaults to host platform unless `--target` is passed in `args`.
- Mobile builds require an explicit target triple.
- If `releaseId` is set, assets are uploaded without creating a release.
- If `tagName` is set (and `releaseId` is not), a release is created/updated.
- Directory artifacts (like `.app`) are zipped before upload.

## Examples

Minimal packaging (Linux):
```yaml
jobs:
  package:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: Project-Robius-China/makepad-packaging-action@v1
        with:
          args: --target x86_64-unknown-linux-gnu --release
```

Matrix build with release upload:
```yaml
jobs:
  package:
    strategy:
      matrix:
        include:
          - os: ubuntu-22.04
            args: --target x86_64-unknown-linux-gnu
          - os: windows-2022
            args: --target x86_64-pc-windows-msvc
          - os: macos-14
            args: --target aarch64-apple-darwin
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: Project-Robius-China/makepad-packaging-action@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tagName: app-v__VERSION__
          releaseName: "App v__VERSION__"
          releaseBody: "See the assets to download this version."
          args: ${{ matrix.args }}
```

Upload to an existing release:
```yaml
- uses: Project-Robius-China/makepad-packaging-action@v1
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  with:
    releaseId: ${{ needs.create_release.outputs.id }}
    args: --target aarch64-linux-android
```

## Status
- Desktop packaging: implemented
- Android packaging: implemented
- iOS packaging: implemented
- OpenHarmony packaging: implemented
- Web packaging: not implemented yet
```

## File: `skills/makepad-deployment/references/platform-troubleshooting.md`
```markdown
# Platform-Specific Troubleshooting

Common deployment issues and solutions for each platform.

## Desktop (Linux)

### Missing System Libraries

**Error**: `error while loading shared libraries: libxxx.so.x`

**Solution**:
```bash
# Common dependencies for Makepad on Debian/Ubuntu
sudo apt-get update
sudo apt-get install -y \
    libssl-dev \
    libsqlite3-dev \
    pkg-config \
    binfmt-support \
    libxcursor-dev \
    libx11-dev \
    libasound2-dev \
    libpulse-dev
```

### Package Build Fails

**Symptom**: `cargo packager` fails with resource errors

**Checklist**:
1. Verify `robius-packaging-commands` version is 0.2.1
2. Ensure `before-packaging-command` path matches your binary name
3. Check `./dist/resources/` exists after running the command

---

## Desktop (macOS)

### Code Signing Issues

**Error**: "your-app is damaged and can't be opened"

**Solutions**:
1. For development, disable Gatekeeper:
   ```bash
   xattr -cr /path/to/your-app.app
   ```
2. For distribution, sign with Developer ID:
   ```toml
   [package.metadata.packager.macos]
   signing_identity = "Developer ID Application: Your Name (TEAMID)"
   ```

### Minimum macOS Version

**Error**: App won't launch on older macOS

**Solution**: Set minimum version in Cargo.toml:
```toml
[package.metadata.packager.macos]
minimum_system_version = "10.15"  # Catalina
```

---

## Desktop (Windows)

### NSIS Installer Issues

**Error**: NSIS build fails

**Solutions**:
1. Install NSIS: https://nsis.sourceforge.io/
2. Add NSIS to PATH
3. Use `--formats nsis` explicitly:
   ```bash
   cargo packager --release --formats nsis
   ```

### DLL Dependencies

**Symptom**: App starts but crashes with missing DLLs

**Solution**: Include Visual C++ Redistributable or static link:
```toml
[target.'cfg(target_os = "windows")'.dependencies]
# Link statically to avoid DLL dependencies
```

---

## Android

### NDK Not Found

**Error**: `NDK not found at expected location`

**Solution**:
```bash
# Reinstall with full NDK
cargo makepad android install-toolchain --full-ndk
```

### APK Install Fails

**Error**: `INSTALL_FAILED_NO_MATCHING_ABIS`

**Solution**: Build for correct architecture:
```bash
# ARM64 devices (most modern phones)
cargo makepad android build -p your-app --release
```

### Resource Loading Fails

**Symptom**: App crashes on startup with "resource not found"

**Checklist**:
1. Check `live_design!` uses correct resource paths
2. Verify resource files are in correct `src/` location
3. Check file names match (case-sensitive on Android)

---

## iOS

### Provisioning Profile Issues

**Error**: `No provisioning profile found`

**Solution**:
1. Create empty project in Xcode with same bundle ID
2. Run on device once to generate profile
3. Find profile path: `~/Library/MobileDevice/Provisioning Profiles/`
4. Get cert fingerprint: `security find-identity -v -p codesigning`

### Simulator vs Device Architecture

**Symptom**: Works on simulator, fails on device

**Solution**: Use correct target:
- Simulator: `run-sim` (arm64-apple-ios-sim)
- Device: `run-device` (arm64-apple-ios)

### App Store Submission

**Requirements**:
1. Create IPA:
   ```bash
   mkdir Payload
   cp -r your-app.app Payload/
   zip -r your-app.ipa Payload
   ```
2. Use App Store Connect / Transporter for upload
3. Ensure proper entitlements and signing

---

## Wasm

### Large Bundle Size

**Problem**: Wasm file too large (>10MB)

**Solutions**:
1. Use release profile with LTO:
   ```toml
   [profile.release]
   lto = "thin"
   opt-level = "z"  # Optimize for size
   ```
2. Use `wasm-opt` for additional optimization:
   ```bash
   wasm-opt -Oz -o output.wasm input.wasm
   ```

### Audio Not Working

**Symptom**: No sound in browser

**Solution**: Audio requires user interaction first (browser security).
Add a "Start" button that initiates audio context.

### CORS Errors

**Error**: `Cross-Origin Request Blocked`

**Solution**: Configure server with proper CORS headers:
```
Access-Control-Allow-Origin: *
Content-Type: application/wasm
```

---

## Common Issues (All Platforms)

### Resources Not Found

**Symptom**: "Failed to load resource: makepad_widgets/..."

**Checklist**:
1. Ensure all required resources in Cargo.toml `resources`:
   - makepad_widgets
   - makepad_fonts_* (if using Chinese/Emoji fonts)
   - Your app resources
2. Verify paths match actual file locations

### Release vs Debug Differences

**Symptom**: Works in debug, fails in release

**Common Causes**:
1. Optimization removes required code (check `#[inline(never)]`)
2. Release build uses different resource paths
3. Debug logging masks timing issues

### Font Rendering Issues

**Symptom**: Text displays as boxes or wrong characters

**Solutions**:
1. Include appropriate font resources:
   - `makepad_fonts_chinese_bold` / `regular` for Chinese
   - `makepad_fonts_emoji` for emoji support
2. Verify font files are in resources array
3. Check font file integrity (not corrupted during packaging)
```

## File: `skills/makepad-dsl/SKILL.md`
```markdown
---
name: makepad-dsl
description: |
  CRITICAL: Use for Makepad DSL syntax and inheritance. Triggers on:
  makepad dsl, live_design, makepad inheritance, makepad prototype,
  "<Widget>", "Foo = { }", makepad object, makepad property,
  makepad DSL 语法, makepad 继承, makepad 原型, 如何定义 makepad 组件
---

# Makepad DSL Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at the Rust `makepad-widgets` crate DSL. Help users by:
- **Writing code**: Generate DSL code following the patterns below
- **Answering questions**: Explain DSL syntax, inheritance, property overriding

## Documentation

Refer to the local files for detailed documentation:
- `./references/dsl-syntax.md` - Complete DSL syntax reference
- `./references/inheritance.md` - Inheritance patterns and examples

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. Anonymous Object

```rust
{
    width: 100.0
    height: 50.0
    color: #FF0000
}
```

### 2. Named Object (Prototype)

```rust
MyButton = {
    width: Fit
    height: 40.0
    padding: 10.0
    draw_bg: { color: #333333 }
}
```

### 3. Inheritance with Override

```rust
PrimaryButton = <MyButton> {
    draw_bg: { color: #0066CC }  // Override parent color
    draw_text: { color: #FFFFFF }  // Add new property
}
```

### 4. Widget Instantiation

```rust
<View> {
    // Inherits from View prototype
    width: Fill
    height: Fill

    <Button> { text: "Click Me" }  // Child widget
    <Label> { text: "Hello" }      // Another child
}
```

### 5. Linking Rust Struct to DSL

```rust
// In live_design!
MyWidget = {{MyWidget}} {
    // DSL properties
    width: 100.0
}

// In Rust
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,
    #[live] width: f64,
}
```

## DSL Syntax Reference

| Syntax | Description | Example |
|--------|-------------|---------|
| `{ ... }` | Anonymous object | `{ width: 100.0 }` |
| `Name = { ... }` | Named prototype | `MyStyle = { color: #FFF }` |
| `<Name> { ... }` | Inherit from prototype | `<MyStyle> { size: 10.0 }` |
| `{{RustType}}` | Link to Rust struct | `App = {{App}} { ... }` |
| `name = <Widget>` | Named child widget | `btn = <Button> { }` |
| `dep("...")` | Resource dependency | `dep("crate://self/img.png")` |

## Property Types

| Type | Example | Description |
|------|---------|-------------|
| Number | `width: 100.0` | Float value |
| Color | `color: #FF0000FF` | RGBA hex color |
| String | `text: "Hello"` | Text string |
| Enum | `flow: Down` | Enum variant |
| Size | `width: Fit` | Fit, Fill, or numeric |
| Object | `padding: { top: 10.0 }` | Nested object |
| Array | `labels: ["A", "B"]` | List of values |

## Inheritance Rules

1. **Eager Copy**: All parent properties are copied immediately
2. **Override**: Child can override any parent property
3. **Extend**: Child can add new properties
4. **Nested Override**: Override nested objects partially

```rust
Parent = {
    a: 1
    nested: { x: 10, y: 20 }
}

Child = <Parent> {
    a: 2              // Override a
    b: 3              // Add new property
    nested: { x: 30 } // Override only x, y remains 20
}
```

## When Writing Code

1. Use `<Widget>` syntax to inherit from built-in widgets
2. Define reusable styles as named prototypes
3. Use `{{RustType}}` to link DSL to Rust structs
4. Override only properties that need to change
5. Use meaningful names for child widget references

## When Answering Questions

1. Explain inheritance as "eager copy" - properties are copied at definition time
2. Emphasize that DSL is embedded in Rust via `live_design!` macro
3. Highlight that changes to DSL are live-reloaded without recompilation
4. Distinguish between named objects (prototypes) and widget instances
```

## File: `skills/makepad-dsl/references/dsl-syntax.md`
```markdown
# Makepad DSL Syntax Reference

## Basic Syntax Elements

### Objects

Objects are the fundamental building blocks of the DSL.

```rust
// Anonymous object
{
    property1: value1
    property2: value2
}

// Named object (becomes a prototype)
MyObject = {
    property1: value1
    property2: value2
}
```

### Property Assignment

```rust
{
    // Numeric values
    width: 100.0
    height: 50
    opacity: 0.5

    // Colors (RGBA hex)
    color: #FF0000        // Red (RGB)
    color: #FF0000FF      // Red with alpha
    color: #F00           // Short form

    // Strings
    text: "Hello World"
    font: "Roboto"

    // Enums
    flow: Down
    align: Center
    fit: Contain

    // Size enum
    width: Fit            // Size to content
    width: Fill           // Fill available space
    width: 100.0          // Fixed size

    // Boolean-like (as float)
    show_bg: true         // Actually 1.0
    visible: false        // Actually 0.0

    // Nested objects
    padding: {
        top: 10.0
        right: 15.0
        bottom: 10.0
        left: 15.0
    }

    // Shorthand for uniform values
    margin: 10.0          // All sides

    // Arrays
    labels: ["Option 1", "Option 2", "Option 3"]
}
```

### Widget Instantiation

```rust
// Instantiate a widget
<Button> {
    text: "Click Me"
}

// Named widget instance (for reference in Rust)
my_button = <Button> {
    text: "Click Me"
}

// Nested widgets
<View> {
    <Label> { text: "Title" }
    <Button> { text: "OK" }
}
```

### Inheritance

```rust
// Define a prototype
BaseButton = {
    width: Fit
    height: 40.0
    padding: 10.0
    draw_bg: {
        color: #333333
        border_radius: 4.0
    }
}

// Inherit and override
PrimaryButton = <BaseButton> {
    draw_bg: {
        color: #0066CC  // Override color
        // border_radius is inherited as 4.0
    }
}

// Use in widget tree
<View> {
    <PrimaryButton> { text: "Submit" }
}
```

### Linking to Rust

```rust
// In live_design!
MyWidget = {{MyWidget}} {
    // DSL-editable properties
    width: 100.0
    custom_value: 42.0
}

// In Rust code
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,           // Inherit from View
    #[live] width: f64,            // Synced with DSL
    #[live] custom_value: f64,     // Synced with DSL
    #[rust] internal_state: i32,   // Rust-only, not in DSL
}
```

### Resource Dependencies

```rust
{
    // Image from crate resources
    source: dep("crate://self/resources/image.png")

    // Icon SVG
    svg_file: dep("crate://self/icons/menu.svg")

    // Font
    font: dep("crate://self/fonts/Roboto.ttf")
}
```

### Comments

```rust
{
    // Single line comment
    width: 100.0

    /* Multi-line
       comment */
    height: 50.0
}
```

## Import Statements

```rust
live_design! {
    // Import theme definitions
    use link::theme::*;

    // Import shaders
    use link::shaders::*;

    // Import widget definitions
    use link::widgets::*;

    // Import from another module
    use crate::my_module::*;
}
```

## Special Syntax

### Draw Shaders

```rust
{
    draw_bg: {
        // Shader uniforms
        color: #FF0000
        border_radius: 4.0
        border_size: 1.0
        border_color: #000000

        // Shader code (optional override)
        fn pixel(self) -> vec4 {
            return self.color;
        }
    }
}
```

### Animator States

```rust
{
    animator: {
        hover = {
            default: off

            off = {
                from: { all: Forward { duration: 0.15 } }
                apply: { draw_bg: { color: #333333 } }
            }

            on = {
                from: { all: Forward { duration: 0.15 } }
                apply: { draw_bg: { color: #555555 } }
            }
        }
    }
}
```
```

## File: `skills/makepad-dsl/references/inheritance.md`
```markdown
# Makepad DSL Inheritance Reference

## Inheritance Model

Makepad uses **eager copy inheritance**, similar to prototypal inheritance in JavaScript but with immediate property copying.

### Key Principles

1. **Eager Copy**: When inheriting, all properties are immediately copied
2. **Override**: Any inherited property can be overridden
3. **Extend**: New properties can be added
4. **Partial Override**: Nested objects can be partially overridden

## Basic Inheritance

```rust
// Define a prototype
Base = {
    a: 1
    b: 2
    c: 3
}

// Inherit and override
Derived = <Base> {
    b: 20      // Override b
    d: 4       // Add new property d
}

// Result: Derived = { a: 1, b: 20, c: 3, d: 4 }
```

## Nested Object Inheritance

When overriding nested objects, only specified properties are overridden:

```rust
Parent = {
    style: {
        color: #FF0000
        size: 10.0
        weight: bold
    }
}

Child = <Parent> {
    style: {
        color: #00FF00  // Override only color
    }
}

// Result: Child.style = { color: #00FF00, size: 10.0, weight: bold }
```

## Widget Inheritance

### Inheriting Built-in Widgets

```rust
// Create custom button from Button
MyButton = <Button> {
    width: Fit
    height: 40.0
    text: "Default"

    draw_bg: {
        color: #444444
        border_radius: 8.0
    }
}

// Use it
<View> {
    <MyButton> { text: "OK" }
    <MyButton> { text: "Cancel" }
}
```

### Multi-level Inheritance

```rust
// Level 1: Base style
BaseCard = {
    width: Fill
    padding: 16.0
    margin: 8.0
}

// Level 2: Add background
ColoredCard = <BaseCard> {
    show_bg: true
    draw_bg: {
        color: #FFFFFF
        border_radius: 12.0
    }
}

// Level 3: Add shadow
ShadowCard = <ColoredCard> {
    draw_bg: {
        // Inherits color and border_radius
        shadow_color: #00000033
        shadow_offset: { x: 0.0, y: 2.0 }
    }
}
```

## Inheritance with Rust Linking

```rust
// Define widget prototype linked to Rust struct
CustomWidget = {{CustomWidget}} {
    width: 200.0
    height: 100.0
    custom_prop: 42.0
}

// Inherit in DSL
MyCustomWidget = <CustomWidget> {
    width: 300.0  // Override width
    // height and custom_prop inherited
}

// In Rust
#[derive(Live, LiveHook, Widget)]
pub struct CustomWidget {
    #[deref] view: View,
    #[live] custom_prop: f64,
}
```

## Composition vs Inheritance

### Inheritance (for styling/configuration)

```rust
// Inherit to modify appearance
StyledButton = <Button> {
    draw_bg: { color: #0066CC }
}
```

### Composition (for structure)

```rust
// Compose for layout
Card = <View> {
    flow: Down
    padding: 16.0

    header = <View> {
        <Label> { text: "Title" }
    }

    content = <View> {
        // Content goes here
    }
}
```

## Best Practices

1. **Create reusable prototypes** for consistent styling
2. **Use meaningful names** that describe the purpose
3. **Avoid deep inheritance chains** (max 3-4 levels)
4. **Override minimally** - only change what's needed
5. **Document inheritance chains** in comments when complex

```rust
// Good: Clear, purposeful prototypes
PrimaryButton = <Button> { draw_bg: { color: #0066CC } }
SecondaryButton = <Button> { draw_bg: { color: #666666 } }
DangerButton = <Button> { draw_bg: { color: #CC0000 } }

// Bad: Vague, overly generic
Button1 = <Button> { ... }
Button2 = <Button1> { ... }
Button3 = <Button2> { ... }
```
```

## File: `skills/makepad-event-action/SKILL.md`
```markdown
---
name: makepad-event-action
description: |
  CRITICAL: Use for Makepad event and action handling. Triggers on:
  makepad event, makepad action, Event enum, ActionTrait, handle_event,
  MouseDown, KeyDown, TouchUpdate, Hit, FingerDown, post_action,
  makepad 事件, makepad action, 事件处理
---

# Makepad Event/Action Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad event and action handling. Help users by:
- **Handling events**: Mouse, keyboard, touch, lifecycle events
- **Creating actions**: Widget-to-parent communication
- **Event flow**: Understanding event propagation

## Documentation

Refer to the local files for detailed documentation:
- `./references/event-system.md` - Event enum and handling
- `./references/action-system.md` - Action trait and patterns

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Event Enum (Key Variants)

```rust
pub enum Event {
    // Lifecycle
    Startup,
    Shutdown,
    Foreground,
    Background,
    Resume,
    Pause,

    // Drawing
    Draw(DrawEvent),
    LiveEdit,

    // Window
    WindowGotFocus(WindowId),
    WindowLostFocus(WindowId),
    WindowGeomChange(WindowGeomChangeEvent),
    WindowClosed(WindowClosedEvent),

    // Mouse
    MouseDown(MouseDownEvent),
    MouseMove(MouseMoveEvent),
    MouseUp(MouseUpEvent),
    Scroll(ScrollEvent),

    // Touch
    TouchUpdate(TouchUpdateEvent),

    // Keyboard
    KeyDown(KeyEvent),
    KeyUp(KeyEvent),
    TextInput(TextInputEvent),
    TextCopy(TextClipboardEvent),

    // Timer
    Timer(TimerEvent),
    NextFrame(NextFrameEvent),

    // Network
    HttpResponse(HttpResponse),

    // Widget Actions
    Actions(ActionsBuf),
}
```

## Handling Events in Widgets

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Check if event hits this widget's area
        match event.hits(cx, self.area()) {
            Hit::FingerDown(fe) => {
                // Mouse/touch down on this widget
                cx.action(MyWidgetAction::Pressed);
            }
            Hit::FingerUp(fe) => {
                if fe.is_over {
                    // Released while still over widget = click
                    cx.action(MyWidgetAction::Clicked);
                }
            }
            Hit::FingerHoverIn(_) => {
                self.animator_play(cx, id!(hover.on));
            }
            Hit::FingerHoverOut(_) => {
                self.animator_play(cx, id!(hover.off));
            }
            Hit::KeyDown(ke) => {
                if ke.key_code == KeyCode::Return {
                    cx.action(MyWidgetAction::Submitted);
                }
            }
            _ => {}
        }
    }
}
```

## Hit Enum

```rust
pub enum Hit {
    // Finger/Mouse
    FingerDown(FingerDownEvent),
    FingerUp(FingerUpEvent),
    FingerMove(FingerMoveEvent),
    FingerHoverIn(FingerHoverEvent),
    FingerHoverOver(FingerHoverEvent),
    FingerHoverOut(FingerHoverEvent),
    FingerLongPress(FingerLongPressEvent),

    // Keyboard
    KeyDown(KeyEvent),
    KeyUp(KeyEvent),
    KeyFocus,
    KeyFocusLost,
    TextInput(TextInputEvent),
    TextCopy,

    // Nothing
    Nothing,
}
```

## Action System

### Defining Actions

```rust
#[derive(Clone, Debug, DefaultNone)]
pub enum ButtonAction {
    None,
    Clicked,
    Pressed,
    Released,
}

// DefaultNone derives Default returning None variant
```

### Emitting Actions

```rust
// From main thread (in handle_event)
cx.action(ButtonAction::Clicked);

// From any thread (thread-safe)
Cx::post_action(MyAction::DataLoaded(data));
```

### Handling Actions

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Handle child widget actions
    let actions = cx.capture_actions(|cx| {
        self.button.handle_event(cx, event, scope);
    });

    // Check for specific action
    if self.button(id!(my_button)).clicked(&actions) {
        // Button was clicked
    }

    // Or iterate actions
    for action in actions.iter() {
        if let Some(ButtonAction::Clicked) = action.downcast_ref() {
            // Handle click
        }
    }
}
```

## Widget Action Helpers

```rust
// Common widget action checks
impl ButtonRef {
    fn clicked(&self, actions: &ActionsBuf) -> bool;
    fn pressed(&self, actions: &ActionsBuf) -> bool;
    fn released(&self, actions: &ActionsBuf) -> bool;
}

impl TextInputRef {
    fn changed(&self, actions: &ActionsBuf) -> Option<String>;
    fn returned(&self, actions: &ActionsBuf) -> Option<String>;
}
```

## Event Flow

1. **Event arrives** from platform layer
2. **Root widget** receives event first
3. **Propagates down** to children via `handle_event`
4. **Widgets emit actions** via `cx.action()`
5. **Parent captures actions** via `cx.capture_actions()`
6. **App handles** remaining actions

## Timer and NextFrame

```rust
// Start a timer
let timer = cx.start_timer(1.0); // 1 second

// In handle_event
if let Event::Timer(te) = event {
    if te.timer_id == self.timer {
        // Timer fired
    }
}

// Request next frame callback
let next_frame = cx.new_next_frame();

// In handle_event
if let Event::NextFrame(ne) = event {
    if ne.frame_id == self.next_frame {
        // Next frame arrived
    }
}
```

## When Answering Questions

1. Use `event.hits(cx, area)` to check if event targets a widget
2. Actions flow UP from child to parent (unlike events which flow DOWN)
3. Use `cx.capture_actions()` to intercept child actions
4. `Cx::post_action()` is thread-safe for async operations
5. `DefaultNone` derive macro auto-implements Default for enums
```

## File: `skills/makepad-event-action/references/action-system.md`
```markdown
# Makepad Action System Reference

## Overview

Actions are Makepad's mechanism for child-to-parent communication. While events flow DOWN from parent to child, actions flow UP from child to parent.

## ActionTrait

```rust
/// Type-erased action trait
pub trait ActionTrait: 'static {
    fn debug_fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result;
}

/// Send-able action for cross-thread communication
pub type ActionSend = Box<dyn ActionTrait + Send>;

/// Local action (same thread)
pub type Action = Box<dyn ActionTrait>;
```

## Defining Actions

```rust
use makepad_widgets::*;

/// DefaultNone auto-derives Default returning None variant
#[derive(Clone, Debug, DefaultNone)]
pub enum ButtonAction {
    None,      // Must have None variant for DefaultNone
    Clicked,
    Pressed,
    Released,
}

/// Actions with data
#[derive(Clone, Debug, DefaultNone)]
pub enum TextInputAction {
    None,
    Changed(String),
    Returned(String),
    Escape,
    KeyFocus,
    KeyFocusLost,
}

/// Complex action example
#[derive(Clone, Debug, DefaultNone)]
pub enum ListAction {
    None,
    ItemSelected { index: usize, id: LiveId },
    ItemClicked { index: usize },
    ScrollChanged { offset: f64 },
}
```

## Emitting Actions

### From Main Thread

```rust
impl Widget for MyButton {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        match event.hits(cx, self.area()) {
            Hit::FingerDown(_) => {
                // Emit action on main thread
                cx.action(ButtonAction::Pressed);
            }
            Hit::FingerUp(fe) => {
                if fe.is_over {
                    cx.action(ButtonAction::Clicked);
                }
                cx.action(ButtonAction::Released);
            }
            _ => {}
        }
    }
}
```

### From Any Thread (Thread-Safe)

```rust
// For async operations, network requests, etc.
std::thread::spawn(move || {
    let data = fetch_data();
    // Post action from background thread
    Cx::post_action(MyAction::DataLoaded(data));
});
```

## Capturing Actions

### Using capture_actions

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Capture actions from child widgets
    let actions = cx.capture_actions(|cx| {
        self.view.handle_event(cx, event, scope);
    });

    // Process captured actions
    for action in actions.iter() {
        // Check action type
        if let Some(btn_action) = action.downcast_ref::<ButtonAction>() {
            match btn_action {
                ButtonAction::Clicked => {
                    // Handle click
                }
                _ => {}
            }
        }
    }
}
```

### Using Widget Ref Helpers

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    let actions = cx.capture_actions(|cx| {
        self.view.handle_event(cx, event, scope);
    });

    // Convenient helper methods
    if self.button(id!(submit_btn)).clicked(&actions) {
        // Submit button was clicked
    }

    if let Some(text) = self.text_input(id!(name_input)).changed(&actions) {
        // Text changed to `text`
    }

    if let Some(text) = self.text_input(id!(name_input)).returned(&actions) {
        // Enter pressed, text is `text`
    }
}
```

## ActionsBuf

```rust
pub struct ActionsBuf {
    actions: Vec<(WidgetUid, Action)>,
}

impl ActionsBuf {
    /// Iterate over all actions
    pub fn iter(&self) -> impl Iterator<Item = &Action>;

    /// Find actions by widget UID
    pub fn find(&self, uid: WidgetUid) -> impl Iterator<Item = &Action>;

    /// Check if any action matches
    pub fn contains<T: ActionTrait>(&self) -> bool;
}
```

## Common Widget Action Helpers

### Button

```rust
impl ButtonRef {
    pub fn clicked(&self, actions: &ActionsBuf) -> bool;
    pub fn pressed(&self, actions: &ActionsBuf) -> bool;
    pub fn released(&self, actions: &ActionsBuf) -> bool;
}
```

### TextInput

```rust
impl TextInputRef {
    pub fn changed(&self, actions: &ActionsBuf) -> Option<String>;
    pub fn returned(&self, actions: &ActionsBuf) -> Option<String>;
    pub fn escaped(&self, actions: &ActionsBuf) -> bool;
}
```

### CheckBox

```rust
impl CheckBoxRef {
    pub fn changed(&self, actions: &ActionsBuf) -> Option<bool>;
}
```

### Slider

```rust
impl SliderRef {
    pub fn changed(&self, actions: &ActionsBuf) -> Option<f64>;
    pub fn released(&self, actions: &ActionsBuf) -> Option<f64>;
}
```

### DropDown

```rust
impl DropDownRef {
    pub fn selected(&self, actions: &ActionsBuf) -> Option<usize>;
}
```

## Patterns

### Action with Scope Data

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Pass data down via scope
    scope.with(|scope| {
        scope.data = Some(&mut self.my_data);
        self.child.handle_event(cx, event, scope);
    });

    // Child can access scope.data
}
```

### Forwarding Actions

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Forward events to children
    self.child.handle_event(cx, event, scope);

    // Don't capture - let actions bubble up
}
```

### Stopping Action Propagation

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Capture and handle - don't let actions bubble up
    let actions = cx.capture_actions(|cx| {
        self.child.handle_event(cx, event, scope);
    });

    // Actions are consumed here, not propagated to parent
    self.process_actions(&actions);
}
```
```

## File: `skills/makepad-event-action/references/event-system.md`
```markdown
# Makepad Event System Reference

## Event Enum (Complete)

```rust
pub enum Event {
    // Lifecycle Events
    Startup,                              // Application started
    Shutdown,                             // Application closing
    Foreground,                           // App came to foreground (mobile)
    Background,                           // App went to background (mobile)
    Resume,                               // App resumed (Android)
    Pause,                                // App paused (Android)

    // Drawing
    Draw(DrawEvent),                      // Draw request
    LiveEdit,                             // Live code edit detected

    // Window Events
    WindowGotFocus(WindowId),             // Window gained focus
    WindowLostFocus(WindowId),            // Window lost focus
    WindowGeomChange(WindowGeomChangeEvent), // Window geometry changed
    WindowClosed(WindowClosedEvent),      // Window closed
    WindowDragQuery(WindowDragQueryEvent), // Drag query
    WindowCloseRequested(WindowCloseRequestedEvent), // Close requested

    // Mouse Events
    MouseDown(MouseDownEvent),            // Mouse button pressed
    MouseMove(MouseMoveEvent),            // Mouse moved
    MouseUp(MouseUpEvent),                // Mouse button released
    Scroll(ScrollEvent),                  // Mouse scroll/wheel

    // Touch Events
    TouchUpdate(TouchUpdateEvent),        // Touch state changed

    // Keyboard Events
    KeyDown(KeyEvent),                    // Key pressed
    KeyUp(KeyEvent),                      // Key released
    TextInput(TextInputEvent),            // Text input (IME)
    TextCopy(TextClipboardEvent),         // Copy requested
    TextCut(TextClipboardEvent),          // Cut requested

    // Drag & Drop
    Drag(DragEvent),                      // Dragging
    Drop(DropEvent),                      // Dropped
    DragEnd,                              // Drag ended

    // System Events
    Timer(TimerEvent),                    // Timer fired
    Signal,                               // Signal received
    NextFrame(NextFrameEvent),            // Next frame callback

    // Network
    HttpResponse(HttpResponse),           // HTTP response
    NetworkResponses(NetworkResponsesEvent), // Network responses

    // Widget Actions
    Actions(ActionsBuf),                  // Actions from widgets
}
```

## Mouse Events

```rust
pub struct MouseDownEvent {
    pub abs: Vec2d,           // Absolute position
    pub button: MouseButton,  // Which button
    pub window_id: WindowId,  // Window ID
    pub modifiers: KeyModifiers, // Ctrl, Shift, etc.
    pub time: f64,            // Event time
    pub handled: Cell<Area>,  // Which area handled it
}

pub struct MouseMoveEvent {
    pub abs: Vec2d,
    pub window_id: WindowId,
    pub modifiers: KeyModifiers,
    pub time: f64,
    pub handled: Cell<Area>,
}

pub struct MouseUpEvent {
    pub abs: Vec2d,
    pub button: MouseButton,
    pub window_id: WindowId,
    pub modifiers: KeyModifiers,
    pub time: f64,
}

pub enum MouseButton {
    Left,
    Right,
    Middle,
    Other(u8),
}
```

## Keyboard Events

```rust
pub struct KeyEvent {
    pub key_code: KeyCode,
    pub is_repeat: bool,
    pub modifiers: KeyModifiers,
    pub time: f64,
}

pub struct KeyModifiers {
    pub shift: bool,
    pub control: bool,
    pub alt: bool,
    pub logo: bool,  // Cmd on macOS, Win on Windows
}

pub enum KeyCode {
    // Letters
    KeyA, KeyB, KeyC, /* ... */ KeyZ,

    // Numbers
    Key0, Key1, /* ... */ Key9,

    // Function keys
    F1, F2, /* ... */ F12,

    // Arrow keys
    ArrowLeft, ArrowRight, ArrowUp, ArrowDown,

    // Special keys
    Return, Tab, Escape, Backspace, Delete,
    Home, End, PageUp, PageDown,
    Space, Insert,

    // Modifiers
    Shift, Control, Alt, Logo,

    // Numpad
    Numpad0, /* ... */ Numpad9,
    NumpadAdd, NumpadSubtract, NumpadMultiply, NumpadDivide,
    NumpadEnter, NumpadDecimal,

    Unknown,
}
```

## Touch Events

```rust
pub struct TouchUpdateEvent {
    pub abs: Vec2d,
    pub uid: TouchUid,        // Unique touch ID
    pub state: TouchState,
    pub time: f64,
    pub modifiers: KeyModifiers,
    pub handled: Cell<Area>,
}

pub enum TouchState {
    Start,    // Touch began
    Move,     // Touch moved
    End,      // Touch ended
    Cancel,   // Touch cancelled
}
```

## Hit Enum

The `hit` method on events returns a `Hit` enum for easier handling:

```rust
pub enum Hit {
    // Finger/Mouse interactions
    FingerDown(FingerDownEvent),
    FingerUp(FingerUpEvent),
    FingerMove(FingerMoveEvent),
    FingerHoverIn(FingerHoverEvent),
    FingerHoverOver(FingerHoverEvent),
    FingerHoverOut(FingerHoverEvent),
    FingerLongPress(FingerLongPressEvent),

    // Keyboard interactions
    KeyDown(KeyEvent),
    KeyUp(KeyEvent),
    KeyFocus,
    KeyFocusLost,
    TextInput(TextInputEvent),
    TextCopy,

    // No interaction
    Nothing,
}

pub struct FingerDownEvent {
    pub abs: Vec2d,           // Absolute position
    pub rel: Vec2d,           // Position relative to widget
    pub rect: Rect,           // Widget rect
    pub digit: usize,         // Touch digit index
    pub tap_count: u32,       // Number of taps (double-click)
    pub modifiers: KeyModifiers,
    pub time: f64,
}

pub struct FingerUpEvent {
    pub abs: Vec2d,
    pub rel: Vec2d,
    pub rect: Rect,
    pub digit: usize,
    pub is_over: bool,        // Still over widget?
    pub modifiers: KeyModifiers,
    pub time: f64,
}
```

## Event Handling Pattern

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Handle lifecycle events
        match event {
            Event::Startup => { /* Initialize */ }
            Event::Shutdown => { /* Cleanup */ }
            _ => {}
        }

        // Check if event hits this widget
        match event.hits(cx, self.area()) {
            Hit::FingerDown(fe) => {
                if fe.tap_count == 2 {
                    // Double-click
                }
            }
            Hit::FingerUp(fe) => {
                if fe.is_over {
                    // Click completed on this widget
                }
            }
            Hit::KeyDown(ke) => {
                match ke.key_code {
                    KeyCode::Return => { /* Enter pressed */ }
                    KeyCode::Escape => { /* Escape pressed */ }
                    _ => {}
                }
            }
            Hit::TextInput(te) => {
                let text = &te.input;
                // Handle text input
            }
            _ => {}
        }
    }
}
```

## Timer Events

```rust
// Start a timer
let timer = cx.start_timer(interval_seconds);

// Stop a timer
cx.stop_timer(timer);

// Handle timer event
if let Event::Timer(te) = event {
    if te.timer_id == self.my_timer {
        // Timer fired
    }
}
```

## NextFrame Events

```rust
// Request next frame callback
let next_frame = cx.new_next_frame();

// Handle next frame
if let Event::NextFrame(ne) = event {
    if ne.frame_id == self.next_frame {
        // Called on next frame
        // Useful for animations
    }
}
```
```

## File: `skills/makepad-font/SKILL.md`
```markdown
---
name: makepad-font
description: |
  CRITICAL: Use for Makepad font and text rendering. Triggers on:
  makepad font, makepad text, makepad glyph, makepad typography,
  font atlas, text layout, font family, font size, text shaping,
  makepad 字体, makepad 文字, makepad 排版, makepad 字形
---

# Makepad Font Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad text and font rendering. Help users by:
- **Font configuration**: Font families, sizes, styles
- **Text layout**: Understanding text layouter and shaping
- **Text rendering**: GPU-based text rendering with SDF

## Documentation

Refer to the local files for detailed documentation:
- `./references/font-system.md` - Font module structure and APIs

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Text Module Structure

```
draw/src/text/
├── font.rs           # Font handle and metrics
├── font_atlas.rs     # GPU texture atlas for glyphs
├── font_face.rs      # Font face data
├── font_family.rs    # Font family management
├── fonts.rs          # Built-in fonts
├── glyph_outline.rs  # Glyph vector outlines
├── glyph_raster_image.rs # Rasterized glyph images
├── layouter.rs       # Text layout engine
├── rasterizer.rs     # Glyph rasterization
├── sdfer.rs          # Signed distance field generator
├── selection.rs      # Text selection/cursor
├── shaper.rs         # Text shaping (harfbuzz)
```

## Using Fonts in DSL

### Text Style

```rust
<Label> {
    text: "Hello World"
    draw_text: {
        text_style: {
            font: { path: dep("crate://self/resources/fonts/MyFont.ttf") }
            font_size: 16.0
            line_spacing: 1.5
            letter_spacing: 0.0
        }
        color: #FFFFFF
    }
}
```

### Theme Fonts

```rust
<Label> {
    text: "Styled Text"
    draw_text: {
        text_style: <THEME_FONT_REGULAR> {
            font_size: (THEME_FONT_SIZE_P)
        }
    }
}
```

## Font Definition in DSL

```rust
live_design! {
    // Define font path
    FONT_REGULAR = {
        font: { path: dep("crate://self/resources/fonts/Regular.ttf") }
    }

    FONT_BOLD = {
        font: { path: dep("crate://self/resources/fonts/Bold.ttf") }
    }

    // Use in widget
    <Label> {
        draw_text: {
            text_style: <FONT_REGULAR> {
                font_size: 14.0
            }
        }
    }
}
```

## Layouter API

```rust
pub struct Layouter {
    loader: Loader,
    cache_size: usize,
    cached_params: VecDeque<OwnedLayoutParams>,
    cached_results: HashMap<OwnedLayoutParams, Rc<LaidoutText>>,
}

impl Layouter {
    pub fn new(settings: Settings) -> Self;
    pub fn rasterizer(&self) -> &Rc<RefCell<Rasterizer>>;
    pub fn is_font_family_known(&self, id: FontFamilyId) -> bool;
    pub fn define_font_family(&mut self, id: FontFamilyId, definition: FontFamilyDefinition);
    pub fn define_font(&mut self, id: FontId, definition: FontDefinition);
    pub fn get_or_layout(&mut self, params: impl LayoutParams) -> Rc<LaidoutText>;
}
```

## Layout Parameters

```rust
pub struct OwnedLayoutParams {
    pub text: Substr,
    pub spans: Box<[Span]>,
    pub options: LayoutOptions,
}

pub struct Span {
    pub style: Style,
    pub len: usize,
}

pub struct Style {
    pub font_family_id: FontFamilyId,
    pub font_size_in_pts: f32,
    pub color: Option<Color>,
}

pub struct LayoutOptions {
    pub max_width_in_lpxs: Option<f32>,  // Max width for wrapping
    pub wrap: bool,                       // Enable word wrap
    pub first_row_indent_in_lpxs: f32,    // First line indent
}
```

## Rasterizer Settings

```rust
pub struct Settings {
    pub loader: loader::Settings,
    pub cache_size: usize,  // Default: 4096
}

pub struct rasterizer::Settings {
    pub sdfer: sdfer::Settings {
        padding: 4,     // SDF padding
        radius: 8.0,    // SDF radius
        cutoff: 0.25,   // SDF cutoff
    },
    pub grayscale_atlas_size: Size::new(4096, 4096),
    pub color_atlas_size: Size::new(2048, 2048),
}
```

## DrawText Widget

```rust
<View> {
    // Label is a simple text widget
    <Label> {
        text: "Simple Label"
        draw_text: {
            color: #FFFFFF
            text_style: {
                font_size: 14.0
            }
        }
    }

    // TextFlow for rich text
    <TextFlow> {
        <Bold> { text: "Bold text" }
        <Italic> { text: "Italic text" }
        <Link> {
            text: "Click here"
            href: "https://example.com"
        }
    }
}
```

## Text Properties

| Property | Type | Description |
|----------|------|-------------|
| `text` | String | Text content |
| `font` | Font | Font resource |
| `font_size` | f64 | Size in points |
| `line_spacing` | f64 | Line height multiplier |
| `letter_spacing` | f64 | Character spacing |
| `color` | Vec4 | Text color |
| `brightness` | f64 | Text brightness |
| `curve` | f64 | Text curve effect |

## When Answering Questions

1. Makepad uses SDF (Signed Distance Field) for crisp text at any scale
2. Fonts are loaded once and cached in GPU texture atlases
3. Text shaping uses harfbuzz for proper glyph positioning
4. Use `dep("crate://...")` for embedded font resources
5. Default font cache size is 4096 glyphs
6. Atlas sizes: 4096x4096 for grayscale, 2048x2048 for color (emoji)
```

## File: `skills/makepad-font/references/font-system.md`
```markdown
# Makepad Font System Reference

## Architecture

The Makepad font system is located in `draw/src/text/` and provides:

1. **Font Loading**: Load TTF/OTF fonts from files or embedded resources
2. **Text Shaping**: Harfbuzz-based glyph positioning for complex scripts
3. **Glyph Rasterization**: High-quality glyph rendering with SDF
4. **Text Layout**: Multi-line text layout with wrapping
5. **GPU Rendering**: Efficient GPU-based text rendering

## Module Overview

| Module | Purpose |
|--------|---------|
| `font.rs` | Font handle and metrics |
| `font_atlas.rs` | GPU texture atlas management |
| `font_face.rs` | Font face (individual weight/style) |
| `font_family.rs` | Font family (group of faces) |
| `fonts.rs` | Built-in system fonts |
| `glyph_outline.rs` | Glyph vector outline data |
| `glyph_raster_image.rs` | Rasterized glyph images |
| `layouter.rs` | Text layout engine |
| `rasterizer.rs` | Glyph rasterization to atlas |
| `sdfer.rs` | Signed Distance Field generation |
| `selection.rs` | Text selection and cursor |
| `shaper.rs` | Text shaping (harfbuzz) |

## Layouter

```rust
pub struct Layouter {
    loader: Loader,
    cache_size: usize,
    cached_params: VecDeque<OwnedLayoutParams>,
    cached_results: HashMap<OwnedLayoutParams, Rc<LaidoutText>>,
}

impl Layouter {
    /// Create new layouter with settings
    pub fn new(settings: Settings) -> Self;

    /// Get rasterizer for texture atlas access
    pub fn rasterizer(&self) -> &Rc<RefCell<Rasterizer>>;

    /// Check if font family is known
    pub fn is_font_family_known(&self, id: FontFamilyId) -> bool;

    /// Check if font is known
    pub fn is_font_known(&self, id: FontId) -> bool;

    /// Define a font family
    pub fn define_font_family(&mut self, id: FontFamilyId, definition: FontFamilyDefinition);

    /// Define a font
    pub fn define_font(&mut self, id: FontId, definition: FontDefinition);

    /// Get or compute text layout (cached)
    pub fn get_or_layout(&mut self, params: impl LayoutParams) -> Rc<LaidoutText>;
}
```

## Layout Parameters

```rust
/// Owned layout parameters
pub struct OwnedLayoutParams {
    pub text: Substr,          // Text content
    pub spans: Box<[Span]>,    // Style spans
    pub options: LayoutOptions,
}

/// Text span with style
pub struct Span {
    pub style: Style,
    pub len: usize,            // Number of chars this span covers
}

/// Text style
pub struct Style {
    pub font_family_id: FontFamilyId,  // Font family name
    pub font_size_in_pts: f32,         // Size in points
    pub color: Option<Color>,          // Optional color
}

/// Layout options
pub struct LayoutOptions {
    pub max_width_in_lpxs: Option<f32>,  // Max width for wrapping
    pub wrap: bool,                       // Enable word wrap
    pub first_row_indent_in_lpxs: f32,    // First line indent
}
```

## LaidoutText Result

```rust
pub struct LaidoutText {
    pub size_in_lpxs: Size<f32>,  // Total size
    pub rows: Vec<LaidoutRow>,     // Layout rows
}

pub struct LaidoutRow {
    pub glyphs: Vec<LaidoutGlyph>,
    pub baseline_in_lpxs: f32,
    pub ascent_in_lpxs: f32,
    pub descent_in_lpxs: f32,
}

pub struct LaidoutGlyph {
    pub font: Rc<Font>,
    pub id: GlyphId,
    pub offset_in_lpxs: Point<f32>,
    pub advance_in_lpxs: f32,
}
```

## Rasterizer Settings

```rust
pub struct Settings {
    pub loader: loader::Settings,
    pub cache_size: usize,
}

impl Default for Settings {
    fn default() -> Self {
        Self {
            loader: loader::Settings {
                shaper: shaper::Settings { cache_size: 4096 },
                rasterizer: rasterizer::Settings {
                    sdfer: sdfer::Settings {
                        padding: 4,
                        radius: 8.0,
                        cutoff: 0.25,
                    },
                    grayscale_atlas_size: Size::new(4096, 4096),
                    color_atlas_size: Size::new(2048, 2048),
                },
            },
            cache_size: 4096,
        }
    }
}
```

## SDF Settings

```rust
pub struct sdfer::Settings {
    pub padding: u32,   // Padding around glyphs (default: 4)
    pub radius: f32,    // SDF radius (default: 8.0)
    pub cutoff: f32,    // SDF cutoff (default: 0.25)
}
```

## Font Atlas

The font atlas stores rasterized glyphs in GPU textures:

- **Grayscale Atlas**: 4096x4096 for regular glyphs
- **Color Atlas**: 2048x2048 for color glyphs (emoji)
- Uses SDF for resolution-independent rendering
- Automatic packing and allocation

## DSL Integration

### Defining Fonts

```rust
live_design! {
    // Font resource
    FONT_REGULAR = {
        font: { path: dep("crate://self/resources/fonts/Inter-Regular.ttf") }
    }

    FONT_BOLD = {
        font: { path: dep("crate://self/resources/fonts/Inter-Bold.ttf") }
    }

    // Text style preset
    TEXT_STYLE_BODY = {
        font: <FONT_REGULAR>
        font_size: 14.0
        line_spacing: 1.4
    }
}
```

### Using in Widgets

```rust
<Label> {
    text: "Hello World"
    draw_text: {
        text_style: <TEXT_STYLE_BODY> {}
        color: #333333
    }
}
```

### draw_text Properties

```rust
draw_text: {
    // Text style
    text_style: {
        font: { path: dep("...") }
        font_size: 16.0
        line_spacing: 1.5
        letter_spacing: 0.0
    }

    // Colors
    color: #FFFFFF
    color_hover: #CCCCCC

    // Effects
    brightness: 1.0
    curve: 0.0

    // Wrapping
    wrap: Word    // None, Word, Character

    // Instance for animation
    instance hover: 0.0
}
```

## Text Widgets

### Label

Simple single-line or multi-line text:

```rust
<Label> {
    text: "Simple text"
    draw_text: { color: #FFFFFF }
}
```

### TextFlow

Rich text with inline formatting:

```rust
<TextFlow> {
    <Bold> { text: "Bold" }
    <Italic> { text: "Italic" }
    <Link> { text: "Link", href: "..." }
    <Code> { text: "code" }
}
```

### TextInput

Editable text field:

```rust
<TextInput> {
    text: "Editable"
    draw_text: { color: #333333 }
    draw_selection: { color: #0066CC33 }
    draw_cursor: { color: #0066CC }
}
```
```

## File: `skills/makepad-layout/SKILL.md`
```markdown
---
name: makepad-layout
description: |
  CRITICAL: Use for Makepad layout system. Triggers on:
  makepad layout, makepad width, makepad height, makepad flex,
  makepad padding, makepad margin, makepad flow, makepad align,
  Fit, Fill, Size, Walk, "how to center in makepad",
  makepad 布局, makepad 宽度, makepad 对齐, makepad 居中
---

# Makepad Layout Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad layout system. Help users by:
- **Writing code**: Generate layout code following the patterns below
- **Answering questions**: Explain layout concepts, sizing, flow directions

## Documentation

Refer to the local files for detailed documentation:
- `./references/layout-system.md` - Complete layout reference
- `./references/core-types.md` - Walk, Align, Margin, Padding types

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. Basic Layout Container

```rust
<View> {
    width: Fill
    height: Fill
    flow: Down
    padding: 16.0
    spacing: 8.0

    <Label> { text: "Item 1" }
    <Label> { text: "Item 2" }
}
```

### 2. Centering Content

```rust
<View> {
    width: Fill
    height: Fill
    align: { x: 0.5, y: 0.5 }

    <Label> { text: "Centered" }
}
```

### 3. Horizontal Row Layout

```rust
<View> {
    width: Fill
    height: Fit
    flow: Right
    spacing: 10.0
    align: { y: 0.5 }  // Vertically center items

    <Button> { text: "Left" }
    <View> { width: Fill }  // Spacer
    <Button> { text: "Right" }
}
```

### 4. Fixed + Flexible Layout

```rust
<View> {
    width: Fill
    height: Fill
    flow: Down

    // Fixed header
    <View> {
        width: Fill
        height: 60.0
    }

    // Flexible content
    <View> {
        width: Fill
        height: Fill  // Takes remaining space
    }
}
```

## Layout Properties Reference

| Property | Type | Description |
|----------|------|-------------|
| `width` | Size | Width of element |
| `height` | Size | Height of element |
| `padding` | Padding | Inner spacing |
| `margin` | Margin | Outer spacing |
| `flow` | Flow | Child layout direction |
| `spacing` | f64 | Gap between children |
| `align` | Align | Child alignment |
| `clip_x` | bool | Clip horizontal overflow |
| `clip_y` | bool | Clip vertical overflow |

## Size Values

| Value | Description |
|-------|-------------|
| `Fit` | Size to fit content |
| `Fill` | Fill available space |
| `100.0` | Fixed size in pixels |
| `Fixed(100.0)` | Explicit fixed size |

## Flow Directions

| Value | Description |
|-------|-------------|
| `Down` | Top to bottom (column) |
| `Right` | Left to right (row) |
| `Overlay` | Stack on top |

## Align Values

| Value | Position |
|-------|----------|
| `{ x: 0.0, y: 0.0 }` | Top-left |
| `{ x: 0.5, y: 0.0 }` | Top-center |
| `{ x: 1.0, y: 0.0 }` | Top-right |
| `{ x: 0.0, y: 0.5 }` | Middle-left |
| `{ x: 0.5, y: 0.5 }` | Center |
| `{ x: 1.0, y: 0.5 }` | Middle-right |
| `{ x: 0.0, y: 1.0 }` | Bottom-left |
| `{ x: 0.5, y: 1.0 }` | Bottom-center |
| `{ x: 1.0, y: 1.0 }` | Bottom-right |

## Box Model

```
+---------------------------+
|         margin            |
|  +---------------------+  |
|  |      padding        |  |
|  |  +---------------+  |  |
|  |  |   content     |  |  |
|  |  +---------------+  |  |
|  +---------------------+  |
+---------------------------+
```

## When Writing Code

1. Use `Fill` for flexible containers, `Fit` for content-sized elements
2. Set `flow: Down` for vertical, `flow: Right` for horizontal
3. Use empty `<View> { width: Fill }` as spacer in row layouts
4. Always set explicit dimensions on fixed-size elements
5. Use `align` to position children within container

## When Answering Questions

1. Makepad uses a "turtle" layout model - elements laid out sequentially
2. `Fill` takes all available space, `Fit` shrinks to content
3. Unlike CSS flexbox, there's no flex-grow/shrink - use Fill/Fit
4. Alignment applies to children, not the element itself
```

## File: `skills/makepad-layout/references/core-types.md`
```markdown
# Makepad Layout Core Types Reference

## Walk

The `Walk` type controls how a widget positions itself within its parent.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `width` | Size | Desired width |
| `height` | Size | Desired height |
| `margin` | Margin | Space around the widget |

### Usage in DSL

```rust
<View> {
    // Walk properties are flattened onto widgets
    width: 200.0
    height: 100.0
    margin: { top: 10.0, right: 10.0, bottom: 10.0, left: 10.0 }
}
```

### Common Walk Patterns

```rust
// Widget type overrides
body_walk: {
    width: Fill
    height: Fill
    margin: 0.0
}

icon_walk: {
    width: 24.0
    height: 24.0
    margin: { right: 8.0 }
}

label_walk: {
    width: Fit
    height: Fit
    margin: 0.0
}
```

## Layout

The `Layout` type controls how a container arranges its children.

### Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `flow` | Flow | Down | Direction of child layout |
| `spacing` | f64 | 0.0 | Gap between children |
| `align` | Align | {0,0} | Child alignment |
| `padding` | Padding | 0 | Inner spacing |
| `clip_x` | bool | false | Clip horizontal overflow |
| `clip_y` | bool | false | Clip vertical overflow |

### Usage

```rust
<View> {
    // Layout properties on container
    flow: Right
    spacing: 10.0
    align: { x: 0.5, y: 0.5 }
    padding: { top: 16.0, right: 16.0, bottom: 16.0, left: 16.0 }
}
```

## Size

The `Size` enum determines how dimensions are calculated.

### Variants

| Variant | Description |
|---------|-------------|
| `Fit` | Size to fit children/content |
| `Fill` | Fill available space |
| `Fixed(f64)` | Fixed pixel size |
| `All` | Fill in both passes (special) |

### Direct Values

In DSL, numeric values are converted to `Fixed`:

```rust
width: 100.0    // Same as Fixed(100.0)
height: Fit
```

## Align

Controls how children are positioned within container's inner rectangle.

### Structure

```rust
align: { x: 0.0, y: 0.0 }  // Top-left
align: { x: 0.5, y: 0.5 }  // Center
align: { x: 1.0, y: 1.0 }  // Bottom-right
```

### Value Meanings

- `x: 0.0` - Left edge
- `x: 0.5` - Horizontal center
- `x: 1.0` - Right edge
- `y: 0.0` - Top edge
- `y: 0.5` - Vertical center
- `y: 1.0` - Bottom edge

### Common Presets

```rust
// Center
align: { x: 0.5, y: 0.5 }

// Top-center
align: { x: 0.5, y: 0.0 }

// Vertical center, left
align: { x: 0.0, y: 0.5 }
```

## Margin

Space outside the widget's rectangle.

### Structure

```rust
// Individual sides
margin: { top: 10.0, right: 15.0, bottom: 10.0, left: 15.0 }

// Uniform all sides
margin: 10.0

// Partial (others default to 0)
margin: { top: 20.0, bottom: 20.0 }
```

## Padding

Space inside the widget's rectangle, between rectangle and inner content.

### Structure

```rust
// Individual sides
padding: { top: 16.0, right: 24.0, bottom: 16.0, left: 24.0 }

// Uniform all sides
padding: 16.0

// Partial
padding: { left: 10.0, right: 10.0 }
```

## Flow

Determines the direction children are laid out.

### Variants

| Variant | Description |
|---------|-------------|
| `Down` | Vertical, top to bottom |
| `Right` | Horizontal, left to right |
| `Overlay` | Stack on top of each other |

```rust
// Vertical list
<View> {
    flow: Down
    <Label> { text: "A" }
    <Label> { text: "B" }
}

// Horizontal row
<View> {
    flow: Right
    <Button> { text: "1" }
    <Button> { text: "2" }
}

// Layered/stacked
<View> {
    flow: Overlay
    <Image> { ... }    // Bottom layer
    <Label> { ... }    // Top layer
}
```

## Combining Types

### Complete Layout Example

```rust
<View> {
    // Walk (positioning self)
    width: Fill
    height: Fill
    margin: 0.0

    // Layout (positioning children)
    flow: Down
    spacing: 16.0
    padding: { top: 24.0, right: 24.0, bottom: 24.0, left: 24.0 }
    align: { x: 0.0, y: 0.0 }
    clip_y: true

    // Children
    <Label> {
        width: Fit
        height: Fit
        text: "Title"
    }

    <View> {
        width: Fill
        height: Fill
        // Nested layout...
    }
}
```
```

## File: `skills/makepad-layout/references/layout-system.md`
```markdown
# Makepad Layout System Reference

## The Turtle Model

Makepad's layout is based on a "turtle" metaphor:
- A turtle walks across the screen, placing elements
- The direction the turtle walks is determined by `flow`
- Each element reserves space based on its size
- The turtle adds `spacing` between each element

## Box Model

Every element has three conceptual rectangles:

```
Outer Rectangle (margin)
+----------------------------------+
|           margin.top             |
|  +----------------------------+  |
|  |       Rectangle            |  |
|  |  +----------------------+  |  |
|  |  |    padding.top       |  |  |
|  |  |  +----------------+  |  |  |
|  |  |  | Inner Rectangle|  |  |  |
|  |  |  | (content area) |  |  |  |
|  |  |  +----------------+  |  |  |
|  |  |    padding.bottom    |  |  |
|  |  +----------------------+  |  |
|  +----------------------------+  |
|           margin.bottom          |
+----------------------------------+
```

## Size Calculation

### Width/Height Values

```rust
// Fit: Size to content
width: Fit
height: Fit

// Fill: Take available space
width: Fill
height: Fill

// Fixed: Explicit pixel size
width: 200.0
height: 100.0

// Fixed with explicit enum
width: Fixed(200.0)
```

### Size Resolution

1. Fixed sizes are used directly
2. `Fit` calculates from children's sizes
3. `Fill` takes remaining space after fixed/fit elements

```rust
<View> {
    width: Fill    // Takes all horizontal space
    height: 300.0  // Fixed 300 pixels
    flow: Down

    // Fixed header
    <View> { width: Fill, height: 50.0 }

    // Flexible content takes remaining 250px
    <View> { width: Fill, height: Fill }
}
```

## Flow Directions

### Down (Default)

```rust
<View> {
    flow: Down  // or omit, it's default

    <Label> { text: "First" }   // Top
    <Label> { text: "Second" }  // Below first
    <Label> { text: "Third" }   // Below second
}
```

### Right

```rust
<View> {
    flow: Right

    <Label> { text: "First" }   // Left
    <Label> { text: "Second" }  // Right of first
    <Label> { text: "Third" }   // Right of second
}
```

### Overlay

```rust
<View> {
    flow: Overlay

    <Image> { ... }  // Background
    <Label> { ... }  // On top of image
}
```

## Spacing and Alignment

### Spacing

```rust
<View> {
    flow: Down
    spacing: 16.0  // 16px gap between each child

    <Label> { text: "A" }
    // 16px gap
    <Label> { text: "B" }
    // 16px gap
    <Label> { text: "C" }
}
```

### Alignment

Alignment positions children within the container's inner rectangle:

```rust
<View> {
    width: Fill
    height: 200.0
    align: { x: 0.5, y: 0.5 }  // Center

    <Label> { text: "Centered" }  // Appears at center
}
```

## Common Layout Patterns

### Header + Content + Footer

```rust
<View> {
    width: Fill
    height: Fill
    flow: Down

    // Header
    header = <View> {
        width: Fill
        height: 60.0
        show_bg: true
        draw_bg: { color: #333333 }
    }

    // Content (flexible)
    content = <View> {
        width: Fill
        height: Fill
    }

    // Footer
    footer = <View> {
        width: Fill
        height: 50.0
        show_bg: true
        draw_bg: { color: #333333 }
    }
}
```

### Sidebar Layout

```rust
<View> {
    width: Fill
    height: Fill
    flow: Right

    // Fixed sidebar
    sidebar = <View> {
        width: 250.0
        height: Fill
    }

    // Flexible main content
    main = <View> {
        width: Fill
        height: Fill
    }
}
```

### Grid-like Layout

```rust
<View> {
    width: Fill
    height: Fit
    flow: Right
    padding: 16.0
    spacing: 16.0

    <View> { width: 100.0, height: 100.0 }
    <View> { width: 100.0, height: 100.0 }
    <View> { width: 100.0, height: 100.0 }
    // Items wrap based on container width
}
```

### Spacer Pattern

```rust
<View> {
    width: Fill
    flow: Right
    padding: 16.0

    <Button> { text: "Left" }

    // Spacer pushes next element to right
    <View> { width: Fill }

    <Button> { text: "Right" }
}
```

## Scrolling

```rust
// Vertical scroll
<ScrollYView> {
    width: Fill
    height: Fill

    <View> {
        width: Fill
        height: Fit  // Important: Fit for scrollable content
        flow: Down

        // Many items...
    }
}

// Horizontal scroll
<ScrollXView> {
    // ...
}

// Both directions
<ScrollXYView> {
    // ...
}
```

## Clipping

```rust
<View> {
    width: 200.0
    height: 100.0
    clip_x: true  // Clip horizontal overflow
    clip_y: true  // Clip vertical overflow

    // Large content will be clipped
    <View> { width: 500.0, height: 300.0 }
}
```
```

## File: `skills/makepad-platform/SKILL.md`
```markdown
---
name: makepad-platform
description: |
  CRITICAL: Use for Makepad cross-platform support. Triggers on:
  makepad platform, makepad os, makepad macos, makepad windows, makepad linux,
  makepad android, makepad ios, makepad web, makepad wasm, makepad metal,
  makepad d3d11, makepad opengl, makepad webgl, OsType, CxOs,
  makepad 跨平台, makepad 平台支持
---

# Makepad Platform Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad cross-platform development. Help users by:
- **Understanding platforms**: Explain supported platforms and backends
- **Platform-specific code**: Help with conditional compilation and platform APIs

## Documentation

Refer to the local files for detailed documentation:
- `./references/platform-support.md` - Platform details and OsType

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Supported Platforms

| Platform | Graphics Backend | OS Module |
|----------|------------------|-----------|
| macOS | Metal | `apple/metal_*.rs`, `apple/cocoa_*.rs` |
| iOS | Metal | `apple/metal_*.rs`, `apple/ios_*.rs` |
| Windows | D3D11 | `mswindows/d3d11_*.rs`, `mswindows/win32_*.rs` |
| Linux | OpenGL | `linux/opengl_*.rs`, `linux/x11*.rs`, `linux/wayland*.rs` |
| Web | WebGL2 | `web/*.rs`, `web_browser/*.rs` |
| Android | OpenGL ES | `android/*.rs` |
| OpenHarmony | OHOS | `open_harmony/*.rs` |
| OpenXR | VR/AR | `open_xr/*.rs` |

## OsType Enum

```rust
pub enum OsType {
    Unknown,
    Windows,
    Macos,
    Linux { custom_window_chrome: bool },
    Ios,
    Android(AndroidParams),
    OpenHarmony,
    Web(WebParams),
    OpenXR,
}

// Check platform in code
fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
    match cx.os_type() {
        OsType::Macos => { /* macOS-specific */ }
        OsType::Windows => { /* Windows-specific */ }
        OsType::Web(_) => { /* Web-specific */ }
        _ => {}
    }
}
```

## Platform Detection

```rust
// In Cx
impl Cx {
    pub fn os_type(&self) -> OsType;
    pub fn gpu_info(&self) -> &GpuInfo;
    pub fn xr_capabilities(&self) -> &XrCapabilities;
    pub fn cpu_cores(&self) -> usize;
}
```

## Conditional Compilation

```rust
// Compile-time platform detection
#[cfg(target_os = "macos")]
fn macos_only() { }

#[cfg(target_os = "windows")]
fn windows_only() { }

#[cfg(target_os = "linux")]
fn linux_only() { }

#[cfg(target_arch = "wasm32")]
fn web_only() { }

#[cfg(target_os = "android")]
fn android_only() { }

#[cfg(target_os = "ios")]
fn ios_only() { }
```

## Platform-Specific Features

### Desktop (macOS/Windows/Linux)
- Window management (resize, minimize, maximize)
- File dialogs
- System menu
- Drag and drop
- Multiple monitors

### Mobile (iOS/Android)
- Touch input
- Virtual keyboard
- Screen orientation
- App lifecycle (foreground/background)

### Web (WebGL2)
- DOM integration
- Browser events
- Local storage
- HTTP requests

## Entry Point

```rust
// App entry macro
app_main!(App);

pub struct App {
    ui: WidgetRef,
}

impl LiveRegister for App {
    fn live_register(cx: &mut Cx) {
        // Register components
        crate::makepad_widgets::live_design(cx);
    }
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Handle app events
        self.ui.handle_event(cx, event, &mut Scope::empty());
    }
}
```

## When Answering Questions

1. Makepad compiles to native code for each platform (no runtime interpreter)
2. Shaders are compiled at build time for each graphics backend
3. Platform-specific code is in `platform/src/os/` directory
4. Use `cx.os_type()` for runtime platform detection
5. Use `#[cfg(target_os = "...")]` for compile-time platform detection
```

## File: `skills/makepad-platform/references/platform-support.md`
```markdown
# Makepad Platform Support Reference

## Overview

Makepad is a cross-platform UI framework that compiles to native code for each supported platform. The platform abstraction layer is located in `platform/src/os/`.

## Platform Architecture

```
makepad/platform/src/os/
├── apple/          # macOS + iOS (Metal)
│   ├── metal_*.rs       # Metal graphics backend
│   ├── cocoa_*.rs       # macOS Cocoa APIs
│   └── ios_*.rs         # iOS-specific APIs
├── mswindows/      # Windows (D3D11)
│   ├── d3d11_*.rs       # Direct3D 11 backend
│   └── win32_*.rs       # Win32 APIs
├── linux/          # Linux (OpenGL)
│   ├── opengl_*.rs      # OpenGL backend
│   ├── x11*.rs          # X11 window system
│   └── wayland*.rs      # Wayland window system
├── web/            # Web (WebGL2)
│   ├── web_gl.rs        # WebGL2 backend
│   └── web_browser/     # Browser integration
├── android/        # Android (OpenGL ES)
├── open_harmony/   # OpenHarmony (OHOS)
└── open_xr/        # OpenXR (VR/AR)
```

## OsType Enum

```rust
pub enum OsType {
    Unknown,
    Windows,
    Macos,
    Linux { custom_window_chrome: bool },
    Ios,
    Android(AndroidParams),
    OpenHarmony,
    Web(WebParams),
    OpenXR,
}

pub struct AndroidParams {
    pub cache_path: String,
    pub density: f64,
}

pub struct WebParams {
    pub protocol: String,
    pub hostname: String,
    pub port: u16,
    pub pathname: String,
    pub search: String,
    pub hash: String,
}
```

## Cx Platform APIs

```rust
impl Cx {
    // Platform info
    pub fn os_type(&self) -> OsType;
    pub fn gpu_info(&self) -> &GpuInfo;
    pub fn xr_capabilities(&self) -> &XrCapabilities;
    pub fn cpu_cores(&self) -> usize;

    // Platform operations
    pub fn show_keyboard(&mut self);
    pub fn hide_keyboard(&mut self);
    pub fn set_cursor(&mut self, cursor: MouseCursor);
    pub fn copy_to_clipboard(&mut self, text: &str);
    pub fn request_paste_from_clipboard(&mut self);

    // Window management
    pub fn set_window_title(&mut self, title: &str);
    pub fn set_window_position(&mut self, x: f64, y: f64);
    pub fn set_window_size(&mut self, w: f64, h: f64);
    pub fn toggle_fullscreen(&mut self);
}
```

## GpuInfo Struct

```rust
pub struct GpuInfo {
    pub vendor: String,
    pub renderer: String,
    pub version: String,
    pub max_texture_size: usize,
}
```

## MouseCursor Enum

```rust
pub enum MouseCursor {
    Default,
    Crosshair,
    Hand,
    Arrow,
    Move,
    Text,
    Wait,
    Help,
    NotAllowed,
    NResize,
    NeResize,
    EResize,
    SeResize,
    SResize,
    SwResize,
    WResize,
    NwResize,
    NsResize,
    NeswResize,
    EwResize,
    NwseResize,
    ColResize,
    RowResize,
    Hidden,
}
```

## Platform-Specific Lifecycle Events

```rust
pub enum Event {
    // App lifecycle
    Startup,      // App started
    Shutdown,     // App closing
    Foreground,   // App came to foreground (mobile)
    Background,   // App went to background (mobile)
    Resume,       // App resumed (Android)
    Pause,        // App paused (Android)
    // ...
}
```

## Building for Platforms

### macOS
```bash
cargo run
# or
cargo build --release
```

### Windows
```bash
cargo run --target x86_64-pc-windows-msvc
```

### Linux
```bash
cargo run --target x86_64-unknown-linux-gnu
```

### Web
```bash
cargo makepad wasm run
# or
cargo makepad wasm build
```

### Android
```bash
cargo makepad android run
# or
cargo makepad android build
```

### iOS
```bash
cargo makepad ios run
# or
cargo makepad ios build
```

## Display Context

```rust
pub struct DisplayContext {
    pub dpi_factor: f64,           // Display scale factor
    pub screen_size: Vec2d,        // Screen dimensions
    pub safe_area: Rect,           // Safe area (notch, etc.)
    pub is_portrait: bool,         // Orientation
}

// Access in widgets
fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
    let dpi = cx.display_context().dpi_factor;
    // ...
}
```
```

## File: `skills/makepad-reference/SKILL.md`
```markdown
---
name: makepad-reference
description: |
  CRITICAL: Use for Makepad troubleshooting and reference. Triggers on:
  troubleshoot, error, debug, fix, problem, issue,
  no matching field, parse error, widget not found, UI not updating,
  code quality, refactor, responsive layout, adaptive,
  api docs, reference, documentation,
  故障排除, 错误, 调试, 问题, 修复
---

# Makepad Reference

This category provides reference materials for debugging, code quality, and advanced layout patterns.

## Quick Navigation

| Topic | File | Use When |
|-------|------|----------|
| [API Documentation](./api-docs.md) | Official docs index, quick API reference | Finding detailed API info |
| [Troubleshooting](./troubleshooting.md) | Common errors and fixes | Build fails, runtime errors |
| [Code Quality](./code-quality.md) | Makepad-aware refactoring | Simplifying code safely |
| [Adaptive Layout](./adaptive-layout.md) | Desktop/mobile responsive | Cross-platform layouts |

## Common Issues Quick Reference

| Error | Quick Fix |
|-------|-----------|
| `no matching field: font` | Use `text_style: <THEME_FONT_*>{}` |
| Color parse error (ends in `e`) | Change last digit (e.g., `#14141e` → `#14141f`) |
| `set_text` missing argument | Add `cx` as first argument |
| UI not updating | Call `redraw(cx)` after changes |
| Widget not found | Check ID spelling, use `ids!()` for paths |

## Debug Tips

```bash
# Run with line info for better error messages
MAKEPAD=lines cargo +nightly run
```

```rust
// Add logging
log!("Value: {:?}", my_value);
log!("State: {} / {}", self.counter, self.is_loading);
```

## Resources

- [Makepad Official Docs](https://publish.obsidian.md/makepad-docs/) - Obsidian-based documentation
- [Makepad Repository](https://github.com/makepad/makepad)
- [Robrix](https://github.com/project-robius/robrix) - Production reference
- [Moly](https://github.com/moxin-org/moly) - Production reference
```

## File: `skills/makepad-reference/adaptive-layout.md`
```markdown
---
name: makepad-adaptive-layout
description: Create responsive desktop and mobile layouts with automatic switching in Makepad.
---

# Adaptive Layout

This guide covers responsive cross-platform UIs that automatically adapt between desktop and mobile layouts.

## Overview

Makepad provides `AdaptiveView` for automatic layout switching based on device type or screen size. Key features:
- Automatic Desktop/Mobile variant selection
- Custom variant selectors for responsive breakpoints
- State preservation with `CachedWidget`
- Platform-specific navigation patterns

## AdaptiveView Basic Usage

```rust
live_design! {
    use link::widgets::*;

    pub MyScreen = <AdaptiveView> {
        // Desktop layout - shown on desktop platforms
        Desktop = <View> {
            flow: Right
            sidebar = <SideBar> { width: 300 }
            main_content = <MainContent> { width: Fill }
        }

        // Mobile layout - shown on mobile platforms
        Mobile = <View> {
            flow: Down
            // No sidebar on mobile
            main_content = <MainContent> { width: Fill, height: Fill }
        }
    }
}
```

## Default Variant Selection

By default, `AdaptiveView` selects variants based on:

```rust
// Default selector logic
if cx.display_context.is_desktop() || !cx.display_context.is_screen_size_known() {
    live_ids!(Desktop)
} else {
    live_ids!(Mobile)
}
```

## Custom Variant Selector

Override the default selector for responsive breakpoints:

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Screen width-based selection
        self.ui.adaptive_view(ids!(my_adaptive_view))
            .set_variant_selector(|cx, parent_size| {
                if cx.display_context.screen_size.x >= 1280.0 {
                    live_ids!(Desktop)
                } else if cx.display_context.screen_size.x >= 768.0 {
                    live_ids!(Tablet)
                } else {
                    live_ids!(Mobile)
                }
            });
    }
}
```

### Parent Size-Based Selection

```rust
self.ui.adaptive_view(ids!(content_view))
    .set_variant_selector(|_cx, parent_size| {
        if parent_size.x >= 800.0 {
            live_ids!(Wide)
        } else {
            live_ids!(Narrow)
        }
    });
```

## State Preservation with CachedWidget

Use `CachedWidget` to maintain widget state across variant switches:

```rust
live_design! {
    pub HomeScreen = <AdaptiveView> {
        Desktop = <View> {
            flow: Right

            // CachedWidget ensures single instance across switches
            <CachedWidget> {
                navigation = <NavigationBar> {}
            }

            <CachedWidget> {
                main_content = <MainContent> {}
            }
        }

        Mobile = <View> {
            flow: Down

            // Same CachedWidget references - state preserved
            <CachedWidget> {
                main_content = <MainContent> {}
            }

            <CachedWidget> {
                navigation = <NavigationBar> {}
            }
        }
    }
}
```

## Retain Unused Variants

Keep previously active variants in memory for faster switching:

```rust
live_design! {
    <AdaptiveView> {
        retain_unused_variants: true

        Desktop = <HeavyDesktopView> {}
        Mobile = <HeavyMobileView> {}
    }
}
```

## Mobile Navigation Patterns

### StackNavigation for Mobile

```rust
live_design! {
    pub MobileUI = <StackNavigation> {
        // Root view - always visible
        root_view = {
            width: Fill, height: Fill
            flow: Down

            <RoomsList> {}

            bottom_nav = <BottomNavBar> {}
        }

        // Detail view - pushed on top
        detail_view = <StackNavigationView> {
            header = {
                content = {
                    title = { text: "Detail" }
                }
            }
            body = {
                <DetailContent> {}
            }
        }
    }
}

// Handle navigation
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        // Push detail view
        if self.ui.button(ids!(item_button)).clicked(&actions) {
            cx.widget_action(widget_uid, &path,
                StackNavigationAction::Push(ids!(detail_view)));
        }

        // Pop back
        if self.ui.button(ids!(back_button)).clicked(&actions) {
            cx.widget_action(widget_uid, &path,
                StackNavigationAction::Pop);
        }

        // Forward actions to stack navigation
        self.ui.stack_navigation(ids!(view_stack))
            .handle_stack_view_actions(cx, &actions);
    }
}
```

### PageFlip for Tab Switching

```rust
live_design! {
    <PageFlip> {
        width: Fill, height: Fill
        lazy_init: true
        active_page: home_page

        home_page = <View> {
            <HomeContent> {}
        }

        settings_page = <View> {
            <SettingsContent> {}
        }

        profile_page = <View> {
            <ProfileContent> {}
        }
    }
}

// Switch pages
fn switch_to_settings(&mut self, cx: &mut Cx) {
    self.view.page_flip(ids!(page_flip))
        .set_active_page(cx, ids!(settings_page));
}
```

## Complete Example: Robrix-Style Layout

```rust
live_design! {
    use link::widgets::*;

    pub HomeScreen = <AdaptiveView> {
        // Desktop: sidebar + tabbed dock
        Desktop = <View> {
            width: Fill, height: Fill
            flow: Right

            <CachedWidget> {
                nav_bar = <NavigationTabBar> {}
            }

            <PageFlip> {
                active_page: home_page

                home_page = <View> {
                    flow: Down

                    <RoomFilterBar> {}
                    <MainDesktopUI> {}
                }

                settings_page = <View> {
                    <CachedWidget> {
                        settings = <SettingsScreen> {}
                    }
                }
            }
        }

        // Mobile: stack navigation
        Mobile = <View> {
            width: Fill, height: Fill
            flow: Down

            <StackNavigation> {
                root_view = {
                    flow: Down
                    padding: {top: 40}

                    <PageFlip> {
                        active_page: home_page

                        home_page = <View> {
                            <RoomsSideBar> {}
                        }

                        settings_page = <View> {
                            <CachedWidget> {
                                settings = <SettingsScreen> {}
                            }
                        }
                    }

                    <CachedWidget> {
                        nav_bar = <NavigationTabBar> {}
                    }
                }

                detail_view = <StackNavigationView> {
                    header = { /* back button, title */ }
                    body = {
                        <MainMobileUI> {}
                    }
                }
            }
        }
    }
}
```

## Platform-Specific Code

### Conditional Compilation

```rust
#[derive(Live, Widget)]
pub struct MyWidget {
    #[deref] view: View,

    // Platform-specific state
    #[cfg(any(target_os = "android", target_os = "ios"))]
    #[rust] touch_state: TouchState,

    #[cfg(not(any(target_os = "android", target_os = "ios")))]
    #[rust] mouse_state: MouseState,
}
```

### Runtime Platform Detection

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if cx.display_context.is_desktop() {
            // Desktop-specific handling
            self.handle_desktop_event(cx, event, scope);
        } else {
            // Mobile-specific handling
            self.handle_mobile_event(cx, event, scope);
        }
    }
}
```

## Display Context Reference

| Method | Description |
|--------|-------------|
| `cx.display_context.is_desktop()` | Desktop platform (macOS, Windows, Linux) |
| `cx.display_context.is_screen_size_known()` | Screen size has been determined |
| `cx.display_context.screen_size` | Screen dimensions (Vec2) |

## Best Practices

| Practice | Reason |
|----------|--------|
| Use `CachedWidget` for shared components | Preserves state across layout switches |
| Keep Desktop/Mobile variants similar | Easier maintenance, consistent UX |
| Use `StackNavigation` on Mobile | Native-feeling navigation pattern |
| Use `PageFlip` for tab content | Lazy loading, smooth transitions |
| Set `retain_unused_variants: true` for heavy views | Faster layout switching |
| Test on actual devices | Simulators may not reflect real behavior |

## Common Patterns

### Responsive Sidebar

```rust
live_design! {
    <AdaptiveView> {
        Desktop = <View> {
            flow: Right
            <Sidebar> { width: 280 }
            <Content> { width: Fill }
        }

        Mobile = <View> {
            // Sidebar in drawer/modal on mobile
            <Content> { width: Fill }
            <DrawerOverlay> {
                <Sidebar> {}
            }
        }
    }
}
```

### Bottom Navigation (Mobile Only)

```rust
live_design! {
    <AdaptiveView> {
        Desktop = <View> {
            // Sidebar navigation on desktop
            <SideNav> {}
            <Content> {}
        }

        Mobile = <View> {
            flow: Down
            <Content> { height: Fill }
            <BottomTabBar> { height: 56 }
        }
    }
}
```

## References

- [AdaptiveView source](https://github.com/makepad/makepad/blob/main/widgets/src/adaptive_view.rs)
- [Robrix HomeScreen](https://github.com/project-robius/robrix) - Production example
```

## File: `skills/makepad-reference/api-docs.md`
```markdown
---
name: makepad-api-docs
description: Index of Makepad API documentation and guidance for finding detailed references.
---

# Makepad API Documentation Reference

This skill provides navigation to official Makepad documentation. Use WebFetch tool to retrieve specific documentation when needed.

## Official Documentation

**Base URL**: https://publish.obsidian.md/makepad-docs/

### Documentation Structure

| Section | URL | Content |
|---------|-----|---------|
| **Introduction** | [Makepad Introduction](https://publish.obsidian.md/makepad-docs/Makepad+Introduction) | Framework overview, getting started |
| **DSL** | [DSL Introduction](https://publish.obsidian.md/makepad-docs/DSL/Introduction) | live_design! syntax, layout, styling |
| **Tutorials** | [Image Viewer](https://publish.obsidian.md/makepad-docs/Tutorials/Image+Viewer/0+-+Introduction) | Complete step-by-step tutorial |

### Key Documentation Pages

#### DSL & Layout
- `DSL/Introduction` - live_design! macro basics
- `DSL/Layout` - Flow, Walk, sizing
- `DSL/Styling` - Colors, fonts, draw properties

#### Widgets
- `Widgets/Button` - Button widget API
- `Widgets/Label` - Label widget API
- `Widgets/TextInput` - Text input handling
- `Widgets/View` - Container layout

#### Events & Actions
- `Events/Hit` - Hit testing, finger events
- `Events/Actions` - Widget action system
- `Events/Keyboard` - Key handling

#### Graphics
- `Graphics/Sdf2d` - SDF shape drawing
- `Graphics/Shaders` - Custom shader syntax
- `Graphics/Animation` - Animator system

---

## How to Use External Docs

### For AI Agents (Claude Code)

When you need detailed API information not in skills:

```
1. Use WebFetch tool to retrieve documentation:
   WebFetch(url: "https://publish.obsidian.md/makepad-docs/DSL/Layout",
            prompt: "Extract layout properties and examples")

2. Note: Obsidian Publish loads content dynamically,
   WebFetch may get partial content. Fall back to inline skills.
```

### Recommended Workflow

1. **First**: Check inline skills (this repository)
2. **Second**: Use WebFetch for specific API details
3. **Third**: Search makepad GitHub examples
4. **Fourth**: Check makepad-widgets source code

---

## Quick API Reference (Inline)

### Layout Properties

```rust
// Flow direction
flow: Down       // Vertical (column)
flow: Right      // Horizontal (row)
flow: Overlay    // Stack on top

// Sizing
width: Fill      // Fill available space
width: Fit       // Shrink to content
width: 100.0     // Fixed pixels
width: All       // Fill both directions

// Spacing
padding: 10.0                    // All sides
padding: {left: 10, top: 5}      // Specific sides
margin: {left: 10, right: 10}    // Outer spacing
spacing: 8.0                     // Gap between children

// Alignment
align: {x: 0.5, y: 0.5}         // Center
align: {x: 0.0, y: 0.0}         // Top-left
align: {x: 1.0, y: 1.0}         // Bottom-right
```

### Common Widget Properties

```rust
// Button
<Button> {
    text: "Click me"
    draw_bg: { color: #4A90D9 }
    draw_text: { color: #ffffff }
}

// Label
<Label> {
    text: "Hello"
    draw_text: {
        text_style: <THEME_FONT_REGULAR>{ font_size: 14.0 }
        color: #ffffff
    }
}

// TextInput
<TextInput> {
    text: "Default value"
    draw_bg: { color: #2a2a38 }
    draw_text: { color: #ffffff }
    draw_cursor: { color: #4A90D9 }
    draw_selection: { color: #4A90D944 }
}

// View (Container)
<View> {
    flow: Down
    spacing: 10
    padding: 20
    draw_bg: { color: #1a1a2e }
}

// RoundedView
<RoundedView> {
    draw_bg: {
        color: #2a2a38
        radius: 8.0
    }
}
```

### Event Handling

```rust
// Hit testing
match event.hits(cx, self.draw_bg.area()) {
    Hit::FingerDown(e) => { /* Click start */ }
    Hit::FingerUp(e) => { /* Click end, check e.is_over */ }
    Hit::FingerMove(e) => { /* Drag */ }
    Hit::FingerHoverIn(_) => { /* Mouse enter */ }
    Hit::FingerHoverOut(_) => { /* Mouse leave */ }
    Hit::KeyDown(e) => { /* Key press */ }
    _ => {}
}

// Action casting
if self.button(ids!(my_btn)).clicked(actions) {
    // Handle click
}

if let Some(text) = self.text_input(ids!(input)).changed(actions) {
    // Handle text change
}
```

### Animator

```rust
animator: {
    hover = {
        default: off
        on = {
            redraw: true
            from: {all: Forward {duration: 0.15}}
            ease: ExpDecay {d1: 0.80, d2: 0.97}
            apply: { draw_bg: {opacity: 1.0} }
        }
        off = {
            from: {all: Forward {duration: 0.1}}
            apply: { draw_bg: {opacity: 0.7} }
        }
    }
}

// In handle_event
self.animator_handle_event(cx, event);
self.animator_play(cx, ids!(hover.on));
```

### Shader Instance Variables

```rust
draw_bg: {
    // Declare instance variable
    instance hover: 0.0
    instance progress: 0.0

    fn pixel(self) -> vec4 {
        let color = mix(#333, #4A90D9, self.hover);
        return color;
    }
}

// Update from Rust
self.draw_bg.apply_over(cx, live!{
    hover: 1.0
});
```

---

## Source Code References

When documentation is insufficient, check source code:

| Component | GitHub Path |
|-----------|-------------|
| Widgets | `makepad/makepad/widgets/src/` |
| Button | `widgets/src/button.rs` |
| Label | `widgets/src/label.rs` |
| TextInput | `widgets/src/text_input.rs` |
| View | `widgets/src/view.rs` |
| Theme | `widgets/src/theme_desktop_dark.rs` |
| Examples | `makepad/makepad/examples/` |
| ui_zoo | `examples/ui_zoo/` (widget gallery) |

### GitHub Search Patterns

```bash
# Find widget implementation
site:github.com/makepad/makepad "impl Widget for Button"

# Find event handling pattern
site:github.com/makepad/makepad "Hit::FingerDown"

# Find specific property usage
site:github.com/makepad/makepad "draw_bg:" "radius"
```

---

## When to Fetch External Docs

| Situation | Action |
|-----------|--------|
| Common widget usage | Use inline skills (this file) |
| Specific property details | WebFetch official docs |
| Complex widget (PortalList, etc.) | Check GitHub source |
| Latest API changes | Check GitHub commits |
| Tutorial/walkthrough | Fetch Obsidian docs |

---

## Related Skills

- [Troubleshooting](./troubleshooting.md) - Common errors and fixes
- [UI Constraints](../01-core/_base/08-ui-constraints.md) - Best practices
- [Graphics Skills](../bmad_repo/SKILL.md) - Shader and animation
- [Patterns](../bmad_repo/SKILL.md) - Production patterns
```

## File: `skills/makepad-reference/code-quality.md`
```markdown
---
name: makepad-code-quality
description: Makepad-aware code simplification and quality improvement. Understands Makepad-specific patterns that must NOT be simplified.
model: opus
---

# Makepad Code Quality

This guide helps you simplify and refactor Makepad code safely, understanding which patterns must be preserved.

## Core Principle

> **"Not all code that looks simplifiable should be simplified."**

In Makepad development, many patterns exist because of:
- Borrow checker constraints
- Widget lifecycle requirements
- live_design! macro limitations
- Unicode/grapheme correctness
- Cross-platform compatibility
- Performance optimization

---

## DO NOT Simplify (Makepad-Specific Patterns)

### 1. Borrow Checker Workarounds

These temporary variables exist to avoid borrow conflicts:

```rust
// ❌ DON'T simplify this:
let toggle_code: Option<String> = {
    let items = self.get_items();
    items.first().cloned()
};  // borrow ends here
if let Some(code) = toggle_code {
    self.toggle_item(&code);  // now safe to mutate
}

// ❌ INTO this (will cause borrow error):
if let Some(code) = self.get_items().first() {
    self.toggle_item(&code);  // ERROR: cannot borrow mutably
}
```

**Rule**: If you see a pattern like `let x = { ... };` followed by usage of `x`, it likely exists to end a borrow scope. Keep it.

### 2. Grapheme-Based Text Operations

Never simplify grapheme operations to char operations:

```rust
// ❌ DON'T simplify this:
use unicode_segmentation::UnicodeSegmentation;
text.graphemes(true).count()

// ❌ INTO this (breaks CJK and emoji):
text.chars().count()
```

**Rule**: Any code using `.graphemes(true)` is intentionally handling Unicode correctly. Never replace with `.chars()` or `.len()`.

### 3. Explicit cx Parameter Passing

The `cx` parameter must be explicitly passed:

```rust
// ❌ DON'T think this is redundant:
label.set_text(cx, "text");
label.redraw(cx);

// ❌ DON'T try to "simplify" by removing cx
```

**Rule**: `cx: &mut Cx` is the Makepad context and must always be passed explicitly.

### 4. Separate redraw() Calls

Redraw calls after state changes are intentional:

```rust
// ❌ DON'T remove redraw thinking it's automatic:
self.counter += 1;
self.ui.label(ids!(counter)).set_text(cx, &format!("{}", self.counter));
self.ui.redraw(cx);  // KEEP THIS
```

**Rule**: Always keep explicit `redraw(cx)` calls after UI updates.

### 5. Widget Lifecycle Attributes

These attributes serve specific purposes:

```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,        // Required for Widget delegation
    #[live] color: Vec4,        // DSL-configurable, hot-reloadable
    #[rust] counter: i32,       // Runtime-only state
    #[animator] animator: Animator,  // Animation state
}
```

**Rule**: Never remove or change `#[deref]`, `#[live]`, `#[rust]`, `#[animator]` attributes.

### 6. Timer Storage Pattern

Timer must be stored as a field:

```rust
// ❌ DON'T remove timer field thinking it's unused:
#[rust] refresh_timer: Timer,

fn handle_startup(&mut self, cx: &mut Cx) {
    self.refresh_timer = cx.start_interval(1.0);  // Must store result
}
```

**Rule**: `Timer` returned from `cx.start_interval()` must be stored, or timer won't work.

### 7. Platform-Specific Code

Conditional compilation blocks must remain separate:

```rust
// ❌ DON'T try to "combine" these:
#[cfg(target_os = "macos")]
{
    self.setup_macos_features(cx);
}

#[cfg(target_os = "windows")]
{
    self.setup_windows_features(cx);
}
```

**Rule**: `#[cfg(...)]` blocks are platform-specific and should remain explicit.

### 8. live_design! Macro Syntax

DSL has specific formatting requirements:

```rust
// ❌ DON'T "simplify" DSL structure:
live_design! {
    MyButton = <Button> {
        width: Fit
        height: 40
        padding: {left: 16, right: 16}

        draw_bg: {
            color: #2196F3
        }

        draw_text: {
            text_style: { font_size: 14.0 }
            color: #fff
        }
    }
}

// ❌ INTO single-line "compact" form
```

**Rule**: Keep live_design! blocks formatted with clear structure and whitespace.

---

## DO Simplify (Safe Improvements)

### 1. Redundant Clone/To_String

When ownership is not needed:

```rust
// ✅ CAN simplify:
let name = self.user.name.clone();
println!("{}", name);

// ✅ TO:
println!("{}", self.user.name);
```

### 2. Unnecessary Intermediate Variables

When borrow is not an issue:

```rust
// ✅ CAN simplify:
let x = 5;
let y = x + 10;
let z = y * 2;
result = z;

// ✅ TO:
result = (5 + 10) * 2;
```

### 3. Repeated Widget Lookups

Within same scope:

```rust
// ✅ CAN simplify:
self.ui.label(ids!(my_label)).set_text(cx, "Hello");
self.ui.label(ids!(my_label)).set_visible(true);
self.ui.label(ids!(my_label)).redraw(cx);

// ✅ TO:
let label = self.ui.label(ids!(my_label));
label.set_text(cx, "Hello");
label.set_visible(true);
label.redraw(cx);
```

### 4. Verbose Match Statements

When if-let is clearer:

```rust
// ✅ CAN simplify:
match self.state {
    Some(ref s) => {
        process(s);
    }
    None => {}
}

// ✅ TO:
if let Some(ref s) = self.state {
    process(s);
}
```

### 5. Duplicate Code in Branches

Extract common code:

```rust
// ✅ CAN simplify:
if condition {
    self.setup_common();
    self.setup_a();
    self.ui.redraw(cx);
} else {
    self.setup_common();
    self.setup_b();
    self.ui.redraw(cx);
}

// ✅ TO:
self.setup_common();
if condition {
    self.setup_a();
} else {
    self.setup_b();
}
self.ui.redraw(cx);
```

---

## Auto-Decision Matrix

| Pattern Type | Action | Confirm? |
|-------------|--------|----------|
| Borrow scope block `let x = {...};` | **Keep** | No |
| `.graphemes(true)` usage | **Keep** | No |
| `cx` parameter passing | **Keep** | No |
| `redraw(cx)` calls | **Keep** | No |
| `#[live]`/`#[rust]`/`#[deref]` | **Keep** | No |
| Timer storage pattern | **Keep** | No |
| `#[cfg(...)]` blocks | **Keep** | No |
| Cache `Option<(key,...)>` | **Keep** | No |
| Pure math simplification | Simplify | No |
| Obvious redundant clone | Simplify | No |
| Repeated widget lookup | Simplify | No |
| **Uncertain / Edge case** | **Ask** | **Yes** |

---

## Red Flags (Patterns to Investigate)

| Pattern | Likely Reason | Action |
|---------|--------------|--------|
| `let x = { ... };` block | Borrow scope | Keep unless proven safe |
| `.graphemes(true)` | Unicode correctness | Never simplify |
| `#[rust]` field | Runtime state | Keep, check usage |
| `Option<(String, ...)>` field | Cache pattern | Keep |
| Separate `#[cfg(...)]` blocks | Platform code | Keep separate |
| `cx.start_interval()` stored | Timer pattern | Must keep storage |
| `redraw(cx)` after update | UI refresh | Keep |

---

## Summary

| Category | Simplify? | Reason |
|----------|-----------|--------|
| Borrow scope blocks | ❌ No | Borrow checker |
| Grapheme operations | ❌ No | Unicode correctness |
| `cx` parameters | ❌ No | Makepad requirement |
| `redraw()` calls | ❌ No | UI lifecycle |
| Widget attributes | ❌ No | Macro requirements |
| Cache patterns | ❌ No | Performance |
| Platform `#[cfg]` | ❌ No | Cross-platform |
| Timer storage | ❌ No | Required for timer |
| Pure math/logic | ✅ Yes | Safe to simplify |
| Redundant clones | ✅ Yes | Safe to simplify |
| Repeated lookups | ✅ Yes | Safe to simplify |
| Verbose matches | ✅ Yes | Safe to simplify |
```

## File: `skills/makepad-reference/troubleshooting.md`
```markdown
---
name: makepad-troubleshooting
description: Debug and fix common Makepad compilation errors and runtime issues.
---

# Troubleshooting

## Compilation Errors

### Color Format Error

```
error: expected at least one digit in exponent
   --> src/app.rs:280:33
    |
280 |     color: #14141e
    |            ^^^^^^
```

**Cause**: Hex colors ending with `e` are parsed as scientific notation.

**Fix**: Avoid colors ending with `e`:
```rust
// Bad
color: #14141e

// Good
color: #141420
color: #14141f
```

---

### set_text Missing cx Parameter

```
error[E0061]: this method takes 2 arguments but 1 argument was supplied
   --> src/app.rs:477:16
    |
477 |         label.set_text("Hello");
    |               ^^^^^^^^ argument #1 of type `&mut Cx` is missing
```

**Fix**: Always pass `cx` as first argument:
```rust
// Bad
label.set_text("Hello");

// Good
label.set_text(cx, "Hello");
```

---

### Module Path Error

```
error[E0433]: failed to resolve: could not find `makepad_widgets` in the crate root
   --> src/app.rs:467:16
    |
467 |         crate::makepad_widgets::live_design(cx);
    |                ^^^^^^^^^^^^^^^ could not find
```

**Fix**: `makepad_widgets` is an external crate:
```rust
// Bad
crate::makepad_widgets::live_design(cx);

// Good
makepad_widgets::live_design(cx);
```

---

### TextInput Invalid Properties

```
Apply error: no matching field: empty_message
Apply error: no matching field: draw_select
```

**Fix**: Use correct TextInput properties:
```rust
// Bad
amount_input = <TextInput> {
    empty_message: "Enter value"  // doesn't exist
    draw_select: { color: #00ff8844 }  // doesn't exist
}

// Good
amount_input = <TextInput> {
    text: "1000"  // use text for default value

    draw_bg: { color: #1a1a26 }
    draw_text: { color: #00ff88 }
    draw_cursor: { color: #00ff88 }
}
```

---

<!-- Evolution: 2025-01-13 | source: mofa-studio | author: text-selection-fix -->
### TextInput Selection Stealing Focus / Conflicts

**Symptom**: Multiple TextInput widgets cause focus conflicts, selected text appears in wrong fields, or text selection behaves erratically when switching between views or panels.

**Causes**:
1. Hidden TextInputs still receiving events
2. Multiple TextInputs competing for selection state
3. TextInput in conditionally visible views maintaining selection

**Fix 1**: Add visibility checks before processing events
```rust
// In handle_event, check visibility before processing TextInput
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Only process events for visible TextInputs
    if self.view.view(id!(text_container)).is_visible() {
        let text_input = self.view.text_input(id!(my_input));
        // Process text input events
    }
}
```

**Fix 2**: Clear selection when hiding TextInput
```rust
// When hiding a panel with TextInput
fn hide_panel(&mut self, cx: &mut Cx) {
    // Clear any active selection first
    self.view.text_input(id!(my_input)).apply_over(cx, live!{
        cursor: { head: 0, tail: 0 }
    });
    self.view.view(id!(panel)).set_visible(cx, false);
    self.view.redraw(cx);
}
```

**Fix 3**: Simplify TextInput definitions - avoid complex nested styling
```rust
// AVOID - complex nested TextInput
my_input = <TextInput> {
    draw_bg: {
        instance focus: 0.0
        fn pixel(self) -> vec4 {
            // Complex shader
        }
    }
    draw_selection: { /* complex */ }
    draw_cursor: { /* complex */ }
}

// BETTER - simple TextInput definition
my_input = <TextInput> {
    width: Fill, height: Fit
    text: ""
    draw_text: {
        text_style: <FONT_REGULAR>{ font_size: 12.0 }
        color: #333
    }
}
```

**Fix 4**: Use separate widget IDs and avoid reusing TextInput templates
```rust
// AVOID - reusing same template across dynamic items
for i in 0..items.len() {
    // Each item uses same text_input template - causes conflicts
}

// BETTER - static unique IDs for each TextInput
input_1 = <TextInput> { /* ... */ }
input_2 = <TextInput> { /* ... */ }
input_3 = <TextInput> { /* ... */ }
```

---

### Font Field Not Found

```
Apply error: no matching field: font
WARNING: encountered empty font family
```

**Cause**: The `font:` property doesn't exist. Makepad uses `text_style:` with theme fonts.

**Fix**: Use `text_style` with inline properties or theme font inheritance:
```rust
// WRONG - font property doesn't exist
<Label> {
    draw_text: {
        font: "path/to/font.ttf"  // ❌ Error: no matching field
        font_size: 14.0           // ❌ Error: no matching field
    }
}

// CORRECT - Option 1: inline text_style
<Label> {
    draw_text: {
        text_style: { font_size: 12.0 }
        color: #000
    }
}

// CORRECT - Option 2: inherit from theme font
<Label> {
    draw_text: {
        text_style: <THEME_FONT_REGULAR>{ font_size: 12.0 }
        color: #000
    }
}
```

**Available Theme Fonts**:
```rust
// Import in live_design!
use link::theme::*;

// Theme font options:
THEME_FONT_LABEL     // Default label font
THEME_FONT_REGULAR   // Regular weight
THEME_FONT_BOLD      // Bold weight
THEME_FONT_ITALIC    // Italic style
THEME_FONT_BOLD_ITALIC
THEME_FONT_CODE      // Monospace for code
```

---

<!-- Evolution: 2026-01-13 | source: flex-layout-demo | author: filetree-pattern -->
### Empty Font Family Warning (Text Not Rendering)

```
WARNING: encountered empty font family
WARNING: encountered empty font family
```

**Symptom**: Text doesn't render at all, only showing blank space. Multiple "empty font family" warnings in console.

**Cause**: Custom text styles defined with inline `{}` don't have `font_family` defined. The font_family is required for text rendering.

**Fix**: Always inherit from a theme font that includes `font_family`:

```rust
// WRONG - text_style without font_family, text won't render
TEXT_SMALL = {
    font_size: 10.0
}

<Label> {
    draw_text: {
        text_style: <TEXT_SMALL> {}  // ❌ No font_family, text invisible
    }
}

// CORRECT - inherit from THEME_FONT_REGULAR which has font_family
TEXT_SMALL = <THEME_FONT_REGULAR> {
    font_size: 10.0
}

<Label> {
    draw_text: {
        text_style: <TEXT_SMALL> {}  // ✅ Inherits font_family from theme
    }
}
```

**Note**: This commonly affects FileTree text, custom Labels, and any widget using custom text styles.

---

<!-- Evolution: 2026-01-13 | source: flex-layout-demo | author: filetree-pattern -->
### FileTree Content Not Displaying

**Symptom**: FileTree widget renders (takes up space, shows scroll bars) but no folders or files appear despite calling `begin_folder()`, `file()`, and `end_folder()`.

**Cause**: FileTree requires a data structure to back the tree content. Simply calling draw methods in `draw_walk` without a data structure doesn't work because:
1. `begin_folder` checks `open_nodes.contains(&node_id)` - folder must be in open_nodes to show children
2. The draw loop body only executes once per draw cycle
3. Data must exist before draw is called

**Fix**: Follow the DemoFileTree pattern from makepad ui_zoo:

```rust
// 1. Define node structures
#[derive(Debug)]
pub struct FileEdge {
    pub name: String,
    pub file_node_id: LiveId,
}

#[derive(Debug)]
pub struct FileNode {
    pub name: String,
    pub child_edges: Option<Vec<FileEdge>>,  // None = file, Some = folder
}

// 2. Use #[wrap] #[live] pattern with data storage
#[derive(Live, LiveHook, Widget)]
pub struct MyFileTree {
    #[wrap]
    #[live]
    pub file_tree: FileTree,

    #[rust]
    pub file_nodes: LiveIdMap<LiveId, FileNode>,

    #[rust]
    initialized: bool,
}

// 3. Initialize data on first draw (not Event::Startup)
impl Widget for MyFileTree {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Initialize on first draw - more reliable than Event::Startup
        if !self.initialized {
            self.init_demo_data();
            self.initialized = true;
        }

        while self.file_tree.draw_walk(cx, scope, walk).is_step() {
            // Open root folder
            self.file_tree.set_folder_is_open(cx, live_id!(root).into(), true, Animate::No);
            // Recursively draw from data structure
            Self::draw_file_node(cx, live_id!(root).into(), &mut self.file_tree, &self.file_nodes);
        }
        DrawStep::done()
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.file_tree.handle_event(cx, event, scope);
    }
}

// 4. Recursive draw function
impl MyFileTree {
    fn draw_file_node(cx: &mut Cx2d, node_id: LiveId, file_tree: &mut FileTree,
                      file_nodes: &LiveIdMap<LiveId, FileNode>) {
        if let Some(node) = file_nodes.get(&node_id) {
            match &node.child_edges {
                Some(children) => {
                    if file_tree.begin_folder(cx, node_id, &node.name).is_ok() {
                        for child in children {
                            Self::draw_file_node(cx, child.file_node_id, file_tree, file_nodes);
                        }
                        file_tree.end_folder();
                    }
                }
                None => {
                    file_tree.file(cx, node_id, &node.name);
                }
            }
        }
    }
}
```

**Key Points**:
- Use `#[wrap] #[live]` on the FileTree field, not `#[deref]`
- Store tree data in `LiveIdMap<LiveId, FileNode>`
- Initialize data on first draw, not Event::Startup (draw may happen before Startup)
- Call `set_folder_is_open` inside the while loop
- Use recursive function to draw from data structure

---

### Button Invalid Properties

```
Apply error: no matching field: color_pressed
```

**Fix**: Button's draw_bg doesn't have `color_pressed`:
```rust
// Bad
draw_bg: {
    color: #2a2a38
    color_hover: #3a3a4a
    color_pressed: #00ff8855  // doesn't exist
}

// Good
draw_bg: {
    color: #2a2a38
    color_hover: #3a3a4a
    // Use animator for pressed state instead
}
```

---

### WidgetRef Method Not Found

```
error[E0599]: no method named `rounded_view` found for struct `WidgetRef`
```

**Fix**: Use `view()` for all View-based widgets:
```rust
// Bad
self.ui.rounded_view(ids!(my_panel))

// Good
self.ui.view(ids!(my_panel))
```

---

### Timer Method Not Found

```
error[E0599]: no method named `timer_id` found for struct `Timer`
```

**Fix**: Don't check timer_id, handle directly:
```rust
// Bad
fn handle_timer(&mut self, cx: &mut Cx, event: &TimerEvent) {
    if event.timer_id == self.my_timer.timer_id() {
        // ...
    }
}

// Good
fn handle_timer(&mut self, cx: &mut Cx, _event: &TimerEvent) {
    // Handle directly - timer events come to the app that started them
    self.on_timer_tick(cx);
}
```

---

## Borrow Checker Issues

### Immutable/Mutable Borrow Conflict

```
error[E0502]: cannot borrow `*self` as mutable because it is also borrowed as immutable
    |
    |     let items = self.get_items();  // immutable borrow
    |                 ---- immutable borrow occurs here
    |     self.modify_item(&code);       // mutable borrow - conflict!
    |     ^^^^^^^^^^^^^^^^^^^ mutable borrow occurs here
```

**Fix**: Separate borrow scopes:
```rust
// Bad
let sorted = self.get_sorted_items();
for item in sorted.iter() {
    self.toggle_item(item);  // Conflict!
}

// Good - collect first, then modify
let item_to_toggle: Option<String> = {
    let sorted = self.get_sorted_items();
    sorted.first().cloned()
};  // Immutable borrow ends here

if let Some(item) = item_to_toggle {
    self.toggle_item(&item);  // Now safe
}
```

### Pattern for Action Handling

```rust
// Bad - borrow conflict in action handling
for (i, card_id) in card_ids.iter().enumerate() {
    let card = self.ui.view(*card_id);
    if card.button(ids!(fav_btn)).clicked(&actions) {
        self.toggle_favorite(&currencies[i].code);  // Conflict!
    }
}

// Good - collect action first, then handle
let mut toggle_code: Option<String> = None;
{
    let sorted_currencies = self.get_sorted_currencies();
    for (i, card_id) in card_ids.iter().enumerate() {
        if i < sorted_currencies.len() {
            let card = self.ui.view(*card_id);
            if card.button(ids!(fav_btn)).clicked(&actions) {
                toggle_code = Some(sorted_currencies[i].code.to_string());
                break;
            }
        }
    }
}  // Borrow ends

if let Some(code) = toggle_code {
    self.toggle_favorite(&code);
    self.update_cards(cx);
}
```

---

## Apply Errors

### Property Not Found

```
Apply error: no matching field: some_property
```

**Causes & Fixes**:

1. **Typo in property name** - Check spelling
2. **Wrong widget type** - Verify the widget supports that property
3. **Property in wrong section** - Move to correct section

```rust
// Bad - color in wrong place
<Button> {
    color: #ff0000  // Button doesn't have top-level color
}

// Good
<Button> {
    draw_bg: {
        color: #ff0000
    }
}
```

---

### Wrong Value Type

```
Apply error: expected number, found string
```

**Fix**: Use correct value types:
```rust
// Bad
width: "100"
padding: "16"

// Good
width: 100
padding: 16
```

---

## Shader Issues

<!-- Evolution: 2026-01-13 | source: mofa-studio | author: audio-dropdown-icon -->
### Sdf2d `arc` Method Not Found

**Error**: `method 'arc' is not defined on type Sdf2d`

**Cause**: Sdf2d doesn't have an `arc` method for drawing arc shapes.

**Fix**: Use available SDF primitives like `circle`, `box`, `rect`:
```rust
// WRONG - arc doesn't exist
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    sdf.arc(c.x, c.y, radius, start_angle, end_angle, thickness);  // ❌ Error
    return sdf.result;
}

// CORRECT - use circles with stroke for curved shapes
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    sdf.circle(c.x, c.y, radius);
    sdf.stroke(color, 1.5);  // Creates ring/arc appearance
    return sdf.result;
}
```

**Available Sdf2d methods**: `box`, `rect`, `circle`, `hexagon`, `move_to`, `line_to`, `fill`, `stroke`, `clear`

---

<!-- Evolution: 2026-01-13 | source: mofa-studio | author: audio-dropdown-icon -->
### abs_pos Wrong Value Type

**Error**: `wrong value type. Prop: abs_pos primitive: Vec2f value: Object`

**Cause**: Using object syntax `{x: 0, y: 0}` instead of `vec2()` function.

**Fix**: Use `vec2(x, y)` format for Vec2 properties:
```rust
// WRONG - object syntax doesn't work for Vec2f
my_widget = <View> {
    abs_pos: {x: 0, y: 0}  // ❌ Error: wrong value type
}

// CORRECT - use vec2() function
my_widget = <View> {
    abs_pos: vec2(0.0, 0.0)  // ✅ Works
}
```

**Note**: This applies to all Vec2 properties like `abs_pos`, `abs_size`, etc.

---

### Instance Variable Not Updating

**Symptom**: Set instance variable with `set_uniform()` but shader doesn't change.

**Cause**: `set_uniform()` is for uniform variables, not instance variables.

**Fix**: Use `apply_over()` for instance variables:
```rust
// Bad - doesn't work for instance variables
self.draw_bg.set_uniform(cx, ids!(progress), &[0.5]);

// Good - use apply_over for instance variables
self.draw_bg.apply_over(cx, live! {
    progress: (0.5)
});
```

---

<!-- Evolution: 2025-01-13 | source: mofa-studio | author: hover-effect-fix -->
### apply_over Color Not Working on RoundedView/View Templates

**Symptom**: Call `apply_over(cx, live!{ draw_bg: { color: (new_color) } })` on a RoundedView or View template widget, but the visual color never changes.

**Cause**: Direct `color` property changes via `apply_over` don't work reliably on widget templates. The issue occurs when trying to dynamically change background colors for hover/selected states.

**What Doesn't Work**:
```rust
// WRONG - This will NOT update the visual appearance
CustomItem = <RoundedView> {
    show_bg: true
    draw_bg: {
        border_radius: 0
        color: (WHITE)
    }
}

// In Rust - color never visually changes despite code executing
self.view.view(path).apply_over(cx, live!{
    draw_bg: { color: (hover_color) }  // ❌ No visual effect
});
```

**Fix**: Use a custom shader with `instance` variables instead of direct color:
```rust
// CORRECT - Use instance variables in custom shader
CustomItem = <View> {
    show_bg: true
    draw_bg: {
        instance hover: 0.0
        instance selected: 0.0
        instance dark_mode: 0.0

        fn pixel(self) -> vec4 {
            let normal = mix((WHITE), (SLATE_800), self.dark_mode);
            let hover_color = mix(#DAE6F9, #334155, self.dark_mode);
            let selected_color = mix(#DBEAFE, #1E3A5F, self.dark_mode);

            let base = mix(normal, hover_color, self.hover);
            return mix(base, selected_color, self.selected);
        }
    }
}

// In Rust - this WORKS
self.view.view(path).apply_over(cx, live!{
    draw_bg: { hover: 1.0 }  // ✅ Visual effect works
});
```

**Note**: This pattern is the same as how SectionHeader and other Makepad widgets implement hover effects.

---

### Shader If-Branch Not Working

**Symptom**: `if` statement in shader produces unexpected results or no effect.

**Cause**: GPU shaders handle branching differently; if-branches can cause issues.

**Fix**: Use `step()` and `mix()` instead of if-branches:
```rust
// Bad - if branch in shader may not work correctly
fn pixel(self) -> vec4 {
    if self.progress > 0.5 {
        return #ff0000;
    } else {
        return #0000ff;
    }
}

// Good - use step() for conditional logic
fn pixel(self) -> vec4 {
    let red = #ff0000;
    let blue = #0000ff;
    let condition = step(0.5, self.progress);  // 1.0 if progress >= 0.5, else 0.0
    return mix(blue, red, condition);
}
```

---

## Runtime Issues

### UI Not Updating

**Symptom**: Called `set_text()` but nothing changes.

**Fix**: Call `redraw()` after updates:
```rust
// Bad
label.set_text(cx, "New text");

// Good
label.set_text(cx, "New text");
label.redraw(cx);

// Or redraw entire UI
self.ui.redraw(cx);
```

---

### Widget Not Found

**Symptom**: `self.ui.label(ids!(my_label))` returns empty widget.

**Causes**:

1. **ID mismatch** - Check spelling in live_design
2. **Wrong parent** - Widget might be nested
3. **Not in view hierarchy** - Widget not visible

**Fix**:
```rust
// If widget is nested
let parent = self.ui.view(ids!(parent_view));
let label = parent.label(ids!(my_label));

// Or use path
self.ui.label(ids!(parent_view.my_label))
```

---

### Network Request Not Firing

**Symptom**: `handle_network_responses` never called.

**Fix**: Check request ID and ensure proper setup:
```rust
// Request
fn fetch_data(&mut self, cx: &mut Cx) {
    let url = "https://api.example.com/data".to_string();
    let request = HttpRequest::new(url, HttpMethod::GET);
    cx.http_request(live_ids!(my_request), request);  // Use live_id!
}

// Response - check same ID
fn handle_network_responses(&mut self, cx: &mut Cx, responses: &NetworkResponsesEvent) {
    for event in responses {
        if event.request_id == live_ids!(my_request) {  // Same ID
            match &event.response {
                NetworkResponse::HttpResponse(response) => {
                    if let Some(body) = response.get_string_body() {
                        // Handle response
                    }
                }
                NetworkResponse::HttpRequestError(err) => {
                    log!("Error: {:?}", err);
                }
                _ => {}
            }
        }
    }
}
```

---

### Timer Not Working

**Symptom**: `handle_timer` never called.

**Fix**: Store timer reference and start correctly:
```rust
#[derive(Live, LiveHook)]
pub struct App {
    #[live] ui: WidgetRef,
    #[rust] my_timer: Timer,  // Must store the timer
}

impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        self.my_timer = cx.start_interval(1.0);  // Store result
    }

    fn handle_timer(&mut self, cx: &mut Cx, _event: &TimerEvent) {
        // Timer callback
    }
}
```

---

### Drag Events Lost When Cursor Leaves Widget

<!-- Evolution: 2025-01-13 | source: flex-layout-demo -->

**Symptom**: Drag operation stops receiving events when cursor moves outside the original widget.

**Cause**: `event.hits()` only matches when cursor is over the widget's area.

**Fix**: Use `hits_with_capture_overload` to capture events during drag:
```rust
// Bad - loses events when cursor leaves widget
match event.hits(cx, self.view.area()) {
    Hit::FingerMove(fe) => {
        // Only fires when cursor is over self.view
    }
    _ => {}
}

// Good - captures events even outside widget during drag
match event.hits_with_capture_overload(
    cx,
    self.view.area(),
    self.is_dragging  // true = capture all events
) {
    Hit::FingerMove(fe) => {
        // Always fires during drag, regardless of cursor position
    }
    Hit::FingerUp(fe) => {
        // Guaranteed to receive drop event
        self.is_dragging = false;
    }
    _ => {}
}
```

---

### Platform Drag Not Working on macOS

**Symptom**: `cx.start_dragging()` prints "Dragging string not implemented on macos yet".

**Cause**: Platform drag API has limited implementation on macOS.

**Fix**: Implement internal drag handling instead:
```rust
// Instead of platform drag
// cx.start_dragging(items);  // Won't work on macOS

// Use internal drag state + hits_with_capture_overload
#[rust]
dragging_item: Option<usize>,

// Set state on drag start
self.dragging_item = Some(item_id);

// Handle with capture override
match event.hits_with_capture_overload(
    cx, self.view.area(),
    self.dragging_item.is_some()
) {
    // ...
}
```

See [Drag-Drop Reorder Pattern](../04-patterns/_base/18-drag-drop-reorder.md) for full implementation.

---

### Visual Updates Not Showing After Widget Changes

**Symptom**: Called `apply_over()` or `set_text()` but UI doesn't update.

**Cause**: Updates applied outside the draw phase may not take effect properly.

**Fix**: Use deferred update pattern:
```rust
#[rust]
needs_visual_update: bool,

pub fn set_item_id(&mut self, cx: &mut Cx, id: usize) {
    self.item_id = id;
    self.needs_visual_update = true;  // Flag for later
    self.view.redraw(cx);              // Schedule redraw
}

fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
    // Apply updates in draw phase
    if self.needs_visual_update {
        self.needs_visual_update = false;
        self.view.apply_over(cx, live! {
            draw_bg: { color: (self.get_color()) }
        });
    }
    self.view.draw_walk(cx, scope, walk)
}
```

---

### Hidden Widget Still Takes Space

**Symptom**: `set_visible(false)` doesn't collapse the widget's space.

**Cause**: Widget with `width: Fill` or `height: Fill` still participates in layout.

**Fix**: Set size to 0 when hiding:
```rust
// Bad - still takes space
self.view.view(id!(my_widget)).apply_over(cx, live! {
    visible: false
});

// Good - truly collapses
self.view.view(id!(my_widget)).apply_over(cx, live! {
    visible: false
    width: 0
    height: 0
});
```

---

## Performance Issues

### Excessive Redraws

**Symptom**: UI stutters or high CPU usage.

**Fix**: Only redraw what's needed:
```rust
// Bad - redraw everything
self.ui.redraw(cx);

// Good - redraw specific widget
self.ui.label(ids!(my_label)).redraw(cx);

// Good - batch updates then redraw once
self.update_multiple_labels(cx);
self.ui.view(ids!(labels_container)).redraw(cx);
```

---

### apply_over Performance

**Symptom**: Slow updates when using apply_over.

**Fix**: Batch apply_over calls:
```rust
// Bad - multiple apply_over calls
for item in items {
    self.ui.label(ids!(label)).apply_over(cx, live!{
        draw_text: { color: (color) }
    });
}

// Good - update once, redraw once
self.update_all_items(cx);
self.ui.redraw(cx);
```

---

## Tooltip Issues

### Tooltip Not Showing

**Symptom**: Called `show()` but tooltip doesn't appear.

**Causes & Fixes**:

1. **Missing action handler in app** - Tooltip actions must be handled globally:
```rust
// In app.rs handle_event or handle_actions
for action in cx.actions() {
    match action.as_widget_action().cast() {
        TooltipAction::HoverIn { text, widget_rect, options } => {
            self.ui.callout_tooltip(ids!(app_tooltip))
                .show_with_options(cx, &text, widget_rect, options);
        }
        TooltipAction::HoverOut => {
            self.ui.callout_tooltip(ids!(app_tooltip)).hide(cx);
        }
        _ => {}
    }
}
```

2. **Tooltip not in layout** - Add global tooltip to app root:
```rust
live_design! {
    App = {{App}} {
        ui: <Root> {
            main_content = <View> { /* app content */ }
            app_tooltip = <CalloutTooltip> {}  // Must be after main content
        }
    }
}
```

3. **Widget rect not available** - Ensure widget has been drawn:
```rust
// Bad - rect may be zero before first draw
let rect = self.draw_bg.area().rect(cx);

// Good - check if rect is valid
let rect = self.draw_bg.area().rect(cx);
if rect.size.x > 0.0 && rect.size.y > 0.0 {
    cx.widget_action(uid, path, TooltipAction::HoverIn { ... });
}
```

---

### Tooltip Arrow Points Wrong Direction

**Symptom**: Arrow doesn't point at target widget.

**Cause**: `target_pos` and `target_size` instance variables not set.

**Fix**: Pass all required shader instance variables:
```rust
tooltip.apply_over(cx, live! {
    content: {
        rounded_view = {
            draw_bg: {
                tooltip_pos: (tooltip_position)      // Tooltip top-left
                target_pos: (widget_rect.pos)        // Target top-left
                target_size: (widget_rect.size)      // Target dimensions
                callout_position: (callout_angle)    // 0/90/180/270
                expected_dimension_x: (tooltip_size.x)
            }
        }
    }
});
```

---

### Tooltip Goes Off Screen

**Symptom**: Tooltip appears partially outside window.

**Fix**: Implement edge detection with fallback:
```rust
fn calculate_position(
    options: &CalloutTooltipOptions,
    widget_rect: Rect,
    tooltip_size: DVec2,
    screen_size: DVec2,
) -> (DVec2, f64) {
    let mut pos = DVec2::default();
    let mut angle = 0.0;

    match options.position {
        TooltipPosition::Bottom => {
            pos.y = widget_rect.pos.y + widget_rect.size.y;
            // Flip if would go off bottom
            if pos.y + tooltip_size.y > screen_size.y {
                pos.y = widget_rect.pos.y - tooltip_size.y;
                angle = 180.0;  // Change arrow direction
            }
        }
        // ... other directions
    }

    // Clamp to screen bounds
    pos.x = pos.x.max(0.0).min(screen_size.x - tooltip_size.x);
    pos.y = pos.y.max(0.0).min(screen_size.y - tooltip_size.y);

    (pos, angle)
}
```

---

### Tooltip Flickers on Hover

**Symptom**: Tooltip appears and disappears rapidly.

**Cause**: Tooltip itself triggers HoverOut on target.

**Fix**: Handle both `FingerHoverIn` and `FingerHoverOver`:
```rust
match event.hits(cx, self.draw_bg.area()) {
    Hit::FingerHoverIn(_) | Hit::FingerHoverOver(_) => {
        // Both events should show tooltip
        cx.widget_action(uid, path, TooltipAction::HoverIn { ... });
    }
    Hit::FingerHoverOut(_) => {
        cx.widget_action(uid, path, TooltipAction::HoverOut);
    }
    _ => {}
}
```

---

### Tooltip Shows With Zero Size

**Symptom**: Tooltip appears as tiny dot or invisible.

**Cause**: `expected_dimension_x` is 0, shader skips drawing.

**Fix**: Get tooltip size after setting text:
```rust
pub fn show_with_options(&mut self, cx: &mut Cx, text: &str, ...) {
    let mut tooltip = self.view.tooltip(ids!(tooltip));

    // 1. Set text first
    tooltip.set_text(cx, text);

    // 2. Then get dimensions (text affects size)
    let tooltip_size = tooltip.view(ids!(rounded_view)).area().rect(cx).size;

    // 3. Check if size is valid
    if tooltip_size.x == 0.0 {
        // May need to wait for layout
        log!("Warning: tooltip size is zero");
        return;
    }

    // 4. Apply with valid dimensions
    tooltip.apply_over(cx, live! {
        content: { rounded_view = { draw_bg: {
            expected_dimension_x: (tooltip_size.x)
        }}}
    });
}
```

---

### Tooltip Persists After Widget Removed

**Symptom**: Tooltip stays visible after navigating away.

**Fix**: Hide tooltip on navigation/cleanup:
```rust
// When changing views
fn navigate_to(&mut self, cx: &mut Cx, screen: Screen) {
    // Hide any active tooltip first
    self.ui.callout_tooltip(ids!(app_tooltip)).hide(cx);

    // Then navigate
    self.current_screen = screen;
    self.ui.redraw(cx);
}
```

---

## Overlay/Popup Issues

<!-- Evolution: 2026-01-12 | source: makepad-component/tooltip | author: @claude -->
### Overlay Position Wrong on First Show

**Symptom**: Popup/tooltip appears at wrong position initially, then jumps to correct position.

**Cause**: Overlay size is unknown until after first draw. Position calculation uses `popup_size = 0`, resulting in wrong position.

**Solution**: Draw off-screen first to measure, then redraw at correct position:

```rust
fn draw_popup_overlay(&mut self, cx: &mut Cx2d, scope: &mut Scope) {
    self.draw_list.begin_overlay_reuse(cx);
    let pass_size = cx.current_pass_size();
    cx.begin_sized_turtle(pass_size, Layout::flow_overlay());

    // First frame: size is 0, draw off-screen to measure
    let is_measuring = self.popup_size.x == 0.0;
    let pos = if is_measuring {
        DVec2 { x: -10000.0, y: -10000.0 }  // Off-screen
    } else {
        self.calculate_position(anchor, pass_size)
    };

    // Draw popup at position
    let mut walk = popup.walk(cx);
    walk.abs_pos = Some(pos);
    let _ = popup.draw_walk(cx, scope, walk);

    // After draw, check if size changed
    let new_size = popup.area().rect(cx).size;
    if (new_size.x - self.popup_size.x).abs() > 1.0 {
        self.popup_size = new_size;
        cx.redraw_all();  // Trigger immediate redraw
    }

    cx.end_pass_sized_turtle();
    self.draw_list.end(cx);
}
```

**Key insight**: Use `cx.redraw_all()` (not just `self.redraw(cx)`) to ensure immediate redraw without waiting for next event.

---

### SDF Triangle Not Filling

**Symptom**: Triangle path is drawn but `fill()` produces no result or only fills some triangles.

**Cause**: SDF fill requires clockwise winding order. Counter-clockwise triangles won't fill.

**Solution**: Draw all triangles starting from tip, going clockwise:

```rust
// WRONG - may not fill depending on direction
sdf.move_to(left_x, base_y);
sdf.line_to(right_x, base_y);
sdf.line_to(center_x, tip_y);
sdf.close_path();
sdf.fill(color);

// CORRECT - always start from tip, go clockwise
sdf.move_to(center_x, tip_y);      // Start at tip
sdf.line_to(right_x, base_y);       // Clockwise to right base
sdf.line_to(left_x, base_y);        // Continue to left base
sdf.close_path();
sdf.fill(color);
```

See [SDF Drawing - Triangle Winding Order](../03-graphics/_base/04-sdf-drawing.md#critical-triangle-winding-order-for-fill) for detailed examples.

---

### Gap/Seam Between Box and Arrow

**Symptom**: Thin white line visible where tooltip arrow meets the box.

**Cause**: Anti-aliasing and floating-point precision at shape boundaries.

**Solution**: Extend arrow base into box by 1-2 pixels (overlap):

```rust
let overlap = 2.0;
let base_y = box_bottom - overlap;  // Arrow base inside box
sdf.move_to(cx, tip_y);
sdf.line_to(cx - half, base_y);
sdf.line_to(cx + half, base_y);
```

---

## Shader Instance Data Issues

### Mat4 as Instance Data Fails on Metal

**Symptom**: Using `#[calc] pub transform: Mat4` causes Metal shader compilation errors:
```
error: expected ';' at end of declaration list
    packed_float4 ds_transform 0;
error: duplicate member 'ds_transform'
```

**Cause**: The shader compiler generates invalid Metal code when decomposing Mat4 into columns - field names like `ds_transform 0` instead of `ds_transform_0`.

**Fix**: Manually decompose Mat4 into 4 Vec4 columns:

```rust
// Instead of:
// #[calc] pub transform: Mat4,  // FAILS on Metal

// Use 4 columns:
#[calc] pub transform_col0: Vec4,
#[calc] pub transform_col1: Vec4,
#[calc] pub transform_col2: Vec4,
#[calc] pub transform_col3: Vec4,

// Set transform method:
pub fn set_transform(&mut self, m: Mat4) {
    self.transform_col0 = vec4(m.v[0], m.v[1], m.v[2], m.v[3]);
    self.transform_col1 = vec4(m.v[4], m.v[5], m.v[6], m.v[7]);
    self.transform_col2 = vec4(m.v[8], m.v[9], m.v[10], m.v[11]);
    self.transform_col3 = vec4(m.v[12], m.v[13], m.v[14], m.v[15]);
}
```

**In shader, reconstruct mat4:**
```rust
fn vertex(self) -> vec4 {
    let transform = mat4(
        self.transform_col0,
        self.transform_col1,
        self.transform_col2,
        self.transform_col3
    );
    let world_pos = transform * vec4(self.geom_pos, 1.0);
    // ...
}
```

**Note**: Use `#[calc]` for computed instance data, not `#[live]`.

---

## Widget Overlay Issues

### DropDown Popup Not Appearing (Z-Order Conflict)

**Symptom**: DropDown button works but popup menu never appears, or Modal doesn't display over content.

**Cause**: Custom 3D rendering (using `DrawMesh`, `draw_3d_shape`, or `draw_abs`) draws directly to the GPU framebuffer, bypassing Makepad's overlay layer system. This causes:
- DropDown popup menus (which use `PopupMenuGlobal` on an overlay layer) to be drawn under the 3D content
- Modal dialogs to be invisible behind 3D viewports

**Affected widgets**:
- `DropDown` - popup uses `Overlay` layer
- `Modal` - content rendered on overlay
- `PopupMenu` - same overlay system
- Any widget using `PopupMenuGlobal`

**Workaround**: Hide the 3D viewport when showing overlay widgets:

```rust
// When opening modal - hide 3D viewport
if self.view.button(id!(open_btn)).clicked(&actions) {
    self.view.view(id!(viewport)).set_visible(cx, false);  // Hide 3D content
    self.view.modal(id!(my_modal)).open(cx);
}

// Robot selection - use buttons inside modal instead of dropdown
if self.view.button(id!(my_modal.robot_btn)).clicked(&actions) {
    // Handle selection
    self.view.modal(id!(my_modal)).close(cx);
    self.view.view(id!(viewport)).set_visible(cx, true);  // Restore 3D content
}

// Modal dismissed (click outside or Escape)
if self.view.modal(id!(my_modal)).dismissed(&actions) {
    self.view.view(id!(viewport)).set_visible(cx, true);  // Restore 3D content
}
```

**Alternative**: Use Buttons or RadioButtons instead of DropDown for selection when 3D content is present.

**Note**: Even placing a DropDown inside a Modal doesn't help - the nested overlay still conflicts with the 3D rendering. Use buttons for selection in modals over 3D viewports.

---

## Debugging Tips

### Enable Debug Output

```bash
# Run with line info for better error messages
MAKEPAD=lines cargo +nightly run
```

### Use log! Macro

```rust
log!("Value: {:?}", my_value);
log!("State: {} / {}", self.counter, self.is_loading);
```

### Check Event Flow

```rust
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        log!("Actions received: {}", actions.len());

        if self.ui.button(ids!(my_btn)).clicked(&actions) {
            log!("Button clicked!");
        }
    }
}
```

---

## Quick Reference

| Error Type | Common Cause | Quick Fix |
|------------|--------------|-----------|
| Color parse error | Color ends in `e` | Change last digit |
| Missing argument | `set_text` needs `cx` | Add `cx` parameter |
| Module not found | Wrong crate path | Use `makepad_widgets::` |
| No matching field: font | Using `font:` property | Use `text_style: <THEME_FONT_*>{}` |
| Empty font family | Missing font_family in text_style | Inherit from `THEME_FONT_REGULAR` not just inline `{}` |
| FileTree no content | Missing data structure | Use `#[wrap] #[live]` pattern with LiveIdMap backing |
| No matching field | Property doesn't exist | Check widget docs |
| Borrow conflict | Mixed mutable/immutable | Separate borrow scopes |
| UI not updating | Missing redraw | Call `redraw(cx)` |
| Widget not found | Wrong ID or path | Check live_design IDs |
| Timer not firing | Timer not stored | Store in `#[rust]` field |
| Instance var not updating | Using set_uniform | Use apply_over instead |
| Shader if-branch fails | GPU branching issue | Use step()/mix() instead |
| Tooltip not showing | Missing action handler | Add TooltipAction handler in app |
| Tooltip arrow wrong | Missing target_pos/size | Pass all shader instance vars |
| Tooltip off screen | No edge detection | Implement position fallback |
| Tooltip flickers | Only HoverIn handled | Handle HoverIn + HoverOver |
| Tooltip zero size | Getting size before text | Set text first, then get size |
| Overlay position wrong | Size unknown on first draw | Draw off-screen first, use `cx.redraw_all()` |
| Triangle not filling | Wrong winding order | Draw from tip, go clockwise |
| Gap between shapes | Float precision | Use 1-2px overlap at joints |
| DropDown not opening | Z-order conflict with 3D | Hide 3D viewport, use buttons |
| Modal invisible | Custom GPU drawing on top | set_visible(cx, false) on 3D view |
| apply_over color no effect | Direct color on templates | Use instance variables in shader |
| TextInput focus conflicts | Hidden inputs receiving events | Add visibility checks, clear selection |
| Mat4 shader compile error | Metal field naming bug | Use 4×Vec4 columns, reconstruct in shader |
```

## File: `skills/makepad-router/SKILL.md`
```markdown
---
name: makepad-router
description: "CRITICAL: Use for ALL Makepad/Robius questions including widgets, layout, events, and shaders.
Triggers on: makepad, robius, live_design, app_main, Widget, View, Button, Label, Image, TextInput,
ScrollView, RoundedView, SolidView, PortalList, Markdown, Html, TextFlow,
layout, Flow, Walk, padding, margin, width, height, Fit, Fill, align, spacing,
event, action, Hit, FingerDown, FingerUp, KeyDown, handle_event, click, tap,
animator, animation, state, transition, hover, pressed, ease,
shader, draw_bg, draw_text, Sdf2d, pixel, gradient, glow, shadow,
font, text_style, font_size, glyph, typography,
tokio, async, spawn, submit_async, SignalToUI, post_action,
apply_over, TextOrImage, modal, collapsible, drag drop,
AppState, persistence, theme, Scope,
deploy, package, APK, IPA, WASM, cargo makepad,
makepad widget, makepad 组件, makepad 按钮, makepad 布局, makepad 事件, makepad 动画, makepad 着色器,
创建组件, 自定义组件, 开发应用, 居中, 对齐, 点击事件, 悬停效果, 渐变, 阴影, 字体大小"
globs: ["**/live_design!*", "**/*.rs"]
---

# Makepad Question Router

> **Version:** 2.0.0 | **Last Updated:** 2026-01-21

## INSTRUCTIONS FOR CLAUDE

When this skill is triggered, you MUST load the appropriate sub-skill(s) based on the question:

### Routing Table

| Keywords | Load Skill |
|----------|------------|
| `live_design!`, `app_main!`, getting started, app structure | **makepad-basics** |
| DSL, inheritance, `<Widget>`, `Foo = { }` | **makepad-dsl** |
| layout, Flow, Walk, padding, width, height, center, align | **makepad-layout** |
| View, Button, Label, Image, TextInput, widget, Markdown, Html | **makepad-widgets** |
| event, action, Hit, FingerDown, handle_event, click | **makepad-event-action** |
| animator, state, transition, hover, pressed | **makepad-animation** |
| shader, draw_bg, Sdf2d, gradient, glow, shadow | **makepad-shaders** |
| font, text_style, font_size, glyph | **makepad-font** |
| platform, macOS, Android, iOS, WASM | **makepad-platform** |
| tokio, async, spawn, submit_async | **robius-app-architecture** |
| apply_over, modal, collapsible, pageflip | **robius-widget-patterns** |
| custom action, MatchEvent, post_action | **robius-event-action** |
| AppState, persistence, theme switch | **robius-state-management** |
| deploy, package, APK, IPA | **makepad-deployment** |
| troubleshoot, error, debug | **makepad-reference** |

### Context Bundle Loading

For complex tasks, load multiple skills:

| Context | Load These Skills |
|---------|-------------------|
| **Create widget/component** | makepad-widgets, makepad-dsl, makepad-layout, makepad-animation, makepad-shaders, makepad-event-action |
| **Build full app** | makepad-basics, makepad-dsl, makepad-layout, makepad-widgets, makepad-event-action, robius-app-architecture |
| **UI design** | makepad-dsl, makepad-layout, makepad-widgets, makepad-animation, makepad-shaders |
| **Production patterns** | robius-app-architecture, robius-widget-patterns, robius-state-management |

### Skill Dependencies

When loading a skill, also load its dependencies:

| Skill | Also Load |
|-------|-----------|
| makepad-widgets | makepad-layout, makepad-dsl |
| makepad-animation | makepad-shaders |
| makepad-shaders | makepad-widgets |
| robius-widget-patterns | makepad-widgets, makepad-layout |

### Example Workflow

```
User: "How do I create a custom button with hover animation?"

Analysis:
1. Keywords: custom, button, hover, animation
2. Context: Widget creation
3. Load: makepad-widgets, makepad-animation, makepad-shaders, makepad-event-action

Answer using patterns from all loaded skills.
```

## Default Project Settings

When creating Makepad projects:

```toml
[package]
edition = "2024"

[dependencies]
makepad-widgets = { git = "https://github.com/makepad/makepad", branch = "dev" }

[features]
default = []
nightly = ["makepad-widgets/nightly"]
```

## Key Patterns Quick Reference

### Widget Definition
```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,
    #[live] property: f64,
    #[rust] state: State,
    #[animator] animator: Animator,
}
```

### Async Pattern (Robius)
```rust
// UI -> Async
submit_async_request(MyRequest { ... });

// Async -> UI
Cx::post_action(MyAction { ... });
SignalToUI::set_ui_signal();
```
```

## File: `skills/makepad-shaders/SKILL.md`
```markdown
---
name: makepad-shaders
description: |
  CRITICAL: Use for Makepad shader system. Triggers on:
  makepad shader, makepad draw_bg, Sdf2d, makepad pixel,
  makepad glsl, makepad sdf, draw_quad, makepad gpu,
  makepad 着色器, makepad shader 语法, makepad 绘制
---

# Makepad Shaders Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad shaders. Help users by:
- **Writing code**: Generate shader code following the patterns below
- **Answering questions**: Explain shader language, Sdf2d, built-in functions

## Documentation

Refer to the local files for detailed documentation:
- `./references/shader-basics.md` - Shader language fundamentals
- `./references/sdf2d-reference.md` - Complete Sdf2d API reference

## Advanced Patterns

For production-ready shader patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| [01-shader-structure](./_base/01-shader-structure.md) | Shader fundamentals |
| [02-shader-math](./_base/02-shader-math.md) | Mathematical functions |
| [03-sdf-shapes](./_base/03-sdf-shapes.md) | SDF shape primitives |
| [04-sdf-drawing](./_base/04-sdf-drawing.md) | Advanced SDF drawing |
| [05-progress-track](./_base/05-progress-track.md) | Progress indicators |
| [09-loading-spinner](./_base/09-loading-spinner.md) | Loading animations |
| [10-hover-effect](./_base/10-hover-effect.md) | Hover visual effects |
| [11-gradient-effects](./_base/11-gradient-effects.md) | Color gradients |
| [12-shadow-glow](./_base/12-shadow-glow.md) | Shadow and glow |
| [13-disabled-state](./_base/13-disabled-state.md) | Disabled visuals |
| [14-toggle-checkbox](./_base/14-toggle-checkbox.md) | Toggle animations |

Community contributions: `./community/`

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. Basic Custom Shader

```rust
<View> {
    show_bg: true
    draw_bg: {
        // Shader uniforms
        color: #FF0000

        // Custom pixel shader
        fn pixel(self) -> vec4 {
            return self.color;
        }
    }
}
```

### 2. Rounded Rectangle with Border

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #333333
        border_color: #666666
        border_radius: 8.0
        border_size: 1.0

        fn pixel(self) -> vec4 {
            let sdf = Sdf2d::viewport(self.pos * self.rect_size);
            sdf.box(1.0, 1.0,
                    self.rect_size.x - 2.0,
                    self.rect_size.y - 2.0,
                    self.border_radius);
            sdf.fill_keep(self.color);
            sdf.stroke(self.border_color, self.border_size);
            return sdf.result;
        }
    }
}
```

### 3. Gradient Background

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #FF0000
        color_2: #0000FF

        fn pixel(self) -> vec4 {
            let t = self.pos.x;  // Horizontal gradient
            return mix(self.color, self.color_2, t);
        }
    }
}
```

### 4. Circle Shape

```rust
<View> {
    show_bg: true
    draw_bg: {
        color: #0066CC

        fn pixel(self) -> vec4 {
            let sdf = Sdf2d::viewport(self.pos * self.rect_size);
            let center = self.rect_size * 0.5;
            let radius = min(center.x, center.y) - 1.0;
            sdf.circle(center.x, center.y, radius);
            sdf.fill(self.color);
            return sdf.result;
        }
    }
}
```

## Shader Structure

| Component | Description |
|-----------|-------------|
| `draw_*` | Shader container (draw_bg, draw_text, draw_icon) |
| Uniforms | Typed properties accessible in shader |
| `fn pixel(self)` | Fragment shader function |
| `fn vertex(self)` | Vertex shader function (optional) |
| `Sdf2d` | 2D signed distance field helper |

## Built-in Variables

| Variable | Type | Description |
|----------|------|-------------|
| `self.pos` | vec2 | Normalized position (0-1) |
| `self.rect_size` | vec2 | Widget size in pixels |
| `self.rect_pos` | vec2 | Widget position |

## Sdf2d Quick Reference

| Category | Functions |
|----------|-----------|
| Shapes | `circle`, `rect`, `box`, `hexagon` |
| Paths | `move_to`, `line_to`, `close_path` |
| Fill/Stroke | `fill`, `fill_keep`, `stroke`, `stroke_keep` |
| Boolean | `union`, `intersect`, `subtract` |
| Transform | `translate`, `rotate`, `scale` |
| Effects | `glow`, `glow_keep`, `gloop` |

## Built-in Functions (GLSL)

| Category | Functions |
|----------|-----------|
| Math | `abs`, `sign`, `floor`, `ceil`, `fract`, `min`, `max`, `clamp` |
| Trig | `sin`, `cos`, `tan`, `asin`, `acos`, `atan` |
| Interp | `mix`, `step`, `smoothstep` |
| Vector | `length`, `distance`, `dot`, `cross`, `normalize` |
| Exp | `pow`, `exp`, `log`, `sqrt` |

## When Writing Code

1. Always use `show_bg: true` to enable background shader
2. Use `Sdf2d::viewport()` to create SDF context
3. Return `vec4` (RGBA) from `fn pixel()`
4. Uniforms must be declared before shader functions
5. Use `self.` prefix to access uniforms and built-ins

## When Answering Questions

1. Makepad shaders use Rust-like syntax, compiled to GPU code
2. Every widget can have custom shaders (draw_bg, draw_text, etc.)
3. Shaders are live-reloaded - edit and see changes instantly
4. Sdf2d is the primary tool for 2D shape rendering
5. GLSL ES 1.0 built-in functions are available
```

## File: `skills/makepad-shaders/_base/01-shader-structure.md`
```markdown
---
name: makepad-shader-structure
author: robius
source: makepad-docs
date: 2024-01-01
tags: [shader, structure, instance, uniform, basics]
level: beginner
---

# Shader Structure

Basic Makepad shader architecture and variable types.

## Basic Structure

```rust
live_design! {
    MyWidget = {{MyWidget}} {
        draw_bg: {
            // Instance variables (per-widget)
            instance hover: 0.0
            instance pressed: 0.0

            // Uniforms (global parameters)
            uniform color: #4A90D9
            uniform border_radius: 4.0

            fn pixel(self) -> vec4 {
                let sdf = Sdf2d::viewport(self.pos * self.rect_size);
                sdf.box(0., 0., self.rect_size.x, self.rect_size.y, self.border_radius);
                sdf.fill(self.color);
                return sdf.result;
            }
        }
    }
}
```

## Variable Types

| Type | Scope | Usage |
|------|-------|-------|
| `instance` | Per-widget | `instance hover: 0.0` |
| `uniform` | Global | `uniform color: #4A90D9` |
| `varying` | Vertex->Fragment | `varying uv: vec2` |
| `texture` | Texture sampler | `texture my_tex: texture2d` |

## Instance Variables

Per-widget state that can be animated:

```rust
draw_bg: {
    instance hover: 0.0      // 0.0 to 1.0 for hover animation
    instance pressed: 0.0    // 0.0 to 1.0 for press animation
    instance selected: 0.0   // 0.0 or 1.0 for selection state
    instance disabled: 0.0   // 0.0 or 1.0 for disabled state
    instance progress: 0.0   // 0.0 to 1.0 for progress
}
```

## Uniform Variables

Global parameters shared across all instances:

```rust
draw_bg: {
    uniform color: #4A90D9           // Color
    uniform border_radius: 4.0       // Number
    uniform shadow_offset: vec2(2.0, 2.0)  // Vector
}
```

## Built-in Variables

| Variable | Type | Description |
|----------|------|-------------|
| `self.pos` | vec2 | Normalized position (0-1) within widget |
| `self.rect_size` | vec2 | Widget size in pixels |
| `self.rect_pos` | vec2 | Widget position in window |
| `self.geom_pos` | vec2 | Geometry position |

## Using Built-in Variables

```rust
fn pixel(self) -> vec4 {
    // Position within widget (0-1)
    let x = self.pos.x;  // 0 at left, 1 at right
    let y = self.pos.y;  // 0 at top, 1 at bottom

    // Pixel position
    let px = self.pos * self.rect_size;  // In pixels

    // Widget dimensions
    let width = self.rect_size.x;
    let height = self.rect_size.y;

    // Create SDF viewport
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    // ...
}
```

## When to Use

- Use `instance` for per-widget animated state (hover, pressed, etc.)
- Use `uniform` for global parameters that apply to all instances
- Access `self.pos` for position-based effects
- Access `self.rect_size` for dimension-based calculations
```

## File: `skills/makepad-shaders/_base/02-shader-math.md`
```markdown
---
name: makepad-shader-math
author: robius
source: makepad-docs
date: 2024-01-01
tags: [shader, math, interpolation, color, texture]
level: beginner
---

# Shader Math & Colors

Math functions, color operations, and texture sampling.

## Interpolation

```rust
// Linear interpolation
let color = mix(#ff0000, #00ff00, 0.5);  // 50% between red and green

// Smooth interpolation (0 to 1 with easing)
let t = smoothstep(0.0, 1.0, self.pos.x);

// Clamp value to range
let clamped = clamp(value, 0.0, 1.0);

// Step function (hard edge)
let mask = step(0.5, self.pos.x);  // 0 if x < 0.5, else 1
```

## Trigonometry

```rust
let angle = self.pos.x * 2.0 * PI;
let wave = sin(angle);
let wave2 = cos(angle);
```

## Vector Math

```rust
let v = vec2(1.0, 2.0);
let len = length(v);           // Vector length
let norm = normalize(v);       // Unit vector
let d = dot(v1, v2);          // Dot product
let dist = length(self.pos - center);  // Distance
```

## Color Operations

```rust
// Color from hex
let color = #4A90D9;      // RGB
let color = #4A90D9FF;    // RGBA

// Color components
let r = color.r;  // 0.0 to 1.0
let g = color.g;
let b = color.b;
let a = color.a;

// Create color
let color = vec4(1.0, 0.0, 0.0, 1.0);  // Red, full opacity

// Mix colors
let blended = mix(color1, color2, factor);

// Adjust alpha
let semi_transparent = vec4(color.rgb, 0.5);
```

## Texture Sampling

```rust
draw_bg: {
    texture my_image: texture2d

    fn pixel(self) -> vec4 {
        // Sample at current position
        let color = sample2d(self.my_image, self.pos);

        // Sample with custom UV (tiling)
        let custom_uv = vec2(self.pos.x * 2.0, self.pos.y);
        let tiled = sample2d(self.my_image, fract(custom_uv));

        return color;
    }
}
```

## Helper Functions

Define reusable functions within shader:

```rust
draw_bg: {
    fn get_color(self) -> vec4 {
        return mix(self.color_normal, self.color_hover, self.hover);
    }

    fn random(st: vec2) -> f32 {
        return fract(sin(dot(st, vec2(12.9898, 78.233))) * 43758.5453);
    }

    fn pixel(self) -> vec4 {
        let color = self.get_color();
        let noise = random(self.pos);
        return color + vec4(noise * 0.05);
    }
}
```

## Avoid Branching

GPU prefers math over if/else:

```rust
// Avoid if statements in pixel shader
if self.hover > 0.5 {
    return color1;
} else {
    return color2;
}

// Use mix instead
return mix(color2, color1, step(0.5, self.hover));

// Or smoothstep for gradual transition
return mix(color1, color2, smoothstep(0.0, 1.0, self.hover));
```

## When to Use

- Use `mix()` for smooth color transitions
- Use `smoothstep()` for antialiased edges
- Use `step()` for hard conditional without branching
- Use custom helper functions for repeated calculations
```

## File: `skills/makepad-shaders/_base/03-sdf-shapes.md`
```markdown
---
name: makepad-sdf-shapes
author: robius
source: makepad-docs
date: 2024-01-01
tags: [sdf, shapes, circle, box, hexagon]
level: beginner
---

# SDF Basic Shapes

Signed Distance Field primitives in Makepad.

## SDF Operations

| Function | Description |
|----------|-------------|
| `sdf.circle(x, y, r)` | Circle at (x,y) with radius r |
| `sdf.box(x, y, w, h, r)` | Rounded rect with corner radius r |
| `sdf.hexagon(x, y, r)` | Hexagon |
| `sdf.fill(color)` | Fill current shape |
| `sdf.stroke(color, width)` | Stroke outline |
| `sdf.fill_keep(color)` | Fill and preserve shape |
| `sdf.stroke_keep(color, width)` | Stroke and preserve shape |

## Circle

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let center = self.rect_size * 0.5;
    let radius = min(center.x, center.y) - 2.0;

    sdf.circle(center.x, center.y, radius);
    sdf.fill(#4A90D9);

    return sdf.result;
}
```

## Rounded Rectangle

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    sdf.box(
        0.0,                   // x
        0.0,                   // y
        self.rect_size.x,      // width
        self.rect_size.y,      // height
        8.0                    // corner radius
    );
    sdf.fill(#ffffff);

    return sdf.result;
}
```

## Capsule/Stadium Shape

**Important**: `sdf.box()` with large radius may not produce correct capsule shapes. Use shape composition:

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let sz = self.rect_size;
    let r = sz.y * 0.5;

    // Draw capsule: left circle + rectangle + right circle
    sdf.circle(r, r, r);
    sdf.rect(r, 0.0, sz.x - sz.y, sz.y);
    sdf.circle(sz.x - r, r, r);

    sdf.fill(#3b82f6);
    return sdf.result;
}
```

## Fill with Stroke

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    sdf.box(2., 2., self.rect_size.x - 4., self.rect_size.y - 4., 6.0);
    sdf.fill(#1a1a26);      // Fill color
    sdf.stroke(#333348, 1.0);  // Border color, width

    return sdf.result;
}
```

## Circular Avatar Mask

```rust
draw_bg: {
    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let c = self.rect_size * 0.5;

        sdf.circle(c.x, c.y, c.x);
        let img_color = sample2d(self.image, self.pos);
        sdf.fill(img_color);

        return sdf.result;
    }
}
```

## Inset for Border Effect

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    // Inset box leaves room for border
    sdf.box(
        1.0,
        1.0,
        self.rect_size.x - 2.0,
        self.rect_size.y - 2.0,
        6.0
    );
    sdf.fill(#1a1a26);
    sdf.stroke(#333348, 1.0);

    return sdf.result;
}
```

## When to Use

- Use `circle` for avatars, dots, round buttons
- Use `box` for cards, panels, buttons
- Use capsule composition for pill-shaped elements (switches, tags)
- Use `fill_keep` when you need to add more shapes to the same SDF
```

## File: `skills/makepad-shaders/_base/04-sdf-drawing.md`
```markdown
---
name: makepad-sdf-drawing
author: robius
source: makepad-docs
date: 2024-01-01
tags: [sdf, line, arc, triangle, path]
level: intermediate
---

# SDF Path Drawing

Lines, arcs, and complex paths in Makepad SDF.

## Line Drawing

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    // Move to start point
    sdf.move_to(10.0, 10.0);

    // Line to end point
    sdf.line_to(100.0, 50.0);

    // Stroke the line
    sdf.stroke(#ffffff, 2.0);

    return sdf.result;
}
```

## Arc Drawing

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let center = self.rect_size * 0.5;
    let radius = min(center.x, center.y) - 4.0;

    // Draw arc from angle1 to angle2
    let start_angle = 0.0;
    let end_angle = PI * 1.5;  // 270 degrees

    sdf.move_to(
        center.x + cos(start_angle) * radius,
        center.y + sin(start_angle) * radius
    );
    sdf.arc(center.x, center.y, radius, start_angle, end_angle);
    sdf.stroke(#4A90D9, 3.0);

    return sdf.result;
}
```

## Triangle Drawing

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    // Define three vertices
    let v1 = vec2(50.0, 10.0);   // Top
    let v2 = vec2(10.0, 90.0);   // Bottom left
    let v3 = vec2(90.0, 90.0);   // Bottom right

    sdf.move_to(v1.x, v1.y);
    sdf.line_to(v2.x, v2.y);
    sdf.line_to(v3.x, v3.y);
    sdf.close_path();

    sdf.fill(#4A90D9);

    return sdf.result;
}
```

<!-- Evolution: 2026-01-12 | source: makepad-component/tooltip | author: @claude -->
### CRITICAL: Triangle Winding Order for Fill

**Problem**: Triangle fills correctly in some directions but not others.

**Cause**: SDF `fill()` requires consistent winding order. Triangles must be drawn in a specific direction (typically starting from the "tip" going clockwise) to fill properly.

**Solution**: Always draw triangles starting from the tip/apex, then go clockwise around the base:

```rust
// Example: Arrow triangles pointing in 4 directions
// ALL start from tip, then clockwise around base

// Arrow pointing DOWN (tip at bottom)
sdf.move_to(cx, tip_y);                    // Start at tip
sdf.line_to(cx - half_w, base_y);          // Go to left base
sdf.line_to(cx + half_w, base_y);          // Go to right base
sdf.close_path();
sdf.fill(color);

// Arrow pointing UP (tip at top)
sdf.move_to(cx, tip_y);                    // Start at tip
sdf.line_to(cx + half_w, base_y);          // Go to right base (clockwise)
sdf.line_to(cx - half_w, base_y);          // Go to left base
sdf.close_path();
sdf.fill(color);

// Arrow pointing RIGHT (tip at right)
sdf.move_to(tip_x, cy);                    // Start at tip
sdf.line_to(base_x, cy + half_w);          // Go to bottom base (clockwise)
sdf.line_to(base_x, cy - half_w);          // Go to top base
sdf.close_path();
sdf.fill(color);

// Arrow pointing LEFT (tip at left)
sdf.move_to(tip_x, cy);                    // Start at tip
sdf.line_to(base_x, cy - half_w);          // Go to top base (clockwise)
sdf.line_to(base_x, cy + half_w);          // Go to bottom base
sdf.close_path();
sdf.fill(color);
```

**Key insight**: The winding must be clockwise relative to the screen (Y increases downward). If your triangle doesn't fill, reverse the order of the last two points.

## Combining Shapes

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    // First shape - fill and keep
    sdf.circle(50., 50., 30.);
    sdf.fill_keep(#FF0000);

    // Second shape - additive
    sdf.circle(80., 50., 30.);
    sdf.fill(#00FF00);

    return sdf.result;
}
```

<!-- Evolution: 2026-01-12 | source: makepad-component/tooltip | author: @claude -->
### Avoiding Gaps Between Connected Shapes

**Problem**: When drawing a box with an attached triangle (like tooltip arrow), there's a visible gap/seam between them.

**Cause**: Anti-aliasing and floating-point precision cause thin gaps at shape boundaries.

**Solution**: Use overlap - extend the triangle's base into the box by 1-2 pixels:

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let overlap = 2.0;  // Overlap to avoid gaps

    // Draw rounded box (leaving space for arrow)
    let box_height = self.rect_size.y - arrow_depth;
    sdf.box(0., 0., self.rect_size.x, box_height, radius);
    sdf.fill_keep(bg_color);

    // Draw arrow with base INSIDE the box (overlap)
    let base_y = box_height - overlap;  // Base extends INTO box
    let tip_y = self.rect_size.y;

    sdf.move_to(cx, tip_y);
    sdf.line_to(cx - arrow_half, base_y);
    sdf.line_to(cx + arrow_half, base_y);
    sdf.close_path();
    sdf.fill_keep(bg_color);

    sdf.stroke(border_color, 1.0);
    return sdf.result;
}
```

**Key insight**: The overlap ensures the shapes "merge" visually. Use 1-2 pixels overlap for clean joins.

## Orientation-Switchable Shape

Use instance variable for vertical/horizontal:

```rust
draw_track: {
    instance vertical: 0.0  // 0.0 = horizontal, 1.0 = vertical

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let sz = self.rect_size;

        let is_vert = self.vertical;
        let length = mix(sz.x, sz.y, is_vert);
        let thickness = mix(sz.y, sz.x, is_vert);
        let r = thickness * 0.5;

        if is_vert > 0.5 {
            sdf.circle(r, r, r);
            sdf.rect(0.0, r, sz.x, sz.y - sz.x);
            sdf.circle(r, sz.y - r, r);
        } else {
            sdf.circle(r, r, r);
            sdf.rect(r, 0.0, sz.x - sz.y, sz.y);
            sdf.circle(sz.x - r, r, r);
        }

        sdf.fill(#e2e8f0);
        return sdf.result;
    }
}
```

Note: Using `if` in shape construction is acceptable since it's a static branch.

## When to Use

- Use `move_to/line_to` for custom polygons and paths
- Use `arc` for progress indicators, circular UI
- Use `close_path` for filled polygons
- Use `fill_keep` to draw multiple shapes additively
```

## File: `skills/makepad-shaders/_base/05-progress-track.md`
```markdown
---
name: makepad-progress-track
author: robius
source: makepad-docs
date: 2024-01-01
tags: [sdf, progress, slider, track]
level: intermediate
---

# Progress & Track Shapes

Progress bars, sliders, and partial fills.

## Progress Bar with Partial Fill

Use `step()` instead of `if` for conditional fill:

```rust
draw_bg: {
    instance progress: 0.0  // 0.0 to 1.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let sz = self.rect_size;
        let r = sz.y * 0.5;

        // Draw track (background capsule)
        sdf.circle(r, r, r);
        sdf.rect(r, 0.0, sz.x - sz.y, sz.y);
        sdf.circle(sz.x - r, r, r);

        let track_color = #e2e8f0;
        let fill_color = #3b82f6;

        sdf.fill(track_color);

        // Calculate fill region using step()
        let fill_end = sz.x * self.progress;
        let px = self.pos.x * sz.x;
        let in_fill = step(px, fill_end);

        // Draw fill shape
        let sdf2 = Sdf2d::viewport(self.pos * self.rect_size);
        sdf2.circle(r, r, r);
        sdf2.rect(r, 0.0, sz.x - sz.y, sz.y);
        sdf2.circle(sz.x - r, r, r);
        sdf2.fill(fill_color);

        return mix(sdf.result, sdf2.result, in_fill * sdf2.result.w);
    }
}
```

## Range Slider Track

For a slider with start and end values:

```rust
draw_track: {
    instance progress_start: 0.0
    instance progress_end: 0.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let sz = self.rect_size;
        let r = sz.y * 0.5;

        // Draw track capsule
        sdf.circle(r, r, r);
        sdf.rect(r, 0.0, sz.x - sz.y, sz.y);
        sdf.circle(sz.x - r, r, r);
        sdf.fill(#e2e8f0);

        // Calculate fill region between start and end
        let fill_start = sz.x * self.progress_start;
        let fill_end = sz.x * self.progress_end;
        let px = self.pos.x * sz.x;

        // Pixel is in fill if: start <= px <= end
        let in_fill = step(fill_start, px) * step(px, fill_end);

        // Draw fill
        let sdf2 = Sdf2d::viewport(self.pos * self.rect_size);
        sdf2.circle(r, r, r);
        sdf2.rect(r, 0.0, sz.x - sz.y, sz.y);
        sdf2.circle(sz.x - r, r, r);
        sdf2.fill(#3b82f6);

        return mix(sdf.result, sdf2.result, in_fill * sdf2.result.w);
    }
}
```

## Usage Example

```rust
live_design! {
    ProgressBar = {{ProgressBar}} {
        width: Fill, height: 8
        show_bg: true
        draw_bg: {
            instance progress: 0.5
            // ... shader code above
        }
    }
}
```

Update progress in Rust:

```rust
impl ProgressBar {
    pub fn set_progress(&mut self, cx: &mut Cx, value: f64) {
        self.draw_bg.apply_over(cx, live!{
            progress: (value)
        });
        self.redraw(cx);
    }
}
```

## When to Use

- Use for progress bars, loading indicators
- Use for slider tracks with highlighted regions
- Use `step()` for GPU-friendly conditional rendering
- Use dual SDF for overlaid fill regions
```

## File: `skills/makepad-shaders/_base/09-loading-spinner.md`
```markdown
---
name: makepad-loading-spinner
author: robius
source: makepad-docs
date: 2024-01-01
tags: [spinner, loading, animation, arc]
level: intermediate
---

# Loading Spinner

Rotating arc animation for loading states.

## Implementation

```rust
live_design! {
    Spinner = {{Spinner}} {
        width: 40, height: 40

        draw_bg: {
            instance rotation: 0.0

            fn pixel(self) -> vec4 {
                let sdf = Sdf2d::viewport(self.pos * self.rect_size);
                let center = self.rect_size * 0.5;
                let radius = min(center.x, center.y) - 4.0;

                // Rotating arc
                let angle = self.rotation * 2.0 * PI;
                let arc_start = angle;
                let arc_end = angle + PI * 1.5;

                sdf.move_to(
                    center.x + cos(arc_start) * radius,
                    center.y + sin(arc_start) * radius
                );
                sdf.arc(center.x, center.y, radius, arc_start, arc_end);
                sdf.stroke(#4A90D9, 3.0);

                return sdf.result;
            }
        }

        animator: {
            spin = {
                default: on,
                on = {
                    from: {all: Loop {duration: 1.0, end: 1.0}}
                    apply: {
                        draw_bg: {
                            rotation: [{time: 0.0, value: 0.0}, {time: 1.0, value: 1.0}]
                        }
                    }
                }
            }
        }
    }
}
```

## Rust Implementation

```rust
#[derive(Live, LiveHook, Widget)]
pub struct Spinner {
    #[deref] view: View,
    #[animator] animator: Animator,
}

impl Widget for Spinner {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if self.animator_handle_event(cx, event).must_redraw() {
            self.redraw(cx);
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Start spinning animation
        if self.animator.is_default() {
            self.animator_play(cx, ids!(spin.on));
        }
        self.view.draw_walk(cx, scope, walk)
    }
}
```

## Usage

```rust
live_design! {
    <Spinner> {
        width: 24, height: 24
    }
}
```

## Customization

### Different Colors

```rust
<Spinner> {
    draw_bg: {
        fn pixel(self) -> vec4 {
            // ... same shader code ...
            sdf.stroke(#10b981, 3.0);  // Green spinner
            return sdf.result;
        }
    }
}
```

### Different Speed

```rust
animator: {
    spin = {
        default: on,
        on = {
            from: {all: Loop {duration: 0.6, end: 1.0}}  // Faster
            // ...
        }
    }
}
```

## When to Use

- Use for loading states during async operations
- Use for indicating background processing
- Auto-starts on draw, no manual triggering needed
```

## File: `skills/makepad-shaders/_base/10-hover-effect.md`
```markdown
---
name: makepad-hover-effect
author: robius
source: makepad-docs
date: 2024-01-01
tags: [hover, effect, interactive, button]
level: beginner
---

# Hover Effect

Interactive hover state for buttons and clickable elements.

## Basic Hover

```rust
draw_bg: {
    instance hover: 0.0
    uniform base_color: #4A90D9

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        sdf.box(0., 0., self.rect_size.x, self.rect_size.y, 4.0);

        let hover_color = mix(self.base_color, #FFFFFF, 0.2);
        let final_color = mix(self.base_color, hover_color, self.hover);

        sdf.fill(final_color);
        return sdf.result;
    }
}
```

## Button with Pressed Effect

```rust
draw_bg: {
    instance hover: 0.0
    instance pressed: 0.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);

        // Slightly smaller when pressed
        let shrink = self.pressed * 2.0;
        sdf.box(
            shrink,
            shrink,
            self.rect_size.x - shrink * 2.0,
            self.rect_size.y - shrink * 2.0,
            4.0
        );

        let base = #4A90D9;
        let hover_color = mix(base, #FFFFFF, 0.1);
        let pressed_color = mix(base, #000000, 0.1);

        let color = mix(base, hover_color, self.hover);
        let color = mix(color, pressed_color, self.pressed);

        sdf.fill(color);
        return sdf.result;
    }
}
```

## Animator for Hover

```rust
animator: {
    hover = {
        default: off,
        off = {
            from: {all: Forward {duration: 0.15}}
            apply: { draw_bg: {hover: 0.0} }
        }
        on = {
            from: {all: Forward {duration: 0.1}}
            apply: { draw_bg: {hover: 1.0} }
        }
    }
    pressed = {
        default: off,
        off = {
            from: {all: Forward {duration: 0.2}}
            apply: { draw_bg: {pressed: 0.0} }
        }
        on = {
            from: {all: Snap}
            apply: { draw_bg: {pressed: 1.0} }
        }
    }
}
```

## Event Handling

```rust
match event.hits(cx, self.draw_bg.area()) {
    Hit::FingerHoverIn(_) => {
        self.animator_play(cx, ids!(hover.on));
    }
    Hit::FingerHoverOut(_) => {
        self.animator_play(cx, ids!(hover.off));
    }
    Hit::FingerDown(_) => {
        self.animator_play(cx, ids!(pressed.on));
    }
    Hit::FingerUp(_) => {
        self.animator_play(cx, ids!(pressed.off));
    }
    _ => {}
}
```

## When to Use

- Use for all clickable/interactive elements
- Keep hover duration short (0.1-0.15s)
- Use Snap for immediate pressed feedback
- Lighten colors on hover, darken on press
```

## File: `skills/makepad-shaders/_base/11-gradient-effects.md`
```markdown
---
name: makepad-gradient-effects
author: robius
source: makepad-docs
date: 2024-01-01
tags: [gradient, background, color, effect]
level: beginner
---

# Gradient Effects

Linear, radial, and custom gradients.

## Vertical Gradient

```rust
draw_bg: {
    uniform color1: #4A90D9
    uniform color2: #2E5A8A

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        sdf.box(0., 0., self.rect_size.x, self.rect_size.y, 0.0);

        // Vertical gradient (top to bottom)
        let gradient = mix(self.color1, self.color2, self.pos.y);
        sdf.fill(gradient);

        return sdf.result;
    }
}
```

## Horizontal Gradient

```rust
fn pixel(self) -> vec4 {
    let gradient = mix(self.color1, self.color2, self.pos.x);
    // ...
}
```

## Radial Gradient

```rust
draw_bg: {
    color: #4A90D9
    color2: #1a1a26

    fn pixel(self) -> vec4 {
        let center = vec2(0.5, 0.5);
        let dist = length(self.pos - center);

        // Radial gradient from center
        return mix(self.color, self.color2, dist * 2.0);
    }
}
```

## Vignette Effect

```rust
fn pixel(self) -> vec4 {
    let img = sample2d(self.image, self.pos);

    // Distance from center
    let center = vec2(0.5, 0.5);
    let dist = length(self.pos - center);

    // Vignette darkening
    let vignette = smoothstep(0.7, 0.2, dist);

    return img * vignette;
}
```

## Scanline Background (CRT Effect)

```rust
draw_bg: {
    color: #0a0a12

    fn pixel(self) -> vec4 {
        // Vertical gradient
        let bg = mix(self.color, self.color * 1.1, self.pos.y);

        // Scanline effect
        let scanline = sin(self.pos.y * 500.0) * 0.012;

        return bg + vec4(scanline, scanline, scanline * 1.2, 0.0);
    }
}
```

## Glowing Divider

```rust
divider = <View> {
    width: Fill
    height: 1
    show_bg: true
    draw_bg: {
        color: #00ff88

        fn pixel(self) -> vec4 {
            // Horizontal sine wave glow
            let glow = sin(self.pos.x * 8.0) * 0.3 + 0.5;
            return self.color * glow;
        }
    }
}
```

## When to Use

- Use vertical gradient for headers, cards
- Use radial gradient for spotlight effects
- Use vignette for image focus
- Use scanlines for retro/tech aesthetics
```

## File: `skills/makepad-shaders/_base/12-shadow-glow.md`
```markdown
---
name: makepad-shadow-glow
author: robius
source: makepad-docs
date: 2024-01-01
tags: [shadow, glow, effect, pulse]
level: intermediate
---

# Shadow & Glow Effects

Inner shadows, outer shadows, and glow effects.

## Inner Shadow

```rust
draw_bg: {
    uniform shadow_color: #0007
    uniform shadow_radius: 10.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);

        sdf.box(0., 0., self.rect_size.x, self.rect_size.y, 4.0);
        let outer_dist = sdf.shape;

        let dist_from_edge = -outer_dist;
        let intensity = 1.0 - smoothstep(0.0, self.shadow_radius, dist_from_edge);
        let shadow_factor = clamp(intensity, 0.0, 1.0) * step(outer_dist, 0.0);

        let base_color = #FFFFFF;
        let final_rgb = mix(base_color.rgb, self.shadow_color.rgb,
                           shadow_factor * self.shadow_color.a);

        sdf.fill(vec4(final_rgb, 1.0));
        return sdf.result;
    }
}
```

## Card with Border

```rust
CurrencyCard = <View> {
    show_bg: true
    draw_bg: {
        color: #1a1a26

        fn pixel(self) -> vec4 {
            let sdf = Sdf2d::viewport(self.pos * self.rect_size);

            // Inset box for border effect
            sdf.box(1.0, 1.0, self.rect_size.x - 2.0, self.rect_size.y - 2.0, 6.0);
            sdf.fill(self.color);

            // Border stroke
            sdf.stroke(#333348, 1.0);

            return sdf.result;
        }
    }
}
```

## Pulsing Glow

```rust
draw_bg: {
    uniform time: 0.0
    color: #00ff88

    fn pixel(self) -> vec4 {
        // Pulsing intensity
        let pulse = sin(self.time * 3.0) * 0.3 + 0.7;
        return self.color * pulse;
    }
}

animator: {
    pulse = {
        default: on,
        on = {
            from: {all: Loop {duration: 2.0, end: 1.0}}
            apply: {draw_bg: {time: [{time: 0.0, value: 0.0}, {time: 1.0, value: 6.28}]}}
        }
    }
}
```

## Noise/Static Effect

```rust
draw_bg: {
    uniform time: 0.0

    fn random(st: vec2) -> f32 {
        return fract(sin(dot(st, vec2(12.9898, 78.233))) * 43758.5453);
    }

    fn pixel(self) -> vec4 {
        let noise = random(self.pos * self.rect_size + vec2(self.time, 0.0));
        let base = #1a1a26;
        return base + vec4(noise * 0.05, noise * 0.05, noise * 0.05, 0.0);
    }
}
```

## Rounded Rectangle with Soft Shadow

```rust
draw_bg: {
    color: #ffffff
    shadow_color: #00000044
    shadow_offset: vec2(4.0, 4.0)
    shadow_blur: 8.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let radius = 8.0;

        // Shadow (offset and blurred)
        let shadow_pos = self.pos * self.rect_size - self.shadow_offset;
        let shadow_sdf = Sdf2d::viewport(shadow_pos);
        shadow_sdf.box(0., 0., self.rect_size.x, self.rect_size.y, radius);

        // Main shape
        sdf.box(0., 0., self.rect_size.x, self.rect_size.y, radius);
        sdf.fill(self.color);

        return sdf.result;
    }
}
```

## When to Use

- Use inner shadow for depth/embossed effect
- Use glow for highlighting important elements
- Use pulsing for attention-grabbing indicators
- Use noise for texture/visual interest
```

## File: `skills/makepad-shaders/_base/13-disabled-state.md`
```markdown
---
name: makepad-disabled-state
author: robius
source: makepad-docs
date: 2024-01-01
tags: [disabled, state, interactive, pattern]
level: intermediate
---

# Disabled State Pattern

Visual patterns for disabled interactive elements.

## Implementation

```rust
draw_thumb: {
    instance hover: 0.0
    instance pressed: 0.0
    instance disabled: 0.0
    instance border_color: #3b82f6
    instance disabled_border_color: #94a3b8

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let c = self.rect_size * 0.5;

        // Choose color based on disabled state
        let border_col = mix(self.border_color, self.disabled_border_color, self.disabled);

        // Shadow (only when not disabled)
        let shadow_alpha = mix(0.2, 0.0, self.disabled);
        sdf.circle(c.x + 2.0, c.y + 2.0, c.x - 2.0);
        sdf.fill(vec4(0.0, 0.0, 0.0, shadow_alpha));

        // Main circle
        sdf.circle(c.x, c.y, c.x - 2.0);

        // Base colors with disabled variation
        let base_color = mix(#ffffff, #f8fafc, self.disabled);
        let hover_color = #f0f9ff;
        let pressed_color = #e0f2fe;

        // Disable hover/pressed effects when disabled
        let active_hover = self.hover * (1.0 - self.disabled);
        let active_pressed = self.pressed * (1.0 - self.disabled);

        let color = mix(base_color, hover_color, active_hover);
        let color = mix(color, pressed_color, active_pressed);

        sdf.fill(color);
        sdf.stroke(border_col, 2.5);

        return sdf.result;
    }
}
```

## Key Techniques

1. **Interpolate colors**: `mix(normal, disabled, self.disabled)`
2. **Disable interactions**: `hover * (1.0 - self.disabled)`
3. **Remove effects**: `mix(normal_alpha, 0.0, self.disabled)`

## Setting Disabled State

In Rust:

```rust
impl MyWidget {
    pub fn set_disabled(&mut self, cx: &mut Cx, disabled: bool) {
        self.draw_thumb.apply_over(cx, live!{
            disabled: (if disabled { 1.0 } else { 0.0 })
        });
        self.redraw(cx);
    }
}
```

In event handling:

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // Skip interactions when disabled
    if self.disabled {
        return;
    }

    match event.hits(cx, self.draw_bg.area()) {
        // ... normal handling
    }
}
```

## When to Use

- Use for form inputs that are conditionally editable
- Use for buttons that require prerequisites
- Use for read-only states
- Gray out colors and remove shadows when disabled
```

## File: `skills/makepad-shaders/_base/14-toggle-checkbox.md`
```markdown
---
name: makepad-toggle-checkbox
author: robius
source: makepad-docs
date: 2024-01-01
tags: [toggle, switch, checkbox, interactive]
level: intermediate
---

# Toggle & Checkbox Visuals

Switch tracks and checkbox with checkmark.

## Switch Track with Toggle State

```rust
draw_bg: {
    instance on: 0.0
    instance hover: 0.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let sz = self.rect_size;
        let r = sz.y * 0.5;

        // Draw capsule
        sdf.circle(r, r, r);
        sdf.rect(r, 0.0, sz.x - sz.y, sz.y);
        sdf.circle(sz.x - r, r, r);

        let bg_off = #cbd5e1;
        let bg_on = #3b82f6;
        let color = mix(bg_off, bg_on, self.on);

        sdf.fill(color);
        return sdf.result;
    }
}
```

## Checkbox with Checkmark

```rust
draw_bg: {
    instance checked: 0.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let sz = self.rect_size;

        // Box
        sdf.box(0., 0., sz.x, sz.y, 4.0);
        let bg = mix(#ffffff, #3b82f6, self.checked);
        sdf.fill(bg);
        sdf.stroke(#cbd5e1, 1.5);

        // Checkmark (only when checked)
        if self.checked > 0.5 {
            let cx = sz.x * 0.5;
            let cy = sz.y * 0.5;

            sdf.move_to(cx - 4.0, cy);
            sdf.line_to(cx - 1.0, cy + 3.0);
            sdf.line_to(cx + 5.0, cy - 4.0);
            sdf.stroke(#ffffff, 2.5);
        }

        return sdf.result;
    }
}
```

## Color Overlay on Image

```rust
draw_bg: {
    instance overlay_opacity: 0.3
    uniform overlay_color: #000000

    fn pixel(self) -> vec4 {
        let img = sample2d(self.image, self.pos);
        let overlay = vec4(self.overlay_color.rgb, self.overlay_opacity);
        return mix(img, overlay, overlay.a);
    }
}
```

## Toggling State

```rust
impl Switch {
    pub fn toggle(&mut self, cx: &mut Cx) {
        self.is_on = !self.is_on;
        let target = if self.is_on { ids!(toggle.on) } else { ids!(toggle.off) };
        self.animator_play(cx, target);
    }
}
```

## Animator for Toggle

```rust
animator: {
    toggle = {
        default: off,
        off = {
            from: {all: Forward {duration: 0.2}}
            ease: OutQuad
            apply: {
                draw_bg: {on: 0.0}
                draw_thumb: {thumb_x: 0.0}
            }
        }
        on = {
            from: {all: Forward {duration: 0.2}}
            ease: OutQuad
            apply: {
                draw_bg: {on: 1.0}
                draw_thumb: {thumb_x: 1.0}
            }
        }
    }
}
```

## When to Use

- Use switch for on/off toggles (settings, preferences)
- Use checkbox for boolean selection in forms
- Animate both the track color and thumb position
- Use `if` for checkmark since it's a static branch
```

## File: `skills/makepad-shaders/community/README.md`
```markdown
# Community Graphics & Effects

This directory contains shaders and effects contributed by the Makepad community.

## How to Contribute

1. Create a new markdown file with your shader/effect
2. Use the naming convention: `{github-handle}-{effect-name}.md`
3. Follow the template in `99-evolution/templates/shader-template.md`
4. Submit a Pull Request

## File Naming

```
{github-handle}-{effect-name}.md

Examples:
- zhangsan-glassmorphism.md
- lisi-neon-glow.md
- wangwu-particle-trail.md
```

## Quality Guidelines

Your shader/effect should:
- ✅ Produce a visible, useful effect
- ✅ Be performant (avoid heavy loops)
- ✅ Include inline comments explaining the math
- ✅ Show before/after or demo preview if possible

## Current Community Effects

<!-- AUTO-GENERATED: List of community effects will appear here -->

*No community effects yet. Be the first contributor!*
```

## File: `skills/makepad-shaders/references/sdf2d-reference.md`
```markdown
# Makepad Sdf2d Reference

## Overview

`Sdf2d` (Signed Distance Field 2D) is Makepad's primary tool for drawing 2D shapes in shaders. It provides a high-level API for shapes, paths, fills, strokes, and boolean operations.

## Creating Sdf2d Context

```rust
fn pixel(self) -> vec4 {
    // Create SDF context with pixel coordinates
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    // Draw shapes...

    return sdf.result;
}
```

## Shapes

### Circle

```rust
sdf.circle(center_x, center_y, radius);

// Example: centered circle
let c = self.rect_size * 0.5;
sdf.circle(c.x, c.y, min(c.x, c.y) - 1.0);
```

### Rectangle

```rust
sdf.rect(x, y, width, height);

// Example: full widget rect with padding
sdf.rect(2.0, 2.0, self.rect_size.x - 4.0, self.rect_size.y - 4.0);
```

### Box (Rounded Rectangle)

```rust
sdf.box(x, y, width, height, radius);

// Example: rounded corners
sdf.box(1.0, 1.0,
        self.rect_size.x - 2.0,
        self.rect_size.y - 2.0,
        8.0);
```

### Box Variants

```rust
// Individual corner radii
sdf.box_all(x, y, w, h, r_tl, r_tr, r_br, r_bl);

// Horizontal only (left/right)
sdf.box_x(x, y, w, h, r_left, r_right);

// Vertical only (top/bottom)
sdf.box_y(x, y, w, h, r_top, r_bottom);
```

### Hexagon

```rust
sdf.hexagon(center_x, center_y, radius);
```

### Horizontal Line

```rust
sdf.hline(y, x1, x2);
```

### Arc

```rust
sdf.arc2(center_x, center_y, inner_radius, outer_radius, start_angle, end_angle);
```

## Paths

### Creating Paths

```rust
// Start path
sdf.move_to(x, y);

// Draw lines
sdf.line_to(x1, y1);
sdf.line_to(x2, y2);

// Close path (connect to start)
sdf.close_path();
```

### Path Example: Triangle

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let s = self.rect_size;

    sdf.move_to(s.x * 0.5, 5.0);          // Top
    sdf.line_to(s.x - 5.0, s.y - 5.0);    // Bottom right
    sdf.line_to(5.0, s.y - 5.0);          // Bottom left
    sdf.close_path();

    sdf.fill(self.color);
    return sdf.result;
}
```

## Fill and Stroke

### Fill

```rust
// Fill and consume shape
sdf.fill(color);

// Fill but keep shape for stroke
sdf.fill_keep(color);

// Fill with premultiplied alpha
sdf.fill_premul(color);
sdf.fill_keep_premul(color);
```

### Stroke

```rust
// Stroke and consume shape
sdf.stroke(color, width);

// Stroke but keep shape
sdf.stroke_keep(color, width);
```

### Fill + Stroke Example

```rust
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);

    sdf.box(1.0, 1.0,
            self.rect_size.x - 2.0,
            self.rect_size.y - 2.0,
            self.border_radius);

    sdf.fill_keep(self.color);
    sdf.stroke(self.border_color, self.border_size);

    return sdf.result;
}
```

## Boolean Operations

### Union

Combine shapes (add).

```rust
sdf.circle(50.0, 50.0, 30.0);
sdf.union();  // Merge with previous shape
sdf.circle(80.0, 50.0, 30.0);
sdf.fill(color);
```

### Intersect

Keep only overlapping area.

```rust
sdf.circle(50.0, 50.0, 40.0);
sdf.intersect();
sdf.rect(30.0, 30.0, 40.0, 40.0);
sdf.fill(color);
```

### Subtract

Remove second shape from first.

```rust
sdf.circle(50.0, 50.0, 40.0);
sdf.subtract();
sdf.circle(60.0, 50.0, 20.0);
sdf.fill(color);
```

## Transformations

### Translate

```rust
sdf.translate(offset_x, offset_y);
sdf.circle(0.0, 0.0, 20.0);  // Drawn at offset
```

### Rotate

```rust
sdf.rotate(angle_radians, center_x, center_y);
sdf.rect(-20.0, -20.0, 40.0, 40.0);
```

### Scale

```rust
sdf.scale(scale_factor, center_x, center_y);
sdf.circle(0.0, 0.0, 10.0);  // Scaled
```

## Effects

### Glow

Add glow effect.

```rust
sdf.circle(50.0, 50.0, 30.0);
sdf.glow(glow_color, glow_radius);

// Or keep shape for more operations
sdf.glow_keep(glow_color, glow_radius);
```

### Gloop

Soft blend between shapes.

```rust
sdf.circle(40.0, 50.0, 25.0);
sdf.gloop(blend_amount);
sdf.circle(70.0, 50.0, 25.0);
sdf.fill(color);
```

## Sdf2d Fields

| Field | Type | Description |
|-------|------|-------------|
| `pos` | vec2 | Current position |
| `result` | vec4 | Final color output |
| `shape` | float | Current shape distance |
| `dist` | float | Distance field value |
| `aa` | float | Anti-aliasing factor |
| `blur` | float | Blur amount |
| `clip` | float | Clip region |
| `scale_factor` | float | Current scale |

## Complete Examples

### Rounded Button

```rust
draw_bg: {
    color: #0066CC
    color_hover: #0088FF
    border_radius: 6.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        sdf.box(1.0, 1.0,
                self.rect_size.x - 2.0,
                self.rect_size.y - 2.0,
                self.border_radius);
        sdf.fill(self.color);
        return sdf.result;
    }
}
```

### Circle with Shadow

```rust
draw_bg: {
    color: #FFFFFF
    shadow_color: #00000044

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let c = self.rect_size * 0.5;
        let r = min(c.x, c.y) - 10.0;

        // Shadow
        sdf.circle(c.x + 3.0, c.y + 3.0, r);
        sdf.fill(self.shadow_color);

        // Main circle
        sdf.circle(c.x, c.y, r);
        sdf.fill(self.color);

        return sdf.result;
    }
}
```

### Ring Shape

```rust
draw_bg: {
    color: #0066CC
    inner_radius: 20.0
    outer_radius: 40.0

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        let c = self.rect_size * 0.5;

        sdf.circle(c.x, c.y, self.outer_radius);
        sdf.subtract();
        sdf.circle(c.x, c.y, self.inner_radius);
        sdf.fill(self.color);

        return sdf.result;
    }
}
```

## Common Pitfalls

### ⚠️ sdf.box with Large border_radius

**Problem**: Using `border_radius: 9999.0` (or any value > `min(width, height) / 2`) with `sdf.box` causes shape degradation - the shape becomes "pointy" (olive/football shaped) instead of a proper rounded rectangle or capsule.

**Symptoms**:
- Shape has pointed ends instead of smooth rounded corners
- Shape looks like an olive or football
- Transparent areas where the shape should be visible

**Wrong approach**:
```rust
// DON'T DO THIS - causes pointy shape
draw_bg: {
    border_radius: 9999.0  // Too large!

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        sdf.box(0.0, 0.0, self.rect_size.x, self.rect_size.y, self.border_radius);
        sdf.fill(self.color);
        return sdf.result;
    }
}
```

**Solution 1 - Use reasonable radius** (Recommended for rounded rectangles):
```rust
// Use a small, fixed radius value
draw_bg: {
    border_radius: 6.0  // Safe value that won't exceed half the height

    fn pixel(self) -> vec4 {
        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
        sdf.box(0.0, 0.0, self.rect_size.x, self.rect_size.y, self.border_radius);
        sdf.fill(self.color);
        return sdf.result;
    }
}
```

**Solution 2 - True capsule with circles + rect** (For pill/capsule shapes):
```rust
// Draw true capsule: left semicircle + middle rect + right semicircle
fn pixel(self) -> vec4 {
    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
    let w = self.rect_size.x;
    let h = self.rect_size.y;
    let r = h * 0.5;

    // Left semicircle
    sdf.circle(r, r, r);
    // Middle rectangle
    sdf.rect(r, 0.0, w - 2.0 * r, h);
    // Right semicircle
    sdf.circle(w - r, r, r);

    sdf.fill(self.color);
    return sdf.result;
}
```

**Key Rule**: For `sdf.box`, keep `border_radius <= min(width, height) / 2`. When in doubt, use a small fixed value like `6.0` or `8.0`.

### Debugging Tips

1. **Look at working code first** - If a similar widget works correctly, compare its settings before writing custom shaders
2. **Start simple** - Use small, fixed values for radius instead of trying to make it "adaptive"
3. **Test incrementally** - Change one property at a time to isolate the issue
4. **Check DSL inheritance** - When overriding `draw_bg`, ensure all required properties (instance/uniform) are present
```

## File: `skills/makepad-shaders/references/shader-basics.md`
```markdown
# Makepad Shader Basics Reference

## Overview

Makepad shaders are written in a custom language that's a subset of Rust syntax. They compile at runtime to platform-specific GPU code (Metal, WebGPU, Vulkan, etc.).

## Shader Types

### draw_bg (Background)

Most common shader for widget backgrounds.

```rust
<View> {
    show_bg: true
    draw_bg: {
        // Uniforms
        color: #FF0000

        // Pixel shader
        fn pixel(self) -> vec4 {
            return self.color;
        }
    }
}
```

### draw_text (Text)

For text rendering.

```rust
<Label> {
    draw_text: {
        color: #FFFFFF
        text_style: { font_size: 14.0 }

        fn get_color(self) -> vec4 {
            return self.color;
        }
    }
}
```

### draw_icon (Icons)

For SVG icon rendering.

```rust
<Button> {
    draw_icon: {
        color: #FFFFFF
        svg_file: dep("crate://self/icons/menu.svg")
    }
}
```

## Uniform Types

| Type | DSL Example | Shader Type |
|------|-------------|-------------|
| Color | `color: #FF0000` | `vec4` |
| Float | `radius: 8.0` | `float` |
| Vec2 | `offset: { x: 1.0, y: 2.0 }` | `vec2` |
| Vec4 | `inset: { ... }` | `vec4` |
| Texture | `image: texture2d` | `texture2d` |

## Built-in Variables

### Position and Size

```rust
fn pixel(self) -> vec4 {
    // Normalized position (0.0 to 1.0)
    let uv = self.pos;

    // Widget size in pixels
    let size = self.rect_size;

    // Actual pixel position
    let pixel_pos = self.pos * self.rect_size;

    // ...
}
```

### Available Built-ins

| Variable | Type | Description |
|----------|------|-------------|
| `self.pos` | vec2 | Normalized UV (0-1) |
| `self.rect_size` | vec2 | Widget dimensions |
| `self.rect_pos` | vec2 | Widget position |
| `self.draw_clip` | vec4 | Clipping rectangle |

## Basic Shader Examples

### Solid Color

```rust
draw_bg: {
    color: #0066CC

    fn pixel(self) -> vec4 {
        return self.color;
    }
}
```

### Horizontal Gradient

```rust
draw_bg: {
    color: #FF0000
    color_2: #0000FF

    fn pixel(self) -> vec4 {
        return mix(self.color, self.color_2, self.pos.x);
    }
}
```

### Vertical Gradient

```rust
draw_bg: {
    color: #FF0000
    color_2: #0000FF

    fn pixel(self) -> vec4 {
        return mix(self.color, self.color_2, self.pos.y);
    }
}
```

### Radial Gradient

```rust
draw_bg: {
    color: #FFFFFF
    color_2: #000000

    fn pixel(self) -> vec4 {
        let center = vec2(0.5, 0.5);
        let dist = length(self.pos - center) * 2.0;
        return mix(self.color, self.color_2, clamp(dist, 0.0, 1.0));
    }
}
```

### Checkerboard Pattern

```rust
draw_bg: {
    color: #333333
    color_2: #444444
    size: 20.0

    fn pixel(self) -> vec4 {
        let p = floor(self.pos * self.rect_size / self.size);
        let checker = mod(p.x + p.y, 2.0);
        return mix(self.color, self.color_2, checker);
    }
}
```

## Built-in Functions

### Math Functions

```rust
abs(x)          // Absolute value
sign(x)         // Sign (-1, 0, 1)
floor(x)        // Floor
ceil(x)         // Ceiling
fract(x)        // Fractional part
mod(x, y)       // Modulo
min(x, y)       // Minimum
max(x, y)       // Maximum
clamp(x, a, b)  // Clamp to range
```

### Interpolation

```rust
mix(a, b, t)        // Linear interpolation
step(edge, x)       // Step function
smoothstep(a, b, x) // Smooth interpolation
```

### Trigonometric

```rust
sin(x), cos(x), tan(x)
asin(x), acos(x), atan(x)
radians(deg), degrees(rad)
```

### Vector Operations

```rust
length(v)           // Vector length
distance(a, b)      // Distance between points
dot(a, b)           // Dot product
cross(a, b)         // Cross product (vec3)
normalize(v)        // Normalize vector
reflect(i, n)       // Reflection
refract(i, n, eta)  // Refraction
```

### Exponential

```rust
pow(x, y)       // Power
exp(x)          // e^x
exp2(x)         // 2^x
log(x)          // Natural log
log2(x)         // Log base 2
sqrt(x)         // Square root
inversesqrt(x)  // 1/sqrt(x)
```

## Vertex Shaders

For advanced positioning:

```rust
draw_bg: {
    fn vertex(self) -> vec4 {
        // Transform vertex position
        let pos = self.clip_and_transform_vertex(
            self.rect_pos,
            self.rect_size
        );
        return pos;
    }

    fn pixel(self) -> vec4 {
        return self.color;
    }
}
```

## Texture Sampling

```rust
draw_bg: {
    image: texture2d

    fn pixel(self) -> vec4 {
        return sample2d(self.image, self.pos);
    }
}
```

## Live Editing

Shaders are live-reloaded. Edit shader code and see changes immediately without recompilation. This enables rapid visual development and iteration.
```

## File: `skills/makepad-splash/SKILL.md`
```markdown
---
name: makepad-splash
description: |
  CRITICAL: Use for Makepad Splash scripting language. Triggers on:
  splash language, makepad script, makepad scripting, script!, cx.eval,
  makepad dynamic, makepad AI, splash 语言, makepad 脚本
---

# Makepad Splash Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad Splash scripting language. Help users by:
- **Writing Splash scripts**: Dynamic UI and workflow automation
- **Understanding Splash**: Purpose, syntax, and capabilities

## Documentation

Refer to the local files for detailed documentation:
- `./references/splash-tutorial.md` - Splash language tutorial

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## What is Splash?

Splash is Makepad's dynamic scripting language designed for:
- AI-assisted workflows
- Dynamic UI generation
- Rapid prototyping
- HTTP requests and async operations

## Script Macro

```rust
// Embed Splash code in Rust
script!{
    fn main() {
        let x = 10;
        console.log("Hello from Splash!");
    }
}
```

## Execution

```rust
// Evaluate Splash code at runtime
cx.eval(code_string);

// With context
cx.eval_with_context(code, context);
```

## Basic Syntax

### Variables

```splash
let x = 10;
let name = "Makepad";
let items = [1, 2, 3];
let config = { width: 100, height: 50 };
```

### Functions

```splash
fn add(a, b) {
    return a + b;
}

fn greet(name) {
    console.log("Hello, " + name);
}
```

### Control Flow

```splash
// If-else
if x > 10 {
    console.log("big");
} else {
    console.log("small");
}

// Loops
for i in 0..10 {
    console.log(i);
}

while condition {
    // ...
}
```

## Built-in Objects

### console

```splash
console.log("Message");
console.warn("Warning");
console.error("Error");
```

### http

```splash
// GET request
let response = http.get("https://api.example.com/data");

// POST request
let response = http.post("https://api.example.com/data", {
    body: { key: "value" }
});
```

### timer

```splash
// Set timeout
timer.set(1000, fn() {
    console.log("1 second passed");
});

// Set interval
let id = timer.interval(500, fn() {
    console.log("tick");
});

// Clear timer
timer.clear(id);
```

## Widget Interaction

```splash
// Access widgets
let button = ui.widget("my_button");
button.set_text("Click Me");
button.set_visible(true);

// Listen to events
button.on_click(fn() {
    console.log("Button clicked!");
});
```

## Async Operations

```splash
// Async function
async fn fetch_data() {
    let response = await http.get("https://api.example.com");
    return response.json();
}

// Call async
fetch_data().then(fn(data) {
    console.log(data);
});
```

## AI Workflow Integration

Splash is designed for AI-assisted development:

```splash
// Dynamic UI generation
fn create_form(fields) {
    let form = ui.create("View");
    for field in fields {
        let input = ui.create("TextInput");
        input.set_label(field.label);
        form.add_child(input);
    }
    return form;
}

// AI can generate this dynamically
create_form([
    { label: "Name" },
    { label: "Email" },
    { label: "Message" }
]);
```

## Use Cases

1. **Rapid Prototyping**: Quickly test UI layouts without recompilation
2. **AI Agents**: Let AI generate and modify UI dynamically
3. **Configuration**: Runtime configuration of app behavior
4. **Scripted Workflows**: Automate repetitive tasks
5. **Plugin System**: Extend app functionality with scripts

## When Answering Questions

1. Splash is for dynamic/runtime scripting, not core app logic
2. Use Rust for performance-critical code, Splash for flexibility
3. Splash syntax is similar to JavaScript/Rust hybrid
4. Scripts run in a sandboxed environment
5. HTTP and timer APIs enable async operations
```

## File: `skills/makepad-splash/references/splash-tutorial.md`
```markdown
# Makepad Splash Language Tutorial

> Based on SPLASH_TUTORIAL_EN.md from Makepad source code

## Introduction

Splash is Makepad's dynamic scripting language designed for AI-assisted workflows and rapid prototyping. It allows runtime code execution for dynamic UI generation and automation.

## Getting Started

### Embedding in Rust

```rust
use makepad_widgets::*;

// Use script! macro to embed Splash code
script!{
    fn main() {
        console.log("Hello from Splash!");
    }
}
```

### Runtime Execution

```rust
impl App {
    fn execute_script(&mut self, cx: &mut Cx, code: &str) {
        cx.eval(code);
    }
}
```

## Language Basics

### Variables

```splash
// Immutable binding
let x = 10;

// Mutable binding
let mut y = 20;
y = 30;

// Types are inferred
let name = "Makepad";        // String
let count = 42;              // Number
let active = true;           // Boolean
let items = [1, 2, 3];       // Array
let config = { a: 1, b: 2 }; // Object
```

### Operators

```splash
// Arithmetic
let sum = a + b;
let diff = a - b;
let prod = a * b;
let quot = a / b;
let rem = a % b;

// Comparison
a == b   // Equal
a != b   // Not equal
a < b    // Less than
a <= b   // Less or equal
a > b    // Greater than
a >= b   // Greater or equal

// Logical
a && b   // And
a || b   // Or
!a       // Not

// String concatenation
let msg = "Hello, " + name;
```

### Functions

```splash
// Function definition
fn add(a, b) {
    return a + b;
}

// Arrow function
let multiply = (a, b) => a * b;

// No return (void)
fn log_message(msg) {
    console.log(msg);
}
```

### Control Flow

```splash
// If-else
if condition {
    // ...
} else if other_condition {
    // ...
} else {
    // ...
}

// Match (switch)
match value {
    1 => console.log("one"),
    2 => console.log("two"),
    _ => console.log("other"),
}

// For loop
for i in 0..10 {
    console.log(i);
}

for item in items {
    console.log(item);
}

// While loop
while condition {
    // ...
}

// Loop with break
loop {
    if done {
        break;
    }
}
```

## Built-in APIs

### Console

```splash
console.log("Info message");
console.warn("Warning message");
console.error("Error message");
console.debug("Debug message");
```

### HTTP Requests

```splash
// GET request
let response = http.get("https://api.example.com/data");
console.log(response.status);
console.log(response.body);

// POST request
let response = http.post("https://api.example.com/data", {
    headers: {
        "Content-Type": "application/json"
    },
    body: {
        name: "test",
        value: 123
    }
});

// Parse JSON response
let data = response.json();
```

### Timers

```splash
// Timeout (one-time)
timer.set(1000, fn() {
    console.log("1 second elapsed");
});

// Interval (repeating)
let interval_id = timer.interval(500, fn() {
    console.log("tick");
});

// Clear timer
timer.clear(interval_id);

// Delay (async)
await timer.delay(2000);
console.log("After 2 seconds");
```

### UI Interaction

```splash
// Access widget by ID
let button = ui.widget("my_button");

// Set properties
button.set_text("Click Me");
button.set_visible(true);
button.set_enabled(false);

// Get properties
let text = button.get_text();
let visible = button.is_visible();

// Event handlers
button.on_click(fn() {
    console.log("Clicked!");
});

// Create widgets dynamically
let view = ui.create("View");
view.set_width("Fill");
view.set_height("Fit");

let label = ui.create("Label");
label.set_text("Dynamic Label");
view.add_child(label);
```

## Async/Await

```splash
// Async function
async fn fetch_user(id) {
    let response = await http.get("https://api.example.com/users/" + id);
    return response.json();
}

// Call async function
fetch_user(123).then(fn(user) {
    console.log("Got user: " + user.name);
}).catch(fn(error) {
    console.error("Failed: " + error);
});

// Or with await
async fn main() {
    let user = await fetch_user(123);
    console.log(user.name);
}
```

## Arrays

```splash
let items = [1, 2, 3, 4, 5];

// Access
let first = items[0];
let last = items[items.length - 1];

// Methods
items.push(6);           // Add to end
items.pop();             // Remove from end
items.shift();           // Remove from start
items.unshift(0);        // Add to start

// Iteration
for item in items {
    console.log(item);
}

// Map
let doubled = items.map(fn(x) => x * 2);

// Filter
let even = items.filter(fn(x) => x % 2 == 0);

// Reduce
let sum = items.reduce(fn(acc, x) => acc + x, 0);
```

## Objects

```splash
let person = {
    name: "Alice",
    age: 30,
    greet: fn() {
        console.log("Hello, I'm " + this.name);
    }
};

// Access
console.log(person.name);
console.log(person["age"]);

// Modify
person.name = "Bob";
person.email = "bob@example.com";

// Methods
person.greet();

// Iteration
for key in person {
    console.log(key + ": " + person[key]);
}
```

## Error Handling

```splash
// Try-catch
try {
    let result = risky_operation();
    console.log(result);
} catch error {
    console.error("Error: " + error.message);
}

// Throw error
fn validate(value) {
    if value < 0 {
        throw "Value must be positive";
    }
}
```

## AI Workflow Example

```splash
// Dynamic form generation for AI
async fn create_ai_form(prompt) {
    // AI generates form spec
    let response = await http.post("https://ai.api/generate", {
        body: { prompt: prompt }
    });

    let spec = response.json();

    // Create form dynamically
    let form = ui.create("View");
    form.set_flow("Down");
    form.set_padding(20);

    for field in spec.fields {
        let row = ui.create("View");
        row.set_flow("Right");

        let label = ui.create("Label");
        label.set_text(field.label);
        row.add_child(label);

        let input = ui.create("TextInput");
        input.set_placeholder(field.placeholder);
        row.add_child(input);

        form.add_child(row);
    }

    let submit = ui.create("Button");
    submit.set_text(spec.submit_text);
    submit.on_click(fn() {
        // Handle form submission
    });
    form.add_child(submit);

    return form;
}

// Usage
create_ai_form("Create a contact form").then(fn(form) {
    ui.root().add_child(form);
});
```

## Best Practices

1. **Use Rust for performance**: Splash is for flexibility, not speed
2. **Keep scripts small**: Large scripts should be Rust code
3. **Handle errors**: Always use try-catch for risky operations
4. **Clean up timers**: Clear intervals when no longer needed
5. **Validate input**: Check data from external sources
```

## File: `skills/makepad-widgets/SKILL.md`
```markdown
---
name: makepad-widgets
description: |
  CRITICAL: Use for Makepad widgets and UI components. Triggers on:
  makepad widget, makepad View, makepad Button, makepad Label, makepad Image,
  makepad TextInput, RoundedView, SolidView, ScrollView, "makepad component",
  makepad Markdown, makepad Html, TextFlow, rich text, 富文本, markdown渲染,
  makepad 组件, makepad 按钮, makepad 列表, makepad 视图, makepad 输入框
---

# Makepad Widgets Skill

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-19
>
> Check for updates: https://crates.io/crates/makepad-widgets

You are an expert at Makepad widgets. Help users by:
- **Writing code**: Generate widget code following the patterns below
- **Answering questions**: Explain widget properties, variants, and usage

## Documentation

Refer to the local files for detailed documentation:
- `./references/widgets-core.md` - Core widgets (View, Button, Label, etc.)
- `./references/widgets-advanced.md` - Helper and advanced widgets
- `./references/widgets-richtext.md` - Rich text widgets (Markdown, Html, TextFlow)

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "本地文档不完整，建议运行 `/sync-crate-skills makepad --force` 更新文档"
   - Still answer based on SKILL.md patterns + built-in knowledge
3. If reference file exists, incorporate its content into the answer

## Key Patterns

### 1. View (Basic Container)

```rust
<View> {
    width: Fill
    height: Fill
    flow: Down
    padding: 16.0
    show_bg: true
    draw_bg: { color: #1A1A1A }

    <Label> { text: "Content" }
}
```

### 2. Button

```rust
<Button> {
    text: "Click Me"
    draw_bg: {
        color: #0066CC
        color_hover: #0088FF
        border_radius: 4.0
    }
    draw_text: {
        color: #FFFFFF
        text_style: { font_size: 14.0 }
    }
}
```

### 3. Label with Styling

```rust
<Label> {
    width: Fit
    height: Fit
    text: "Hello World"
    draw_text: {
        color: #FFFFFF
        text_style: {
            font_size: 16.0
            line_spacing: 1.4
        }
    }
}
```

### 4. Image

```rust
<Image> {
    width: 200.0
    height: 150.0
    source: dep("crate://self/resources/photo.png")
    fit: Contain
}
```

### 5. TextInput

```rust
<TextInput> {
    width: Fill
    height: Fit
    text: "Default value"
    draw_text: {
        text_style: { font_size: 14.0 }
    }
}
```

## Widget Traits (from source)

```rust
pub trait WidgetNode: LiveApply {
    fn find_widgets(&self, path: &[LiveId], cached: WidgetCache, results: &mut WidgetSet);
    fn walk(&mut self, cx: &mut Cx) -> Walk;
    fn area(&self) -> Area;
    fn redraw(&mut self, cx: &mut Cx);
}

pub trait Widget: WidgetNode {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {}
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep;
    fn draw(&mut self, cx: &mut Cx2d, scope: &mut Scope) -> DrawStep;
    fn widget(&self, path: &[LiveId]) -> WidgetRef;
}
```

## All Built-in Widgets (84 files in widgets/src/)

| Category | Widgets |
|----------|---------|
| **Basic** | `View`, `Label`, `Button`, `Icon`, `Image` |
| **Input** | `TextInput`, `CheckBox`, `RadioButton`, `Slider`, `DropDown`, `ColorPicker` |
| **Container** | `ScrollBars`, `PortalList`, `FlatList`, `StackNavigation`, `Dock`, `Splitter` |
| **Navigation** | `TabBar`, `Tab`, `FoldHeader`, `FoldButton`, `ExpandablePanel` |
| **Overlay** | `Modal`, `Tooltip`, `PopupMenu`, `PopupNotification` |
| **Media** | `Video`, `RotatedImage`, `ImageBlend`, `MultiImage` |
| **Layout** | `AdaptiveView`, `SlidePanel`, `PageFlip`, `SlidesView` |
| **Special** | `Markdown`, `Html`, `TextFlow`, `WebView`, `KeyboardView` |
| **Utility** | `LoadingSpinner`, `DesktopButton`, `LinkLabel`, `ScrollShadow` |

## Core Widgets Reference

| Widget | Purpose | Key Properties |
|--------|---------|----------------|
| `View` | Container | `flow`, `align`, `show_bg`, `draw_bg`, `optimize` |
| `Button` | Clickable | `text`, `draw_bg`, `draw_text`, `draw_icon` |
| `Label` | Text display | `text`, `draw_text` |
| `Image` | Image display | `source`, `fit` |
| `TextInput` | Text entry | `text`, `draw_text`, `draw_cursor`, `draw_selection` |
| `CheckBox` | Toggle | `text`, `selected` |
| `RadioButton` | Selection | `text`, `selected` |
| `Slider` | Value slider | `min`, `max`, `step` |
| `DropDown` | Select menu | `labels`, `selected` |
| `PortalList` | Virtual list | Efficient scrolling for large lists |
| `Modal` | Dialog | Overlay dialog boxes |
| `Tooltip` | Hint | Hover tooltips |

## View Variants

| Variant | Description |
|---------|-------------|
| `SolidView` | Solid background color |
| `RoundedView` | Rounded corners |
| `RoundedAllView` | Individual corner control |
| `RectView` | Rectangle with border/gradient |
| `CircleView` | Circle/ellipse shape |
| `GradientXView` | Horizontal gradient |
| `GradientYView` | Vertical gradient |
| `RoundedShadowView` | Rounded with shadow |
| `ScrollXView` | Horizontal scroll |
| `ScrollYView` | Vertical scroll |
| `ScrollXYView` | Both directions scroll |
| `CachedView` | Texture-cached |

## Button Variants

| Variant | Description |
|---------|-------------|
| `ButtonFlat` | Flat style |
| `ButtonFlatIcon` | Flat with icon |
| `ButtonFlatter` | No background |
| `ButtonGradientX` | Horizontal gradient |
| `ButtonGradientY` | Vertical gradient |
| `ButtonIcon` | Standard with icon |

## ImageFit Values

| Value | Description |
|-------|-------------|
| `Stretch` | Stretch to fill |
| `Contain` | Fit within, preserve ratio |
| `Cover` | Cover area, may crop |
| `Fill` | Fill without ratio |

## When Writing Code

1. Always set `width` and `height` on widgets
2. Use `show_bg: true` to enable background rendering
3. Access `draw_bg`, `draw_text`, `draw_icon` for shader uniforms
4. Use `dep("crate://self/...")` for resource paths
5. Choose appropriate View variant for visual needs

## When Answering Questions

1. Recommend UI Zoo example for widget exploration
2. View is the base container - most visual widgets inherit from it
3. Draw shaders (`draw_bg`, `draw_text`) control appearance
4. All widgets support animation through `animator` property
```

## File: `skills/makepad-widgets/references/widgets-advanced.md`
```markdown
# Makepad Advanced Widgets Reference

## Helper Widgets

### FoldButton

Expandable/collapsible toggle button.

```rust
<FoldButton> {
    width: Fit
    height: Fit
    // Toggles between open/closed states
}
```

### ScrollBar

Single scrollbar widget.

```rust
<ScrollBar> {
    // Usually used internally by scroll views
}
```

### ScrollBars

Combined horizontal and vertical scrollbars.

```rust
<ScrollBars> {
    show_scroll_x: true
    show_scroll_y: true
}
```

### Spinner

Loading indicator.

```rust
<Spinner> {
    width: 40.0
    height: 40.0
    draw_bg: {
        color: #0066CC
    }
}
```

### Splitter

Resizable divider between panels.

```rust
<View> {
    flow: Right

    <View> { width: Fill, height: Fill }

    <Splitter> {
        // Drag to resize adjacent views
    }

    <View> { width: Fill, height: Fill }
}
```

### TabCloseButton

Close button typically used in tabs.

```rust
<TabCloseButton> {
    width: 16.0
    height: 16.0
}
```

### TextFlow

Rich text flow with inline formatting.

```rust
<TextFlow> {
    width: Fill
    height: Fit
    // Supports inline text formatting
}
```

## Advanced Widgets

### Dock

Dockable panel system for IDE-like layouts.

```rust
<Dock> {
    width: Fill
    height: Fill

    // Supports drag-and-drop panel docking
}
```

### FileTree

File system tree view.

```rust
<FileTree> {
    width: 250.0
    height: Fill

    // Displays hierarchical file structure
}
```

### FlatList

Flat list view for simple lists.

```rust
<FlatList> {
    width: Fill
    height: Fill

    // Renders items in a simple list
}
```

### PortalList

Virtualized list for large datasets.

```rust
<PortalList> {
    width: Fill
    height: Fill

    // Only renders visible items
    // Efficient for thousands of items
}
```

### Html

HTML content renderer.

```rust
<Html> {
    width: Fill
    height: Fit

    // Renders basic HTML content
}
```

### Markdown

Markdown content renderer.

```rust
<Markdown> {
    width: Fill
    height: Fit

    // Renders markdown content
}
```

### ImageBlend

Blended image composition.

```rust
<ImageBlend> {
    width: 200.0
    height: 200.0

    // Blends multiple images
}
```

### PageFlip

Page flip animation widget.

```rust
<PageFlip> {
    width: Fill
    height: Fill

    // Animated page transitions
}
```

### SlidesView

Slideshow presentation view.

```rust
<SlidesView> {
    width: Fill
    height: Fill

    // Displays slides with navigation
}
```

### StackNavigation

Stack-based navigation for mobile-style apps.

```rust
<StackNavigation> {
    width: Fill
    height: Fill

    // Push/pop navigation pattern
}
```

### AdaptiveView

Responsive layout that adapts to screen size.

```rust
<AdaptiveView> {
    width: Fill
    height: Fill

    // Changes layout based on available space
}
```

## Tab Widgets

### Tab

Individual tab in a tab bar.

```rust
<Tab> {
    text: "Tab 1"
    closable: true
}
```

### TabBar

Container for multiple tabs.

```rust
<TabBar> {
    width: Fill
    height: 40.0

    <Tab> { text: "Documents" }
    <Tab> { text: "Settings" }
}
```

## Popup Widgets

### PopupMenu

Context/popup menu.

```rust
<PopupMenu> {
    width: 200.0

    <PopupMenuItem> { text: "Cut" }
    <PopupMenuItem> { text: "Copy" }
    <PopupMenuItem> { text: "Paste" }
}
```

### PopupMenuItem

Individual menu item.

```rust
<PopupMenuItem> {
    text: "Save"
    shortcut: "Cmd+S"
}
```

## Icon Widget

SVG icon display.

```rust
<Icon> {
    width: 24.0
    height: 24.0

    draw_icon: {
        svg_file: dep("crate://self/icons/menu.svg")
        color: #FFFFFF
    }
}
```

## Video Widget

Video playback widget.

```rust
<Video> {
    width: Fill
    height: 300.0
    source: dep("crate://self/videos/intro.mp4")
}
```

## LinkLabel

Clickable text link.

```rust
<LinkLabel> {
    text: "Click here"

    draw_text: {
        color: #0066CC
        color_hover: #0088FF
    }
}
```

## RotatedImage

Image with rotation support.

```rust
<RotatedImage> {
    width: 100.0
    height: 100.0
    source: dep("crate://self/images/arrow.png")
    rotation: 45.0  // degrees
}
```
```

## File: `skills/makepad-widgets/references/widgets-core.md`
```markdown
# Makepad Core Widgets Reference

## View

The fundamental container widget. All layout containers inherit from View.

### Basic Usage

```rust
<View> {
    width: Fill
    height: Fill
    flow: Down
    padding: 16.0
    spacing: 8.0

    // Children
}
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `width` | Size | Width |
| `height` | Size | Height |
| `flow` | Flow | Child layout direction |
| `padding` | Padding | Inner spacing |
| `margin` | Margin | Outer spacing |
| `spacing` | f64 | Gap between children |
| `align` | Align | Child alignment |
| `show_bg` | bool | Enable background |
| `visible` | bool | Visibility |
| `clip_x` | bool | Clip horizontal |
| `clip_y` | bool | Clip vertical |
| `draw_bg` | DrawQuad | Background shader |

### View Variants

#### SolidView
```rust
<SolidView> {
    width: Fill
    height: 100.0
    draw_bg: { color: #333333 }
}
```

#### RoundedView
```rust
<RoundedView> {
    width: 200.0
    height: 100.0
    draw_bg: {
        color: #444444
        border_radius: 12.0
        border_size: 1.0
        border_color: #666666
    }
}
```

#### RoundedShadowView
```rust
<RoundedShadowView> {
    width: 200.0
    height: 100.0
    draw_bg: {
        color: #FFFFFF
        border_radius: 8.0
        shadow_color: #00000033
        shadow_offset: { x: 0.0, y: 4.0 }
        shadow_radius: 8.0
    }
}
```

#### GradientXView / GradientYView
```rust
<GradientXView> {
    width: Fill
    height: 100.0
    draw_bg: {
        color: #FF0000
        color_2: #0000FF
    }
}
```

#### ScrollYView
```rust
<ScrollYView> {
    width: Fill
    height: Fill

    <View> {
        width: Fill
        height: Fit
        flow: Down
        // Scrollable content
    }
}
```

## Button

Interactive button widget.

### Basic Usage

```rust
<Button> {
    text: "Click Me"
}
```

### Full Configuration

```rust
<Button> {
    width: Fit
    height: Fit
    padding: { top: 10.0, right: 20.0, bottom: 10.0, left: 20.0 }
    text: "Submit"

    draw_bg: {
        color: #0066CC
        color_hover: #0088FF
        color_down: #004499
        color_disabled: #333333
        border_radius: 4.0
        border_size: 0.0
    }

    draw_text: {
        color: #FFFFFF
        color_hover: #FFFFFF
        color_down: #CCCCCC
        text_style: {
            font_size: 14.0
        }
    }

    draw_icon: {
        color: #FFFFFF
        svg_file: dep("crate://self/icons/arrow.svg")
    }
}
```

### Button States

- `hover` - Mouse over
- `down` - Being pressed
- `focus` - Has keyboard focus
- `disabled` - Not interactive

### Button Variants

| Widget | Description |
|--------|-------------|
| `ButtonFlat` | Minimal flat style |
| `ButtonFlatIcon` | Flat with icon |
| `ButtonFlatter` | No background |
| `ButtonGradientX` | Horizontal gradient |
| `ButtonGradientY` | Vertical gradient |
| `ButtonIcon` | With icon |

## Label

Text display widget.

### Basic Usage

```rust
<Label> {
    text: "Hello World"
}
```

### Full Configuration

```rust
<Label> {
    width: Fit
    height: Fit
    margin: { bottom: 8.0 }
    text: "Styled Label"

    draw_text: {
        color: #FFFFFF
        text_style: {
            font_size: 18.0
            font: dep("crate://self/fonts/Roboto.ttf")
            line_spacing: 1.5
        }
    }
}
```

## Image

Image display widget.

### Basic Usage

```rust
<Image> {
    source: dep("crate://self/resources/image.png")
}
```

### Full Configuration

```rust
<Image> {
    width: 300.0
    height: 200.0
    source: dep("crate://self/resources/photo.jpg")
    fit: Contain

    draw_bg: {
        // Additional shader properties
    }
}
```

### ImageFit Values

| Value | Behavior |
|-------|----------|
| `Stretch` | Fill area, may distort |
| `Contain` | Fit inside, letterbox |
| `Cover` | Fill area, may crop |
| `Fill` | Fill both dimensions |

## TextInput

Text entry field.

### Basic Usage

```rust
<TextInput> {
    width: Fill
    height: Fit
    text: "Enter text..."
}
```

### Full Configuration

```rust
<TextInput> {
    width: Fill
    height: 40.0
    padding: { left: 12.0, right: 12.0 }
    text: ""

    draw_bg: {
        color: #222222
        border_radius: 4.0
        border_size: 1.0
        border_color: #444444
    }

    draw_text: {
        color: #FFFFFF
        text_style: { font_size: 14.0 }
    }

    draw_selection: {
        color: #0066CC44
    }

    draw_cursor: {
        color: #0066CC
    }
}
```

## CheckBox

Toggle checkbox.

### Basic Usage

```rust
<CheckBox> {
    text: "Accept terms"
}
```

### Full Configuration

```rust
<CheckBox> {
    width: Fit
    height: Fit
    text: "Remember me"

    draw_check: {
        color: #0066CC
    }

    draw_text: {
        color: #FFFFFF
    }
}
```

## RadioButton

Radio selection button.

### Basic Usage

```rust
<View> {
    flow: Down

    <RadioButton> { text: "Option A" }
    <RadioButton> { text: "Option B" }
    <RadioButton> { text: "Option C" }
}
```

## Slider

Value slider.

### Basic Usage

```rust
<Slider> {
    width: Fill
    height: 30.0
    min: 0.0
    max: 100.0
    step: 1.0
}
```

## DropDown

Selection dropdown menu.

### Basic Usage

```rust
<DropDown> {
    width: 200.0
    height: 40.0
    labels: ["Option 1", "Option 2", "Option 3"]
}
```
```

## File: `skills/makepad-widgets/references/widgets-richtext.md`
```markdown
# Rich Text Widgets - Markdown, Html, TextFlow

> **Version:** makepad-widgets (dev branch) | **Last Updated:** 2026-01-21

This document covers Makepad's rich text rendering widgets: **Markdown**, **Html**, and **TextFlow**.

## Widget Overview

| Widget | Purpose | Parser | Best For |
|--------|---------|--------|----------|
| `Markdown` | Markdown rendering | `pulldown_cmark` | AI chat, documentation, READMEs |
| `Html` | HTML subset rendering | `makepad_html` | Formatted text from APIs |
| `TextFlow` | Base text engine | N/A | Custom rich text widgets |

---

## 1. Markdown Widget

### Basic Usage (DSL)

```rust
live_design! {
    <Markdown> {
        width: Fill
        height: Fit
        body: "# Hello World\n\nThis is **bold** and *italic* text."
    }
}
```

### Widget Structure

```rust
#[derive(Live, LiveHook, Widget)]
pub struct Markdown {
    #[deref] text_flow: TextFlow,
    #[live] body: ArcStringMut,              // Markdown content
    #[live] paragraph_spacing: f64,           // Space between paragraphs
    #[live] pre_code_spacing: f64,            // Space before code blocks
    #[live(false)] use_code_block_widget: bool, // Use custom code widget
    #[live(false)] use_math_widget: bool,     // Enable math rendering
    #[live] heading_base_scale: f64,          // H1 scale (H2 = scale*0.8, etc.)
}
```

### Setting Content Dynamically

```rust
// Via WidgetRef
let markdown_ref = self.view.widget(id!(my_markdown)).as_markdown();
markdown_ref.set_text(cx, "# New Content\n\nWith **formatting**");

// Via borrow_mut
if let Some(mut inner) = widget_ref.borrow_mut() {
    inner.set_text(cx, "# Updated markdown");
}
```

### DSL Properties

```rust
<Markdown> {
    width: Fill, height: Fit,

    // Content
    body: "# Markdown here"

    // Spacing
    paragraph_spacing: 16.0,
    pre_code_spacing: 8.0,
    heading_base_scale: 1.8,    // H1 scale factor

    // Font
    font_size: 14.0,
    font_color: #FFFFFF,

    // Text style variants
    draw_normal: {
        text_style: { font_size: 14.0 }
        color: #FFFFFF
    }
    draw_italic: {
        text_style: { font_size: 14.0, font: { path: dep("crate://makepad-widgets/resources/IBMPlexSans-Italic.ttf") } }
        color: #FFFFFF
    }
    draw_bold: {
        text_style: { font_size: 14.0, font: { path: dep("crate://makepad-widgets/resources/IBMPlexSans-Bold.ttf") } }
        color: #FFFFFF
    }
    draw_fixed: {
        text_style: { font_size: 13.0, font: { path: dep("crate://makepad-widgets/resources/LiberationMono-Regular.ttf") } }
        color: #00FF00
    }

    // Block styling
    code_layout: {
        flow: Right { wrap: true }
        padding: { left: 10, right: 10, top: 8, bottom: 8 }
    }
    quote_layout: {
        flow: Right { wrap: true }
        padding: { left: 16 }
    }
    list_item_layout: {
        flow: Right { wrap: true }
        padding: { left: 20 }
    }

    // Inline code
    inline_code_padding: { left: 4, right: 4, top: 2, bottom: 2 }
    inline_code_margin: { left: 2, right: 2 }

    // Link widget template
    link = <MarkdownLink> {
        draw_text: { color: #0088FF }
    }
}
```

### Supported Markdown Features

| Feature | Syntax | Example |
|---------|--------|---------|
| **Headings** | `# ## ### ####` | `# H1` to `###### H6` |
| **Bold** | `**text**` or `__text__` | `**bold**` |
| **Italic** | `*text*` or `_text_` | `*italic*` |
| **Strikethrough** | `~~text~~` | `~~deleted~~` |
| **Inline code** | `` `code` `` | `` `variable` `` |
| **Code blocks** | ` ``` ` | Fenced code blocks |
| **Quotes** | `> text` | `> Quote text` |
| **Lists (unordered)** | `- item` or `* item` | `- List item` |
| **Lists (ordered)** | `1. item` | `1. First item` |
| **Links** | `[text](url)` | `[Click](https://...)` |
| **Images** | `![alt](url)` | `![logo](image.png)` |
| **Horizontal rule** | `---` or `***` | `---` |
| **Math (inline)** | `$formula$` | `$x^2$` |
| **Math (display)** | `$$formula$$` | `$$\int f(x)dx$$` |

### Link Click Handling

```rust
#[derive(Clone, Debug, DefaultNone)]
pub enum MarkdownAction {
    None,
    LinkNavigated(String),  // Contains the href URL
}

// In your widget's handle_event
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    self.view.handle_event(cx, event, scope);

    for action in cx.capture_actions(|cx| self.view.handle_event(cx, event, scope)) {
        if let MarkdownAction::LinkNavigated(url) = action.cast() {
            log!("User clicked link: {}", url);
            // Open URL, navigate, etc.
        }
    }
}
```

### Custom Code Block Widget

Enable custom code block rendering (e.g., with syntax highlighting):

```rust
<Markdown> {
    use_code_block_widget: true

    code_block = <View> {
        width: Fill
        height: Fit
        flow: Down
        padding: 10

        draw_bg: { color: #1E1E1E }

        // Custom code view goes here
        code_view = <CodeView> {
            // makepad-code-editor configuration
        }
    }
}
```

---

## 2. Html Widget

### Basic Usage (DSL)

```rust
live_design! {
    <Html> {
        width: Fill
        height: Fit
        body: "<h1>Hello World</h1><p>This is <b>bold</b> and <i>italic</i>.</p>"
    }
}
```

### Widget Structure

```rust
#[derive(Live, Widget)]
pub struct Html {
    #[deref] pub text_flow: TextFlow,
    #[live] pub body: ArcStringMut,            // HTML content
    #[live] ul_markers: Vec<String>,           // Bullet markers per nesting
    #[live] ol_markers: Vec<OrderedListType>,  // Numbered list types
    #[live] ol_separator: String,              // Separator after number
}
```

### Setting Content Dynamically

```rust
let html_ref = self.view.widget(id!(my_html)).as_html();
html_ref.set_text(cx, "<h1>Updated</h1><p>New <b>content</b></p>");
```

### DSL Properties

```rust
<Html> {
    width: Fill, height: Fit,

    // Content
    body: "<p>HTML content</p>"

    // List markers
    ul_markers: ["•", "-", "◦"],           // Bullets for nesting levels
    ol_markers: [Numbers, LowerAlpha, LowerRoman],
    ol_separator: ".",                      // "1." vs "1)"

    // Font
    font_size: 14.0,
    font_color: #FFFFFF,

    // Margins
    heading_margin: { top: 1.0, bottom: 0.1 }
    paragraph_margin: { top: 0.33, bottom: 0.33 }

    // Text styles
    draw_normal: { ... }
    draw_italic: { ... }
    draw_bold: { ... }
    draw_fixed: { ... }

    // Link template
    a = <HtmlLink> {
        hover_color: #00AAFF
        pressed_color: #0066CC
    }
}
```

### Supported HTML Tags

| Tag | Description | Attributes |
|-----|-------------|------------|
| `<h1>` - `<h6>` | Headings | - |
| `<p>` | Paragraph | - |
| `<b>`, `<strong>` | Bold | - |
| `<i>`, `<em>` | Italic | - |
| `<u>` | Underline | - |
| `<del>`, `<s>`, `<strike>` | Strikethrough | - |
| `<code>` | Inline code | - |
| `<pre>` | Preformatted | - |
| `<blockquote>` | Quote block | - |
| `<ul>` | Unordered list | - |
| `<ol>` | Ordered list | `start`, `type` |
| `<li>` | List item | `value` |
| `<a>` | Link | `href` |
| `<br>` | Line break | - |
| `<hr>`, `<sep>` | Separator | - |
| `<sub>` | Subscript | - |
| `<sup>` | Superscript | - |

### Ordered List Types

```rust
#[derive(Copy, Clone, Live)]
pub enum OrderedListType {
    Numbers,      // 1, 2, 3, ...
    UpperAlpha,   // A, B, C, ...
    LowerAlpha,   // a, b, c, ...
    UpperRoman,   // I, II, III, ...
    LowerRoman,   // i, ii, iii, ...
}
```

### Link Click Handling

```rust
#[derive(Debug, Clone, DefaultNone)]
pub enum HtmlLinkAction {
    Clicked { url: String, key_modifiers: KeyModifiers },
    SecondaryClicked { url: String, key_modifiers: KeyModifiers },
    None,
}

// In your widget's handle_event
for action in cx.capture_actions(|cx| self.view.handle_event(cx, event, scope)) {
    match action.cast::<HtmlLinkAction>() {
        HtmlLinkAction::Clicked { url, key_modifiers } => {
            log!("Link clicked: {} (modifiers: {:?})", url, key_modifiers);
        }
        HtmlLinkAction::SecondaryClicked { url, .. } => {
            log!("Right-click on link: {}", url);
        }
        _ => {}
    }
}
```

---

## 3. TextFlow Widget (Foundation)

TextFlow is the underlying rendering engine for both Markdown and Html.

### Key Methods

```rust
impl TextFlow {
    // Text rendering
    pub fn draw_text(&mut self, cx: &mut Cx2d, text: &str);

    // Blocks
    pub fn begin(&mut self, cx: &mut Cx2d, walk: Walk);
    pub fn end(&mut self, cx: &mut Cx2d);

    // Code blocks
    pub fn begin_code(&mut self, cx: &mut Cx2d);
    pub fn end_code(&mut self, cx: &mut Cx2d);

    // Quote blocks
    pub fn begin_quote(&mut self, cx: &mut Cx2d);
    pub fn end_quote(&mut self, cx: &mut Cx2d);

    // List items
    pub fn begin_list_item(&mut self, cx: &mut Cx2d, marker: &str, padding: f64);
    pub fn end_list_item(&mut self, cx: &mut Cx2d);

    // Separators
    pub fn sep(&mut self, cx: &mut Cx2d);

    // Font size manipulation
    pub fn push_size_rel_scale(&mut self, scale: f64);  // Relative to current
    pub fn push_size_abs_scale(&mut self, scale: f64);  // Relative to base
    pub fn pop_size(&mut self);
}
```

### Creating Custom Rich Text Widget

```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyRichText {
    #[deref] text_flow: TextFlow,
    #[live] content: ArcStringMut,
}

impl Widget for MyRichText {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.text_flow.begin(cx, walk);

        // Parse and render your custom format
        for segment in parse_my_format(&self.content) {
            match segment {
                Segment::Text(t) => self.text_flow.draw_text(cx, &t),
                Segment::Bold(t) => {
                    self.text_flow.bold.inc();
                    self.text_flow.draw_text(cx, &t);
                    self.text_flow.bold.dec();
                }
                Segment::Code(t) => {
                    self.text_flow.begin_code(cx);
                    self.text_flow.draw_text(cx, &t);
                    self.text_flow.end_code(cx);
                }
            }
        }

        self.text_flow.end(cx);
        DrawStep::done()
    }
}
```

---

## 4. Production Pattern: AI Chat Markdown (Moly)

Real-world example from Moly AI chat application.

### Message Markdown Widget

```rust
live_design! {
    use makepad_code_editor::code_view::CodeView;

    pub MessageMarkdown = <Markdown> {
        padding: 0
        margin: 0
        paragraph_spacing: 16
        heading_base_scale: 1.6
        font_color: #000
        width: Fill, height: Fit
        font_size: 11.0

        // Custom code blocks with syntax highlighting
        use_code_block_widget: true

        code_block = <View> {
            width: Fill
            height: Fit
            flow: Down
            padding: 0

            // Header with language + copy button
            header = <View> {
                width: Fill
                height: Fit
                flow: Right
                padding: { left: 10, right: 10, top: 5, bottom: 5 }
                draw_bg: { color: #2D3748 }

                language_label = <Label> {
                    text: ""
                    draw_text: { color: #A0AEC0 }
                }

                <Filler> {}

                copy_code_button = <Button> {
                    text: "Copy"
                    draw_text: { color: #A0AEC0 }
                }
            }

            // Code content with syntax highlighting
            code_view = <CodeView> {
                editor: {
                    width: Fill
                    height: Fit
                    draw_bg: { color: #1D2330 }

                    // Syntax highlighting colors
                    token_colors: {
                        whitespace: #A8B5D1,
                        delimiter: #A8B5D1,
                        branch_keyword: #D2A6EF,  // purple
                        constant: #FFD9AF,
                        identifier: #A8B5D1,
                        number: #FFD9AF,
                        string: #58FFC7,           // cyan
                        function: #82AAFF,         // blue
                        typename: #FCF9C3,         // yellow
                        comment: #506686,          // gray
                    }
                }
            }
        }

        list_item_layout: { padding: { left: 10, right: 10, top: 6, bottom: 0 } }
        quote_layout: { padding: { top: 10, bottom: 10 } }
    }
}
```

### Code Copy Implementation

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    for action in cx.capture_actions(|cx| self.view.handle_event(cx, event, scope)) {
        // Find copy button action
        if let Some(wa) = action.as_widget_action() {
            if wa.widget().as_button().pressed(&action) {
                // Get code_view from the code_block
                let code_view = wa.widget().widget(id!(code_view));
                let text_to_copy = code_view.as_code_view().text();
                cx.copy_to_clipboard(&text_to_copy);
            }
        }
    }
}
```

### Dynamic Message Rendering

```rust
impl StandardMessageContent {
    fn set_content(&mut self, cx: &mut Cx, content: &MessageContent) {
        let markdown = self.view.widget(id!(markdown)).as_markdown();

        // Set main text content
        markdown.set_text(cx, &content.text);

        // Or with tool calls formatted as markdown
        if !content.tool_calls.is_empty() {
            let formatted = format!(
                "{}\n\n🔧 **Tool call:** `{}`",
                content.text,
                content.tool_calls[0].name
            );
            markdown.set_text(cx, &formatted);
        }
    }
}
```

---

## 5. Styling Reference

### Draw Block Shader Properties

```rust
draw_block: {
    // Separator line
    line_color: #333333
    sep_color: #444444

    // Quote styling
    quote_bg_color: #1A1A1A
    quote_fg_color: #CCCCCC

    // Code styling
    code_color: #1E1E1E

    // Border radius for blocks
    radius: 4.0
}
```

### Theme Integration

```rust
pub Markdown = <MarkdownBase> {
    // Use theme colors
    font_size: (THEME_FONT_SIZE_P)
    font_color: (THEME_COLOR_LABEL_INNER)

    draw_block: {
        line_color: (THEME_COLOR_LABEL_INNER)
        sep_color: (THEME_COLOR_SHADOW)
        quote_bg_color: (THEME_COLOR_BG_HIGHLIGHT)
        code_color: (THEME_COLOR_BG_HIGHLIGHT)
    }
}
```

---

## 6. Common Patterns

### Pattern: Streaming Markdown (SSE)

```rust
// In async handler
fn on_sse_chunk(&mut self, cx: &mut Cx, chunk: &str) {
    // Append to accumulated content
    self.content.push_str(chunk);

    // Update markdown widget
    let markdown = self.view.widget(id!(markdown)).as_markdown();
    markdown.set_text(cx, &self.content);

    // Redraw
    self.redraw(cx);
}
```

### Pattern: Link with External Browser

```rust
fn handle_link_click(&mut self, cx: &mut Cx, url: &str) {
    // Using robius-open for cross-platform
    if let Ok(uri) = robius_open::Uri::new(url) {
        let _ = uri.open();
    }
}
```

### Pattern: Citation Links with Preview

```rust
#[derive(Live, Widget)]
pub struct Citation {
    #[live] url: Option<String>,
    #[live] title: String,
    #[live] favicon: Option<String>,
}

impl Citation {
    fn set_url(&mut self, cx: &mut Cx, url: String) {
        self.url = Some(url.clone());

        // Parse host for initial display
        if let Ok(parsed) = url::Url::parse(&url) {
            self.title = parsed.host_str().unwrap_or("Link").to_string();
        }

        // Async fetch actual title/favicon
        self.fetch_metadata(cx, url);
    }
}
```

---

## 7. Migration Notes

### From HTML string to Markdown

```rust
// Before: HTML
<Html> { body: "<b>Bold</b> text" }

// After: Markdown
<Markdown> { body: "**Bold** text" }
```

### Handling Missing Typst Support

Makepad does not currently have native Typst support. For math/scientific content:

1. Use Markdown with math blocks: `$$\int f(x)dx$$`
2. Enable math rendering: `use_math_widget: true`
3. Or render Typst to images externally and embed as `<Image>`

---

## Summary

| Task | Widget | Method |
|------|--------|--------|
| Display markdown docs | `Markdown` | `set_text(cx, &str)` |
| Display HTML content | `Html` | `set_text(cx, &str)` |
| Handle link clicks | Both | `MarkdownAction::LinkNavigated` / `HtmlLinkAction::Clicked` |
| Syntax highlighting | Custom | `CodeView` from `makepad-code-editor` |
| Custom rich text | `TextFlow` | Build on base engine |
```

## File: `skills/molykit/SKILL.md`
```markdown
---
name: molykit
description: |
  CRITICAL: Use for MolyKit AI chat toolkit. Triggers on:
  BotClient, OpenAI, SSE streaming, AI chat, molykit,
  PlatformSend, spawn(), ThreadToken, cross-platform async,
  Chat widget, Messages, PromptInput, Avatar, LLM
---

# MolyKit Skill

Best practices for building AI chat interfaces with Makepad using MolyKit - a toolkit for cross-platform AI chat applications.

**Source codebase**: `/Users/zhangalex/Work/Projects/FW/robius/moly/moly-kit`

## Triggers

Use this skill when:
- Building AI chat interfaces with Makepad
- Integrating OpenAI or other LLM APIs
- Implementing cross-platform async for native and WASM
- Creating chat widgets (messages, prompts, avatars)
- Handling SSE streaming responses
- Keywords: molykit, moly-kit, ai chat, bot client, openai makepad, chat widget, sse streaming

## Overview

MolyKit provides:
- Cross-platform async utilities (PlatformSend, spawn(), ThreadToken)
- Ready-to-use chat widgets (Chat, Messages, PromptInput, Avatar)
- BotClient trait for AI provider integration
- OpenAI-compatible client with SSE streaming
- Protocol types for messages, bots, and tool calls
- MCP (Model Context Protocol) support

## Cross-Platform Async Patterns

### PlatformSend - Send Only on Native

```rust
/// Implies Send only on native platforms, not on WASM
/// - On native: implemented by types that implement Send
/// - On WASM: implemented by ALL types
pub trait PlatformSend: PlatformSendInner {}

/// Boxed future type for cross-platform use
pub type BoxPlatformSendFuture<'a, T> = Pin<Box<dyn PlatformSendFuture<Output = T> + 'a>>;

/// Boxed stream type for cross-platform use
pub type BoxPlatformSendStream<'a, T> = Pin<Box<dyn PlatformSendStream<Item = T> + 'a>>;
```

### Platform-Agnostic Spawning

```rust
/// Runs a future independently
/// - Uses tokio on native (requires Send)
/// - Uses wasm-bindgen-futures on WASM (no Send required)
pub fn spawn(fut: impl PlatformSendFuture<Output = ()> + 'static);

// Usage
spawn(async move {
    let result = fetch_data().await;
    Cx::post_action(DataReady(result));
    SignalToUI::set_ui_signal();
});
```

### Task Cancellation with AbortOnDropHandle

```rust
/// Handle that aborts its future when dropped
pub struct AbortOnDropHandle(AbortHandle);

// Usage - task cancelled when widget dropped
#[rust]
task_handle: Option<AbortOnDropHandle>,

fn start_task(&mut self) {
    let (future, handle) = abort_on_drop(async move {
        // async work...
    });
    self.task_handle = Some(handle);
    spawn(async move { let _ = future.await; });
}
```

### ThreadToken for Non-Send Types on WASM

```rust
/// Store non-Send value in thread-local, access via token
pub struct ThreadToken<T: 'static>;

impl<T> ThreadToken<T> {
    pub fn new(value: T) -> Self;
    pub fn peek<R>(&self, f: impl FnOnce(&T) -> R) -> R;
    pub fn peek_mut<R>(&self, f: impl FnOnce(&mut T) -> R) -> R;
}

// Usage - wrap non-Send type for use across Send boundaries
let token = ThreadToken::new(non_send_value);
spawn(async move {
    token.peek(|value| {
        // use value...
    });
});
```

## BotClient Trait

### Implementing AI Provider Integration

```rust
pub trait BotClient: Send {
    /// Send message with streamed response
    fn send(
        &mut self,
        bot_id: &BotId,
        messages: &[Message],
        tools: &[Tool],
    ) -> BoxPlatformSendStream<'static, ClientResult<MessageContent>>;

    /// Get available bots/models
    fn bots(&self) -> BoxPlatformSendFuture<'static, ClientResult<Vec<Bot>>>;

    /// Clone for passing around
    fn clone_box(&self) -> Box<dyn BotClient>;
}

// Usage
let client = OpenAIClient::new("https://api.openai.com/v1".into());
client.set_key("sk-...")?;
let context = BotContext::from(client);
```

### BotContext - Sharable Wrapper

```rust
/// Sharable wrapper with loaded bots for sync UI access
pub struct BotContext(Arc<Mutex<InnerBotContext>>);

impl BotContext {
    pub fn load(&mut self) -> BoxPlatformSendFuture<ClientResult<()>>;
    pub fn bots(&self) -> Vec<Bot>;
    pub fn get_bot(&self, id: &BotId) -> Option<Bot>;
    pub fn client(&self) -> Box<dyn BotClient>;
}

// Usage
let mut context = BotContext::from(client);
spawn(async move {
    if let Err(errors) = context.load().await.into_result() {
        // handle errors
    }
    Cx::post_action(BotsLoaded);
});
```

## Protocol Types

### Message Structure

```rust
pub struct Message {
    pub from: EntityId,         // User, System, Bot(BotId), App
    pub metadata: MessageMetadata,
    pub content: MessageContent,
}

pub struct MessageContent {
    pub text: String,           // Main content (markdown)
    pub reasoning: String,      // AI reasoning/thinking
    pub citations: Vec<String>, // Source URLs
    pub attachments: Vec<Attachment>,
    pub tool_calls: Vec<ToolCall>,
    pub tool_results: Vec<ToolResult>,
}

pub struct MessageMetadata {
    pub is_writing: bool,       // Still being streamed
    pub created_at: DateTime<Utc>,
}
```

### Bot Identification

```rust
/// Globally unique bot ID: <len>;<id>@<provider>
pub struct BotId(Arc<str>);

impl BotId {
    pub fn new(id: &str, provider: &str) -> Self;
    pub fn id(&self) -> &str;       // provider-local id
    pub fn provider(&self) -> &str; // provider domain
}

// Example: BotId::new("gpt-4", "api.openai.com")
// -> "5;gpt-4@api.openai.com"
```

## Widget Patterns

### Slot Widget - Runtime Content Replacement

```rust
live_design! {
    pub Slot = {{Slot}} {
        width: Fill, height: Fit,
        slot = <View> {}  // default content
    }
}

// Usage - replace content at runtime
let mut slot = widget.slot(id!(content));
if let Some(custom) = client.content_widget(cx, ...) {
    slot.replace(custom);
} else {
    slot.restore();  // back to default
    slot.default().as_standard_message_content().set_content(cx, &content);
}
```

### Avatar Widget - Text/Image Toggle

```rust
live_design! {
    pub Avatar = {{Avatar}} <View> {
        grapheme = <RoundedView> {
            visible: false,
            label = <Label> { text: "P" }
        }
        dependency = <RoundedView> {
            visible: false,
            image = <Image> {}
        }
    }
}

impl Widget for Avatar {
    fn draw_walk(&mut self, cx: &mut Cx2d, ...) -> DrawStep {
        if let Some(avatar) = &self.avatar {
            match avatar {
                Picture::Grapheme(g) => {
                    self.view(id!(grapheme)).set_visible(cx, true);
                    self.view(id!(dependency)).set_visible(cx, false);
                    self.label(id!(label)).set_text(cx, &g);
                }
                Picture::Dependency(d) => {
                    self.view(id!(dependency)).set_visible(cx, true);
                    self.view(id!(grapheme)).set_visible(cx, false);
                    self.image(id!(image)).load_image_dep_by_path(cx, d.as_str());
                }
            }
        }
        self.deref.draw_walk(cx, scope, walk)
    }
}
```

### PromptInput Widget

```rust
#[derive(Live, Widget)]
pub struct PromptInput {
    #[deref] deref: CommandTextInput,
    #[live] pub send_icon: LiveValue,
    #[live] pub stop_icon: LiveValue,
    #[rust] pub task: Task,           // Send or Stop
    #[rust] pub interactivity: Interactivity,
}

impl PromptInput {
    pub fn submitted(&self, actions: &Actions) -> bool;
    pub fn reset(&mut self, cx: &mut Cx);
    pub fn set_send(&mut self);
    pub fn set_stop(&mut self);
    pub fn enable(&mut self);
    pub fn disable(&mut self);
}
```

### Messages Widget - Conversation View

```rust
#[derive(Live, Widget)]
pub struct Messages {
    #[deref] deref: View,
    #[rust] pub messages: Vec<Message>,
    #[rust] pub bot_context: Option<BotContext>,
}

impl Messages {
    pub fn set_messages(&mut self, messages: Vec<Message>, scroll_to_bottom: bool);
    pub fn scroll_to_bottom(&mut self, cx: &mut Cx, triggered_by_stream: bool);
    pub fn is_at_bottom(&self) -> bool;
}
```

## UiRunner Pattern for Async-to-UI

```rust
impl Widget for PromptInput {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.deref.handle_event(cx, event, scope);
        self.ui_runner().handle(cx, event, scope, self);

        if self.button(id!(attach)).clicked(event.actions()) {
            let ui = self.ui_runner();
            Attachment::pick_multiple(move |result| match result {
                Ok(attachments) => {
                    ui.defer_with_redraw(move |me, cx, _| {
                        me.attachment_list_ref().write().attachments.extend(attachments);
                    });
                }
                Err(_) => {}
            });
        }
    }
}
```

## SSE Streaming

```rust
/// Parse SSE byte stream into message stream
pub fn parse_sse<S, B, E>(s: S) -> impl Stream<Item = Result<String, E>>
where
    S: Stream<Item = Result<B, E>>,
    B: AsRef<[u8]>,
{
    // Split on "\n\n", extract "data:" content
    // Filter comments and [DONE] messages
}

// Usage in BotClient::send
fn send(&mut self, ...) -> BoxPlatformSendStream<...> {
    let stream = stream! {
        let response = client.post(url).send().await?;
        let events = parse_sse(response.bytes_stream());

        for await event in events {
            let completion: Completion = serde_json::from_str(&event)?;
            content.text.push_str(&completion.delta.content);
            yield ClientResult::new_ok(content.clone());
        }
    };
    Box::pin(stream)
}
```

## Best Practices

1. **Use PlatformSend for cross-platform**: Same code works on native and WASM
2. **Use spawn() not tokio::spawn**: Platform-agnostic task spawning
3. **Use AbortOnDropHandle**: Cancel tasks when widget drops
4. **Use ThreadToken for non-Send on WASM**: Thread-local storage with token access
5. **Use Slot for custom content**: Allow BotClient to provide custom widgets
6. **Use read()/write() pattern**: Safe borrow access via WidgetRef
7. **Use UiRunner::defer_with_redraw**: Update widget from async context
8. **Handle ClientResult partial success**: May have value AND errors

## Reference Files

- `llms.txt` - Complete MolyKit API reference
```

## File: `skills/molykit/llms.txt`
```
# MolyKit - AI Chat UI Toolkit for Makepad

> MolyKit is a library of reusable components for building AI chat interfaces with Makepad and Robius framework.

## Overview

MolyKit provides:
- Cross-platform async utilities for native and WASM
- Ready-to-use chat widgets (Chat, Messages, PromptInput, Avatar)
- BotClient trait for integrating AI providers
- OpenAI-compatible API client with SSE streaming
- Protocol types for messages, bots, and tool calls
- MCP (Model Context Protocol) integration

---

## Core Protocol Types

### EntityId - Message Sender Identification

```rust
/// Identify entities in a chat
#[derive(Clone, PartialEq, Eq, Hash, Debug, Default)]
pub enum EntityId {
    User,           // The user operating the app
    System,         // System/developer messages for LLM context
    Bot(BotId),     // Automated assistant (model, agent)
    #[default]
    App,            // App-specific information (inline errors)
}
```

### BotId - Globally Unique Bot Identifier

```rust
/// Globally unique and stable bot identifier
/// Format: <id_len>;<id>@<provider>
#[derive(Clone, PartialEq, Eq, Hash, Debug, Default)]
pub struct BotId(Arc<str>);

impl BotId {
    /// Creates a new bot id from provider-local id and provider domain/url
    pub fn new(id: &str, provider: &str) -> Self {
        let id = format!("{};{}@{}", id.len(), id, provider);
        BotId(id.into())
    }

    pub fn id(&self) -> &str { /* provider-local id */ }
    pub fn provider(&self) -> &str { /* provider domain */ }
}
```

### Message and MessageContent

```rust
/// A message in a conversation
#[derive(Clone, PartialEq, Debug, Default)]
pub struct Message {
    pub from: EntityId,
    pub metadata: MessageMetadata,
    pub content: MessageContent,
}

/// Standard message content format
#[derive(Clone, Debug, PartialEq, Default)]
pub struct MessageContent {
    pub text: String,                    // Main body (markdown)
    pub citations: Vec<String>,          // Source URLs
    pub reasoning: String,               // Reasoning/thinking content
    pub attachments: Vec<Attachment>,    // File attachments
    pub tool_calls: Vec<ToolCall>,       // AI tool calls
    pub tool_results: Vec<ToolResult>,   // Tool execution results
    pub data: Option<String>,            // Non-standard data
    pub upgrade: Option<Upgrade>,        // Realtime communication upgrade
}

/// Metadata tracked for each message
#[derive(Clone, Debug, PartialEq)]
pub struct MessageMetadata {
    pub is_writing: bool,                       // Message still being written
    pub created_at: DateTime<Utc>,
    pub reasoning_updated_at: DateTime<Utc>,
    pub text_updated_at: DateTime<Utc>,
}
```

### Bot and BotCapabilities

```rust
#[derive(Clone, Debug)]
pub struct Bot {
    pub id: BotId,
    pub name: String,
    pub avatar: Picture,
    pub capabilities: BotCapabilities,
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub enum BotCapability {
    Realtime,        // Supports realtime audio
    Attachments,     // Supports image/file attachments
    FunctionCalling, // Supports function calling
}

#[derive(Clone, Debug, Default)]
pub struct BotCapabilities {
    capabilities: HashSet<BotCapability>,
}

impl BotCapabilities {
    pub fn new() -> Self;
    pub fn with_capability(mut self, capability: BotCapability) -> Self;
    pub fn supports_realtime(&self) -> bool;
    pub fn supports_attachments(&self) -> bool;
    pub fn supports_function_calling(&self) -> bool;
}
```

### Tool Calls and Results

```rust
/// Function/tool call made by the AI
#[derive(Clone, PartialEq, Debug, Default)]
pub struct ToolCall {
    pub id: String,
    pub name: String,
    pub arguments: serde_json::Map<String, serde_json::Value>,
    pub permission_status: ToolCallPermissionStatus,
    pub permission_options: Vec<PermissionOption>,
    pub execution_status: ToolCallExecutionStatus,
    pub output: Option<String>,
}

#[derive(Clone, PartialEq, Debug, Default)]
pub enum ToolCallPermissionStatus {
    #[default]
    Pending,
    Approved,
    Denied,
}

#[derive(Clone, PartialEq, Debug, Default)]
pub enum ToolCallExecutionStatus {
    #[default]
    NotStarted,
    InProgress,
    Completed,
    Failed,
}

/// Tool definition
#[derive(Clone, Debug, PartialEq)]
pub struct Tool {
    pub name: String,
    pub description: Option<String>,
    pub input_schema: Arc<serde_json::Map<String, serde_json::Value>>,
}
```

---

## Async Utilities

### PlatformSend - Cross-Platform Send Trait

```rust
/// Implies Send only on native platforms, not on WASM
/// - On native: implemented by all types that implement Send
/// - On WASM: implemented by all types, regardless of Send
pub trait PlatformSend: PlatformSendInner {}

cfg_if::cfg_if! {
    if #[cfg(target_arch = "wasm32")] {
        pub trait PlatformSendInner {}
        impl<T> PlatformSendInner for T {}
    } else {
        pub trait PlatformSendInner: Send {}
        impl<T> PlatformSendInner for T where T: Send {}
    }
}

/// A future that requires Send on native, but not on WASM
pub trait PlatformSendFuture: Future + PlatformSend {}

/// A stream that requires Send on native, but not on WASM
pub trait PlatformSendStream: Stream + PlatformSend {}

/// Boxed platform-send future type
pub type BoxPlatformSendFuture<'a, T> = Pin<Box<dyn PlatformSendFuture<Output = T> + 'a>>;

/// Boxed platform-send stream type
pub type BoxPlatformSendStream<'a, T> = Pin<Box<dyn PlatformSendStream<Item = T> + 'a>>;
```

### spawn() - Platform-Agnostic Task Spawning

```rust
/// Runs a future independently, in a platform-specific way
/// - Uses tokio and requires Send on native platforms
/// - Uses wasm-bindgen-futures on WASM and does not require Send
pub fn spawn(fut: impl PlatformSendFuture<Output = ()> + 'static) {
    spawn_impl(fut);
}

#[cfg(not(target_arch = "wasm32"))]
fn spawn_impl(fut: impl Future<Output = ()> + 'static + Send) {
    use std::sync::OnceLock;
    use tokio::runtime::{Builder, Handle, Runtime};

    static RUNTIME: OnceLock<Runtime> = OnceLock::new();

    if let Ok(handle) = Handle::try_current() {
        handle.spawn(fut);
    } else {
        log::warn!("No Tokio runtime found. Creating a shared runtime.");
        let rt = RUNTIME.get_or_init(|| {
            Builder::new_multi_thread()
                .enable_io()
                .enable_time()
                .thread_name("moly-kit-tokio")
                .build()
                .expect("Failed to create Tokio runtime for MolyKit")
        });
        rt.spawn(fut);
    }
}

#[cfg(target_arch = "wasm32")]
fn spawn_impl(fut: impl Future<Output = ()> + 'static) {
    wasm_bindgen_futures::spawn_local(fut);
}
```

### AbortOnDropHandle - Task Cancellation

```rust
/// A handle that aborts its associated future when dropped
/// Useful in Makepad to ensure tasks get cancelled on widget drop
pub struct AbortOnDropHandle(AbortHandle);

impl Drop for AbortOnDropHandle {
    fn drop(&mut self) {
        self.abort();
    }
}

impl AbortOnDropHandle {
    pub fn abort(&mut self) {
        self.0.abort();
    }
}

/// Constructs a future + AbortOnDropHandle pair
pub fn abort_on_drop<F, T>(future: F) -> (Abortable<F>, AbortOnDropHandle)
where
    F: PlatformSendFuture<Output = T> + 'static,
{
    let (abort_handle, abort_registration) = abortable(future);
    (abort_handle, AbortOnDropHandle(abort_registration))
}
```

### ThreadToken - Thread-Local Storage for non-Send Types

```rust
/// Holds a value inside thread-local storage
/// Token can access the value only from the same thread that created it
/// Useful on web where you need to pass non-Send values across Send boundaries
pub struct ThreadToken<T: 'static>(Arc<ThreadTokenInner<T>>);

impl<T> ThreadToken<T> {
    /// Put value in thread-local storage, return token to access it
    pub fn new(value: T) -> Self;

    /// Immutable access to the value
    pub fn peek<R>(&self, f: impl FnOnce(&T) -> R) -> R;

    /// Mutable access to the value
    pub fn peek_mut<R>(&self, f: impl FnOnce(&mut T) -> R) -> R;
}

impl<T: Clone> ThreadToken<T> {
    /// Clone the associated value and return it
    pub fn clone_inner(&self) -> T;
}
```

### DeferAsync - Awaitable UI Operations

```rust
/// Async extension to UiRunner
pub trait DeferAsync<T> {
    /// Awaitable variant of UiRunner::defer
    /// Returns None if widget couldn't execute the closure
    async fn defer_async<R>(self, f: impl AsyncDeferCallback<T, R>) -> Option<R>
    where
        R: Send + 'static,
        Self: Sized;
}

impl<T: 'static> DeferAsync<T> for UiRunner<T> {
    async fn defer_async<R: Send + 'static>(self, f: impl AsyncDeferCallback<T, R>) -> Option<R> {
        let (tx, rx) = futures::channel::oneshot::channel::<R>();
        self.defer(move |me, cx, scope| {
            let _ = tx.send(f(me, cx, scope));
        });
        rx.await.ok()
    }
}

/// With redraw variant
pub trait DeferWithRedrawAsync<T: 'static> {
    async fn defer_with_redraw_async<R>(self, f: impl AsyncDeferCallback<T, R>) -> Option<R>
    where
        R: Send + 'static;
}
```

---

## BotClient Trait

```rust
/// Standard interface to fetch bots and send messages
/// Warning: Expected to be cloned (keep cheap to clone and synced)
pub trait BotClient: Send {
    /// Send a message with streamed response
    /// Each message in stream is a snapshot of the full message being built
    fn send(
        &mut self,
        bot_id: &BotId,
        messages: &[Message],
        tools: &[Tool],
    ) -> BoxPlatformSendStream<'static, ClientResult<MessageContent>>;

    /// Get available bots
    fn bots(&self) -> BoxPlatformSendFuture<'static, ClientResult<Vec<Bot>>>;

    /// Make a boxed clone for passing around
    fn clone_box(&self) -> Box<dyn BotClient>;

    /// Optional: Override content rendering
    fn content_widget(
        &mut self,
        _cx: &mut Cx,
        _previous_widget: WidgetRef,
        _templates: &HashMap<LiveId, LivePtr>,
        _content: &MessageContent,
    ) -> Option<WidgetRef> {
        None
    }

    /// Approve a tool call by ID
    fn approve_tool_call(&self, _tool_call_id: &str, _option_id: Option<&str>) -> bool {
        false
    }

    /// Deny a tool call by ID
    fn deny_tool_call(&self, _tool_call_id: &str, _option_id: Option<&str>) -> bool {
        false
    }
}

impl Clone for Box<dyn BotClient> {
    fn clone(&self) -> Self {
        self.clone_box()
    }
}
```

### BotContext - Sharable Client Wrapper

```rust
/// Sharable wrapper around BotClient with loaded bots
/// Provides synchronous APIs for UI access
pub struct BotContext(Arc<Mutex<InnerBotContext>>);

impl BotContext {
    /// Differentiates BotContexts by pointer address
    pub fn id(&self) -> usize;

    /// Fetches bots and keeps them for sync access later
    pub fn load(&mut self) -> BoxPlatformSendFuture<ClientResult<()>>;

    /// Get cloned client
    pub fn client(&self) -> Box<dyn BotClient>;

    /// Get loaded bots
    pub fn bots(&self) -> Vec<Bot>;

    /// Get specific bot by ID
    pub fn get_bot(&self, id: &BotId) -> Option<Bot>;

    /// Get/set tool manager
    pub fn tool_manager(&self) -> Option<McpManagerClient>;
    pub fn set_tool_manager(&mut self, tool_manager: McpManagerClient);
}

impl<T: BotClient + 'static> From<T> for BotContext {
    fn from(client: T) -> Self { /* wrap in Arc<Mutex> */ }
}
```

---

## ClientError and ClientResult

```rust
/// Standard error kinds for client implementations
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum ClientErrorKind {
    Network,    // Connection could not be established or was lost
    Response,   // Remote server returned an error (HTTP error code)
    Format,     // Response parsed but content invalid
    Unknown,    // Uncontemplated error
}

/// Standard client error
#[derive(Debug, Clone)]
pub struct ClientError {
    kind: ClientErrorKind,
    message: String,
    source: Option<Arc<dyn Error + Send + Sync + 'static>>,
}

impl ClientError {
    pub fn new(kind: ClientErrorKind, message: String) -> Self;
    pub fn new_with_source<S>(kind: ClientErrorKind, message: String, source: Option<S>) -> Self
    where S: Error + Send + Sync + 'static;
}

/// Outcome that may contain both value and errors
#[derive(Debug)]
pub struct ClientResult<T> {
    errors: Vec<ClientError>,
    value: Option<T>,
}

impl<T> ClientResult<T> {
    pub fn new_ok(value: T) -> Self;
    pub fn new_err(errors: Vec<ClientError>) -> Self;
    pub fn new_ok_and_err(value: T, errors: Vec<ClientError>) -> Self;

    pub fn value(&self) -> Option<&T>;
    pub fn errors(&self) -> &[ClientError];
    pub fn has_value(&self) -> bool;
    pub fn has_errors(&self) -> bool;
    pub fn into_result(self) -> Result<T, Vec<ClientError>>;
}
```

---

## OpenAI Client

```rust
/// Client for OpenAI-compatible APIs with SSE streaming
#[derive(Debug, Clone)]
pub struct OpenAIClient(Arc<RwLock<OpenAIClientInner>>);

impl OpenAIClient {
    /// Create client with OpenAI-compatible API URL
    pub fn new(url: String) -> Self;

    /// Set custom header
    pub fn set_header(&mut self, key: &str, value: &str) -> Result<(), &'static str>;

    /// Set API key (Authorization: Bearer <key>)
    pub fn set_key(&mut self, key: &str) -> Result<(), &'static str>;
}

impl BotClient for OpenAIClient {
    fn bots(&self) -> BoxPlatformSendFuture<'static, ClientResult<Vec<Bot>>> {
        // GET /models -> list of Bot
    }

    fn send(
        &mut self,
        bot_id: &BotId,
        messages: &[Message],
        tools: &[Tool],
    ) -> BoxPlatformSendStream<'static, ClientResult<MessageContent>> {
        // POST /chat/completions with stream: true
        // Parse SSE events, yield MessageContent snapshots
    }
}
```

### SSE Parsing

```rust
/// Convert a stream of bytes into a stream of SSE messages
pub fn parse_sse<S, B, E>(s: S) -> impl Stream<Item = Result<String, E>>
where
    S: Stream<Item = Result<B, E>>,
    B: AsRef<[u8]>,
{
    stream! {
        let mut buffer: Vec<u8> = Vec::new();
        for await chunk in s {
            buffer.extend_from_slice(chunk.as_ref());
            // Split on "\n\n" terminator
            // Filter comments (lines starting with ":")
            // Extract data after "data:" prefix
            // Filter "[DONE]" messages
            for message in completed_messages {
                yield Ok(message);
            }
        }
    }
}
```

---

## MultiClient - Compose Multiple Clients

```rust
/// Client composed from multiple subclients
#[derive(Clone)]
pub struct MultiClient {
    clients_with_bots: Arc<Mutex<Vec<(Box<dyn BotClient>, Vec<Bot>)>>>,
}

impl MultiClient {
    pub fn new() -> Self;
    pub fn add_client(&mut self, client: Box<dyn BotClient>);
}

impl BotClient for MultiClient {
    fn bots(&self) -> BoxPlatformSendFuture<'static, ClientResult<Vec<Bot>>> {
        // Fetch from all clients, merge results
    }

    fn send(&mut self, bot_id: &BotId, ...) -> BoxPlatformSendStream<...> {
        // Find client that owns the bot, delegate to it
    }
}
```

---

## Widgets

### Slot Widget - Runtime Content Replacement

```rust
live_design! {
    pub Slot = {{Slot}} {
        width: Fill, height: Fit
        slot = <View> {}
    }
}

/// Widget that allows runtime content replacement
#[derive(Live, Widget, LiveHook)]
pub struct Slot {
    #[deref] deref: View,
    #[rust] current_widget: Option<WidgetRef>,
    #[rust] default_widget: Option<WidgetRef>,
}

impl Slot {
    /// Returns the current widget or the default slot content
    pub fn current(&self) -> WidgetRef;

    /// Returns the default slot content
    pub fn default(&self) -> WidgetRef;

    /// Replaces the current widget (restored on restore())
    pub fn replace(&mut self, widget: WidgetRef);

    /// Restore to default widget
    pub fn restore(&mut self);
}

impl SlotRef {
    pub fn current(&self) -> WidgetRef;
    pub fn replace(&mut self, widget: WidgetRef);
    pub fn restore(&mut self);
}
```

### Avatar Widget - Text/Image Toggle

```rust
live_design! {
    pub Avatar = {{Avatar}} <View> {
        height: Fit, width: Fit,

        grapheme = <RoundedView> {
            visible: false,
            width: 24, height: 24,
            draw_bg: { color: #37567d, border_radius: 3 }
            label = <Label> { text: "P" }
        }

        dependency = <RoundedView> {
            visible: false,
            width: 28, height: 28,
            image = <Image> { width: 28, height: 28 }
        }
    }
}

#[derive(Live, Widget, LiveHook)]
pub struct Avatar {
    #[deref] deref: View,
    #[rust] pub avatar: Option<Picture>,
}

impl Widget for Avatar {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        if let Some(avatar) = &self.avatar {
            match avatar {
                Picture::Grapheme(grapheme) => {
                    self.view(id!(grapheme)).set_visible(cx, true);
                    self.view(id!(dependency)).set_visible(cx, false);
                    self.label(id!(label)).set_text(cx, &grapheme);
                }
                Picture::Dependency(dependency) => {
                    self.view(id!(dependency)).set_visible(cx, true);
                    self.view(id!(grapheme)).set_visible(cx, false);
                    self.image(id!(image)).load_image_dep_by_path(cx, dependency.as_str());
                }
            }
        }
        self.deref.draw_walk(cx, scope, walk)
    }
}
```

### PromptInput Widget

```rust
live_design! {
    pub PromptInput = {{PromptInput}} <CommandTextInput> {
        send_icon: dep("crate://self/resources/send.svg"),
        stop_icon: dep("crate://self/resources/stop.svg"),
        // ... styling
    }
}

#[derive(Default, Copy, Clone, PartialEq)]
pub enum Task { #[default] Send, Stop }

#[derive(Default, Copy, Clone, PartialEq)]
pub enum Interactivity { #[default] Enabled, Disabled }

#[derive(Live, Widget)]
pub struct PromptInput {
    #[deref] deref: CommandTextInput,
    #[live] pub send_icon: LiveValue,
    #[live] pub stop_icon: LiveValue,
    #[rust] pub task: Task,
    #[rust] pub interactivity: Interactivity,
    #[rust] pub bot_capabilities: Option<BotCapabilities>,
}

impl PromptInput {
    pub fn reset(&mut self, cx: &mut Cx);
    pub fn submitted(&self, actions: &Actions) -> bool;
    pub fn has_send_task(&self) -> bool;
    pub fn has_stop_task(&self) -> bool;
    pub fn enable(&mut self);
    pub fn disable(&mut self);
    pub fn set_send(&mut self);
    pub fn set_stop(&mut self);
    pub fn set_bot_capabilities(&mut self, cx: &mut Cx, capabilities: Option<BotCapabilities>);
}
```

### Messages Widget - Conversation View

```rust
live_design! {
    pub Messages = {{Messages}} {
        flow: Overlay,
        list = <PortalList> {
            UserLine = <UserLine> {}
            BotLine = <BotLine> {}
            LoadingLine = <LoadingLine> {}
            AppLine = <AppLine> {}
            ErrorLine = <ErrorLine> {}
            SystemLine = <SystemLine> {}
            ToolLine = <ToolLine> {}
            EndOfChat = <View> { height: 0.1 }
        }
        jump_to_bottom = <Button> { /* ... */ }
    }
}

#[derive(Debug, PartialEq, Copy, Clone, DefaultNone)]
pub enum MessagesAction {
    Copy(usize),
    Delete(usize),
    EditSave(usize),
    EditRegenerate(usize),
    ToolApprove(usize),
    ToolDeny(usize),
    None,
}

#[derive(Live, Widget)]
pub struct Messages {
    #[deref] deref: View,
    #[rust] pub messages: Vec<Message>,
    #[rust] pub bot_context: Option<BotContext>,
    #[rust] pub templates: HashMap<LiveId, LivePtr>,
    #[rust] current_editor: Option<Editor>,
    #[rust] visible_range: Option<(usize, usize)>,
    // ...
}

impl Messages {
    pub fn is_at_bottom(&self) -> bool;
    pub fn user_scrolled(&self) -> bool;
    pub fn scroll_to_bottom(&mut self, cx: &mut Cx, triggered_by_stream: bool);
    pub fn set_message_editor_visibility(&mut self, index: usize, visible: bool);
    pub fn current_editor_text(&self) -> Option<String>;
    pub fn set_messages(&mut self, messages: Vec<Message>, scroll_to_bottom: bool);
    pub fn reset_scroll_state(&mut self);
}
```

### Chat Line Variants

```rust
live_design! {
    // Base chat line structure
    ChatLine = <View> {
        flow: Down,
        header = <View> {
            avatar = <Avatar> {}
            name = <Label> {}
        }
        message_section = <View> {
            content_section = <View> {
                content = <Slot> {
                    slot = <StandardMessageContent> {}
                }
            }
            actions = <View> { /* copy, edit, delete buttons */ }
            editor = <View> { /* edit mode */ }
            edit_actions = <View> { /* save, cancel */ }
        }
    }

    // Variants
    UserLine = <ChatLine> { /* user styling */ }
    BotLine = <ChatLine> { /* bot styling */ }
    AppLine = <ChatLine> { /* app message styling */ }
    ErrorLine = <ChatLine> { /* error styling */ }
    SystemLine = <ChatLine> { /* system styling */ }
    ToolLine = <ChatLine> { /* tool call styling with approve/deny buttons */ }
    LoadingLine = <ChatLine> { /* loading animation */ }
}
```

---

## Widget Reference Pattern

```rust
impl PromptInputRef {
    /// Immutable access (panics if empty or already borrowed)
    pub fn read(&self) -> Ref<PromptInput> {
        self.borrow().unwrap()
    }

    /// Mutable access (panics if empty or already borrowed)
    pub fn write(&mut self) -> RefMut<PromptInput> {
        self.borrow_mut().unwrap()
    }

    /// Immutable reader
    pub fn read_with<R>(&self, f: impl FnOnce(&PromptInput) -> R) -> R {
        f(&*self.read())
    }

    /// Mutable writer
    pub fn write_with<R>(&mut self, f: impl FnOnce(&mut PromptInput) -> R) -> R {
        f(&mut *self.write())
    }
}
```

---

## UiRunner Pattern for Async-to-UI

```rust
// From async task, update widget via UiRunner
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    self.deref.handle_event(cx, event, scope);
    self.ui_runner().handle(cx, event, scope, self);

    if self.button(id!(attach)).clicked(event.actions()) {
        let ui = self.ui_runner();
        Attachment::pick_multiple(move |result| match result {
            Ok(attachments) => {
                ui.defer_with_redraw(move |me, _, _| {
                    let mut list = me.attachment_list_ref();
                    list.write().attachments.extend(attachments);
                    list.write().on_tap(move |list, index| {
                        list.attachments.remove(index);
                    });
                });
            }
            Err(_) => {}
        });
    }
}
```

---

## Best Practices

1. **Use PlatformSend for cross-platform async**: Allows same code to work on native and WASM
2. **Use spawn() for platform-agnostic task spawning**: Handles tokio vs wasm-bindgen-futures
3. **Use AbortOnDropHandle for widget cleanup**: Cancel tasks when widget is dropped
4. **Use ThreadToken for non-Send types on WASM**: Store in thread-local, access via token
5. **Use Slot for runtime widget replacement**: Allows custom content from BotClient
6. **Use WidgetRef patterns (read/write)**: Safe borrow access to widget internals
7. **Use UiRunner::defer_with_redraw for async-to-UI**: Update widget state from async tasks
8. **Implement BotClient for AI providers**: Standard interface for chat integration
9. **Use MultiClient to combine providers**: Single interface for multiple AI services
10. **Handle ClientResult partial success**: May have value AND errors
```

## File: `skills/robius-app-architecture/SKILL.md`
```markdown
---
name: robius-app-architecture
description: |
  CRITICAL: Use for Robius app architecture patterns. Triggers on:
  Tokio, async, submit_async_request, 异步, 架构,
  SignalToUI, Cx::post_action, worker task,
  app structure, MatchEvent, handle_startup
---

# Robius App Architecture Skill

Best practices for structuring Makepad applications based on the Robrix and Moly codebases - production applications built with Makepad and Robius framework.

**Source codebases:**
- **Robrix**: Matrix chat client - complex sync/async with background subscriptions
- **Moly**: AI chat application - cross-platform (native + WASM) with streaming APIs

## Triggers

Use this skill when:
- Building a Makepad application with async backend integration
- Designing sync/async communication patterns in Makepad
- Structuring a Robius-style application
- Keywords: robrix, robius, makepad app structure, async makepad, tokio makepad

## Production Patterns

For production-ready async patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| [08-async-loading](./_base/08-async-loading.md) | Async data loading with loading states |
| [09-streaming-results](./_base/09-streaming-results.md) | Incremental results with SignalToUI |
| [13-tokio-integration](./_base/13-tokio-integration.md) | Full tokio runtime integration |

## Core Architecture Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                     UI Thread (Makepad)                     │
│  ┌─────────┐     ┌──────────┐     ┌──────────────────────┐ │
│  │   App   │────▶│ WidgetRef │────▶│ Widget Tree (View)  │ │
│  │ State   │     │    ui     │     │ Scope::with_data()  │ │
│  └────┬────┘     └──────────┘     └──────────────────────┘ │
│       │                                                     │
│       │ submit_async_request()                              │
│       ▼                                                     │
│  ┌─────────────────┐          ┌─────────────────────────┐  │
│  │ REQUEST_SENDER  │─────────▶│  Crossbeam SegQueue     │  │
│  │ (MPSC Channel)  │          │  (Lock-free Updates)    │  │
│  └─────────────────┘          └─────────────────────────┘  │
└───────────────────────────────────┬─────────────────────────┘
                                    │
                    SignalToUI::set_ui_signal()
                                    │
┌───────────────────────────────────┴─────────────────────────┐
│                   Tokio Runtime (Async)                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           worker_task (Request Handler)               │   │
│  │  - Receives Request from UI                           │   │
│  │  - Spawns async tasks per request                     │   │
│  │  - Posts actions back via Cx::post_action()           │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Per-Item Subscriber Tasks                     │   │
│  │  - Listens to external data stream                    │   │
│  │  - Sends Update via crossbeam channel                 │   │
│  │  - Calls SignalToUI::set_ui_signal() to wake UI       │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## App Structure

### Top-Level App Definition

```rust
use makepad_widgets::*;

live_design! {
    use link::theme::*;
    use link::widgets::*;

    App = {{App}} {
        ui: <Root>{
            main_window = <Window> {
                window: {inner_size: vec2(1280, 800), title: "MyApp"},
                body = {
                    // Main content here
                }
            }
        }
    }
}

app_main!(App);

#[derive(Live)]
pub struct App {
    #[live] ui: WidgetRef,
    #[rust] app_state: AppState,
}

impl LiveRegister for App {
    fn live_register(cx: &mut Cx) {
        // Order matters: register base widgets first
        makepad_widgets::live_design(cx);
        // Then shared/common widgets
        crate::shared::live_design(cx);
        // Then feature modules
        crate::home::live_design(cx);
    }
}

impl LiveHook for App {
    fn after_new_from_doc(&mut self, cx: &mut Cx) {
        // One-time initialization after widget tree is created
    }
}
```

### AppMain Implementation

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Forward to MatchEvent trait
        self.match_event(cx, event);

        // Pass AppState through widget tree via Scope
        let scope = &mut Scope::with_data(&mut self.app_state);
        self.ui.handle_event(cx, event, scope);
    }
}
```

## Tokio Runtime Integration

### Static Runtime Initialization

```rust
use std::sync::Mutex;
use tokio::sync::mpsc::{UnboundedReceiver, UnboundedSender};

static TOKIO_RUNTIME: Mutex<Option<tokio::runtime::Runtime>> = Mutex::new(None);
static REQUEST_SENDER: Mutex<Option<UnboundedSender<AppRequest>>> = Mutex::new(None);

pub fn start_async_runtime() -> Result<tokio::runtime::Handle> {
    let (request_sender, request_receiver) = tokio::sync::mpsc::unbounded_channel();

    let rt_handle = TOKIO_RUNTIME.lock().unwrap()
        .get_or_insert_with(|| {
            tokio::runtime::Runtime::new()
                .expect("Failed to create Tokio runtime")
        })
        .handle()
        .clone();

    // Store sender for UI thread to use
    *REQUEST_SENDER.lock().unwrap() = Some(request_sender);

    // Spawn the main worker task
    rt_handle.spawn(worker_task(request_receiver));

    Ok(rt_handle)
}
```

### Request Submission Pattern

```rust
pub enum AppRequest {
    FetchData { id: String },
    SendMessage { content: String },
    // ... other request types
}

/// Submit a request from UI thread to async runtime
pub fn submit_async_request(req: AppRequest) {
    if let Some(sender) = REQUEST_SENDER.lock().unwrap().as_ref() {
        sender.send(req)
            .expect("BUG: worker task receiver has died!");
    }
}
```

### Worker Task Pattern

```rust
async fn worker_task(mut request_receiver: UnboundedReceiver<AppRequest>) -> Result<()> {
    while let Some(request) = request_receiver.recv().await {
        match request {
            AppRequest::FetchData { id } => {
                // Spawn a new task for each request
                let _task = tokio::spawn(async move {
                    let result = fetch_data(&id).await;
                    // Post result back to UI thread
                    Cx::post_action(DataFetchedAction { id, result });
                });
            }
            AppRequest::SendMessage { content } => {
                let _task = tokio::spawn(async move {
                    match send_message(&content).await {
                        Ok(()) => Cx::post_action(MessageSentAction::Success),
                        Err(e) => Cx::post_action(MessageSentAction::Failed(e)),
                    }
                });
            }
        }
    }
    Ok(())
}
```

## Lock-Free Update Queue Pattern

For high-frequency updates from background tasks:

```rust
use crossbeam_queue::SegQueue;
use makepad_widgets::SignalToUI;

pub enum DataUpdate {
    NewItem { item: Item },
    ItemChanged { id: String, changes: Changes },
    Status { message: String },
}

static PENDING_UPDATES: SegQueue<DataUpdate> = SegQueue::new();

/// Called from background async tasks
pub fn enqueue_update(update: DataUpdate) {
    PENDING_UPDATES.push(update);
    SignalToUI::set_ui_signal();  // Wake UI thread
}

// In widget's handle_event:
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Poll for updates on Signal events
        if let Event::Signal = event {
            while let Some(update) = PENDING_UPDATES.pop() {
                match update {
                    DataUpdate::NewItem { item } => {
                        self.items.push(item);
                        self.redraw(cx);
                    }
                    // ... handle other updates
                }
            }
        }
    }
}
```

## Startup Sequence

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // 1. Initialize logging
        let _ = tracing_subscriber::fmt::try_init();

        // 2. Initialize app data directory
        let _app_data_dir = crate::app_data_dir();

        // 3. Load persisted state
        if let Err(e) = persistence::load_window_state(
            self.ui.window(ids!(main_window)), cx
        ) {
            error!("Failed to load window state: {}", e);
        }

        // 4. Update UI based on loaded state
        self.update_ui_visibility(cx);

        // 5. Start async runtime
        let _rt_handle = crate::start_async_runtime().unwrap();
    }
}
```

## Shutdown Sequence

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        if let Event::Shutdown = event {
            // Save window geometry
            let window_ref = self.ui.window(ids!(main_window));
            if let Err(e) = persistence::save_window_state(window_ref, cx) {
                error!("Failed to save window state: {e}");
            }

            // Save app state
            if let Some(user_id) = current_user_id() {
                if let Err(e) = persistence::save_app_state(
                    self.app_state.clone(), user_id
                ) {
                    error!("Failed to save app state: {e}");
                }
            }
        }
        // ... rest of event handling
    }
}
```

## Best Practices

1. **Separation of Concerns**: Keep UI logic on the main thread, async operations in Tokio runtime
2. **Request/Response Pattern**: Use typed enums for requests and actions
3. **Lock-Free Updates**: Use `crossbeam::SegQueue` for high-frequency background updates
4. **SignalToUI**: Always call `SignalToUI::set_ui_signal()` after enqueueing updates
5. **Cx::post_action()**: Use for async task results that need action handling
6. **Scope::with_data()**: Pass shared state through widget tree
7. **Module Registration Order**: Register base widgets before dependent modules in `live_register()`

## Reference Files

- `references/tokio-integration.md` - Detailed Tokio runtime patterns (Robrix)
- `references/channel-patterns.md` - Channel communication patterns (Robrix)
- `references/moly-async-patterns.md` - Cross-platform async patterns (Moly)
  - `PlatformSend` trait for native/WASM compatibility
  - `UiRunner` for async defer operations
  - `AbortOnDropHandle` for task cancellation
  - `ThreadToken` for non-Send types on WASM
  - `spawn()` platform-agnostic function
```

## File: `skills/robius-app-architecture/_base/08-async-loading.md`
```markdown
---
name: makepad-async-loading
author: robius
source: robrix
date: 2024-01-01
tags: [async, loading, spinner, data-fetch]
level: intermediate
---

# Pattern 8: Async Data Loading

Show loading state while fetching data asynchronously.

## Problem

You need to fetch data from an API or database without blocking the UI, showing a loading spinner while waiting.

## Solution

Show loading UI, spawn async task, update UI when data arrives via `Cx::post_action`.

## Implementation

```rust
#[derive(Debug)]
pub enum DataAction {
    Loading,
    Loaded(Vec<Item>),
    Error(String),
}

#[derive(Live)]
pub struct App {
    #[live] ui: WidgetRef,
    #[rust] store: Option<Store>,
    #[rust] loading: bool,
}

impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Show loading state
        self.ui.view(ids!(main_content)).set_visible(cx, false);
        self.ui.view(ids!(loading_spinner)).set_visible(cx, true);
        self.loading = true;

        // Spawn async task
        spawn(async move {
            match fetch_data().await {
                Ok(data) => Cx::post_action(DataAction::Loaded(data)),
                Err(e) => Cx::post_action(DataAction::Error(e.to_string())),
            }
        });
    }

    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        for action in actions {
            if let Some(data_action) = action.downcast_ref::<DataAction>() {
                match data_action {
                    DataAction::Loaded(data) => {
                        self.store = Some(Store::new(data.clone()));
                        self.loading = false;

                        self.ui.view(ids!(main_content)).set_visible(cx, true);
                        self.ui.view(ids!(loading_spinner)).set_visible(cx, false);
                        self.ui.redraw(cx);
                    }
                    DataAction::Error(err) => {
                        self.loading = false;
                        self.ui.view(ids!(loading_spinner)).set_visible(cx, false);
                        self.ui.view(ids!(error_view)).set_visible(cx, true);
                        self.ui.label(ids!(error_message)).set_text(cx, err);
                        self.ui.redraw(cx);
                    }
                    _ => {}
                }
            }
        }
    }
}
```

## live_design!

```rust
live_design! {
    App = {{App}} {
        ui: <Root> {
            <Window> {
                body = <View> {
                    flow: Overlay

                    main_content = <View> {
                        visible: false
                        // Your main content...
                    }

                    loading_spinner = <View> {
                        align: { x: 0.5, y: 0.5 }
                        <Spinner> { width: 48, height: 48 }
                        <Label> { text: "Loading..." }
                    }

                    error_view = <View> {
                        visible: false
                        align: { x: 0.5, y: 0.5 }
                        flow: Down

                        <Label> { text: "Error" }
                        error_message = <Label> { text: "" }
                        <Button> { text: "Retry" }
                    }
                }
            }
        }
    }
}
```

## When to Use

- Initial app data loading
- API requests
- Database queries
- File loading
```

## File: `skills/robius-app-architecture/_base/09-streaming-results.md`
```markdown
---
name: makepad-streaming-results
author: robius
source: moly
date: 2024-01-01
tags: [streaming, search, incremental, background]
level: advanced
---

# Pattern 9: Streaming Results

Process and display results as they arrive from a background thread.

## Problem

You have a long-running operation (like search) that produces results incrementally. You want to show results as they're found, not wait for completion.

## Solution

Use `mpsc::channel` to stream results from background thread, with `SignalToUI` to wake the UI.

## Implementation

```rust
use std::sync::mpsc;
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;
use makepad_widgets::SignalToUI;

pub fn spawn_search(
    query: String,
    items: Vec<Item>,
    cancel: Arc<AtomicBool>,
) -> mpsc::Receiver<Item> {
    let (tx, rx) = mpsc::channel();

    std::thread::spawn(move || {
        for (i, item) in items.iter().enumerate() {
            // Check for cancellation
            if cancel.load(Ordering::Relaxed) {
                return;
            }

            if item.matches(&query) {
                let _ = tx.send(item.clone());

                // Wake UI periodically (not every item for performance)
                if i % 10 == 0 {
                    SignalToUI::set_ui_signal();
                }
            }
        }
        // Final wake to ensure UI gets last items
        SignalToUI::set_ui_signal();
    });

    rx
}

#[derive(Live, Widget)]
pub struct SearchWidget {
    #[deref] view: View,
    #[rust] search_receiver: Option<mpsc::Receiver<Item>>,
    #[rust] cancel_token: Option<Arc<AtomicBool>>,
    #[rust] results: Vec<Item>,
}

impl MatchEvent for SearchWidget {
    fn handle_signal(&mut self, cx: &mut Cx) {
        // Drain all available results
        if let Some(rx) = &self.search_receiver {
            while let Ok(item) = rx.try_recv() {
                self.results.push(item);
            }
            if !self.results.is_empty() {
                self.redraw(cx);
            }
        }
    }
}

impl SearchWidget {
    fn start_search(&mut self, cx: &mut Cx, query: String) {
        // Cancel previous search
        if let Some(cancel) = &self.cancel_token {
            cancel.store(true, Ordering::Relaxed);
        }

        // Clear results
        self.results.clear();

        // Start new search
        let cancel = Arc::new(AtomicBool::new(false));
        let rx = spawn_search(query, self.all_items.clone(), cancel.clone());

        self.cancel_token = Some(cancel);
        self.search_receiver = Some(rx);
        self.redraw(cx);
    }
}
```

## Usage

```rust
// Start search when text changes
if let Some(query) = self.ui.text_input(ids!(search_input)).changed(&actions) {
    self.start_search(cx, query);
}
```

## When to Use

- Search with live results
- File scanning
- Log streaming
- Any incremental processing

## Performance Tips

- Don't signal on every item (batch with `i % 10`)
- Use `try_recv()` to drain all available items
- Provide cancellation for user experience
```

## File: `skills/robius-app-architecture/_base/13-tokio-integration.md`
```markdown
---
name: makepad-tokio-integration
author: robius
source: robrix
date: 2024-01-01
tags: [async, tokio, runtime, channel, background]
level: advanced
---

# Pattern 13: Tokio Async Integration

Full tokio runtime integration for complex async operations.

## Problem

Your app needs real async capabilities: multiple concurrent requests, WebSockets, or integration with async SDKs like Matrix.

## Solution

Create a global tokio runtime with request channels and `Cx::post_action` for responses.

## Implementation

```rust
use std::sync::Mutex;
use tokio::runtime::{Runtime, Handle};
use tokio::sync::mpsc::{unbounded_channel, UnboundedSender};

// Global runtime
static TOKIO_RUNTIME: Mutex<Option<Runtime>> = Mutex::new(None);
static REQUEST_SENDER: Mutex<Option<UnboundedSender<AppRequest>>> = Mutex::new(None);

// Request types
pub enum AppRequest {
    FetchUsers,
    SendMessage { room_id: String, content: String },
    Logout,
}

// Response types
#[derive(Debug)]
pub enum AppResponse {
    UsersFetched(Vec<User>),
    MessageSent(Result<(), String>),
    LoggedOut,
}

pub fn start_async_runtime() {
    let rt = TOKIO_RUNTIME.lock().unwrap()
        .get_or_insert_with(|| {
            Runtime::new().expect("Failed to create Tokio runtime")
        })
        .handle()
        .clone();

    rt.spawn(async {
        let (sender, mut receiver) = unbounded_channel::<AppRequest>();
        *REQUEST_SENDER.lock().unwrap() = Some(sender);

        while let Some(request) = receiver.recv().await {
            match request {
                AppRequest::FetchUsers => {
                    let result = fetch_users_impl().await;
                    Cx::post_action(AppResponse::UsersFetched(result));
                }
                AppRequest::SendMessage { room_id, content } => {
                    let result = send_message_impl(&room_id, &content).await;
                    Cx::post_action(AppResponse::MessageSent(result));
                }
                AppRequest::Logout => {
                    logout_impl().await;
                    Cx::post_action(AppResponse::LoggedOut);
                }
            }
        }
    });
}

// Helper to submit requests (non-blocking)
pub fn submit_request(request: AppRequest) {
    if let Some(sender) = REQUEST_SENDER.lock().unwrap().as_ref() {
        let _ = sender.send(request);
    }
}
```

## App Integration

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        start_async_runtime();
        submit_request(AppRequest::FetchUsers);
        self.show_loading(cx);
    }

    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        // Handle button clicks
        if self.ui.button(ids!(refresh_btn)).clicked(&actions) {
            submit_request(AppRequest::FetchUsers);
        }

        if self.ui.button(ids!(send_btn)).clicked(&actions) {
            let content = self.ui.text_input(ids!(message_input)).text();
            submit_request(AppRequest::SendMessage {
                room_id: self.current_room.clone(),
                content,
            });
        }

        // Handle async responses
        for action in actions {
            if let Some(response) = action.downcast_ref::<AppResponse>() {
                match response {
                    AppResponse::UsersFetched(users) => {
                        self.users = users.clone();
                        self.hide_loading(cx);
                        self.update_user_list(cx);
                    }
                    AppResponse::MessageSent(Ok(())) => {
                        self.ui.text_input(ids!(message_input)).set_text(cx, "");
                    }
                    AppResponse::MessageSent(Err(e)) => {
                        show_error(cx, e);
                    }
                    AppResponse::LoggedOut => {
                        self.navigate_to_login(cx);
                    }
                }
            }
        }
    }
}
```

## Cargo.toml

```toml
[dependencies]
tokio = { version = "1", features = ["rt-multi-thread", "macros", "sync"] }
```

## When to Use

- Multiple concurrent API requests
- WebSocket connections
- SDK integration (Matrix, etc.)
- Long-running background services

## vs std::thread

| Use Case | Use |
|----------|-----|
| One-off CPU work | `std::thread::spawn` |
| Single blocking HTTP | `std::thread::spawn` |
| Multiple concurrent I/O | Tokio |
| WebSockets/streaming | Tokio |
| Async SDK integration | Tokio |
```

## File: `skills/robius-app-architecture/references/channel-patterns.md`
```markdown
# Channel Communication Patterns

Patterns for communication between UI thread and async runtime.

## Request Channel (UI → Async)

Using `tokio::sync::mpsc::unbounded_channel`:

```rust
use tokio::sync::mpsc::{UnboundedSender, UnboundedReceiver};

static REQUEST_SENDER: Mutex<Option<UnboundedSender<AppRequest>>> = Mutex::new(None);

pub fn submit_async_request(req: AppRequest) {
    if let Some(sender) = REQUEST_SENDER.lock().unwrap().as_ref() {
        sender.send(req).expect("Worker task died");
    }
}
```

## Update Queue (Async → UI)

Using `crossbeam_queue::SegQueue` for lock-free operations:

```rust
use crossbeam_queue::SegQueue;

static PENDING_UPDATES: SegQueue<Update> = SegQueue::new();

// Async side: enqueue update
pub fn enqueue_update(update: Update) {
    PENDING_UPDATES.push(update);
    SignalToUI::set_ui_signal();
}

// UI side: drain updates
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    if let Event::Signal = event {
        while let Some(update) = PENDING_UPDATES.pop() {
            self.apply_update(cx, update);
        }
    }
}
```

## Per-Item Channels

Using `crossbeam_channel` for per-item communication:

```rust
use crossbeam_channel::{Sender, Receiver, unbounded};

struct ItemState {
    update_sender: Sender<ItemUpdate>,
    update_receiver: Receiver<ItemUpdate>,
}

impl ItemState {
    fn new() -> Self {
        let (sender, receiver) = unbounded();
        Self {
            update_sender: sender,
            update_receiver: receiver,
        }
    }

    fn poll_updates(&mut self, cx: &mut Cx) {
        while let Ok(update) = self.update_receiver.try_recv() {
            self.apply_update(cx, update);
        }
    }
}
```

## Action Posting (Async → UI Actions)

For result actions that need central handling:

```rust
// In async task
Cx::post_action(ResultAction::Success { data });
SignalToUI::set_ui_signal();

// In App::handle_actions
fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
    for action in actions {
        if let Some(result) = action.downcast_ref::<ResultAction>() {
            match result {
                ResultAction::Success { data } => { /* handle */ }
                ResultAction::Failed { error } => { /* handle */ }
            }
        }
    }
}
```

## Thread-Local State

For UI-thread-only state:

```rust
use std::{cell::RefCell, rc::Rc};

thread_local! {
    static UI_ONLY_STATE: Rc<RefCell<HashMap<Id, Data>>> =
        Rc::new(RefCell::new(HashMap::new()));
}

pub fn get_ui_state(_cx: &mut Cx) -> Rc<RefCell<HashMap<Id, Data>>> {
    // _cx parameter ensures this is called from UI thread
    UI_ONLY_STATE.with(Rc::clone)
}

pub fn clear_ui_state(_cx: &mut Cx) {
    UI_ONLY_STATE.with(|state| state.borrow_mut().clear());
}
```
```

## File: `skills/robius-app-architecture/references/moly-async-patterns.md`
```markdown
# Moly Async Patterns

Additional async patterns from Moly codebase - an AI chat application with cross-platform support (native + WASM).

## Platform-Agnostic Spawn

Moly provides a unified `spawn()` function that works on both native (Tokio) and WASM:

```rust
use std::pin::Pin;
use futures::Future;

cfg_if::cfg_if! {
    if #[cfg(target_arch = "wasm32")] {
        pub trait PlatformSendInner {}
        impl<T> PlatformSendInner for T {}
    } else {
        pub trait PlatformSendInner: Send {}
        impl<T> PlatformSendInner for T where T: Send {}
    }
}

/// Implies [`Send`] only on native platforms, but not on WASM.
pub trait PlatformSend: PlatformSendInner {}
impl<T> PlatformSend for T where T: PlatformSendInner {}

/// A future that requires [`Send`] on native, but not on WASM.
pub trait PlatformSendFuture: Future + PlatformSend {}
impl<F, O> PlatformSendFuture for F where F: Future<Output = O> + PlatformSend {}

/// Platform-agnostic spawn
pub fn spawn(fut: impl PlatformSendFuture<Output = ()> + 'static) {
    #[cfg(not(target_arch = "wasm32"))]
    spawn_native(fut);

    #[cfg(target_arch = "wasm32")]
    wasm_bindgen_futures::spawn_local(fut);
}

#[cfg(not(target_arch = "wasm32"))]
fn spawn_native(fut: impl Future<Output = ()> + 'static + Send) {
    use std::sync::OnceLock;
    use tokio::runtime::{Builder, Handle, Runtime};

    static RUNTIME: OnceLock<Runtime> = OnceLock::new();

    if let Ok(handle) = Handle::try_current() {
        handle.spawn(fut);
    } else {
        // Create shared runtime if none exists
        let rt = RUNTIME.get_or_init(|| {
            Builder::new_multi_thread()
                .enable_io()
                .enable_time()
                .thread_name("app-tokio")
                .build()
                .expect("Failed to create Tokio runtime")
        });
        rt.spawn(fut);
    }
}
```

## UiRunner Pattern

Moly extends Makepad's `UiRunner` for async defer operations:

```rust
use makepad_widgets::{Cx, DeferWithRedraw, Scope, UiRunner, Widget};
use futures::channel::oneshot;

pub trait AsyncDeferCallback<T, R>:
    FnOnce(&mut T, &mut Cx, &mut Scope) -> R + Send + 'static
where
    R: Send + 'static,
{
}

impl<T, R: Send + 'static, F: FnOnce(&mut T, &mut Cx, &mut Scope) -> R + Send + 'static>
    AsyncDeferCallback<T, R> for F
{
}

/// Async extension to UiRunner
pub trait DeferAsync<T> {
    /// Awaitable variant of UiRunner::defer
    async fn defer_async<R>(self, f: impl AsyncDeferCallback<T, R>) -> Option<R>
    where
        R: Send + 'static,
        Self: Sized;
}

impl<T: 'static> DeferAsync<T> for UiRunner<T> {
    async fn defer_async<R: Send + 'static>(
        self,
        f: impl AsyncDeferCallback<T, R>
    ) -> Option<R> {
        let (tx, rx) = oneshot::channel::<R>();
        self.defer(move |me, cx, scope| {
            let _ = tx.send(f(me, cx, scope));
        });
        rx.await.ok()
    }
}

/// Usage example - async Store initialization:
pub fn load_store_into_app() {
    spawn(async move {
        let store = Store::load().await;

        // Use UiRunner to update App on UI thread
        app_runner().defer(move |app, cx, _| {
            app.store = Some(store);
            app.ui.view(id!(body)).set_visible(cx, true);
            cx.redraw_all();
        });
    });
}
```

## AbortOnDropHandle

Task cancellation when widget is dropped:

```rust
use futures::future::{AbortHandle, Abortable, abortable};

/// Handle that aborts its associated future when dropped.
pub struct AbortOnDropHandle(AbortHandle);

impl Drop for AbortOnDropHandle {
    fn drop(&mut self) {
        self.0.abort();
    }
}

impl AbortOnDropHandle {
    pub fn abort(&mut self) {
        self.0.abort();
    }
}

/// Constructs a future + AbortOnDropHandle pair.
pub fn abort_on_drop<F, T>(future: F) -> (Abortable<F>, AbortOnDropHandle)
where
    F: PlatformSendFuture<Output = T> + 'static,
{
    let (abort_handle, abort_registration) = abortable(future);
    (abort_handle, AbortOnDropHandle(abort_registration))
}

// Usage in widget
#[derive(Live, Widget)]
pub struct ChatWidget {
    #[deref] view: View,
    #[rust] task_handle: Option<AbortOnDropHandle>,
}

impl ChatWidget {
    fn start_streaming(&mut self) {
        let (future, handle) = abort_on_drop(async {
            // Streaming task...
        });
        self.task_handle = Some(handle);
        spawn(async { let _ = future.await; });
    }
}
// Task automatically cancelled when widget is dropped
```

## ThreadToken for Non-Send Types

For WASM where you need to pass non-Send values across async boundaries:

```rust
use std::cell::RefCell;
use std::collections::HashMap;
use std::sync::Arc;
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_KEY: AtomicU64 = AtomicU64::new(0);

thread_local! {
    static STORAGE: RefCell<HashMap<u64, Option<Box<dyn std::any::Any>>>> =
        RefCell::new(HashMap::new());
}

/// Holds a value in thread-local storage, accessible via token.
/// Token is Send even if the value isn't (useful for WASM).
pub struct ThreadToken<T: 'static> {
    key: u64,
    _phantom: std::marker::PhantomData<fn() -> T>,
}

// ThreadToken is Send because it only stores a key
unsafe impl<T> Send for ThreadToken<T> {}

impl<T> ThreadToken<T> {
    pub fn new(value: T) -> Self {
        let key = NEXT_KEY.fetch_add(1, Ordering::Relaxed);
        STORAGE.with_borrow_mut(|storage| {
            storage.insert(key, Some(Box::new(value)));
        });
        Self { key, _phantom: std::marker::PhantomData }
    }

    pub fn peek<R>(&self, f: impl FnOnce(&T) -> R) -> R {
        STORAGE.with_borrow_mut(|storage| {
            let value = storage.get(&self.key)
                .expect("Token used from different thread")
                .as_ref()
                .expect("Value already taken")
                .downcast_ref::<T>()
                .unwrap();
            f(value)
        })
    }

    pub fn peek_mut<R>(&self, f: impl FnOnce(&mut T) -> R) -> R {
        STORAGE.with_borrow_mut(|storage| {
            let value = storage.get_mut(&self.key)
                .expect("Token used from different thread")
                .as_mut()
                .expect("Value already taken")
                .downcast_mut::<T>()
                .unwrap();
            f(value)
        })
    }
}

// Usage: Pass non-Send FileHandle across async boundary on WASM
let file_token = ThreadToken::new(file_handle);
spawn(async move {
    file_token.peek(|handle| {
        // Use handle...
    });
});
```

## App Runner Global Access

Create a global accessor for the App's UiRunner:

```rust
pub fn app_runner() -> UiRunner<App> {
    // `0` is reserved for whatever implements `AppMain`
    UiRunner::new(0)
}

// Usage from any async context:
spawn(async move {
    let result = fetch_data().await;

    app_runner().defer(move |app, cx, _| {
        app.data = result;
        cx.redraw_all();
    });
});
```
```

## File: `skills/robius-app-architecture/references/tokio-integration.md`
```markdown
# Tokio Integration Reference

Detailed patterns for integrating Tokio async runtime with Makepad UI.

## Runtime Initialization

```rust
use std::sync::Mutex;
use tokio::runtime::Runtime;

// Global static for the Tokio runtime
static TOKIO_RUNTIME: Mutex<Option<Runtime>> = Mutex::new(None);

/// Get or create the Tokio runtime handle
pub fn get_runtime_handle() -> tokio::runtime::Handle {
    TOKIO_RUNTIME.lock().unwrap()
        .get_or_insert_with(|| {
            Runtime::new().expect("Failed to create Tokio runtime")
        })
        .handle()
        .clone()
}
```

## Per-Item Background Task Management

For items that need dedicated background listeners (like room timelines):

```rust
use tokio::task::JoinHandle;
use matrix_sdk::event_handler::EventHandlerDropGuard;

struct ItemDetails {
    item_id: OwnedItemId,
    data: Arc<ItemData>,
    update_sender: crossbeam_channel::Sender<ItemUpdate>,
    // Task handle for cleanup
    subscriber_task: JoinHandle<()>,
    // Event handlers dropped on item close
    event_handlers: Option<EventHandlerDropGuard>,
}

impl Drop for ItemDetails {
    fn drop(&mut self) {
        // Abort background task when item is closed
        self.subscriber_task.abort();
        // Drop event handlers
        drop(self.event_handlers.take());
    }
}
```

## Subscriber Task Pattern

```rust
async fn spawn_item_subscriber(
    item_id: OwnedItemId,
    data_stream: impl Stream<Item = DataUpdate>,
    sender: crossbeam_channel::Sender<ItemUpdate>,
) -> JoinHandle<()> {
    tokio::spawn(async move {
        pin_mut!(data_stream);

        while let Some(update) = data_stream.next().await {
            // Process update
            let processed = process_update(update);

            // Send to UI
            if sender.send(processed).is_err() {
                // Receiver dropped, exit
                break;
            }

            // Wake UI thread
            SignalToUI::set_ui_signal();
        }
    })
}
```

## Blocking with Timeout

For shutdown scenarios where you need to wait for async operations:

```rust
pub fn block_on_async_with_timeout<F, T>(
    timeout: Option<Duration>,
    future: F,
) -> Result<T, Elapsed>
where
    F: Future<Output = T>,
{
    let rt_handle = get_runtime_handle();

    rt_handle.block_on(async {
        match timeout {
            Some(duration) => tokio::time::timeout(duration, future).await,
            None => Ok(future.await),
        }
    })
}

// Usage in shutdown:
let res = block_on_async_with_timeout(
    Some(Duration::from_secs(3)),
    async move {
        // Save state...
    },
);
```

## Client Access Pattern

```rust
static CLIENT: Mutex<Option<Client>> = Mutex::new(None);

pub fn get_client() -> Option<Client> {
    CLIENT.lock().unwrap().clone()
}

pub fn set_client(client: Client) {
    *CLIENT.lock().unwrap() = Some(client);
}
```
```

## File: `skills/robius-event-action/SKILL.md`
```markdown
---
name: robius-event-action
description: |
  CRITICAL: Use for Robius event and action patterns. Triggers on:
  custom action, MatchEvent, post_action, cx.widget_action,
  handle_actions, DefaultNone, widget action, event handling,
  事件处理, 自定义动作
---

# Robius Event and Action Patterns Skill

Best practices for event handling and action patterns in Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix chat client - MessageAction, RoomsListAction, AppStateAction
- **Moly**: AI chat application - StoreAction, ChatAction, NavigationAction, Timer patterns

## Triggers

Use this skill when:
- Implementing custom actions in Makepad
- Handling events in widgets
- Centralizing action handling in App
- Widget-to-widget communication
- Keywords: makepad action, makepad event, widget action, handle_actions, cx.widget_action

## Custom Action Pattern

### Defining Domain-Specific Actions

```rust
use makepad_widgets::*;

/// Actions emitted by the Message widget
#[derive(Clone, DefaultNone, Debug)]
pub enum MessageAction {
    /// User wants to react to a message
    React { details: MessageDetails, reaction: String },
    /// User wants to reply to a message
    Reply(MessageDetails),
    /// User wants to edit a message
    Edit(MessageDetails),
    /// User wants to delete a message
    Delete(MessageDetails),
    /// User requested to open context menu
    OpenContextMenu { details: MessageDetails, abs_pos: DVec2 },
    /// Required default variant
    None,
}

/// Data associated with a message action
#[derive(Clone, Debug)]
pub struct MessageDetails {
    pub room_id: OwnedRoomId,
    pub event_id: OwnedEventId,
    pub content: String,
    pub sender_id: OwnedUserId,
}
```

### Emitting Actions from Widgets

```rust
impl Widget for Message {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        let area = self.view.area();
        match event.hits(cx, area) {
            Hit::FingerDown(_fe) => {
                cx.set_key_focus(area);
            }
            Hit::FingerUp(fe) => {
                if fe.is_over && fe.is_primary_hit() && fe.was_tap() {
                    // Emit widget action
                    cx.widget_action(
                        self.widget_uid(),
                        &scope.path,
                        MessageAction::Reply(self.get_details()),
                    );
                }
            }
            Hit::FingerLongPress(lpe) => {
                cx.widget_action(
                    self.widget_uid(),
                    &scope.path,
                    MessageAction::OpenContextMenu {
                        details: self.get_details(),
                        abs_pos: lpe.abs,
                    },
                );
            }
            _ => {}
        }
    }
}
```

## Centralized Action Handling in App

### Using MatchEvent Trait

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Called once on app startup
        self.initialize(cx);
    }

    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        for action in actions {
            // Pattern 1: Direct downcast for non-widget actions
            if let Some(action) = action.downcast_ref::<LoginAction>() {
                match action {
                    LoginAction::LoginSuccess => {
                        self.app_state.logged_in = true;
                        self.update_ui_visibility(cx);
                    }
                    LoginAction::LoginFailure(error) => {
                        self.show_error(cx, error);
                    }
                }
                continue;  // Action handled
            }

            // Pattern 2: Widget action cast
            if let MessageAction::OpenContextMenu { details, abs_pos } =
                action.as_widget_action().cast()
            {
                self.show_context_menu(cx, details, abs_pos);
                continue;
            }

            // Pattern 3: Match on downcast_ref for enum variants
            match action.downcast_ref() {
                Some(AppStateAction::RoomFocused(room)) => {
                    self.app_state.selected_room = Some(room.clone());
                    continue;
                }
                Some(AppStateAction::NavigateToRoom { destination }) => {
                    self.navigate_to_room(cx, destination);
                    continue;
                }
                _ => {}
            }

            // Pattern 4: Modal actions
            match action.downcast_ref() {
                Some(ModalAction::Open { kind }) => {
                    self.ui.modal(ids!(my_modal)).open(cx);
                    continue;
                }
                Some(ModalAction::Close { was_internal }) => {
                    if *was_internal {
                        self.ui.modal(ids!(my_modal)).close(cx);
                    }
                    continue;
                }
                _ => {}
            }
        }
    }
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Forward to MatchEvent
        self.match_event(cx, event);

        // Pass events to widget tree
        let scope = &mut Scope::with_data(&mut self.app_state);
        self.ui.handle_event(cx, event, scope);
    }
}
```

## Action Types

### Widget Actions (UI Thread)

Emitted by widgets, handled in the same frame:

```rust
// Emitting
cx.widget_action(
    self.widget_uid(),
    &scope.path,
    MyAction::Something,
);

// Handling (two patterns)
// Pattern A: Direct cast for widget actions
if let MyAction::Something = action.as_widget_action().cast() {
    // handle...
}

// Pattern B: With widget UID matching
if let Some(uid) = action.as_widget_action().widget_uid() {
    if uid == my_expected_uid {
        if let MyAction::Something = action.as_widget_action().cast() {
            // handle...
        }
    }
}
```

### Posted Actions (From Async)

Posted from async tasks, received in next event cycle:

```rust
// In async task
Cx::post_action(DataFetchedAction { data });
SignalToUI::set_ui_signal();  // Wake UI thread

// Handling in App (NOT widget actions)
if let Some(action) = action.downcast_ref::<DataFetchedAction>() {
    self.process_data(&action.data);
}
```

### Global Actions

For app-wide state changes:

```rust
// Using cx.action() for global actions
cx.action(NavigationAction::GoBack);

// Handling
if let Some(NavigationAction::GoBack) = action.downcast_ref() {
    self.navigate_back(cx);
}
```

## Event Handling Patterns

### Hit Testing

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        let area = self.view.area();
        match event.hits(cx, area) {
            Hit::FingerDown(fe) => {
                cx.set_key_focus(area);
                // Start drag, capture, etc.
            }
            Hit::FingerUp(fe) => {
                if fe.is_over && fe.is_primary_hit() {
                    if fe.was_tap() {
                        // Single tap
                    }
                    if fe.was_long_press() {
                        // Long press
                    }
                }
            }
            Hit::FingerMove(fe) => {
                // Drag handling
            }
            Hit::FingerHoverIn(_) => {
                self.animator_play(cx, id!(hover.on));
            }
            Hit::FingerHoverOut(_) => {
                self.animator_play(cx, id!(hover.off));
            }
            Hit::FingerScroll(se) => {
                // Scroll handling
            }
            _ => {}
        }
    }
}
```

### Keyboard Events

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    if let Event::KeyDown(ke) = event {
        match ke.key_code {
            KeyCode::Return if !ke.modifiers.shift => {
                self.submit(cx);
            }
            KeyCode::Escape => {
                self.cancel(cx);
            }
            KeyCode::KeyC if ke.modifiers.control || ke.modifiers.logo => {
                self.copy_to_clipboard(cx);
            }
            _ => {}
        }
    }
}
```

### Signal Events

For handling async updates:

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    if let Event::Signal = event {
        // Poll update queues
        while let Some(update) = PENDING_UPDATES.pop() {
            self.apply_update(cx, update);
        }
    }
}
```

## Action Chaining Pattern

Widget emits action → Parent catches and re-emits with more context:

```rust
// In child widget
cx.widget_action(
    self.widget_uid(),
    &scope.path,
    ItemAction::Selected(item_id),
);

// In parent widget's handle_event
if let ItemAction::Selected(item_id) = action.as_widget_action().cast() {
    // Add context and forward to App
    cx.widget_action(
        self.widget_uid(),
        &scope.path,
        ListAction::ItemSelected {
            list_id: self.list_id.clone(),
            item_id,
        },
    );
}
```

## Best Practices

1. **Use `DefaultNone` derive**: All action enums must have a `None` variant
2. **Use `continue` after handling**: Prevents unnecessary processing
3. **Downcast pattern for async actions**: Posted actions are not widget actions
4. **Widget action cast for UI actions**: Use `as_widget_action().cast()`
5. **Always call `SignalToUI::set_ui_signal()`**: After posting actions from async
6. **Centralize in App::handle_actions**: Keep action handling in one place
7. **Use descriptive action names**: `MessageAction::Reply` not `MessageAction::Action1`

## Reference Files

- `references/action-patterns.md` - Additional action patterns (Robrix)
- `references/event-handling.md` - Event handling reference (Robrix)
- `references/moly-action-patterns.md` - Moly-specific patterns
  - Store-based action forwarding
  - Timer-based retry pattern
  - Radio button navigation
  - External link handling
  - Platform-conditional actions (#[cfg])
  - UiRunner event handling
```

## File: `skills/robius-event-action/references/action-patterns.md`
```markdown
# Action Patterns Reference

Additional action patterns from Robrix codebase.

## Selection Action Pattern

```rust
#[derive(Clone, Debug, DefaultNone)]
pub enum RoomsListAction {
    /// A room was selected
    Selected(SelectedRoom),
    /// An invite was accepted, convert InviteScreen to RoomScreen
    InviteAccepted { room_name_id: RoomNameId },
    None,
}

// In RoomsList widget
fn handle_item_click(&mut self, cx: &mut Cx, scope: &mut Scope, room_id: &RoomId) {
    let selected_room = SelectedRoom::JoinedRoom {
        room_name_id: self.get_room_name(room_id),
    };

    cx.widget_action(
        self.widget_uid(),
        &scope.path,
        RoomsListAction::Selected(selected_room),
    );
}

// In App::handle_actions
if let RoomsListAction::Selected(selected_room) = action.as_widget_action().cast() {
    self.app_state.selected_room = Some(selected_room);
    self.update_header(cx, &selected_room);
    self.ui.redraw(cx);
    continue;
}
```

## Modal Action Pattern

```rust
#[derive(Debug, Clone)]
pub enum ModalAction {
    Open { kind: ModalKind },
    Close { was_internal: bool },
}

pub enum ModalKind {
    Confirmation { title: String, message: String },
    Input { title: String, placeholder: String },
}

// Opening modal from anywhere
cx.action(ModalAction::Open {
    kind: ModalKind::Confirmation {
        title: "Delete?".to_string(),
        message: "This cannot be undone.".to_string(),
    },
});

// In App::handle_actions
match action.downcast_ref() {
    Some(ModalAction::Open { kind }) => {
        self.ui.my_modal(ids!(modal_inner)).set_kind(cx, kind.clone());
        self.ui.modal(ids!(modal_container)).open(cx);
        continue;
    }
    Some(ModalAction::Close { was_internal }) => {
        if *was_internal {
            self.ui.modal(ids!(modal_container)).close(cx);
        }
        continue;
    }
    _ => {}
}
```

## Result Action Pattern

For async operation results:

```rust
#[derive(Debug)]
pub enum JoinRoomResultAction {
    Joined { room_id: OwnedRoomId },
    Failed { room_id: OwnedRoomId, error: Error },
}

// In async task
let result_action = match client.join_room_by_id(&room_id).await {
    Ok(_room) => JoinRoomResultAction::Joined { room_id },
    Err(e) => JoinRoomResultAction::Failed { room_id, error: e },
};
Cx::post_action(result_action);

// In App::handle_actions (NOT widget action!)
if let Some(result) = action.downcast_ref::<JoinRoomResultAction>() {
    match result {
        JoinRoomResultAction::Joined { room_id } => {
            self.show_notification(cx, "Room joined!");
            self.navigate_to_room(cx, room_id);
        }
        JoinRoomResultAction::Failed { room_id, error } => {
            self.show_error(cx, &format!("Failed to join: {}", error));
        }
    }
    continue;
}
```

## Tooltip Action Pattern

```rust
#[derive(Clone, DefaultNone)]
pub enum TooltipAction {
    HoverIn { text: String, widget_rect: Rect, options: TooltipOptions },
    HoverOut,
    None,
}

// In widget that shows tooltip
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    match event.hits(cx, self.view.area()) {
        Hit::FingerHoverIn(_) => {
            let rect = self.view.area().rect(cx);
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                TooltipAction::HoverIn {
                    text: self.tooltip_text.clone(),
                    widget_rect: rect,
                    options: TooltipOptions::default(),
                },
            );
        }
        Hit::FingerHoverOut(_) => {
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                TooltipAction::HoverOut,
            );
        }
        _ => {}
    }
}

// In App::handle_actions
match action.as_widget_action().cast() {
    TooltipAction::HoverIn { text, widget_rect, options } => {
        self.ui.tooltip(ids!(app_tooltip))
            .show_with_options(cx, &text, widget_rect, options);
        continue;
    }
    TooltipAction::HoverOut => {
        self.ui.tooltip(ids!(app_tooltip)).hide(cx);
        continue;
    }
    _ => {}
}
```

## Navigation Action Pattern

```rust
#[derive(Debug)]
pub enum AppStateAction {
    RoomFocused(SelectedRoom),
    FocusNone,
    NavigateToRoom {
        room_to_close: Option<OwnedRoomId>,
        destination_room: BasicRoomDetails,
    },
    RoomLoadedSuccessfully(RoomNameId),
}

// Usage
cx.action(AppStateAction::NavigateToRoom {
    room_to_close: Some(current_room_id.clone()),
    destination_room: new_room_details,
});
```

## State Synchronization Action

For keeping state in sync across widgets:

```rust
#[derive(Debug, Clone)]
pub enum SyncAction {
    SelectedItemChanged(ItemId),
    FilterChanged(String),
    SortChanged(SortOrder),
}

// Emitting from source widget
fn on_selection_change(&mut self, cx: &mut Cx, scope: &mut Scope, item_id: ItemId) {
    cx.widget_action(
        self.widget_uid(),
        &scope.path,
        SyncAction::SelectedItemChanged(item_id),
    );
}

// Multiple widgets can listen and react
// In DetailView:
if let SyncAction::SelectedItemChanged(item_id) = action.as_widget_action().cast() {
    self.load_item_details(cx, item_id);
}

// In SidePanel:
if let SyncAction::SelectedItemChanged(item_id) = action.as_widget_action().cast() {
    self.highlight_item(cx, item_id);
}
```
```

## File: `skills/robius-event-action/references/event-handling.md`
```markdown
# Event Handling Reference

Detailed event handling patterns.

## Event Types

### System Events

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    match event {
        Event::Startup => {
            // App just started
        }
        Event::Shutdown => {
            // App is closing, save state
        }
        Event::Signal => {
            // Background task signaled UI
            self.poll_updates(cx);
        }
        Event::WindowGeomChange(geom) => {
            // Window size/position changed
        }
        Event::WindowCloseRequested(_) => {
            // User clicked close button
        }
        _ => {}
    }
}
```

### Input Events

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    match event {
        Event::KeyDown(ke) => {
            // Key pressed
            if ke.key_code == KeyCode::Return {
                // Enter key
            }
        }
        Event::KeyUp(ke) => {
            // Key released
        }
        Event::TextInput(ti) => {
            // Text was typed
            let text = &ti.input;
        }
        Event::TextCopy(tc) => {
            // Copy requested
            tc.response = Some(self.get_selected_text());
        }
        _ => {}
    }
}
```

### Hit Events

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    let area = self.view.area();

    match event.hits(cx, area) {
        Hit::FingerDown(fe) => {
            // Touch/click started
            cx.set_key_focus(area);
            self.drag_start = Some(fe.abs);
        }
        Hit::FingerUp(fe) => {
            // Touch/click ended
            if fe.is_over && fe.is_primary_hit() {
                if fe.was_tap() {
                    // Quick tap
                }
                if fe.was_long_press() {
                    // Long press (context menu)
                }
            }
            self.drag_start = None;
        }
        Hit::FingerMove(fe) => {
            // Drag
            if let Some(start) = self.drag_start {
                let delta = fe.abs - start;
                self.handle_drag(cx, delta);
            }
        }
        Hit::FingerHoverIn(_) => {
            self.is_hovered = true;
            self.animator_play(cx, id!(hover.on));
        }
        Hit::FingerHoverOut(_) => {
            self.is_hovered = false;
            self.animator_play(cx, id!(hover.off));
        }
        Hit::FingerHoverOver(fe) => {
            // Continuous hover position
            self.hover_pos = fe.abs;
        }
        Hit::FingerScroll(se) => {
            // Scroll wheel
            self.scroll_offset += se.scroll;
        }
        Hit::FingerLongPress(lpe) => {
            // Long press detected (before finger up)
            self.show_context_menu(cx, lpe.abs);
        }
        Hit::Nothing => {
            // Event didn't hit this widget
        }
    }
}
```

## Focus Management

```rust
impl Widget for MyInput {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        let area = self.view.area();

        match event.hits(cx, area) {
            Hit::FingerDown(_) => {
                // Take keyboard focus
                cx.set_key_focus(area);
            }
            _ => {}
        }

        // Check if we have focus
        if cx.has_key_focus(area) {
            if let Event::KeyDown(ke) = event {
                // Handle keyboard input
            }
        }
    }
}
```

## Event Bubbling Control

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Forward to children first
        self.view.handle_event(cx, event, scope);

        // Then handle at this level
        // If you want to stop propagation, simply don't forward

        // For hit events, use captures
        let area = self.view.area();
        match event.hits(cx, area) {
            Hit::FingerDown(_) => {
                cx.set_key_focus(area);
                // Capture all future events until finger up
                cx.set_finger_capture(area);
            }
            _ => {}
        }
    }
}
```

## Timer Events

```rust
live_design! {
    MyWidget = {{MyWidget}} {
        animator: {
            tick = {
                default: on
                on = {
                    from: { all: Loop { duration: 1.0 } }
                    apply: { }  // Empty, just triggers redraw
                }
            }
        }
    }
}

impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if self.animator_handle_event(cx, event).is_animating() {
            // Animation is running, update state
            self.update_animation(cx);
        }
    }
}
```

## Window Events

```rust
impl MatchEvent for App {
    fn handle_window_close_requested(&mut self, cx: &mut Cx, _ce: &WindowCloseRequestedEvent) {
        // Can prevent close
        // cx.prevent_default();

        // Or allow it
        // (do nothing)
    }

    fn handle_window_focus_change(&mut self, cx: &mut Cx, event: &WindowFocusChangeEvent) {
        if event.is_focused {
            // Window gained focus
        } else {
            // Window lost focus
        }
    }
}
```

## Drag and Drop

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    match event {
        Event::DragEnter(de) => {
            self.show_drop_indicator(cx);
        }
        Event::DragLeave(_) => {
            self.hide_drop_indicator(cx);
        }
        Event::DragOver(de) => {
            self.update_drop_position(cx, de.abs);
        }
        Event::Drop(de) => {
            self.handle_drop(cx, &de.items);
        }
        _ => {}
    }
}
```
```

## File: `skills/robius-event-action/references/moly-action-patterns.md`
```markdown
# Moly Action Patterns

Additional action patterns from Moly codebase.

## Store-Based Action Handling

Moly uses a central Store that handles its own actions:

```rust
#[derive(Clone, DefaultNone, Debug)]
pub enum StoreAction {
    Search(String),
    ResetSearch,
    Sort(SortCriteria),
    None,
}

impl Store {
    pub fn handle_action(&mut self, action: &Action) {
        self.search.handle_action(action);
        self.downloads.handle_action(action);

        if let Some(_) = action.downcast_ref::<DownloadFileAction>() {
            self.update_downloads();
        }
    }
}

// In App::handle_actions:
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        for action in actions.iter() {
            // Forward all actions to Store
            self.store.as_mut().unwrap().handle_action(action);

            // Handle app-level actions
            match action.cast() {
                StoreAction::Search(keywords) => {
                    self.store.as_mut().unwrap().search.load_search_results(keywords);
                }
                StoreAction::ResetSearch => {
                    self.store.as_mut().unwrap().search.load_featured_models();
                }
                _ => {}
            }
        }
    }
}
```

## Domain-Specific Action Enums

Organize actions by domain:

```rust
// Chat domain actions
#[derive(Clone, DefaultNone, Debug)]
pub enum ChatAction {
    StartWithoutEntity,
    Start(BotId),
    ChatSelected(ChatID),
    None,
}

// Download domain actions
#[derive(Clone, DefaultNone, Debug)]
pub enum DownloadAction {
    Play(FileID),
    Pause(FileID),
    Cancel(FileID),
    None,
}

// Navigation actions
#[derive(Clone, DefaultNone, Debug)]
pub enum NavigationAction {
    NavigateToProviders,
    NavigateToMyModels,
    None,
}

// Popup actions
#[derive(Clone, DefaultNone, Debug)]
pub enum DownloadNotificationPopupAction {
    ActionLinkClicked,
    CloseButtonClicked,
    None,
}
```

## Timer-Based Retry Pattern

Using timers for retry logic:

```rust
#[derive(Live, LiveHook)]
pub struct App {
    #[live]
    pub ui: WidgetRef,

    #[rust]
    timer: Timer,

    #[rust]
    retry_attempts: usize,

    #[rust]
    pending_file_id: Option<FileID>,
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Check if timer fired
        if self.timer.is_event(event).is_some() {
            if let Some(file_id) = &self.pending_file_id {
                // Retry the operation
                self.store.as_mut().unwrap().downloads.retry(file_id);
                self.ui.redraw(cx);
            }
        }

        // ... rest of event handling
    }
}

impl App {
    fn start_retry_timeout(&mut self, cx: &mut Cx, file: File) {
        match self.retry_attempts {
            0 => {
                self.timer = cx.start_timeout(15.0);
                self.retry_attempts += 1;
            }
            1 => {
                self.timer = cx.start_timeout(30.0);
                self.retry_attempts += 1;
            }
            2 => {
                self.timer = cx.start_timeout(60.0);
                self.retry_attempts += 1;
            }
            _ => {
                // Max retries reached
                self.show_error(cx, &file);
                self.retry_attempts = 0;
            }
        }
    }
}
```

## Radio Button Navigation Pattern

Using radio buttons for tab navigation:

```rust
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        let mut navigate_to_chat = false;
        let mut navigate_to_settings = false;
        let mut navigate_to_providers = false;

        // Create radio button set
        let radio_button_set = self.ui.radio_button_set(ids!(
            sidebar_menu.chat_tab,
            sidebar_menu.settings_tab,
            sidebar_menu.providers_tab,
        ));

        // Check which tab was selected
        if let Some(selected_tab) = radio_button_set.selected(cx, actions) {
            match selected_tab {
                0 => navigate_to_chat = true,
                1 => navigate_to_settings = true,
                2 => navigate_to_providers = true,
                _ => {}
            }
        }

        // Process other actions...
        for action in actions.iter() {
            // Auto-select chat tab when starting a new chat
            if let ChatAction::Start(_) = action.cast() {
                let chat_button = self.ui.radio_button(id!(chat_tab));
                chat_button.select(cx, &mut Scope::empty());
            }

            // Handle navigation action from anywhere
            if let NavigationAction::NavigateToProviders = action.cast() {
                let providers_button = self.ui.radio_button(id!(providers_tab));
                providers_button.select(cx, &mut Scope::empty());
                navigate_to_providers = true;
            }
        }

        // Execute navigation after processing all actions
        if navigate_to_providers {
            self.navigate_to(cx, id!(providers_frame));
        } else if navigate_to_chat {
            self.navigate_to(cx, id!(chat_frame));
        } else if navigate_to_settings {
            self.navigate_to(cx, id!(settings_frame));
        }
    }
}
```

## External Link Action Pattern

Handle link clicks to open external URLs:

```rust
use markdown::MarkdownAction;

impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        for action in actions.iter() {
            // Handle markdown link clicks
            if let MarkdownAction::LinkNavigated(url) = action.as_widget_action().cast() {
                // Open external link using robius-open
                let _ = robius_open::Uri::new(&url).open();
            }
        }
    }
}
```

## Conditional Feature Actions

Platform-specific action handling:

```rust
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        let radio_button_set;

        // Different tab sets for different platforms
        #[cfg(not(target_arch = "wasm32"))]
        {
            radio_button_set = self.ui.radio_button_set(ids!(
                sidebar_menu.chat_tab,
                sidebar_menu.local_tab,
                sidebar_menu.mcp_tab,      // MCP only on native
                sidebar_menu.providers_tab,
            ));
            // Show MCP tab on native
            self.ui.view(id!(sidebar_menu.mcp_tab_container))
                .set_visible(cx, true);
        }

        #[cfg(target_arch = "wasm32")]
        {
            radio_button_set = self.ui.radio_button_set(ids!(
                sidebar_menu.chat_tab,
                sidebar_menu.local_tab,
                sidebar_menu.providers_tab,
            ));
            // Hide MCP tab on WASM
            self.ui.view(id!(sidebar_menu.mcp_tab_container))
                .set_visible(cx, false);
        }

        if let Some(selected_tab) = radio_button_set.selected(cx, actions) {
            #[cfg(not(target_arch = "wasm32"))]
            match selected_tab {
                0 => self.navigate_to(cx, id!(chat_frame)),
                1 => self.navigate_to(cx, id!(local_frame)),
                2 => self.navigate_to(cx, id!(mcp_frame)),
                3 => self.navigate_to(cx, id!(providers_frame)),
                _ => {}
            }

            #[cfg(target_arch = "wasm32")]
            match selected_tab {
                0 => self.navigate_to(cx, id!(chat_frame)),
                1 => self.navigate_to(cx, id!(local_frame)),
                2 => self.navigate_to(cx, id!(providers_frame)),
                _ => {}
            }
        }
    }
}
```

## UiRunner Event Handling

Using UiRunner in AppMain:

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Handle UiRunner deferred callbacks first
        self.ui_runner()
            .handle(cx, event, &mut Scope::empty(), self);

        // Handle startup
        if let Event::Startup = event {
            self.ui.view(id!(body)).set_visible(cx, false);
            Store::load_into_app();  // Async store loading
        }

        // Early return if store not loaded
        let Some(store) = self.store.as_mut() else {
            self.ui.handle_event(cx, event, &mut Scope::empty());
            return;
        };

        // Pass store through scope
        let scope = &mut Scope::with_data(store);
        self.ui.handle_event(cx, event, scope);
        self.match_event(cx, event);
    }
}

// The UiRunner accessor
pub fn app_runner() -> UiRunner<App> {
    UiRunner::new(0)  // 0 is reserved for AppMain implementor
}
```
```

## File: `skills/robius-matrix-integration/SKILL.md`
```markdown
---
name: robius-matrix-integration
description: |
  CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on:
  Matrix SDK, sliding sync, MatrixRequest, timeline,
  matrix-sdk, matrix client, robrix, matrix room,
  Matrix 集成, 聊天客户端
---

# Robius Matrix SDK Integration Skill

Best practices for integrating external APIs with Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix SDK integration - sliding sync, timeline subscriptions, real-time updates
- **Moly**: OpenAI/LLM API integration - SSE streaming, MCP protocol, multi-provider support

## Triggers

Use this skill when:
- Integrating Matrix SDK with Makepad
- Building a Matrix client with Makepad
- Implementing Matrix features (rooms, timelines, messages)
- Handling Matrix SDK async operations in UI
- Keywords: matrix-sdk, matrix client, robrix, matrix timeline, matrix room, sliding sync

## Overview

Robrix uses the `matrix-sdk` and `matrix-sdk-ui` crates to connect to Matrix homeservers. The key architectural decisions:

1. **Sliding Sync**: Uses native sliding sync for efficient room list updates
2. **Separate Runtime**: Tokio runtime runs Matrix operations, Makepad handles UI
3. **Request/Response Pattern**: UI sends requests, receives actions/updates back
4. **Per-Room Background Tasks**: Each room has dedicated timeline subscriber task

## MatrixRequest Pattern

### Request Enum Definition

```rust
/// All async requests that can be made to the Matrix worker task
pub enum MatrixRequest {
    /// Login requests
    Login(LoginRequest),
    Logout { is_desktop: bool },

    /// Timeline operations
    PaginateRoomTimeline {
        room_id: OwnedRoomId,
        num_events: u16,
        direction: PaginationDirection,
    },
    SendMessage {
        room_id: OwnedRoomId,
        message: RoomMessageEventContent,
        replied_to: Option<Reply>,
    },
    EditMessage {
        room_id: OwnedRoomId,
        timeline_event_item_id: TimelineEventItemId,
        edited_content: EditedContent,
    },
    RedactMessage {
        room_id: OwnedRoomId,
        timeline_event_id: TimelineEventItemId,
        reason: Option<String>,
    },

    /// Room operations
    JoinRoom { room_id: OwnedRoomId },
    LeaveRoom { room_id: OwnedRoomId },
    GetRoomMembers {
        room_id: OwnedRoomId,
        memberships: RoomMemberships,
        local_only: bool,
    },

    /// User operations
    GetUserProfile {
        user_id: OwnedUserId,
        room_id: Option<OwnedRoomId>,
        local_only: bool,
    },
    IgnoreUser {
        ignore: bool,
        room_member: RoomMember,
        room_id: OwnedRoomId,
    },

    /// Media operations
    FetchAvatar {
        mxc_uri: OwnedMxcUri,
        on_fetched: fn(AvatarUpdate),
    },
    FetchMedia {
        media_request: MediaRequestParameters,
        on_fetched: OnMediaFetchedFn,
        destination: MediaCacheEntryRef,
        update_sender: Option<crossbeam_channel::Sender<TimelineUpdate>>,
    },

    /// Typing/read indicators
    SendTypingNotice { room_id: OwnedRoomId, typing: bool },
    ReadReceipt { room_id: OwnedRoomId, event_id: OwnedEventId },
    FullyReadReceipt { room_id: OwnedRoomId, event_id: OwnedEventId },

    /// Reactions
    ToggleReaction {
        room_id: OwnedRoomId,
        timeline_event_id: TimelineEventItemId,
        reaction: String,
    },

    /// Subscriptions
    SubscribeToTypingNotices { room_id: OwnedRoomId, subscribe: bool },
    SubscribeToPinnedEvents { room_id: OwnedRoomId, subscribe: bool },
}
```

### Submit Pattern

```rust
static REQUEST_SENDER: Mutex<Option<UnboundedSender<MatrixRequest>>> = Mutex::new(None);

/// Submit request from UI thread to async runtime
pub fn submit_async_request(req: MatrixRequest) {
    if let Some(sender) = REQUEST_SENDER.lock().unwrap().as_ref() {
        sender.send(req).expect("BUG: matrix worker task receiver died!");
    }
}

// Usage in UI
submit_async_request(MatrixRequest::SendMessage {
    room_id: room_id.clone(),
    message: RoomMessageEventContent::text_plain(&text),
    replied_to: self.reply_to.take(),
});
```

## Worker Task Handler

```rust
async fn matrix_worker_task(
    mut request_receiver: UnboundedReceiver<MatrixRequest>,
    login_sender: Sender<LoginRequest>,
) -> Result<()> {
    while let Some(request) = request_receiver.recv().await {
        match request {
            MatrixRequest::PaginateRoomTimeline { room_id, num_events, direction } => {
                let (timeline, sender) = {
                    let rooms = ALL_JOINED_ROOMS.lock().unwrap();
                    let Some(room_info) = rooms.get(&room_id) else {
                        continue;  // Room not ready yet
                    };
                    (room_info.timeline.clone(), room_info.update_sender.clone())
                };

                // Spawn dedicated task for this operation
                Handle::current().spawn(async move {
                    // Notify UI pagination is starting
                    sender.send(TimelineUpdate::PaginationRunning(direction)).unwrap();
                    SignalToUI::set_ui_signal();

                    // Perform pagination
                    let res = if direction == PaginationDirection::Forwards {
                        timeline.paginate_forwards(num_events).await
                    } else {
                        timeline.paginate_backwards(num_events).await
                    };

                    // Send result to UI
                    match res {
                        Ok(fully_paginated) => {
                            sender.send(TimelineUpdate::PaginationIdle {
                                fully_paginated,
                                direction,
                            }).unwrap();
                        }
                        Err(error) => {
                            sender.send(TimelineUpdate::PaginationError {
                                error,
                                direction,
                            }).unwrap();
                        }
                    }
                    SignalToUI::set_ui_signal();
                });
            }

            MatrixRequest::JoinRoom { room_id } => {
                let Some(client) = get_client() else { continue };

                Handle::current().spawn(async move {
                    let result_action = if let Some(room) = client.get_room(&room_id) {
                        match room.join().await {
                            Ok(()) => JoinRoomResultAction::Joined { room_id },
                            Err(e) => JoinRoomResultAction::Failed { room_id, error: e },
                        }
                    } else {
                        match client.join_room_by_id(&room_id).await {
                            Ok(_) => JoinRoomResultAction::Joined { room_id },
                            Err(e) => JoinRoomResultAction::Failed { room_id, error: e },
                        }
                    };
                    Cx::post_action(result_action);
                });
            }
            // ... handle other requests
        }
    }
    Ok(())
}
```

## Timeline Updates

### TimelineUpdate Enum

```rust
pub enum TimelineUpdate {
    /// New items added to timeline
    NewItems {
        new_items: Vector<Arc<TimelineItem>>,
        changed_indices: BTreeSet<usize>,
        is_append: bool,
    },
    /// Pagination state changes
    PaginationRunning(PaginationDirection),
    PaginationIdle {
        fully_paginated: bool,
        direction: PaginationDirection,
    },
    PaginationError {
        error: Error,
        direction: PaginationDirection,
    },
    /// Message edit result
    MessageEdited {
        timeline_event_id: TimelineEventItemId,
        result: Result<(), Error>,
    },
    /// Room members fetched
    RoomMembersListFetched {
        members: Vec<RoomMember>,
        sort: PrecomputedMemberSort,
        is_local_fetch: bool,
    },
    /// Unread count updated
    NewUnreadMessagesCount(UnreadMessageCount),
    /// User power levels fetched
    UserPowerLevels(UserPowerLevels),
}
```

### Per-Room Update Flow

```rust
struct JoinedRoomDetails {
    room_id: OwnedRoomId,
    timeline: Arc<Timeline>,
    timeline_update_sender: crossbeam_channel::Sender<TimelineUpdate>,
    timeline_subscriber_handler_task: JoinHandle<()>,
    typing_notice_subscriber: Option<EventHandlerDropGuard>,
}

impl Drop for JoinedRoomDetails {
    fn drop(&mut self) {
        // Cleanup background tasks when room closes
        self.timeline_subscriber_handler_task.abort();
        drop(self.typing_notice_subscriber.take());
    }
}

// Spawn subscriber for a room
async fn spawn_timeline_subscriber(
    room_id: OwnedRoomId,
    timeline: Arc<Timeline>,
    sender: crossbeam_channel::Sender<TimelineUpdate>,
) -> JoinHandle<()> {
    tokio::spawn(async move {
        let (items, mut stream) = timeline.subscribe().await;

        // Send initial items
        sender.send(TimelineUpdate::NewItems {
            new_items: items,
            changed_indices: BTreeSet::new(),
            is_append: false,
        }).unwrap();
        SignalToUI::set_ui_signal();

        // Listen for updates
        while let Some(diff) = stream.next().await {
            let update = process_timeline_diff(diff);
            sender.send(update).unwrap();
            SignalToUI::set_ui_signal();
        }
    })
}
```

### Handling Updates in UI

```rust
impl Widget for RoomScreen {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Poll timeline updates on Signal events
        if let Event::Signal = event {
            while let Ok(update) = self.timeline_state.update_receiver.try_recv() {
                match update {
                    TimelineUpdate::NewItems { new_items, changed_indices, is_append } => {
                        self.apply_new_items(cx, new_items, changed_indices, is_append);
                    }
                    TimelineUpdate::PaginationIdle { fully_paginated, direction } => {
                        self.set_pagination_idle(cx, direction, fully_paginated);
                    }
                    TimelineUpdate::PaginationError { error, direction } => {
                        self.show_pagination_error(cx, direction, &error);
                    }
                    // ... handle other updates
                }
            }
        }

        self.view.handle_event(cx, event, scope);
    }
}
```

## Room List Updates

### RoomsListUpdate Enum

```rust
pub enum RoomsListUpdate {
    NotLoaded,
    LoadedRooms { max_rooms: Option<u32> },
    AddInvitedRoom(InvitedRoomInfo),
    AddJoinedRoom(JoinedRoomInfo),
    ClearRooms,
    UpdateLatestEvent {
        room_id: OwnedRoomId,
        timestamp: MilliSecondsSinceUnixEpoch,
        latest_message_text: String,
    },
    UpdateNumUnreadMessages {
        room_id: OwnedRoomId,
        unread_messages: UnreadMessageCount,
        unread_mentions: u64,
    },
    UpdateRoomName { new_room_name: RoomNameId },
    UpdateRoomAvatar { room_id: OwnedRoomId, avatar: FetchedRoomAvatar },
    RemoveRoom { room_id: OwnedRoomId, new_state: RoomState },
    Status { status: String },
    ScrollToRoom(OwnedRoomId),
}

static PENDING_ROOM_UPDATES: SegQueue<RoomsListUpdate> = SegQueue::new();

pub fn enqueue_rooms_list_update(update: RoomsListUpdate) {
    PENDING_ROOM_UPDATES.push(update);
    SignalToUI::set_ui_signal();
}
```

## Client Build Pattern

```rust
async fn build_client(
    homeserver_url: &str,
    data_dir: &Path,
) -> Result<(Client, ClientSessionPersisted)> {
    // Generate unique subfolder for this session
    let db_subfolder = format!("db_{}", chrono::Local::now().format("%F_%H_%M_%S_%f"));
    let db_path = data_dir.join(db_subfolder);

    // Generate random passphrase for encryption
    let passphrase: String = {
        use rand::{Rng, thread_rng};
        thread_rng()
            .sample_iter(rand::distributions::Alphanumeric)
            .take(32)
            .map(char::from)
            .collect()
    };

    let client = Client::builder()
        .server_name_or_homeserver_url(homeserver_url)
        .sqlite_store(&db_path, Some(&passphrase))
        .sliding_sync_version_builder(VersionBuilder::DiscoverNative)
        .with_decryption_settings(DecryptionSettings {
            sender_device_trust_requirement: TrustRequirement::Untrusted,
        })
        .with_encryption_settings(EncryptionSettings {
            auto_enable_cross_signing: true,
            backup_download_strategy: BackupDownloadStrategy::OneShot,
            auto_enable_backups: true,
        })
        .request_config(
            RequestConfig::new().timeout(Duration::from_secs(60))
        )
        .build()
        .await?;

    Ok((client, ClientSessionPersisted { homeserver: homeserver_url.to_string(), db_path, passphrase }))
}
```

## Best Practices

1. **Always spawn tasks**: Don't block the worker task receiver loop
2. **Use crossbeam channels for per-room updates**: More efficient than global queue
3. **Always call SignalToUI::set_ui_signal()**: After enqueueing any update
4. **Handle room not ready**: Skip requests for rooms not yet in `ALL_JOINED_ROOMS`
5. **Cleanup on drop**: Abort background tasks when rooms are closed
6. **Use Cx::post_action for results**: Posted actions are handled in App::handle_actions
7. **Use SegQueue for high-frequency updates**: Lock-free for room list updates

## Reference Files

- `references/matrix-client.md` - Matrix client setup and login patterns (Robrix)
- `references/timeline-handling.md` - Matrix timeline subscription patterns (Robrix)
- `references/moly-api-integration.md` - Moly API integration patterns
  - OpenAI client with SSE streaming
  - Platform-agnostic async streams
  - MCP (Model Context Protocol) integration
  - Tool approval flow
  - MolyClient for local server
  - BotContext for multi-provider support
```

## File: `skills/robius-matrix-integration/references/matrix-client.md`
```markdown
# Matrix Client Reference

Client setup, login, and session management patterns.

## Login Flow

### Login Types

```rust
pub enum LoginRequest {
    /// Login with username/password
    LoginByPassword(LoginByPassword),
    /// Login via SSO completed
    LoginBySSOSuccess(Client, ClientSessionPersisted),
    /// Login with CLI args (testing)
    LoginByCli,
    /// Query available login types for homeserver
    HomeserverLoginTypesQuery(String),
}

pub struct LoginByPassword {
    pub user_id: String,
    pub password: String,
    pub homeserver: Option<String>,
}
```

### Login Implementation

```rust
async fn login(
    login_request: LoginRequest,
) -> Result<(Client, Option<String>)> {
    match login_request {
        LoginRequest::LoginByPassword(creds) => {
            let (client, session) = build_client(&creds.homeserver, app_data_dir()).await?;

            let login_result = client
                .matrix_auth()
                .login_username(&creds.user_id, &creds.password)
                .initial_device_display_name("my-app-device")
                .send()
                .await?;

            if client.matrix_auth().logged_in() {
                log!("Logged in successfully.");

                // Save session for future restoration
                if let Err(e) = persistence::save_session(&client, session).await {
                    error!("Failed to save session: {e}");
                }

                // Notify UI of success
                enqueue_rooms_list_update(RoomsListUpdate::Status {
                    status: format!("Logged in as {}. Loading rooms...", creds.user_id)
                });

                Ok((client, None))
            } else {
                bail!("Login failed: {:?}", login_result);
            }
        }

        LoginRequest::LoginBySSOSuccess(client, session) => {
            if let Err(e) = persistence::save_session(&client, session).await {
                error!("Failed to save session: {e:?}");
            }
            Ok((client, None))
        }
        // ...
    }
}
```

### Session Restoration

```rust
async fn try_restore_session() -> Result<Option<(Client, String)>> {
    let session_path = app_data_dir().join("session.json");

    let session: ClientSessionPersisted = match tokio::fs::read_to_string(&session_path).await {
        Ok(json) => serde_json::from_str(&json)?,
        Err(e) if e.kind() == std::io::ErrorKind::NotFound => {
            return Ok(None);
        }
        Err(e) => return Err(e.into()),
    };

    // Rebuild client from saved session
    let client = Client::builder()
        .homeserver_url(&session.homeserver)
        .sqlite_store(&session.db_path, Some(&session.passphrase))
        .sliding_sync_version_builder(VersionBuilder::DiscoverNative)
        .build()
        .await?;

    // Check if still logged in
    if !client.logged_in() {
        log!("Session expired, need to re-login");
        return Ok(None);
    }

    // Get sync token if available
    let sync_token = client.sync_token().await;

    Ok(Some((client, sync_token.unwrap_or_default())))
}
```

## Room List Service

```rust
async fn setup_room_list_service(client: &Client) -> Result<RoomListService> {
    let room_list_service = client
        .room_list_service()
        .all_rooms()
        .await?;

    // Configure filters
    room_list_service.apply_input(
        RoomListInput::Visible {
            ranges: vec![0..20],  // Initial visible range
        }
    ).await?;

    Ok(room_list_service)
}

async fn subscribe_to_room_list(room_list_service: RoomListService) {
    let mut rooms_stream = room_list_service.entries();

    while let Some(room_list_entries) = rooms_stream.next().await {
        for entry in room_list_entries {
            match entry {
                RoomListEntry::Filled(room_id) => {
                    // Room became available
                    if let Some(room) = client.get_room(&room_id) {
                        let room_info = build_room_info(&room).await;
                        enqueue_rooms_list_update(RoomsListUpdate::AddJoinedRoom(room_info));
                    }
                }
                RoomListEntry::Empty | RoomListEntry::Invalidated(_) => {
                    // Room removed or invalidated
                }
            }
        }
    }
}
```

## Sync Service

```rust
async fn run_sync_service(client: Client) -> Result<()> {
    let sync_service = SyncService::builder(client.clone())
        .build()
        .await?;

    // Start syncing
    sync_service.start().await;

    // Monitor sync state
    let mut state_stream = sync_service.state();
    while let Some(state) = state_stream.next().await {
        match state {
            SyncServiceState::Running => {
                log!("Sync running");
            }
            SyncServiceState::Terminated => {
                log!("Sync terminated");
                break;
            }
            SyncServiceState::Error => {
                error!("Sync error");
            }
            _ => {}
        }
    }

    Ok(())
}
```

## Logout Flow

```rust
async fn logout_with_state_machine(is_desktop: bool) -> Result<()> {
    let Some(client) = get_client() else {
        return Ok(());
    };

    // 1. Notify UI logout is starting
    Cx::post_action(LogoutAction::LogoutStarted);

    // 2. Stop sync service
    if let Some(sync_service) = get_sync_service() {
        sync_service.stop().await?;
    }

    // 3. Clear all room state
    {
        let mut rooms = ALL_JOINED_ROOMS.lock().unwrap();
        rooms.clear();  // Drop will abort background tasks
    }

    // 4. Clear UI state (posted action, handled on UI thread)
    let notify = Arc::new(Notify::new());
    Cx::post_action(LogoutAction::ClearAppState {
        on_clear_appstate: notify.clone(),
    });
    SignalToUI::set_ui_signal();

    // 5. Wait for UI to clear state
    notify.notified().await;

    // 6. Logout from server
    client.matrix_auth().logout().await?;

    // 7. Clear client
    clear_client();

    // 8. Delete session file
    tokio::fs::remove_file(app_data_dir().join("session.json")).await.ok();

    // 9. Notify UI logout complete
    Cx::post_action(LogoutAction::LogoutSuccess);
    SignalToUI::set_ui_signal();

    Ok(())
}
```

## Global Client Access

```rust
static CLIENT: Mutex<Option<Client>> = Mutex::new(None);
static CURRENT_USER_ID: Mutex<Option<OwnedUserId>> = Mutex::new(None);

pub fn get_client() -> Option<Client> {
    CLIENT.lock().unwrap().clone()
}

pub fn set_client(client: Client) {
    let user_id = client.user_id().map(|u| u.to_owned());
    *CLIENT.lock().unwrap() = Some(client);
    *CURRENT_USER_ID.lock().unwrap() = user_id;
}

pub fn clear_client() {
    *CLIENT.lock().unwrap() = None;
    *CURRENT_USER_ID.lock().unwrap() = None;
}

pub fn current_user_id() -> Option<OwnedUserId> {
    CURRENT_USER_ID.lock().unwrap().clone()
}
```
```

## File: `skills/robius-matrix-integration/references/moly-api-integration.md`
```markdown
# Moly API Integration Patterns

Patterns for integrating external APIs with Makepad (OpenAI, MCP, etc.) - complementary to Matrix SDK patterns.

## OpenAI Client Pattern

```rust
use async_stream::stream;
use reqwest::header::{HeaderMap, HeaderName};
use std::sync::Arc;

use crate::utils::asynchronous::{BoxPlatformSendFuture, BoxPlatformSendStream};
use crate::utils::sse::parse_sse;

pub struct OpenAIClient {
    endpoint: String,
    api_key: Option<String>,
    http_client: reqwest::Client,
}

impl OpenAIClient {
    pub fn new(endpoint: String, api_key: Option<String>) -> Self {
        Self {
            endpoint,
            api_key,
            http_client: reqwest::Client::new(),
        }
    }

    /// Fetch available models
    pub fn bots(&self) -> BoxPlatformSendFuture<'static, Result<Vec<Bot>, Error>> {
        let url = format!("{}/models", self.endpoint);
        let client = self.http_client.clone();
        let api_key = self.api_key.clone();

        Box::pin(async move {
            let mut request = client.get(&url);

            if let Some(key) = api_key {
                request = request.bearer_auth(key);
            }

            let response = request.send().await?;
            let models: Models = response.json().await?;

            Ok(models.data.into_iter().map(|m| Bot {
                id: BotId::new(&m.id),
                name: m.id,
            }).collect())
        })
    }

    /// Stream chat completion
    pub fn stream(
        &self,
        bot: &BotId,
        messages: Vec<Message>,
    ) -> BoxPlatformSendStream<'static, StreamItem> {
        let url = format!("{}/chat/completions", self.endpoint);
        let client = self.http_client.clone();
        let api_key = self.api_key.clone();
        let model = bot.id().to_string();

        Box::pin(stream! {
            // Build request body
            let body = serde_json::json!({
                "model": model,
                "messages": messages,
                "stream": true,
            });

            // Send request
            let mut request = client.post(&url)
                .header("Content-Type", "application/json")
                .body(body.to_string());

            if let Some(key) = api_key {
                request = request.bearer_auth(key);
            }

            let response = match request.send().await {
                Ok(r) => r,
                Err(e) => {
                    yield StreamItem::Error(e.into());
                    return;
                }
            };

            if !response.status().is_success() {
                yield StreamItem::Error(format!("HTTP {}", response.status()).into());
                return;
            }

            // Process SSE stream
            let mut stream = response.bytes_stream();
            let mut buffer = String::new();

            while let Some(chunk) = stream.next().await {
                match chunk {
                    Ok(bytes) => {
                        buffer.push_str(&String::from_utf8_lossy(&bytes));

                        // Parse SSE events from buffer
                        for event in parse_sse(&mut buffer) {
                            if event.data == "[DONE]" {
                                yield StreamItem::Done;
                                return;
                            }

                            match serde_json::from_str::<StreamResponse>(&event.data) {
                                Ok(response) => {
                                    if let Some(content) = response.delta_content() {
                                        yield StreamItem::Chunk(content);
                                    }
                                }
                                Err(e) => {
                                    yield StreamItem::Error(e.into());
                                }
                            }
                        }
                    }
                    Err(e) => {
                        yield StreamItem::Error(e.into());
                        return;
                    }
                }
            }
        })
    }
}

pub enum StreamItem {
    Chunk(String),
    Done,
    Error(Error),
}
```

## SSE Parsing Utility

```rust
pub struct SseEvent {
    pub event: Option<String>,
    pub data: String,
}

/// Parse SSE events from a buffer, removing consumed data
pub fn parse_sse(buffer: &mut String) -> Vec<SseEvent> {
    let mut events = Vec::new();

    while let Some(end) = buffer.find("\n\n") {
        let event_str = buffer.drain(..=end + 1).collect::<String>();

        let mut event = SseEvent {
            event: None,
            data: String::new(),
        };

        for line in event_str.lines() {
            if let Some(data) = line.strip_prefix("data: ") {
                event.data.push_str(data);
            } else if let Some(evt) = line.strip_prefix("event: ") {
                event.event = Some(evt.to_string());
            }
        }

        if !event.data.is_empty() {
            events.push(event);
        }
    }

    events
}
```

## Client Integration with UI

```rust
use moly_kit::utils::asynchronous::spawn;
use futures::StreamExt;

impl ChatWidget {
    fn send_message(&mut self, cx: &mut Cx, message: String) {
        let client = self.client.clone();
        let bot_id = self.current_bot.clone();
        let messages = self.build_message_history();

        // Start streaming
        self.set_state(cx, ChatState::Streaming);

        spawn(async move {
            let mut stream = client.stream(&bot_id, messages);

            while let Some(item) = stream.next().await {
                match item {
                    StreamItem::Chunk(text) => {
                        // Defer UI update to main thread
                        chat_runner().defer_with_redraw(move |widget, cx, _| {
                            widget.append_text(cx, &text);
                        });
                    }
                    StreamItem::Done => {
                        chat_runner().defer_with_redraw(move |widget, cx, _| {
                            widget.set_state(cx, ChatState::Idle);
                        });
                    }
                    StreamItem::Error(e) => {
                        chat_runner().defer_with_redraw(move |widget, cx, _| {
                            widget.show_error(cx, &e.to_string());
                            widget.set_state(cx, ChatState::Error);
                        });
                    }
                }
            }
        });
    }
}
```

## MCP (Model Context Protocol) Integration

```rust
pub struct McpManager {
    servers: HashMap<String, McpServer>,
    tools: HashMap<String, Tool>,
}

impl McpManager {
    pub async fn connect_server(&mut self, config: McpServerConfig) -> Result<()> {
        let server = McpServer::connect(&config).await?;

        // Fetch available tools
        let tools = server.list_tools().await?;

        for tool in tools {
            self.tools.insert(tool.name.clone(), tool);
        }

        self.servers.insert(config.name, server);
        Ok(())
    }

    pub async fn call_tool(
        &self,
        tool_name: &str,
        arguments: serde_json::Value,
    ) -> Result<ToolResult> {
        let tool = self.tools.get(tool_name)
            .ok_or_else(|| Error::ToolNotFound(tool_name.to_string()))?;

        // Find server that provides this tool
        for server in self.servers.values() {
            if server.has_tool(tool_name) {
                return server.call_tool(tool_name, arguments).await;
            }
        }

        Err(Error::NoServerForTool(tool_name.to_string()))
    }
}
```

## Tool Approval Flow

```rust
live_design! {
    ToolApprovalActions = <View> {
        spacing: 5,
        approve = <Button> {
            text: "Approve",
            draw_bg: {color: #4CAF50}
        }
        deny = <Button> {
            text: "Deny",
            draw_bg: {color: #f44336}
        }
    }

    pub ToolLine = <ChatLine> {
        message_section = {
            draw_bg: {color: #fff3e0}
            sender = {
                name = {text: "Permission Request"}
            }
            content_section = {
                tool_actions = <ToolApprovalActions> { visible: false }
            }
        }
    }
}

#[derive(Clone, DefaultNone, Debug)]
pub enum ToolApprovalAction {
    Approved { tool_call_id: String },
    Denied { tool_call_id: String },
    None,
}

impl ToolLine {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        if self.button(ids!(approve)).clicked(cx) {
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                ToolApprovalAction::Approved {
                    tool_call_id: self.tool_call_id.clone(),
                },
            );
        }

        if self.button(ids!(deny)).clicked(cx) {
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                ToolApprovalAction::Denied {
                    tool_call_id: self.tool_call_id.clone(),
                },
            );
        }
    }
}
```

## MolyClient Pattern (Local Server)

```rust
#[derive(Clone)]
pub struct MolyClient {
    address: String,
    http_client: reqwest::Client,
    connected: Arc<AtomicBool>,
}

impl MolyClient {
    pub fn new(address: String) -> Self {
        Self {
            address,
            http_client: reqwest::Client::new(),
            connected: Arc::new(AtomicBool::new(false)),
        }
    }

    pub fn address(&self) -> &str {
        &self.address
    }

    pub fn is_connected(&self) -> bool {
        self.connected.load(Ordering::Relaxed)
    }

    pub async fn test_connection(&self) -> Result<()> {
        let url = format!("{}/health", self.address);

        match self.http_client.get(&url).send().await {
            Ok(response) if response.status().is_success() => {
                self.connected.store(true, Ordering::Relaxed);
                Ok(())
            }
            Ok(response) => {
                self.connected.store(false, Ordering::Relaxed);
                Cx::post_action(MolyClientAction::ServerUnreachable);
                Err(format!("Server returned {}", response.status()).into())
            }
            Err(e) => {
                self.connected.store(false, Ordering::Relaxed);
                Cx::post_action(MolyClientAction::ServerUnreachable);
                Err(e.into())
            }
        }
    }

    pub async fn get_featured_models(&self) -> Result<Vec<Model>> {
        let url = format!("{}/api/v1/models/featured", self.address);
        let response = self.http_client.get(&url).send().await?;
        let models: Vec<Model> = response.json().await?;
        Ok(models)
    }

    pub async fn download_file(&self, model: Model, file: File) -> Result<()> {
        // ... download implementation
    }
}

#[derive(Clone, DefaultNone, Debug)]
pub enum MolyClientAction {
    ServerUnreachable,
    None,
}
```

## BotContext for Multi-Provider Support

```rust
pub struct BotContext {
    providers: HashMap<String, Box<dyn BotProvider>>,
    current_provider: Option<String>,
}

pub trait BotProvider: Send + Sync {
    fn bots(&self) -> BoxPlatformSendFuture<'static, Result<Vec<Bot>, Error>>;

    fn stream(
        &self,
        bot: &BotId,
        messages: Vec<Message>,
    ) -> BoxPlatformSendStream<'static, StreamItem>;
}

impl BotContext {
    pub fn add_provider(&mut self, name: String, provider: Box<dyn BotProvider>) {
        self.providers.insert(name, provider);
    }

    pub fn set_current(&mut self, name: &str) {
        if self.providers.contains_key(name) {
            self.current_provider = Some(name.to_string());
        }
    }

    pub fn current(&self) -> Option<&dyn BotProvider> {
        self.current_provider.as_ref()
            .and_then(|name| self.providers.get(name))
            .map(|p| p.as_ref())
    }
}
```
```

## File: `skills/robius-matrix-integration/references/timeline-handling.md`
```markdown
# Timeline Handling Reference

Patterns for Matrix timeline subscription and display.

## Timeline Setup

```rust
async fn setup_room_timeline(
    room: &Room,
    room_id: OwnedRoomId,
) -> Result<JoinedRoomDetails> {
    // Build timeline with options
    let timeline = room
        .timeline_builder()
        .build()
        .await?;

    let timeline = Arc::new(timeline);

    // Create update channel
    let (update_sender, update_receiver) = crossbeam_channel::unbounded();

    // Spawn subscriber task
    let subscriber_task = spawn_timeline_subscriber(
        room_id.clone(),
        timeline.clone(),
        update_sender.clone(),
    );

    Ok(JoinedRoomDetails {
        room_id,
        timeline,
        timeline_update_sender: update_sender,
        timeline_subscriber_handler_task: subscriber_task,
        typing_notice_subscriber: None,
    })
}

fn spawn_timeline_subscriber(
    room_id: OwnedRoomId,
    timeline: Arc<Timeline>,
    sender: crossbeam_channel::Sender<TimelineUpdate>,
) -> JoinHandle<()> {
    tokio::spawn(async move {
        let (initial_items, mut stream) = timeline.subscribe().await;

        // Send initial items
        if sender.send(TimelineUpdate::NewItems {
            new_items: initial_items,
            changed_indices: BTreeSet::new(),
            is_append: false,
        }).is_err() {
            return;  // Receiver dropped
        }
        SignalToUI::set_ui_signal();

        // Process stream updates
        while let Some(diffs) = stream.next().await {
            for diff in diffs {
                let update = match diff {
                    VectorDiff::Append { values } => {
                        TimelineUpdate::NewItems {
                            new_items: values,
                            changed_indices: BTreeSet::new(),
                            is_append: true,
                        }
                    }
                    VectorDiff::PushFront { value } => {
                        TimelineUpdate::NewItems {
                            new_items: Vector::unit(value),
                            changed_indices: BTreeSet::new(),
                            is_append: false,
                        }
                    }
                    VectorDiff::Set { index, value } => {
                        let mut changed = BTreeSet::new();
                        changed.insert(index);
                        TimelineUpdate::NewItems {
                            new_items: Vector::unit(value),
                            changed_indices: changed,
                            is_append: false,
                        }
                    }
                    VectorDiff::Clear => {
                        TimelineUpdate::NewItems {
                            new_items: Vector::new(),
                            changed_indices: BTreeSet::new(),
                            is_append: false,
                        }
                    }
                    _ => continue,
                };

                if sender.send(update).is_err() {
                    return;  // Receiver dropped
                }
                SignalToUI::set_ui_signal();
            }
        }
    })
}
```

## Pagination

```rust
/// Direction of pagination
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum PaginationDirection {
    /// Load older events
    Backwards,
    /// Load newer events (focused mode only)
    Forwards,
}

async fn paginate_timeline(
    timeline: Arc<Timeline>,
    direction: PaginationDirection,
    num_events: u16,
    sender: crossbeam_channel::Sender<TimelineUpdate>,
) {
    // Notify UI pagination started
    sender.send(TimelineUpdate::PaginationRunning(direction)).unwrap();
    SignalToUI::set_ui_signal();

    let result = match direction {
        PaginationDirection::Backwards => {
            timeline.paginate_backwards(num_events).await
        }
        PaginationDirection::Forwards => {
            timeline.paginate_forwards(num_events).await
        }
    };

    let update = match result {
        Ok(fully_paginated) => TimelineUpdate::PaginationIdle {
            fully_paginated,
            direction,
        },
        Err(error) => TimelineUpdate::PaginationError {
            error,
            direction,
        },
    };

    sender.send(update).unwrap();
    SignalToUI::set_ui_signal();
}
```

## Timeline Item Processing

```rust
fn process_timeline_item(item: &TimelineItem) -> ProcessedItem {
    match item.kind() {
        TimelineItemKind::Event(event_item) => {
            process_event_item(event_item)
        }
        TimelineItemKind::Virtual(virtual_item) => {
            process_virtual_item(virtual_item)
        }
    }
}

fn process_event_item(event: &EventTimelineItem) -> ProcessedItem {
    match event.content() {
        TimelineItemContent::Message(msg) => {
            process_message(msg, event)
        }
        TimelineItemContent::RedactedMessage => {
            ProcessedItem::Redacted
        }
        TimelineItemContent::Sticker(sticker) => {
            ProcessedItem::Sticker(sticker.clone())
        }
        TimelineItemContent::MembershipChange(change) => {
            ProcessedItem::Membership(change.clone())
        }
        TimelineItemContent::ProfileChange(change) => {
            ProcessedItem::ProfileChange(change.clone())
        }
        TimelineItemContent::OtherState(state) => {
            ProcessedItem::State(state.clone())
        }
        _ => ProcessedItem::Unsupported,
    }
}

fn process_message(msg: &MsgLikeContent, event: &EventTimelineItem) -> ProcessedItem {
    match msg.kind() {
        MsgLikeKind::Regular(content) => {
            match content.msgtype() {
                MessageType::Text(text) => {
                    ProcessedItem::Text {
                        body: text.body.clone(),
                        formatted: text.formatted.clone(),
                    }
                }
                MessageType::Image(image) => {
                    ProcessedItem::Image {
                        source: image.source.clone(),
                        info: image.info.clone(),
                    }
                }
                MessageType::Video(video) => {
                    ProcessedItem::Video {
                        source: video.source.clone(),
                        info: video.info.clone(),
                    }
                }
                MessageType::Audio(audio) => {
                    ProcessedItem::Audio {
                        source: audio.source.clone(),
                        info: audio.info.clone(),
                    }
                }
                MessageType::File(file) => {
                    ProcessedItem::File {
                        source: file.source.clone(),
                        info: file.info.clone(),
                    }
                }
                MessageType::Location(location) => {
                    ProcessedItem::Location {
                        body: location.body.clone(),
                        geo_uri: location.geo_uri.clone(),
                    }
                }
                _ => ProcessedItem::Unsupported,
            }
        }
        MsgLikeKind::Emote(emote) => {
            ProcessedItem::Emote {
                body: emote.body.clone(),
            }
        }
        MsgLikeKind::Notice(notice) => {
            ProcessedItem::Notice {
                body: notice.body.clone(),
            }
        }
    }
}
```

## Sending Messages

```rust
async fn send_message(
    timeline: Arc<Timeline>,
    room_id: OwnedRoomId,
    message: RoomMessageEventContent,
    replied_to: Option<Reply>,
) {
    let result = if let Some(reply) = replied_to {
        timeline.send_reply(message, reply, ForwardThread::Yes).await
    } else {
        timeline.send(message.into()).await
    };

    match result {
        Ok(()) => {
            log!("Message sent to room {}", room_id);
        }
        Err(e) => {
            error!("Failed to send message: {}", e);
            enqueue_popup_notification(PopupItem {
                message: format!("Failed to send: {}", e),
                kind: PopupKind::Error,
                auto_dismissal_duration: None,
            });
        }
    }
}

async fn edit_message(
    timeline: Arc<Timeline>,
    event_id: TimelineEventItemId,
    new_content: EditedContent,
    sender: crossbeam_channel::Sender<TimelineUpdate>,
) {
    let result = timeline.edit(&event_id, new_content).await;

    sender.send(TimelineUpdate::MessageEdited {
        timeline_event_id: event_id,
        result,
    }).unwrap();
    SignalToUI::set_ui_signal();
}
```

## Media Handling

```rust
async fn fetch_media(
    client: &Client,
    media_request: MediaRequestParameters,
    on_fetched: OnMediaFetchedFn,
    destination: MediaCacheEntryRef,
    update_sender: Option<crossbeam_channel::Sender<TimelineUpdate>>,
) {
    let result = client.media().get_media_content(&media_request, true).await;

    on_fetched(
        &destination,
        media_request,
        result,
        update_sender,
    );
    SignalToUI::set_ui_signal();
}

// Callback function signature
pub type OnMediaFetchedFn = fn(
    &Mutex<MediaCacheEntry>,
    MediaRequestParameters,
    matrix_sdk::Result<Vec<u8>>,
    Option<crossbeam_channel::Sender<TimelineUpdate>>,
);
```

## Event Subscriptions

```rust
async fn subscribe_to_typing_notices(
    room: &Room,
    room_id: OwnedRoomId,
    sender: crossbeam_channel::Sender<TimelineUpdate>,
) -> EventHandlerDropGuard {
    let client = room.client();

    client.add_room_event_handler(&room_id, move |event: SyncTypingEvent| {
        let typing_user_ids: Vec<_> = event.content.user_ids.iter().cloned().collect();

        sender.send(TimelineUpdate::TypingUsers(typing_user_ids)).ok();
        SignalToUI::set_ui_signal();

        async {}
    })
}
```
```

## File: `skills/robius-state-management/SKILL.md`
```markdown
---
name: robius-state-management
description: |
  CRITICAL: Use for Robius state management patterns. Triggers on:
  AppState, persistence, theme switch, 状态管理,
  Scope::with_data, save state, load state, serde,
  状态持久化, 主题切换
---

# Robius State Management Skill

Best practices for state management and persistence in Makepad applications based on Robrix and Moly codebases.

**Source codebases:**
- **Robrix**: Matrix chat client - AppState, SelectedRoom, persistence via serde
- **Moly**: AI chat application - Central Store pattern, async initialization, Preferences

## Triggers

Use this skill when:
- Designing application state structure
- Implementing state persistence
- Passing state through widget tree
- Managing UI state across sessions
- Keywords: app state, makepad state, persistence, Scope::with_data, save state, load state

## Production Patterns

For production-ready state management patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| [06-global-registry](./_base/06-global-registry.md) | Global widget registry with Cx::set_global |
| [07-radio-navigation](./_base/07-radio-navigation.md) | Tab-style navigation with radio buttons |
| [10-state-machine](./_base/10-state-machine.md) | Enum-based state machine widgets |
| [11-theme-switching](./_base/11-theme-switching.md) | Multi-theme support with apply_over |
| [12-local-persistence](./_base/12-local-persistence.md) | Save/load user preferences |

## AppState Structure

### Core State Definition

```rust
use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use matrix_sdk::ruma::OwnedRoomId;

/// App-wide state that is stored persistently across multiple app runs
/// and shared/updated across various parts of the app.
#[derive(Clone, Default, Debug, Serialize, Deserialize)]
pub struct AppState {
    /// The currently-selected room
    pub selected_room: Option<SelectedRoom>,

    /// Saved UI layout state for main view
    pub saved_layout_state: SavedLayoutState,

    /// Per-item saved states (e.g., per-space dock layouts)
    pub saved_state_per_item: HashMap<OwnedRoomId, SavedLayoutState>,

    /// Whether a user is currently logged in
    #[serde(skip)]  // Don't persist login state
    pub logged_in: bool,
}

/// Represents a currently selected item
#[derive(Clone, Debug, Serialize, Deserialize)]
pub enum SelectedRoom {
    JoinedRoom { room_name_id: RoomNameId },
    InvitedRoom { room_name_id: RoomNameId },
    Space { space_name_id: RoomNameId },
}

impl SelectedRoom {
    pub fn room_id(&self) -> &OwnedRoomId {
        match self {
            Self::JoinedRoom { room_name_id } => room_name_id.room_id(),
            Self::InvitedRoom { room_name_id } => room_name_id.room_id(),
            Self::Space { space_name_id } => space_name_id.room_id(),
        }
    }

    /// Upgrade from invited to joined state
    pub fn upgrade_invite_to_joined(&mut self, room_id: &RoomId) -> bool {
        match self {
            Self::InvitedRoom { room_name_id } if room_name_id.room_id() == room_id => {
                let name = room_name_id.clone();
                *self = Self::JoinedRoom { room_name_id: name };
                true
            }
            _ => false,
        }
    }
}

// Equality based on room_id only
impl PartialEq for SelectedRoom {
    fn eq(&self, other: &Self) -> bool {
        self.room_id() == other.room_id()
    }
}
impl Eq for SelectedRoom {}
```

### Layout/Dock State Persistence

```rust
/// A snapshot of UI layout state for restoration
#[derive(Clone, Default, Debug, Serialize, Deserialize)]
pub struct SavedLayoutState {
    /// All items contained in the layout, keyed by ID
    pub layout_items: HashMap<LiveIdSerde, LayoutItemSerde>,

    /// Items currently open, keyed by ID
    pub open_items: HashMap<LiveIdSerde, SelectedRoom>,

    /// Order items were opened (chronological)
    pub item_order: Vec<SelectedRoom>,

    /// Currently selected item when state was saved
    pub selected_item: Option<SelectedRoom>,
}

/// Serializable wrapper for LiveId
#[derive(Clone, Debug, Hash, Eq, PartialEq, Serialize, Deserialize)]
pub struct LiveIdSerde(pub u64);

impl From<LiveId> for LiveIdSerde {
    fn from(id: LiveId) -> Self {
        Self(id.0)
    }
}

impl From<LiveIdSerde> for LiveId {
    fn from(s: LiveIdSerde) -> Self {
        LiveId(s.0)
    }
}
```

## State Propagation via Scope

### Passing State Through Widget Tree

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Forward to MatchEvent
        self.match_event(cx, event);

        // Create Scope with AppState data
        let scope = &mut Scope::with_data(&mut self.app_state);

        // Pass to widget tree - all children can access AppState
        self.ui.handle_event(cx, event, scope);
    }
}
```

### Accessing State in Child Widgets

```rust
impl Widget for RoomScreen {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Access AppState from scope
        if let Some(app_state) = scope.data.get::<AppState>() {
            if let Some(selected) = &app_state.selected_room {
                self.update_for_room(cx, selected);
            }
        }

        self.view.handle_event(cx, event, scope);
    }
}
```

### Modifying State

```rust
impl Widget for RoomsList {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Mutable access to AppState
        if let Some(app_state) = scope.data.get_mut::<AppState>() {
            if self.selection_changed {
                app_state.selected_room = self.get_selected();
            }
        }
    }
}
```

## Persistence Layer

### File Paths

```rust
use std::path::{Path, PathBuf};

const LATEST_APP_STATE_FILE_NAME: &str = "latest_app_state.json";
const WINDOW_GEOM_STATE_FILE_NAME: &str = "window_geom_state.json";

/// Get user-specific persistent state directory
fn persistent_state_dir(user_id: &UserId) -> PathBuf {
    app_data_dir()
        .join("users")
        .join(user_id.to_string().replace(':', "_"))
}

/// Get app-wide data directory
fn app_data_dir() -> &'static Path {
    // Platform-specific app data location
    static APP_DATA_DIR: OnceLock<PathBuf> = OnceLock::new();
    APP_DATA_DIR.get_or_init(|| {
        dirs::data_dir()
            .unwrap_or_else(|| PathBuf::from("."))
            .join("myapp")
    })
}
```

### Saving State

```rust
use std::io::Write;

pub fn save_app_state(
    app_state: AppState,
    user_id: OwnedUserId,
) -> anyhow::Result<()> {
    let file = std::fs::File::create(
        persistent_state_dir(&user_id).join(LATEST_APP_STATE_FILE_NAME)
    )?;
    let mut writer = std::io::BufWriter::new(file);
    serde_json::to_writer(&mut writer, &app_state)?;
    writer.flush()?;
    log!("Successfully saved app state to persistent storage.");
    Ok(())
}

/// Save window geometry state (user-agnostic)
pub fn save_window_state(window_ref: WindowRef, cx: &Cx) -> anyhow::Result<()> {
    let inner_size = window_ref.get_inner_size(cx);
    let position = window_ref.get_position(cx);
    let window_geom = WindowGeomState {
        inner_size: (inner_size.x, inner_size.y),
        position: (position.x, position.y),
        is_fullscreen: window_ref.is_fullscreen(cx),
    };
    std::fs::write(
        app_data_dir().join(WINDOW_GEOM_STATE_FILE_NAME),
        serde_json::to_string(&window_geom)?,
    )?;
    Ok(())
}
```

### Loading State

```rust
/// Load app state with graceful fallback
pub async fn load_app_state(user_id: &UserId) -> anyhow::Result<AppState> {
    let state_path = persistent_state_dir(user_id).join(LATEST_APP_STATE_FILE_NAME);

    // Read file
    let file_bytes = match tokio::fs::read(&state_path).await {
        Ok(fb) => fb,
        Err(e) if e.kind() == std::io::ErrorKind::NotFound => {
            log!("No saved app state found, using default.");
            return Ok(AppState::default());
        }
        Err(e) => return Err(e.into()),
    };

    // Deserialize with fallback
    match serde_json::from_slice(&file_bytes) {
        Ok(app_state) => {
            log!("Successfully loaded app state.");
            Ok(app_state)
        }
        Err(e) => {
            error!("Failed to deserialize: {e}. May be incompatible format.");

            // Backup old file
            let backup_path = state_path.with_extension("json.bak");
            if let Err(backup_err) = tokio::fs::rename(&state_path, &backup_path).await {
                error!("Failed to backup old state: {}", backup_err);
            } else {
                log!("Old state backed up to: {:?}", backup_path);
            }

            log!("Using default app state.");
            Ok(AppState::default())
        }
    }
}

/// Load window geometry (synchronous, on UI thread)
pub fn load_window_state(window_ref: WindowRef, cx: &mut Cx) -> anyhow::Result<()> {
    let file = match std::fs::File::open(app_data_dir().join(WINDOW_GEOM_STATE_FILE_NAME)) {
        Ok(file) => file,
        Err(e) if e.kind() == std::io::ErrorKind::NotFound => return Ok(()),
        Err(e) => return Err(e.into()),
    };

    let window_geom: WindowGeomState = serde_json::from_reader(file)?;
    log!("Restoring window geometry: {window_geom:?}");

    window_ref.configure_window(
        cx,
        dvec2(window_geom.inner_size.0, window_geom.inner_size.1),
        dvec2(window_geom.position.0, window_geom.position.1),
        window_geom.is_fullscreen,
        "MyApp".to_string(),
    );
    Ok(())
}
```

### Startup/Shutdown Integration

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Load window geometry (sync, on UI thread)
        if let Err(e) = persistence::load_window_state(
            self.ui.window(ids!(main_window)), cx
        ) {
            error!("Failed to load window state: {}", e);
        }

        // Trigger async app state load
        let user_id = get_current_user_id();
        tokio::spawn(async move {
            match persistence::load_app_state(&user_id).await {
                Ok(app_state) => {
                    Cx::post_action(AppStateAction::RestoreFromPersistence(app_state));
                    SignalToUI::set_ui_signal();
                }
                Err(e) => error!("Failed to load app state: {}", e),
            }
        });
    }
}

impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        if let Event::Shutdown = event {
            // Save window state (sync)
            if let Err(e) = persistence::save_window_state(
                self.ui.window(ids!(main_window)), cx
            ) {
                error!("Failed to save window state: {e}");
            }

            // Save app state (sync)
            if let Some(user_id) = current_user_id() {
                if let Err(e) = persistence::save_app_state(
                    self.app_state.clone(), user_id
                ) {
                    error!("Failed to save app state: {e}");
                }
            }
        }
        // ...
    }
}
```

## Thread-Local State (UI-Only)

```rust
use std::{cell::RefCell, rc::Rc, collections::HashMap};

thread_local! {
    /// UI-thread-only cache
    static UI_CACHE: Rc<RefCell<HashMap<OwnedRoomId, CachedData>>> =
        Rc::new(RefCell::new(HashMap::new()));
}

/// Get cache reference (requires Cx to ensure UI thread)
pub fn get_ui_cache(_cx: &mut Cx) -> Rc<RefCell<HashMap<OwnedRoomId, CachedData>>> {
    UI_CACHE.with(Rc::clone)
}

/// Clear cache (requires Cx)
pub fn clear_ui_cache(_cx: &mut Cx) {
    UI_CACHE.with(|cache| cache.borrow_mut().clear());
}
```

## Best Practices

1. **Separate persistent vs runtime state**: Use `#[serde(skip)]` for non-persistent fields
2. **Use Scope::with_data() for tree propagation**: Don't pass state through widget refs
3. **Graceful deserialization fallback**: Handle format changes between versions
4. **Backup old state files**: Preserve user data when format changes
5. **User-specific persistent paths**: Separate state per user account
6. **Sync window state, async app state**: Window geometry loads sync on UI thread
7. **Thread-local for UI-only caches**: Use `thread_local!` with Cx parameter guard

## Reference Files

- `references/persistence-patterns.md` - Additional persistence patterns (Robrix)
- `references/state-structures.md` - State structure examples (Robrix)
- `references/moly-state-patterns.md` - Moly-specific patterns
  - Central Store struct containing all state
  - Async Store initialization with `load_into_app()`
  - App state check pattern (early return if not loaded)
  - Submodule state managers (Search, Downloads, Chats)
  - Provider syncing status tracking
  - Store action forwarding to submodules
```

## File: `skills/robius-state-management/_base/06-global-registry.md`
```markdown
---
name: makepad-global-registry
author: robius
source: robrix
date: 2024-01-01
tags: [global, registry, singleton, toast, notification]
level: intermediate
---

# Pattern 6: Global Widget Registry

Access widgets from anywhere in the app using `Cx::set_global`.

## Problem

You have app-wide widgets like toast notifications or tooltips that need to be triggered from deep in the widget tree.

## Solution

Use `Cx::set_global()` to register a widget reference, then access it from anywhere.

## Implementation

```rust
// In shared/popup.rs
pub fn set_global_popup(cx: &mut Cx, popup: PopupRef) {
    Cx::set_global(cx, popup);
}

pub fn get_global_popup(cx: &mut Cx) -> &mut PopupRef {
    cx.get_global::<PopupRef>()
}

pub fn show_notification(cx: &mut Cx, message: &str) {
    get_global_popup(cx).show(cx, message);
}

pub fn show_error(cx: &mut Cx, error: &str) {
    get_global_popup(cx).show_error(cx, error);
}
```

## Setup in App

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Register global widgets
        set_global_popup(cx, self.ui.popup(ids!(global_popup)));
        set_global_tooltip(cx, self.ui.tooltip(ids!(global_tooltip)));
    }
}
```

## live_design!

```rust
live_design! {
    App = {{App}} {
        ui: <Root> {
            main_window = <Window> {
                body = <View> {
                    // Your app content...

                    // Global popup (rendered on top)
                    global_popup = <ToastPopup> {}
                    global_tooltip = <Tooltip> {}
                }
            }
        }
    }
}
```

## Usage from Anywhere

```rust
// In any widget, any depth
impl Widget for DeepNestedWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if some_error_occurred {
            // Call global helper
            show_error(cx, "Something went wrong!");
        }

        if operation_succeeded {
            show_notification(cx, "Saved successfully!");
        }
    }
}
```

## When to Use

- Toast notifications
- Global tooltips
- Loading overlays
- Error displays
- Any UI that can be triggered from multiple places

## Caution

- Don't overuse - only for truly global UI elements
- Register in `handle_startup` before any usage
- Widget must exist in the view hierarchy
```

## File: `skills/robius-state-management/_base/07-radio-navigation.md`
```markdown
---
name: makepad-radio-navigation
author: robius
source: robrix
date: 2024-01-01
tags: [navigation, tabs, radio, sidebar]
level: beginner
---

# Pattern 7: Radio Button Navigation

Tab-style navigation using radio button sets.

## Problem

You need tab navigation where selecting one tab deselects others and shows the corresponding page.

## Solution

Use `radio_button_set()` to group radio buttons and handle selection changes.

## Implementation

```rust
impl MatchEvent for App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        let tabs = self.ui.radio_button_set(ids!(
            sidebar.home_tab,
            sidebar.settings_tab,
            sidebar.profile_tab
        ));

        if let Some(selected) = tabs.selected(cx, actions) {
            // Hide all pages
            self.ui.view(ids!(pages.home)).set_visible(cx, false);
            self.ui.view(ids!(pages.settings)).set_visible(cx, false);
            self.ui.view(ids!(pages.profile)).set_visible(cx, false);

            // Show selected page
            match selected {
                0 => self.ui.view(ids!(pages.home)).set_visible(cx, true),
                1 => self.ui.view(ids!(pages.settings)).set_visible(cx, true),
                2 => self.ui.view(ids!(pages.profile)).set_visible(cx, true),
                _ => {}
            }
        }
    }
}
```

## live_design!

```rust
live_design! {
    App = {{App}} {
        ui: <Root> {
            <Window> {
                body = <View> {
                    flow: Right

                    // Sidebar with tabs
                    sidebar = <View> {
                        width: 200, height: Fill
                        flow: Down

                        home_tab = <RadioButton> {
                            text: "Home"
                            animator: { selected = { default: on } }
                        }
                        settings_tab = <RadioButton> {
                            text: "Settings"
                        }
                        profile_tab = <RadioButton> {
                            text: "Profile"
                        }
                    }

                    // Page content
                    pages = <View> {
                        width: Fill, height: Fill
                        flow: Overlay

                        home = <HomeScreen> {}
                        settings = <SettingsScreen> { visible: false }
                        profile = <ProfileScreen> { visible: false }
                    }
                }
            }
        }
    }
}
```

## Alternative: PageFlip

For lazy-loaded pages, use `PageFlip`:

```rust
if let Some(selected) = tabs.selected(cx, actions) {
    let page_id = match selected {
        0 => ids!(home),
        1 => ids!(settings),
        2 => ids!(profile),
        _ => return,
    };
    self.ui.page_flip(ids!(pages)).set_active_page(cx, page_id);
}
```

## When to Use

- Main app navigation
- Settings tabs
- Dashboard sections
- Any mutually exclusive selection
```

## File: `skills/robius-state-management/_base/10-state-machine.md`
```markdown
---
name: makepad-state-machine
author: robius
source: moly
date: 2024-01-01
tags: [state-machine, lifecycle, enum, complex-state]
level: advanced
---

# Pattern 10: State Machine Widget

Manage complex widget lifecycle with enum states.

## Problem

Your widget has multiple states (idle, searching, showing results, error) with different behaviors and transitions. Using multiple boolean flags gets messy.

## Solution

Use an enum to represent all possible states, with each state containing its relevant data.

## Implementation

```rust
enum SearchState {
    Idle,
    Searching {
        query: String,
        receiver: mpsc::Receiver<SearchResult>,
        cancel_token: Arc<AtomicBool>,
    },
    ShowingResults(Vec<SearchResult>),
    Error(String),
}

#[derive(Live, Widget)]
pub struct SearchWidget {
    #[deref] view: View,
    #[rust] state: SearchState,
    #[rust] all_items: Vec<Item>,
}

impl Default for SearchState {
    fn default() -> Self {
        SearchState::Idle
    }
}

impl Widget for SearchWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        // State-specific event handling
        match &mut self.state {
            SearchState::Searching { receiver, .. } => {
                // Check for results
                while let Ok(result) = receiver.try_recv() {
                    // Collect results...
                }
            }
            _ => {}
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // State-specific drawing
        match &self.state {
            SearchState::Idle => {
                self.view.view(ids!(empty_state)).set_visible(cx, true);
                self.view.view(ids!(loading_state)).set_visible(cx, false);
                self.view.view(ids!(results_state)).set_visible(cx, false);
            }
            SearchState::Searching { .. } => {
                self.view.view(ids!(empty_state)).set_visible(cx, false);
                self.view.view(ids!(loading_state)).set_visible(cx, true);
                self.view.view(ids!(results_state)).set_visible(cx, false);
            }
            SearchState::ShowingResults(results) => {
                self.view.view(ids!(empty_state)).set_visible(cx, false);
                self.view.view(ids!(loading_state)).set_visible(cx, false);
                self.view.view(ids!(results_state)).set_visible(cx, true);
                // Render results...
            }
            SearchState::Error(msg) => {
                // Show error...
            }
        }

        self.view.draw_walk(cx, scope, walk)
    }
}

impl SearchWidget {
    fn start_search(&mut self, cx: &mut Cx, query: String) {
        // Cancel previous search if any
        if let SearchState::Searching { cancel_token, .. } = &self.state {
            cancel_token.store(true, Ordering::Relaxed);
        }

        let cancel = Arc::new(AtomicBool::new(false));
        let rx = spawn_search(query.clone(), self.all_items.clone(), cancel.clone());

        self.state = SearchState::Searching {
            query,
            receiver: rx,
            cancel_token: cancel,
        };
        self.redraw(cx);
    }

    fn show_results(&mut self, cx: &mut Cx, results: Vec<SearchResult>) {
        self.state = SearchState::ShowingResults(results);
        self.redraw(cx);
    }

    fn show_error(&mut self, cx: &mut Cx, error: String) {
        self.state = SearchState::Error(error);
        self.redraw(cx);
    }

    fn reset(&mut self, cx: &mut Cx) {
        if let SearchState::Searching { cancel_token, .. } = &self.state {
            cancel_token.store(true, Ordering::Relaxed);
        }
        self.state = SearchState::Idle;
        self.redraw(cx);
    }
}
```

## When to Use

- Widgets with complex lifecycles
- Multi-step wizards
- Connection states (connecting, connected, error)
- Media players (loading, playing, paused, ended)

## Benefits

- Compile-time state validation
- Clear state transitions
- State-specific data is scoped
- Easy to add new states
```

## File: `skills/robius-state-management/_base/11-theme-switching.md`
```markdown
---
name: makepad-theme-switching
author: robius
source: moly
date: 2024-01-01
tags: [theme, dark-mode, light-mode, colors, styling]
level: intermediate
---

# Pattern 11: Theme Switching

Multi-theme support with dynamic color application.

## Problem

Your app needs multiple themes (dark, light, custom) that users can switch between at runtime.

## Solution

Define theme colors as structs, store current theme, and use `apply_over()` to update widget colors.

## Implementation

```rust
#[derive(Clone, Copy, Debug, PartialEq, Default)]
pub enum Theme {
    #[default]
    Dark,
    Light,
    Cyberpunk,
}

struct ThemeColors {
    bg_primary: Vec4,
    bg_card: Vec4,
    accent: Vec4,
    text_primary: Vec4,
    text_secondary: Vec4,
}

impl Theme {
    fn next(&self) -> Theme {
        match self {
            Theme::Dark => Theme::Light,
            Theme::Light => Theme::Cyberpunk,
            Theme::Cyberpunk => Theme::Dark,
        }
    }

    fn colors(&self) -> ThemeColors {
        match self {
            Theme::Dark => ThemeColors {
                bg_primary: vec4(0.04, 0.04, 0.07, 1.0),
                bg_card: vec4(0.10, 0.10, 0.15, 1.0),
                accent: vec4(0.0, 1.0, 0.53, 1.0),
                text_primary: vec4(0.9, 0.9, 0.9, 1.0),
                text_secondary: vec4(0.5, 0.5, 0.5, 1.0),
            },
            Theme::Light => ThemeColors {
                bg_primary: vec4(0.96, 0.96, 0.98, 1.0),
                bg_card: vec4(1.0, 1.0, 1.0, 1.0),
                accent: vec4(0.2, 0.6, 0.86, 1.0),
                text_primary: vec4(0.1, 0.1, 0.1, 1.0),
                text_secondary: vec4(0.5, 0.5, 0.5, 1.0),
            },
            Theme::Cyberpunk => ThemeColors {
                bg_primary: vec4(0.08, 0.02, 0.12, 1.0),
                bg_card: vec4(0.15, 0.05, 0.2, 1.0),
                accent: vec4(1.0, 0.0, 0.6, 1.0),
                text_primary: vec4(0.95, 0.9, 1.0, 1.0),
                text_secondary: vec4(0.6, 0.5, 0.7, 1.0),
            },
        }
    }
}

#[derive(Live, LiveHook)]
pub struct App {
    #[live] ui: WidgetRef,
    #[rust] current_theme: Theme,
}

impl App {
    fn apply_theme(&mut self, cx: &mut Cx) {
        let colors = self.current_theme.colors();

        // Apply to various widgets
        self.ui.apply_over(cx, live!{
            draw_bg: { color: (colors.bg_primary) }
        });

        self.ui.view(ids!(card)).apply_over(cx, live!{
            draw_bg: { color: (colors.bg_card) }
        });

        self.ui.label(ids!(title)).apply_over(cx, live!{
            draw_text: { color: (colors.accent) }
        });

        self.ui.label(ids!(subtitle)).apply_over(cx, live!{
            draw_text: { color: (colors.text_secondary) }
        });

        self.ui.redraw(cx);
    }
}

impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        self.apply_theme(cx);
    }

    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        if self.ui.button(ids!(theme_btn)).clicked(&actions) {
            self.current_theme = self.current_theme.next();
            self.apply_theme(cx);
        }
    }
}
```

## Persistence

Save theme preference:

```rust
fn save_theme(&self) {
    let config_path = get_config_path();
    let _ = fs::write(&config_path, self.current_theme.to_string());
}

fn load_theme(&mut self) {
    let config_path = get_config_path();
    if let Ok(theme_str) = fs::read_to_string(&config_path) {
        self.current_theme = theme_str.parse().unwrap_or_default();
    }
}
```

## When to Use

- Dark/light mode toggle
- Brand customization
- Accessibility (high contrast)
- User personalization
```

## File: `skills/robius-state-management/_base/12-local-persistence.md`
```markdown
---
name: makepad-local-persistence
author: robius
source: moly
date: 2024-01-01
tags: [persistence, storage, config, preferences, save]
level: beginner
---

# Pattern 12: Local Data Persistence

Save and load user preferences and app state.

## Problem

You need to persist user settings, favorites, or app state between sessions.

## Solution

Use simple file I/O with JSON serialization for structured data.

## Basic Implementation (Text)

```rust
use std::fs;
use std::path::PathBuf;

fn get_config_path() -> PathBuf {
    let home = std::env::var("HOME").unwrap_or_else(|_| ".".to_string());
    PathBuf::from(home).join(".myapp_config.txt")
}

impl App {
    fn save_favorites(&self) {
        let path = get_config_path();
        let content = self.favorites.join("\n");
        let _ = fs::write(&path, content);
    }

    fn load_favorites(&mut self) {
        let path = get_config_path();
        if let Ok(content) = fs::read_to_string(&path) {
            self.favorites = content.lines()
                .map(|s| s.trim().to_string())
                .filter(|s| !s.is_empty())
                .collect();
        }
    }

    fn toggle_favorite(&mut self, item: &str) {
        if self.favorites.contains(&item.to_string()) {
            self.favorites.retain(|f| f != item);
        } else {
            self.favorites.push(item.to_string());
        }
        self.save_favorites();
    }
}
```

## JSON Implementation (Structured)

```rust
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Default)]
pub struct AppConfig {
    pub theme: String,
    pub favorites: Vec<String>,
    pub last_opened: Option<String>,
    pub window_size: Option<(u32, u32)>,
}

impl AppConfig {
    fn path() -> PathBuf {
        dirs::config_dir()
            .unwrap_or_else(|| PathBuf::from("."))
            .join("myapp")
            .join("config.json")
    }

    pub fn load() -> Self {
        let path = Self::path();
        if path.exists() {
            if let Ok(content) = fs::read_to_string(&path) {
                if let Ok(config) = serde_json::from_str(&content) {
                    return config;
                }
            }
        }
        Self::default()
    }

    pub fn save(&self) {
        let path = Self::path();
        if let Some(parent) = path.parent() {
            let _ = fs::create_dir_all(parent);
        }
        if let Ok(content) = serde_json::to_string_pretty(self) {
            let _ = fs::write(path, content);
        }
    }
}
```

## Usage

```rust
impl MatchEvent for App {
    fn handle_startup(&mut self, cx: &mut Cx) {
        // Load saved config
        self.config = AppConfig::load();
        self.apply_config(cx);
    }
}

impl App {
    fn apply_config(&mut self, cx: &mut Cx) {
        // Apply theme
        if let Ok(theme) = self.config.theme.parse() {
            self.current_theme = theme;
            self.apply_theme(cx);
        }

        // Apply window size if saved
        if let Some((w, h)) = self.config.window_size {
            // Set window size...
        }
    }

    fn on_window_resize(&mut self, width: u32, height: u32) {
        self.config.window_size = Some((width, height));
        self.config.save();
    }
}
```

## Cargo.toml

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
dirs = "5.0"  # For cross-platform config directories
```

## When to Use

- User preferences (theme, language)
- Favorites/bookmarks
- Recent items
- Window position/size
- Any state that should survive app restart

## Platform Paths

| Platform | `dirs::config_dir()` |
|----------|---------------------|
| Linux | `~/.config/` |
| macOS | `~/Library/Application Support/` |
| Windows | `C:\Users\<User>\AppData\Roaming\` |
```

## File: `skills/robius-state-management/references/moly-state-patterns.md`
```markdown
# Moly State Management Patterns

Additional state management patterns from Moly codebase.

## Central Store Pattern

Moly uses a central Store struct containing all application state:

```rust
pub struct Store {
    pub search: Search,
    pub downloads: Downloads,
    pub chats: Chats,
    pub preferences: Preferences,
    pub bot_context: Option<BotContext>,
    moly_client: MolyClient,
    pub provider_syncing_status: ProviderSyncingStatus,
    pub provider_icons: Vec<LiveDependency>,
}
```

## Async Store Initialization

Load store asynchronously, then inject into App:

```rust
use crate::app::app_runner;
use moly_kit::utils::asynchronous::spawn;

impl Store {
    pub fn load_into_app() {
        spawn(async move {
            // Load preferences first
            let preferences = Preferences::load().await;

            // Initialize client
            let server_port = std::env::var("MOLY_SERVER_PORT")
                .ok()
                .and_then(|p| p.parse::<u16>().ok())
                .unwrap_or(8765);

            let moly_client = MolyClient::new(format!("http://localhost:{}", server_port));

            // Load chats with client
            let chats = Chats::load(moly_client.clone()).await;

            // Build store
            let mut store = Self {
                search: Search::new(moly_client.clone()),
                downloads: Downloads::new(moly_client.clone()),
                chats,
                moly_client,
                preferences,
                bot_context: None,
                provider_syncing_status: ProviderSyncingStatus::NotSyncing,
                provider_icons: vec![],
            };

            // Initialize store
            store.init_current_chat();
            store.sync_with_server();
            store.load_preference_connections();

            // Inject into App via UiRunner
            app_runner().defer(move |app, cx, _| {
                app.store = Some(store);
                app.ui.view(id!(body)).set_visible(cx, true);
                cx.redraw_all();
            });
        })
    }
}
```

## App State Check Pattern

Check if store is loaded before processing:

```rust
impl AppMain for App {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {
        // Handle UiRunner callbacks
        self.ui_runner().handle(cx, event, &mut Scope::empty(), self);

        if let Event::Startup = event {
            self.ui.view(id!(body)).set_visible(cx, false);
            Store::load_into_app();
        }

        // If store not loaded, only handle Makepad events
        let Some(store) = self.store.as_mut() else {
            self.ui.handle_event(cx, event, &mut Scope::empty());
            return;
        };

        // Hide loading view once store is ready
        self.ui.view(id!(loading_view)).set_visible(cx, false);

        // Pass store through scope
        let scope = &mut Scope::with_data(store);
        self.ui.handle_event(cx, event, scope);
        self.match_event(cx, event);
    }
}
```

## Submodule State Management

Each domain has its own state manager:

```rust
// Search state
pub struct Search {
    client: MolyClient,
    pub featured_models: Vec<Model>,
    pub search_results: Vec<Model>,
    pub current_query: String,
}

impl Search {
    pub fn new(client: MolyClient) -> Self {
        Self {
            client,
            featured_models: vec![],
            search_results: vec![],
            current_query: String::new(),
        }
    }

    pub fn load_featured_models(&mut self) {
        let client = self.client.clone();
        spawn(async move {
            let models = client.get_featured_models().await;
            app_runner().defer(move |app, _, _| {
                let store = app.store.as_mut().unwrap();
                store.search.featured_models = models.unwrap_or_default();
            });
        });
    }

    pub fn handle_action(&mut self, action: &Action) {
        // Handle search-specific actions
    }
}

// Downloads state
pub struct Downloads {
    client: MolyClient,
    pub downloaded_files: Vec<File>,
    pub pending_downloads: Vec<PendingDownload>,
    pending_notifications: Vec<DownloadPendingNotification>,
}

impl Downloads {
    pub fn handle_action(&mut self, action: &Action) {
        // Handle download-specific actions
    }
}
```

## Provider Syncing Status

Track background sync state:

```rust
#[derive(Clone, Debug, PartialEq)]
pub enum ProviderSyncingStatus {
    NotSyncing,
    Syncing(ProviderSyncing),
    Synced,
}

#[derive(Clone, Debug, PartialEq)]
pub struct ProviderSyncing {
    pub current: u32,
    pub total: u32,
}

// In Store
pub fn sync_with_server(&mut self) {
    if !self.is_server_enabled() {
        return;
    }

    let client = self.moly_client.clone();
    spawn(async move {
        let Ok(()) = client.test_connection().await else {
            return;
        };

        app_runner().defer(|app, _, _| {
            let store = app.store.as_mut().unwrap();
            store.downloads.load_downloaded_files();
            store.downloads.load_pending_downloads();
            store.search.load_featured_models();
        });
    });
}
```

## Chat State Management

Chat state with current chat tracking:

```rust
pub struct Chats {
    client: MolyClient,
    chats: HashMap<ChatID, RefCell<Chat>>,
    current_chat_id: Option<ChatID>,
    pub providers: HashMap<String, Provider>,
}

impl Chats {
    pub fn set_current_chat(&mut self, chat_id: Option<ChatID>) {
        // Deselect previous
        if let Some(prev_id) = self.current_chat_id {
            if let Some(chat) = self.chats.get(&prev_id) {
                chat.borrow_mut().is_selected = false;
            }
        }

        // Select new
        if let Some(id) = chat_id {
            if let Some(chat) = self.chats.get(&id) {
                chat.borrow_mut().is_selected = true;
            }
        }

        self.current_chat_id = chat_id;
    }

    pub fn get_chat_by_id(&self, id: ChatID) -> Option<&RefCell<Chat>> {
        self.chats.get(&id)
    }

    pub fn get_last_selected_chat_id(&self) -> Option<ChatID> {
        self.current_chat_id
    }
}
```

## Preferences Persistence

Load/save user preferences:

```rust
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Preferences {
    pub providers_preferences: Vec<ProviderPreference>,
    pub last_selected_chat_id: Option<ChatID>,
    // ... other preferences
}

impl Preferences {
    pub async fn load() -> Self {
        let path = preferences_path();

        match tokio::fs::read_to_string(&path).await {
            Ok(json) => serde_json::from_str(&json).unwrap_or_default(),
            Err(e) if e.kind() == std::io::ErrorKind::NotFound => {
                Self::default()
            }
            Err(e) => {
                error!("Failed to load preferences: {}", e);
                Self::default()
            }
        }
    }

    pub fn save(&self) {
        let preferences = self.clone();
        spawn(async move {
            let json = serde_json::to_string_pretty(&preferences).unwrap();
            if let Err(e) = tokio::fs::write(preferences_path(), json).await {
                error!("Failed to save preferences: {}", e);
            }
        });
    }
}
```

## Store Action Forwarding

Forward actions to appropriate handlers:

```rust
impl Store {
    pub fn handle_action(&mut self, action: &Action) {
        // Forward to submodules
        self.search.handle_action(action);
        self.downloads.handle_action(action);

        // Handle download completion
        if action.downcast_ref::<DownloadFileAction>().is_some() {
            self.update_downloads();
        }
    }

    fn update_downloads(&mut self) {
        let completed_ids = self.downloads.refresh_downloads_data();

        // Refresh provider models if downloads completed
        if !completed_ids.is_empty() {
            if let Some(provider) = self.get_server_provider() {
                if provider.enabled {
                    self.chats.test_provider_and_fetch_models(
                        &provider.url,
                        &mut self.provider_syncing_status,
                    );
                }
            }
        }

        // Update search results with download state
        for file_id in completed_ids {
            self.search.update_downloaded_file_in_search_results(&file_id, true);
        }
    }
}
```
```

## File: `skills/robius-state-management/references/persistence-patterns.md`
```markdown
# Persistence Patterns Reference

Additional patterns for state persistence.

## Session Persistence

For client/auth sessions:

```rust
use matrix_sdk::Client;

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct ClientSessionPersisted {
    pub homeserver: String,
    pub db_path: PathBuf,
    pub passphrase: String,
}

/// Save client session after login
pub async fn save_session(
    client: &Client,
    session: ClientSessionPersisted,
) -> anyhow::Result<()> {
    let session_path = app_data_dir().join("session.json");
    let session_json = serde_json::to_string(&session)?;
    tokio::fs::write(&session_path, session_json).await?;
    log!("Session saved to {:?}", session_path);
    Ok(())
}

/// Try to restore existing session
pub async fn restore_session() -> anyhow::Result<Option<(Client, ClientSessionPersisted)>> {
    let session_path = app_data_dir().join("session.json");

    let session_json = match tokio::fs::read_to_string(&session_path).await {
        Ok(json) => json,
        Err(e) if e.kind() == std::io::ErrorKind::NotFound => {
            return Ok(None);
        }
        Err(e) => return Err(e.into()),
    };

    let session: ClientSessionPersisted = serde_json::from_str(&session_json)?;

    // Rebuild client from session
    let client = Client::builder()
        .homeserver_url(&session.homeserver)
        .sqlite_store(&session.db_path, Some(&session.passphrase))
        .build()
        .await?;

    Ok(Some((client, session)))
}
```

## Versioned State Migration

```rust
#[derive(Serialize, Deserialize)]
struct VersionedState {
    version: u32,
    data: serde_json::Value,
}

const CURRENT_VERSION: u32 = 2;

pub async fn load_with_migration(path: &Path) -> anyhow::Result<AppState> {
    let bytes = tokio::fs::read(path).await?;
    let versioned: VersionedState = serde_json::from_slice(&bytes)?;

    let migrated = match versioned.version {
        1 => migrate_v1_to_v2(versioned.data)?,
        2 => versioned.data,
        v => {
            error!("Unknown state version: {}", v);
            return Ok(AppState::default());
        }
    };

    Ok(serde_json::from_value(migrated)?)
}

fn migrate_v1_to_v2(v1_data: serde_json::Value) -> anyhow::Result<serde_json::Value> {
    // Transform v1 format to v2
    let mut data = v1_data;

    // Add new fields with defaults
    if let Some(obj) = data.as_object_mut() {
        obj.insert("new_field".to_string(), serde_json::json!([]));

        // Rename field
        if let Some(old_value) = obj.remove("old_field_name") {
            obj.insert("new_field_name".to_string(), old_value);
        }
    }

    Ok(data)
}

pub fn save_versioned(path: &Path, state: &AppState) -> anyhow::Result<()> {
    let versioned = VersionedState {
        version: CURRENT_VERSION,
        data: serde_json::to_value(state)?,
    };
    let json = serde_json::to_string_pretty(&versioned)?;
    std::fs::write(path, json)?;
    Ok(())
}
```

## Atomic Saves

```rust
use std::fs;
use tempfile::NamedTempFile;

/// Atomic save to prevent corruption on crash
pub fn save_atomic(path: &Path, data: &impl Serialize) -> anyhow::Result<()> {
    let dir = path.parent().ok_or_else(|| anyhow!("Invalid path"))?;

    // Write to temp file in same directory
    let temp_file = NamedTempFile::new_in(dir)?;
    serde_json::to_writer(&temp_file, data)?;

    // Atomic rename
    temp_file.persist(path)?;

    Ok(())
}
```

## Lazy State Loading

```rust
use std::sync::OnceLock;

static HEAVY_STATE: OnceLock<HeavyState> = OnceLock::new();

pub fn get_heavy_state() -> &'static HeavyState {
    HEAVY_STATE.get_or_init(|| {
        // Load expensive state only when first needed
        load_heavy_state_sync().unwrap_or_default()
    })
}

// Alternative: Async lazy loading
pub async fn get_or_load_state(
    cache: &RwLock<Option<CachedState>>,
) -> Arc<CachedState> {
    // Try read lock first
    {
        let guard = cache.read().await;
        if let Some(ref state) = *guard {
            return Arc::new(state.clone());
        }
    }

    // Need to load - upgrade to write lock
    let mut guard = cache.write().await;

    // Double-check after acquiring write lock
    if let Some(ref state) = *guard {
        return Arc::new(state.clone());
    }

    // Actually load
    let state = load_state_from_disk().await.unwrap_or_default();
    *guard = Some(state.clone());
    Arc::new(state)
}
```

## Cache with TTL

```rust
use std::time::{Duration, Instant};

pub struct TimestampedCache<T> {
    data: Option<T>,
    last_updated: Option<Instant>,
    ttl: Duration,
}

impl<T> TimestampedCache<T> {
    pub fn new(ttl: Duration) -> Self {
        Self {
            data: None,
            last_updated: None,
            ttl,
        }
    }

    pub fn get(&self) -> Option<&T> {
        let last_updated = self.last_updated?;
        if last_updated.elapsed() > self.ttl {
            return None;  // Expired
        }
        self.data.as_ref()
    }

    pub fn set(&mut self, data: T) {
        self.data = Some(data);
        self.last_updated = Some(Instant::now());
    }

    pub fn invalidate(&mut self) {
        self.data = None;
        self.last_updated = None;
    }
}
```

## Cleanup on Logout

```rust
pub async fn clear_user_data(user_id: &UserId) -> anyhow::Result<()> {
    let user_dir = persistent_state_dir(user_id);

    // Remove user-specific files
    if user_dir.exists() {
        tokio::fs::remove_dir_all(&user_dir).await?;
    }

    Ok(())
}

pub fn clear_all_caches(cx: &mut Cx) {
    // Clear all UI-thread caches
    clear_ui_cache(cx);
    clear_avatar_cache(cx);
    clear_profile_cache(cx);

    // Clear async caches
    GLOBAL_CACHE.lock().unwrap().clear();
}
```
```

## File: `skills/robius-state-management/references/state-structures.md`
```markdown
# State Structures Reference

Common state structure patterns from Robrix.

## Window Geometry State

```rust
#[derive(Default, Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct WindowGeomState {
    /// Window width and height
    pub inner_size: (f64, f64),
    /// Window x and y position
    pub position: (f64, f64),
    /// Whether window is maximized/fullscreen
    pub is_fullscreen: bool,
}
```

## Room/Item Info Structures

```rust
/// UI-related info about a joined room
#[derive(Debug)]
pub struct JoinedRoomInfo {
    /// Displayable name (includes room ID for fallback)
    pub room_name_id: RoomNameId,
    /// Number of unread messages
    pub num_unread_messages: u64,
    /// Number of unread mentions
    pub num_unread_mentions: u64,
    /// Canonical alias for this room
    pub canonical_alias: Option<OwnedRoomAliasId>,
    /// Alternative aliases
    pub alt_aliases: Vec<OwnedRoomAliasId>,
    /// Room tags (favourite, low_priority, etc.)
    pub tags: Tags,
    /// Latest message timestamp and preview text
    pub latest: Option<(MilliSecondsSinceUnixEpoch, String)>,
    /// Room avatar (image bytes or first character)
    pub avatar: FetchedRoomAvatar,
    /// Whether room has been paginated at least once
    pub has_been_paginated: bool,
    /// Whether room is currently selected in UI
    pub is_selected: bool,
    /// Whether this is a direct message room
    pub is_direct: bool,
    /// Whether room is tombstoned (replaced by successor)
    pub is_tombstoned: bool,
}
```

## Invite State Machine

```rust
/// State of a pending invite
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub enum InviteState {
    /// Waiting for user to accept or decline
    #[default]
    WaitingOnUserInput,
    /// Waiting for server response to join
    WaitingForJoinResult,
    /// Waiting for server response to leave
    WaitingForLeaveResult,
    /// Invite accepted, waiting for room to appear
    WaitingForJoinedRoom,
    /// Invite declined, room was left
    RoomLeft,
}

/// Info about an invited room
pub struct InvitedRoomInfo {
    pub room_name_id: RoomNameId,
    pub canonical_alias: Option<OwnedRoomAliasId>,
    pub alt_aliases: Vec<OwnedRoomAliasId>,
    pub room_avatar: FetchedRoomAvatar,
    pub inviter_info: Option<InviterInfo>,
    pub latest: Option<(MilliSecondsSinceUnixEpoch, String)>,
    pub invite_state: InviteState,
    pub is_selected: bool,
    pub is_direct: bool,
}
```

## User Profile State

```rust
#[derive(Clone, Debug)]
pub struct UserProfile {
    pub user_id: OwnedUserId,
    pub username: Option<String>,
    pub avatar_state: AvatarState,
}

#[derive(Clone, Debug)]
pub enum AvatarState {
    /// Avatar URL unknown yet
    Unknown,
    /// Avatar URL known (None = no avatar set)
    Known(Option<OwnedMxcUri>),
    /// Avatar image data loaded
    Loaded(Arc<[u8]>),
    /// Failed to load avatar
    Failed,
}

/// Profile with room context
#[derive(Clone, Debug)]
pub struct UserProfileAndRoomId {
    pub user_profile: UserProfile,
    pub room_id: OwnedRoomId,
}
```

## Filter/Display State

```rust
/// Active display filter for a list
pub struct RoomDisplayFilter {
    /// Filter function
    filter_fn: Box<dyn Fn(&RoomInfo) -> bool>,
    /// Sort function
    sort_fn: SortFn,
    /// Filter keywords
    keywords: String,
}

/// Filter criteria configuration
pub struct RoomFilterCriteria {
    pub include_direct: bool,
    pub include_regular: bool,
    pub include_invited: bool,
    pub space_filter: Option<OwnedRoomId>,
}
```

## Per-Widget State

```rust
/// State for the room input bar
#[derive(Default, Debug)]
pub struct RoomInputBarState {
    /// Currently composing message
    pub draft: String,
    /// Message being replied to
    pub reply_to: Option<ReplyInfo>,
    /// Message being edited
    pub editing: Option<EditInfo>,
    /// Typing indicator active
    pub is_typing: bool,
}

/// State for timeline display
pub struct TimelineState {
    /// All timeline items
    pub items: Vector<Arc<TimelineItem>>,
    /// Items drawn in last frame (for caching)
    pub drawn_items: RangeSet<usize>,
    /// Scroll position
    pub scroll_offset: f64,
    /// Whether we've hit the start of timeline
    pub fully_paginated_back: bool,
    /// Whether we've hit the end (live) of timeline
    pub fully_paginated_forward: bool,
}
```

## Global Singleton Pattern

```rust
use std::sync::Mutex;

/// Global client singleton
static CLIENT: Mutex<Option<Client>> = Mutex::new(None);

pub fn get_client() -> Option<Client> {
    CLIENT.lock().unwrap().clone()
}

pub fn set_client(client: Client) {
    *CLIENT.lock().unwrap() = Some(client);
}

pub fn clear_client() {
    *CLIENT.lock().unwrap() = None;
}

/// Global user ID cache
static CURRENT_USER_ID: Mutex<Option<OwnedUserId>> = Mutex::new(None);

pub fn current_user_id() -> Option<OwnedUserId> {
    CURRENT_USER_ID.lock().unwrap().clone()
}
```

## Per-Item State Storage

```rust
use std::collections::HashMap;

/// Store per-room joined details
static ALL_JOINED_ROOMS: Mutex<HashMap<OwnedRoomId, JoinedRoomDetails>> =
    Mutex::new(HashMap::new());

struct JoinedRoomDetails {
    room_id: OwnedRoomId,
    timeline: Arc<Timeline>,
    update_sender: crossbeam_channel::Sender<TimelineUpdate>,
    subscriber_task: JoinHandle<()>,
    event_handlers: Option<EventHandlerDropGuard>,
}

impl Drop for JoinedRoomDetails {
    fn drop(&mut self) {
        // Cleanup when room is closed
        self.subscriber_task.abort();
        drop(self.event_handlers.take());
    }
}
```
```

## File: `skills/robius-widget-patterns/SKILL.md`
```markdown
---
name: robius-widget-patterns
description: |
  CRITICAL: Use for Robius widget patterns. Triggers on:
  apply_over, TextOrImage, modal, 可复用, 模态,
  collapsible, drag drop, reusable widget, widget design,
  pageflip, 组件设计, 组件模式
---

# Robius Widget Patterns Skill

Best practices for designing reusable Makepad widgets based on Robrix and Moly codebase patterns.

**Source codebases:**
- **Robrix**: Matrix chat client - Avatar, RoomsList, RoomScreen widgets
- **Moly**: AI chat application - Slot, ChatLine, PromptInput, AdaptiveView widgets

## Triggers

Use this skill when:
- Creating reusable Makepad widgets
- Designing widget component APIs
- Implementing text/image toggle patterns
- Dynamic styling in Makepad
- Keywords: robrix widget, makepad component, reusable widget, widget design pattern

## Production Patterns

For production-ready widget patterns, see the `_base/` directory:

| Pattern | Description |
|---------|-------------|
| [01-widget-extension](./_base/01-widget-extension.md) | Add helper methods to widget references |
| [02-modal-overlay](./_base/02-modal-overlay.md) | Popups, dialogs using DrawList2d overlay |
| [03-collapsible](./_base/03-collapsible.md) | Expandable/collapsible sections |
| [04-list-template](./_base/04-list-template.md) | Dynamic lists with LivePtr templates |
| [05-lru-view-cache](./_base/05-lru-view-cache.md) | Memory-efficient view caching |
| [14-callout-tooltip](./_base/14-callout-tooltip.md) | Tooltips with arrow positioning |
| [20-redraw-optimization](./_base/20-redraw-optimization.md) | Efficient redraw patterns |
| [15-dock-studio-layout](./_base/15-dock-studio-layout.md) | IDE-style resizable panels |
| [16-hover-effect](./_base/16-hover-effect.md) | Hover effects with instance variables |
| [17-row-based-grid-layout](./_base/17-row-based-grid-layout.md) | Dynamic grid layouts |
| [18-drag-drop-reorder](./_base/18-drag-drop-reorder.md) | Drag-and-drop widget reordering |
| [19-pageflip-optimization](./_base/19-pageflip-optimization.md) | PageFlip 切换优化，即刻销毁/缓存模式 |
| [21-collapsible-row-portal-list](./_base/21-collapsible-row-portal-list.md) | Auto-grouping consecutive items in portal lists with FoldHeader |
| [22-dropdown-overlay](./_base/22-dropdown-overlay.md) | Dropdown popups using DrawList2d overlay (no layout push) |

## Standard Widget Structure

```rust
use makepad_widgets::*;

live_design! {
    use link::theme::*;
    use link::widgets::*;

    pub MyWidget = {{MyWidget}} {
        width: Fill, height: Fit,
        flow: Down,

        // Child widgets defined in DSL
        inner_view = <View> {
            // ...
        }
    }
}

#[derive(Live, LiveHook, Widget)]
pub struct MyWidget {
    #[deref] view: View,              // Delegate to inner View

    #[live] some_property: f64,       // DSL-configurable property
    #[live(100.0)] default_val: f64,  // With default value

    #[rust] internal_state: State,    // Rust-only state (not in DSL)

    #[animator] animator: Animator,   // For animations
}

impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);
        // Custom event handling...
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.view.draw_walk(cx, scope, walk)
    }
}
```

## Text/Image Toggle Pattern

A common pattern for widgets that show either text or an image (like avatars):

```rust
live_design! {
    pub Avatar = {{Avatar}} {
        width: 36.0, height: 36.0,
        align: { x: 0.5, y: 0.5 }
        flow: Overlay,  // Stack views on top of each other

        text_view = <View> {
            visible: true,  // Default visible
            show_bg: true,
            draw_bg: {
                uniform background_color: #888888
                fn pixel(self) -> vec4 {
                    let sdf = Sdf2d::viewport(self.pos * self.rect_size);
                    let c = self.rect_size * 0.5;
                    sdf.circle(c.x, c.x, c.x)
                    sdf.fill_keep(self.background_color);
                    return sdf.result
                }
            }
            text = <Label> {
                text: "?"
            }
        }

        img_view = <View> {
            visible: false,  // Hidden by default
            img = <Image> {
                fit: Stretch,
                width: Fill, height: Fill,
            }
        }
    }
}

#[derive(LiveHook, Live, Widget)]
pub struct Avatar {
    #[deref] view: View,
    #[rust] info: Option<UserInfo>,
}

impl Avatar {
    /// Show text content, hiding the image
    pub fn show_text<T: AsRef<str>>(
        &mut self,
        cx: &mut Cx,
        bg_color: Option<Vec4>,
        info: Option<AvatarTextInfo>,
        username: T,
    ) {
        self.info = info.map(|i| i.into());

        // Get first character
        let first_char = utils::first_letter(username.as_ref())
            .unwrap_or("?").to_uppercase();
        self.label(ids!(text_view.text)).set_text(cx, &first_char);

        // Toggle visibility
        self.view(ids!(text_view)).set_visible(cx, true);
        self.view(ids!(img_view)).set_visible(cx, false);

        // Apply optional background color
        if let Some(color) = bg_color {
            self.view(ids!(text_view)).apply_over(cx, live! {
                draw_bg: { background_color: (color) }
            });
        }
    }

    /// Show image content, hiding the text
    pub fn show_image<F, E>(
        &mut self,
        cx: &mut Cx,
        info: Option<AvatarImageInfo>,
        image_set_fn: F,
    ) -> Result<(), E>
    where
        F: FnOnce(&mut Cx, ImageRef) -> Result<(), E>
    {
        let img_ref = self.image(ids!(img_view.img));
        let res = image_set_fn(cx, img_ref);

        if res.is_ok() {
            self.view(ids!(img_view)).set_visible(cx, true);
            self.view(ids!(text_view)).set_visible(cx, false);
            self.info = info.map(|i| i.into());
        }
        res
    }

    /// Check current display status
    pub fn status(&mut self) -> DisplayStatus {
        if self.view(ids!(img_view)).visible() {
            DisplayStatus::Image
        } else {
            DisplayStatus::Text
        }
    }
}
```

## Dynamic Styling with apply_over

Apply dynamic styles at runtime:

```rust
// Apply single property
self.view(ids!(content)).apply_over(cx, live! {
    draw_bg: { color: #ff0000 }
});

// Apply multiple properties
self.view(ids!(message)).apply_over(cx, live! {
    padding: { left: 20, right: 20 }
    margin: { top: 10 }
});

// Apply with variables
let highlight_color = if is_selected { vec4(1.0, 0.0, 0.0, 1.0) } else { vec4(0.5, 0.5, 0.5, 1.0) };
self.view(ids!(item)).apply_over(cx, live! {
    draw_bg: { color: (highlight_color) }
});
```

## Widget Reference Pattern

Implement `*Ref` methods for external API:

```rust
impl AvatarRef {
    /// See [`Avatar::show_text()`].
    pub fn show_text<T: AsRef<str>>(
        &self,
        cx: &mut Cx,
        bg_color: Option<Vec4>,
        info: Option<AvatarTextInfo>,
        username: T,
    ) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.show_text(cx, bg_color, info, username);
        }
    }

    /// See [`Avatar::show_image()`].
    pub fn show_image<F, E>(
        &self,
        cx: &mut Cx,
        info: Option<AvatarImageInfo>,
        image_set_fn: F,
    ) -> Result<(), E>
    where
        F: FnOnce(&mut Cx, ImageRef) -> Result<(), E>
    {
        if let Some(mut inner) = self.borrow_mut() {
            inner.show_image(cx, info, image_set_fn)
        } else {
            Ok(())
        }
    }
}
```

## Collapsible/Expandable Pattern

```rust
live_design! {
    pub CollapsibleSection = {{CollapsibleSection}} {
        flow: Down,

        header = <View> {
            cursor: Hand,
            icon = <Icon> { }
            title = <Label> { text: "Section" }
        }

        content = <View> {
            visible: false,
            // Expandable content here
        }
    }
}

#[derive(Live, LiveHook, Widget)]
pub struct CollapsibleSection {
    #[deref] view: View,
    #[rust] is_expanded: bool,
}

impl CollapsibleSection {
    pub fn toggle(&mut self, cx: &mut Cx) {
        self.is_expanded = !self.is_expanded;
        self.view(ids!(content)).set_visible(cx, self.is_expanded);

        // Rotate icon
        let rotation = if self.is_expanded { 90.0 } else { 0.0 };
        self.view(ids!(header.icon)).apply_over(cx, live! {
            draw_icon: { rotation: (rotation) }
        });

        self.redraw(cx);
    }
}
```

## Loading State Pattern

```rust
live_design! {
    pub LoadableContent = {{LoadableContent}} {
        flow: Overlay,

        content = <View> {
            visible: true,
            // Main content
        }

        loading_overlay = <View> {
            visible: false,
            show_bg: true,
            draw_bg: { color: #00000088 }
            align: { x: 0.5, y: 0.5 }
            <BouncingDots> { }
        }

        error_view = <View> {
            visible: false,
            error_label = <Label> { }
        }
    }
}

#[derive(Live, LiveHook, Widget)]
pub struct LoadableContent {
    #[deref] view: View,
    #[rust] state: LoadingState,
}

pub enum LoadingState {
    Idle,
    Loading,
    Loaded,
    Error(String),
}

impl LoadableContent {
    pub fn set_state(&mut self, cx: &mut Cx, state: LoadingState) {
        self.state = state;
        match &self.state {
            LoadingState::Idle | LoadingState::Loaded => {
                self.view(ids!(content)).set_visible(cx, true);
                self.view(ids!(loading_overlay)).set_visible(cx, false);
                self.view(ids!(error_view)).set_visible(cx, false);
            }
            LoadingState::Loading => {
                self.view(ids!(content)).set_visible(cx, true);
                self.view(ids!(loading_overlay)).set_visible(cx, true);
                self.view(ids!(error_view)).set_visible(cx, false);
            }
            LoadingState::Error(msg) => {
                self.view(ids!(content)).set_visible(cx, false);
                self.view(ids!(loading_overlay)).set_visible(cx, false);
                self.view(ids!(error_view)).set_visible(cx, true);
                self.label(ids!(error_view.error_label)).set_text(cx, msg);
            }
        }
        self.redraw(cx);
    }
}
```

## PortalList Item Pattern

For virtual list items:

```rust
live_design! {
    pub ItemsList = {{ItemsList}} {
        list = <PortalList> {
            keep_invisible: false,
            auto_tail: false,
            width: Fill, height: Fill,
            flow: Down,

            // Item templates
            item_entry = <ItemEntry> {}
            header = <SectionHeader> {}
            empty = <View> {}
        }
    }
}

impl Widget for ItemsList {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        while let Some(item) = self.view.draw_walk(cx, scope, walk).step() {
            if let Some(mut list) = item.as_portal_list().borrow_mut() {
                list.set_item_range(cx, 0, self.items.len());

                while let Some(item_id) = list.next_visible_item(cx) {
                    let item = list.item(cx, item_id, live_id!(item_entry));
                    // Populate item with data
                    self.populate_item(cx, item, &self.items[item_id]);
                    item.draw_all(cx, scope);
                }
            }
        }
        DrawStep::done()
    }
}
```

## Best Practices

1. **Use `#[deref]` for delegation**: Delegate to inner View for standard behavior
2. **Separate DSL properties (`#[live]`) from Rust state (`#[rust]`)**
3. **Implement both inner methods and `*Ref` wrappers**
4. **Use `apply_over` for dynamic runtime styling**
5. **Use `flow: Overlay` for toggle/swap patterns**
6. **Use `set_visible()` to toggle between alternative views**
7. **Always call `redraw(cx)` after state changes**

## Reference Files

- `references/widget-patterns.md` - Additional widget patterns (Robrix)
- `references/styling-patterns.md` - Dynamic styling patterns (Robrix)
- `references/moly-widget-patterns.md` - Moly-specific patterns
  - `Slot` widget for runtime content replacement
  - `MolyRoot` conditional rendering wrapper
  - `AdaptiveView` for responsive Mobile/Desktop layouts
  - Chat line variants (UserLine, BotLine, ErrorLine, etc.)
  - `CommandTextInput` with action buttons
  - Sidebar navigation with radio buttons
```

## File: `skills/robius-widget-patterns/_base/01-widget-extension.md`
```markdown
---
name: makepad-widget-extension
author: robius
source: robrix
date: 2024-01-01
tags: [widget, extension, trait, helper]
level: intermediate
---

# Pattern 1: Widget Reference Extension

Add helper methods to widget references without modifying the widget itself.

## Problem

You want to add convenience methods like `set_user()` to a widget reference, but you don't own the widget code.

## Solution

Use Rust extension traits on the widget's `Ref` type.

## Implementation

```rust
pub trait AvatarWidgetRefExt {
    fn set_user(&self, cx: &mut Cx, user: &UserInfo);
    fn show_placeholder(&self, cx: &mut Cx);
}

impl AvatarWidgetRefExt for AvatarRef {
    fn set_user(&self, cx: &mut Cx, user: &UserInfo) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.user_info = Some(user.clone());
            inner.view.label(ids!(name)).set_text(cx, &user.name);
            inner.redraw(cx);
        }
    }

    fn show_placeholder(&self, cx: &mut Cx) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.user_info = None;
            inner.view.label(ids!(name)).set_text(cx, "?");
            inner.redraw(cx);
        }
    }
}
```

## Usage

```rust
// Now you can call extension methods on any AvatarRef
self.ui.avatar(ids!(user_avatar)).set_user(cx, &user_info);
```

## When to Use

- Adding domain-specific helpers to generic widgets
- Encapsulating common widget update patterns
- Creating fluent APIs for your app's widgets
```

## File: `skills/robius-widget-patterns/_base/02-modal-overlay.md`
```markdown
---
name: makepad-modal-overlay
author: robius
source: robrix
date: 2024-01-01
tags: [modal, overlay, popup, dialog, dropdown]
level: intermediate
---

# Pattern 2: Modal/Overlay Widget

Renders content above all other UI using `DrawList2d`.

## Problem

You need popups, dialogs, or dropdowns that render on top of everything else and can be dismissed by clicking outside.

## Solution

Use `DrawList2d::begin_overlay_reuse()` to render content in overlay layer.

## Implementation

```rust
#[derive(Live, Widget)]
pub struct Modal {
    #[live] content: View,
    #[live] draw_bg: DrawQuad,
    #[rust(DrawList2d::new(cx))] draw_list: DrawList2d,
    #[rust] opened: bool,
}

impl Widget for Modal {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        if !self.opened {
            return DrawStep::done();
        }

        // Begin overlay rendering
        self.draw_list.begin_overlay_reuse(cx);

        cx.begin_pass_sized_turtle(Layout::flow_down());
        self.draw_bg.draw_walk(cx, Walk::fill());
        self.content.draw_all(cx, scope);
        cx.end_pass_sized_turtle();

        self.draw_list.end(cx);
        DrawStep::done()
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if !self.opened { return; }

        cx.sweep_unlock(self.draw_bg.area());
        self.content.handle_event(cx, event, scope);
        cx.sweep_lock(self.draw_bg.area());

        // Click outside to dismiss
        match event.hits(cx, self.draw_bg.area()) {
            Hit::FingerDown(fe) => {
                let content_rect = self.content.area().rect(cx);
                if !content_rect.contains(fe.abs) {
                    self.close(cx);
                    cx.widget_action(self.widget_uid(), &scope.path,
                        ModalAction::Dismissed);
                }
            }
            _ => {}
        }
    }
}

impl ModalRef {
    pub fn open(&self, cx: &mut Cx) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.opened = true;
            inner.redraw(cx);
        }
    }

    pub fn close(&self, cx: &mut Cx) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.opened = false;
            inner.redraw(cx);
        }
    }
}
```

## Usage

```rust
// Open modal
self.ui.modal(ids!(confirm_dialog)).open(cx);

// Close modal
self.ui.modal(ids!(confirm_dialog)).close(cx);

// Handle dismissal
for action in actions {
    if let ModalAction::Dismissed = action.as_widget_action().cast() {
        // User clicked outside
    }
}
```

## When to Use

- Confirmation dialogs
- Dropdown menus
- Image lightboxes
- Context menus
```

## File: `skills/robius-widget-patterns/_base/03-collapsible.md`
```markdown
---
name: makepad-collapsible
author: robius
source: robrix
date: 2024-01-01
tags: [collapsible, expandable, accordion, toggle]
level: intermediate
---

# Pattern 3: Collapsible Widget

Toggle visibility of content with animation.

## Problem

You need expandable/collapsible sections like accordions, expandable cards, or tree nodes.

## Solution

Use animator states to control visibility and rotation of indicator icons.

## Implementation

```rust
#[derive(Clone, Debug, DefaultNone)]
pub enum CollapsibleAction {
    Toggled { now_expanded: bool },
    None,
}

#[derive(Live, LiveHook, Widget)]
pub struct CollapsibleHeader {
    #[deref] view: View,
    #[animator] animator: Animator,
    #[rust] is_expanded: bool,
}

impl Widget for CollapsibleHeader {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        if self.animator_handle_event(cx, event).must_redraw() {
            self.redraw(cx);
        }

        self.view.handle_event(cx, event, scope);

        match event.hits(cx, self.view.area()) {
            Hit::FingerDown(_) => {
                self.is_expanded = !self.is_expanded;

                if self.is_expanded {
                    self.animator_play(cx, ids!(expand.on));
                } else {
                    self.animator_play(cx, ids!(expand.off));
                }

                cx.widget_action(self.widget_uid(), &scope.path,
                    CollapsibleAction::Toggled { now_expanded: self.is_expanded });
            }
            _ => {}
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Rotate arrow icon based on state
        let rotation = if self.is_expanded { 180.0_f64.to_radians() } else { 0.0 };
        self.view.icon(ids!(arrow)).apply_over(cx, live! {
            draw_icon: { rotation_angle: (rotation) }
        });

        self.view.draw_walk(cx, scope, walk)
    }
}
```

## live_design!

```rust
live_design! {
    CollapsibleSection = <View> {
        flow: Down

        header = <CollapsibleHeader> {
            width: Fill, height: 48
            padding: { left: 16, right: 16 }
            align: { y: 0.5 }

            <Label> { text: "Section Title" }
            <Filler> {}
            arrow = <Icon> {
                draw_icon: { svg_file: dep("crate://self/icons/chevron-down.svg") }
            }
        }

        body = <View> {
            visible: false
            padding: 16

            <Label> { text: "Expandable content here" }
        }
    }
}
```

## Usage

```rust
// Handle toggle in parent
for action in actions {
    if let CollapsibleAction::Toggled { now_expanded } = action.as_widget_action().cast() {
        self.ui.view(ids!(body)).set_visible(cx, now_expanded);
    }
}
```

## When to Use

- FAQ sections
- Settings categories
- File tree nodes
- Accordion menus
```

## File: `skills/robius-widget-patterns/_base/04-list-template.md`
```markdown
---
name: makepad-list-template
author: robius
source: robrix
date: 2024-01-01
tags: [list, template, dynamic, data-driven]
level: intermediate
---

# Pattern 4: List with Template

Dynamic list from data using a template widget.

## Problem

You need to render a list of items where the number of items is determined at runtime, and each item follows the same template.

## Solution

Use `LivePtr` to store a template reference and `WidgetRef::new_from_ptr()` to instantiate items.

## Implementation

```rust
#[derive(Live, Widget)]
pub struct ItemList {
    #[deref] view: View,
    #[live] item_template: Option<LivePtr>,
    #[rust] items: Vec<ItemData>,
    #[rust] item_widgets: Vec<WidgetRef>,
}

impl Widget for ItemList {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Ensure we have enough widgets
        while self.item_widgets.len() < self.items.len() {
            let widget = WidgetRef::new_from_ptr(cx, self.item_template);
            self.item_widgets.push(widget);
        }

        cx.begin_turtle(walk, self.layout);

        for (i, item) in self.items.iter().enumerate() {
            let widget = &self.item_widgets[i];

            // Populate widget with data
            widget.label(ids!(title)).set_text(cx, &item.title);
            widget.label(ids!(subtitle)).set_text(cx, &item.subtitle);

            widget.draw_all(cx, scope);
        }

        cx.end_turtle();
        DrawStep::done()
    }
}

impl ItemListRef {
    pub fn set_items(&self, cx: &mut Cx, items: Vec<ItemData>) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.items = items;
            inner.redraw(cx);
        }
    }
}
```

## live_design!

```rust
live_design! {
    ItemList = {{ItemList}} {
        flow: Down
        spacing: 8

        item_template: <ListItem> {
            width: Fill, height: 64
            padding: 12

            title = <Label> { text: "" }
            subtitle = <Label> {
                draw_text: { color: #888 }
                text: ""
            }
        }
    }
}
```

## Usage

```rust
// Set data
let items = vec![
    ItemData { title: "Item 1".into(), subtitle: "Description 1".into() },
    ItemData { title: "Item 2".into(), subtitle: "Description 2".into() },
];
self.ui.item_list(ids!(my_list)).set_items(cx, items);
```

## When to Use

- Contact lists
- Message threads
- Product catalogs
- Search results
```

## File: `skills/robius-widget-patterns/_base/05-lru-view-cache.md`
```markdown
---
name: makepad-lru-view-cache
author: robius
source: moly
date: 2024-01-01
tags: [cache, lru, memory, view, performance]
level: advanced
---

# Pattern 5: LRU Cache for Views

Keep only N views in memory for memory-constrained applications.

## Problem

Your app has many screens/views (e.g., chat rooms), but keeping all of them in memory is expensive. You want to cache recently used views and evict old ones.

## Solution

Use `HashMap` with `VecDeque` access order tracking to implement LRU eviction.

## Implementation

```rust
use std::collections::{HashMap, VecDeque};

const MAX_CACHED_VIEWS: usize = 10;

#[derive(Live, Widget)]
pub struct ViewDeck {
    #[deref] view: View,
    #[live] view_template: Option<LivePtr>,
    #[rust] view_refs: HashMap<ViewId, WidgetRef>,
    #[rust] access_order: VecDeque<ViewId>,
    #[rust] current_view: Option<ViewId>,
}

impl ViewDeck {
    fn get_or_create_view(&mut self, cx: &mut Cx, id: ViewId) -> &WidgetRef {
        if !self.view_refs.contains_key(&id) {
            // Create new view
            let widget = WidgetRef::new_from_ptr(cx, self.view_template);
            self.view_refs.insert(id.clone(), widget);

            // Evict oldest if over limit
            if self.view_refs.len() > MAX_CACHED_VIEWS {
                if let Some(oldest) = self.access_order.pop_front() {
                    self.view_refs.remove(&oldest);
                }
            }
        }

        // Update access order (move to back = most recent)
        self.access_order.retain(|x| x != &id);
        self.access_order.push_back(id.clone());

        self.view_refs.get(&id).unwrap()
    }

    pub fn switch_to(&mut self, cx: &mut Cx, id: ViewId) {
        self.get_or_create_view(cx, id.clone());
        self.current_view = Some(id);
        self.redraw(cx);
    }
}

impl Widget for ViewDeck {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        if let Some(id) = &self.current_view {
            if let Some(view) = self.view_refs.get(id) {
                return view.draw_walk(cx, scope, walk);
            }
        }
        DrawStep::done()
    }
}
```

## Usage

```rust
// Switch to a room view (auto-creates if needed, evicts old if full)
self.ui.view_deck(ids!(chat_deck)).switch_to(cx, room_id);
```

## When to Use

- Chat applications with many rooms
- Tab systems with heavy content
- Image galleries
- Any app where views are expensive to keep in memory

## Configuration

Adjust `MAX_CACHED_VIEWS` based on:
- Memory constraints of target platform
- Complexity of each view
- User behavior (how often they switch)
```

## File: `skills/robius-widget-patterns/_base/14-callout-tooltip.md`
```markdown
---
name: makepad-callout-tooltip
author: robius
source: robrix
date: 2024-01-01
tags: [tooltip, callout, popup, hover, sdf, overlay]
level: advanced
---

# Pattern 14: Callout Tooltip

Tooltip with arrow/triangle pointing at the referenced widget, with automatic edge detection and position adjustment.

## Problem

You need tooltips that:
- Visually connect to their target element with an arrow
- Automatically adjust position when near screen edges
- Can be triggered from any widget without tight coupling
- Support all four directions (top/bottom/left/right)

## Solution

Use a global tooltip widget with:
1. Action-based event system for decoupled show/hide
2. SDF shader for drawing the callout triangle
3. Position calculation with edge detection
4. Instance variables for dynamic arrow positioning

## Implementation

### Data Types

```rust
use makepad_widgets::*;

/// The location of the tooltip with respect to its target widget.
#[derive(Clone, Debug, Default, PartialEq, Eq)]
pub enum TooltipPosition {
    Top,
    Bottom,
    Left,
    #[default]
    Right,
}

/// Options that affect how a CalloutTooltip is displayed.
#[derive(Clone, Debug)]
pub struct CalloutTooltipOptions {
    pub text_color: Vec4,
    pub bg_color: Vec4,
    pub position: TooltipPosition,
    pub triangle_height: f64,
}

impl Default for CalloutTooltipOptions {
    fn default() -> Self {
        Self {
            text_color: vec4(1.0, 1.0, 1.0, 1.0),      // White text
            bg_color: vec4(0.26, 0.30, 0.33, 1.0),     // Dark gray bg
            position: TooltipPosition::Right,
            triangle_height: 7.5,
        }
    }
}

/// Actions emitted to show/hide the tooltip from anywhere.
#[derive(Clone, Debug, DefaultNone)]
pub enum TooltipAction {
    HoverIn {
        text: String,
        widget_rect: Rect,
        options: CalloutTooltipOptions,
    },
    HoverOut,
    None,
}
```

### Position Calculation (Key Algorithm)

```rust
struct PositionCalculation {
    tooltip_pos: DVec2,
    callout_angle: f64,
}

impl CalloutTooltip {
    /// Calculate tooltip position with edge detection and fallback.
    fn calculate_position(
        options: &CalloutTooltipOptions,
        widget_rect: Rect,
        tooltip_size: DVec2,
        screen_size: DVec2,
        triangle_height: f64,
    ) -> PositionCalculation {
        let target_pos = widget_rect.pos;
        let target_size = widget_rect.size;
        let mut tooltip_pos = DVec2::default();
        let mut callout_angle = 0.0;

        match options.position {
            TooltipPosition::Top => {
                // Position above target
                tooltip_pos.x = target_pos.x + (target_size.x - tooltip_size.x) * 0.5;
                tooltip_pos.y = target_pos.y - tooltip_size.y - triangle_height;
                callout_angle = 180.0;  // Arrow points down

                // Flip to bottom if would go off top
                if tooltip_pos.y < 0.0 {
                    tooltip_pos.y = target_pos.y + target_size.y + triangle_height;
                    callout_angle = 0.0;
                }
            }
            TooltipPosition::Bottom => {
                // Position below target
                tooltip_pos.x = target_pos.x + (target_size.x - tooltip_size.x) * 0.5;
                tooltip_pos.y = target_pos.y + target_size.y + triangle_height;
                callout_angle = 0.0;  // Arrow points up

                // Flip to top if would go off bottom
                if tooltip_pos.y + tooltip_size.y > screen_size.y {
                    tooltip_pos.y = target_pos.y - tooltip_size.y - triangle_height;
                    callout_angle = 180.0;
                }
            }
            TooltipPosition::Left => {
                // Position to left of target
                tooltip_pos.x = target_pos.x - tooltip_size.x - triangle_height;
                tooltip_pos.y = target_pos.y + (target_size.y - tooltip_size.y) * 0.5;
                callout_angle = 90.0;  // Arrow points right

                // Flip to right if would go off left
                if tooltip_pos.x < 0.0 {
                    tooltip_pos.x = target_pos.x + target_size.x + triangle_height;
                    callout_angle = 270.0;
                }
            }
            TooltipPosition::Right => {
                // Position to right of target
                tooltip_pos.x = target_pos.x + target_size.x + triangle_height;
                tooltip_pos.y = target_pos.y + (target_size.y - tooltip_size.y) * 0.5;
                callout_angle = 270.0;  // Arrow points left

                // Flip to left if would go off right
                if tooltip_pos.x + tooltip_size.x > screen_size.x {
                    tooltip_pos.x = target_pos.x - tooltip_size.x - triangle_height;
                    callout_angle = 90.0;
                }
            }
        }

        // Clamp horizontal position to screen bounds
        tooltip_pos.x = tooltip_pos.x.max(0.0).min(screen_size.x - tooltip_size.x);
        // Clamp vertical position to screen bounds
        tooltip_pos.y = tooltip_pos.y.max(0.0).min(screen_size.y - tooltip_size.y);

        PositionCalculation { tooltip_pos, callout_angle }
    }
}
```

### Widget Implementation

```rust
#[derive(Live, LiveHook, Widget)]
pub struct CalloutTooltip {
    #[deref] view: View,
}

impl CalloutTooltip {
    pub fn show_with_options(
        &mut self,
        cx: &mut Cx,
        text: &str,
        widget_rect: Rect,
        options: CalloutTooltipOptions,
    ) {
        let mut tooltip = self.view.tooltip(ids!(tooltip));
        tooltip.set_text(cx, text);

        // Get tooltip dimensions after setting text
        let tooltip_size = tooltip.view(ids!(rounded_view)).area().rect(cx).size;
        let screen_size = tooltip.area().rect(cx).size;

        let calc = Self::calculate_position(
            &options,
            widget_rect,
            tooltip_size,
            screen_size,
            options.triangle_height,
        );

        // Apply shader instance variables
        tooltip.apply_over(cx, live! {
            content: {
                rounded_view = {
                    draw_bg: {
                        background_color: (options.bg_color)
                        triangle_height: (options.triangle_height)
                        callout_position: (calc.callout_angle)
                        tooltip_pos: (calc.tooltip_pos)
                        target_pos: (widget_rect.pos)
                        target_size: (widget_rect.size)
                        expected_dimension_x: (tooltip_size.x)
                    }
                    tooltip_label = {
                        draw_text: { color: (options.text_color) }
                    }
                }
            }
        });

        tooltip.show(cx);
    }

    pub fn show(&mut self, cx: &mut Cx) {
        self.view.tooltip(ids!(tooltip)).show(cx);
    }

    pub fn hide(&mut self, cx: &mut Cx) {
        self.view.tooltip(ids!(tooltip)).hide(cx);
    }
}
```

## live_design! (Complete Shader)

```rust
live_design! {
    use link::theme::*;
    use link::widgets::*;

    CalloutTooltipInner = <Tooltip> {
        content: <View> {
            flow: Overlay,
            width: Fit,
            height: Fit,

            rounded_view = <RoundedView> {
                width: Fit,
                height: Fit,
                padding: 15,

                draw_bg: {
                    color: #fff,
                    border_radius: 2.,

                    // Instance variables for dynamic positioning
                    instance background_color: #3b444b
                    instance tooltip_pos: vec2(0.0, 0.0)
                    instance target_pos: vec2(0.0, 0.0)
                    instance target_size: vec2(0.0, 0.0)
                    instance expected_dimension_x: 0.0
                    instance triangle_height: 7.5
                    instance callout_position: 180.0  // 0=Up, 90=Right, 180=Down, 270=Left

                    fn pixel(self) -> vec4 {
                        let sdf = Sdf2d::viewport(self.pos * self.rect_size);
                        let rect_size = self.rect_size;
                        let h = self.triangle_height;

                        // Don't draw until we have dimensions
                        if self.expected_dimension_x == 0.0 {
                            return sdf.result;
                        }

                        // Draw rounded box with padding for triangle
                        sdf.box(
                            h,
                            h,
                            rect_size.x - h * 2.0,
                            rect_size.y - h * 2.0,
                            max(1.0, self.border_radius)
                        );
                        sdf.fill(self.background_color);

                        // Calculate triangle vertices based on direction
                        let mut v1 = vec2(0.0, 0.0);
                        let mut v2 = vec2(0.0, 0.0);
                        let mut v3 = vec2(0.0, 0.0);

                        if self.callout_position == 0.0 {
                            // Arrow points UP (tooltip below target)
                            let center_x = self.target_pos.x + self.target_size.x * 0.5
                                         - self.tooltip_pos.x;
                            let clamped_x = min(
                                max(h * 3.0 + 2.0, center_x),
                                rect_size.x - h * 3.0 - 2.0
                            );
                            v1 = vec2(clamped_x, h + 2.0);
                            v2 = vec2(v1.x - h, 2.0);
                            v3 = vec2(v1.x + h, 2.0);
                        }
                        else if self.callout_position == 90.0 {
                            // Arrow points RIGHT (tooltip left of target)
                            v1 = vec2(rect_size.x - 2.0, rect_size.y * 0.5);
                            v2 = vec2(v1.x - h, v1.y - h);
                            v3 = vec2(v1.x - h, v1.y + h);
                        }
                        else if self.callout_position == 180.0 {
                            // Arrow points DOWN (tooltip above target)
                            let center_x = self.target_pos.x + self.target_size.x * 0.5
                                         - self.tooltip_pos.x + h;
                            let clamped_x = min(
                                max(h * 3.0 + 2.0, center_x),
                                rect_size.x - h - 2.0
                            );
                            v1 = vec2(clamped_x, rect_size.y - h - 2.0);
                            v2 = vec2(v1.x - h, rect_size.y - 2.0);
                            v3 = vec2(v1.x - h * 2.0, rect_size.y - h - 2.0);
                        }
                        else {
                            // Arrow points LEFT (tooltip right of target) - 270
                            v1 = vec2(2.0, rect_size.y * 0.5);
                            v2 = vec2(v1.x + h, v1.y - h);
                            v3 = vec2(v1.x + h, v1.y + h);
                        }

                        // Draw the triangle
                        sdf.move_to(v1.x, v1.y);
                        sdf.line_to(v2.x, v2.y);
                        sdf.line_to(v3.x, v3.y);
                        sdf.close_path();
                        sdf.fill(self.background_color);

                        return sdf.result;
                    }
                }

                tooltip_label = <Label> {
                    width: Fit,
                    height: Fit,
                    draw_text: {
                        text_style: <THEME_FONT_REGULAR>{ font_size: 9 },
                        text_wrap: Line,
                        color: #fff,
                    }
                }
            }
        }
    }

    // Public widget definition
    pub CalloutTooltip = {{CalloutTooltip}} {
        width: Fill,
        height: Fill,

        tooltip = <CalloutTooltipInner> {}
    }
}
```

## Integration in App (Action Handler)

```rust
// In app.rs or main widget handle_event
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    // ... other event handling ...

    // Handle tooltip actions from any widget
    for action in cx.actions() {
        match action.as_widget_action().cast() {
            TooltipAction::HoverIn { text, widget_rect, options } => {
                self.ui.callout_tooltip(ids!(app_tooltip))
                    .show_with_options(cx, &text, widget_rect, options);
            }
            TooltipAction::HoverOut => {
                self.ui.callout_tooltip(ids!(app_tooltip)).hide(cx);
            }
            _ => {}
        }
    }
}
```

## Usage (Emit from Any Widget)

```rust
impl Widget for MyButton {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        match event.hits(cx, self.draw_bg.area()) {
            Hit::FingerHoverIn(_) | Hit::FingerHoverOver(_) => {
                // Emit action to show tooltip
                cx.widget_action(
                    self.widget_uid(),
                    &scope.path,
                    TooltipAction::HoverIn {
                        text: "Button description".to_string(),
                        widget_rect: self.draw_bg.area().rect(cx),
                        options: CalloutTooltipOptions {
                            position: TooltipPosition::Top,
                            ..Default::default()
                        },
                    },
                );
            }
            Hit::FingerHoverOut(_) => {
                cx.widget_action(
                    self.widget_uid(),
                    &scope.path,
                    TooltipAction::HoverOut,
                );
            }
            _ => {}
        }
    }
}
```

## App Layout

```rust
live_design! {
    App = {{App}} {
        ui: <Root> {
            main_content = <View> {
                // Your app content here
            }

            // Global tooltip - always on top due to declaration order
            app_tooltip = <CalloutTooltip> {}
        }
    }
}
```

## Key Techniques

### 1. Dynamic Arrow Positioning
The arrow automatically points to the target's center:
```rust
let center_x = self.target_pos.x + self.target_size.x * 0.5 - self.tooltip_pos.x;
```

### 2. Edge Detection & Fallback
When tooltip would go off-screen, it flips to the opposite side:
```rust
if tooltip_pos.y < 0.0 {
    tooltip_pos.y = target_pos.y + target_size.y + triangle_height;
    callout_angle = 0.0;  // Flip direction
}
```

### 3. Triangle Padding
The box is inset by `triangle_height` to leave room for the arrow:
```rust
sdf.box(h, h, rect_size.x - h*2.0, rect_size.y - h*2.0, radius);
```

### 4. Decoupled Event System
Any widget can trigger tooltips via actions without direct references:
```rust
cx.widget_action(uid, &path, TooltipAction::HoverIn { ... });
```

## When to Use

- User guidance and feature explanations
- Hover information for icons
- Error/warning details
- Reaction/emoji explanations
- Read receipts or status indicators

## When NOT to Use

- For persistent information (use labels)
- For interactive content (use popups/modals)
- For very long text (use expandable sections)
```

## File: `skills/robius-widget-patterns/_base/15-dock-studio-layout.md`
```markdown
# Pattern 15: Dock-Based Studio Layout

<!-- Evolution: 2025-01-12 | source: flex-layout-demo | author: dorobot -->

Create IDE/studio-style layouts with resizable panels using Makepad's Dock and Splitter widgets.

## Overview

This pattern creates a professional studio layout with:
- Fixed header
- Resizable left sidebar, main content, right sidebar
- Resizable footer/timeline area
- Nested splitters for complex layouts

## live_design!

```rust
live_design! {
    use link::theme::*;
    use link::shaders::*;
    use link::widgets::*;

    // Panel components
    LeftSidebar = <View> {
        width: Fill, height: Fill
        flow: Down
        show_bg: true
        draw_bg: { color: #80a0d0 }
        // Sidebar content...
    }

    RightSidebar = <View> {
        width: Fill, height: Fill
        flow: Down
        show_bg: true
        draw_bg: { color: #a0a0c0 }
        // Sidebar content...
    }

    ContentArea = <View> {
        width: Fill, height: Fill
        show_bg: true
        draw_bg: { color: #e8e8f0 }
        // Main content...
    }

    StudioHeader = <View> {
        width: Fill, height: 48
        show_bg: true
        draw_bg: { color: #4080c0 }
        padding: { left: 16, right: 16 }
        flow: Right
        align: { y: 0.5 }

        <Label> { text: "Studio Title" }
    }

    StudioFooter = <View> {
        width: Fill, height: Fill
        show_bg: true
        draw_bg: { color: #60a060 }
        padding: 12

        <Label> { text: "Footer / Timeline" }
    }

    // Main layout using Dock with nested Splitters
    StudioLayout = {{StudioLayout}} {
        width: Fill, height: Fill
        flow: Down

        // Fixed header (not in Dock)
        <StudioHeader> {}

        // Resizable areas using Dock
        <Dock> {
            width: Fill, height: Fill

            // Root: vertical splitter for footer
            root = Splitter {
                axis: Vertical
                align: FromB(100.0)  // Footer starts at 100px from bottom
                a: main_area
                b: footer_panel
            }

            // Main area: horizontal splitter for left sidebar
            main_area = Splitter {
                axis: Horizontal
                align: FromA(280.0)  // Left sidebar 280px from left
                a: left_panel
                b: right_area
            }

            // Right area: horizontal splitter for right sidebar
            right_area = Splitter {
                axis: Horizontal
                align: FromB(300.0)  // Right sidebar 300px from right
                a: center_panel
                b: right_panel
            }

            // Tab wrappers for each panel
            left_panel = Tab { name: "", kind: left_sidebar }
            center_panel = Tab { name: "", kind: center_content }
            right_panel = Tab { name: "", kind: right_sidebar }
            footer_panel = Tab { name: "", kind: footer_content }

            // Actual content widgets
            left_sidebar = <LeftSidebar> {}
            center_content = <ContentArea> {}
            right_sidebar = <RightSidebar> {}
            footer_content = <StudioFooter> {}
        }
    }

    App = {{App}} {
        ui: <Root> {
            main_window = <Window> {
                window: { title: "Studio Layout", inner_size: vec2(1400, 900) }
                body = <StudioLayout> {}
            }
        }
    }
}
```

## Dock Structure

The Dock widget creates a tree of splitters:

```
root (Vertical Splitter)
├── main_area (Horizontal Splitter)
│   ├── left_panel (Tab → LeftSidebar)
│   └── right_area (Horizontal Splitter)
│       ├── center_panel (Tab → ContentArea)
│       └── right_panel (Tab → RightSidebar)
└── footer_panel (Tab → StudioFooter)
```

## Splitter Alignment

| Alignment | Meaning |
|-----------|---------|
| `FromA(px)` | Panel A has fixed size from start |
| `FromB(px)` | Panel B has fixed size from end |
| `Weighted(0.5)` | 50/50 split (0.0 to 1.0) |

## Rust Implementation

```rust
#[derive(Live, LiveHook, Widget)]
pub struct StudioLayout {
    #[deref]
    view: View,
}

impl Widget for StudioLayout {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.view.draw_walk(cx, scope, walk)
    }
}
```

## Alternative: Simple Splitter (Without Dock)

For simpler layouts without Tab support:

```rust
live_design! {
    // Nested Splitters directly
    CenterRightSplit = <Splitter> {
        width: Fill, height: Fill
        axis: Horizontal
        align: FromB(300.0)

        a = <ContentArea> {}
        b = <RightSidebar> {}
    }

    MiddleSplit = <Splitter> {
        width: Fill, height: Fill
        axis: Horizontal
        align: FromA(280.0)

        a = <LeftSidebar> {}
        b = <CenterRightSplit> {}
    }

    // Main layout
    SimpleStudioLayout = <View> {
        width: Fill, height: Fill
        flow: Down

        <StudioHeader> {}

        <Splitter> {
            width: Fill, height: Fill
            axis: Vertical
            align: FromB(100.0)

            a = <MiddleSplit> {}
            b = <StudioFooter> {}
        }
    }
}
```

## When to Use

| Scenario | Recommendation |
|----------|----------------|
| IDE/editor layout | Use Dock (supports tabs) |
| Simple 2-3 panel split | Use nested Splitters |
| Fixed panels (no resize) | Use View with fixed sizes |

## References

- [Makepad Studio](https://github.com/makepad/makepad/tree/main/studio) - Production example
- [Dock widget source](https://github.com/makepad/makepad/blob/main/widgets/src/dock.rs)
- [Splitter widget source](https://github.com/makepad/makepad/blob/main/widgets/src/splitter.rs)
```

## File: `skills/robius-widget-patterns/_base/16-hover-effect.md`
```markdown
# Pattern 16: Hover Effect with Instance Variables

<!-- Evolution: 2025-01-13 | source: mofa-studio | author: hover-effect-fix -->

Implement reliable hover effects on custom View widgets using shader instance variables.

## Problem

Direct color changes via `apply_over` don't work on RoundedView or View templates. When you try to change background colors dynamically for hover/selected states, the visual doesn't update even though the code executes.

## Solution

Use a custom shader with `instance` variables instead of direct color properties. This pattern is used by Makepad's built-in widgets like SectionHeader.

## live_design!

```rust
live_design! {
    use link::theme::*;
    use link::widgets::*;

    // Custom item with hover/selected effects
    HoverableItem = <View> {
        width: Fill, height: Fit
        padding: {left: 16, right: 16, top: 12, bottom: 12}
        show_bg: true
        cursor: Hand
        flow: Right
        align: {x: 0.0, y: 0.5}

        draw_bg: {
            // Instance variables - can be updated via apply_over
            instance hover: 0.0
            instance selected: 0.0
            instance dark_mode: 0.0

            fn pixel(self) -> vec4 {
                // Light mode colors
                let light_normal = (WHITE);
                let light_hover = #DAE6F9;     // Light blue hover
                let light_selected = #DBEAFE;   // Blue selected

                // Dark mode colors
                let dark_normal = (SLATE_800);
                let dark_hover = #334155;       // Slate-700
                let dark_selected = #1E3A5F;    // Blue-ish selected

                // Pick colors based on dark mode
                let normal = mix(light_normal, dark_normal, self.dark_mode);
                let hover_color = mix(light_hover, dark_hover, self.dark_mode);
                let selected_color = mix(light_selected, dark_selected, self.dark_mode);

                // Calculate final color: selected takes priority, then hover
                let base = mix(normal, hover_color, self.hover);
                return mix(base, selected_color, self.selected);
            }
        }

        // Child widgets go here
        item_label = <Label> {
            width: Fill
            draw_text: {
                text_style: <FONT_REGULAR>{ font_size: 12.0 }
                color: #383A40
            }
            text: "Item"
        }
    }
}
```

## Rust Implementation

```rust
impl Widget for MyWidget {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        // Define item paths
        let items = [
            ids!(item_1),
            ids!(item_2),
            ids!(item_3),
        ];

        // Handle hover for each item
        for (i, path) in items.iter().enumerate() {
            let item = self.view.view(*path);
            let area = item.area();

            match event.hits(cx, area) {
                Hit::FingerHoverIn(_) => {
                    // Check if this item is selected
                    let is_selected = self.selected_index == Some(i);
                    if !is_selected {
                        // Apply hover effect via instance variable
                        self.view.view(*path).apply_over(cx, live!{
                            draw_bg: { hover: 1.0 }
                        });
                        self.view.redraw(cx);
                    }
                }
                Hit::FingerHoverOut(_) => {
                    let is_selected = self.selected_index == Some(i);
                    if !is_selected {
                        // Remove hover effect
                        self.view.view(*path).apply_over(cx, live!{
                            draw_bg: { hover: 0.0 }
                        });
                        self.view.redraw(cx);
                    }
                }
                _ => {}
            }
        }
    }
}
```

## Selection Handling

```rust
impl MyWidget {
    fn select_item(&mut self, cx: &mut Cx, index: usize) {
        let items = [ids!(item_1), ids!(item_2), ids!(item_3)];

        // Reset all items
        for path in &items {
            self.view.view(*path).apply_over(cx, live!{
                draw_bg: { selected: 0.0, hover: 0.0 }
            });
        }

        // Apply selection to chosen item
        if index < items.len() {
            self.view.view(items[index]).apply_over(cx, live!{
                draw_bg: { selected: 1.0 }
            });
        }

        self.selected_index = Some(index);
        self.view.redraw(cx);
    }
}
```

## Dark Mode Support

```rust
impl MyWidgetRef {
    pub fn update_dark_mode(&self, cx: &mut Cx, dark_mode: f64) {
        if let Some(mut inner) = self.borrow_mut() {
            let items = [ids!(item_1), ids!(item_2), ids!(item_3)];

            for path in &items {
                inner.view.view(*path).apply_over(cx, live!{
                    draw_bg: { dark_mode: (dark_mode) }
                });
            }

            inner.view.redraw(cx);
        }
    }
}
```

## Key Points

1. **Use `<View>` not `<RoundedView>`** - Custom shaders work better with base View
2. **Instance variables** - Declare with `instance name: default_value`
3. **mix() function** - Use for smooth interpolation between states
4. **Priority order** - Selected should override hover (check order in shader)
5. **Always redraw** - Call `redraw(cx)` after `apply_over`

## Why This Works

- Instance variables are per-draw-call GPU values
- `apply_over` with instance variables directly updates shader uniforms
- Direct `color` property changes don't propagate to the GPU correctly on templates
- This matches how Makepad's built-in widgets handle hover states

## Common Mistakes

```rust
// WRONG - direct color won't update visually
self.view.view(path).apply_over(cx, live!{
    draw_bg: { color: #ff0000 }  // ❌ No effect
});

// CORRECT - instance variable updates work
self.view.view(path).apply_over(cx, live!{
    draw_bg: { hover: 1.0 }  // ✅ Works
});
```

## References

- [Troubleshooting: apply_over Color Not Working](troubleshooting.md#apply_over-color-not-working-on-roundedviewview-templates)
- [Theme Switching Pattern](./_base/11-theme-switching.md)
```

## File: `skills/robius-widget-patterns/_base/17-row-based-grid-layout.md`
```markdown
# Pattern 17: Row-Based Grid Layout

<!-- Evolution: 2025-01-12 | source: flex-layout-demo | author: dorobot -->

Create dynamic grid layouts where different rows can have different numbers of columns, each filling their row equally.

## Problem

Using `RightWrap` flow with calculated pixel widths doesn't work reliably for layouts where:
- Row 1: 3 windows each filling 1/3 width
- Row 2: 2 windows each filling 1/2 width

`RightWrap` wraps items based on available width, not respecting intended row structure. Calculated pixel sizes often have measurement timing issues.

## Solution

Use **explicit row containers** with `Fill` sizing:
1. Container uses `flow: Down` to stack rows vertically
2. Each row uses `flow: Right` with `height: Fill`
3. Windows use `width: Fill, height: Fill` to auto-distribute within their row
4. Control layout by showing/hiding windows and setting size to 0 for hidden ones

## Key Insight

**`set_visible(false)` alone doesn't collapse space** when a widget has `width: Fill`. You must also set `width: 0, height: 0` to truly collapse hidden widgets.

## live_design!

```rust
live_design! {
    use link::theme::*;
    use link::widgets::*;

    GridContainer = {{GridContainer}} {
        width: Fill
        height: Fill

        // Container with explicit row structure
        window_container = <View> {
            width: Fill
            height: Fill
            flow: Down  // Stack rows vertically

            // Row 1: up to 3 windows
            row1 = <View> {
                width: Fill
                height: Fill
                flow: Right  // Distribute windows horizontally

                w1 = <SubWindow> { width: Fill, height: Fill }
                w2 = <SubWindow> { width: Fill, height: Fill }
                w3 = <SubWindow> { width: Fill, height: Fill }
            }

            // Row 2: up to 3 windows
            row2 = <View> {
                width: Fill
                height: Fill
                flow: Right

                w4 = <SubWindow> { width: Fill, height: Fill }
                w5 = <SubWindow> { width: Fill, height: Fill }
                w6 = <SubWindow> { width: Fill, height: Fill }
            }

            // Row 3: up to 3 windows
            row3 = <View> {
                width: Fill
                height: Fill
                flow: Right

                w7 = <SubWindow> { width: Fill, height: Fill }
                w8 = <SubWindow> { width: Fill, height: Fill }
                w9 = <SubWindow> { width: Fill, height: Fill }
            }
        }
    }
}
```

## Rust Implementation

```rust
impl GridContainer {
    /// Fixed layout mapping: window_count -> windows per row
    fn get_layout_config(&self, window_count: usize) -> Vec<usize> {
        match window_count {
            0 => vec![],
            1 => vec![1],           // 1 row: 1
            2 => vec![1, 1],        // 2 rows: 1+1
            3 => vec![2, 1],        // 2 rows: 2+1
            4 => vec![2, 2],        // 2 rows: 2+2
            5 => vec![3, 2],        // 2 rows: 3+2
            6 => vec![3, 3],        // 2 rows: 3+3
            7 => vec![3, 3, 1],     // 3 rows: 3+3+1
            8 => vec![3, 3, 2],     // 3 rows: 3+3+2
            9 => vec![3, 3, 3],     // 3 rows: 3+3+3
            _ => vec![3, 3, 3],
        }
    }

    fn apply_row_layout(&mut self, cx: &mut Cx) {
        let visible_windows = self.collect_visible_windows();
        let window_count = visible_windows.len();

        let row1_ids = [
            id!(window_container.row1.w1),
            id!(window_container.row1.w2),
            id!(window_container.row1.w3),
        ];
        let row2_ids = [
            id!(window_container.row2.w4),
            id!(window_container.row2.w5),
            id!(window_container.row2.w6),
        ];
        let row3_ids = [
            id!(window_container.row3.w7),
            id!(window_container.row3.w8),
            id!(window_container.row3.w9),
        ];
        let all_rows = [&row1_ids[..], &row2_ids[..], &row3_ids[..]];

        let row_config = self.get_layout_config(window_count);
        let num_rows = row_config.len();

        // CRITICAL: Collapse all windows first (set size to 0, not just visibility)
        for row_ids in &all_rows {
            for win_id in *row_ids {
                self.view.view(*win_id).apply_over(cx, live! {
                    visible: false
                    width: 0
                    height: 0
                });
            }
        }

        // Show/hide rows (must also set height to 0 for hidden rows)
        if num_rows >= 1 {
            self.view.view(id!(window_container.row1))
                .apply_over(cx, live! { visible: true, height: Fill });
        } else {
            self.view.view(id!(window_container.row1))
                .apply_over(cx, live! { visible: false, height: 0 });
        }
        // ... repeat for row2, row3

        // Assign windows to slots based on config
        let mut window_idx = 0;
        for (row, &cols_in_row) in row_config.iter().enumerate() {
            if row >= 3 { break; }

            for col in 0..3 {
                let win_id = all_rows[row][col];
                if col < cols_in_row && window_idx < visible_windows.len() {
                    // Show this slot with Fill sizing
                    self.view.view(win_id).apply_over(cx, live! {
                        visible: true
                        width: Fill
                        height: Fill
                    });
                    window_idx += 1;
                }
                // Hidden windows already collapsed above
            }
        }
    }
}
```

## Why This Works

| Approach | Problem |
|----------|---------|
| RightWrap + pixel widths | Wraps based on container width, not row structure |
| set_visible(false) only | Widget still occupies space with `width: Fill` |
| **Row containers + Fill** | Makepad auto-distributes Fill equally within each row |

## Critical Points

1. **Collapse hidden widgets completely**: Set both `visible: false` AND `width: 0, height: 0`
2. **Collapse hidden rows too**: Hidden rows with `height: Fill` still take space
3. **Use Fill for auto-distribution**: Don't calculate pixel sizes - let Makepad handle it
4. **Apply layout in draw_walk**: Call `apply_row_layout` when `needs_layout_update` is true

## When to Use

- Sub-window layouts in IDE/studio apps
- Dashboard tiles with variable columns per row
- Any grid where rows have different numbers of items
- Re-layouting when items are added/removed

## References

- [flex-layout-demo](examples/flex-layout-demo) - Working implementation
- [Dock-Based Studio Layout](./_base/15-dock-studio-layout.md) - Overall studio structure
```

## File: `skills/robius-widget-patterns/_base/18-drag-drop-reorder.md`
```markdown
# Pattern 18: Drag-and-Drop Widget Reordering

<!-- Evolution: 2025-01-13 | source: flex-layout-demo | author: dorobot -->

Implement drag-and-drop reordering of widgets with visual preview and physical layout changes.

## Problem

Need to allow users to drag widgets between containers (e.g., moving windows between rows) with:
- Visual feedback during drag (drop preview)
- Physical layout changes (rows resize based on content)
- Proper event handling that works across widget boundaries

## Solution

Use a combination of:
1. **Per-row assignment tracking** instead of flat ordering
2. **`hits_with_capture_overload`** to capture events during drag
3. **Deferred visual updates** via `needs_visual_update` flag
4. **Dynamic slot assignment** where each row has excess slots

## Key Insight

**`hits_with_capture_overload(cx, area, true)`** allows a widget to receive mouse events even when the cursor moves outside its original hit area - essential for drag operations that cross widget boundaries.

## live_design!

```rust
live_design! {
    use link::theme::*;
    use link::widgets::*;

    // Draggable item with drag handle
    DraggableItem = {{DraggableItem}} {
        width: Fill
        height: Fill

        flow: Down

        title_bar = <View> {
            width: Fill
            height: 28
            flow: Right
            align: { y: 0.5 }

            // Drag handle - 6 dots pattern
            drag_handle = <View> {
                width: 16
                height: 20
                cursor: Hand
                // Draw dots in shader...
            }

            title = <Label> { text: "Item" }
        }

        content = <View> { /* content here */ }
    }

    // Container with drop preview support
    DragContainer = {{DragContainer}} {
        width: Fill
        height: Fill

        // Semi-transparent overlay for drop preview
        drop_preview: {
            draw_depth: 10.0
            color: #4080c080
        }

        // Rows with excess slots for flexibility
        container = <View> {
            flow: Down

            row1 = <View> {
                flow: Right
                s1_1 = <DraggableItem> {}
                s1_2 = <DraggableItem> {}
                s1_3 = <DraggableItem> {}
                // ... up to 9 slots per row
            }
            // ... more rows
        }
    }
}
```

## Rust Implementation

### Action Enum

```rust
/// Actions emitted during drag operations
#[derive(Clone, Debug, DefaultNone)]
pub enum DragAction {
    /// Drag started - emitted when threshold exceeded
    StartDrag(usize),  // item_id
    None,
}
```

### Draggable Item

```rust
#[derive(Live, LiveHook, Widget)]
pub struct DraggableItem {
    #[deref]
    view: View,

    #[rust]
    item_id: usize,

    #[rust]
    is_dragging: bool,

    #[rust]
    drag_start: DVec2,

    /// Deferred visual update flag
    #[rust]
    needs_visual_update: bool,
}

impl Widget for DraggableItem {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        let drag_handle = self.view.view(id!(title_bar.drag_handle));

        match event.hits(cx, drag_handle.area()) {
            Hit::FingerDown(fe) => {
                self.is_dragging = false;
                self.drag_start = fe.abs;
            }
            Hit::FingerMove(fe) => {
                // 10-pixel threshold prevents accidental drags
                let dist = (fe.abs - self.drag_start).length();
                if !self.is_dragging && dist > 10.0 {
                    self.is_dragging = true;
                    cx.widget_action(
                        self.widget_uid(),
                        &scope.path,
                        DragAction::StartDrag(self.item_id),
                    );
                }
            }
            Hit::FingerUp(_) => {
                self.is_dragging = false;
            }
            _ => {}
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Apply deferred visual updates in draw phase
        self.apply_visual_update(cx);
        self.view.draw_walk(cx, scope, walk)
    }
}

impl DraggableItem {
    pub fn set_item_id(&mut self, cx: &mut Cx, id: usize) {
        if self.item_id == id { return; }
        self.item_id = id;
        self.needs_visual_update = true;
        self.view.redraw(cx);
    }

    fn apply_visual_update(&mut self, cx: &mut Cx2d) {
        if !self.needs_visual_update { return; }
        self.needs_visual_update = false;

        // Apply visual changes based on item_id
        let colors = [/* distinct colors */];
        let color = colors[self.item_id % colors.len()];

        self.view.apply_over(cx, live! {
            draw_bg: { color: (color) }
        });

        self.view.label(id!(title_bar.title))
            .set_text(cx, &format!("Item {}", self.item_id + 1));
    }
}
```

### Container with Drop Handling

```rust
#[derive(Clone, Debug)]
struct DropPosition {
    row: usize,
    col: usize,
    rect: Rect,  // For visual preview
}

#[derive(Live, LiveHook, Widget)]
pub struct DragContainer {
    #[deref]
    view: View,

    #[live]
    drop_preview: DrawColor,

    /// Per-row item assignments (source of truth)
    #[rust]
    row_assignments: [Vec<usize>; 3],

    /// Currently dragging item ID
    #[rust]
    dragging_item: Option<usize>,

    /// Current drop target for preview
    #[rust]
    drop_state: Option<DropPosition>,

    #[rust]
    needs_layout_update: bool,
}

impl Widget for DragContainer {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        let actions = cx.capture_actions(|cx| {
            self.view.handle_event(cx, event, scope);
        });

        // Capture StartDrag actions from children
        for action in actions.iter() {
            if let DragAction::StartDrag(id) = action.as_widget_action().cast() {
                self.dragging_item = Some(id);
            }
        }

        // KEY: Use capture_overload to receive events during drag
        match event.hits_with_capture_overload(
            cx,
            self.view.area(),
            self.dragging_item.is_some()  // Enable capture when dragging
        ) {
            Hit::FingerMove(fe) if self.dragging_item.is_some() => {
                // Update drop preview
                self.drop_state = self.find_drop_position(cx, fe.abs);
                self.view.redraw(cx);
            }
            Hit::FingerUp(fe) => {
                if let Some(dragged_id) = self.dragging_item {
                    self.handle_drop(cx, fe.abs, dragged_id);
                }
                self.dragging_item = None;
                self.drop_state = None;
                self.view.redraw(cx);
            }
            _ => {}
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        if self.needs_layout_update {
            self.needs_layout_update = false;
            self.apply_layout(cx);
        }

        let result = self.view.draw_walk(cx, scope, walk);

        // Draw drop preview overlay
        if let Some(ref pos) = self.drop_state {
            self.drop_preview.draw_abs(cx, pos.rect);
        }

        result
    }
}

impl DragContainer {
    fn find_drop_position(&self, cx: &Cx, abs: DVec2) -> Option<DropPosition> {
        let container = self.view.view(id!(container));
        let rect = container.area().rect(cx);

        if !rect.contains(abs) { return None; }

        // Calculate row from Y position
        let visible_rows: Vec<_> = (0..3)
            .filter(|&r| !self.row_assignments[r].is_empty())
            .collect();

        let num_rows = visible_rows.len();
        if num_rows == 0 { return None; }

        let row_height = rect.size.y / num_rows as f64;
        let rel_y = abs.y - rect.pos.y;
        let visual_row = ((rel_y / row_height) as usize).min(num_rows - 1);
        let actual_row = visible_rows[visual_row];

        // Calculate column from X position
        let cols = self.row_assignments[actual_row].len().max(1);
        let col_width = rect.size.x / cols as f64;
        let rel_x = abs.x - rect.pos.x;
        let col = ((rel_x / col_width) as usize).min(cols);

        let preview_rect = Rect {
            pos: DVec2 {
                x: rect.pos.x + col.min(cols - 1) as f64 * col_width,
                y: rect.pos.y + visual_row as f64 * row_height,
            },
            size: DVec2 { x: col_width, y: row_height },
        };

        Some(DropPosition { row: actual_row, col, rect: preview_rect })
    }

    fn find_item_row(&self, item_id: usize) -> Option<(usize, usize)> {
        for (row, items) in self.row_assignments.iter().enumerate() {
            if let Some(col) = items.iter().position(|&id| id == item_id) {
                return Some((row, col));
            }
        }
        None
    }

    fn handle_drop(&mut self, cx: &mut Cx, abs: DVec2, dragged_id: usize) {
        let Some(drop_pos) = self.find_drop_position(cx, abs) else { return };
        let Some((src_row, src_col)) = self.find_item_row(dragged_id) else { return };

        if src_row == drop_pos.row && src_col == drop_pos.col { return; }

        // Remove from source
        self.row_assignments[src_row].remove(src_col);

        // Calculate insert position
        let target_len = self.row_assignments[drop_pos.row].len();
        let mut insert_col = drop_pos.col.min(target_len);

        // Adjust for same-row moves
        if src_row == drop_pos.row && drop_pos.col > src_col {
            insert_col = insert_col.saturating_sub(1);
        }

        // Insert at target
        self.row_assignments[drop_pos.row].insert(insert_col, dragged_id);

        self.needs_layout_update = true;
        self.view.redraw(cx);
    }

    fn apply_layout(&mut self, cx: &mut Cx) {
        // Hide all slots first, then show only assigned ones
        // See Pattern 17: Row-Based Grid Layout for details
    }
}
```

## Critical Points

1. **Use `hits_with_capture_overload`**: Pass `true` during drag to receive events outside original hit area

2. **Per-row tracking**: `row_assignments: [Vec<usize>; 3]` enables true physical movement between rows

3. **Deferred visual updates**: Set `needs_visual_update = true`, apply in `draw_walk` for proper Makepad integration

4. **Drop preview**: Draw overlay in `draw_walk` AFTER drawing main view, use `draw_depth` for z-ordering

5. **Excess slots**: Define more slots than typically needed (e.g., 9 per row) for flexibility

## Why Not Platform Drag?

`cx.start_dragging()` has limitations:
- "Dragging string not implemented on macos yet"
- Limited to predefined drag data types

Internal drag handling via `hits_with_capture_overload` works consistently across platforms.

## When to Use

- IDE/studio window management
- Kanban boards with column reordering
- Dashboard tile arrangement
- Any drag-to-reorder UI

## References

- [Row-Based Grid Layout](./_base/17-row-based-grid-layout.md) - Foundation pattern
- [flex-layout-demo](examples/flex-layout-demo) - Full working implementation
```

## File: `skills/robius-widget-patterns/_base/19-pageflip-optimization.md`
```markdown
---
name: makepad-pageflip-optimization
author: robius
source: moly, robrix
date: 2025-01-20
tags: [pageflip, performance, cache, lifecycle, optimization]
level: advanced
---

# Pattern 19: PageFlip 切换优化

解决 PageFlip 页面切换慢的问题 —— 当页面组件多或组件树深时，所有组件在 visible 时都会走创建生命周期。

## Problem

PageFlip（或类似的页面切换组件）切换慢，原因：
- 页面中组件数量多
- 组件树层级深
- 所有组件在 `visible` 时都要完成创建生命周期
- 用户快速切换时，前一个页面还没加载完

## Solution

两种模式：

| 模式 | 行为 | 适用场景 |
|-----|------|---------|
| **即刻销毁** | 切换时强制销毁未加载完的组件 | 内存敏感，页面不常回切 |
| **即刻缓存** | 暂停加载但不销毁，切回继续 | 频繁切换的页面 |

---

## Pattern 1: 即刻销毁模式 (Immediate Destroy)

通过事件通知父 View 强制销毁未完成加载的子组件。

### 定义 Action

```rust
#[derive(Clone, Debug, DefaultNone)]
pub enum PageSwitchAction {
    None,
    /// 请求销毁当前页面未完成的加载
    RequestDestroy { page_id: LiveId },
    /// 页面切换开始
    SwitchStarted { from: LiveId, to: LiveId },
}
```

### PageFlip 包装器

```rust
#[derive(Live, LiveHook, Widget)]
pub struct ManagedPageFlip {
    #[deref] view: View,
    #[live] page_flip: PageFlip,

    #[rust] current_page: Option<LiveId>,
    #[rust] loading_pages: HashSet<LiveId>,
    #[rust] page_load_state: HashMap<LiveId, PageLoadState>,
}

#[derive(Clone, Default)]
pub struct PageLoadState {
    pub is_loading: bool,
    pub loaded_count: usize,
    pub total_count: usize,
}

impl ManagedPageFlip {
    pub fn switch_to(&mut self, cx: &mut Cx, page_id: LiveId) {
        let old_page = self.current_page;

        // 1. 通知旧页面停止加载
        if let Some(old_id) = old_page {
            if self.loading_pages.contains(&old_id) {
                // 发送销毁请求
                cx.widget_action(
                    self.widget_uid(),
                    &HeapLiveIdPath::default(),
                    PageSwitchAction::RequestDestroy { page_id: old_id }
                );
            }
        }

        // 2. 切换到新页面
        self.current_page = Some(page_id);
        self.page_flip.set_active(cx, page_id);

        // 3. 发送切换事件
        if let Some(from) = old_page {
            cx.widget_action(
                self.widget_uid(),
                &HeapLiveIdPath::default(),
                PageSwitchAction::SwitchStarted { from, to: page_id }
            );
        }

        self.redraw(cx);
    }

    pub fn mark_page_loading(&mut self, page_id: LiveId) {
        self.loading_pages.insert(page_id);
    }

    pub fn mark_page_loaded(&mut self, page_id: LiveId) {
        self.loading_pages.remove(&page_id);
    }
}
```

### 页面组件响应销毁请求

```rust
#[derive(Live, LiveHook, Widget)]
pub struct HeavyPage {
    #[deref] view: View,

    #[rust] is_loading: bool,
    #[rust] loaded_items: Vec<WidgetRef>,
    #[rust] pending_items: VecDeque<ItemData>,
    #[rust] load_batch_size: usize,
}

impl Widget for HeavyPage {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // 处理销毁请求
        if let Event::Actions(actions) = event {
            for action in actions {
                if let Some(PageSwitchAction::RequestDestroy { page_id }) = action.downcast_ref() {
                    if self.is_this_page(*page_id) {
                        self.force_destroy_pending(cx);
                        return;
                    }
                }
            }
        }

        // 正常事件处理...
        self.view.handle_event(cx, event, scope);
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // 增量加载：每帧只加载一批
        if self.is_loading && !self.pending_items.is_empty() {
            self.load_next_batch(cx);
        }

        self.view.draw_walk(cx, scope, walk)
    }
}

impl HeavyPage {
    fn force_destroy_pending(&mut self, cx: &mut Cx) {
        // 清空待加载队列
        self.pending_items.clear();
        self.is_loading = false;

        // 可选：销毁部分已加载的组件以释放内存
        // self.loaded_items.truncate(MIN_KEEP_COUNT);

        log!("Page loading interrupted, pending items destroyed");
    }

    fn load_next_batch(&mut self, cx: &mut Cx) {
        let batch: Vec<_> = self.pending_items
            .drain(..self.load_batch_size.min(self.pending_items.len()))
            .collect();

        for item_data in batch {
            let widget = self.create_item_widget(cx, &item_data);
            self.loaded_items.push(widget);
        }

        if self.pending_items.is_empty() {
            self.is_loading = false;
            // 通知加载完成
            Cx::post_action(PageSwitchAction::None);  // 或自定义完成事件
        }

        self.redraw(cx);
    }
}
```

---

## Pattern 2: 即刻缓存模式 (Immediate Cache)

暂停加载但保留已加载的组件，切回时继续加载。

### CacheView 定义

```rust
#[derive(Live, LiveHook, Widget)]
pub struct CacheView {
    #[deref] view: View,

    #[rust] is_active: bool,
    #[rust] load_paused: bool,
    #[rust] load_progress: LoadProgress,
}

#[derive(Clone, Default)]
pub struct LoadProgress {
    pub loaded_count: usize,
    pub total_count: usize,
    pub pending_items: VecDeque<ItemData>,
}

impl CacheView {
    /// 暂停加载（切换离开时调用）
    pub fn pause_loading(&mut self) {
        if !self.load_paused {
            self.load_paused = true;
            log!("CacheView: Loading paused at {}/{}",
                self.load_progress.loaded_count,
                self.load_progress.total_count);
        }
    }

    /// 恢复加载（切换回来时调用）
    pub fn resume_loading(&mut self, cx: &mut Cx) {
        if self.load_paused {
            self.load_paused = false;
            log!("CacheView: Resuming loading from {}/{}",
                self.load_progress.loaded_count,
                self.load_progress.total_count);
            self.redraw(cx);  // 触发继续加载
        }
    }

    /// 检查是否还有待加载内容
    pub fn has_pending_load(&self) -> bool {
        !self.load_progress.pending_items.is_empty()
    }
}

impl Widget for CacheView {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // 只在激活且未暂停时继续加载
        if self.is_active && !self.load_paused && self.has_pending_load() {
            self.load_next_chunk(cx);
        }

        self.view.draw_walk(cx, scope, walk)
    }
}
```

### 使用 CacheView 的 PageFlip

```rust
#[derive(Live, LiveHook, Widget)]
pub struct CachedPageFlip {
    #[deref] view: View,

    #[rust] pages: HashMap<LiveId, CacheViewRef>,
    #[rust] current_page: Option<LiveId>,
}

impl CachedPageFlip {
    pub fn switch_to(&mut self, cx: &mut Cx, page_id: LiveId) {
        // 1. 暂停当前页面的加载
        if let Some(current) = self.current_page {
            if let Some(page) = self.pages.get_mut(&current) {
                page.pause_loading();
            }
        }

        // 2. 切换页面
        self.current_page = Some(page_id);

        // 3. 恢复新页面的加载（如果之前暂停过）
        if let Some(page) = self.pages.get_mut(&page_id) {
            page.resume_loading(cx);
        }

        self.redraw(cx);
    }
}
```

---

## Pattern 3: 混合模式 (Hybrid)

根据内存压力动态选择销毁或缓存。

```rust
#[derive(Clone, Copy, PartialEq)]
pub enum PageCachePolicy {
    /// 总是缓存（内存充足）
    AlwaysCache,
    /// 总是销毁（内存紧张）
    AlwaysDestroy,
    /// LRU 策略（保留最近 N 个）
    LruCache { max_cached: usize },
}

#[derive(Live, Widget)]
pub struct SmartPageFlip {
    #[deref] view: View,

    #[rust] cache_policy: PageCachePolicy,
    #[rust] page_cache: HashMap<LiveId, CachedPage>,
    #[rust] access_order: VecDeque<LiveId>,
    #[rust] current_page: Option<LiveId>,
}

impl SmartPageFlip {
    pub fn switch_to(&mut self, cx: &mut Cx, page_id: LiveId) {
        let old_page = self.current_page;

        match self.cache_policy {
            PageCachePolicy::AlwaysDestroy => {
                // 销毁旧页面
                if let Some(old_id) = old_page {
                    self.destroy_page(cx, old_id);
                }
            }
            PageCachePolicy::AlwaysCache => {
                // 暂停旧页面
                if let Some(old_id) = old_page {
                    self.pause_page(old_id);
                }
            }
            PageCachePolicy::LruCache { max_cached } => {
                // 暂停旧页面
                if let Some(old_id) = old_page {
                    self.pause_page(old_id);
                }
                // 更新访问顺序
                self.update_access_order(page_id);
                // 淘汰超出限制的页面
                self.evict_if_needed(cx, max_cached);
            }
        }

        self.current_page = Some(page_id);
        self.activate_page(cx, page_id);
        self.redraw(cx);
    }

    fn evict_if_needed(&mut self, cx: &mut Cx, max_cached: usize) {
        while self.page_cache.len() > max_cached {
            if let Some(oldest) = self.access_order.pop_front() {
                self.destroy_page(cx, oldest);
            }
        }
    }
}
```

---

## 增量加载模式

避免一次性创建所有组件，分帧加载。

```rust
const ITEMS_PER_FRAME: usize = 5;

impl HeavyPage {
    fn start_incremental_load(&mut self, items: Vec<ItemData>) {
        self.pending_items = VecDeque::from(items);
        self.is_loading = true;
        self.loaded_items.clear();
    }

    fn load_next_chunk(&mut self, cx: &mut Cx) {
        if self.load_paused || self.pending_items.is_empty() {
            return;
        }

        // 每帧只加载固定数量
        for _ in 0..ITEMS_PER_FRAME {
            if let Some(item_data) = self.pending_items.pop_front() {
                let widget = self.create_item_widget(cx, &item_data);
                self.loaded_items.push(widget);
            } else {
                break;
            }
        }

        // 如果还有待加载，请求下一帧继续
        if !self.pending_items.is_empty() {
            self.redraw(cx);  // 触发下一帧的 draw_walk
        } else {
            self.is_loading = false;
        }
    }
}
```

---

## Makepad 官方 CachedWidget

Makepad 提供了内置的 `CachedWidget`，是一个**全局单例包装器**，用于跨布局共享 widget 实例。

### 源码位置

`makepad-widgets/src/cached_widget.rs`

### 核心实现

```rust
/// A Singleton wrapper widget that caches and reuses its child widget across multiple instances.
#[derive(Live, LiveRegisterWidget, WidgetRef)]
pub struct CachedWidget {
    #[walk] walk: Walk,
    #[rust] template_id: LiveId,
    #[rust] template: Option<LivePtr>,
    #[rust] widget: Option<WidgetRef>,
}

/// 全局缓存存储
#[derive(Default)]
pub struct WidgetWrapperCache {
    map: HashMap<LiveId, WidgetRef>,
}

impl LiveHook for CachedWidget {
    fn after_apply(&mut self, cx: &mut Cx, ...) {
        // 确保全局缓存存在
        if !cx.has_global::<WidgetWrapperCache>() {
            cx.set_global(WidgetWrapperCache::default())
        }

        if self.widget.is_none() {
            // 尝试从全局缓存获取
            if let Some(widget) = cx.get_global::<WidgetWrapperCache>()
                .map.get_mut(&self.template_id)
            {
                self.widget = Some(widget.clone());
            } else {
                // 不存在则创建并缓存
                let widget = WidgetRef::new_from_ptr(cx, self.template);
                cx.get_global::<WidgetWrapperCache>()
                    .map.insert(self.template_id, widget.clone());
                self.widget = Some(widget);
            }
        }
    }
}
```

### DSL 用法

```rust
live_design! {
    <CachedWidget> {
        my_widget = <MyWidget> {}
    }
}
```

### 特点

- **全局单例**：相同 `template_id` 的 widget 只创建一次
- **状态保持**：切换布局时保持 widget 状态
- **透明代理**：自动代理 `handle_event` 和 `draw_walk`

---

## Moly 的 ChatsDeck 实现

Moly 使用**自定义 LRU 缓存** + `CachedWidget` 组合方案。

### 架构

```
ChatScreen
  └── <CachedWidget>           // 跨布局共享
        └── ChatsDeck          // 自定义 LRU 缓存
              └── HashMap<ChatID, ChatViewRef>  // 聊天视图缓存
```

### 核心代码 (moly/src/chat/chats_deck.rs)

```rust
const MAX_CHAT_VIEWS: usize = 10;

#[derive(Live, LiveHook, Widget)]
pub struct ChatsDeck {
    #[deref] view: View,

    /// 所有聊天视图缓存
    #[rust] chat_view_refs: HashMap<ChatID, ChatViewRef>,

    /// LRU 访问顺序
    #[rust] chat_view_accesed_order: VecDeque<ChatID>,

    /// 当前可见的聊天 ID
    #[rust] currently_visible_chat_id: Option<ChatID>,

    /// 聊天视图模板
    #[live] chat_view_template: Option<LivePtr>,
}

impl ChatsDeck {
    pub fn create_or_update_chat_view(&mut self, cx: &mut Cx, chat: &ChatData, ...) {
        // 1. 检查是否已存在
        if let Some(chat_view) = self.chat_view_refs.get_mut(&chat.id) {
            // 更新现有视图
            self.currently_visible_chat_id = Some(chat.id);
        } else {
            // 2. 创建新视图
            let chat_view = WidgetRef::new_from_ptr(cx, self.chat_view_template);
            self.chat_view_refs.insert(chat.id, chat_view.as_chat_view());
            self.currently_visible_chat_id = Some(chat.id);
        }

        // 3. 更新 LRU 访问顺序
        self.chat_view_accesed_order.retain(|id| *id != chat.id);
        self.chat_view_accesed_order.push_back(chat.id);

        // 4. 超出限制时淘汰（但保护正在流式传输的聊天）
        if self.chat_view_accesed_order.len() > MAX_CHAT_VIEWS {
            let oldest_id = self.chat_view_accesed_order.pop_front().unwrap();
            if let Some(chat_view) = self.chat_view_refs.get_mut(&oldest_id) {
                // 🔑 关键：不淘汰正在流式传输的聊天
                if !chat_view.chat(id!(chat)).read().is_streaming() {
                    self.chat_view_refs.remove(&oldest_id);
                }
            }
        }
    }
}
```

### 亮点

- **流式保护**：不淘汰正在接收 AI 响应的聊天
- **懒加载**：只在需要时创建 ChatView
- **状态同步**：通过 `chats_views_pending_sync` 延迟更新上下文

---

## Robrix 的 CachedWidget 使用

Robrix 大量使用 `CachedWidget` 实现 **Desktop/Mobile 布局状态共享**。

### 使用场景

```rust
live_design! {
    pub HomeScreen = {{HomeScreen}} {
        <AdaptiveView> {
            // NOTE: 使用 CachedWidget 包装确保只有一个全局实例
            // 这样在 Desktop 和 Mobile 布局切换时保持状态

            Desktop = <View> {
                <CachedWidget> {
                    navigation_tab_bar = <NavigationTabBar> {}
                }
                <CachedWidget> {
                    rooms_list = <RoomsList> {}
                }
                <CachedWidget> {
                    settings_screen = <SettingsScreen> {}
                }
            }

            Mobile = <View> {
                // 同样的 widget ID，复用同一实例
                <CachedWidget> {
                    navigation_tab_bar = <NavigationTabBar> {}
                }
                <CachedWidget> {
                    rooms_list = <RoomsList> {}
                }
            }
        }
    }
}
```

### 典型包装对象

| Widget | 为什么缓存 |
|--------|----------|
| `NavigationTabBar` | 保持选中状态 |
| `RoomsList` | 保持滚动位置和加载状态 |
| `RoomFilterInputBar` | 保持搜索文本 |
| `SettingsScreen` | 保持设置状态 |
| `SpacesBar` | 保持展开/折叠状态 |

### 注意事项

```rust
// ⚠️ CachedWidget + AdaptiveView 的 DSL 样式覆盖问题
// DSL 级别的样式覆盖可能不生效，需要在代码中手动 apply_over

fn draw_walk(&mut self, cx: &mut Cx2d, ...) {
    // 因为 chats_deck 被缓存，DSL 属性覆盖不会生效
    // 需要通过 apply_over 手动覆盖
    if cx.display_context.is_desktop() {
        self.view.apply_over(cx, live! {
            padding: {top: 18, bottom: 10, right: 28, left: 28}
        });
    } else {
        self.view.apply_over(cx, live! {
            padding: {top: 55, left: 0, right: 0, bottom: 0}
        });
    }
}
```

---

## 对比总结

| 特性 | Makepad CachedWidget | Moly ChatsDeck | 本文档 Pattern |
|------|---------------------|----------------|---------------|
| **目标** | 跨布局状态共享 | 聊天视图 LRU 缓存 | PageFlip 切换优化 |
| **粒度** | Widget 级单例 | 视图级 LRU | 页面级生命周期 |
| **缓存策略** | 永久缓存 | LRU (max=10) | 可配置 |
| **淘汰条件** | 不淘汰 | 非流式传输时淘汰 | 暂停/销毁可选 |
| **适用场景** | Desktop/Mobile 切换 | 多聊天切换 | 深组件树页面切换 |

---

## When to Use

| 场景 | 推荐模式 |
|------|---------|
| 页面组件 100+ | 增量加载 + 即刻销毁 |
| 频繁切换的标签页 | 即刻缓存 |
| 内存敏感的移动端 | LRU 混合模式 |
| 简单页面 (<20 组件) | 无需优化 |

## 性能对比

| 模式 | 首次切换 | 回切 | 内存占用 |
|------|---------|------|---------|
| 无优化 | 慢 | 慢 | 高 |
| 即刻销毁 | 快 | 慢（重建） | 低 |
| 即刻缓存 | 快 | 快（恢复） | 中 |
| LRU 混合 | 快 | 取决于缓存命中 | 可控 |

## References

### Makepad 源码
- `makepad-widgets/src/cached_widget.rs` - CachedWidget 官方实现

### Moly 源码
- `moly/src/chat/chats_deck.rs` - ChatsDeck LRU 缓存实现
- `moly/src/chat/chat_screen.rs` - CachedWidget 使用示例
- `moly/src/chat/chat_screen_mobile.rs` - Mobile 布局 CachedWidget

### Robrix 源码
- `robrix/src/home/home_screen.rs:62-226` - 大量 CachedWidget 使用
- `robrix/src/home/rooms_sidebar.rs` - RoomsList 缓存
- `robrix/src/home/navigation_tab_bar.rs` - 导航栏缓存
- `robrix/src/shared/room_filter_input_bar.rs` - 搜索栏缓存说明

### GitHub
- [Moly](https://github.com/moxin-org/moly) - AI 聊天应用
- [Robrix](https://github.com/project-robius/robrix) - Matrix 客户端
```

## File: `skills/robius-widget-patterns/_base/20-redraw-optimization.md`
```markdown
---
name: makepad-redraw-optimization
author: robius
source: robrix
date: 2024-01-12
tags: [redraw, performance, optimization, animation, visibility]
level: intermediate
---

# Pattern 15: Redraw Optimization

Efficient redraw patterns to avoid unnecessary GPU work and improve performance.

## Problem

Calling `redraw()` after every state change causes:
- Unnecessary GPU work
- UI flicker
- Poor performance with complex widget trees

## Solution

Use conditional redraws, batch updates, and leverage animator auto-redraw.

## Key Principles

| Principle | Description |
|-----------|-------------|
| **Conditional redraw** | Only redraw when visual state actually changes |
| **Batch updates** | Multiple mutations, single redraw at end |
| **Animator-driven** | Let animations handle their own redraws |
| **Separate concerns** | Update methods without redraw, caller decides |

## Pattern 1: Conditional Redraw

Only redraw when state actually changes:

```rust
pub fn update_visibility(&mut self, cx: &mut Cx, should_show: bool) {
    let was_visible = self.visible;  // Store previous state

    self.visible = should_show;
    self.view(ids!(content)).set_visible(cx, should_show);

    // Only redraw if visibility actually changed
    if self.visible != was_visible {
        self.redraw(cx);
    }
}
```

## Pattern 2: Separate Update and Redraw

Create update methods that don't redraw:

```rust
impl MyWidget {
    /// Updates state WITHOUT redrawing. Caller must redraw.
    pub fn update_state(&mut self, cx: &mut Cx, new_value: String) {
        self.value = new_value;
        self.label(ids!(display)).set_text(cx, &self.value);
        // NOTE: No redraw here - caller decides when
    }

    /// Updates state AND redraws.
    pub fn set_value(&mut self, cx: &mut Cx, new_value: String) {
        self.update_state(cx, new_value);
        self.redraw(cx);
    }
}

// Usage: batch multiple updates
widget.update_state(cx, "value1");
widget.update_other(cx, 42);
widget.redraw(cx);  // Single redraw for all updates
```

## Pattern 3: Animator-Driven Redraw

Let animations auto-handle redraws:

```rust
live_design! {
    MyPanel = {{MyPanel}} {
        animator: {
            panel = {
                default: hide,
                show = {
                    redraw: true,  // Auto redraw during animation
                    from: {all: Forward {duration: 0.3}}
                    ease: ExpDecay {d1: 0.80, d2: 0.97}
                    apply: { draw_bg: {opacity: 1.0} }
                }
                hide = {
                    redraw: true,  // Auto redraw during animation
                    from: {all: Forward {duration: 0.2}}
                    apply: { draw_bg: {opacity: 0.0} }
                }
            }
        }
    }
}
```

## Pattern 4: Check Animator State

Only redraw when animator requires it:

```rust
fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
    let animator_action = self.animator_handle_event(cx, event);

    // Only redraw if animation needs it
    if animator_action.must_redraw() {
        self.redraw(cx);
    }

    // Check if animation finished
    if self.animator_in_state(cx, ids!(panel.hide)) {
        if self.is_animating_out && !animator_action.is_animating() {
            // Animation completed
            self.visible = false;
            self.redraw(cx);
            return;
        }
    }
}
```

## Pattern 5: Batch Updates Before Redraw

```rust
fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
    let mut needs_redraw = false;

    // Process multiple actions
    if self.button(ids!(btn1)).clicked(actions) {
        self.state1 = true;
        needs_redraw = true;
    }

    if self.button(ids!(btn2)).clicked(actions) {
        self.state2 = false;
        needs_redraw = true;
    }

    if let Some(text) = self.text_input(ids!(input)).changed(actions) {
        self.value = text;
        needs_redraw = true;
    }

    // Single redraw for all changes
    if needs_redraw {
        self.redraw(cx);
    }
}
```

## Pattern 6: Visibility Changes

Always redraw after visibility changes:

```rust
pub fn show(&mut self, cx: &mut Cx) {
    self.visible = true;
    self.view(ids!(content)).set_visible(cx, true);
    cx.set_key_focus(self.view.area());
    self.redraw(cx);  // MUST redraw after visibility
}

pub fn hide(&mut self, cx: &mut Cx) {
    self.visible = false;
    self.view(ids!(content)).set_visible(cx, false);
    self.redraw(cx);  // MUST redraw after visibility
}
```

## Pattern 7: Deferred Expensive Operations

For expensive operations, defer and batch:

```rust
impl RoomsList {
    // Don't auto-apply filter on every change
    #[rust] display_filter: RoomDisplayFilter,
    #[rust] filter_dirty: bool,

    pub fn set_filter(&mut self, filter: RoomDisplayFilter) {
        self.display_filter = filter;
        self.filter_dirty = true;
        // Don't apply yet - wait for explicit call
    }

    pub fn apply_filter_if_needed(&mut self, cx: &mut Cx) {
        if self.filter_dirty {
            self.filter_dirty = false;
            self.apply_filter();  // Expensive operation
            self.redraw(cx);
        }
    }
}
```

## Anti-Patterns to Avoid

### 1. Unconditional Redraw
```rust
// BAD: Redraws even if nothing visual changed
fn update(&mut self, cx: &mut Cx) {
    self.internal_counter += 1;
    self.redraw(cx);  // Unnecessary if counter not displayed
}
```

### 2. Multiple Sequential Redraws
```rust
// BAD: Multiple redraws
fn setup(&mut self, cx: &mut Cx) {
    self.set_title(cx, "Hello");
    self.redraw(cx);  // Redraw 1
    self.set_subtitle(cx, "World");
    self.redraw(cx);  // Redraw 2
    self.set_icon(cx, icon);
    self.redraw(cx);  // Redraw 3
}

// GOOD: Single redraw
fn setup(&mut self, cx: &mut Cx) {
    self.set_title(cx, "Hello");
    self.set_subtitle(cx, "World");
    self.set_icon(cx, icon);
    self.redraw(cx);  // Single redraw
}
```

### 3. Forgetting Redraw After set_visible
```rust
// BAD: Visibility not reflected
self.view(ids!(panel)).set_visible(cx, false);
// Missing redraw!

// GOOD
self.view(ids!(panel)).set_visible(cx, false);
self.redraw(cx);
```

## When to Redraw

| Situation | Redraw? |
|-----------|---------|
| State change affecting display | Yes |
| Internal state (not displayed) | No |
| After `set_visible()` | Yes |
| After `set_text()` | Yes |
| Animation start/stop | Yes (or use `redraw: true` in animator) |
| After animator action | Only if `must_redraw()` |
| Multiple updates | Batch, then single redraw |

## Performance Tips

1. **Use `redraw: true` in animator** - Auto-handles animation frames
2. **Store previous state** - Compare before redrawing
3. **Separate update methods** - Let caller batch redraws
4. **Defer expensive operations** - Mark dirty, apply on demand
5. **Check `must_redraw()`** - Don't redraw unnecessarily during animations

## References

- [Robrix editing_pane.rs](https://github.com/project-robius/robrix/blob/main/src/home/editing_pane.rs)
- [Robrix jump_to_bottom_button.rs](https://github.com/project-robius/robrix/blob/main/src/shared/jump_to_bottom_button.rs)
```

## File: `skills/robius-widget-patterns/_base/21-collapsible-row-portal-list.md`
```markdown
---
name: collapsible-row-portal-list
author: alanpoon
source: robrix
date: 2026-01-19
tags: [portal-list, grouping, collapsible, fold-header, rangemap]
level: advanced
---

# Portal List Auto-Grouping

Automatically group consecutive identical items in a portal list under collapsible headers.

## Problem

When displaying large datasets in a portal list (like a news feed or message list), consecutive items with the same category or key can create visual clutter. Users need a way to collapse related items into groups to better scan and navigate the list, especially when 3 or more consecutive items share the same key.

## Solution

Use a `GroupHeaderManager` with `RangeMap` to track consecutive items with identical keys and automatically render them as `FoldHeader` widgets with collapsible content. This pattern integrates seamlessly with Makepad's portal list rendering system.

## Implementation

### Custom Widgets

This pattern uses two custom helper widgets that extend Makepad's built-in functionality:

#### FoldButtonWithText

**Derived from**: `FoldButton` widget

**Unique Functionality**:
- Combines the triangular fold indicator with dynamic text labels in a single interactive component
- Text automatically switches between `open_text` and `close_text` based on fold state
- Unified hover and click interactions for both indicator and text
- Useful for accessibility and clearer UI communication (e.g., "Show More" / "Show Less")

**Key Differences from FoldButton**:
- Standard `FoldButton`: Only displays animated triangle indicator
- `FoldButtonWithText`: Triangle + text label that changes with state

**IMPORTANT**: Must use `makepad_widgets::fold_button::FoldButtonAction` for action events. Do NOT create a custom FoldButtonAction type. This ensures compatibility with the FoldHeader widget system.

```rust
use makepad_widgets::*;
use makepad_widgets::widget::WidgetActionData;
use makepad_widgets::fold_button::FoldButtonAction;  // IMPORTANT: Use existing action type

#[derive(Live, Widget)]
pub struct FoldButtonWithText {
    #[animator] animator: Animator,
    #[redraw] #[live] draw_bg: DrawQuad,
    #[redraw] #[live] draw_text: DrawText,
    #[walk] walk: Walk,
    #[layout] layout: Layout,
    #[live] active: f64,
    #[live] triangle_size: f64,
    #[live] open_text: ArcStringMut,   // Text when closed
    #[live] close_text: ArcStringMut,  // Text when open
    #[action_data] #[rust] action_data: WidgetActionData,
}

impl Widget for FoldButtonWithText {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        let uid = self.widget_uid();
        let res = self.animator_handle_event(cx, event);

        if res.is_animating() {
            if self.animator.is_track_animating(cx, ids!(active)) {
                let mut value = [0.0];
                self.draw_bg.get_instance(cx, ids!(active), &mut value);
                // Use makepad's FoldButtonAction, not a custom one
                cx.widget_action(uid, &scope.path, FoldButtonAction::Animating(value[0] as f64))
            }
            if res.must_redraw() {
                self.draw_bg.redraw(cx);
            }
        }

        match event.hits(cx, self.draw_bg.area()) {
            Hit::FingerDown(_fe) => {
                if self.animator_in_state(cx, ids!(active.on)) {
                    self.animator_play(cx, ids!(active.off));
                    // Use makepad's FoldButtonAction::Closing
                    cx.widget_action(uid, &scope.path, FoldButtonAction::Closing)
                } else {
                    self.animator_play(cx, ids!(active.on));
                    // Use makepad's FoldButtonAction::Opening
                    cx.widget_action(uid, &scope.path, FoldButtonAction::Opening)
                }
                self.animator_play(cx, ids!(hover.on));
            },
            Hit::FingerHoverIn(_) => {
                cx.set_cursor(MouseCursor::Hand);
                self.animator_play(cx, ids!(hover.on));
            }
            Hit::FingerHoverOut(_) => {
                self.animator_play(cx, ids!(hover.off));
            }
            Hit::FingerUp(fe) => {
                if fe.is_over {
                    if fe.device.has_hovers() {
                        self.animator_play(cx, ids!(hover.on));
                    } else {
                        self.animator_play(cx, ids!(hover.off));
                    }
                } else {
                    self.animator_play(cx, ids!(hover.off));
                }
            }
            _ => ()
        }
    }

    fn draw_walk(&mut self, cx: &mut Cx2d, _scope: &mut Scope, walk: Walk) -> DrawStep {
        self.draw_bg.begin(cx, walk, self.layout);

        // Dynamically select text based on state
        let text = if self.active > 0.5 {
            self.close_text.as_ref()  // Expanded state
        } else {
            self.open_text.as_ref()   // Collapsed state
        };

        let label_walk = walk.with_margin_left(self.triangle_size * 2.0 + 10.0);
        self.draw_text.draw_walk(cx, label_walk, Align::default(), text);
        self.draw_bg.end(cx);
        DrawStep::done()
    }
}

// Helper methods can use the standard FoldButtonAction
impl FoldButtonWithText {
    pub fn opening(&self, actions: &Actions) -> bool {
        if let Some(item) = actions.find_widget_action(self.widget_uid()) {
            if let FoldButtonAction::Opening = item.cast() {
                return true
            }
        }
        false
    }

    pub fn closing(&self, actions: &Actions) -> bool {
        if let Some(item) = actions.find_widget_action(self.widget_uid()) {
            if let FoldButtonAction::Closing = item.cast() {
                return true
            }
        }
        false
    }
}
```

#### PortalList in FoldHeader Body

**Derived from**: Standard `PortalList` widget

**Unique Functionality**:
- Directly embeds a PortalList inside the FoldHeader body for dynamic content rendering
- Leverages the portal list's built-in template instantiation and rendering system
- No need for intermediate ViewList widget or dummy portal list pattern
- Manages widget lifecycle, drawing, and event handling automatically

**Key Differences from Dummy PortalList Pattern**:
- Old approach: Dummy PortalList (height: 0) + ViewList + manual WidgetRef management
- New approach: Direct PortalList in body with `height: Fit`

**Direct PortalList Pattern**:

This pattern uses a real PortalList directly inside the FoldHeader body:

```rust
// 1. Define a PortalList directly in your FoldHeader body
live_design! {
    SmallStateGroupHeader = <FoldHeader> {
        body: <View> {
            width: Fill,
            height: Fit
            flow: Down
            <PortalList> {
                height: Fit, width: Fill
                SmallStateEvent = <SmallStateEvent> {}
                Message = <Message> {}
            }
        }
    }
}

// 2. Use the FoldHeader's draw_walk to access and render the portal list
let mut walk = walk;
walk.height = Size::Fit;
while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
    if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
        let list = list_ref.deref_mut();

        // Directly render items in the range
        for tl_idx in (group_range.start)..group_range.end {
            if let Some(timeline_item) = tl_items.get(tl_idx) {
                // Populate and draw items directly
                let item = list.item(cx, tl_idx, live_id!(SmallStateEvent));
                item.label(ids!(text)).set_text(cx, &data_item.text);
                item.draw_all(cx, scope);
            }
        }
    }
}
```

**Why Use Direct PortalList?**

This pattern has several advantages over the dummy PortalList + ViewList approach:
1. **Simpler architecture**: No need for intermediate ViewList widget
2. **Native portal list features**: Automatic virtualization, scroll handling, and item management
3. **Better performance**: Direct rendering without WidgetRef collection overhead
4. **Height: Fit support**: Portal list automatically sizes to content with `height: Fit`
5. **Less code**: Eliminates ViewList widget implementation and dummy portal list pattern

### GroupHeaderManager

```rust
use std::{collections::HashMap, ops::Range};
use rangemap::RangeMap;

#[derive(Debug, Clone, Default)]
struct GroupMeta {
    key: String,
    count: usize,
}

#[derive(Default)]
struct GroupHeaderManager {
    group_ranges: RangeMap<usize, String>,
    groups_by_id: HashMap<String, GroupMeta>,
}

impl GroupHeaderManager {
    fn new() -> Self {
        Self {
            group_ranges: RangeMap::new(),
            groups_by_id: HashMap::new(),
        }
    }

    fn check_group_header_status(&self, item_id: usize) -> Option<Range<usize>> {
        for (range, _) in self.group_ranges.iter() {
            if range.contains(&item_id) {
                return Some(range.clone())
            }
        }
        None
    }

    fn get_group_at_item_id(&self, item_id: usize) -> Option<&GroupMeta> {
        self.group_ranges
            .iter()
            .find(|(range, _)| range.start == item_id)
            .and_then(|(_, header_id)| self.groups_by_id.get(header_id))
    }

    /// Computes groups from data.
    ///
    /// **IMPORTANT**: Call this ONLY when data is first available or when data changes.
    /// DO NOT call this during `draw_walk()` as it would recompute on every frame.
    ///
    /// Correct usage:
    /// - In `after_new_from_doc()` hook after initializing data
    /// - When receiving new data from network/updates
    /// - In response to user actions that modify data
    ///
    /// Incorrect usage:
    /// - Inside `draw_walk()` or any rendering method
    /// - On every frame or animation tick
    fn compute_groups(&mut self, data: &[(String, String)]) {
        self.group_ranges.clear();
        let mut i = 0;

        while i < data.len() {
            let current_key = &data[i].0;
            let mut count = 1;

            // Count consecutive items with same key
            while i + count < data.len() && &data[i + count].0 == current_key {
                count += 1;
            }

            // Only create groups for 3+ consecutive items
            if count >= 3 {
                let header_id = format!("{}_group_{}", current_key, i);
                let start_index = i;
                let end_index = i + count - 1;

                self.group_ranges.insert(start_index..end_index + 1, header_id.clone());
                self.groups_by_id.insert(
                    header_id,
                    GroupMeta {
                        key: current_key.clone(),
                        count,
                    },
                );
            }

            i += count;
        }
    }
}
```

### Using FoldHeader Widget

**FoldHeader** is a built-in Makepad widget that provides collapsible sections with a header and body.

#### Basic FoldHeader Structure

```rust
live_design! {
    MyFoldHeader = <FoldHeader> {
        // Header: Always visible, controls fold state
        header: <View> {
            width: Fill, height: 50
            // Add fold button and header content
            fold_button = <FoldButton> {}
        }

        // Body: Collapsible content
        body: <View> {
            width: Fill, height: Fit
            // Add body content here
        }
    }
}
```

#### Accessing FoldHeader in Code

```rust
use makepad_widgets::fold_header::FoldHeaderWidgetRefExt;

// Get a reference to a FoldHeader
let fold_header_ref = some_view.as_fold_header();

// Access nested widgets within the FoldHeader (no need to specify header/body)
let view_list_ref = fold_header_ref.view_list(ids!(my_view_list));
```

#### Programmatically Populating FoldHeader Body

When you need to dynamically generate content inside the FoldHeader body:

```rust
// 1. Get reference to FoldHeader from portal list item
let item = list.item(cx, item_id, live_id!(FoldHeader));

// 2. Set header text (no need to specify "header" prefix)
item.label(ids!(summary_text))
    .set_text(cx, &format!("Group {} ({} items)", group_name, count));

// 3. Access dummy portal list (no need to specify "body" prefix)
let mut widgetref_list = vec![];
let dummy_portal_list = item.portal_list(ids!(dummy_portal_list));

// 4. Use dummy portal list to create widget instances
if let Some(mut list_ref) = dummy_portal_list.borrow_mut() {
    let list = list_ref.deref_mut();

    // 5. Create widget instances from templates
    for (idx, data_item) in my_data_items.iter().enumerate() {
        let widget_item = list.item(cx, idx, live_id!(SmallStateEvent));
        widget_item.label(ids!(text)).set_text(cx, &data_item.text);
        widgetref_list.push(widget_item);
    }
}

// 6. Access ViewList and set widgets (no need to specify "body" prefix)
let mut view_widget = item.view_list(ids!(view_list));
view_widget.set_widgetref_list(widgetref_list);

// 7. Draw the complete FoldHeader
item.draw_all(cx, &mut Scope::empty());
```

### Using PortalList in FoldHeader Body

**PortalList** directly embedded in the FoldHeader body provides native list rendering capabilities.

#### Direct PortalList Rendering Pattern

```rust
// 1. Get FoldHeader item from the main portal list
let fold_item = list.item(cx, item_id, live_id!(FoldHeader));

// 2. Set header content (no need to specify "header" prefix)
fold_item.label(ids!(summary_text)).set_text(cx, "Group Summary");

// 3. Draw FoldHeader and access the inner PortalList
let mut walk = walk;
walk.height = Size::Fit;  // IMPORTANT: Use Fit for proper sizing
while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
    if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
        let list = list_ref.deref_mut();

        // 4. Directly render items in the portal list
        for i in 0..10 {
            let widget_item = list.item(cx, i, live_id!(ItemTemplate));

            // Populate the widget with data
            widget_item.label(ids!(title)).set_text(cx, &format!("Item {}", i));
            widget_item.button(ids!(action_btn)).set_text(cx, "Click");

            // Draw immediately
            widget_item.draw_all(cx, scope);
        }
    }
}
```

### Portal List Integration

Integrating FoldHeader with GroupHeaderManager in a portal list:

```rust
use makepad_widgets::*;
use makepad_widgets::fold_header::FoldHeaderWidgetRefExt;

#[derive(Live, Widget)]
struct MyPortalList {
    #[deref] view: View,
    #[rust] data: Vec<(String, String)>,
    #[rust] group_manager: GroupHeaderManager,
}

impl Widget for MyPortalList {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        while let Some(item) = self.view.draw_walk(cx, scope, walk).step() {
            if let Some(mut list) = item.as_portal_list().borrow_mut() {
                list.set_item_range(cx, 0, self.data.len());

                // IMPORTANT: Do NOT call compute_groups() here!
                // Groups should already be computed when data was loaded/updated

                while let Some(item_id) = list.next_visible_item(cx) {
                    // Check if this item is part of a group
                    if let Some(range) = self.group_manager.check_group_header_status(item_id) {
                        if item_id == range.start {
                            // This is the start of a group (item_id == range.start)
                            // Render FoldHeader and populate it with ALL items in the range
                            self.render_fold_header(cx, &mut list, item_id, &range);
                        } else {
                            // This item is within the range (range.start < item_id < range.end)
                            // Render Empty placeholder - content already shown in FoldHeader
                            list.item(cx, item_id, live_id!(Empty)).draw_all(cx, &mut Scope::empty());
                        }
                    } else {
                        // Normal ungrouped item (outside any range)
                        self.render_normal_item(cx, &mut list, item_id);
                    }
                }
            }
        }
        DrawStep::done()
    }
}

impl MyPortalList {
    fn render_fold_header(&mut self, cx: &mut Cx2d, scope: &mut Scope, list: &mut PortalListRef,
                          item_id: usize, range: &Range<usize>, walk: Walk) {
        // item_id == range.start when this function is called
        let group_meta = self.group_manager.get_group_at_item_id(item_id).unwrap();

        // Get FoldHeader item from portal list at range.start
        let fold_item = list.item(cx, item_id, live_id!(FoldHeader));

        // Set header summary text (no need to specify "header" prefix)
        fold_item.label(ids!(summary_text))
            .set_text(cx, &format!("{} ({} items)", group_meta.key, group_meta.count));

        // Draw the FoldHeader and access the inner PortalList
        let mut walk = walk;
        walk.height = Size::Fit;
        while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
            if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
                let list = list_ref.deref_mut();

                // Iterate through the ENTIRE range to render items directly
                for tl_idx in range.start..range.end {
                    if let Some((key, text)) = self.data.get(tl_idx) {
                        let widget_item = list.item(cx, tl_idx, live_id!(Post));
                        widget_item.label(ids!(content.text))
                            .set_text(cx, &format!("{}: {}", key, text));
                        widget_item.draw_all(cx, scope);
                    }
                }
            }
        }
    }

    fn render_normal_item(&mut self, cx: &mut Cx2d, list: &mut PortalListRef, item_id: usize) {
        if let Some((key, text)) = self.data.get(item_id) {
            let item = list.item(cx, item_id, live_id!(Post));
            item.label(ids!(content.text))
                .set_text(cx, &format!("{}: {}", key, text));
            item.draw_all(cx, &mut Scope::empty());
        }
    }
}
```

## Complete Usage Example

### Step 1: Project Setup

```toml
# Cargo.toml
[dependencies]
rangemap = "1.5"
makepad-widgets = { path = "../../widgets" }
```

```rust
// lib.rs or main.rs
pub mod fold_button_with_text;  // Custom widget (see "Custom Widgets" section)
```

### Step 2: Define live_design! Structure

```rust
live_design! {
    use link::widgets::*;
    use crate::fold_button_with_text::*;

    MyApp = <View> {
        width: Fill, height: Fill

        my_list = <PortalList> {
            width: Fill, height: Fill

            // Template for normal ungrouped items
            Post = <View> {
                width: Fill, height: 60
                padding: 10
                content = <View> {
                    text = <Label> { text: "" }
                }
            }

            // Empty placeholder for items within groups
            Empty = <View> { height: 0, show_bg: false }

            // FoldHeader for grouped items
            FoldHeader = <FoldHeader> {
                header: <View> {
                    width: Fill, height: 50
                    align: { x: 0.5, y: 0.5 }
                    fold_button = <FoldButtonWithText> {
                        open_text: "Show More"
                        close_text: "Show Less"
                    }
                    summary_text = <Label> { text: "" }
                }

                body: <View> {
                    width: Fill, height: Fit
                    flow: Down
                    // Direct PortalList for rendering grouped items
                    <PortalList> {
                        height: Fit, width: Fill
                        Post = <Post> {}  // Reuse Post template
                    }
                }
            }
        }
    }
}
```

### Step 3: Implement Widget with GroupHeaderManager

```rust
use makepad_widgets::*;
use makepad_widgets::fold_header::FoldHeaderWidgetRefExt;

#[derive(Live, Widget)]
struct MyApp {
    #[deref] view: View,
    #[rust] data: Vec<(String, String)>,
    #[rust] group_manager: GroupHeaderManager,
}

impl LiveHook for MyApp {
    fn after_new_from_doc(&mut self, _cx: &mut Cx) {
        // Initialize data with groupable keys
        self.data = vec![
            ("Category A".to_string(), "Item 1".to_string()),
            ("Category A".to_string(), "Item 2".to_string()),
            ("Category A".to_string(), "Item 3".to_string()),  // Group forms here
            ("Category B".to_string(), "Item 4".to_string()),
            ("Category C".to_string(), "Item 5".to_string()),
            ("Category C".to_string(), "Item 6".to_string()),
            ("Category C".to_string(), "Item 7".to_string()),  // Another group
        ];

        // IMPORTANT: Compute groups ONCE when data is first available
        // Do NOT call compute_groups() in draw_walk()
        self.group_manager = GroupHeaderManager::new();
        self.group_manager.compute_groups(&self.data);
    }
}

// When data changes (e.g., from network updates or user actions)
impl MyApp {
    fn handle_data_update(&mut self, new_data: Vec<(String, String)>) {
        self.data = new_data;

        // Recompute groups when data changes
        self.group_manager.compute_groups(&self.data);

        // Trigger redraw
        // self.redraw(cx);
    }
}

impl Widget for MyApp {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Standard portal list rendering with grouping logic
        // See "Portal List Integration" section for complete implementation
        // ...
        DrawStep::done()
    }
}
```

### Step 4: Understanding the Rendering Flow

When the portal list renders with grouping logic:

1. **Item ID 0-2** (Category A - forms a group):
   - `next_visible_item()` returns 0
   - Check: `item_id == range.start` (0 == 0) → TRUE
   - **Render `FoldHeader` at position 0**
   - Iterate through range (0..3) to generate widgetref_list with items 0, 1, 2
   - Call `view_list.set_widgetref_list()` to populate FoldHeader body
   - `next_visible_item()` returns 1
   - Check: 1 is within range (0..3) but not at start → Render `Empty`
   - `next_visible_item()` returns 2
   - Check: 2 is within range (0..3) but not at start → Render `Empty`

2. **Item ID 3** (Category B - not grouped):
   - `next_visible_item()` returns 3
   - Not part of any group → Render normal `Post` template

3. **Item ID 4-6** (Category C - forms a group):
   - `next_visible_item()` returns 4
   - Check: `item_id == range.start` (4 == 4) → TRUE
   - **Render `FoldHeader` at position 4**
   - Iterate through range (4..7) to generate widgetref_list with items 4, 5, 6
   - Call `view_list.set_widgetref_list()` to populate FoldHeader body
   - `next_visible_item()` returns 5
   - Check: 5 is within range (4..7) but not at start → Render `Empty`
   - `next_visible_item()` returns 6
   - Check: 6 is within range (4..7) but not at start → Render `Empty`

### Step 5: Key FoldHeader Operations

```rust
// Called when item_id == range.start
// range represents all items in the group (e.g., 0..3)

// 1. Get FoldHeader reference from portal list at range.start position
let fold_item = list.item(cx, item_id, live_id!(FoldHeader));

// 2. Set header text (no need to specify "header" prefix)
fold_item.label(ids!(summary_text))
    .set_text(cx, "Group Name (3 items)");

// 3. Draw FoldHeader and access the inner PortalList
let mut walk = walk;
walk.height = Size::Fit;
while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
    if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
        let list = list_ref.deref_mut();

        // 4. Iterate through the ENTIRE range to render items directly
        for tl_idx in range.start..range.end {
            if let Some(data) = my_data.get(tl_idx) {
                let widget_item = list.item(cx, tl_idx, live_id!(Post));
                widget_item.label(ids!(content.text)).set_text(cx, &data.text);
                widget_item.draw_all(cx, scope);
            }
        }
    }
}

// Note: When next_visible_item() later returns item_ids within the range
// (range.start < item_id < range.end), they will render as Empty widgets
```

## When to Use

- News feeds or social media feeds grouped by topic/author
- Message lists grouped by conversation thread
- File browsers grouped by directory or file type
- E-commerce catalogs grouped by category
- Event lists grouped by date or location
- Any scrollable list where consecutive identical keys indicate natural groupings

## When NOT to Use

- When items don't have natural grouping keys
- When groups are expected to be smaller than 3 items (configure threshold)
- When you need groups to persist across non-consecutive items
- When manual grouping control is required

## Key Concepts

### Custom Widget Extensions

The pattern uses a custom helper widget (`FoldButtonWithText`) that extends the standard Makepad `FoldButton` widget with domain-specific functionality:

- **Alternative**: You can use the standard `FoldButton` widget instead of `FoldButtonWithText` if dynamic text labels aren't needed
- **Reusability**: The custom widget can be reused in other contexts beyond this pattern

**Important Note on FoldButtonWithText**: This custom widget MUST use `makepad_widgets::fold_button::FoldButtonAction` for its action events. Do not create a custom `FoldButtonAction` enum. Using the standard action type ensures proper integration with FoldHeader and the broader Makepad widget system.

### The Direct PortalList Pattern Explained

The "direct PortalList" pattern uses a real PortalList directly inside the FoldHeader body:

**Why Use Direct PortalList Instead of ViewList?**
- No need for intermediate ViewList widget or dummy portal list
- Portal lists provide native virtualization and scroll handling
- Simpler architecture with fewer custom components
- Built-in support for `height: Fit` to automatically size to content

**How It Works:**
1. Define a PortalList with `height: Fit` inside the FoldHeader body
2. Use `fold_item.draw_walk()` to step through and access the inner PortalList
3. Use `item.as_portal_list()` to get a mutable reference to the PortalList
4. Directly render items using `list.item()` and `item.draw_all()`

**Benefits:**
- **Simpler**: No intermediate widgets or WidgetRef collection
- **Native Features**: Full portal list capabilities (virtualization, scrolling)
- **Better Performance**: Direct rendering without overhead
- **Height: Fit**: Automatic content sizing
- **Less Code**: Eliminates ViewList widget implementation

### RangeMap for Efficient Lookups

The pattern uses `RangeMap<usize, String>` to efficiently map item indices to group IDs. This allows O(log n) lookup to check if an item belongs to a group.

### Three Rendering Modes

The portal list rendering logic handles three cases based on the item's position:

1. **Group Header** (`item_id == range.start`):
   - Renders a `FoldHeader` widget at this position
   - Iterates through the **entire range** (from `range.start` to `range.end`) to generate `widgetref_list`
   - Calls `view_list.set_widgetref_list()` to populate the FoldHeader body with all grouped items
   - This single FoldHeader contains all items in the group

2. **Empty Placeholder** (`range.start < item_id < range.end`):
   - When `next_visible_item()` returns an `item_id` within the range (but not at start)
   - Renders `Empty` widget with 0 height
   - Content already displayed in the FoldHeader, so these items are hidden

3. **Normal Item** (outside range):
   - Renders regular item template
   - Not part of any group

### Threshold Configuration

The default threshold is 3 consecutive items. Adjust this based on your use case:

```rust
if count >= 3 {  // Change to >= 2 or >= 4 as needed
    // Create group
}
```

### Performance Considerations

1. **Caching Group Metadata**: Pre-compute summaries and avatar lists to avoid recalculation during rendering
2. **RangeMap Efficiency**: O(log n) lookups for checking if an item belongs to a group
3. **Empty Placeholders**: Items within a group render as 0-height views, minimal overhead
4. **Lazy Widget Creation**: Widgets in collapsed FoldHeaders aren't created until expanded
5. **Compute Groups ONLY When Data Changes**: **CRITICAL** - Never call `compute_groups()` during `draw_walk()`

#### ❌ WRONG: Computing Groups During Rendering

```rust
impl Widget for MyPortalList {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // ❌ WRONG: This recomputes groups on EVERY FRAME
        self.group_manager.compute_groups(&self.data);

        // ... rendering logic
    }
}
```

#### ✅ CORRECT: Computing Groups When Data Changes

```rust
impl LiveHook for MyApp {
    fn after_new_from_doc(&mut self, _cx: &mut Cx) {
        self.data = load_initial_data();

        // ✅ CORRECT: Compute once when data is first available
        self.group_manager.compute_groups(&self.data);
    }
}

impl MyApp {
    fn handle_data_update(&mut self, new_data: Vec<Item>) {
        self.data = new_data;

        // ✅ CORRECT: Recompute when data changes
        self.group_manager.compute_groups(&self.data);
    }
}

impl Widget for MyApp {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // ✅ CORRECT: Only READ group data during rendering
        if let Some(range) = self.group_manager.check_group_header_status(item_id) {
            // Use pre-computed group data
        }
    }
}
```

#### Caching Expensive Computations

```rust
// Good: Cache expensive computations when groups are created
impl SmallStateGroup {
    pub fn update_cached_data(&mut self) {
        self.cached_summary = Some(generate_summary(&self.user_events_map, SUMMARY_LENGTH));
        self.cached_avatar_user_ids = Some(extract_avatar_user_ids(&self.user_events_map, MAX_VISIBLE_AVATARS));
    }
}

// Use cached data during rendering (no "header" prefix needed)
if let Some(summary) = &group.cached_summary {
    fold_item.label(ids!(summary_text)).set_text(cx, summary);
}
```

## Related Patterns

- [Pattern 3: Collapsible Widget](./_base/03-collapsible.md) - Basic collapsible behavior
- [Pattern 4: List with Template](./_base/04-list-template.md) - Dynamic list rendering
- [Pattern 5: LRU View Cache](./_base/05-lru-view-cache.md) - Performance optimization for large lists

## API Reference

### FoldHeader Widget

**Import**: `use makepad_widgets::fold_header::FoldHeaderWidgetRefExt;`

**Core Methods**:
```rust
// Access nested widgets within FoldHeader
// Note: No need to specify "header" or "body" prefixes
fn label(&self, path: &[LiveId]) -> LabelRef
fn button(&self, path: &[LiveId]) -> ButtonRef

// Draw the FoldHeader and get access to body widgets
fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep

// Example usage
fold_item.label(ids!(summary_text))  // Not ids!(header.summary_text)

// Access inner PortalList during draw_walk
while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
    if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
        // Access the PortalList inside the FoldHeader body
    }
}
```

**Structure in live_design!**:
```rust
<FoldHeader> {
    header: <View> {
        // Always visible header content
        // Must include a fold button (FoldButton or FoldButtonWithText)
    }
    body: <View> {
        // Collapsible body content with direct PortalList
        <PortalList> {
            height: Fit, width: Fill
            // Templates for items
        }
    }
}
```

### PortalList in FoldHeader Body

**Built-in Makepad widget** used directly inside FoldHeader body.

**Core Methods**:
```rust
// Access PortalList during FoldHeader draw_walk
item.as_portal_list().borrow_mut()

// Render items in the PortalList
list.item(cx, index, template_id)
```

**Structure in live_design!**:
```rust
body: <View> {
    width: Fill, height: Fit
    flow: Down
    <PortalList> {
        height: Fit, width: Fill  // IMPORTANT: Use Fit not 0
        ItemTemplate = <ItemView> {}
    }
}
```

**Note**: The PortalList uses `height: Fit` to automatically size to its content, not `height: 0` like the old dummy portal list pattern.

### GroupHeaderManager

**Custom utility struct** - see "GroupHeaderManager" section for implementation.

**Core Methods**:
```rust
// Check if item_id is part of a group, returns the full range
// Called during draw_walk() - fast O(log n) lookup
pub fn check_group_header_status(&self, item_id: usize) -> Option<Range<usize>>

// Get metadata for group starting at item_id
// Called during draw_walk() - fast lookup
pub fn get_group_at_item_id(&self, item_id: usize) -> Option<&GroupMeta>

// Compute groups from data
// IMPORTANT: Call ONLY when data is first available or changes
// DO NOT call during draw_walk() - would recompute on every frame!
pub fn compute_groups(&mut self, data: &[(String, String)])
```

**When to Call `compute_groups()`**:
- ✅ In `after_new_from_doc()` after loading initial data
- ✅ When receiving new data from network/updates
- ✅ In response to user actions that modify data
- ❌ **NEVER** in `draw_walk()` or any rendering method
- ❌ **NEVER** on every frame or animation tick

### Portal List Integration Pattern

```rust
while let Some(item_id) = list.next_visible_item(cx) {
    if let Some(range) = group_manager.check_group_header_status(item_id) {
        if item_id == range.start {
            // item_id == range.start: Render FoldHeader
            // Inside render function:
            // - Iterate through range.start..range.end
            // - Generate widgetref_list for all items in range
            // - Call view_list.set_widgetref_list(widgetref_list)
        } else {
            // range.start < item_id < range.end: Render Empty
            // Content already shown in FoldHeader
        }
    } else {
        // Outside any range: Render normal item
    }
}
```

## External Dependencies

- **RangeMap**: https://docs.rs/rangemap/ - Efficient range-to-value mapping for O(log n) group lookups
- **Makepad Widgets**: Built-in FoldHeader widget and portal list infrastructure

## Real-World Example: Small State Event Grouping (Robrix)

The Robrix Matrix client uses this pattern to group consecutive small state events (membership changes, profile updates, etc.) in chat room timelines. Here's a simplified version of the implementation:

### SmallStateGroupManager (Based on GroupHeaderManager pattern)

```rust
use rangemap::RangeMap;
use std::collections::HashMap;

#[derive(Debug, Default, Clone)]
pub struct SmallStateGroup {
    pub user_events_map: HashMap<OwnedUserId, Vec<UserEvent>>,
    pub cached_summary: Option<String>,
    pub cached_avatar_user_ids: Option<Vec<OwnedUserId>>,
}

#[derive(Default, Debug)]
pub struct SmallStateGroupManager {
    pub small_state_groups: RangeMap<usize, OwnedEventId>,
    pub groups_by_event_id: HashMap<OwnedEventId, SmallStateGroup>,
}

impl SmallStateGroupManager {
    pub fn check_group_range(&self, item_id: usize) -> Option<std::ops::Range<usize>> {
        self.small_state_groups.get_key_value(&item_id)
            .map(|(range, _)| range.clone())
    }

    pub fn get_group_at_item_id(&self, item_id: usize) -> Option<&SmallStateGroup> {
        self.small_state_groups
            .iter()
            .find(|(range, _)| range.start == item_id)
            .and_then(|(_, event_id)| self.groups_by_event_id.get(event_id))
    }

    /// Computes group state from small state events.
    ///
    /// **IMPORTANT**: Call this ONLY when timeline data is first loaded or updated.
    /// DO NOT call during draw_walk() rendering.
    pub fn compute_group_state(&mut self, small_state_events: Vec<UserEvent>) {
        // Clear existing groups
        self.small_state_groups.clear();
        self.groups_by_event_id.clear();

        // Group consecutive events with same characteristics
        // (See full implementation in PR for details)
    }
}
```

### When to Compute Groups

```rust
// ✅ CORRECT: Compute groups when timeline data is loaded or updated
impl RoomScreen {
    fn process_timeline_updates(&mut self, timeline_update: TimelineUpdate) {
        match timeline_update {
            TimelineUpdate::InitialItems { initial_items } => {
                tl.items = initial_items;

                // Compute groups ONCE when data is first available
                let small_state_events = extract_small_state_events(tl.items.iter().cloned());
                tl.small_state_group_manager.compute_group_state(small_state_events);
            }
            TimelineUpdate::NewItems { new_items, .. } => {
                tl.items = new_items;

                // Recompute groups when data changes
                let small_state_events = extract_small_state_events(tl.items.iter().cloned());
                tl.small_state_group_manager.compute_group_state(small_state_events);
            }
        }
    }
}
```

### Integration in RoomScreen Portal List

```rust
// ❌ DO NOT compute groups here - this is called every frame!
// ✅ Groups should already be computed when data was loaded

// In the portal list draw loop
while let Some(item_id) = list.next_visible_item(cx) {
    // Check if this item is part of a group (fast O(log n) lookup)
    if let Some(group_range) = tl_state.small_state_group_manager.check_group_range(item_id) {
        if item_id == group_range.start {
            // item_id == range.start: Render FoldHeader
            // This FoldHeader will contain ALL items in the range
            if let Some(group) = tl_state.small_state_group_manager.get_group_at_item_id(item_id) {
                let item = populate_small_state_group_header(
                    cx,
                    list,
                    item_id,
                    room_id,
                    &group_range,  // Pass the full range
                    group,
                    tl_items,
                    // ... other parameters
                );
                item.draw_all(cx, scope);
            }
            continue;
        } else if group_range.contains(&item_id) {
            // range.start < item_id < range.end: Render Empty
            // Content already displayed in the FoldHeader at range.start
            let item = list.item(cx, item_id, id!(Empty));
            item.draw_all(cx, scope);
            continue;
        }
    }

    // Normal ungrouped item rendering (outside any range)
    // ...
}
```

### Populating the FoldHeader with Small State Events

```rust
fn populate_small_state_group_header(
    cx: &mut Cx2d,
    scope: &mut Scope,
    walk: Walk,
    list: &mut PortalList,
    item_id: usize,
    room_id: &OwnedRoomId,
    group_range: &std::ops::Range<usize>,
    group: &SmallStateGroup,
    tl_items: &imbl::Vector<Arc<TimelineItem>>,
    // ... other parameters
) {
    // Get the FoldHeader item from portal list
    let (fold_item, _existed) = list.item_with_existed(cx, item_id, id!(SmallStateGroupHeader));

    // Set the header summary text from cached data (no "header" prefix needed)
    if let Some(summary) = &group.cached_summary {
        fold_item.label(ids!(summary_text)).set_text(cx, summary);
    }

    // Set the avatars in the header from cached user IDs (no "header" prefix needed)
    if let Some(user_ids) = &group.cached_avatar_user_ids {
        populate_avatar_row_from_user_ids(cx, &fold_item, room_id, user_ids);
    }

    // Draw the FoldHeader and access the inner PortalList
    let mut walk = walk;
    walk.height = Size::fit();  // IMPORTANT: Use Fit for proper sizing
    while let Some(item) = fold_item.draw_walk(cx, scope, walk).step() {
        if let Some(mut list_ref) = item.as_portal_list().borrow_mut() {
            let list = list_ref.deref_mut();

            // Directly render SmallStateEvent widgets for each item in the group range
            for tl_idx in (group_range.start)..group_range.end {
                if let Some(timeline_item) = tl_items.get(tl_idx) {
                    if let TimelineItemKind::Event(event_tl_item) = timeline_item.kind() {
                        // Create and draw appropriate widget based on event type
                        let (item, item_drawn_status) = match event_tl_item.content() {
                            TimelineItemContent::MembershipChange(membership_change) =>
                                populate_small_state_event(cx, list, tl_idx, room_id, event_tl_item, membership_change, item_drawn_status),
                            TimelineItemContent::ProfileChange(profile_change) =>
                                populate_small_state_event(cx, list, tl_idx, room_id, event_tl_item, profile_change, item_drawn_status),
                            // ... handle other event types
                            _ => (list.item_with_existed(cx, tl_idx, id!(Empty)).0, item_drawn_status)
                        };

                        // Draw the item immediately
                        item.draw_all(cx, scope);
                    }
                }
            }
        }
    }
}
```

### Live Design Structure

```rust
live_design! {
    SmallStateGroupHeader = <FoldHeader> {
        // Header: Always visible, shows summary and fold button
        header: <View> {
            width: Fill, height: Fit
            padding: { left: 7.0, top: 2.0, bottom: 2.0 }
            flow: Down, spacing: 7.0

            <View> {
                width: Fill, height: Fit
                user_event_avatar_row = <AvatarRow> {
                    margin: { left: 10.0 }
                }
                summary_text = <Label> {
                    width: Fill, height: Fit
                    draw_text: {
                        wrap: Word
                        text_style: <THEME_FONT_REGULAR> {
                            font_size: (SMALL_STATE_FONT_SIZE)
                        }
                    }
                }
            }

            <View> {
                width: Fill, height: Fit
                flow: Right, align: {x: 0.5, y: 0.5}
                fold_button = <FoldButtonWithText> {
                    open_text: "Show More"
                    close_text: "Show Less"
                }
            }
        }

        // Body: Collapsible content with direct PortalList
        body: <View> {
            width: Fill, height: Fit, flow: Down

            // Direct PortalList for rendering grouped items
            <PortalList> {
                height: Fit, width: Fill
                SmallStateEvent = <SmallStateEvent> {}
                CondensedMessage = <CondensedMessage> {}
                Message = <Message> {}
            }
        }
    }
}
```

### Key Benefits in This Use Case

1. **Reduced Visual Clutter**: Consecutive membership changes (joins/leaves) are collapsed into a single expandable summary
2. **Performance**: Only visible items are rendered, and group metadata is cached
3. **User Experience**: Users can expand groups to see details when needed
4. **Automatic Grouping**: Groups are computed automatically based on timeline data changes
```

## File: `skills/robius-widget-patterns/_base/22-dropdown-overlay.md`
```markdown
---
name: dropdown-overlay
author: makepad
source: makepad-widgets
date: 2026-01-19
tags: [dropdown, popup, overlay, drawlist2d, fold-header]
level: intermediate
---

# Dropdown Popup That Does Not Change Widget Area

Create dropdown popups that float over other content without affecting the parent layout.

## Problem

When a widget has expandable content (like a dropdown body), drawing that content inline within the widget's turtle causes it to push surrounding layout elements. The widget's total area grows to include the expanded content.

## Solution

Use a `DrawList2d` overlay to draw the popup content in a separate layer that doesn't participate in the parent's layout system.

## Two Approaches Compared

### Approach 1: Inline Body (FoldHeader) -- Body DOES change widget area

`widgets/src/fold_header.rs:91-119`

```
Outer Turtle (walk, layout)
  +-- Header (drawn inline)
  +-- Body Turtle (body_walk, with scroll offset)
        +-- Body content
End Body Turtle    <-- takes up space in outer turtle
End Outer Turtle   <-- total area = header + body
```

The body is drawn inside the same turtle hierarchy as the header. The outer turtle's used size includes the body, so surrounding widgets are pushed down.

The scroll trick `Layout::flow_down().with_scroll(dvec2(0.0, rect_size * (1.0 - opened)))` slides the body in/out during animation, but it still occupies layout space in the parent.

### Approach 2: Overlay Body (FoldHeaderDropDown) -- Body does NOT change widget area

`widgets/src/fold_header_dropdown.rs:91-126`

```
Outer Turtle (walk, layout)
  +-- Header (drawn inline)
  +-- [Body turtle started but body drawn elsewhere]

--- Separate overlay layer ---
DrawList2d overlay
  +-- Root Turtle (full pass size)
        +-- Body content (shifted to header position)
```

The body is drawn in a **separate overlay draw list**, not inside the widget's own turtle. The widget's area is only the header. The body floats on top of everything.

## Implementation

### 1. Add a `DrawList2d` field to your struct

```rust
#[derive(Live, LiveHook, Widget)]
pub struct MyDropdownWidget {
    #[deref] view: View,
    #[live] header: View,
    #[live] body: View,
    #[live] draw_list: DrawList2d,  // enables overlay drawing
    #[rust] is_open: bool,
    #[rust] area: Area,
}
```

`DrawList2d` is a separate draw list that can be registered as an overlay, meaning its contents render on top of the normal widget tree without participating in the parent's layout.

### 2. Draw the popup body in an overlay, not in the widget's turtle

From `fold_header_dropdown.rs:111-123`:

```rust
// Step 1: Begin the overlay draw list
self.draw_list.begin_overlay_reuse(cx);

// Step 2: Create a root turtle covering the entire pass (screen)
let size = cx.current_pass_size();
cx.begin_root_turtle(size, Layout::flow_down());

// Step 3: Draw your popup content
let _ = self.body.draw_walk(cx, scope, walk);

// Step 4: End the root turtle, shifting content to desired position
let shift = DVec2 { x: header_area.pos.x, y: header_area.size.y + header_area.pos.y };
cx.end_pass_sized_turtle_with_shift(self.area, shift);

// Step 5: End the overlay draw list
self.draw_list.end(cx);
```

### 3. Compute the shift to position the overlay relative to the trigger

`end_pass_sized_turtle_with_shift(area, shift)` positions all content drawn inside the root turtle relative to `area.pos + shift`.

In FoldHeaderDropDown (`fold_header_dropdown.rs:121`):

```rust
let header_area = self.header.area().rect(cx);
let shift = DVec2 {
    x: header_area.pos.x,                          // align horizontally with header
    y: header_area.size.y + header_area.pos.y       // place below header
};
cx.end_pass_sized_turtle_with_shift(self.area, shift);
```

The first argument (`self.area`) is the **reference area** -- the overlay is positioned relative to this area's position. The second argument (`shift`) is an additional offset applied on top.

## Complete Pattern

```rust
fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
    // 1. Draw the trigger/header normally (this determines widget area)
    cx.begin_turtle(walk, self.layout);
    let header_walk = self.header.walk(cx);
    self.header.draw_walk(cx, scope, header_walk)?;
    cx.end_turtle_with_area(&mut self.area);

    // 2. If open, draw body in overlay (does NOT affect widget area)
    if self.is_open {
        self.draw_list.begin_overlay_reuse(cx);
        cx.begin_root_turtle(cx.current_pass_size(), Layout::flow_down());

        // draw popup content here
        let _ = self.body.draw_walk(cx, scope, body_walk);

        // position relative to trigger
        let trigger_rect = self.area.rect(cx);
        let shift = DVec2 { x: 0.0, y: trigger_rect.size.y };
        cx.end_pass_sized_turtle_with_shift(self.area, shift);
        self.draw_list.end(cx);
    }

    DrawStep::done()
}
```

## Side-by-Side Comparison

| | FoldHeader (inline) | FoldHeaderDropDown (overlay) |
|---|---|---|
| Body drawn in | Widget's own turtle | Separate `DrawList2d` overlay |
| Widget area | Header + Body | Header only |
| Pushes siblings | Yes | No |
| Extra field needed | None | `DrawList2d` |
| Positioning | Automatic (flow layout) | Manual (shift calculation) |
| Body turtle | `begin_turtle` / `end_turtle` inside outer | `begin_root_turtle` / `end_pass_sized_turtle_with_shift` in overlay |

## Key Rules

1. **Always close what you open.** `begin_overlay_reuse` must pair with `draw_list.end`. `begin_root_turtle` must pair with `end_pass_sized_turtle_with_shift` or `end_pass_sized_turtle`. Close them even if there is nothing to draw.

2. **The overlay root turtle covers the full pass.** Use `cx.current_pass_size()` so the overlay has the entire screen to position content in.

3. **Shift is relative to the reference area.** `end_pass_sized_turtle_with_shift(ref_area, shift)` places content at `ref_area.pos + shift`. To place a dropdown below its trigger, use `shift.y = trigger_height`.

4. **The widget's own area is determined only by non-overlay content.** Whatever you draw before the overlay block determines the widget's footprint in the parent layout. The overlay content is invisible to the parent's layout system.

## live_design! Example

```rust
live_design! {
    use link::widgets::*;

    MyDropdown = {{MyDropdown}} {
        width: Fit, height: Fit

        header: <View> {
            width: 200, height: 40
            show_bg: true
            draw_bg: { color: #333 }

            <Label> { text: "Click to expand" }
            <Icon> {
                draw_icon: { svg_file: dep("crate://self/icons/chevron-down.svg") }
            }
        }

        body: <View> {
            width: 200, height: Fit
            show_bg: true
            draw_bg: { color: #444 }
            padding: 10

            <Label> { text: "Dropdown content here" }
            <Button> { text: "Option 1" }
            <Button> { text: "Option 2" }
        }
    }
}
```

## When to Use

- Dropdown menus that should float over other content
- Autocomplete suggestions
- Context menus
- Tooltips that shouldn't push content
- Any expandable content that should overlay rather than push

## When NOT to Use

- Accordion-style collapsible sections where you WANT content to push down
- Inline expandable cards
- Tree view nodes where children should be part of the flow

## Related Patterns

- [Pattern 2: Modal Overlay](./02-modal-overlay.md) - Full-screen modal dialogs
- [Pattern 3: Collapsible Widget](./03-collapsible.md) - Inline collapsible sections
- [Pattern 14: Callout Tooltip](./14-callout-tooltip.md) - Positioned tooltips with arrows

## API Reference

### DrawList2d

**Import**: Built into makepad-widgets

**Key Methods**:
```rust
// Begin drawing in overlay mode (reuses existing draw list if available)
fn begin_overlay_reuse(&mut self, cx: &mut Cx2d)

// End the draw list
fn end(&mut self, cx: &mut Cx2d)
```

### Turtle Methods

**Key Methods**:
```rust
// Start a root turtle covering the full pass size
fn begin_root_turtle(&mut self, size: DVec2, layout: Layout)

// End turtle and position content relative to area + shift
fn end_pass_sized_turtle_with_shift(&mut self, area: Area, shift: DVec2)

// Get current pass (screen) size
fn current_pass_size(&self) -> DVec2
```

### Positioning

```rust
// Position dropdown below header
let header_rect = self.header.area().rect(cx);
let shift = DVec2 {
    x: 0.0,                    // same x as widget
    y: header_rect.size.y      // directly below header
};

// Position dropdown above header (menu opening upward)
let shift = DVec2 {
    x: 0.0,
    y: -body_height            // negative y to go above
};

// Position to the right of header
let shift = DVec2 {
    x: header_rect.size.x,     // right edge of header
    y: 0.0
};
```
```

## File: `skills/robius-widget-patterns/references/moly-widget-patterns.md`
```markdown
# Moly Widget Patterns

Additional widget patterns from Moly codebase.

## Slot Widget Pattern

A wrapper widget whose content can be replaced at runtime:

```rust
live_design! {
    use link::theme::*;
    use link::widgets::*;

    pub Slot = {{Slot}} {}
}

/// A wrapper widget whose content can be replaced from Rust.
#[derive(Live, Widget)]
pub struct Slot {
    #[wrap]
    wrap: WidgetRef,

    /// The default content defined in DSL
    #[live]
    default: WidgetRef,
}

impl Widget for Slot {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        self.wrap.draw_walk(cx, scope, walk)
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.wrap.handle_event(cx, event, scope)
    }
}

impl LiveHook for Slot {
    fn after_new_from_doc(&mut self, _cx: &mut Cx) {
        self.wrap = self.default.clone();
    }
}

impl Slot {
    /// Replace the current widget with a new one.
    pub fn replace(&mut self, widget: WidgetRef) {
        self.wrap = widget;
    }

    /// Restore the default/original widget.
    pub fn restore(&mut self) {
        self.wrap = self.default.clone();
    }

    /// Get the current widget.
    pub fn current(&self) -> WidgetRef {
        self.wrap.clone()
    }
}

// Usage in DSL:
live_design! {
    ChatLine = <View> {
        content = <Slot> {
            default: <StandardMessageContent> {}
        }
    }
}

// Runtime replacement:
let slot = self.slot(ids!(content));
slot.replace(custom_widget);  // Replace with custom
slot.restore();               // Restore to default
```

## Conditional Root Wrapper Pattern

Prevent rendering until state is ready:

```rust
#[derive(Live, Widget, LiveHook)]
pub struct MolyRoot {
    #[deref]
    view: View,
}

impl Widget for MolyRoot {
    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {
        // Don't render if Store isn't loaded
        if scope.data.get::<Store>().is_none() {
            return DrawStep::done();
        }
        self.view.draw_walk(cx, scope, walk)
    }

    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        // Don't handle events if Store isn't loaded
        if scope.data.get::<Store>().is_none() {
            return;
        }
        self.view.handle_event(cx, event, scope);
    }
}

// Usage in App:
live_design! {
    App = {{App}} {
        ui: <Window> {
            body = {
                flow: Overlay

                // Loading view shown first
                loading_view = <View> {
                    <Label> { text: "Loading..." }
                }

                // Root only renders when ready
                root = {{MolyRoot}} {
                    // Main app content
                }
            }
        }
    }
}
```

## AdaptiveView Pattern

Responsive layouts for different screen sizes:

```rust
live_design! {
    App = {{App}} {
        ui: <Window> {
            body = {
                root = <View> {
                    root_adaptive_view = <AdaptiveView> {
                        Mobile = {
                            application_pages = <ApplicationPages> {
                                margin: 0  // Full width on mobile
                            }
                        }

                        Desktop = {
                            sidebar_menu = <SidebarMenu> {}
                            application_pages = <ApplicationPages> {
                                margin: {top: 12, right: 12, bottom: 12}
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Chat Line Variants Pattern

Different styled variants for message types:

```rust
live_design! {
    // Base chat line
    pub ChatLine = <RoundedView> {
        flow: Down,
        height: Fit,
        margin: {left: 10, right: 10}

        message_section = <RoundedView> {
            sender = <Sender> {}
            content_section = <View> {
                content = <Slot> { default: <StandardMessageContent> {} }
            }
        }
        actions_section = <View> {
            actions = <Actions> { visible: false }
        }
    }

    // User message variant
    pub UserLine = <ChatLine> {
        message_section = {
            sender = {
                avatar = {
                    grapheme = {
                        draw_bg: { color: #008F7E }
                    }
                }
            }
        }
    }

    // Bot message variant
    pub BotLine = <ChatLine> {}

    // Loading state variant
    pub LoadingLine = <BotLine> {
        message_section = {
            content_section = <View> {
                loading = <MessageLoading> {}
            }
        }
    }

    // Error variant
    pub ErrorLine = <ChatLine> {
        message_section = {
            draw_bg: {color: #f003}
        }
    }

    // System message variant
    pub SystemLine = <ChatLine> {
        message_section = {
            draw_bg: {color: #e3f2fd}
            sender = {
                name = {text: "System"}
            }
        }
    }
}
```

## CommandTextInput Pattern

Text input with attached action buttons:

```rust
live_design! {
    pub PromptInput = {{PromptInput}} <CommandTextInput> {
        send_icon: dep("crate://self/resources/send.svg"),
        stop_icon: dep("crate://self/resources/stop.svg"),

        persistent = {
            center = {
                left = {
                    attach = <Button> { visible: false }
                }
                text_input = {
                    empty_text: "Start typing...",
                }
                right = {
                    audio = <Button> { visible: false }
                    submit = <Button> {
                        // Circular submit button
                    }
                }
            }
            bottom = {
                attachments = <AttachmentList> {}
            }
        }
    }
}

#[derive(Live, Widget)]
pub struct PromptInput {
    #[deref]
    deref: CommandTextInput,

    #[live]
    pub send_icon: LiveValue,

    #[live]
    pub stop_icon: LiveValue,

    #[rust]
    pub task: Task,  // Send or Stop

    #[rust]
    pub interactivity: Interactivity,

    #[rust]
    pub bot_capabilities: Option<BotCapabilities>,
}

impl PromptInput {
    fn update_button_visibility(&mut self, cx: &mut Cx) {
        let can_attach = self.bot_capabilities
            .as_ref()
            .map(|c| c.accepts_images())
            .unwrap_or(false);

        self.button(ids!(attach)).set_visible(cx, can_attach);
    }
}
```

## Popup Notification Pattern

Global popup notifications:

```rust
live_design! {
    App = {{App}} {
        ui: <Window> {
            body = {
                flow: Overlay

                // Main content
                main_content = <View> { }

                // Popups overlay
                download_popup = <PopupNotification> {
                    content: {
                        popup_download_notification = <DownloadNotificationPopup> {}
                    }
                }

                server_popup = <PopupNotification> {
                    content: {
                        popup_server = <ServerPopup> {}
                    }
                }
            }
        }
    }
}

// Opening/closing popups from actions:
if let ServerPopupAction::CloseButtonClicked = action.cast() {
    self.ui.popup_notification(id!(server_popup)).close(cx);
}

if let ServerAction::Unreachable = action.cast() {
    self.ui.popup_notification(id!(server_popup)).open(cx);
}
```

## Sidebar Navigation Pattern

Tab-based navigation with radio buttons:

```rust
live_design! {
    SidebarMenu = <RoundedView> {
        width: 90, height: Fill,
        flow: Down, spacing: 15.0,
        padding: { top: 40, bottom: 20 },
        align: {x: 0.5, y: 0.5},

        logo = <Image> { }

        chat_tab = <SidebarMenuButton> {
            animator: {active = {default: on}}
            text: "Chat",
        }
        settings_tab = <SidebarMenuButton> {
            text: "Settings",
        }

        <HorizontalFiller> {}

        providers_tab = <SidebarMenuButton> {
            text: "Providers",
        }
    }
}

// Handle tab selection:
impl App {
    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions) {
        let radio_set = self.ui.radio_button_set(ids!(
            sidebar_menu.chat_tab,
            sidebar_menu.settings_tab,
            sidebar_menu.providers_tab,
        ));

        if let Some(selected) = radio_set.selected(cx, actions) {
            match selected {
                0 => self.navigate_to(cx, id!(chat_frame)),
                1 => self.navigate_to(cx, id!(settings_frame)),
                2 => self.navigate_to(cx, id!(providers_frame)),
                _ => {}
            }
        }
    }

    fn navigate_to(&mut self, cx: &mut Cx, target: &[LiveId]) {
        // Hide all frames
        self.ui.widget(id!(chat_frame)).set_visible(cx, false);
        self.ui.widget(id!(settings_frame)).set_visible(cx, false);
        self.ui.widget(id!(providers_frame)).set_visible(cx, false);

        // Show target frame
        self.ui.widget(target).set_visible(cx, true);
    }
}
```
```

## File: `skills/robius-widget-patterns/references/styling-patterns.md`
```markdown
# Styling Patterns Reference

Dynamic styling patterns in Makepad.

## apply_over Usage

```rust
// Apply color
self.view(ids!(bg)).apply_over(cx, live! {
    draw_bg: { color: #ff0000 }
});

// Apply multiple properties
self.view(ids!(content)).apply_over(cx, live! {
    padding: { left: 20, right: 20, top: 10, bottom: 10 }
    margin: { left: 5 }
});

// Apply with Rust variables
let color = if is_active { vec4(1.0, 0.0, 0.0, 1.0) } else { vec4(0.5, 0.5, 0.5, 1.0) };
let padding = if is_compact { 5.0 } else { 15.0 };

self.view(ids!(item)).apply_over(cx, live! {
    draw_bg: { color: (color) }
    padding: (padding)
});
```

## Shader Uniforms

Define custom shader uniforms:

```rust
live_design! {
    MyView = <View> {
        show_bg: true,
        draw_bg: {
            uniform highlight: 0.0
            uniform border_color: #000

            fn pixel(self) -> vec4 {
                let base_color = mix(#fff, #fafafa, self.highlight);
                // Use uniforms in shader
                return base_color
            }
        }
    }
}

// Update uniform at runtime
self.view(ids!(my_view)).apply_over(cx, live! {
    draw_bg: { highlight: 1.0 }
});
```

## Animator for Transitions

```rust
live_design! {
    MyWidget = {{MyWidget}} {
        animator: {
            highlight = {
                default: off
                off = {
                    redraw: true,
                    from: { all: Forward {duration: 2.0} }
                    ease: ExpDecay {d1: 0.80, d2: 0.97}
                    apply: { draw_bg: {highlight: 0.0} }
                }
                on = {
                    redraw: true,
                    from: { all: Forward {duration: 0.5} }
                    ease: ExpDecay {d1: 0.80, d2: 0.97}
                    apply: { draw_bg: {highlight: 1.0} }
                }
            }
            hover = {
                default: off
                off = {
                    redraw: true,
                    from: { all: Snap }
                    apply: { draw_bg: {hover: 0.0} }
                }
                on = {
                    redraw: true,
                    from: { all: Snap }
                    apply: { draw_bg: {hover: 1.0} }
                }
            }
        }
    }
}

impl MyWidget {
    fn highlight(&mut self, cx: &mut Cx) {
        self.animator_play(cx, id!(highlight.on));
    }

    fn unhighlight(&mut self, cx: &mut Cx) {
        self.animator_play(cx, id!(highlight.off));
    }
}
```

## Conditional Styling

```rust
impl MyWidget {
    fn update_style(&mut self, cx: &mut Cx) {
        // Based on state
        let (bg_color, text_color) = match self.state {
            State::Normal => (vec4(1.0, 1.0, 1.0, 1.0), vec4(0.0, 0.0, 0.0, 1.0)),
            State::Selected => (vec4(0.9, 0.95, 1.0, 1.0), vec4(0.0, 0.0, 0.8, 1.0)),
            State::Disabled => (vec4(0.9, 0.9, 0.9, 1.0), vec4(0.5, 0.5, 0.5, 1.0)),
        };

        self.view(ids!(container)).apply_over(cx, live! {
            draw_bg: { color: (bg_color) }
        });

        self.label(ids!(text)).apply_over(cx, live! {
            draw_text: { color: (text_color) }
        });
    }
}
```

## Size and Layout

```rust
// Dynamic sizing
let width = if is_expanded { 300.0 } else { 100.0 };
self.view(ids!(panel)).apply_over(cx, live! {
    width: (width)
});

// Fit vs Fill
self.view(ids!(content)).apply_over(cx, live! {
    width: Fill,
    height: Fit,
});

// Absolute positioning (in Overlay flow)
let pos_x = 100.0;
let pos_y = 50.0;
self.view(ids!(popup)).apply_over(cx, live! {
    margin: { left: (pos_x), top: (pos_y) }
});
```

## Theme-Aware Colors

```rust
// Define theme colors in styles
live_design! {
    // In styles.rs
    COLOR_PRIMARY = #1a73e8
    COLOR_BG = #ffffff
    COLOR_TEXT = #202124
    COLOR_SECONDARY = #5f6368

    // Use in widgets
    MyButton = <Button> {
        draw_bg: { color: (COLOR_PRIMARY) }
        draw_text: { color: #fff }
    }
}
```

## Mentions Bar Pattern

Custom shader for side indicator:

```rust
live_design! {
    Message = <View> {
        show_bg: true
        draw_bg: {
            instance mentions_bar_color: #ffffff
            instance mentions_bar_width: 4.0

            fn pixel(self) -> vec4 {
                let sdf = Sdf2d::viewport(self.pos * self.rect_size);

                // Draw main background
                sdf.rect(0., 0., self.rect_size.x, self.rect_size.y);
                sdf.fill(self.color);

                // Draw left vertical indicator bar
                sdf.rect(0., 0., self.mentions_bar_width, self.rect_size.y);
                sdf.fill(self.mentions_bar_color);

                return sdf.result;
            }
        }
    }
}

// Set mentions bar color
let bar_color = if has_mention { vec4(1.0, 0.8, 0.0, 1.0) } else { vec4(1.0, 1.0, 1.0, 0.0) };
self.view(ids!(message)).apply_over(cx, live! {
    draw_bg: { mentions_bar_color: (bar_color) }
});
```
```

## File: `skills/robius-widget-patterns/references/widget-patterns.md`
```markdown
# Widget Patterns Reference

Additional widget patterns from Robrix codebase.

## Popup/Modal Pattern

```rust
live_design! {
    App = {{App}} {
        ui: <Root>{
            main_window = <Window> {
                body = {
                    flow: Overlay,

                    // Main content
                    main_content = <View> { }

                    // Modal (shown on top)
                    my_modal = <Modal> {
                        content: {
                            my_modal_inner = <MyModalContent> {}
                        }
                    }
                }
            }
        }
    }
}

// Opening modal
self.ui.modal(ids!(my_modal)).open(cx);

// Closing modal
self.ui.modal(ids!(my_modal)).close(cx);
```

## Tooltip Pattern

```rust
live_design! {
    pub CalloutTooltip = {{CalloutTooltip}} {
        width: Fit, height: Fit,
        visible: false,

        tooltip_bg = <View> {
            show_bg: true,
            draw_bg: { color: #333 }
            padding: 8,

            label = <Label> {
                draw_text: { color: #fff }
            }
        }
    }
}

impl CalloutTooltip {
    pub fn show(&mut self, cx: &mut Cx, text: &str, position: DVec2) {
        self.label(ids!(tooltip_bg.label)).set_text(cx, text);
        self.apply_over(cx, live! {
            margin: { left: (position.x), top: (position.y) }
        });
        self.set_visible(cx, true);
        self.redraw(cx);
    }

    pub fn hide(&mut self, cx: &mut Cx) {
        self.set_visible(cx, false);
        self.redraw(cx);
    }
}
```

## Badge Pattern

```rust
live_design! {
    pub UnreadBadge = {{UnreadBadge}} {
        width: Fit, height: Fit,
        visible: false,

        show_bg: true,
        draw_bg: {
            color: #e00,
            fn pixel(self) -> vec4 {
                let sdf = Sdf2d::viewport(self.pos * self.rect_size);
                sdf.box(0., 0., self.rect_size.x, self.rect_size.y, 8.0);
                sdf.fill(self.color);
                return sdf.result
            }
        }
        padding: { left: 6, right: 6, top: 2, bottom: 2 }

        count_label = <Label> {
            draw_text: { color: #fff, text_style: { font_size: 10 } }
        }
    }
}

impl UnreadBadge {
    pub fn set_count(&mut self, cx: &mut Cx, count: u64) {
        if count == 0 {
            self.set_visible(cx, false);
        } else {
            self.set_visible(cx, true);
            let text = if count > 99 { "99+".to_string() } else { count.to_string() };
            self.label(ids!(count_label)).set_text(cx, &text);
        }
        self.redraw(cx);
    }
}
```

## Input Bar Pattern

```rust
live_design! {
    pub RoomInputBar = {{RoomInputBar}} {
        width: Fill, height: Fit,
        flow: Right,
        padding: 10,

        text_input = <TextInput> {
            width: Fill,
            empty_message: "Type a message..."
        }

        send_button = <IconButton> {
            draw_icon: { svg_file: dep("icons/send.svg") }
        }
    }
}

impl Widget for RoomInputBar {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        // Handle send button click
        if self.button(ids!(send_button)).clicked(cx) {
            self.send_message(cx, scope);
        }

        // Handle Enter key
        if let Event::KeyDown(ke) = event {
            if ke.key_code == KeyCode::Return && !ke.modifiers.shift {
                self.send_message(cx, scope);
            }
        }
    }

    fn send_message(&mut self, cx: &mut Cx, scope: &mut Scope) {
        let text = self.text_input(ids!(text_input)).text();
        if !text.trim().is_empty() {
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                InputBarAction::SendMessage(text.to_string()),
            );
            self.text_input(ids!(text_input)).set_text(cx, "");
        }
    }
}
```

## Filter Input Pattern

```rust
live_design! {
    pub FilterInput = {{FilterInput}} {
        width: Fill, height: Fit,
        flow: Right,
        padding: 8,

        search_icon = <Icon> { }
        input = <TextInput> {
            width: Fill,
            empty_message: "Search..."
        }
        clear_button = <IconButton> {
            visible: false,
        }
    }
}

impl Widget for FilterInput {
    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {
        self.view.handle_event(cx, event, scope);

        // Show/hide clear button based on input
        if let Some(text_changed) = self.text_input(ids!(input)).text_changed(cx) {
            let has_text = !text_changed.is_empty();
            self.view(ids!(clear_button)).set_visible(cx, has_text);

            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                FilterAction::Changed(text_changed),
            );
        }

        // Handle clear button
        if self.button(ids!(clear_button)).clicked(cx) {
            self.text_input(ids!(input)).set_text(cx, "");
            self.view(ids!(clear_button)).set_visible(cx, false);
            cx.widget_action(
                self.widget_uid(),
                &scope.path,
                FilterAction::Cleared,
            );
        }
    }
}
```

## Extension Trait Pattern

For adding methods to widget refs:

```rust
pub trait MyWidgetWidgetRefExt {
    fn set_data(&self, cx: &mut Cx, data: &Data);
    fn get_value(&self) -> Option<Value>;
}

impl MyWidgetWidgetRefExt for MyWidgetRef {
    fn set_data(&self, cx: &mut Cx, data: &Data) {
        if let Some(mut inner) = self.borrow_mut() {
            inner.set_data(cx, data);
        }
    }

    fn get_value(&self) -> Option<Value> {
        self.borrow().map(|inner| inner.get_value())
    }
}

// Usage
let my_widget = self.my_widget(ids!(some_widget));
my_widget.set_data(cx, &data);
```
```


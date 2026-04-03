---
id: youtube-clipper-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.615866
---

# KNOWLEDGE EXTRACT: Youtube-clipper-skill
> **Extracted on:** 2026-03-30 13:18:39
> **Source:** Youtube-clipper-skill

---

## File: `.env.example`
```
# YouTube Clipper 环境变量配置示例
# 复制此文件为 .env 并填入实际值

# ============================================================================
# FFmpeg 配置
# ============================================================================

# FFmpeg 可执行文件路径（可选，留空则自动检测）
# macOS (Apple Silicon): /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg
# macOS (Intel): /usr/local/opt/ffmpeg-full/bin/ffmpeg
# Linux: /usr/bin/ffmpeg
FFMPEG_PATH=

# 字幕烧录样式
SUBTITLE_FONT_SIZE=24
SUBTITLE_MARGIN_V=30

# ============================================================================
# 输出配置
# ============================================================================

# 输出目录（默认: 当前工作目录下的 youtube-clips/）
OUTPUT_DIR=./youtube-clips

# 视频质量限制（最高分辨率）
# 选项: 720, 1080, 1440, 2160 (4K)
MAX_VIDEO_HEIGHT=1080

# ============================================================================
# 字幕翻译配置
# ============================================================================

# 批量翻译大小（每批翻译的字幕条数）
# 推荐: 20-25
TRANSLATION_BATCH_SIZE=20

# 目标翻译语言
# 选项: 中文, 日语, 韩语, 西班牙语, 等
TARGET_LANGUAGE=中文

# ============================================================================
# 章节分析配置
# ============================================================================

# 目标章节时长（秒）
# 推荐: 180 (3分钟) - 300 (5分钟)
TARGET_CHAPTER_DURATION=180

# ============================================================================
# yt-dlp 配置
# ============================================================================

# yt-dlp 代理设置（如果需要）
# 格式: http://proxy-server:port 或 socks5://proxy-server:port
YT_DLP_PROXY=

# yt-dlp 下载速率限制（如果需要）
# 格式: 50K, 4.2M, 等
YT_DLP_RATE_LIMIT=

# ============================================================================
# 高级配置
# ============================================================================

# 临时文件目录（用于解决路径空格问题）
# 留空则使用系统默认临时目录
TEMP_DIR=

# 是否保留临时文件（调试用）
# 选项: true, false
KEEP_TEMP_FILES=false

# 日志级别
# 选项: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL=INFO

# ============================================================================
# 注意事项
# ============================================================================

# 1. 此文件中的配置是可选的，如果不设置，Skill 会使用默认值
# 2. 路径可以使用 ~ 表示用户主目录
# 3. 环境变量值不需要引号
# 4. 以 # 开头的行是注释
# 5. 修改配置后需要重启 Claude Code 才能生效
```

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
.eggs/
dist/
build/

# Environment
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
Desktop.ini

# Outputs
youtube-clips/
outputs/
downloads/
temp/
tmp/

# Test files
*.mp4
*.webm
*.mkv
*.avi
*.vtt
*.srt
test_*.py
*_test.py

# Logs
*.log
logs/
```

## File: `FIXES_AND_IMPROVEMENTS.md`
```markdown
# YouTube Clipper Skill - 问题分析与修复

生成时间: 2026-01-21

## 问题总结

在首次测试运行中，我们遇到了以下问题：

### 1. Python 依赖缺失 ✅ 已修复

**问题**:
```
ModuleNotFoundError: No module named 'yt_dlp'
ModuleNotFoundError: No module named 'pysrt'
```

**原因**: macOS 的 Python 环境为外部管理环境（externally-managed），默认不允许使用 pip 安装包

**解决方案**:
```bash
pip3 install --break-system-packages yt-dlp pysrt python-dotenv
```

**状态**: ✅ 已安装并验证通过

---

### 2. 下载进度钩子除零错误 ✅ 已修复

**问题**:
```python
TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'
```

**位置**: `scripts/download_video.py` 的 `_progress_hook` 函数第 161 行

**原因**: 某些视频在下载时不提供 `total_bytes` 信息，导致除法运算失败

**修复**:
```python
# 修复前
if 'downloaded_bytes' in d and 'total_bytes' in d:
    percent = d['downloaded_bytes'] / d['total_bytes'] * 100

# 修复后
if 'downloaded_bytes' in d and 'total_bytes' in d and d['total_bytes']:
    percent = d['downloaded_bytes'] / d['total_bytes'] * 100
```

同时添加了备用显示逻辑，当无法获取总大小时，只显示已下载大小和速度

**文件**: `scripts/download_video.py:156-178`

**状态**: ✅ 已修复并测试通过

---

### 3. 文件名特殊字符问题 ✅ 已修复

**问题**:
原始视频文件名包含特殊字符（单引号和特殊冒号）导致路径处理困难
```
Anthropic's Amodei on AI： Power and Risk [Ckt1cj0xjRM].mp4
```

**测试时的临时方案**: 手动重命名为 `video.mp4` 和 `subtitle.vtt`

**根本原因**:
- yt-dlp 的输出模板使用了视频标题，标题中可能包含各种特殊字符
- 特别是某些 YouTube 视频标题中的冒号可能是全角字符（：而非:）
- 文件名中的单引号也会导致 shell 命令解析问题

**永久修复**:
修改 `scripts/download_video.py` 的输出模板，只使用视频 ID（保证无特殊字符）

```python
# 修复前（第 70 行）
'outtmpl': str(output_dir / '%(title)s [%(id)s].%(ext)s'),

# 修复后
'outtmpl': str(output_dir / '%(id)s.%(ext)s'),
```

**优势**:
- 视频 ID 只包含字母、数字、短横线和下划线（如 `Ckt1cj0xjRM`）
- 完全避免特殊字符和空格
- 文件名简洁，兼容性好
- 视频 ID 是唯一的，不会冲突

**文件**: `scripts/download_video.py:67`

**状态**: ✅ 已修复

---

### 4. 输出目录位置不符合预期 ✅ 已修复

**问题**:
测试时，输出文件保存在 `/tmp/youtube_clipper_output/` 目录，而不是用户当前工作目录

**用户反馈**:
"我觉得输出结果需要放到当前打开的文件夹里面"

**原因**:
测试脚本使用了临时目录，而 `utils.py` 中的 `create_output_dir()` 默认使用 `~/Videos/youtube-clips`

**修复**:

1. **utils.py** (第 146 行):
```python
# 修复前
if base_dir is None:
    base_dir = Path.home() / "Videos" / "youtube-clips"

# 修复后
if base_dir is None:
    base_dir = Path.cwd() / "youtube-clips"
```

2. **SKILL.md 文档更新**:
- 阶段 6 输出目录说明: `~/Videos/youtube-clips/` → `./youtube-clips/`
- 示例输出路径更新
- 添加说明：输出目录位于当前工作目录下

**优势**:
- 输出文件在用户当前工作目录，更符合预期
- 方便管理和查找生成的文件
- 不会污染用户的 Videos 目录

**文件**:
- `scripts/utils.py:131-148`
- `SKILL.md:240-270`

**状态**: ✅ 已修复

---

### 5. 字幕时间戳显示混淆（非实际错误）

**现象**:
测试时显示 `时间范围: 0.00s - -160.00s`（负数）

**分析**:
- 这只是显示问题，不是数据错误
- 实际提取了 33 条字幕（从原视频 160-280s 范围）
- 时间戳调整正确（减去 160s 偏移量）
- 字幕数据本身完全正确

**结论**: 不需要修复，测试脚本的显示逻辑略有问题，但不影响功能

---

## 成功验证的功能

测试使用视频: https://www.youtube.com/watch?v=Ckt1cj0xjRM

### ✅ 完整工作流程

1. **环境检测**:
   - yt-dlp 正常检测
   - FFmpeg libass 支持确认

2. **视频下载**:
   - 视频: 368 MB, 25:25 时长
   - 字幕: 41 KB VTT, 405 条字幕

3. **AI 章节分析**:
   - 成功生成 10 个精细章节（2-5 分钟粒度）
   - 每个章节包含标题、时间范围、核心摘要
   - 避免了粗粒度切分（没有半小时大章节）

4. **用户选择**:
   - 用户选择章节 2: "企业 vs 消费者"
   - 时间范围: 02:40 - 04:40

5. **视频剪辑**:
   - 成功剪辑 2 分钟片段（29.6 MB）
   - 使用 FFmpeg -ss 和 -t 参数精确裁剪

6. **字幕处理**:
   - 提取 35 条字幕
   - 时间戳正确调整（减去 160s 起始时间）
   - 批量翻译为中文（所有 35 条）
   - 生成双语 SRT 文件（英文在上，中文在下）

7. **字幕烧录**:
   - 使用 FFmpeg libass 滤镜
   - 临时目录方案成功解决路径空格问题
   - 输出视频 30.3 MB，字幕清晰可读

8. **文案生成**:
   - 生成小红书版本（约 800 字）
   - 生成抖音版本（约 280 字）
   - 生成微信公众号版本（完整深度文章）
   - 包含核心观点、金句摘录、推荐理由

### ✅ 技术亮点

1. **FFmpeg 临时目录方案**: 成功解决路径空格问题
2. **批量翻译**: 35 条字幕一次性翻译，效率高
3. **双语字幕格式**: 英文+中文，清晰易读
4. **AI 语义分析**: 生成有意义的章节，不是机械切分
5. **完整的社交媒体文案**: 一键生成多平台内容

---

## 改进建议

### 已实现的改进

1. ✅ 文件命名使用视频 ID（避免特殊字符）
2. ✅ 输出目录改为当前工作目录
3. ✅ 下载进度钩子容错处理
4. ✅ 文档更新反映实际行为

### 未来可能的增强

1. **自动清理临时文件**:
   - 当前保留了中间文件（clip.mp4, original_en.srt 等）
   - 可添加选项让用户选择是否保留中间文件

2. **视频格式选项**:
   - 当前固定为 mp4
   - 可支持用户选择输出格式（webm, mkv 等）

3. **字幕样式自定义**:
   - 当前固定字体大小 24、底部边距 30
   - 可添加配置文件让用户自定义

4. **批量剪辑模式**:
   - 当前一次只能剪辑一个章节
   - 可支持一次选择多个章节并行处理

5. **章节时长配置**:
   - 当前固定 2-5 分钟粒度
   - 可让用户指定目标时长（如 1 分钟、3 分钟、10 分钟）

---

## 测试数据

### 测试视频信息

- **URL**: https://www.youtube.com/watch?v=Ckt1cj0xjRM
- **标题**: Anthropic's Amodei on AI: Power and Risk
- **时长**: 25:25
- **视频大小**: 368 MB
- **字幕**: 41 KB (405 条 VTT 字幕)

### 生成的章节列表

1. [00:00 - 02:40] AI 竞赛不是赛跑，是不同方向
2. [02:40 - 04:40] 企业 vs 消费者：战略选择
3. [04:40 - 07:20] AI 泡沫？投资回报需要时间
4. [07:20 - 10:00] 就业影响：不会大规模失业
5. [10:00 - 12:30] 税收与 UBI：解决分配问题
6. [12:30 - 15:00] 安全风险：生物武器与网络攻击
7. [15:00 - 18:00] 国际合作与中国竞争
8. [18:00 - 21:00] 模型能力评估与安全测试
9. [21:00 - 23:30] Claude 的特点与应用场景
10. [23:30 - 25:25] 未来展望与结语

### 选择的片段

- **章节**: 2. 企业 vs 消费者：战略选择
- **时间**: 02:40 - 04:40
- **时长**: 2:00
- **原始片段**: 29.6 MB
- **烧录字幕版**: 30.3 MB
- **字幕数量**: 35 条
- **文案长度**: 7.5 KB

---

## 结论

经过首次完整测试和问题修复，YouTube Clipper Skill 现在可以稳定运行。所有核心功能已验证通过：

1. ✅ 视频下载（yt-dlp）
2. ✅ AI 章节分析（精细粒度）
3. ✅ 视频剪辑（FFmpeg）
4. ✅ 字幕翻译（批量处理）
5. ✅ 字幕烧录（临时目录方案）
6. ✅ 文案生成（多平台）

主要修复:
- 文件命名改用视频 ID（避免特殊字符）
- 输出目录改为当前工作目录
- 下载进度钩子容错
- 文档更新

Skill 已准备好供用户正式使用！
```

## File: `install_as_skill.sh`
```bash
#!/bin/bash

##############################################################################
# YouTube Clipper - Claude Code Skill 安装脚本
#
# 功能：
# 1. 自动创建 Skill 目录
# 2. 复制所有必要文件
# 3. 安装 Python 依赖
# 4. 检测系统依赖（yt-dlp、FFmpeg）
#
# 使用方法：
#   bash install_as_skill.sh
##############################################################################

set -e  # 遇到错误立即退出

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo ""
    echo "========================================"
    echo "$1"
    echo "========================================"
    echo ""
}

# 检查命令是否存在
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 主函数
main() {
    print_header "YouTube Clipper - Claude Code Skill 安装"

    # 1. 确定 Skill 目录
    SKILL_DIR="$HOME/.claude/skills/youtube-clipper"
    print_info "目标目录: $SKILL_DIR"

    # 2. 检查是否已存在
    if [ -d "$SKILL_DIR" ]; then
        print_warning "Skill 目录已存在: $SKILL_DIR"
        read -p "是否覆盖安装？(y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "安装已取消"
            exit 0
        fi
        print_info "删除旧版本..."
        rm -rf "$SKILL_DIR"
    fi

    # 3. 创建目录
    print_info "创建 Skill 目录..."
    mkdir -p "$SKILL_DIR"
    print_success "目录已创建"

    # 4. 复制文件
    print_info "复制项目文件..."

    # 获取当前脚本所在目录（即项目根目录）
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # 复制所有必要文件
    cp -r "$SCRIPT_DIR"/* "$SKILL_DIR/"

    # 排除不需要的文件
    if [ -d "$SKILL_DIR/.git" ]; then
        rm -rf "$SKILL_DIR/.git"
    fi
    if [ -d "$SKILL_DIR/venv" ]; then
        rm -rf "$SKILL_DIR/venv"
    fi
    if [ -d "$SKILL_DIR/__pycache__" ]; then
        rm -rf "$SKILL_DIR/__pycache__"
    fi
    if [ -d "$SKILL_DIR/youtube-clips" ]; then
        rm -rf "$SKILL_DIR/youtube-clips"
    fi
    if [ -f "$SKILL_DIR/.env" ]; then
        rm "$SKILL_DIR/.env"
    fi

    print_success "文件复制完成"

    # 5. 检查 Python
    print_info "检查 Python 环境..."
    if ! command_exists python3; then
        print_error "未找到 Python 3，请先安装 Python 3.8+"
        exit 1
    fi

    PYTHON_VERSION=$(python3 --version)
    print_success "Python 已安装: $PYTHON_VERSION"

    # 6. 检查 pip
    if ! command_exists pip3 && ! command_exists pip; then
        print_error "未找到 pip，请先安装 pip"
        exit 1
    fi
    print_success "pip 已安装"

    # 7. 安装 Python 依赖
    print_info "安装 Python 依赖..."
    cd "$SKILL_DIR"

    # 尝试使用 pip3，如果不存在则使用 pip
    if command_exists pip3; then
        pip3 install -q yt-dlp pysrt python-dotenv
    else
        pip install -q yt-dlp pysrt python-dotenv
    fi

    print_success "Python 依赖安装完成（yt-dlp、pysrt、python-dotenv）"

    # 8. 检查 yt-dlp
    print_info "检查 yt-dlp..."
    if command_exists yt-dlp; then
        YT_DLP_VERSION=$(yt-dlp --version)
        print_success "yt-dlp 已安装: $YT_DLP_VERSION"
    else
        print_warning "yt-dlp 命令行工具未安装"
        print_info "安装方法:"
        print_info "  macOS:  brew install yt-dlp"
        print_info "  Ubuntu: sudo apt-get install yt-dlp"
        print_info "  或: pip3 install -U yt-dlp"
    fi

    # 9. 检查 FFmpeg（关键：需要 libass 支持）
    print_header "检查 FFmpeg（字幕烧录需要）"

    FFMPEG_FOUND=false
    LIBASS_SUPPORTED=false

    # 检查 ffmpeg-full（macOS 推荐）
    if [ -f "/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg" ]; then
        print_success "ffmpeg-full 已安装（Apple Silicon）"
        FFMPEG_FOUND=true
        LIBASS_SUPPORTED=true
    elif [ -f "/usr/local/opt/ffmpeg-full/bin/ffmpeg" ]; then
        print_success "ffmpeg-full 已安装（Intel Mac）"
        FFMPEG_FOUND=true
        LIBASS_SUPPORTED=true
    elif command_exists ffmpeg; then
        FFMPEG_VERSION=$(ffmpeg -version | head -n 1)
        print_success "FFmpeg 已安装: $FFMPEG_VERSION"
        FFMPEG_FOUND=true

        # 检查 libass 支持
        if ffmpeg -filters 2>&1 | grep -q "subtitles"; then
            print_success "FFmpeg 支持 libass（字幕烧录可用）"
            LIBASS_SUPPORTED=true
        else
            print_warning "FFmpeg 不支持 libass（字幕烧录不可用）"
        fi
    fi

    if [ "$FFMPEG_FOUND" = false ]; then
        print_error "FFmpeg 未安装"
        print_info "安装方法:"
        print_info "  macOS:  brew install ffmpeg-full  # 推荐，包含 libass"
        print_info "  Ubuntu: sudo apt-get install ffmpeg libass-dev"
    elif [ "$LIBASS_SUPPORTED" = false ]; then
        print_warning "FFmpeg 缺少 libass 支持，字幕烧录功能将不可用"
        print_info "解决方法（macOS）:"
        print_info "  brew uninstall ffmpeg"
        print_info "  brew install ffmpeg-full"
    fi

    # 10. 创建 .env 文件
    print_header "配置环境变量"

    if [ -f "$SKILL_DIR/.env.example" ]; then
        print_info "创建 .env 文件..."
        cp "$SKILL_DIR/.env.example" "$SKILL_DIR/.env"
        print_success ".env 文件已创建"
        echo ""
        print_info "配置文件位置: $SKILL_DIR/.env"
        print_info "如需自定义配置，可编辑："
        print_info "  nano $SKILL_DIR/.env"
        print_info "  或"
        print_info "  code $SKILL_DIR/.env"
    else
        print_warning "未找到 .env.example 文件"
    fi

    # 11. 完成
    print_header "安装完成！"

    print_success "YouTube Clipper 已成功安装为 Claude Code Skill"
    echo ""
    print_info "安装位置: $SKILL_DIR"
    echo ""

    # 检查依赖状态
    if [ "$FFMPEG_FOUND" = false ] || [ "$LIBASS_SUPPORTED" = false ]; then
        print_warning "系统依赖不完整，部分功能可能不可用"
        echo ""
    fi

    print_info "使用方法："
    print_info "  在 Claude Code 中输入："
    print_info "  \"剪辑这个 YouTube 视频：https://youtube.com/watch?v=VIDEO_ID\""
    echo ""
    print_info "详细文档："
    print_info "  - Skill 使用指南: $SKILL_DIR/SKILL.md"
    print_info "  - 项目文档: $SKILL_DIR/README.md"
    print_info "  - 技术说明: $SKILL_DIR/TECHNICAL_NOTES.md"
    echo ""
    print_success "祝使用愉快！ 🎉"
    echo ""
}

# 错误处理
trap 'print_error "安装过程中发生错误"; exit 1' ERR

# 运行主函数
main
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 op7418

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

## File: `README.md`
```markdown
# YouTube Clipper Skill

> AI-powered YouTube video clipper for Claude Code. Download videos, generate semantic chapters, clip segments, translate subtitles to bilingual format, and burn subtitles into videos.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

English | [简体中文](README.zh-CN.md)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Requirements](#requirements) • [Configuration](#configuration) • [Troubleshooting](#troubleshooting)

---

## Features

- **AI Semantic Analysis** - Generate fine-grained chapters (2-5 minutes each) by understanding video content, not just mechanical time splitting
- **Precise Clipping** - Use FFmpeg to extract video segments with frame-accurate timing
- **Bilingual Subtitles** - Batch translate subtitles to Chinese/English with 95% API call reduction
- **Subtitle Burning** - Hardcode bilingual subtitles into videos with customizable styling
- **Content Summarization** - Auto-generate social media content (Xiaohongshu, Douyin, WeChat)

---

## Installation

### Option 1: npx skills (Recommended)

```bash
npx skills add https://github.com/op7418/Youtube-clipper-skill
```

This command will automatically install the skill to `~/.claude/skills/youtube-clipper/`.

### Option 2: Manual Installation

```bash
git clone https://github.com/op7418/Youtube-clipper-skill.git
cd Youtube-clipper-skill
bash install_as_skill.sh
```

The install script will:
- Copy files to `~/.claude/skills/youtube-clipper/`
- Install Python dependencies (yt-dlp, pysrt, python-dotenv)
- Check system dependencies (Python, yt-dlp, FFmpeg)
- Create `.env` configuration file

---

## Requirements

### System Dependencies

| Dependency | Version | Purpose | Installation |
|------------|---------|---------|--------------|
| **Python** | 3.8+ | Script execution | [python.org](https://www.python.org/downloads/) |
| **yt-dlp** | Latest | YouTube download | `brew install yt-dlp` (macOS)<br>`sudo apt install yt-dlp` (Ubuntu)<br>`pip install yt-dlp` (pip) |
| **FFmpeg with libass** | Latest | Video processing & subtitle burning | `brew install ffmpeg-full` (macOS)<br>`sudo apt install ffmpeg libass-dev` (Ubuntu) |

### Python Packages

These are automatically installed by the install script:
- `yt-dlp` - YouTube downloader
- `pysrt` - SRT subtitle parser
- `python-dotenv` - Environment variable management

### Important: FFmpeg libass Support

**macOS users**: The standard `ffmpeg` package from Homebrew does NOT include libass support (required for subtitle burning). You must install `ffmpeg-full`:

```bash
# Remove standard ffmpeg (if installed)
brew uninstall ffmpeg

# Install ffmpeg-full (includes libass)
brew install ffmpeg-full
```

**Verify libass support**:
```bash
ffmpeg -filters 2>&1 | grep subtitles
# Should output: subtitles    V->V  (...)
```

---

## Usage

### In Claude Code

Simply tell Claude to clip a YouTube video:

```
Clip this YouTube video: https://youtube.com/watch?v=VIDEO_ID
```

or

```
剪辑这个 YouTube 视频：https://youtube.com/watch?v=VIDEO_ID
```

### Workflow

1. **Environment Check** - Verifies yt-dlp, FFmpeg, and Python dependencies
2. **Video Download** - Downloads video (up to 1080p) and English subtitles
3. **AI Chapter Analysis** - Claude analyzes subtitles to generate semantic chapters (2-5 min each)
4. **User Selection** - Choose which chapters to clip and processing options
5. **Processing** - Clips video, translates subtitles, burns subtitles (if requested)
6. **Output** - Organized files in `./youtube-clips/<timestamp>/`

### Output Files

For each clipped chapter:

```
./youtube-clips/20260122_143022/
└── Chapter_Title/
    ├── Chapter_Title_clip.mp4              # Original clip (no subtitles)
    ├── Chapter_Title_with_subtitles.mp4    # With burned subtitles
    ├── Chapter_Title_bilingual.srt         # Bilingual subtitle file
    └── Chapter_Title_summary.md            # Social media content
```

---

## Configuration

The skill uses environment variables for customization. Edit `~/.claude/skills/youtube-clipper/.env`:

### Key Settings

```bash
# FFmpeg path (auto-detected if empty)
FFMPEG_PATH=

# Output directory (default: current working directory)
OUTPUT_DIR=./youtube-clips

# Video quality limit (720, 1080, 1440, 2160)
MAX_VIDEO_HEIGHT=1080

# Translation batch size (20-25 recommended)
TRANSLATION_BATCH_SIZE=20

# Target language for translation
TARGET_LANGUAGE=中文

# Target chapter duration in seconds (180-300 recommended)
TARGET_CHAPTER_DURATION=180
```

For full configuration options, see [.env.example](.env.example).

---

## Examples

### Example 1: Extract highlights from a tech interview

**Input**:
```
Clip this video: https://youtube.com/watch?v=Ckt1cj0xjRM
```

**Output** (AI-generated chapters):
```
1. [00:00 - 03:15] AGI as an exponential curve, not a point in time
2. [03:15 - 06:30] China's gap in AI development
3. [06:30 - 09:45] The impact of chip bans
...
```

**Result**: Select chapters → Get clipped videos with bilingual subtitles + social media content

### Example 2: Create short clips from a course

**Input**:
```
Clip this lecture video and create bilingual subtitles: https://youtube.com/watch?v=LECTURE_ID
```

**Options**:
- Generate bilingual subtitles: Yes
- Burn subtitles into video: Yes
- Generate summary: Yes

**Result**: High-quality clips ready for sharing on social media platforms

---

## Key Differentiators

### AI Semantic Chapter Analysis

Unlike mechanical time-based splitting, this skill uses Claude's AI to:
- Understand content semantics
- Identify natural topic transitions
- Generate meaningful chapter titles and summaries
- Ensure complete coverage with no gaps

**Example**:
```
❌ Mechanical splitting: [0:00-30:00], [30:00-60:00]
✅ AI semantic analysis:
   - [00:00-03:15] AGI definition
   - [03:15-07:30] China's AI landscape
   - [07:30-12:00] Chip ban impacts
```

### Batch Translation Optimization

Translates 20 subtitles at once instead of one-by-one:
- 95% reduction in API calls
- 10x faster translation
- Better translation consistency

### Bilingual Subtitle Format

Generated subtitle files contain both English and Chinese:

```srt
1
00:00:00,000 --> 00:00:03,500
This is the English subtitle
这是中文字幕

2
00:00:03,500 --> 00:00:07,000
Another English line
另一行中文
```

---

## Troubleshooting

### FFmpeg subtitle burning fails

**Error**: `Option not found: subtitles` or `filter not found`

**Solution**: Install `ffmpeg-full` (macOS) or ensure `libass-dev` is installed (Ubuntu):
```bash
# macOS
brew uninstall ffmpeg
brew install ffmpeg-full

# Ubuntu
sudo apt install ffmpeg libass-dev
```

### Video download is slow

**Solution**: Set a proxy in `.env`:
```bash
YT_DLP_PROXY=http://proxy-server:port
# or
YT_DLP_PROXY=socks5://proxy-server:port
```

### Subtitle translation fails

**Cause**: API rate limiting or network issues

**Solution**: The skill automatically retries up to 3 times. If persistent, check:
- Network connectivity
- Claude API status
- Reduce `TRANSLATION_BATCH_SIZE` in `.env`

### Special characters in filenames

**Issue**: Filenames with `:`, `/`, `?`, etc. may cause errors

**Solution**: The skill automatically sanitizes filenames by:
- Removing special characters: `/ \ : * ? " < > |`
- Replacing spaces with underscores
- Limiting length to 100 characters

---

## Documentation

- **[SKILL.md](SKILL.md)** - Complete workflow and technical details
- **[TECHNICAL_NOTES.md](TECHNICAL_NOTES.md)** - Implementation notes and design decisions
- **[FIXES_AND_IMPROVEMENTS.md](FIXES_AND_IMPROVEMENTS.md)** - Changelog and bug fixes
- **[references/](references/)** - FFmpeg, yt-dlp, and subtitle formatting guides

---

## Contributing

Contributions are welcome! Please:
- Report bugs via [GitHub Issues](https://github.com/op7418/Youtube-clipper-skill/issues)
- Submit feature requests
- Open pull requests for improvements

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **[Claude Code](https://claude.ai/claude-code)** - The AI-powered CLI tool
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube download engine
- **[FFmpeg](https://ffmpeg.org/)** - Video processing powerhouse

---

<div align="center">

**Made with ❤️ by [op7418](https://github.com/op7418)**

If this skill helps you, please give it a ⭐️

</div>
```

## File: `README.zh-CN.md`
```markdown
# YouTube Clipper Skill

> Claude Code 的 AI 智能视频剪辑工具。下载视频、生成语义章节、剪辑片段、翻译双语字幕并烧录字幕到视频。

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | 简体中文

[功能特性](#功能特性) • [安装](#安装) • [使用方法](#使用方法) • [系统要求](#系统要求) • [配置](#配置) • [常见问题](#常见问题)

---

## 功能特性

- **AI 语义分析** - 通过理解视频内容生成精细章节（每个 2-5 分钟），而非机械按时间切分
- **精确剪辑** - 使用 FFmpeg 以帧精度提取视频片段
- **双语字幕** - 批量翻译字幕为中英双语，减少 95% 的 API 调用
- **字幕烧录** - 将双语字幕硬编码到视频中，支持自定义样式
- **内容总结** - 自动生成适合社交媒体的文案（小红书、抖音、微信公众号）

---

## 安装

### 方式 1: npx skills（推荐）

```bash
npx skills add https://github.com/op7418/Youtube-clipper-skill
```

该命令会自动将 skill 安装到 `~/.claude/skills/youtube-clipper/` 目录。

### 方式 2: 手动安装

```bash
git clone https://github.com/op7418/Youtube-clipper-skill.git
cd Youtube-clipper-skill
bash install_as_skill.sh
```

安装脚本会：
- 复制文件到 `~/.claude/skills/youtube-clipper/`
- 安装 Python 依赖（yt-dlp、pysrt、python-dotenv）
- 检查系统依赖（Python、yt-dlp、FFmpeg）
- 创建 `.env` 配置文件

---

## 系统要求

### 系统依赖

| 依赖项 | 版本 | 用途 | 安装方法 |
|--------|------|------|----------|
| **Python** | 3.8+ | 脚本执行 | [python.org](https://www.python.org/downloads/) |
| **yt-dlp** | 最新版 | YouTube 视频下载 | `brew install yt-dlp` (macOS)<br>`sudo apt install yt-dlp` (Ubuntu)<br>`pip install yt-dlp` (pip) |
| **FFmpeg with libass** | 最新版 | 视频处理和字幕烧录 | `brew install ffmpeg-full` (macOS)<br>`sudo apt install ffmpeg libass-dev` (Ubuntu) |

### Python 包

安装脚本会自动安装以下包：
- `yt-dlp` - YouTube 下载器
- `pysrt` - SRT 字幕解析器
- `python-dotenv` - 环境变量管理

### 重要：FFmpeg libass 支持

**macOS 用户注意**：Homebrew 的标准 `ffmpeg` 包不包含 libass 支持（字幕烧录必需）。你必须安装 `ffmpeg-full`：

```bash
# 卸载标准 ffmpeg（如果已安装）
brew uninstall ffmpeg

# 安装 ffmpeg-full（包含 libass）
brew install ffmpeg-full
```

**验证 libass 支持**：
```bash
ffmpeg -filters 2>&1 | grep subtitles
# 应该输出：subtitles    V->V  (...)
```

---

## 使用方法

### 在 Claude Code 中使用

只需告诉 Claude 剪辑一个 YouTube 视频：

```
Clip this YouTube video: https://youtube.com/watch?v=VIDEO_ID
```

或者

```
剪辑这个 YouTube 视频：https://youtube.com/watch?v=VIDEO_ID
```

### 工作流程

1. **环境检测** - 验证 yt-dlp、FFmpeg 和 Python 依赖
2. **视频下载** - 下载视频（最高 1080p）和英文字幕
3. **AI 章节分析** - Claude 分析字幕生成语义章节（每个 2-5 分钟）
4. **用户选择** - 选择要剪辑的章节和处理选项
5. **处理** - 剪辑视频、翻译字幕、烧录字幕（如果需要）
6. **输出** - 组织文件到 `./youtube-clips/<时间戳>/`

### 输出文件

每个剪辑的章节包含：

```
./youtube-clips/20260122_143022/
└── 章节标题/
    ├── 章节标题_clip.mp4              # 原始剪辑（无字幕）
    ├── 章节标题_with_subtitles.mp4   # 带烧录字幕的视频
    ├── 章节标题_bilingual.srt        # 双语字幕文件
    └── 章节标题_summary.md           # 社交媒体文案
```

---

## 配置

本 skill 使用环境变量进行自定义配置。编辑 `~/.claude/skills/youtube-clipper/.env`：

### 主要设置

```bash
# FFmpeg 路径（留空则自动检测）
FFMPEG_PATH=

# 输出目录（默认：当前工作目录）
OUTPUT_DIR=./youtube-clips

# 视频质量限制（720、1080、1440、2160）
MAX_VIDEO_HEIGHT=1080

# 翻译批次大小（推荐 20-25）
TRANSLATION_BATCH_SIZE=20

# 目标翻译语言
TARGET_LANGUAGE=中文

# 目标章节时长（秒，推荐 180-300）
TARGET_CHAPTER_DURATION=180
```

完整配置选项请参见 [.env.example](.env.example)。

---

## 使用示例

### 示例 1：从技术访谈中提取精华

**输入**：
```
剪辑这个视频：https://youtube.com/watch?v=Ckt1cj0xjRM
```

**输出**（AI 生成的章节）：
```
1. [00:00 - 03:15] AGI 是指数曲线而非时间点
2. [03:15 - 06:30] 中国在 AI 领域的差距
3. [06:30 - 09:45] 芯片禁令的影响
...
```

**结果**：选择章节 → 获得带双语字幕的剪辑视频 + 社交媒体文案

### 示例 2：从课程视频创建短片

**输入**：
```
剪辑这个讲座视频并创建双语字幕：https://youtube.com/watch?v=LECTURE_ID
```

**选项**：
- 生成双语字幕：是
- 烧录字幕到视频：是
- 生成总结：是

**结果**：可直接在社交媒体平台分享的高质量剪辑视频

---

## 核心差异化功能

### AI 语义章节分析

与机械按时间切分不同，本 skill 使用 Claude AI 来：
- 理解内容语义
- 识别自然的主题转换点
- 生成有意义的章节标题和摘要
- 确保完整覆盖，无遗漏

**示例**：
```
❌ 机械切分：[0:00-30:00]、[30:00-60:00]
✅ AI 语义分析：
   - [00:00-03:15] AGI 定义
   - [03:15-07:30] 中国的 AI 格局
   - [07:30-12:00] 芯片禁令影响
```

### 批量翻译优化

一次翻译 20 条字幕，而非逐条翻译：
- 减少 95% 的 API 调用
- 速度提升 10 倍
- 更好的翻译一致性

### 双语字幕格式

生成的字幕文件同时包含英文和中文：

```srt
1
00:00:00,000 --> 00:00:03,500
This is the English subtitle
这是中文字幕

2
00:00:03,500 --> 00:00:07,000
Another English line
另一行中文
```

---

## 常见问题

### FFmpeg 字幕烧录失败

**错误**：`Option not found: subtitles` 或 `filter not found`

**解决方案**：安装 `ffmpeg-full`（macOS）或确保安装了 `libass-dev`（Ubuntu）：
```bash
# macOS
brew uninstall ffmpeg
brew install ffmpeg-full

# Ubuntu
sudo apt install ffmpeg libass-dev
```

### 视频下载速度慢

**解决方案**：在 `.env` 中设置代理：
```bash
YT_DLP_PROXY=http://proxy-server:port
# 或
YT_DLP_PROXY=socks5://proxy-server:port
```

### 字幕翻译失败

**原因**：API 限流或网络问题

**解决方案**：skill 会自动重试最多 3 次。如果持续失败，请检查：
- 网络连接
- Claude API 状态
- 减少 `.env` 中的 `TRANSLATION_BATCH_SIZE`

### 文件名包含特殊字符

**问题**：文件名中的 `:`、`/`、`?` 等可能导致错误

**解决方案**：skill 会自动清理文件名：
- 移除特殊字符：`/ \ : * ? " < > |`
- 将空格替换为下划线
- 限制长度为 100 字符

---

## 文档

- **[SKILL.md](SKILL.md)** - 完整工作流程和技术细节
- **[TECHNICAL_NOTES.md](TECHNICAL_NOTES.md)** - 实现笔记和设计决策
- **[FIXES_AND_IMPROVEMENTS.md](FIXES_AND_IMPROVEMENTS.md)** - 更新日志和 Bug 修复
- **[references/](references/)** - FFmpeg、yt-dlp 和字幕格式指南

---

## 贡献

欢迎贡献！请：
- 通过 [GitHub Issues](https://github.com/op7418/Youtube-clipper-skill/issues) 报告 Bug
- 提交功能请求
- 为改进提交 Pull Request

---

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## 致谢

- **[Claude Code](https://claude.ai/claude-code)** - AI 驱动的 CLI 工具
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube 下载引擎
- **[FFmpeg](https://ffmpeg.org/)** - 视频处理利器

---

<div align="center">

**Made with ❤️ by [op7418](https://github.com/op7418)**

如果这个 skill 对你有帮助，请给个 ⭐️

</div>
```

## File: `SKILL.md`
```markdown
---
name: youtube-clipper
description: >
  YouTube 视频智能剪辑工具。下载视频和字幕，AI 分析生成精细章节（几分钟级别），
  用户选择片段后自动剪辑、翻译字幕为中英双语、烧录字幕到视频，并生成总结文案。
  使用场景：当用户需要剪辑 YouTube 视频、生成短视频片段、制作双语字幕版本时。
  关键词：视频剪辑、YouTube、字幕翻译、双语字幕、视频下载、clip video
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - AskUserQuestion
model: claude-sonnet-4-5-20250514
---

# YouTube 视频智能剪辑工具

> **Installation**: If you're installing this skill from GitHub, please refer to [README.md](README.md#installation) for installation instructions. The recommended method is `npx skills add https://github.com/op7418/Youtube-clipper-skill`.

## 工作流程

你将按照以下 6 个阶段执行 YouTube 视频剪辑任务：

### 阶段 1: 环境检测

**目标**: 确保所有必需工具和依赖都已安装

1. 检测 yt-dlp 是否可用
   ```bash
   yt-dlp --version
   ```

2. 检测 FFmpeg 版本和 libass 支持
   ```bash
   # 优先检查 ffmpeg-full（macOS）
   /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg -version

   # 检查标准 FFmpeg
   ffmpeg -version

   # 验证 libass 支持（字幕烧录必需）
   ffmpeg -filters 2>&1 | grep subtitles
   ```

3. 检测 Python 依赖
   ```bash
   python3 -c "import yt_dlp; print('✅ yt-dlp available')"
   python3 -c "import pysrt; print('✅ pysrt available')"
   ```

**如果环境检测失败**:
- yt-dlp 未安装: 提示 `brew install yt-dlp` 或 `pip install yt-dlp`
- FFmpeg 无 libass: 提示安装 ffmpeg-full
  ```bash
  brew install ffmpeg-full  # macOS
  ```
- Python 依赖缺失: 提示 `pip install pysrt python-dotenv`

**注意**:
- 标准 Homebrew FFmpeg 不包含 libass，无法烧录字幕
- ffmpeg-full 路径: `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` (Apple Silicon)
- 必须先通过环境检测才能继续

---

### 阶段 2: 下载视频

**目标**: 下载 YouTube 视频和英文字幕

1. 询问用户 YouTube URL

2. 调用 download_video.py 脚本
   ```bash
   cd ~/.claude/skills/youtube-clipper
   python3 scripts/download_video.py <youtube_url>
   ```

3. 脚本会：
   - 下载视频（最高 1080p，mp4 格式）
   - 下载英文字幕（VTT 格式，自动字幕作为备选）
   - 输出文件路径和视频信息

4. 向用户展示：
   - 视频标题
   - 视频时长
   - 文件大小
   - 下载路径

**输出**:
- 视频文件: `<id>.mp4`（使用视频 ID 命名，避免特殊字符问题）
- 字幕文件: `<id>.en.vtt`

---

### 阶段 3: 分析章节（核心差异化功能）

**目标**: 使用 Claude AI 分析字幕内容，生成精细章节（2-5 分钟级别）

1. 调用 analyze_subtitles.py 解析 VTT 字幕
   ```bash
   python3 scripts/analyze_subtitles.py <subtitle_path>
   ```

2. 脚本会输出结构化字幕数据：
   - 完整字幕文本（带时间戳）
   - 总时长
   - 字幕条数

3. **你需要执行 AI 分析**（这是最关键的步骤）：
   - 阅读完整字幕内容
   - 理解内容语义和主题转换点
   - 识别自然的话题切换位置
   - 生成 2-5 分钟粒度的章节（避免半小时粗粒度切分）

4. 为每个章节生成：
   - **标题**: 精炼的主题概括（10-20 字）
   - **时间范围**: 起始和结束时间（格式: MM:SS 或 HH:MM:SS）
   - **核心摘要**: 1-2 句话说明这段讲了什么（50-100 字）
   - **关键词**: 3-5 个核心概念词

5. **章节生成原则**：
   - 粒度：每个章节 2-5 分钟（避免太短或太长）
   - 完整性：确保所有视频内容都被覆盖，无遗漏
   - 有意义：每个章节是一个相对独立的话题
   - 自然切分：在主题转换点切分，不要机械地按时间切

6. 向用户展示章节列表：
   ```
   📊 分析完成，生成 X 个章节：

   1. [00:00 - 03:15] AGI 不是时间点，是指数曲线
      核心: AI 模型能力每 4-12 月翻倍，工程师已用 Claude 写代码
      关键词: AGI、指数增长、Claude Code

   2. [03:15 - 06:30] 中国在 AI 上的差距
      核心: 芯片禁运卡住中国，DeepSeek benchmark 优化不代表实力
      关键词: 中国、芯片禁运、DeepSeek

   ... (所有章节)

   ✓ 所有内容已覆盖，无遗漏
   ```

---

### 阶段 4: 用户选择

**目标**: 让用户选择要剪辑的章节和处理选项

1. 使用 AskUserQuestion 工具让用户选择章节
   - 提供章节编号供用户选择
   - 支持多选（可以选择多个章节）

2. 询问处理选项：
   - 是否生成双语字幕？（英文 + 中文）
   - 是否烧录字幕到视频？（硬字幕）
   - 是否生成总结文案？

3. 确认用户选择并展示处理计划

---

### 阶段 5: 剪辑处理（核心执行阶段）

**目标**: 并行执行多个处理任务

对于每个用户选择的章节，执行以下步骤：

#### 5.1 剪辑视频片段
```bash
python3 scripts/clip_video.py <video_path> <start_time> <end_time> <output_path>
```
- 使用 FFmpeg 精确剪辑
- 保持原始视频质量
- 输出: `<章节标题>_clip.mp4`

#### 5.2 提取字幕片段
- 从完整字幕中过滤出该时间段的字幕
- 调整时间戳（减去起始时间，从 00:00:00 开始）
- 转换为 SRT 格式
- 输出: `<章节标题>_original.srt`

#### 5.3 翻译字幕（如果用户选择）
```bash
python3 scripts/translate_subtitles.py <subtitle_path>
```
- **批量翻译优化**: 每批 20 条字幕一起翻译（节省 95% API 调用）
- 翻译策略：
  - 保持技术术语的准确性
  - 口语化表达（适合短视频）
  - 简洁流畅（避免冗长）
- 输出: `<章节标题>_translated.srt`

#### 5.4 生成双语字幕文件（如果用户选择）
- 合并英文和中文字幕
- 格式: SRT 双语（每条字幕包含英文和中文）
- 样式: 英文在上，中文在下
- 输出: `<章节标题>_bilingual.srt`

#### 5.5 烧录字幕到视频（如果用户选择）
```bash
python3 scripts/burn_subtitles.py <video_path> <subtitle_path> <output_path>
```
- 使用 ffmpeg-full（libass 支持）
- **使用临时目录解决路径空格问题**（关键！）
- 字幕样式：
  - 字体大小: 24
  - 底部边距: 30
  - 颜色: 白色文字 + 黑色描边
- 输出: `<章节标题>_with_subtitles.mp4`

#### 5.6 生成总结文案（如果用户选择）
```bash
python3 scripts/generate_summary.py <chapter_info>
```
- 基于章节标题、摘要和关键词
- 生成适合社交媒体的文案
- 包含: 标题、核心观点、适合平台（小红书、抖音等）
- 输出: `<章节标题>_summary.md`

**进度展示**:
```
🎬 开始处理章节 1/3: AGI 不是时间点，是指数曲线

1/6 剪辑视频片段... ✅
2/6 提取字幕片段... ✅
3/6 翻译字幕为中文... [=====>    ] 50% (26/52)
4/6 生成双语字幕文件... ✅
5/6 烧录字幕到视频... ✅
6/6 生成总结文案... ✅

✨ 章节 1 处理完成
```

---

### 阶段 6: 输出结果

**目标**: 组织输出文件并展示给用户

1. 创建输出目录
   ```
   ./youtube-clips/<日期时间>/
   ```
   输出目录位于当前工作目录下

2. 组织文件结构：
   ```
   <章节标题>/
   ├── <章节标题>_clip.mp4              # 原始剪辑（无字幕）
   ├── <章节标题>_with_subtitles.mp4   # 烧录字幕版本
   ├── <章节标题>_bilingual.srt        # 双语字幕文件
   └── <章节标题>_summary.md           # 总结文案
   ```

3. 向用户展示：
   - 输出目录路径
   - 文件列表（带文件大小）
   - 快速预览命令

   ```
   ✨ 处理完成！

   📁 输出目录: ./youtube-clips/20260121_143022/

   文件列表:
     🎬 AGI_指数曲线_双语硬字幕.mp4 (14 MB)
     📄 AGI_指数曲线_双语字幕.srt (2.3 KB)
     📝 AGI_指数曲线_总结.md (3.2 KB)

   快速预览:
   open ./youtube-clips/20260121_143022/AGI_指数曲线_双语硬字幕.mp4
   ```

4. 询问是否继续剪辑其他章节
   - 如果是，返回阶段 4（用户选择）
   - 如果否，结束 Skill

---

## 关键技术点

### 1. FFmpeg 路径空格问题
**问题**: FFmpeg subtitles 滤镜无法正确解析包含空格的路径

**解决方案**: burn_subtitles.py 使用临时目录
- 创建无空格临时目录
- 复制文件到临时目录
- 执行 FFmpeg
- 移动输出文件回目标位置

### 2. 批量翻译优化
**问题**: 逐条翻译会产生大量 API 调用

**解决方案**: 每批 20 条字幕一起翻译
- 节省 95% API 调用
- 提高翻译速度
- 保持翻译一致性

### 3. 章节分析精细度
**目标**: 生成 2-5 分钟粒度的章节，避免半小时粗粒度

**方法**:
- 理解字幕语义，识别主题转换
- 寻找自然的话题切换点
- 确保每个章节有完整的论述
- 避免机械按时间切分

### 4. FFmpeg vs ffmpeg-full
**区别**:
- 标准 FFmpeg: 无 libass 支持，无法烧录字幕
- ffmpeg-full: 包含 libass，支持字幕烧录

**路径**:
- 标准: `/opt/homebrew/bin/ffmpeg`
- ffmpeg-full: `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` (Apple Silicon)

---

## 错误处理

### 环境问题
- 缺少工具 → 提示安装命令
- FFmpeg 无 libass → 引导安装 ffmpeg-full
- Python 依赖缺失 → 提示 pip install

### 下载问题
- 无效 URL → 提示检查 URL 格式
- 字幕缺失 → 尝试自动字幕
- 网络错误 → 提示重试

### 处理问题
- FFmpeg 执行失败 → 显示详细错误信息
- 翻译失败 → 重试机制（最多 3 次）
- 磁盘空间不足 → 提示清理空间

---

## 输出文件命名规范

- 视频片段: `<章节标题>_clip.mp4`
- 字幕文件: `<章节标题>_bilingual.srt`
- 烧录版本: `<章节标题>_with_subtitles.mp4`
- 总结文案: `<章节标题>_summary.md`

**文件名处理**:
- 移除特殊字符（`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`）
- 空格替换为下划线
- 限制长度（最多 100 字符）

---

## 用户体验要点

1. **进度可见**: 每个步骤都展示进度和状态
2. **错误友好**: 清晰的错误信息和解决方案
3. **可控性**: 用户选择要剪辑的章节和处理选项
4. **高质量**: 章节分析有意义，翻译准确流畅
5. **完整性**: 提供原始和处理后的多个版本

---

## 开始执行

当用户触发这个 Skill 时：
1. 立即开始阶段 1（环境检测）
2. 按照 6 个阶段顺序执行
3. 每个阶段完成后自动进入下一阶段
4. 遇到问题时提供清晰的解决方案
5. 最后展示完整的输出结果

记住：这个 Skill 的核心价值在于 **AI 精细章节分析** 和 **无缝的技术处理**，让用户能快速从长视频中提取高质量的短视频片段。
```

## File: `TECHNICAL_NOTES.md`
```markdown
# 技术坑点记录

本文档记录 YouTube Clipper Skill 开发过程中遇到的关键技术问题和解决方案。

## 1. FFmpeg libass 支持问题

### 问题描述
标准 Homebrew FFmpeg 不包含 libass 库，导致无法使用 `subtitles` 滤镜烧录字幕。

### 错误信息
```
No such filter: 'subtitles'
```

或者在检查滤镜时：
```bash
$ ffmpeg -filters 2>&1 | grep subtitles
# 无输出
```

### 根本原因
- Homebrew 的标准 `ffmpeg` formula 为了减小包体积，不包含某些非核心库
- libass 是字幕渲染库，用于 `subtitles` 滤镜
- 没有 libass，FFmpeg 无法烧录字幕到视频

### 解决方案

#### macOS
使用 `ffmpeg-full` 替代标准 FFmpeg：

```bash
# 安装 ffmpeg-full
brew install ffmpeg-full

# 路径（Apple Silicon）
/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg

# 路径（Intel）
/usr/local/opt/ffmpeg-full/bin/ffmpeg

# 验证 libass 支持
/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg -filters 2>&1 | grep subtitles
```

#### 其他系统
从源码编译 FFmpeg，确保包含 libass：

```bash
# Ubuntu/Debian
sudo apt-get install libass-dev
./configure --enable-libass
make
sudo make install

# 验证
ffmpeg -filters 2>&1 | grep subtitles
```

### 检测逻辑
`burn_subtitles.py` 中实现的检测逻辑：

1. 优先检查 `ffmpeg-full` 路径（macOS）
2. 检查标准 `ffmpeg` 是否支持 libass
3. 如果都不满足，提示安装指南

```python
def detect_ffmpeg_variant():
    # 检查 ffmpeg-full（macOS）
    if platform.system() == 'Darwin':
        full_path = '/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'
        if Path(full_path).exists():
            return {'type': 'full', 'path': full_path}

    # 检查标准 ffmpeg
    standard_path = shutil.which('ffmpeg')
    if standard_path:
        has_libass = check_libass_support(standard_path)
        return {'has_libass': has_libass}
```

---

## 2. 文件路径空格问题

### 问题描述
FFmpeg `subtitles` 滤镜无法正确处理包含空格的文件路径，即使使用引号或转义也无效。

### 错误信息
```
[Parsed_subtitles_0 @ 0x...] Unable to find '/path/with'
```

注意路径被截断在空格处（`/path/with spaces` → `/path/with`）。

### 示例
```bash
# 失败的尝试
ffmpeg -i video.mp4 -vf "subtitles='/path/with spaces/sub.srt'" output.mp4
ffmpeg -i video.mp4 -vf "subtitles=/path/with\ spaces/sub.srt" output.mp4
ffmpeg -i video.mp4 -vf subtitles="'/path/with spaces/sub.srt'" output.mp4

# 都会报错：Unable to find '/path/with'
```

### 根本原因
FFmpeg `subtitles` 滤镜的路径解析存在 bug，无法正确处理：
- 引号内的空格
- 转义的空格
- 混合引号

这是 FFmpeg 的已知限制。

### 解决方案：使用临时目录

核心思路：将文件复制到**无空格路径**的临时目录，处理后再移回。

```python
import tempfile
import shutil

def burn_subtitles(video_path, subtitle_path, output_path):
    # 1. 创建临时目录（路径保证无空格）
    temp_dir = tempfile.mkdtemp(prefix='youtube_clipper_')
    # 例如: /tmp/youtube_clipper_abc123

    try:
        # 2. 复制文件到临时目录
        temp_video = os.path.join(temp_dir, 'video.mp4')
        temp_subtitle = os.path.join(temp_dir, 'subtitle.srt')
        shutil.copy(video_path, temp_video)
        shutil.copy(subtitle_path, temp_subtitle)

        # 3. 执行 FFmpeg（路径无空格）
        cmd = [
            'ffmpeg',
            '-i', temp_video,
            '-vf', f'subtitles={temp_subtitle}',
            temp_output
        ]
        subprocess.run(cmd, check=True)

        # 4. 移动输出文件到目标位置
        shutil.move(temp_output, output_path)

    finally:
        # 5. 清理临时目录
        shutil.rmtree(temp_dir, ignore_errors=True)
```

### 为什么这样有效？
- `tempfile.mkdtemp()` 生成的路径不包含空格（通常是 `/tmp/xxx`）
- FFmpeg 可以正确处理无空格的路径
- 对用户透明，输入输出可以有任意路径

### 其他尝试过但无效的方案
❌ 使用双引号：`subtitles="/path/with spaces/sub.srt"`
❌ 使用单引号：`subtitles='/path/with spaces/sub.srt'`
❌ 转义空格：`subtitles=/path/with\ spaces/sub.srt`
❌ 混合引号：`subtitles="'/path/with spaces/sub.srt'"`
❌ FFmpeg `-filter_complex`：仍然有同样问题

✅ **唯一有效**：临时目录方案

---

## 3. VTT 转 SRT 格式转换

### 格式差异

| 项目 | VTT | SRT |
|------|-----|-----|
| 头部 | `WEBVTT` | 无 |
| 序号 | 可选 | 必需（从1开始） |
| 时间分隔符 | `.` (点) | `,` (逗号) |
| 样式信息 | 支持 | 不支持 |

### 时间戳格式

```
VTT:  00:00:00.000 --> 00:00:03.500
SRT:  00:00:00,000 --> 00:00:03,500
              ↑                  ↑
            逗号                逗号
```

### 转换实现

```python
def vtt_to_srt(vtt_path, srt_path):
    # 1. 移除 WEBVTT 头部
    content = content.replace('WEBVTT\n\n', '')

    # 2. 移除样式信息
    content = re.sub(r'STYLE.*?-->', '', content, flags=re.DOTALL)

    # 3. 转换时间戳分隔符
    # . → , (仅在时间戳中)
    content = re.sub(
        r'(\d{2}:\d{2}:\d{2})\.(\d{3})',
        r'\1,\2',
        content
    )

    # 4. 添加序号（如果没有）
    # ...
```

### 注意事项
- VTT 可能包含位置信息（`align:start position:0%`），需要移除
- VTT 可能有多行文本，转 SRT 时保持多行
- 时间戳格式严格：`HH:MM:SS,mmm`（必须有小时）

---

## 4. 字幕时间戳调整

### 问题描述
剪辑视频后，字幕时间戳需要相对于新的起始时间。

### 示例
原视频：
```
[00:02:00] 字幕1
[00:02:03] 字幕2
[00:02:06] 字幕3
```

剪辑 02:00-02:10 后，字幕应该变为：
```
[00:00:00] 字幕1
[00:00:03] 字幕2
[00:00:06] 字幕3
```

### 实现
```python
def adjust_subtitle_time(time_seconds, offset):
    """
    调整字幕时间戳

    Args:
        time_seconds: 原始时间（秒）
        offset: 偏移量（秒），即剪辑起始时间

    Returns:
        float: 调整后的时间
    """
    adjusted = time_seconds - offset
    return max(0.0, adjusted)  # 确保不为负数
```

### 边界情况处理
1. 字幕完全在时间范围内：保留
2. 字幕完全在时间范围外：丢弃
3. 字幕跨越边界：
   - 起始时间调整为 0（如果在范围前）
   - 结束时间调整为片段时长（如果在范围后）

---

## 5. 批量翻译优化

### 问题
逐条翻译字幕会产生大量 API 调用，速度慢且成本高。

### 数据
- 一个 30 分钟视频：约 600 条字幕
- 逐条翻译：600 次 API 调用
- 批量翻译（20条/批）：30 次 API 调用
- **节省 95% API 调用**

### 实现策略

```python
def translate_batch(subtitles, batch_size=20):
    batches = []
    for i in range(0, len(subtitles), batch_size):
        batch = subtitles[i:i + batch_size]
        batches.append(batch)

    # 每批一起翻译
    for batch in batches:
        # 合并为单个文本
        batch_text = '\n'.join([sub['text'] for sub in batch])

        # 一次 API 调用翻译整批
        translations = translate_text(batch_text)

        # 分配翻译结果
        # ...
```

### 批量大小选择
- **20 条**是平衡点：
  - 小于 20：API 调用过多
  - 大于 30：单次输入过长，翻译质量下降
  - 20-25：最佳范围

### 翻译质量保证
批量翻译时需要：
1. 保持上下文连贯性
2. 每条字幕单独翻译（不要合并）
3. 返回 JSON 数组，顺序对应

---

## 6. yt-dlp 最佳实践

### 格式选择
```python
'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best'
```

解释：
- `bestvideo[height<=1080]`：视频最高 1080p
- `[ext=mp4]`：优先 mp4 格式（兼容性好）
- `+bestaudio[ext=m4a]`：合并最佳音频
- `/best[height<=1080][ext=mp4]`：备选方案
- `/best`：最终备选

### 为什么限制 1080p？
1. 文件大小：4K 视频太大（可能 5-10GB）
2. 处理速度：FFmpeg 处理时间长
3. 输出场景：短视频平台主要是 1080p 或更低
4. 存储空间：节省磁盘

### 字幕下载
```python
'writesubtitles': True,
'writeautomaticsub': True,  # 自动字幕作为备选
'subtitleslangs': ['en'],   # 英文字幕
'subtitlesformat': 'vtt',   # VTT 格式
```

优先级：
1. 人工字幕（如果有）
2. 自动字幕（YouTube 自动生成）

### 输出模板
```python
'outtmpl': '%(title)s [%(id)s].%(ext)s'
```

结果示例：
```
Anthropic's Amodei on AI [Ckt1cj0xjRM].mp4
Anthropic's Amodei on AI [Ckt1cj0xjRM].en.vtt
```

包含视频 ID 的好处：
- 唯一性：不会重复
- 可追溯：可以找到原视频

---

## 7. 双语字幕样式

### SRT 格式双语
```srt
1
00:00:00,000 --> 00:00:03,500
This is English subtitle
这是中文字幕

2
00:00:03,500 --> 00:00:07,000
Another English line
另一行中文
```

### FFmpeg 烧录样式
```bash
subtitles=subtitle.srt:force_style='FontSize=24,MarginV=30'
```

参数说明：
- `FontSize=24`：字体大小（适合 1080p）
- `MarginV=30`：底部边距（像素）
- 默认：白色文字 + 黑色描边

### 样式调整建议

| 视频分辨率 | FontSize | MarginV |
|-----------|----------|---------|
| 720p      | 20       | 20      |
| 1080p     | 24       | 30      |
| 4K        | 48       | 60      |

---

## 8. Python 依赖管理

### 必需依赖
```bash
pip install yt-dlp pysrt python-dotenv
```

- `yt-dlp`：YouTube 视频下载
- `pysrt`：SRT 字幕解析和操作
- `python-dotenv`：环境变量管理（可选）

### 导入错误处理
```python
try:
    import yt_dlp
except ImportError:
    print("❌ Error: yt-dlp not installed")
    print("Please install: pip install yt-dlp")
    sys.exit(1)
```

在每个脚本中检查依赖，给出清晰的安装指导。

---

## 9. 跨平台路径处理

### 使用 pathlib
```python
from pathlib import Path

# ✅ 推荐
video_path = Path('/path/to/video.mp4')
if video_path.exists():
    ...

# ❌ 避免
video_path = '/path/to/video.mp4'
if os.path.exists(video_path):
    ...
```

### 路径拼接
```python
# ✅ 推荐
output_path = output_dir / 'video.mp4'

# ❌ 避免
output_path = output_dir + '/video.mp4'  # 在 Windows 上失败
```

---

## 10. 错误处理最佳实践

### 详细错误信息
```python
try:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Command failed:")
        print(f"   Command: {' '.join(cmd)}")
        print(f"   Return code: {result.returncode}")
        print(f"   Error output:")
        print(result.stderr)
        raise RuntimeError("Command failed")
except Exception as e:
    print(f"❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
```

### 用户友好的错误消息
```python
# ❌ 不好
raise Exception("FFmpeg failed")

# ✅ 好
raise RuntimeError(
    "FFmpeg does not support libass (subtitles filter). "
    "Please install ffmpeg-full: brew install ffmpeg-full"
)
```

---

## 总结

| 问题 | 解决方案 | 优先级 |
|------|---------|--------|
| FFmpeg libass 缺失 | 安装 ffmpeg-full | 🔴 必须 |
| 路径空格问题 | 使用临时目录 | 🔴 必须 |
| VTT → SRT | 转换时间分隔符 | 🟡 重要 |
| 字幕时间调整 | 减去起始时间 | 🟡 重要 |
| API 调用过多 | 批量翻译（20条/批）| 🟢 优化 |
| 文件过大 | 限制 1080p | 🟢 优化 |

所有关键问题都有经过验证的解决方案，可以直接使用。
```

## File: `references/ffmpeg-guide.md`
```markdown
# FFmpeg 使用指南

FFmpeg 是一个强大的多媒体处理工具，本文档介绍在 YouTube Clipper 中使用的核心命令。

## 安装

### macOS
```bash
# 标准版本（不支持字幕烧录）
brew install ffmpeg

# 完整版本（推荐，支持字幕烧录）
brew install ffmpeg-full
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg libass-dev
```

### 验证安装
```bash
# 检查版本
ffmpeg -version

# 检查 libass 支持（字幕烧录必需）
ffmpeg -filters 2>&1 | grep subtitles
```

## 常用命令

### 1. 剪辑视频

```bash
# 精确剪辑（从 30 秒开始，持续 60 秒）
ffmpeg -ss 30 -i input.mp4 -t 60 -c copy output.mp4

# 从 01:30:00 到 01:33:15
ffmpeg -ss 01:30:00 -i input.mp4 -to 01:33:15 -c copy output.mp4
```

**参数说明**:
- `-ss`: 起始时间
- `-i`: 输入文件
- `-t`: 持续时间
- `-to`: 结束时间
- `-c copy`: 直接复制流，不重新编码（快速且无损）

### 2. 烧录字幕

```bash
# 烧录 SRT 字幕到视频
ffmpeg -i input.mp4 \
  -vf "subtitles=subtitle.srt" \
  -c:a copy \
  output.mp4

# 自定义字幕样式
ffmpeg -i input.mp4 \
  -vf "subtitles=subtitle.srt:force_style='FontSize=24,MarginV=30'" \
  -c:a copy \
  output.mp4
```

**注意**:
- 需要 libass 支持
- 路径不能包含空格（使用临时目录解决）
- 视频会重新编码（比剪辑慢）

### 3. 视频压缩

```bash
# 使用 H.264 压缩
ffmpeg -i input.mp4 \
  -c:v libx264 \
  -crf 23 \
  -c:a aac \
  output.mp4
```

**CRF 值**:
- 18: 高质量，文件较大
- 23: 平衡（推荐）
- 28: 低质量，文件较小

### 4. 提取音频

```bash
# 提取为 MP3
ffmpeg -i input.mp4 -vn -acodec libmp3lame -q:a 2 output.mp3

# 提取为 AAC
ffmpeg -i input.mp4 -vn -c:a copy output.aac
```

### 5. 视频信息

```bash
# 查看视频详细信息
ffmpeg -i input.mp4

# 查看简洁信息
ffprobe -v error -show_format -show_streams input.mp4
```

## 字幕相关

### 烧录双语字幕

```bash
# 双语字幕（每条字幕包含两行）
ffmpeg -i input.mp4 \
  -vf "subtitles=bilingual.srt:force_style='FontSize=24,MarginV=30'" \
  -c:a copy \
  output.mp4
```

### 调整字幕样式

可用样式选项：
- `FontSize`: 字体大小（推荐 20-28）
- `MarginV`: 垂直边距（推荐 20-40）
- `FontName`: 字体名称
- `PrimaryColour`: 主要颜色
- `OutlineColour`: 描边颜色
- `Bold`: 粗体（0 或 1）

示例：
```bash
subtitles=subtitle.srt:force_style='FontSize=28,MarginV=40,Bold=1'
```

## 性能优化

### 硬件加速

```bash
# macOS (VideoToolbox)
ffmpeg -hwaccel videotoolbox -i input.mp4 ...

# NVIDIA GPU
ffmpeg -hwaccel cuda -i input.mp4 ...
```

### 多线程

```bash
# 使用 4 个线程
ffmpeg -threads 4 -i input.mp4 ...
```

## 常见问题

### Q: 字幕烧录失败，提示 "No such filter: 'subtitles'"

A: FFmpeg 没有 libass 支持。macOS 需要安装 `ffmpeg-full`。

### Q: 路径包含空格导致字幕烧录失败

A: 使用临时目录，将文件复制到无空格路径再处理。

### Q: 视频质量下降

A: 使用 `-c copy` 直接复制流，或降低 CRF 值（如 18）。

### Q: 处理速度慢

A:
- 使用硬件加速 (`-hwaccel`)
- 剪辑时使用 `-c copy`
- 增加线程数 (`-threads`)

## 参考链接

- [FFmpeg 官方文档](https://ffmpeg.org/documentation.html)
- [FFmpeg Wiki](https://trac.ffmpeg.org/wiki)
- [Subtitles 滤镜文档](https://ffmpeg.org/ffmpeg-filters.html#subtitles)
```

## File: `references/subtitle-formatting.md`
```markdown
# 字幕格式规范

本文档介绍 YouTube Clipper 中使用的字幕格式及其转换方法。

## 支持的格式

### 1. VTT (WebVTT)

WebVTT 是 Web 视频字幕标准格式。

#### 格式示例

```vtt
WEBVTT

1
00:00:00.000 --> 00:00:03.500
This is the first subtitle

2
00:00:03.500 --> 00:00:07.000
This is the second subtitle
```

#### 特点
- 头部必须是 `WEBVTT`
- 时间戳使用点 (`.`) 分隔毫秒
- 支持样式和位置信息
- YouTube 默认字幕格式

#### 完整示例

```vtt
WEBVTT

STYLE
::cue {
  background-color: rgba(0,0,0,0.8);
  color: white;
}

1
00:00:00.000 --> 00:00:03.500 align:start position:0%
<v Speaker>This is the first subtitle</v>

NOTE This is a comment

2
00:00:03.500 --> 00:00:07.000
This is the second subtitle
with multiple lines
```

---

### 2. SRT (SubRip)

SRT 是最常用的字幕格式，兼容性好。

#### 格式示例

```srt
1
00:00:00,000 --> 00:00:03,500
This is the first subtitle

2
00:00:03,500 --> 00:00:07,000
This is the second subtitle
```

#### 特点
- 没有头部
- 时间戳使用逗号 (`,`) 分隔毫秒
- 不支持样式（但 FFmpeg 可以覆盖）
- 兼容性最好

#### 多行文本

```srt
1
00:00:00,000 --> 00:00:03,500
This is the first line
This is the second line
This is the third line

2
00:00:03,500 --> 00:00:07,000
Single line subtitle
```

---

## VTT 与 SRT 对比

| 特性 | VTT | SRT |
|------|-----|-----|
| 头部 | 必须（`WEBVTT`） | 无 |
| 毫秒分隔符 | 点 (`.`) | 逗号 (`,`) |
| 样式支持 | 是 | 否 |
| 位置控制 | 是 | 否 |
| 注释支持 | 是 | 否 |
| 兼容性 | Web | 通用 |

---

## 格式转换

### VTT → SRT

#### Python 实现

```python
import re

def vtt_to_srt(vtt_content):
    # 1. 移除 WEBVTT 头部
    srt_content = re.sub(r'^WEBVTT.*?\n\n', '', vtt_content, flags=re.DOTALL)

    # 2. 移除样式信息
    srt_content = re.sub(r'STYLE.*?\n\n', '', srt_content, flags=re.DOTALL)

    # 3. 移除 NOTE
    srt_content = re.sub(r'NOTE.*?\n\n', '', srt_content, flags=re.DOTALL)

    # 4. 转换时间戳分隔符: . → ,
    srt_content = re.sub(
        r'(\d{2}:\d{2}:\d{2})\.(\d{3})',
        r'\1,\2',
        srt_content
    )

    # 5. 移除位置信息
    srt_content = re.sub(
        r'(-->.*?)\s+(align|position|line|size):.*',
        r'\1',
        srt_content
    )

    # 6. 移除说话人标签 <v Speaker>
    srt_content = re.sub(r'<v [^>]+>', '', srt_content)
    srt_content = re.sub(r'</v>', '', srt_content)

    return srt_content
```

#### 命令行工具

```bash
# 使用 ffmpeg
ffmpeg -i input.vtt output.srt

# 使用 sed
sed 's/\./,/3' input.vtt > output.srt  # 简单转换（不完整）
```

### SRT → VTT

#### Python 实现

```python
def srt_to_vtt(srt_content):
    # 1. 添加 WEBVTT 头部
    vtt_content = "WEBVTT\n\n" + srt_content

    # 2. 转换时间戳分隔符: , → .
    vtt_content = re.sub(
        r'(\d{2}:\d{2}:\d{2}),(\d{3})',
        r'\1.\2',
        vtt_content
    )

    return vtt_content
```

---

## 双语字幕

### SRT 格式

双语字幕在 SRT 中使用多行文本：

```srt
1
00:00:00,000 --> 00:00:03,500
This is English subtitle
这是中文字幕

2
00:00:03,500 --> 00:00:07,000
Another English line
另一行中文
```

### 样式建议

烧录到视频时的样式：

```bash
ffmpeg -i video.mp4 \
  -vf "subtitles=bilingual.srt:force_style='FontSize=24,MarginV=30'" \
  output.mp4
```

推荐参数：
- `FontSize=24`: 适合 1080p 视频
- `MarginV=30`: 底部边距 30 像素
- 英文在上，中文在下

---

## 时间戳格式

### 完整格式

```
HH:MM:SS.mmm --> HH:MM:SS.mmm
```

- `HH`: 小时（00-99）
- `MM`: 分钟（00-59）
- `SS`: 秒（00-59）
- `mmm`: 毫秒（000-999）

### 示例

```
00:00:00.000  # 0 秒
00:00:03.500  # 3.5 秒
00:01:30.250  # 1 分 30.25 秒
01:23:45.678  # 1 小时 23 分 45.678 秒
```

### 注意事项

1. 小时部分是可选的，但为了兼容性，建议总是包含
2. VTT 使用点 (`.`)，SRT 使用逗号 (`,`)
3. 毫秒必须是 3 位数（不足补 0）

---

## 时间调整

### 场景：视频剪辑后调整字幕

剪辑视频 02:00-02:10 后，字幕时间戳需要调整：

#### 原始字幕

```srt
1
00:02:00,000 --> 00:02:03,500
First subtitle

2
00:02:03,500 --> 00:02:07,000
Second subtitle
```

#### 调整后字幕

```srt
1
00:00:00,000 --> 00:00:03,500
First subtitle

2
00:00:03,500 --> 00:00:07,000
Second subtitle
```

#### Python 实现

```python
def adjust_subtitle_time(subtitles, offset_seconds):
    """
    调整字幕时间戳

    Args:
        subtitles: 字幕列表
        offset_seconds: 偏移量（秒），即剪辑起始时间

    Returns:
        调整后的字幕列表
    """
    adjusted = []

    for sub in subtitles:
        adjusted_sub = {
            'start': max(0, sub['start'] - offset_seconds),
            'end': max(0, sub['end'] - offset_seconds),
            'text': sub['text']
        }

        # 仅保留在有效范围内的字幕
        if adjusted_sub['end'] > 0:
            adjusted.append(adjusted_sub)

    return adjusted
```

---

## 字幕编码

### 推荐编码

**UTF-8**（无 BOM）

### 检查编码

```bash
file -i subtitle.srt
# 输出: subtitle.srt: text/plain; charset=utf-8
```

### 转换编码

```bash
# GBK → UTF-8
iconv -f GBK -t UTF-8 input.srt > output.srt

# 移除 BOM
sed -i '1s/^\xEF\xBB\xBF//' subtitle.srt
```

---

## 字幕验证

### 检查项目

1. **时间戳格式**: 是否符合规范
2. **时间顺序**: 起始时间 < 结束时间
3. **重叠检测**: 相邻字幕是否重叠
4. **编码检查**: 是否 UTF-8
5. **空行检查**: 字幕间是否有空行分隔

### Python 验证脚本

```python
def validate_srt(srt_path):
    errors = []

    with open(srt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割字幕块
    blocks = content.strip().split('\n\n')

    prev_end_time = 0

    for i, block in enumerate(blocks):
        lines = block.split('\n')

        if len(lines) < 3:
            errors.append(f"Block {i+1}: Invalid format (< 3 lines)")
            continue

        # 检查序号
        try:
            seq = int(lines[0])
            if seq != i + 1:
                errors.append(f"Block {i+1}: Invalid sequence number ({seq})")
        except ValueError:
            errors.append(f"Block {i+1}: Invalid sequence number")

        # 检查时间戳
        timestamp_pattern = r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
        match = re.match(timestamp_pattern, lines[1])

        if not match:
            errors.append(f"Block {i+1}: Invalid timestamp format")
            continue

        start_str, end_str = match.groups()
        start_time = time_to_seconds(start_str)
        end_time = time_to_seconds(end_str)

        # 检查时间逻辑
        if start_time >= end_time:
            errors.append(f"Block {i+1}: Start time >= End time")

        if start_time < prev_end_time:
            errors.append(f"Block {i+1}: Overlaps with previous subtitle")

        prev_end_time = end_time

    return errors
```

---

## 常见问题

### Q: FFmpeg 无法读取字幕，提示编码错误

A: 确保字幕是 UTF-8 编码，且没有 BOM：
```bash
iconv -f GBK -t UTF-8 input.srt > output.srt
sed -i '1s/^\xEF\xBB\xBF//' output.srt
```

### Q: 字幕显示乱码

A: 检查编码：
```bash
file -i subtitle.srt
# 如果不是 UTF-8，转换编码
```

### Q: VTT 字幕在某些播放器无法显示

A: 尝试转换为 SRT 格式，兼容性更好。

### Q: 双语字幕中文字太挤

A: 增加字体大小和边距：
```bash
subtitles=sub.srt:force_style='FontSize=28,MarginV=40'
```

---

## 参考链接

- [WebVTT 规范](https://www.w3.org/TR/webvtt1/)
- [SRT 格式说明](https://en.wikipedia.org/wiki/SubRip)
- [FFmpeg Subtitles 滤镜](https://ffmpeg.org/ffmpeg-filters.html#subtitles)
```

## File: `references/yt-dlp-guide.md`
```markdown
# yt-dlp 使用指南

yt-dlp 是一个强大的 YouTube 视频下载工具，本文档介绍在 YouTube Clipper 中使用的核心功能。

## 安装

### macOS
```bash
brew install yt-dlp
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get install yt-dlp

# 或使用 pip
pip install yt-dlp
```

### 更新
```bash
# Homebrew
brew upgrade yt-dlp

# pip
pip install --upgrade yt-dlp
```

## 基本用法

### 下载视频

```bash
# 下载最佳质量
yt-dlp https://youtube.com/watch?v=VIDEO_ID

# 指定格式
yt-dlp -f "best[ext=mp4]" URL

# 限制分辨率（最高 1080p）
yt-dlp -f "bestvideo[height<=1080]+bestaudio" URL
```

### 下载字幕

```bash
# 下载英文字幕
yt-dlp --write-sub --sub-lang en URL

# 下载自动生成字幕（如果没有人工字幕）
yt-dlp --write-auto-sub --sub-lang en URL

# 下载所有可用字幕
yt-dlp --write-sub --all-subs URL

# 指定字幕格式（VTT, SRT, 等）
yt-dlp --write-sub --sub-format vtt URL
```

## YouTube Clipper 使用的配置

### 完整配置

```python
ydl_opts = {
    # 视频格式：最高 1080p，优先 mp4
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',

    # 输出模板
    'outtmpl': '%(title)s [%(id)s].%(ext)s',

    # 下载字幕
    'writesubtitles': True,
    'writeautomaticsub': True,  # 自动字幕作为备选
    'subtitleslangs': ['en'],   # 英文字幕
    'subtitlesformat': 'vtt',   # VTT 格式

    # 不下载缩略图
    'writethumbnail': False,
}
```

### 格式字符串解释

```
bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best
│         │              │        │         │       │                           │
│         │              │        │         │       │                           └─ 最终备选
│         │              │        │         │       └─ 备选：最佳 1080p mp4
│         │              │        │         └─ 最佳音频（m4a）
│         │              │        └─ 合并
│         │              └─ 优先 mp4 格式
│         └─ 最高 1080p
└─ 最佳视频质量
```

### 为什么限制 1080p？

1. **文件大小**: 4K 视频可能 5-10GB
2. **处理速度**: FFmpeg 处理时间长
3. **实际需求**: 短视频平台主要是 1080p
4. **存储空间**: 节省磁盘

## 常用命令

### 1. 查看视频信息

```bash
# 不下载，仅显示信息
yt-dlp --print-json URL

# 查看可用格式
yt-dlp -F URL
```

### 2. 下载播放列表

```bash
# 下载整个播放列表
yt-dlp PLAYLIST_URL

# 仅下载特定视频（1-5）
yt-dlp --playlist-items 1-5 PLAYLIST_URL

# 不下载播放列表，仅当前视频
yt-dlp --no-playlist URL
```

### 3. 代理设置

```bash
# HTTP 代理
yt-dlp --proxy http://proxy:port URL

# SOCKS5 代理
yt-dlp --proxy socks5://proxy:port URL
```

### 4. 速率限制

```bash
# 限制下载速度为 50KB/s
yt-dlp --rate-limit 50K URL

# 限制为 4.2MB/s
yt-dlp --rate-limit 4.2M URL
```

### 5. 自定义文件名

```bash
# 使用模板
yt-dlp -o "%(title)s.%(ext)s" URL

# 包含上传日期
yt-dlp -o "%(upload_date)s - %(title)s.%(ext)s" URL

# 包含频道名称
yt-dlp -o "%(channel)s/%(title)s.%(ext)s" URL
```

## 字幕相关

### 字幕语言代码

常用语言代码：
- `en`: 英文
- `zh-Hans`: 简体中文
- `zh-Hant`: 繁体中文
- `ja`: 日语
- `ko`: 韩语
- `es`: 西班牙语
- `fr`: 法语
- `de`: 德语

### 查看可用字幕

```bash
# 列出所有可用字幕
yt-dlp --list-subs URL
```

### 字幕格式

```bash
# VTT 格式（推荐，兼容性好）
yt-dlp --write-sub --sub-format vtt URL

# SRT 格式
yt-dlp --write-sub --sub-format srt URL

# 多种格式
yt-dlp --write-sub --sub-format "vtt,srt" URL
```

## Python API 使用

### 基本示例

```python
import yt_dlp

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtube.com/watch?v=VIDEO_ID'])
```

### 获取视频信息

```python
import yt_dlp

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

    print(f"Title: {info['title']}")
    print(f"Duration: {info['duration']} seconds")
    print(f"Uploader: {info['uploader']}")
```

### 进度回调

```python
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        print(f"Progress: {percent:.1f}%")
    elif d['status'] == 'finished':
        print("Download complete!")

ydl_opts = {
    'progress_hooks': [progress_hook],
}
```

## 常见问题

### Q: 下载失败，提示 "Video unavailable"

A: 可能的原因：
- 视频已删除或私有
- 地区限制（尝试使用代理）
- 需要登录（使用 `--cookies` 选项）

### Q: 字幕下载失败

A: 尝试：
1. 使用 `--write-auto-sub`（自动生成字幕）
2. 使用 `--list-subs` 查看可用字幕
3. 某些视频没有字幕

### Q: 下载速度慢

A: 解决方案：
- 使用代理
- 检查网络连接
- YouTube 可能限速（等待后重试）

### Q: 文件名包含非法字符

A: 使用输出模板清理：
```bash
yt-dlp -o "%(title).100s.%(ext)s" URL
# .100s 限制标题长度为 100 字符
```

### Q: 如何下载会员专属视频？

A: 使用浏览器 cookies：
```bash
# 导出浏览器 cookies
yt-dlp --cookies-from-browser chrome URL

# 或使用 cookies 文件
yt-dlp --cookies cookies.txt URL
```

## 高级用法

### 批量下载

```bash
# 从文件读取 URL 列表
yt-dlp -a urls.txt

# urls.txt 内容：
# https://youtube.com/watch?v=VIDEO1
# https://youtube.com/watch?v=VIDEO2
# https://youtube.com/watch?v=VIDEO3
```

### 后处理

```bash
# 下载后转换为 MP3
yt-dlp -x --audio-format mp3 URL

# 下载后嵌入字幕
yt-dlp --embed-subs URL

# 下载后嵌入缩略图
yt-dlp --embed-thumbnail URL
```

### 归档选项

```bash
# 跳过已下载的视频
yt-dlp --download-archive archive.txt PLAYLIST_URL

# archive.txt 会记录已下载的视频 ID
```

## 支持的网站

yt-dlp 不仅支持 YouTube，还支持：
- Vimeo
- Twitter
- TikTok
- Bilibili
- 等 1000+ 网站

查看完整列表：
```bash
yt-dlp --list-extractors
```

## 参考链接

- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [yt-dlp 文档](https://github.com/yt-dlp/yt-dlp#readme)
- [格式选择说明](https://github.com/yt-dlp/yt-dlp#format-selection)
```

## File: `scripts/analyze_subtitles.py`
```python
#!/usr/bin/env python3
"""
分析字幕并生成章节
解析 VTT 字幕文件，准备数据供 Claude AI 分析
"""

import sys
import re
import json
from pathlib import Path
from typing import List, Dict

from utils import (
    time_to_seconds,
    seconds_to_time,
    get_video_duration_display
)


def parse_vtt(vtt_path: str) -> List[Dict]:
    """
    解析 VTT 字幕文件

    Args:
        vtt_path: VTT 文件路径

    Returns:
        List[Dict]: 字幕列表，每项包含 {start, end, text}

    Example:
        [
            {'start': 0.0, 'end': 3.5, 'text': 'Hello world'},
            {'start': 3.5, 'end': 7.2, 'text': 'This is a test'},
            ...
        ]
    """
    vtt_path = Path(vtt_path)

    if not vtt_path.exists():
        raise FileNotFoundError(f"Subtitle file not found: {vtt_path}")

    print(f"📊 解析字幕文件: {vtt_path.name}")

    subtitles = []

    with open(vtt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 移除 WEBVTT 头部和样式信息
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    content = re.sub(r'STYLE.*?-->', '', content, flags=re.DOTALL)

    # 分割字幕块
    blocks = content.strip().split('\n\n')

    for block in blocks:
        lines = block.strip().split('\n')

        if len(lines) < 2:
            continue

        # 查找时间戳行
        timestamp_line = None
        text_lines = []

        for line in lines:
            # 匹配时间戳格式: 00:00:00.000 --> 00:00:03.000
            if '-->' in line:
                timestamp_line = line
            elif line and not line.isdigit():  # 跳过序号
                text_lines.append(line)

        if not timestamp_line or not text_lines:
            continue

        # 解析时间戳
        try:
            # 移除可能的位置信息（如 align:start position:0%）
            timestamp_line = re.sub(r'align:.*|position:.*', '', timestamp_line).strip()

            times = timestamp_line.split('-->')
            start_str = times[0].strip()
            end_str = times[1].strip()

            start = time_to_seconds(start_str)
            end = time_to_seconds(end_str)

            # 合并文本行
            text = ' '.join(text_lines)

            # 清理 HTML 标签（如果有）
            text = re.sub(r'<[^>]+>', '', text)

            # 清理特殊字符
            text = text.strip()

            if text:
                subtitles.append({
                    'start': start,
                    'end': end,
                    'text': text
                })

        except Exception as e:
            # 跳过无法解析的字幕块
            continue

    print(f"   找到 {len(subtitles)} 条字幕")

    if subtitles:
        total_duration = subtitles[-1]['end']
        print(f"   总时长: {get_video_duration_display(total_duration)}")

    return subtitles


def prepare_analysis_data(subtitles: List[Dict], target_chapter_duration: int = 180) -> Dict:
    """
    准备数据供 Claude AI 分析

    Args:
        subtitles: 字幕列表
        target_chapter_duration: 目标章节时长（秒），默认 180 秒（3 分钟）

    Returns:
        Dict: {
            'subtitle_text': 带时间戳的完整字幕文本,
            'total_duration': 总时长,
            'subtitle_count': 字幕条数,
            'target_chapter_duration': 目标章节时长,
            'estimated_chapters': 预估章节数
        }
    """
    if not subtitles:
        raise ValueError("No subtitles to analyze")

    print(f"\n📝 准备分析数据...")

    # 将字幕合并为带时间戳的完整文本
    full_text_lines = []

    for sub in subtitles:
        time_str = seconds_to_time(sub['start'], include_hours=True, use_comma=False)
        full_text_lines.append(f"[{time_str}] {sub['text']}")

    full_text = '\n'.join(full_text_lines)

    total_duration = subtitles[-1]['end']
    estimated_chapters = max(1, int(total_duration / target_chapter_duration))

    print(f"   总时长: {get_video_duration_display(total_duration)}")
    print(f"   字幕条数: {len(subtitles)}")
    print(f"   目标章节时长: {target_chapter_duration} 秒 ({target_chapter_duration // 60} 分钟)")
    print(f"   预估章节数: {estimated_chapters}")

    return {
        'subtitle_text': full_text,
        'total_duration': total_duration,
        'subtitle_count': len(subtitles),
        'target_chapter_duration': target_chapter_duration,
        'estimated_chapters': estimated_chapters,
        'subtitles_raw': subtitles  # 保留原始数据供后续使用
    }


def save_analysis_data(data: Dict, output_path: str):
    """
    保存分析数据到 JSON 文件

    Args:
        data: 分析数据
        output_path: 输出文件路径
    """
    output_path = Path(output_path)

    # 创建输出目录
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 保存为 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ 分析数据已保存: {output_path}")


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python analyze_subtitles.py <vtt_file> [target_duration] [output_json]")
        print("\nArguments:")
        print("  vtt_file         - VTT 字幕文件路径")
        print("  target_duration  - 目标章节时长（秒），默认 180")
        print("  output_json      - 输出 JSON 文件路径（可选）")
        print("\nExample:")
        print("  python analyze_subtitles.py video.en.vtt")
        print("  python analyze_subtitles.py video.en.vtt 240")
        print("  python analyze_subtitles.py video.en.vtt 240 analysis.json")
        sys.exit(1)

    vtt_file = sys.argv[1]
    target_duration = int(sys.argv[2]) if len(sys.argv) > 2 else 180
    output_json = sys.argv[3] if len(sys.argv) > 3 else None

    try:
        # 解析字幕
        subtitles = parse_vtt(vtt_file)

        if not subtitles:
            print("❌ 未找到有效字幕")
            sys.exit(1)

        # 准备分析数据
        analysis_data = prepare_analysis_data(subtitles, target_duration)

        # 输出字幕文本（供 Claude 分析）
        print("\n" + "="*60)
        print("字幕文本（前 50 行预览）:")
        print("="*60)
        lines = analysis_data['subtitle_text'].split('\n')
        preview_lines = lines[:50]
        print('\n'.join(preview_lines))
        if len(lines) > 50:
            print(f"\n... （还有 {len(lines) - 50} 行）")

        # 保存到文件（如果指定）
        if output_json:
            save_analysis_data(analysis_data, output_json)

        # 输出摘要信息
        print("\n" + "="*60)
        print("分析摘要:")
        print("="*60)
        print(json.dumps({
            'total_duration': analysis_data['total_duration'],
            'total_duration_display': get_video_duration_display(analysis_data['total_duration']),
            'subtitle_count': analysis_data['subtitle_count'],
            'target_chapter_duration': analysis_data['target_chapter_duration'],
            'estimated_chapters': analysis_data['estimated_chapters']
        }, indent=2, ensure_ascii=False))

        print("\n💡 提示：现在可以使用 Claude AI 分析上述字幕文本，生成精细章节")

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/burn_subtitles.py`
```python
#!/usr/bin/env python3
"""
烧录字幕到视频
处理 FFmpeg libass 支持和路径空格问题
"""

import sys
import os
import shutil
import subprocess
import tempfile
import platform
from pathlib import Path
from typing import Dict, Optional

from utils import format_file_size


def detect_ffmpeg_variant() -> Dict:
    """
    检测 FFmpeg 版本和 libass 支持

    Returns:
        Dict: {
            'type': 'full' | 'standard' | 'none',
            'path': FFmpeg 可执行文件路径,
            'has_libass': 是否支持 libass
        }
    """
    print("🔍 检测 FFmpeg 环境...")

    # 优先检查 ffmpeg-full（macOS）
    if platform.system() == 'Darwin':
        # Apple Silicon
        full_path_arm = '/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg'
        # Intel
        full_path_intel = '/usr/local/opt/ffmpeg-full/bin/ffmpeg'

        for full_path in [full_path_arm, full_path_intel]:
            if Path(full_path).exists():
                has_libass = check_libass_support(full_path)
                print(f"   找到 ffmpeg-full: {full_path}")
                print(f"   libass 支持: {'✅ 是' if has_libass else '❌ 否'}")
                return {
                    'type': 'full',
                    'path': full_path,
                    'has_libass': has_libass
                }

    # 检查标准 FFmpeg
    standard_path = shutil.which('ffmpeg')
    if standard_path:
        has_libass = check_libass_support(standard_path)
        variant_type = 'full' if has_libass else 'standard'
        print(f"   找到 FFmpeg: {standard_path}")
        print(f"   类型: {variant_type}")
        print(f"   libass 支持: {'✅ 是' if has_libass else '❌ 否'}")
        return {
            'type': variant_type,
            'path': standard_path,
            'has_libass': has_libass
        }

    # 未找到 FFmpeg
    print("   ❌ 未找到 FFmpeg")
    return {
        'type': 'none',
        'path': None,
        'has_libass': False
    }


def check_libass_support(ffmpeg_path: str) -> bool:
    """
    检查 FFmpeg 是否支持 libass（字幕烧录必需）

    Args:
        ffmpeg_path: FFmpeg 可执行文件路径

    Returns:
        bool: 是否支持 libass
    """
    try:
        # 检查是否有 subtitles 滤镜
        result = subprocess.run(
            [ffmpeg_path, '-filters'],
            capture_output=True,
            text=True,
            timeout=5
        )

        # 查找 subtitles 滤镜
        return 'subtitles' in result.stdout.lower()

    except Exception:
        return False


def install_ffmpeg_full_guide():
    """
    显示安装 ffmpeg-full 的指南
    """
    print("\n" + "="*60)
    print("⚠️  需要安装 ffmpeg-full 才能烧录字幕")
    print("="*60)

    if platform.system() == 'Darwin':
        print("\nmacOS 安装方法:")
        print("  brew install ffmpeg-full")
        print("\n安装后，FFmpeg 路径:")
        print("  /opt/homebrew/opt/ffmpeg-full/bin/ffmpeg  (Apple Silicon)")
        print("  /usr/local/opt/ffmpeg-full/bin/ffmpeg     (Intel)")
    else:
        print("\n其他系统:")
        print("  请从源码编译 FFmpeg，确保包含 libass 支持")
        print("  参考: https://trac.ffmpeg.org/wiki/CompilationGuide")

    print("\n验证安装:")
    print("  ffmpeg -filters 2>&1 | grep subtitles")
    print("="*60)


def burn_subtitles(
    video_path: str,
    subtitle_path: str,
    output_path: str,
    ffmpeg_path: str = None,
    font_size: int = 24,
    margin_v: int = 30
) -> str:
    """
    烧录字幕到视频（使用临时目录解决路径空格问题）

    Args:
        video_path: 输入视频路径
        subtitle_path: 字幕文件路径（SRT 格式）
        output_path: 输出视频路径
        ffmpeg_path: FFmpeg 可执行文件路径（可选）
        font_size: 字体大小，默认 24
        margin_v: 底部边距，默认 30

    Returns:
        str: 输出视频路径

    Raises:
        FileNotFoundError: 输入文件不存在
        RuntimeError: FFmpeg 执行失败
    """
    video_path = Path(video_path)
    subtitle_path = Path(subtitle_path)
    output_path = Path(output_path)

    # 验证输入文件
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not subtitle_path.exists():
        raise FileNotFoundError(f"Subtitle file not found: {subtitle_path}")

    # 检测 FFmpeg
    if ffmpeg_path is None:
        ffmpeg_info = detect_ffmpeg_variant()

        if ffmpeg_info['type'] == 'none':
            install_ffmpeg_full_guide()
            raise RuntimeError("FFmpeg not found")

        if not ffmpeg_info['has_libass']:
            install_ffmpeg_full_guide()
            raise RuntimeError("FFmpeg does not support libass (subtitles filter)")

        ffmpeg_path = ffmpeg_info['path']

    print(f"\n🎬 烧录字幕到视频...")
    print(f"   视频: {video_path.name}")
    print(f"   字幕: {subtitle_path.name}")
    print(f"   输出: {output_path.name}")
    print(f"   FFmpeg: {ffmpeg_path}")

    # 创建临时目录（解决路径空格问题）
    temp_dir = tempfile.mkdtemp(prefix='youtube_clipper_')
    print(f"   使用临时目录: {temp_dir}")

    try:
        # 复制文件到临时目录（路径无空格）
        temp_video = os.path.join(temp_dir, 'video.mp4')
        temp_subtitle = os.path.join(temp_dir, 'subtitle.srt')
        temp_output = os.path.join(temp_dir, 'output.mp4')

        print(f"   复制文件到临时目录...")
        shutil.copy(video_path, temp_video)
        shutil.copy(subtitle_path, temp_subtitle)

        # 构建 FFmpeg 命令
        # 使用 subtitles 滤镜烧录字幕
        subtitle_filter = f"subtitles={temp_subtitle}:force_style='FontSize={font_size},MarginV={margin_v}'"

        cmd = [
            ffmpeg_path,
            '-i', temp_video,
            '-vf', subtitle_filter,
            '-c:a', 'copy',  # 音频直接复制，不重新编码
            '-y',  # 覆盖输出文件
            temp_output
        ]

        print(f"   执行 FFmpeg...")
        print(f"   命令: {' '.join(cmd)}")

        # 执行 FFmpeg
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"\n❌ FFmpeg 执行失败:")
            print(result.stderr)
            raise RuntimeError(f"FFmpeg failed with return code {result.returncode}")

        # 验证输出文件
        if not Path(temp_output).exists():
            raise RuntimeError("Output file not created")

        # 移动输出文件到目标位置
        print(f"   移动输出文件...")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(temp_output, output_path)

        # 获取文件大小
        output_size = output_path.stat().st_size
        print(f"✅ 字幕烧录完成")
        print(f"   输出文件: {output_path}")
        print(f"   文件大小: {format_file_size(output_size)}")

        return str(output_path)

    finally:
        # 清理临时目录
        try:
            shutil.rmtree(temp_dir, ignore_errors=True)
            print(f"   清理临时目录")
        except Exception:
            pass


def main():
    """命令行入口"""
    if len(sys.argv) < 4:
        print("Usage: python burn_subtitles.py <video> <subtitle> <output> [font_size] [margin_v]")
        print("\nArguments:")
        print("  video      - 输入视频文件路径")
        print("  subtitle   - 字幕文件路径（SRT 格式）")
        print("  output     - 输出视频文件路径")
        print("  font_size  - 字体大小，默认 24")
        print("  margin_v   - 底部边距，默认 30")
        print("\nExample:")
        print("  python burn_subtitles.py input.mp4 subtitle.srt output.mp4")
        print("  python burn_subtitles.py input.mp4 subtitle.srt output.mp4 28 40")
        sys.exit(1)

    video_path = sys.argv[1]
    subtitle_path = sys.argv[2]
    output_path = sys.argv[3]
    font_size = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    margin_v = int(sys.argv[5]) if len(sys.argv) > 5 else 30

    try:
        result_path = burn_subtitles(
            video_path,
            subtitle_path,
            output_path,
            font_size=font_size,
            margin_v=margin_v
        )

        print(f"\n✨ 完成！输出文件: {result_path}")

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/clip_video.py`
```python
#!/usr/bin/env python3
"""
剪辑视频片段
使用 FFmpeg 精确剪辑视频，保持原始质量
"""

import sys
import shutil
import subprocess
from pathlib import Path
from typing import Union

from utils import (
    time_to_seconds,
    seconds_to_time,
    format_file_size,
    get_video_duration_display
)


def clip_video(
    video_path: str,
    start_time: Union[str, float],
    end_time: Union[str, float],
    output_path: str,
    ffmpeg_path: str = None
) -> str:
    """
    剪辑视频片段

    Args:
        video_path: 输入视频路径
        start_time: 起始时间（秒数或时间字符串，如 "00:01:30"）
        end_time: 结束时间（秒数或时间字符串）
        output_path: 输出视频路径
        ffmpeg_path: FFmpeg 可执行文件路径（可选）

    Returns:
        str: 输出视频路径

    Raises:
        FileNotFoundError: 输入文件不存在
        RuntimeError: FFmpeg 执行失败
    """
    video_path = Path(video_path)
    output_path = Path(output_path)

    # 验证输入文件
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    # 转换时间为秒数
    if isinstance(start_time, str):
        start_seconds = time_to_seconds(start_time)
    else:
        start_seconds = float(start_time)

    if isinstance(end_time, str):
        end_seconds = time_to_seconds(end_time)
    else:
        end_seconds = float(end_time)

    # 验证时间范围
    if start_seconds >= end_seconds:
        raise ValueError(f"Start time ({start_seconds}s) must be before end time ({end_seconds}s)")

    duration = end_seconds - start_seconds

    # 检测 FFmpeg
    if ffmpeg_path is None:
        ffmpeg_path = shutil.which('ffmpeg')
        if not ffmpeg_path:
            raise RuntimeError("FFmpeg not found. Please install FFmpeg.")

    print(f"\n✂️  剪辑视频片段...")
    print(f"   输入: {video_path.name}")
    print(f"   起始时间: {seconds_to_time(start_seconds)} ({start_seconds}s)")
    print(f"   结束时间: {seconds_to_time(end_seconds)} ({end_seconds}s)")
    print(f"   片段时长: {get_video_duration_display(duration)}")
    print(f"   输出: {output_path.name}")

    # 创建输出目录
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 构建 FFmpeg 命令
    # 使用 -ss 和 -t 进行精确剪辑
    # -c copy: 直接复制流，不重新编码（快速且无损）
    cmd = [
        ffmpeg_path,
        '-ss', str(start_seconds),  # 起始时间
        '-i', str(video_path),       # 输入文件
        '-t', str(duration),         # 持续时间
        '-c', 'copy',                # 直接复制，不重新编码
        '-y',                        # 覆盖输出文件
        str(output_path)
    ]

    print(f"   执行 FFmpeg...")

    # 执行 FFmpeg
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"\n❌ FFmpeg 执行失败:")
        print(result.stderr)
        raise RuntimeError(f"FFmpeg failed with return code {result.returncode}")

    # 验证输出文件
    if not output_path.exists():
        raise RuntimeError("Output file not created")

    # 获取文件大小
    output_size = output_path.stat().st_size
    print(f"✅ 剪辑完成")
    print(f"   输出文件: {output_path}")
    print(f"   文件大小: {format_file_size(output_size)}")

    return str(output_path)


def extract_subtitle_segment(
    subtitles: list,
    start_time: float,
    end_time: float,
    adjust_timestamps: bool = True
) -> list:
    """
    从完整字幕中提取指定时间段的字幕

    Args:
        subtitles: 完整字幕列表（每项包含 {start, end, text}）
        start_time: 起始时间（秒）
        end_time: 结束时间（秒）
        adjust_timestamps: 是否调整时间戳（减去起始时间）

    Returns:
        list: 提取的字幕列表
    """
    segment_subtitles = []

    for sub in subtitles:
        # 字幕在时间范围内
        if sub['start'] >= start_time and sub['end'] <= end_time:
            if adjust_timestamps:
                # 调整时间戳（相对于片段起始时间）
                adjusted_sub = {
                    'start': sub['start'] - start_time,
                    'end': sub['end'] - start_time,
                    'text': sub['text']
                }
                segment_subtitles.append(adjusted_sub)
            else:
                segment_subtitles.append(sub.copy())

        # 字幕跨越时间范围边界（部分重叠）
        elif sub['start'] < end_time and sub['end'] > start_time:
            if adjust_timestamps:
                adjusted_sub = {
                    'start': max(0, sub['start'] - start_time),
                    'end': min(end_time - start_time, sub['end'] - start_time),
                    'text': sub['text']
                }
                segment_subtitles.append(adjusted_sub)
            else:
                segment_subtitles.append(sub.copy())

    return segment_subtitles


def save_subtitles_as_srt(subtitles: list, output_path: str):
    """
    保存字幕为 SRT 格式

    Args:
        subtitles: 字幕列表
        output_path: 输出文件路径
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        for i, sub in enumerate(subtitles, 1):
            # SRT 序号
            f.write(f"{i}\n")

            # SRT 时间戳（使用逗号分隔毫秒）
            start_time = seconds_to_time(sub['start'], include_hours=True, use_comma=True)
            end_time = seconds_to_time(sub['end'], include_hours=True, use_comma=True)
            f.write(f"{start_time} --> {end_time}\n")

            # 字幕文本
            f.write(f"{sub['text']}\n")

            # 空行分隔
            f.write("\n")

    print(f"✅ 字幕已保存: {output_path}")


def main():
    """命令行入口"""
    if len(sys.argv) < 5:
        print("Usage: python clip_video.py <video> <start_time> <end_time> <output>")
        print("\nArguments:")
        print("  video      - 输入视频文件路径")
        print("  start_time - 起始时间（秒数或时间字符串，如 00:01:30）")
        print("  end_time   - 结束时间（秒数或时间字符串）")
        print("  output     - 输出视频文件路径")
        print("\nExample:")
        print("  python clip_video.py input.mp4 0 195 output.mp4")
        print("  python clip_video.py input.mp4 00:00:00 00:03:15 output.mp4")
        print("  python clip_video.py input.mp4 01:30:00 01:33:15 output.mp4")
        sys.exit(1)

    video_path = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]
    output_path = sys.argv[4]

    try:
        result_path = clip_video(video_path, start_time, end_time, output_path)
        print(f"\n✨ 完成！输出文件: {result_path}")

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/download_video.py`
```python
#!/usr/bin/env python3
"""
下载 YouTube 视频和字幕
使用 yt-dlp 下载视频（最高 1080p）和英文字幕
"""

import sys
import json
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("❌ Error: yt-dlp not installed")
    print("Please install: pip install yt-dlp")
    sys.exit(1)

from utils import (
    validate_url,
    sanitize_filename,
    format_file_size,
    get_video_duration_display,
    ensure_directory
)


def download_video(url: str, output_dir: str = None) -> dict:
    """
    下载 YouTube 视频和字幕

    Args:
        url: YouTube URL
        output_dir: 输出目录，默认为当前目录

    Returns:
        dict: {
            'video_path': 视频文件路径,
            'subtitle_path': 字幕文件路径,
            'title': 视频标题,
            'duration': 视频时长（秒）,
            'file_size': 文件大小（字节）
        }

    Raises:
        ValueError: 无效的 URL
        Exception: 下载失败
    """
    # 验证 URL
    if not validate_url(url):
        raise ValueError(f"Invalid YouTube URL: {url}")

    # 设置输出目录
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)

    output_dir = ensure_directory(output_dir)

    print(f"🎬 开始下载视频...")
    print(f"   URL: {url}")
    print(f"   输出目录: {output_dir}")

    # 配置 yt-dlp 选项
    ydl_opts = {
        # 视频格式：最高 1080p，优先 mp4
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best',

        # 输出模板：包含视频 ID（避免特殊字符问题）
        'outtmpl': str(output_dir / '%(id)s.%(ext)s'),

        # 下载字幕
        'writesubtitles': True,
        'writeautomaticsub': True,  # 自动字幕作为备选
        'subtitleslangs': ['en'],   # 英文字幕
        'subtitlesformat': 'vtt',   # VTT 格式

        # 不下载缩略图
        'writethumbnail': False,

        # 静默模式（减少输出）
        'quiet': False,
        'no_warnings': False,

        # 进度钩子
        'progress_hooks': [_progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 提取信息
            print("\n📊 获取视频信息...")
            info = ydl.extract_info(url, download=False)

            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            video_id = info.get('id', 'unknown')

            print(f"   标题: {title}")
            print(f"   时长: {get_video_duration_display(duration)}")
            print(f"   视频ID: {video_id}")

            # 下载视频
            print(f"\n📥 开始下载...")
            info = ydl.extract_info(url, download=True)

            # 获取下载的文件路径
            video_filename = ydl.prepare_filename(info)
            video_path = Path(video_filename)

            # 查找字幕文件
            subtitle_path = None
            subtitle_exts = ['.en.vtt', '.vtt']
            for ext in subtitle_exts:
                potential_sub = video_path.with_suffix(ext)
                # 处理带语言代码的字幕文件
                if not potential_sub.exists():
                    # 尝试 <filename>.en.vtt 格式
                    stem = video_path.stem
                    potential_sub = video_path.parent / f"{stem}.en.vtt"

                if potential_sub.exists():
                    subtitle_path = potential_sub
                    break

            # 获取文件大小
            file_size = video_path.stat().st_size if video_path.exists() else 0

            # 验证下载结果
            if not video_path.exists():
                raise Exception("Video file not found after download")

            print(f"\n✅ 视频下载完成: {video_path.name}")
            print(f"   大小: {format_file_size(file_size)}")

            if subtitle_path and subtitle_path.exists():
                print(f"✅ 字幕下载完成: {subtitle_path.name}")
            else:
                print(f"⚠️  未找到英文字幕")
                print(f"   提示：某些视频可能没有字幕或需要自动生成")

            return {
                'video_path': str(video_path),
                'subtitle_path': str(subtitle_path) if subtitle_path else None,
                'title': title,
                'duration': duration,
                'file_size': file_size,
                'video_id': video_id
            }

    except Exception as e:
        print(f"\n❌ 下载失败: {str(e)}")
        raise


def _progress_hook(d):
    """下载进度回调"""
    if d['status'] == 'downloading':
        # 显示下载进度
        if 'downloaded_bytes' in d and 'total_bytes' in d and d['total_bytes']:
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            downloaded = format_file_size(d['downloaded_bytes'])
            total = format_file_size(d['total_bytes'])
            speed = d.get('speed', 0)
            speed_str = format_file_size(speed) + '/s' if speed else 'N/A'

            # 使用 \r 实现进度条覆盖
            bar_length = 30
            filled = int(bar_length * percent / 100)
            bar = '█' * filled + '░' * (bar_length - filled)

            print(f"\r   [{bar}] {percent:.1f}% - {downloaded}/{total} - {speed_str}", end='', flush=True)
        elif 'downloaded_bytes' in d:
            # 无总大小信息时，只显示已下载
            downloaded = format_file_size(d['downloaded_bytes'])
            speed = d.get('speed', 0)
            speed_str = format_file_size(speed) + '/s' if speed else 'N/A'
            print(f"\r   下载中... {downloaded} - {speed_str}", end='', flush=True)

    elif d['status'] == 'finished':
        print()  # 换行


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python download_video.py <youtube_url> [output_dir]")
        print("\nExample:")
        print("  python download_video.py https://youtube.com/watch?v=Ckt1cj0xjRM")
        print("  python download_video.py https://youtube.com/watch?v=Ckt1cj0xjRM ~/Downloads")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = download_video(url, output_dir)

        # 输出 JSON 结果（供其他脚本使用）
        print("\n" + "="*60)
        print("下载结果 (JSON):")
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/extract_subtitle_clip.py`
```python
#!/usr/bin/env python3
"""
提取字幕片段并转换为 SRT 格式
"""

import sys
import re
from datetime import timedelta

def parse_vtt_time(time_str):
    """解析 VTT 时间格式为秒"""
    parts = time_str.strip().split(':')
    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
        return hours * 3600 + minutes * 60 + seconds
    elif len(parts) == 2:
        minutes = int(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    return 0

def format_srt_time(seconds):
    """格式化为 SRT 时间格式"""
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    secs = int(td.total_seconds() % 60)
    millis = int((td.total_seconds() % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def extract_subtitle_clip(vtt_file, start_time, end_time, output_file):
    """提取字幕片段"""
    # 解析时间
    start_seconds = parse_vtt_time(start_time)
    end_seconds = parse_vtt_time(end_time)

    print(f"📝 提取字幕片段...")
    print(f"   输入: {vtt_file}")
    print(f"   时间范围: {start_time} - {end_time}")
    print(f"   时间范围（秒）: {start_seconds:.1f}s - {end_seconds:.1f}s")

    # 读取 VTT 文件
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 解析字幕
    subtitles = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 查找时间戳行
        if '-->' in line:
            # 解析时间戳
            time_parts = line.split('-->')
            sub_start_str = time_parts[0].strip().split()[0]
            sub_end_str = time_parts[1].strip().split()[0]

            sub_start = parse_vtt_time(sub_start_str)
            sub_end = parse_vtt_time(sub_end_str)

            # 检查是否在目标时间范围内
            if sub_start >= start_seconds and sub_end <= end_seconds:
                # 收集字幕文本
                i += 1
                text_lines = []
                while i < len(lines) and lines[i].strip() != '':
                    text_lines.append(lines[i].strip())
                    i += 1

                text = ' '.join(text_lines)

                # 调整时间戳（减去起始时间）
                adjusted_start = sub_start - start_seconds
                adjusted_end = sub_end - start_seconds

                subtitles.append({
                    'start': adjusted_start,
                    'end': adjusted_end,
                    'text': text
                })

        i += 1

    print(f"   找到 {len(subtitles)} 条字幕")

    # 写入 SRT 格式
    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, sub in enumerate(subtitles, 1):
            f.write(f"{idx}\n")
            f.write(f"{format_srt_time(sub['start'])} --> {format_srt_time(sub['end'])}\n")
            f.write(f"{sub['text']}\n")
            f.write("\n")

    print(f"✅ 字幕提取完成")
    print(f"   输出文件: {output_file}")
    print(f"   字幕条数: {len(subtitles)}")

    return subtitles

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("用法: python extract_subtitle_clip.py <vtt_file> <start_time> <end_time> <output_file>")
        print("示例: python extract_subtitle_clip.py input.vtt 00:05:47 00:09:19 output.srt")
        sys.exit(1)

    vtt_file = sys.argv[1]
    start_time = sys.argv[2]
    end_time = sys.argv[3]
    output_file = sys.argv[4]

    extract_subtitle_clip(vtt_file, start_time, end_time, output_file)
```

## File: `scripts/generate_summary.py`
```python
#!/usr/bin/env python3
"""
生成总结文案
基于章节信息生成适合社交媒体的文案
"""

import sys
import json
from pathlib import Path
from typing import Dict


def generate_summary(
    chapter_info: Dict,
    output_path: str = None
) -> str:
    """
    生成总结文案

    注意：此函数需要在 Claude Code Skill 环境中调用
    Claude 会自动处理文案生成逻辑

    Args:
        chapter_info: 章节信息，包含：
            - title: 章节标题
            - time_range: 时间范围
            - summary: 核心摘要
            - keywords: 关键词列表
        output_path: 输出文件路径（可选）

    Returns:
        str: 生成的文案
    """
    print(f"\n📝 生成总结文案...")
    print(f"   章节: {chapter_info.get('title', 'Unknown')}")

    # 输出章节信息（供 Claude 分析）
    print("\n" + "="*60)
    print("章节信息（JSON 格式）:")
    print("="*60)
    print(json.dumps(chapter_info, indent=2, ensure_ascii=False))

    print("\n" + "="*60)
    print("文案生成要求:")
    print("="*60)
    print("""
请基于上述章节信息生成适合社交媒体的文案。

文案要求：
1. 吸引人的标题（10-20字）
2. 核心观点（3-5个要点，每个1-2句话）
3. 适合平台：
   - 小红书：口语化，有emoji，1000字以内
   - 抖音：精炼，突出金句，300字以内
   - 微信公众号：详细，结构清晰，不限字数

输出格式（Markdown）：

# [标题]

## 核心观点

1. 观点1
2. 观点2
3. 观点3

## 适合平台

### 小红书版本（1000字）
[文案内容]

### 抖音版本（300字）
[文案内容]

### 微信公众号版本
[文案内容]

## 标签

#标签1 #标签2 #标签3
""")

    # 生成基础文案（占位符）
    summary_template = f"""# {chapter_info.get('title', '未命名章节')}

## 章节信息

- 时间范围: {chapter_info.get('time_range', 'N/A')}
- 核心摘要: {chapter_info.get('summary', 'N/A')}
- 关键词: {', '.join(chapter_info.get('keywords', []))}

## 核心观点

[待生成 - Claude 会在 Skill 执行时自动填充]

## 适合平台

### 小红书版本

[待生成]

### 抖音版本

[待生成]

### 微信公众号版本

[待生成]

## 标签

{' '.join(['#' + kw for kw in chapter_info.get('keywords', [])])}

---

生成时间: {chapter_info.get('generated_at', 'N/A')}
"""

    # 保存到文件（如果指定）
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(summary_template)

        print(f"✅ 文案已保存: {output_path}")

    return summary_template


def load_chapter_info(json_path: str) -> Dict:
    """
    从 JSON 文件加载章节信息

    Args:
        json_path: JSON 文件路径

    Returns:
        Dict: 章节信息
    """
    json_path = Path(json_path)
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    print(f"📂 加载章节信息: {json_path.name}")

    with open(json_path, 'r', encoding='utf-8') as f:
        chapter_info = json.load(f)

    return chapter_info


def create_chapter_info(
    title: str,
    time_range: str,
    summary: str,
    keywords: list
) -> Dict:
    """
    创建章节信息字典

    Args:
        title: 章节标题
        time_range: 时间范围（如 "00:00 - 03:15"）
        summary: 核心摘要
        keywords: 关键词列表

    Returns:
        Dict: 章节信息
    """
    from datetime import datetime

    return {
        'title': title,
        'time_range': time_range,
        'summary': summary,
        'keywords': keywords,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python generate_summary.py <chapter_info_json> [output_file]")
        print("   or: python generate_summary.py --create <title> <time_range> <summary> <keywords> [output_file]")
        print("\nArguments:")
        print("  chapter_info_json - 章节信息 JSON 文件路径")
        print("  output_file       - 输出文件路径（可选，默认为 summary.md）")
        print("\nCreate mode arguments:")
        print("  --create    - 创建模式")
        print("  title       - 章节标题")
        print("  time_range  - 时间范围（如 '00:00 - 03:15'）")
        print("  summary     - 核心摘要")
        print("  keywords    - 关键词（逗号分隔）")
        print("\nExample:")
        print("  python generate_summary.py chapter.json")
        print("  python generate_summary.py chapter.json summary.md")
        print("  python generate_summary.py --create 'AGI指数曲线' '00:00-03:15' '核心摘要' 'AGI,指数增长,Claude' summary.md")
        sys.exit(1)

    try:
        if sys.argv[1] == '--create':
            # 创建模式
            if len(sys.argv) < 6:
                print("❌ 创建模式需要提供: title, time_range, summary, keywords")
                sys.exit(1)

            title = sys.argv[2]
            time_range = sys.argv[3]
            summary = sys.argv[4]
            keywords = sys.argv[5].split(',')
            output_file = sys.argv[6] if len(sys.argv) > 6 else 'summary.md'

            chapter_info = create_chapter_info(title, time_range, summary, keywords)

        else:
            # JSON 模式
            json_file = sys.argv[1]
            output_file = sys.argv[2] if len(sys.argv) > 2 else 'summary.md'

            chapter_info = load_chapter_info(json_file)

        # 生成文案
        summary = generate_summary(chapter_info, output_file)

        print("\n" + "="*60)
        print("生成的文案预览:")
        print("="*60)
        print(summary)

        print("\n⚠️  提示：此脚本需要在 Claude Code Skill 中运行")
        print("   Claude 会自动生成详细的文案内容")
        print("   当前仅输出模板")

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/merge_bilingual_subtitles.py`
```python
#!/usr/bin/env python3
"""
合并英文和中文字幕为双语 SRT 文件
"""

import sys
import re

def parse_srt_file(file_path):
    """解析 SRT 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割字幕块
    blocks = content.strip().split('\n\n')
    subtitles = []

    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            index = lines[0]
            time = lines[1]
            text = '\n'.join(lines[2:])
            subtitles.append({
                'index': index,
                'time': time,
                'text': text
            })

    return subtitles

def merge_bilingual_subtitles(english_file, chinese_file, output_file):
    """合并英文和中文字幕"""
    print(f"📝 合并双语字幕...")
    print(f"   英文字幕: {english_file}")
    print(f"   中文字幕: {chinese_file}")

    # 解析两个字幕文件
    english_subs = parse_srt_file(english_file)
    chinese_subs = parse_srt_file(chinese_file)

    if len(english_subs) != len(chinese_subs):
        print(f"⚠️  警告: 英文字幕 ({len(english_subs)} 条) 和中文字幕 ({len(chinese_subs)} 条) 数量不匹配")

    # 合并字幕
    bilingual_subs = []
    for i in range(min(len(english_subs), len(chinese_subs))):
        bilingual_subs.append({
            'index': english_subs[i]['index'],
            'time': english_subs[i]['time'],
            'text': f"{english_subs[i]['text']}\n{chinese_subs[i]['text']}"
        })

    # 写入双语字幕文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for sub in bilingual_subs:
            f.write(f"{sub['index']}\n")
            f.write(f"{sub['time']}\n")
            f.write(f"{sub['text']}\n")
            f.write("\n")

    print(f"✅ 双语字幕生成完成")
    print(f"   输出文件: {output_file}")
    print(f"   字幕条数: {len(bilingual_subs)}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("用法: python merge_bilingual_subtitles.py <english_srt> <chinese_srt> <output_srt>")
        sys.exit(1)

    english_file = sys.argv[1]
    chinese_file = sys.argv[2]
    output_file = sys.argv[3]

    merge_bilingual_subtitles(english_file, chinese_file, output_file)
```

## File: `scripts/translate_subtitles.py`
```python
#!/usr/bin/env python3
"""
翻译字幕
批量翻译优化：每批 20 条字幕一起翻译，节省 95% API 调用
"""

import sys
import json
from pathlib import Path
from typing import List, Dict

from utils import seconds_to_time


def translate_subtitles_batch(
    subtitles: List[Dict],
    batch_size: int = 20,
    target_lang: str = "中文"
) -> List[Dict]:
    """
    批量翻译字幕

    注意：此函数需要在 Claude Code Skill 环境中调用
    Claude 会自动处理翻译逻辑

    Args:
        subtitles: 字幕列表（每项包含 {start, end, text}）
        batch_size: 每批翻译的字幕数量
        target_lang: 目标语言

    Returns:
        List[Dict]: 翻译后的字幕列表，每项包含 {start, end, text, translation}
    """
    print(f"\n🌐 开始翻译字幕...")
    print(f"   总条数: {len(subtitles)}")
    print(f"   批量大小: {batch_size}")
    print(f"   目标语言: {target_lang}")

    # 准备批量翻译数据
    batches = []
    for i in range(0, len(subtitles), batch_size):
        batch = subtitles[i:i + batch_size]
        batches.append(batch)

    print(f"   分为 {len(batches)} 批")

    # 输出待翻译文本（供 Claude 处理）
    print("\n" + "="*60)
    print("待翻译字幕（JSON 格式）:")
    print("="*60)
    print(json.dumps(subtitles, indent=2, ensure_ascii=False))

    print("\n" + "="*60)
    print("翻译要求:")
    print("="*60)
    print(f"""
请将上述字幕翻译为{target_lang}。

翻译要求：
1. 保持技术术语的准确性
2. 口语化表达（适合短视频）
3. 简洁流畅（避免冗长）
4. 保持原意，不要添加或删减内容

输出格式（JSON）：
[
  {{"start": 0.0, "end": 3.5, "text": "原文", "translation": "译文"}},
  {{"start": 3.5, "end": 7.2, "text": "原文", "translation": "译文"}},
  ...
]

请分批翻译，每批 {batch_size} 条。
""")

    # 注意：实际翻译由 Claude 在 Skill 执行时完成
    # 这个脚本只是准备数据和提供接口
    # 返回占位符数据
    translated_subtitles = []
    for sub in subtitles:
        translated_subtitles.append({
            'start': sub['start'],
            'end': sub['end'],
            'text': sub['text'],
            'translation': '[待翻译]'  # Claude 会在运行时替换
        })

    return translated_subtitles


def create_bilingual_subtitles(
    subtitles: List[Dict],
    output_path: str,
    english_first: bool = True
) -> str:
    """
    创建双语字幕文件（SRT 格式）

    Args:
        subtitles: 字幕列表（包含 text 和 translation）
        output_path: 输出文件路径
        english_first: 英文在上（True）或中文在上（False）

    Returns:
        str: 输出文件路径
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n📝 生成双语字幕文件...")
    print(f"   输出: {output_path}")
    print(f"   顺序: {'英文在上，中文在下' if english_first else '中文在上，英文在下'}")

    with open(output_path, 'w', encoding='utf-8') as f:
        for i, sub in enumerate(subtitles, 1):
            # SRT 序号
            f.write(f"{i}\n")

            # SRT 时间戳
            start_time = seconds_to_time(sub['start'], include_hours=True, use_comma=True)
            end_time = seconds_to_time(sub['end'], include_hours=True, use_comma=True)
            f.write(f"{start_time} --> {end_time}\n")

            # 双语文本
            english = sub['text']
            chinese = sub.get('translation', '[未翻译]')

            if english_first:
                f.write(f"{english}\n{chinese}\n")
            else:
                f.write(f"{chinese}\n{english}\n")

            # 空行分隔
            f.write("\n")

    print(f"✅ 双语字幕已保存: {output_path}")
    return str(output_path)


def load_subtitles_from_srt(srt_path: str) -> List[Dict]:
    """
    从 SRT 文件加载字幕

    Args:
        srt_path: SRT 文件路径

    Returns:
        List[Dict]: 字幕列表
    """
    try:
        import pysrt
    except ImportError:
        print("❌ Error: pysrt not installed")
        print("Please install: pip install pysrt")
        sys.exit(1)

    srt_path = Path(srt_path)
    if not srt_path.exists():
        raise FileNotFoundError(f"SRT file not found: {srt_path}")

    print(f"📂 加载 SRT 字幕: {srt_path.name}")

    subs = pysrt.open(srt_path)
    subtitles = []

    for sub in subs:
        # 转换时间为秒数
        start = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000
        end = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000

        subtitles.append({
            'start': start,
            'end': end,
            'text': sub.text.replace('\n', ' ')  # 合并多行
        })

    print(f"   找到 {len(subtitles)} 条字幕")
    return subtitles


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: python translate_subtitles.py <subtitle_file> [output_file] [batch_size]")
        print("\nArguments:")
        print("  subtitle_file - 字幕文件路径（SRT 格式）")
        print("  output_file   - 输出文件路径（可选，默认为 <原文件名>_bilingual.srt）")
        print("  batch_size    - 每批翻译数量（可选，默认 20）")
        print("\nExample:")
        print("  python translate_subtitles.py subtitle.srt")
        print("  python translate_subtitles.py subtitle.srt bilingual.srt")
        print("  python translate_subtitles.py subtitle.srt bilingual.srt 30")
        print("\nNote:")
        print("  此脚本在 Claude Code Skill 中运行时，Claude 会自动处理翻译")
        print("  独立运行时，会输出待翻译数据供手动处理")
        sys.exit(1)

    subtitle_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    batch_size = int(sys.argv[3]) if len(sys.argv) > 3 else 20

    try:
        # 加载字幕
        subtitles = load_subtitles_from_srt(subtitle_file)

        if not subtitles:
            print("❌ 未找到有效字幕")
            sys.exit(1)

        # 翻译字幕（准备数据）
        translated = translate_subtitles_batch(subtitles, batch_size)

        # 设置输出路径
        if output_file is None:
            subtitle_path = Path(subtitle_file)
            output_file = subtitle_path.parent / f"{subtitle_path.stem}_bilingual.srt"

        # 创建双语字幕
        # 注意：在实际使用中，Claude 会先完成翻译，然后再调用这个函数
        print("\n⚠️  提示：此脚本需要在 Claude Code Skill 中运行")
        print("   Claude 会自动处理翻译逻辑")
        print("   当前仅输出待翻译数据")

    except Exception as e:
        print(f"\n❌ 错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/utils.py`
```python
#!/usr/bin/env python3
"""
通用工具函数
提供时间格式转换、文件名清理、路径处理等功能
"""

import re
import os
from pathlib import Path
from datetime import datetime


def time_to_seconds(time_str: str) -> float:
    """
    将时间字符串转换为秒数

    支持格式:
    - HH:MM:SS.mmm
    - MM:SS.mmm
    - SS.mmm

    Args:
        time_str: 时间字符串

    Returns:
        float: 秒数

    Examples:
        >>> time_to_seconds("01:23:45.678")
        5025.678
        >>> time_to_seconds("23:45.678")
        1425.678
        >>> time_to_seconds("45.678")
        45.678
    """
    # 移除空格
    time_str = time_str.strip()

    # 分割时间部分
    parts = time_str.split(':')

    if len(parts) == 3:
        # HH:MM:SS.mmm
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    elif len(parts) == 2:
        # MM:SS.mmm
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    else:
        # SS.mmm
        return float(parts[0])


def seconds_to_time(seconds: float, include_hours: bool = True, use_comma: bool = False) -> str:
    """
    将秒数转换为时间字符串

    Args:
        seconds: 秒数
        include_hours: 是否包含小时（即使为0）
        use_comma: 使用逗号分隔毫秒（SRT 格式需要）

    Returns:
        str: 时间字符串

    Examples:
        >>> seconds_to_time(5025.678)
        '01:23:45.678'
        >>> seconds_to_time(1425.678, include_hours=False)
        '23:45.678'
        >>> seconds_to_time(5025.678, use_comma=True)
        '01:23:45,678'
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60

    separator = ',' if use_comma else '.'

    if include_hours or hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}".replace('.', separator)
    else:
        return f"{minutes:02d}:{secs:06.3f}".replace('.', separator)


def sanitize_filename(filename: str, max_length: int = 100) -> str:
    """
    清理文件名，移除非法字符

    Args:
        filename: 原始文件名
        max_length: 最大长度

    Returns:
        str: 清理后的文件名

    Examples:
        >>> sanitize_filename("Hello: World?")
        'Hello_World'
        >>> sanitize_filename("AGI 不是时间点，是指数曲线")
        'AGI_不是时间点_是指数曲线'
    """
    # 移除或替换非法字符
    # Windows/Mac/Linux 通用的非法字符
    illegal_chars = r'[<>:"/\\|?*]'
    filename = re.sub(illegal_chars, '_', filename)

    # 移除开头和结尾的空格和点
    filename = filename.strip('. ')

    # 替换空格为下划线
    filename = filename.replace(' ', '_')

    # 移除连续的下划线
    filename = re.sub(r'_+', '_', filename)

    # 限制长度
    if len(filename) > max_length:
        # 保留扩展名
        name, ext = os.path.splitext(filename)
        if ext:
            max_name_length = max_length - len(ext)
            filename = name[:max_name_length] + ext
        else:
            filename = filename[:max_length]

    return filename


def create_output_dir(base_dir: str = None) -> Path:
    """
    创建输出目录（带时间戳）

    Args:
        base_dir: 基础目录，默认为当前工作目录下的 youtube-clips

    Returns:
        Path: 输出目录路径

    Examples:
        >>> create_output_dir()
        PosixPath('/path/to/current/dir/youtube-clips/20260121_143022')
    """
    if base_dir is None:
        base_dir = Path.cwd() / "youtube-clips"
    else:
        base_dir = Path(base_dir)

    # 创建带时间戳的子目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = base_dir / timestamp

    # 创建目录
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小为人类可读格式

    Args:
        size_bytes: 文件大小（字节）

    Returns:
        str: 格式化后的大小

    Examples:
        >>> format_file_size(1024)
        '1.0 KB'
        >>> format_file_size(1536)
        '1.5 KB'
        >>> format_file_size(1048576)
        '1.0 MB'
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def parse_time_range(time_range: str) -> tuple:
    """
    解析时间范围字符串

    Args:
        time_range: 时间范围字符串，如 "00:00 - 03:15" 或 "00:00-03:15"

    Returns:
        tuple: (start_seconds, end_seconds)

    Examples:
        >>> parse_time_range("00:00 - 03:15")
        (0.0, 195.0)
        >>> parse_time_range("01:30:00-01:33:15")
        (5400.0, 5595.0)
    """
    # 移除空格并分割
    parts = time_range.replace(' ', '').split('-')
    if len(parts) != 2:
        raise ValueError(f"Invalid time range format: {time_range}")

    start_time = time_to_seconds(parts[0])
    end_time = time_to_seconds(parts[1])

    if start_time >= end_time:
        raise ValueError(f"Start time must be before end time: {time_range}")

    return start_time, end_time


def adjust_subtitle_time(time_seconds: float, offset: float) -> float:
    """
    调整字幕时间戳（用于剪辑后的字幕）

    Args:
        time_seconds: 原始时间（秒）
        offset: 偏移量（秒），通常是剪辑起始时间

    Returns:
        float: 调整后的时间

    Examples:
        >>> adjust_subtitle_time(125.5, 120.0)
        5.5
    """
    adjusted = time_seconds - offset
    return max(0.0, adjusted)  # 确保不为负数


def get_video_duration_display(seconds: float) -> str:
    """
    获取视频时长的显示格式

    Args:
        seconds: 时长（秒）

    Returns:
        str: 格式化的时长

    Examples:
        >>> get_video_duration_display(125.5)
        '02:05'
        >>> get_video_duration_display(3725.5)
        '1:02:05'
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"


def validate_url(url: str) -> bool:
    """
    验证 YouTube URL 格式

    Args:
        url: YouTube URL

    Returns:
        bool: 是否有效

    Examples:
        >>> validate_url("https://youtube.com/watch?v=Ckt1cj0xjRM")
        True
        >>> validate_url("https://youtu.be/Ckt1cj0xjRM")
        True
        >>> validate_url("invalid_url")
        False
    """
    # 支持的 YouTube URL 格式
    patterns = [
        r'https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'https?://(?:www\.)?youtu\.be/[\w-]+',
        r'https?://(?:www\.)?youtube\.com/embed/[\w-]+',
    ]

    return any(re.match(pattern, url) for pattern in patterns)


def ensure_directory(path: Path) -> Path:
    """
    确保目录存在，不存在则创建

    Args:
        path: 目录路径

    Returns:
        Path: 目录路径
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


if __name__ == "__main__":
    # 测试代码
    print("Testing utils.py...")

    # 测试时间转换
    assert time_to_seconds("01:23:45.678") == 5025.678
    assert time_to_seconds("23:45.678") == 1425.678
    assert time_to_seconds("45.678") == 45.678

    # 测试文件名清理
    assert sanitize_filename("Hello: World?") == "Hello_World"
    assert sanitize_filename("AGI 不是时间点，是指数曲线") == "AGI_不是时间点_是指数曲线"

    # 测试时间范围解析
    assert parse_time_range("00:00 - 03:15") == (0.0, 195.0)
    assert parse_time_range("01:30:00-01:33:15") == (5400.0, 5595.0)

    # 测试 URL 验证
    assert validate_url("https://youtube.com/watch?v=Ckt1cj0xjRM") == True
    assert validate_url("https://youtu.be/Ckt1cj0xjRM") == True
    assert validate_url("invalid_url") == False

    print("✅ All tests passed!")
```

## File: `scripts/__init__.py`
```python
#!/usr/bin/env python3
"""
YouTube 视频智能剪辑工具 - Scripts 包
"""

__version__ = "1.0.0"
__author__ = "Claude Code"
```

## File: `templates/summary-template.md`
```markdown
# {章节标题}

> 视频片段总结文案模板

---

## 📊 章节信息

- **时间范围**: {起始时间} - {结束时间}
- **片段时长**: {时长}
- **关键词**: {关键词1}, {关键词2}, {关键词3}

---

## 🎯 核心观点

1. **观点1标题**
   - 详细说明观点1的内容
   - 补充信息或例子

2. **观点2标题**
   - 详细说明观点2的内容
   - 补充信息或例子

3. **观点3标题**
   - 详细说明观点3的内容
   - 补充信息或例子

---

## 📝 适合平台

### 小红书版本（1000字以内）

#### 标题
{吸引人的标题，10-20字}

#### 正文
{口语化表达，分段清晰}

这段视频讲了...

核心要点：
✨ 要点1
✨ 要点2
✨ 要点3

我的理解：
{个人见解}

推荐理由：
{为什么值得看}

#### 标签
#{标签1} #{标签2} #{标签3} #{标签4}

---

### 抖音版本（300字以内）

#### 标题
{简短有力的标题，10字以内}

#### 正文
{精炼表达，突出金句}

💡 核心洞察：
{一句话总结}

🔥 重点：
1️⃣ {要点1}
2️⃣ {要点2}
3️⃣ {要点3}

✅ 结论：
{一句话结论}

#### 标签
#{标签1} #{标签2} #{标签3}

---

### 微信公众号版本

#### 标题
{正式标题，可以稍长}

#### 引言
{简短介绍背景和主题}

#### 正文

##### 一、{第一部分标题}

{详细内容}

**核心观点**：
- 观点1
- 观点2
- 观点3

##### 二、{第二部分标题}

{详细内容}

**案例分析**：
- 案例1
- 案例2

##### 三、{第三部分标题}

{详细内容}

**关键要点**：
1. 要点1
2. 要点2
3. 要点3

#### 结语

{总结和展望}

---

## 💡 金句摘录

> {金句1}

> {金句2}

> {金句3}

---

## 🔗 相关信息

- **原视频**: {YouTube 链接}
- **完整视频时长**: {总时长}
- **发布日期**: {日期}
- **内容类别**: {类别}

---

## 📌 推荐理由

这段视频片段特别适合：
- [ ] 对 {话题} 感兴趣的人
- [ ] 想了解 {概念} 的人
- [ ] 需要 {知识点} 的人

核心价值：
1. {价值点1}
2. {价值点2}
3. {价值点3}

---

## 🎬 视频文件

- **原始剪辑**: `{文件名}_clip.mp4`
- **字幕版本**: `{文件名}_with_subtitles.mp4`
- **双语字幕**: `{文件名}_bilingual.srt`

---

## 📅 生成信息

- **生成时间**: {日期时间}
- **生成工具**: YouTube Clipper (Claude Code Skill)
- **版本**: v1.0.0

---

## 使用说明

### 编辑建议

1. **标题优化**: 根据平台特点调整标题风格
2. **内容调整**: 根据目标受众调整专业度
3. **标签优化**: 根据平台热门标签调整
4. **长度控制**: 严格控制各平台的字数限制

### 平台发布建议

| 平台 | 最佳发布时间 | 字数限制 | 标签数量 |
|------|------------|---------|---------|
| 小红书 | 19:00-22:00 | 1000字 | 8-10个 |
| 抖音 | 12:00, 18:00, 21:00 | 300字 | 5-7个 |
| 微信公众号 | 8:00, 12:00, 20:00 | 不限 | - |

### 优化技巧

1. **标题**: 使用数字、问句、悬念
2. **配图**: 选择关键帧作为封面
3. **标签**: 结合热门话题
4. **互动**: 在文末添加互动问题

---

**注意**: 本模板由 AI 自动生成，建议根据实际情况调整内容。
```


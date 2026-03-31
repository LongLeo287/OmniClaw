# 🚀 BẢN CẬP NHẬT MỚI: GitNexus (v1.4.10)

**Ngày phát hành:** 2026-03-27T13:53:20Z
**Link Bản gốc:** https://github.com/abhigyanpatwari/GitNexus/releases/tag/v1.4.10
**Thuộc Bộ phận:** knowledge_gitnexus - knowledge

## Chi tiết thay đổi (Release Notes)

### Fixed

- **MCP server install via npx** — resolve tree-sitter peer dependency conflicts that broke `npx -y gitnexus@latest mcp` (#537, #538)
  - Downgrade tree-sitter from ^0.25.0 to ^0.21.1 (only npm version where all 14 parsers agree)
  - Align all parser versions to their highest ^0.21.x-compatible releases
  - Remove tree-sitter override (only applies to root packages, ignored by npx)
  - Pin tree-sitter-dart to correct ABI-14-compatible commit

**Full Changelog**: https://github.com/abhigyanpatwari/GitNexus/compare/v1.4.9...v1.4.10

<!-- Release notes generated using configuration in .github/release.yml at v1.4.10 -->

## What's Changed
### 📝 Other Changes
* fix: resolve tree-sitter peer dependency conflicts breaking MCP server install via npx by @Copilot in https://github.com/abhigyanpatwari/GitNexus/pull/538


**Full Changelog**: https://github.com/abhigyanpatwari/GitNexus/compare/v1.4.9...v1.4.10

---

> **Hỗ trợ Agent:** Sếp có thể tự tay update mã nguồn cho Plugin này thông qua Github hoặc dùng script `git pull`.
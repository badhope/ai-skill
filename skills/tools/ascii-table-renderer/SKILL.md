---
name: ascii-table-renderer
version: 1.0.0
description: "Render structured data as aligned ASCII tables (column width rules, truncate/wrap, border styles, compact/readable variants) for terminal/log/email."
author: Fullstack Skills Community
category: tools
tags: [ascii-table-renderer]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----+----------+--------+
| Name  | Role     | Status |
+-------+----------+--------+
| Alice | Engineer | Active |
| Bob   | Designer | Away   |
+-------+----------+--------+
```

## Examples
- `examples/basic.md`

## Quality checklist
1. Columns align consistently; each line does not exceed maxWidth
2. Null values are rendered as `-`
3. Copy/paste safe (no trailing spaces)

## Keywords
**English:** ascii-table-renderer, ascii table, align, columns, rows, truncate, wrap, terminal, log
**中文:** ascii-table-renderer, ASCII 表格, 对齐, 列宽, 截断, 换行, 终端, 日志, 工单

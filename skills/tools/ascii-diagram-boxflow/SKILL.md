---
name: ascii-diagram-boxflow
version: 1.0.0
description: "Generate plain ASCII box-flow diagrams (boxes + arrows) for environments without renderers, with alignment rules and split strategies for complex graphs."
author: Fullstack Skills Community
category: tools
tags: [ascii-diagram-boxflow]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-------------+
|     Login      |
+----------------+
        |
        v
+----------------+
|   Validate     |
+----------------+
        |
        v
+----------------+
|   Dashboard    |
+----------------+
```

Long name truncation (boxWidth=16): `"Authentication Service"` becomes `"Authenticati..."`.

## Quality checklist
1. Arrow direction is unambiguous; avoid crossings
2. Line width `<= width`; no trailing spaces
3. Long node names must be truncated or wrapped consistently

## Keywords
**English:** ascii-diagram-boxflow, ascii diagram, flowchart, box, arrow, plain text, terminal
**中文:** ascii-diagram-boxflow, ASCII 框图, 流程图, 纯文本, 盒子, 箭头, 终端

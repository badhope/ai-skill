---
name: pencil-ui-designer
version: 1.0.0
description: "Orchestrates Pencil design system initialization by routing framework requests to the correct pencil-ui-design-system-* skill. Use when the user explicitly mentions Pencil and wants to initialize a design system (antd, Bootstrap, Element Plus, Layui, uView, Vant, uCharts, ECharts), set up component libraries, or create design tokens in a .pen file."
author: Fullstack Skills Community
category: tools
tags: [pencil-ui-designer]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

|---|
| `layui`, `layui-vue` | `pencil-ui-design-system-layui` |
| `antd`, `ant design` | `pencil-ui-design-system-antd` |
| `bootstrap` | `pencil-ui-design-system-bootstrap` |
| `element`, `element-plus` | `pencil-ui-design-system-element` |
| `uview` (2.x) | `pencil-ui-design-system-uview` |
| `uview pro`, `uviewpro` | `pencil-ui-design-system-uviewpro` |
| `vant`, `vant 4` | `pencil-ui-design-system-vant` |
| `ucharts`, `qiun-data-charts` | `pencil-ui-design-system-ucharts` |
| `echarts` | `pencil-ui-design-system-echarts` |

### 3) Execution

Invoke the target skill which generates a PENCIL_PLAN: a sequence of Pencil MCP tool calls (`open_document` -> `set_variables` -> `batch_design` -> `get_screenshot`).

### 4) Output

Return the structured plan (JSON/Action List) to the user for execution or approval.

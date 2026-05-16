
# SKILL.md 格式规范

## YAML Frontmatter 元数据

每个 SKILL.md 文件必须以 YAML Frontmatter 开头，包含以下字段：

### 必填字段

| 字段 | 类型 | 描述 | 示例 |
|------|------|------|------|
| `name` | string | 技能名称（小写，连字符分隔） | `code-reviewer` |
| `version` | string | 版本号（语义化版本） | `1.0.0` |
| `description` | string | 简洁描述（1-2句话） | `代码审查和最佳实践检查` |
| `category` | string | 分类名称 | `development` |

### 可选字段

| 字段 | 类型 | 描述 | 示例 |
|------|------|------|------|
| `author` | string | 作者名称 | `badhope` |
| `tags` | array | 标签数组 | `["code-review", "quality"]` |
| `allowed-tools` | array | 允许使用的工具 | `["Read", "Write"]` |
| `requires` | array | 依赖的其他技能 | `["base-skill"]` |

### 完整示例

```markdown
---
name: code-reviewer
version: 1.0.0
description: 代码审查和最佳实践检查，帮助提高代码质量
author: badhope
category: development
tags: [code-review, quality, best-practices]
allowed-tools: [Read, Write, Grep]
---
```

## 文档结构

### 推荐章节顺序

1. **概述** - 技能介绍
2. **何时使用** - 适用场景
3. **何时不使用** - 不适用场景
4. **工作流程** - 分阶段描述
5. **核心原则** - 重要原则
6. **使用示例** - 具体示例
7. **最佳实践** - 实践建议
8. **常见问题** - FAQ
9. **参考资料** - 相关链接

## 渐进式披露

技能采用三级渐进式加载机制：

### Level 1: 元数据（始终加载）

仅加载 YAML Frontmatter，包含：
- name
- description
- category
- tags

消耗：约 50-100 tokens

### Level 2: 完整指令（按需加载）

当技能相关时加载完整 SKILL.md 内容

消耗：约 500-2000 tokens

### Level 3: 资源文件（仅在引用时加载）

- scripts/ - 脚本文件
- templates/ - 模板文件
- assets/ - 资源文件

消耗：按需加载

## 分类列表

| 分类 | 目录 | 描述 |
|------|------|------|
| `development` | `skills/development/` | 开发类技能 |
| `product` | `skills/product/` | 产品类技能 |
| `design` | `skills/design/` | 设计类技能 |
| `data` | `skills/data/` | 数据类技能 |
| `ai` | `skills/ai/` | AI 类技能 |
| `docs` | `skills/docs/` | 文档类技能 |
| `devops` | `skills/devops/` | 运维类技能 |
| `tools` | `skills/tools/` | 工具类技能 |
| `business` | `skills/business/` | 商业类技能 |
| `learning` | `skills/learning/` | 学习类技能 |

## 技能目录结构

```
skill-name/
├── SKILL.md              # 技能定义（必需）
├── README.md             # 额外文档（可选）
├── scripts/              # 可执行脚本（可选）
│   ├── main.py
│   └── helper.sh
├── templates/            # 模板文件（可选）
│   └── template.md
├── assets/               # 资源文件（可选）
│   └── diagram.png
└── tests/                # 测试文件（可选）
    └── test_skill.py
```

## 编写指南

### 1. 保持简洁

- 元数据描述 1-2 句话
- 每个章节重点突出
- 避免冗余信息

### 2. 使用清晰的结构

- 使用标题层级
- 列表和表格增强可读性
- 代码块提供示例

### 3. 提供具体示例

- 真实场景的例子
- 可运行的代码片段
- 输入输出示例

### 4. 渐进式披露设计

- 元数据足够用于初步判断
- 详细内容按需加载
- 大文件放在 assets/ 中

## 验证工具

可以使用以下工具验证 SKILL.md 格式：

```bash
# 检查 YAML 语法
yamllint SKILL.md

# 检查 Markdown 格式
markdownlint SKILL.md
```

## 示例

完整的示例技能请参考：
- [code-reviewer](../skills/development/code-reviewer/SKILL.md)
- [file-organizer](../skills/tools/file-organizer/SKILL.md)

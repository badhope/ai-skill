
# 万能技能格式规范 (Universal Skill Format)

## 概述

这是一个跨平台、兼容性强的技能格式规范，适用于：
- Claude Code / Claude.ai
- Cursor
- Gemini CLI
- AI Studio
- 其他任何支持 Agent Skills 的平台

## 格式说明

### 基础结构

```
skill-name/
├── SKILL.md           # 技能主文件（必须）
├── README.md          # 附加文档（可选）
├── scripts/           # 可执行脚本（可选）
│   ├── main.py        # Python 脚本
│   └── helper.sh      # Shell 脚本
├── references/        # 参考文档（可选）
│   ├── patterns.md    # 详细模式说明
│   └── examples.md    # 使用示例
├── assets/            # 资源文件（可选）
│   ├── template.pdf   # 模板文件
│   └── fonts/         # 字体文件
└── tests/             # 测试文件（可选）
    └── test_skill.py
```

### SKILL.md 格式

#### YAML Frontmatter（元数据头）

```markdown
---
name: skill-name                          # 必须：技能标识符（小写，连字符分隔）
version: 1.0.0                           # 推荐：语义化版本号
description: 简短描述何时使用该技能，包含触发关键词  # 必须：技能描述（50-200字）
author: Author Name                      # 可选：作者姓名
category: development                    # 推荐：技能分类
tags: [tag1, tag2, tag3]                 # 可选：标签数组
license: MIT                             # 可选：许可证
allowed-tools: [tool1, tool2]            # 可选：允许使用的工具
platforms: [claude, cursor, gemini]      # 可选：支持的平台
compatibility: "Python 3.8+, Linux/macOS" # 可选：兼容性说明
---
```

#### 内容结构

```markdown
# 技能名称

## 概述
详细说明技能的功能和用途（1-2段）

## 何时使用
- 列出明确的使用场景
- 使用关键词帮助触发
- 具体而不是模糊

## 何时不使用
- 列出不适用的场景
- 避免误用

## 工作流程
### 阶段 1: [阶段名称]
- 步骤说明
- 具体操作

### 阶段 2: [阶段名称]
- 步骤说明
- 具体操作

## 核心原则
1. 原则一说明
2. 原则二说明

## 使用示例
### 示例 1: [示例名称]
```
具体示例代码或对话
```

## 最佳实践
- 实践建议 1
- 实践建议 2

## 常见问题
### Q: 问题？
A: 答案

## 参考资料
- [链接 1](url)
- [链接 2](url)
```

## 分类标准

### 一级分类

1. **development** - 开发类
   - 代码审查
   - 开发工作流
   - 测试
   - 重构
   - 调试

2. **product** - 产品类
   - PRD 写作
   - 需求分析
   - 用户故事

3. **design** - 设计类
   - UI 设计
   - 设计系统
   - 原型制作

4. **data** - 数据类
   - 数据分析
   - 数据库设计
   - API 设计

5. **ai** - AI 类
   - 提示词工程
   - 技能创建
   - Agent 设计

6. **docs** - 文档类
   - 技术文档
   - 博客写作

7. **devops** - 运维类
   - CI/CD
   - 容器化
   - 监控

8. **tools** - 工具类
   - 文件操作
   - 自动化
   - 实用工具

9. **business** - 商业类
   - 市场分析
   - 商业计划

10. **learning** - 学习类
    - 概念解释
    - 教程指导

## 渐进式披露原则

1. **Level 1 (Metadata)** - YAML frontmatter 中的 name 和 description
   - 始终加载
   - ~50-100 tokens
   - 用于技能选择

2. **Level 2 (Body)** - SKILL.md 的 Markdown 内容
   - 技能触发时加载
   - 理想情况下 &lt; 500 行
   - 提供完整指令

3. **Level 3 (Resources)** - 附加文件（references/, scripts/, assets/）
   - 按需加载
   - 无大小限制
   - 通过 SKILL.md 中的链接引用

## 平台兼容性

### Claude 平台
- 完整支持所有字段
- 需要 name 和 description
- 可选 license 字段

### Cursor 平台
- 完整支持
- 自动检测并使用

### Gemini CLI
- 兼容基础格式
- 扩展字段被忽略

## 许可证说明

- MIT - 推荐用于社区技能
- Apache 2.0 - 适用于企业技能
- Proprietary - 适用于私有技能
- Custom - 自定义许可证

## 验证清单

发布技能前检查：
- [ ] SKILL.md 存在
- [ ] YAML frontmatter 格式正确
- [ ] name 和 description 字段完整
- [ ] 内容结构清晰
- [ ] 有至少一个使用示例
- [ ] 无恶意代码
- [ ] 适当的许可证

## 示例技能

参考以下标准技能：
- [file-organizer](../skills/tools/file-organizer/SKILL.md)
- [code-reviewer](../skills/development/code-reviewer/SKILL.md)
- [prd-writer](../skills/product/prd-writer/SKILL.md)


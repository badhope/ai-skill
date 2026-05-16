# 项目结构说明

## 项目根目录

```
AI-SKILL/
├── .claude-plugin/          # Claude Code 插件配置
│   └── marketplace.json    # Claude 市场配置文件
├── .github/              # GitHub 社区文件
│   ├── ISSUE_TEMPLATE/  # Issue 模板
│   └── PULL_REQUEST_TEMPLATE.md  # PR 模板
├── examples/             # 示例文件
├── scripts/              # 项目脚本目录
├── skills/             # 技能目录（核心内容）
│   ├── ai/           # AI & 代理技能
│   ├── business/       # 商业技能
│   ├── compliance/     # 合规技能
│   ├── data/         # 数据技能
│   ├── design/       # 设计技能
│   ├── development/  # 开发技能
│   ├── devops/       # DevOps技能
│   ├── docs/         # 文档技能
│   ├── finance/       # 金融技能
│   ├── knowledge/    # 知识管理技能
│   ├── leadership/   # 领导力技能
│   ├── product/      # 产品技能
│   ├── tools/        # 工具技能
│   ├── all_skills.json      # 完整技能列表
│   ├── by_category.json   # 按分类索引
│   ├── by_platform.json  # 按平台索引
│   ├── by_keyword.json   # 按关键词索引
│   ├── index.html        # 可视化导航页面
│   └── index.json        # 主索引文件
├── vendor/             # 供应商（原始技能来源
├── CHANGELOG.md        # 变更日志
├── CODE_OF_CONDUCT.md  # 行为准则
├── CONTRIBUTING.md      # 贡献指南
├── GIT_SYNC.md      # Git 同步指南
├── LICENSE          # 许可证
├── README.md        # 主文档
├── QUICKSTART.md    # 快速开始指南
├── SECURITY.md      # 安全策略
├── SKILL_TEMPLATE.md  # 技能创建模板
├── config.example.json  # 配置示例
└── .gitignore        # Git 忽略文件
```

## 目录详解

### skills/ - 技能目录

这是项目的核心，包含所有 2200+ 技能。

```
skills/
├── [分类]/
│   └── [技能名称]/
│       ├── SKILL.md         # 技能主体文件
│       ├── examples/      # 示例
│       ├── scripts/      # 脚本
│       └── references/ # 参考
```

### scripts/ - 脚本目录

包含所有项目的自动化脚本。

```
scripts/
├── build_index.py         # 构建索引
├── dedup.py          # 去重
├── publish.py         # 发布工具
└── ...
```

### vendor/ - 供应商来源

原始技能来源目录，包含原始技能仓库。

## 主要来源列表：

- `antigravity-awesome-skills
- `AI-Research-SKILLs
- `agent-skills-hub
- `agent-skills-library
- `anthropic-skills
- `mattpocock-skills
- `alirezarezvani-skills
- `fullstack-skills
- `spring-ai-agent-utils
- `stitch-skills

## 索引系统

我们有几个关键的索引系统：

- `all_skills.json`: 完整的完整列表
- `by_category.json`: 按分类索引
- `by_platform.json`: 按平台索引
- `by_keyword.json`: 按关键词索引
- `index.html`: 可视化导航（带搜索）
- `index.json`: 主索引

## 技能格式

所有技能使用统一格式，包含：

```yaml
---
name: skill-name
version: 1.0.0
description: 描述
author: 作者
category: 分类
tags: [标签]
license: MIT
platforms: [平台列表]
---

# 技能标题

## 概述
...

## 使用场景
...

## 使用方法
...
```

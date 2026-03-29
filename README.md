# ai-skill - Woclaw 技能仓库 🌟

> Woclaw 启明星 AI 助手的官方技能存储库

[English](README_en.md) | [中文](README.md) | [日本語](README_ja.md)

---

## ✨ 什么是 ai-skill？

**ai-skill** 是 [Woclaw 启明星 AI 助手](https://github.com/badhope/Woclaw) 的官方技能仓库。

这里收录了所有可在 Woclaw 中使用的技能（Skills），让 Woclaw 能够完成各种特定任务。

## 🎯 快速开始

### 在 Woclaw 中安装技能

```bash
# 安装技能
woclaw skill install <skill-name>

# 示例：安装文件整理技能
woclaw skill install file-organizer

# 安装多个技能
woclaw skill install file-organizer screenshot-ocr habit-tracker
```

### 从 GitHub 直接安装

```bash
# 直接从 GitHub 安装
woclaw skill install badhope/ai-skill/file-organizer

# 指定分支
woclaw skill install badhope/ai-skill/web-scraper --branch main
```

## 📦 内置技能

### 文件处理类
| 技能 | 说明 | 命令 |
|------|------|------|
| `file-organizer` | 文件自动整理 | 按类型/日期整理文件 |
| `batch-rename` | 批量重命名 | 批量修改文件名 |
| `duplicate-finder` | 重复文件查找 | 查找并清理重复文件 |

### 截图识别类
| 技能 | 说明 | 命令 |
|------|------|------|
| `screenshot-ocr` | 截图文字识别 | 从截图提取文字 |
| `screenshot-translate` | 截图翻译 | 截图内容翻译 |

### 自动化类
| 技能 | 说明 | 命令 |
|------|------|------|
| `habit-tracker` | 习惯追踪 | 每日打卡、追踪进度 |
| `schedule-task` | 定时任务 | 定时执行任务 |
| `auto-backup` | 自动备份 | 定时备份重要文件 |

### 信息处理类
| 技能 | 说明 | 命令 |
|------|------|------|
| `web-scraper` | 网页抓取 | 自动抓取网页内容 |
| `rss-reader` | RSS 阅读器 | 聚合订阅源 |
| `news-digest` | 新闻摘要 | 每日新闻摘要 |

### 效率工具类
| 技能 | 说明 | 命令 |
|------|------|------|
| `quick-note` | 快捷笔记 | 快速记录想法 |
| `link-saver` | 链接收藏 | 收藏和管理链接 |
| `todo-list` | 待办清单 | 管理待办事项 |

## 🛠️ 开发自己的技能

### 技能结构

```
my-skill/
├── SKILL.md          # 技能定义（必需）
├── scripts/
│   └── run.py        # 技能执行脚本
├── config.json       # 技能配置
├── requirements.txt  # 依赖
└── README.md        # 说明文档
```

### SKILL.md 示例

```markdown
# 我的技能

## 基本信息
- **名称**: my-skill
- **版本**: 1.0.0
- **作者**: 你的名字
- **描述**: 这个技能做什么

## 使用方法
`woclaw skill run my-skill --arg value`

## 参数说明
| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| --arg | string | 输入参数 | - |

## 示例
```bash
woclaw skill run my-skill --arg hello
```
```

### 发布技能

1. Fork 这个仓库
2. 在 `skills/` 目录下创建你的技能
3. 提交 Pull Request
4. 审核通过后合并

## 📁 目录结构

```
ai-skill/
├── README.md
├── README_en.md
├── README_ja.md
├── skills/           # 技能目录
│   ├── file-organizer/
│   ├── screenshot-ocr/
│   ├── habit-tracker/
│   └── ...
├── docs/             # 文档
├── scripts/         # 工具脚本
└── tests/           # 测试
```

## 🤝 贡献

欢迎提交新的技能！

### 贡献流程
1. Fork 仓库
2. 创建技能目录
3. 编写 SKILL.md
4. 提交 PR
5. 等待审核

### 技能审核标准
- ✅ SKILL.md 格式正确
- ✅ 有完整的使用说明
- ✅ 代码安全，无恶意行为
- ✅ 有适当的错误处理

## 📄 许可证

MIT License

## 🔗 相关链接

- [Woclaw 主仓库](https://github.com/badhope/Woclaw)
- [Woclaw 文档](https://github.com/badhope/Woclaw#readme)
- [问题反馈](https://github.com/badhope/Woclaw/issues)

---

<div align="center">

**⭐ 如果 ai-skill 对你有帮助，请给我们一个 Star！**

*让 Woclaw 更强大*

**Made with ✨ by Woclaw Team**

</div>

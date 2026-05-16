---
name: file-organizer
version: 1.0.0
description: 自动将文件夹中的文件按类型或日期分类整理
author: Woclaw Team
category: tools
tags: [file, organize, automation]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
allowed-tools: [Read, Write, Bash]
---

---|------|------|--------|
| `--directory` | string | 要整理的目录路径 | 必填 |
| `--mode` | string | 整理方式: type/date | `type` |
| `--dry-run` | flag | 预览模式，不实际移动 | `false` |

## 最佳实践

1. **先预览再执行** - 首次使用建议加 `--dry-run` 参数
2. **定期整理** - 设置每周/每月自动整理任务
3. **备份重要文件** - 整理前备份重要数据
4. **从简单开始** - 先在小文件夹测试，再用于大目录

## 常见问题

### Q: 会删除文件吗？

A: 不会！本技能只移动文件，从不删除任何内容。

### Q: 如果目标文件夹已有同名文件怎么办？

A: 会自动重命名为 `file_1.ext`, `file_2.ext` 等格式。

### Q: 可以撤销整理操作吗？

A: 当前版本不支持自动撤销，但会记录操作日志。未来版本将添加撤销功能。

### Q: 会处理子文件夹吗？

A: 当前版本只处理目标目录的顶层文件，不递归处理子文件夹。

## 参考资料

- [Python Pathlib 文档](https://docs.python.org/3/library/pathlib.html)
- [Shutil 模块文档](https://docs.python.org/3/library/shutil.html)

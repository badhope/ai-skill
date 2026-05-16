---
name: screenshot-ocr
version: 1.0.0
description: 从截图中提取文字内容，支持多种语言识别
author: Woclaw Team
category: tools
tags: [screenshot, ocr, text, extraction]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
allowed-tools: [Read, Write]
---

------|------|------|
| 产品A | ¥99 | 100 |
| 产品B | ¥199 | 50 |

需要格式化输出吗？
```

## 最佳实践

1. **提高图片质量** - 确保文字清晰无模糊
2. **正确设置语言** - 选择正确的识别语言
3. **验证结果** - 检查并修正识别错误
4. **保留原文** - 保存原始图片以备后续参考

## 常见问题

### Q: 识别准确率不高怎么办？

A: 尝试提高图片质量、增加对比度、确保文字方向正确。

### Q: 支持哪些语言？

A: 主要支持中文、英文、日文、韩文等主流语言，具体取决于使用的OCR引擎。

### Q: 可以识别手写文字吗？

A: 对工整的手写文字有一定识别能力，但打印文字的识别效果更好。

## 参考资料

- [OCR基础介绍](https://en.wikipedia.org/wiki/Optical_character_recognition)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

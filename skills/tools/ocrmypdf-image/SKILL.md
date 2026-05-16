---
name: ocrmypdf-image
version: 1.0.0
description: OCRmyPDF image processing skill — deskew, rotate, clean, despeckle, remove border from scanned documents. Use when the user needs to improve scanned PDF quality, fix skewed pages, remove noise, or clean up scanned documents before OCR.
author: Fullstack Skills Community
category: tools
tags: [ocrmypdf-image]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

---|---------|
| Auto deskew | `--deskew` |
| Auto rotate | `--rotate-pages` |
| Remove borders | `--remove-bordering` |
| Remove speckles | `--despeckle` |
| Unpaper | `--unpaper` |
| Oversample DPI | `--oversample N` |

## Troubleshooting

- **Poor OCR after cleaning**: Try `--oversample 300` to increase input quality.
- **Artifacts remain**: Use `--unpaper` for aggressive cleanup.
- **Over-cleaned image**: Reduce cleaning options for preserve original quality.

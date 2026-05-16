---
name: ocrmypdf-batch
version: 1.0.0
description: OCRmyPDF batch processing skill — process multiple PDFs, Docker automation, shell scripting, and CI/CD integration. Use when the user needs to OCR many PDFs, set up automated OCR pipelines, or integrate OCR into workflows.
author: Fullstack Skills Community
category: tools
tags: [ocrmypdf-batch]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

---|---------|
| Sequential batch | `for f in *.pdf; do ocrmypdf "$f" out/"$f"; done` |
| Parallel batch | `parallel ocrmypdf {} out/{/} ::: *.pdf` |
| Docker basic | `docker run -v $(pwd):/data jbarlow83/ocrmypdf in.pdf out.pdf` |
| Recursive | `find . -name "*.pdf" -exec ocrmypdf {} out/{/} \;` |

## Troubleshooting

- **Permission denied**: Ensure output directory is writable.
- **Memory issues**: Process in smaller batches or use `--jobs 1`.
- **Docker path issues**: Use absolute paths with `-v`.

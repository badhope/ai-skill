---
name: ocrmypdf-optimize
version: 1.0.0
description: OCRmyPDF optimization skill — compress PDFs, configure PDF/A output, JBIG2 encoding, and lossless optimization. Use when the user needs to reduce PDF file size, create archival PDF/A files, or optimize OCR output.
author: Fullstack Skills Community
category: tools
tags: [ocrmypdf-optimize]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

---|---------|
| No optimization | `--optimize 0` |
| Lossless default | `--optimize 1` |
| Aggressive lossy | `--optimize 2` |
| Max quality | `--optimize 3` |
| PDF/A-1b (default) | `--output-type pdfa` |
| PDF/A-2b | `--output-type pdfa2b` |
| JBIG2 lossy | `--jbig2-lossy` |
| PNG lossy | `--png-lossy` |
| Sidecar text | `--sidecar text.txt` |

## Troubleshooting

- **Large file size**: Try `--optimize 2` or `--png-lossy`.
- **PDF/A validation fails**: Use `--output-type pdfa2b` for better compatibility.
- **Font issues**: PDF/A-2u ensures full Unicode support.

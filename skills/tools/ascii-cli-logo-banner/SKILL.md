---
name: ascii-cli-logo-banner
version: 1.0.0
description: "Entry point for ASCII CLI banners that routes to the Python built-in font skill or figlet.js/FIGfont skill. Use when the user wants a startup banner, ASCII logo, terminal welcome screen, or CLI branding for a service."
author: Fullstack Skills Community
category: tools
tags: [ascii-cli-logo-banner]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

---|-------------|-----|
| Simple built-in font, no npm/node deps | `ascii-cli-logo-banner-python` | Uses a built-in 5x5 font, Python only |
| TAAG/FIGlet fonts, layout smushing | `ascii-cli-logo-banner-figletjs` | Full FIGfont spec via figlet.js |

**Example**: For a quick startup banner with `brandName="MyApp"` and no external font engine needed, route to `ascii-cli-logo-banner-python`. For a FIGlet "Standard" or "Big" font banner with horizontal smushing, route to `ascii-cli-logo-banner-figletjs`.

## Script (optional)
- Use `ascii-cli-logo-banner-python` for the Python implementation.
- Use `ascii-cli-logo-banner-figletjs` for the figlet.js/FIGfont implementation.

## Examples
- See examples in the two implementation skills:
  - `ascii-cli-logo-banner-python/examples/*`
  - `ascii-cli-logo-banner-figletjs/examples/*`

## Quality checklist
1. Does not wrap or misalign at 80 columns; no trailing spaces
2. Copy-pastes cleanly into logs/email/tickets
3. Never prints secrets (tokens, internal URLs, personal data)

## Keywords
**English:** ascii, banner, logo, cli, terminal, startup, welcome, plain text, ansi, no-color
**中文:** ASCII, 启动横幅, 终端 Banner, CLI Logo, 欢迎页, 纯文本, ANSI 上色, 无色回退

---
name: ascii-motd-profile-banner
version: 1.0.0
description: "Generate ASCII-only MOTD / SSH login banner / shell profile welcome messages (short/long variants, quiet mode guidance, security notices)."
author: Fullstack Skills Community
category: tools
tags: [ascii-motd-profile-banner]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-----------------------------------------------------------------------------
  WARNING: Do not store credentials in shell history
================================================================================
```

### Workflow

1. Define `title` and `messageBullets` (1-5 items)
2. Choose `mode` (short for <= 12 lines, long for <= 30 lines)
3. Generate `bannerShort` and `bannerLong` variants
4. Include `safetyNotes` (>= 3 actionable security reminders)
5. **Validate**: Confirm line count, width <= 80, no trailing spaces

## Examples
- `examples/ssh-short.md`
- `examples/ssh-long.md`

## Quality checklist
1. Short mode does not spam (<= 12 lines)
2. Copy/paste safe (no trailing spaces)
3. Security notes are clear, short, and actionable

## Keywords
**English:** ascii-motd-profile-banner, motd, ssh banner, profile, welcome message, security notice, terminal
**中文:** ascii-motd-profile-banner, MOTD, SSH Banner, 登录欢迎, Profile, 安全提示, 终端

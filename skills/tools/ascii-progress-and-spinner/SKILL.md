---
name: ascii-progress-and-spinner
version: 1.0.0
description: "Design ASCII progress bars and spinners for CLI UX (determinate/indeterminate, TTY single-line refresh, non-interactive log fallback) with copy-pastable style specs. Use when the user needs terminal progress indicators, loading animations, or CLI feedback elements."
author: Fullstack Skills Community
category: tools
tags: [ascii-progress-and-spinner]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

--------]  42%  ETA 3s
```

**Spinner styles:**
```
Style 1 (braille): ⠋ Loading...  →  ⠙ Loading...  →  ⠹ Loading...
Style 2 (pipe):    | Loading...  →  / Loading...  →  - Loading...
```

**Non-TTY log fallback:**
```
[task-1] 25% complete
[task-1] 50% complete
[task-1] 75% complete
[task-1] 100% complete - done (4.2s)
```

### Workflow

1. Determine mode: `determinate` (known total) or `indeterminate` (spinner)
2. Select styles from the style gallery (>= 3 progress, >= 2 spinner)
3. Define render rules: TTY uses single-line refresh, non-TTY uses log lines
4. Define fallback rules for redirected output (no carriage returns)
5. **Validate**: Fixed-width percent field, no jitter, grep-friendly log mode

## Script
- `scripts/demo.py`: local demo for progress bar + spinner shapes

## Examples
- `examples/styles.md`

## Quality checklist
1. Fixed width (percent field is fixed-width to avoid jitter)
2. Log mode is grep-friendly (no overwrite)
3. ASCII-only defaults are available (avoid ambiguous-width Unicode)

## Keywords
**English:** ascii-progress-and-spinner, progress bar, spinner, loading, tty, non-interactive, log output, ascii
**中文:** ascii-progress-and-spinner, 进度条, Spinner, Loading, 终端, TTY, 日志降级, ASCII

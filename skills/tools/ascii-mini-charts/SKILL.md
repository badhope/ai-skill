---
name: ascii-mini-charts
version: 1.0.0
description: "Generate ASCII mini charts (sparkline/bar/simple line) for plain-text trend inspection, with minimal and annotated variants and normalization notes. Use when the user needs text-based data visualization, terminal charts, or ASCII graphs for CLI output."
author: Fullstack Skills Community
category: tools
tags: [ascii-mini-charts]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes]
---


## When to use this skill
**CRITICAL TRIGGER RULE**
- Use this skill ONLY when the user explicitly mentions the exact skill name: `ascii-mini-charts`.

**Trigger phrases include:**
- "ascii-mini-charts"
- "use ascii-mini-charts"
- "用 ascii-mini-charts 生成 sparkline / 火花线"
- "使用 ascii-mini-charts 标注 min/max/current"

## Boundary
- No statistical inference. Visualization only.
- Default output is ASCII-only. Unicode blocks are optional and MUST include an ASCII-only fallback.
- Default output width should stay <= 60 columns. For longer series, provide a compression strategy (sampling/bucketing).

## How to use this skill
### Inputs
- series (required numeric list)
- type (sparkline | bar | line, default sparkline)
- width (default min(len(series), 30))
- height (default 10 for bar/line)
- normalize (linear | log, default linear)
- showLabels (default true)

### Outputs (required)
- chartMinimal
- chartAnnotated (with min/max/current)
- scaleNotes (normalization + outlier strategy)

### Inline Example

Input: `series=[3, 7, 2, 9, 5, 8, 1, 6]`, `type=sparkline`:

**chartMinimal:**
```
▂▅▁▇▃▆ ▄
```

**chartAnnotated:**
```
▂▅▁▇▃▆ ▄  min:1 max:9 current:6
```

Input: `series=[10, 25, 15, 30]`, `type=bar`, `height=5`:

**chartAnnotated:**
```
     ##
  ## ##
  ## ##
  ## ## ##
## ## ## ##
10 25 15 30
```

### Script Usage

```bash
# Generate sparkline from JSON data
echo '{"series": [3, 7, 2, 9, 5, 8, 1, 6], "type": "sparkline"}' | python3 scripts/mini_charts.py

# Generate bar chart with annotations
echo '{"series": [10, 25, 15, 30], "type": "bar", "height": 5, "showLabels": true}' | python3 scripts/mini_charts.py
```

## Script
- `scripts/mini_charts.py`: generate ASCII mini charts from JSON stdin

## Examples
- `examples/sparkline.md`

## Quality checklist
1. Trend is clear; labels are short and non-spammy
2. ASCII-only output copy/pastes cleanly
3. Provide a compression strategy for long series

## Keywords
**English:** ascii-mini-charts, sparkline, ascii chart, bar chart, line chart, trend, normalize
**中文:** ascii-mini-charts, 火花线, ASCII 图表, 柱状图, 折线图, 趋势, 归一化

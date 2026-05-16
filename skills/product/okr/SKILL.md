---
name: okr
version: 1.0.0
description: okr command/skill
author: Alireza Rezvani
category: product
tags: [okr]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

# /okr

Generate cascaded OKR frameworks from company-level strategy down to team-level key results.

## Usage

```
/okr generate <strategy>                                     Generate OKR cascade
```

Supported strategies: `growth`, `retention`, `revenue`, `innovation`, `operational`

## Input Format

Pass a strategy keyword directly. The generator produces company, department, and team-level OKRs aligned to the chosen strategy.

## Examples

```
/okr generate growth
/okr generate retention
/okr generate revenue
/okr generate innovation
/okr generate operational
/okr generate growth --json
```

## Scripts
- `product-team/product-strategist/scripts/okr_cascade_generator.py` — OKR cascade generator (`<strategy> [--teams "A,B,C"] [--contribution 0.3] [--json]`)

## Skill Reference
> `product-team/product-strategist/SKILL.md`

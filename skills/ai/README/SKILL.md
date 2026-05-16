---
name: README
version: 1.0.0
description: README command/skill
author: Alireza Rezvani
category: ai
tags: [README]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

------|-------|--------|----------|
| [Startup CTO](startup-cto.md) | 🏗️ | Engineering + Strategy | Technical co-founders, architecture decisions, team building |
| [Growth Marketer](growth-marketer.md) | 🚀 | Marketing + Growth | Bootstrapped founders, content-led growth, launches |
| [Solo Founder](solo-founder.md) | 🦄 | Cross-domain | One-person startups, side projects, MVP building |

## Personas vs Task Agents

| | Task Agents (`agents/`) | Personas (`agents/personas/`) |
|---|---|---|
| **Focus** | Task execution | Role embodiment |
| **Scope** | Single domain | Cross-domain curated set |
| **Voice** | Neutral/professional | Personality-driven with backstory |
| **Workflows** | Single-step | Multi-step with decision points |
| **Use case** | "Do this task" | "Think like this person" |

Both coexist. Use task agents for focused work, personas for ongoing collaboration.

## Creating Your Own

See [TEMPLATE.md](template.md) for the format specification. Key elements:

```yaml
---
name: Agent Name
description: What this agent does and when to activate it.
color: blue          # Agent color theme
emoji: 🎯           # Single emoji identifier
vibe: One sentence personality capture.
tools: Read, Write, Bash, Grep, Glob
---
```

Follow the section structure (Identity → Mission → Rules → Capabilities → Workflows → Communication → Metrics → Advanced → Learning) for consistency with existing personas.

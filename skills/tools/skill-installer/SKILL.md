---
name: skill-installer
version: 1.0.0
description: "Discovers, installs, and manages AI skills from the PartMe marketplace. Acts as the local package manager for Knowledge-as-a-Service (KaaS) and Tool-as-a-Service (TaaS) skills. Use when the user wants to search for available skills, install a new skill into their environment, or list currently installed skills."
author: Fullstack Skills Community
category: tools
tags: [skill-installer]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

---|-------|--------|
| `search_skills` | `query` (string) | JSON list of matching skills with descriptions and paths |
| `install_skill` | `skill_path` (string) | Confirmation of installation |
| `list_installed_skills` | None | JSON list of installed skills with status |

## Best Practices

1. **Search before installing** - Check what is available to avoid duplicates
2. **Use specific queries** - Search "avue-crud" rather than just "crud" for better results
3. **Verify after install** - Run `list_installed_skills` to confirm the skill is active

## Keywords

skill installer, marketplace, KaaS, TaaS, install skill, search skills, PartMe, skill management

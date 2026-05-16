---
name: speckit-initial
version: 1.0.0
description: Run `specify init` in the current or target directory to bootstrap a Spec Kit project (pull .specify/ and slash commands); supports multiple AI agents and --script sh/ps. Use when the user says "initialize Spec Kit project", "specify init", or "set up Spec Kit in this repo".
author: Fullstack Skills Community
category: tools
tags: [speckit-initial]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----------|---------|
| **Linux / macOS, Cursor** | `specify init . --ai cursor-agent` |
| **Linux / macOS, Claude** | `specify init . --ai claude` |
| **Windows, Copilot, PowerShell** | `specify init . --ai copilot --script ps` |
| **New subdirectory** | `specify init my-project --ai gemini` |
| **Overwrite existing .specify** | `specify init . --ai claude --force` |
| **No git** | `specify init . --ai claude --no-git` |
| **Templates only (no agent tools)** | `specify init . --ai claude --ignore-agent-tools` |

## Troubleshooting

- **"specify: command not found"**: Use **speckit-install** first.
- **Windows slash commands not appearing**: Ensure you used `--script ps` if the agent expects PowerShell, and that the agent is configured to load commands from the project.
- **Private repo / rate limit**: Set `GITHUB_TOKEN` or pass `--github-token <token>` as documented by spec-kit.

## References

- [GitHub spec-kit](https://github.com/github/spec-kit) — Get Started: Initialize your project

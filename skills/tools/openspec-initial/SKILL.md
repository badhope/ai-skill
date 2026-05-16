---
name: openspec-initial
version: 1.0.0
description: Run `openspec init` to initialize OpenSpec in a project directory, creating the openspec/ folder structure and configuring AI tool integrations. Use when the user says "initialize OpenSpec", "openspec init", or "set up OpenSpec in this project".
author: Fullstack Skills Community
category: tools
tags: [openspec-initial]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-------|---------|
| **Interactive** | `openspec init` |
| **Claude + Cursor** | `openspec init --tools claude,cursor` |
| **All tools** | `openspec init --tools all` |
| **Specific directory** | `openspec init ./my-project` |
| **CI / non-interactive** | `openspec init --tools claude --force` |
| **Skip tool config** | `openspec init --tools none` |

## Troubleshooting

- **"openspec: command not found"**: Use **openspec-install** first.
- **Legacy files detected**: Use `--force` to auto-cleanup, or follow the interactive prompts.
- **Tool not in list**: Check the [supported tools list](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md) for the correct ID.

## References

- [OpenSpec CLI: init](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md)
- [OpenSpec Supported Tools](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md)

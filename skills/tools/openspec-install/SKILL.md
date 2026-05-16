---
name: openspec-install
version: 1.0.0
description: Install the OpenSpec CLI globally via npm, pnpm, yarn, bun, or nix. Use when the user says "install OpenSpec", "set up OpenSpec", or "openspec command not found".
author: Fullstack Skills Community
category: tools
tags: [openspec-install]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----------|---------|
| **npm** | `npm install -g @fission-ai/openspec@latest` |
| **pnpm** | `pnpm add -g @fission-ai/openspec@latest` |
| **yarn** | `yarn global add @fission-ai/openspec@latest` |
| **bun** | `bun add -g @fission-ai/openspec@latest` |
| **nix (one-time)** | `nix run github:Fission-AI/OpenSpec -- init` |
| **nix (persistent)** | `nix profile install github:Fission-AI/OpenSpec` |
| **CI** | `npm install -g @fission-ai/openspec@latest` in a cacheable step |

## Troubleshooting

- **Node.js version too old**: OpenSpec requires Node.js 20.19.0+. Upgrade Node.js first.
- **Permission errors (npm)**: Use `npm install -g` without sudo if using nvm/fnm; otherwise consider using nvm.
- **Command not found after install**: Ensure the global bin directory is in PATH (check `npm bin -g`).
- **nix not available**: Install nix or use npm/pnpm/yarn/bun instead.

## References

- [OpenSpec Installation docs](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md)
- [OpenSpec GitHub](https://github.com/Fission-AI/OpenSpec)

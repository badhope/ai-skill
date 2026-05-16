---
name: speckit-install
version: 1.0.0
description: Install the Specify CLI on the host machine (uv tool install or uvx one-time); supports multiple OS, persistent or one-time install, and corporate or restricted-network environments. Use when the user says "install Spec Kit", "install Specify CLI", or "specify command not found".
author: Fullstack Skills Community
category: tools
tags: [speckit-install]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----------|--------|
| **Linux** | Install uv if needed; then `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`. WSL: same as Linux. |
| **macOS** | Same as Linux; ensure Python 3.11+ available for uv if required. |
| **Windows** | Install uv (see uv docs); use PowerShell or cmd. For project init, **speckit-initial** will use `--script ps` when needed. |
| **Corporate / proxy** | Use GH_TOKEN/GITHUB_TOKEN if GitHub API is restricted; ensure uv can reach GitHub. |
| **CI** | Prefer persistent install in a cacheable step: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`; then run `specify init` or `specify check` in the same runner. |

## Troubleshooting

- **uv not found**: Direct user to install [uv](https://docs.astral.sh/uv/).
- **Python version**: uv usually manages Python; if errors mention Python, ensure 3.11+ is available.
- **Network / SSL**: Check firewall, proxy, and GitHub access; avoid disabling TLS unless necessary and documented.
- **Permission errors**: On Linux/macOS, user install with uv typically does not need sudo; if using system Python, consider user-level uv install.

## References

- [GitHub spec-kit](https://github.com/github/spec-kit) — Get Started: Install Specify CLI
- [uv documentation](https://docs.astral.sh/uv/)

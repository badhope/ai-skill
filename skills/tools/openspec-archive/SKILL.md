---
name: openspec-archive
version: 1.0.0
description: Archive a completed change with `/opsx:archive`, merging delta specs into main specs and preserving the change for history. Use when the user says "archive the change", "finish up", "/opsx:archive", or "mark this change as done".
author: Fullstack Skills Community
category: tools
tags: [openspec-archive]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

------|--------------|
| `## ADDED Requirements` | Appended to main spec |
| `## MODIFIED Requirements` | Replaces existing requirement in main spec |
| `## REMOVED Requirements` | Deleted from main spec |

## Outputs

- Delta specs merged into `openspec/specs/`.
- Change moved to `openspec/changes/archive/YYYY-MM-DD-<name>/`.

## Next Steps

- Start a new change with **openspec-new**.
- The main specs now reflect the changes — future changes build on the updated source of truth.

## Troubleshooting

- **"Incomplete tasks"**: Archive warns but does not block. Decide whether to complete tasks first or archive as-is.
- **"Delta specs not synced"**: Archive will prompt to sync; or run **openspec-sync** beforehand.
- **Multiple changes to archive**: Use **openspec-bulk-archive** instead.

## References

- [OpenSpec Commands: /opsx:archive](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
- [OpenSpec Concepts: Archive](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)

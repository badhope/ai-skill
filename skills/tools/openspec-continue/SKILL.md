---
name: openspec-continue
version: 1.0.0
description: Create the next artifact in the dependency chain with `/opsx:continue`, building up a change incrementally. Use when the user says "continue the change", "create next artifact", "/opsx:continue", or wants step-by-step artifact creation.
author: Fullstack Skills Community
category: tools
tags: [openspec-continue]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

> specs (requires: proposal)
    |
    +---> design (requires: proposal)
            |
            +---> tasks (requires: specs + design)
```

## Outputs

- One artifact file created per invocation (e.g. `proposal.md`, `specs/**/*.md`, `design.md`, `tasks.md`).

## Next Steps

- Run `/opsx:continue` again for the next artifact.
- When all planning artifacts are done: use **openspec-apply** to implement tasks.
- Or use **openspec-ff** to fast-forward remaining artifacts.

## Troubleshooting

- **"No artifacts ready"**: All artifacts are either complete or blocked. Check `openspec status --change <name>`.
- **"Change not found"**: Specify the change name explicitly: `/opsx:continue add-dark-mode`.

## References

- [OpenSpec Commands: /opsx:continue](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)
- [OpenSpec Concepts: Artifacts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)

---
name: openspec-verify
version: 1.0.0
description: Validate that implementation matches change artifacts using `/opsx:verify`, checking completeness, correctness, and coherence. Use when the user says "verify implementation", "check my work", "/opsx:verify", or wants quality validation before archiving.
author: Fullstack Skills Community
category: tools
tags: [openspec-verify]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

--------|-------------------|
   | **Completeness** | All tasks done, all requirements implemented, scenarios covered |
   | **Correctness** | Implementation matches spec intent, edge cases handled |
   | **Coherence** | Design decisions reflected in code, patterns consistent |

3. **Review the report**
   - **CRITICAL**: Must fix before archiving.
   - **WARNING**: Should address; does not block archive.
   - **SUGGESTION**: Optional improvements.

4. **Fix issues if needed**
   - Address critical issues, optionally fix warnings.
   - Run `/opsx:verify` again to confirm.

## Outputs

- Verification report with categorized issues (CRITICAL / WARNING / SUGGESTION).
- Summary: ready to archive or not.

## Next Steps

- If ready: use **openspec-archive** to archive the change.
- If issues found: fix code or update artifacts, then re-verify.

## Troubleshooting

- **Many false positives**: Add project context in `openspec/config.yaml` to help the agent understand conventions. See **openspec-config**.

## References

- [OpenSpec Commands: /opsx:verify](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md)

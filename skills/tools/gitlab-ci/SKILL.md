---
name: gitlab-ci
version: 1.0.0
description: "Provides comprehensive guidance for GitLab CI/CD including pipeline configuration, runners, artifacts, environments, and deployment automation. Use when the user asks about GitLab CI, needs to create pipelines, configure runners, or automate builds and deployments."
author: Fullstack Skills Community
category: tools
tags: [gitlab-ci]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

------|---------|
| `stages` | Define execution order |
| `needs` | Create DAG dependencies (skip stage waiting) |
| `artifacts` | Pass files between jobs |
| `cache` | Speed up repeated installs |
| `rules` | Control when jobs run |
| `environment` | Track deployment targets |

## Best Practices

- Use `stages` to define clear build order; jobs within a stage run in parallel
- Store sensitive values in CI/CD Variables (Settings > CI/CD > Variables) — never hardcode in YAML
- Use `needs` to create complex dependency graphs and avoid unnecessary waiting
- Preserve logs and artifacts on failure with `artifacts: when: on_failure`
- Use `rules` instead of deprecated `only/except` for conditional job execution

## Troubleshooting

- **Job stuck pending**: Check runner tags match and runners are available
- **Artifact not found**: Verify the producing job completed and artifact paths are correct
- **Cache not restoring**: Ensure cache key is consistent; check runner cache configuration
- **Pipeline not triggered**: Verify `rules` conditions match the event (push, merge request, etc.)

## Keywords

gitlab ci, gitlab-ci, pipeline, runner, ci/cd, artifacts, cache, environments, deployment automation

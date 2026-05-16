---
name: stitch-skill-creator
version: 1.0.0
description: "Factory skill for creating new Stitch Scenario Skills with the Design First, Execute Last SOP. Use when you need to add a new domain (e.g. Music Apps, Social Networks, Login Pages) to the Stitch ecosystem. Generates SKILL.md templates, directory structure, and examples via automated script or manual workflow."
author: Fullstack Skills Community
category: tools
tags: [stitch-skill-creator]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

# <Scenario> Screen Designer

**Constraint**: Only use this skill when the user explicitly mentions "Stitch" or when orchestrating a Stitch design task.

This skill helps you construct high-quality prompts for <Scenario> flows to be used by the Stitch Orchestrator.

## Functionality
It encapsulates best practices for <Scenario> UI design and translates user intent into a structured Stitch prompt.

## Integration with Stitch Designer SOP
This skill is part of the **Stitch UI Orchestration** flow.
1.  **Orchestrator**: `stitch-ui-designer` calls this skill when a scenario-specific prompt is needed.
2.  **Guidelines**: You MUST apply principles from `stitch-ued-guide` (e.g., visual vocabulary, device constraints).
3.  **Output**: You do NOT execute. You return a prompt only.

## Prompt Template

When the user asks for a <Scenario> screen, use this template to construct the prompt:

```text
[Context]
[Device] <Scenario> screen for [App Name]. [Style] aesthetic.

[Layout]
Header: [...]
Body: [...]
Footer: [...]

[Components]
- [...]
- [...]
```

## Output Format (STRICT)

Return exactly one code block and no extra prose:

```text
[Context]
...

[Layout]
...

[Components]
...
```

## Usage in Orchestrator
This skill is designed to be called by `stitch-ui-designer`. It does NOT execute; it returns a prompt only.
````

### Step 4: Write `examples/usage.md`
Provide at least 2 distinct examples of how this skill transforms a vague request into a detailed prompt.

## Best Practices for New Skills

1.  **Domain Specificity**: The value of a Scenario Skill is in its *specific knowledge*.
    *   *Bad*: "A page with text."
    *   *Good (Music)*: "A player view with a scrubbing bar, album art, and waveform visualization."
2.  **Device Awareness**: Ensure the template supports Mobile (default) and Desktop.
3.  **No Direct Execution**: The Scenario Skill must not call any MCP tool. It produces the prompt that the Orchestrator uses.

## References

- [Examples](examples/usage.md)
- [Workflows](references/workflows.md)
- [Output Patterns](references/output-patterns.md)
- [Init Script](scripts/init_stitch_skill.py)

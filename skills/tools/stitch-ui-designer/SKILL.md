---
name: stitch-ui-designer
version: 1.0.0
description: "Master orchestrator for end-to-end Stitch UI design and generation. Use when the user asks to design, create, or make a UI screen using Stitch. Coordinates design spec generation, framework contract injection, prompt assembly, and MCP execution (create_project, generate_screen_from_text, get_screen) in a single workflow."
author: Fullstack Skills Community
category: tools
tags: [stitch-ui-designer]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----|---------|--------|
| **Platform** | Web / Mobile / Desktop, target device or width | "Mobile miniapp, prioritize iOS and Android" / "Admin Web, min width 1280px" |
| **Theme** | Mood + domain affinity | "Bright and fresh, professional and trustworthy, with domain-friendly tone" |
| **Color scheme** | Primary + Secondary + Warning + Neutrals (Background, Text, Secondary text, Divider), each with **#hex** and usage | Primary #165DFF for buttons/nav; Secondary #36D399 for positive cues; Background #FFFFFF; Text #1D2129; Secondary text #86909C; Divider #F2F3F5 |
| **Typography** | Title / Body / Auxiliary: **size (px)** + **font** + **weight** | Title 20px Bold; Body 16px Regular; Auxiliary 14px Light |
| **Component style** | Buttons / Cards / Icons: radius, shadow, interaction | Buttons 8px radius, soft shadow; Cards 12px radius, light shadow; Icons linear, minimal |

If a **named design system** (uView Pro, Bootstrap, Element Plus, etc.) is used, the contract prefix from step 3 already supplies tokens; the assembled prompt must still state **Platform**, **Theme**, and **Layout invariants** in human-readable form so Stitch understands intent.

### 3) Page Structure and Function

For **each** page or major section:

- **Core function**: One line — "This page/section is for... so that..."
- **Areas** (choose as needed): **Top nav** / **Hero / main visual** / **Function area** / **Action area** / **Footer** / **Sidebar**.
- Under each area: **concrete elements** (e.g. "Brand logo + Help entry", "Primary CTA 'Scan label' large filled", "Secondary 'Choose from gallery' outline"). Use specific copy and roles (primary button, secondary button, card, list item) instead of "a button" or "some text".

**Example (single section):**

```text
### 1. Home (Scan / Upload)
**Core function**: App entry, guide user to start
- **Top nav**: Brand logo + Help entry
- **Hero**: Headline "Ingredient Translator" + subhead "Understand food labels at a glance"
- **Function area**: Primary button "Scan label" (large, primary fill); Secondary "Choose from gallery" (outline, primary border); short usage copy
- **Footer**: Privacy and terms links
```

### 4) Prompt Structure Checklist (before calling generate_screen_from_text)

Verify (and if missing, request the prompt-architect to add):

- [ ] **Project overview** present for app/product-level requests? (one paragraph: what, who, style, key attributes)
- [ ] **Design system (required)** present? Platform, Theme, **Color scheme with #hex**, **Typography (px + font + weight)**, **Component style** (buttons, cards, icons)
- [ ] **Per-page/section**: **Core function** one line + **areas** (top nav / hero / function / action / footer) with **concrete elements** and specific copy?
- [ ] **Layout** and **Components** sections still populated? (macro layout + component list)
- [ ] No vague placeholders? ("a button" → "primary CTA button 'Sign In'"; "some list" → "vertical list of Workout Cards with thumbnail, duration, Start button")

If any of the above is missing, **re-invoke** `stitch-ui-prompt-architect` with explicit instructions to fill the Optimized Prompt Structure (project overview, design system with hex/px, page structure with core function and area-level details), then re-run the checklist before execution.

---

## Anti-Patterns (Strict Prohibitions)
*   ⛔ **NO FAKE SUCCESS**: If you didn't get a real API response, do not say "Project Created".
*   ⛔ **NO APP SCAFFOLDING**: Do not invoke any external project scaffolding skills (e.g., `uniappx-project-creator`, `flutter-project-creater`, `react-native-project-creater`) and do not run scripts to create codebases.
*   ⛔ **NO CODING**: Do not write Vue/React/HTML code in this flow. This skill is for **Design Generation** only.
*   ⛔ **NO CONFUSION**: A "Stitch Project" is a design workspace, NOT a code repository.

## Keywords
orchestrator, design agent, ui designer, master skill, design flow, stitch pilot

## References

- [Workflow End-to-End](examples/workflow_end_to_end.md)
- [Workflows Reference](references/workflows.md)
- [Optimized Prompt Output Examples (ZH + EN)](examples/optimized_prompt_output_examples.md) — full Chinese and English examples of the optimized prompt (project overview + design system + page structure and function) from the blog "Trae+Stitch MCP+Skills: My New AI Programming Paradigm".
- **Optimized prompt structure**: Project Overview + Design System (required) + Page Structure and Function. See blog "Trae+Stitch MCP+Skills: My New AI Programming Paradigm" (optimized prompt section). Goal: turn a vague idea into a detailed construction blueprint (colors, font sizes, button styles, layout, UX) to improve Stitch output precision.

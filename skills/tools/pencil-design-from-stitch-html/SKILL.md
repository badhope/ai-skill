---
name: pencil-design-from-stitch-html
version: 1.0.0
description: "When you need to turn Stitch page HTML (or a Stitch URL) into a Pencil .pen design. Parses DOM and Tailwind, applies HTML→Pencil mapping and execution order, outputs sequential batch_design for layout and style fidelity (background, color, size, margin, padding, shadow). Supports multi-framework tokens."
author: Fullstack Skills Community
category: tools
tags: [pencil-design-from-stitch-html]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----|-------------|---------------|------------|
| 0 | Canvas prep (optional) | — | — |
| 1 | Document + root + header + main placeholder | Batch 1 | document → root, main |
| 2 | Header content (back, title, actions) | Batch 2 | header |
| 3 | Tabs bar (if present) | Batch 3 | root |
| 4 | Section 1 (card + title + body placeholder) | Batch 4 | main |
| 5 | Section 1 body (form rows, inputs, buttons) | Batch 5 | card1Body |
| 6 | Section 2 (card + …) | Batch 6 | main |
| 7 | Section 2 body | Batch 7 | card2Body |
| … | One batch per section body if large | … | … |
| N | Footer or final dividers | Batch N | main |

Parents created in an earlier batch are referenced by **binding name** in later batches (e.g. `I(main, ...)`, `I(card1Body, ...)`). Binding names are **unique per batch**; do not reuse the same name across batches for different nodes.

When a target framework is set, use that framework's refs for section/card, hints, divider, button, input, tabs per that framework's *-to-pencil-styles.md section 15 and [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md) section 16.

### 2. Phase 0: Canvas prep (optional)

- **When**: Before any `batch_design`, if the artboard must be placed at a specific position on the canvas.
- **Actions**: Call `find_empty_space_on_canvas` with desired width/height (e.g. screen width × height from Stitch get_screen). Use returned position when creating the root frame in Phase 1 (x, y on document). No `batch_design` in this phase.

### 3. Phase 1: Root and main structure (Batch 1)

**Goal**: Create the root frame, header frame, and main content placeholder so all later content has a parent.

**Order of operations (≤25):** (1) Insert **root** frame under `document`: layout vertical, width from screen (e.g. 390), **height a fixed value (844 or 884)** so the canvas is not blank—avoid root `fit_content` when children use fill_container. Fill = page background. (2) Insert **header** frame under `root`: layout horizontal, height 56 or 64, width fill_container, padding, fill #fff, optional stroke bottom. (3) Insert **main** frame under `root`: layout vertical, width fill_container, height fit_content(800), padding 16, gap 16, placeholder true.

**Binding names for later batches:** `root`, `header`, `main`. Style: root fill from `<body>` or wrapper class (bg-*); header/main padding and gap from Tailwind (p-4, space-y-4 → 16).

### 4. Phase 2: Header content (Batch 2)

**Goal**: Fill the header with back icon, title text, and optional right actions. **Parent:** `header`. Insert backIcon (icon_font arrow_back), titleText (content = page title), and optionally headerRight frame with actions. Binding names: `backIcon`, `titleText`, `headerRight`.

### 5. Phase 3: Tabs bar (Batch 3, if present)

**Goal**: Create the tab row. **Parent:** `root`. Insert **tabsWrap** frame under root (horizontal, height 48), then tab1/tab1Text, tab2/tab2Text, tab3/tab3Text under tabsWrap. If more than 3 tabs, split into Batch 3a/3b or keep under 25 ops total.

### 6. Phase 4–5: First section / card (Batch 4 + 5)

**Batch 4** — Parent: `main`. Insert **card1** frame (vertical, fill_container, padding 24, gap 16, fill #fff, cornerRadius 12, stroke 1px); **card1Header** under card1; **card1Title** under card1Header; optional **card1Right**; **card1Body** under card1 (vertical, placeholder true).

**Batch 5** — Parent: `card1Body`. For each form row: insert row frame, label text, input frame (or ref). If more than ~8 rows, split into Batch 5a, 5b. Binding names: `card1`, `card1Header`, `card1Title`, `card1Body`.

### 7. Phase 6–7: Second section (Batch 6 + 7)

Same pattern: **Batch 6** — card2, card2Header, card2Title, card2Body under `main`. **Batch 7** — card2Body children. Repeat for Section 3, 4, … (Batch 8, 9, …). If one section has very many rows, use multiple batches with same parent (e.g. card3Body).

### 8. Phase N: Footer and final elements

Insert any footer frame under `main`, or final divider lines. Keep under 25 ops; if many small elements, group into one batch.

### 9. Batch size and naming rules

- **Max 25 operations per `batch_design` call.** Split large section bodies (e.g. 15 form rows → Batch 5 first 7, Batch 5b next 8).
- **Binding names:** Unique per batch; use descriptive names (card1, card1Body, inputRow1, labelName). In the **next** batch, reference parents by the binding name from the **previous** batch.
- **Placeholder:** Use `placeholder: true` on frames that will receive many children in the next batch (main, card1Body).

### 10. Execution order checklist

Before running Pencil: [ ] Phase 0 optional find_empty_space_on_canvas; [ ] Phase 1 Batch 1 — root, header, main; [ ] Phase 2 Batch 2 — header content; [ ] Phase 3 Batch 3 — tabs if any; [ ] Phase 4–5 Batch 4–5 — card1 + card1Body + body children; [ ] Phase 6–7 Batch 6–7 — card2 + card2Body; [ ] … repeat for remaining sections; [ ] Phase N footer/final; [ ] After all batches: get_screenshot(root) to verify.

### 11. Example: Minimal page (header + 1 card + 2 rows)

| Batch | Ops | Content |
|-------|-----|---------|
| 1 | 3 | root, header, main |
| 2 | 2 | backIcon, titleText under header |
| 3 | 6 | card1, card1Header, card1Title, card1Body |
| 4 | 5 | row1, label1, input1; row2, label2, input2 under card1Body |

Total: 4 batches, 16 operations. Order is fixed: 1 → 2 → 3 → 4.

## Integration

- **Stitch screens**: Same pattern as stitch-remotion / stitch-uviewpro-components: list_projects, list_screens, get_screen, download URLs (when user provides Stitch URL/IDs).
- **Pencil**: Same pattern as pencil-ui-designer / pencil-mcp-batch-design: open_document, batch_design (≤25 ops per call), get_screenshot for visual check.
- **Design system**: If .pen has a design system (e.g. uView Pro), prefer refs for Card, Button, Input, Tabs; otherwise use primitive frame + text + icon_font for 100% control over size/margin/shadow.

## File Structure

```
skills/pencil-design-from-stitch-html/
├── SKILL.md
├── LICENSE.txt
├── references/
│   ├── html-to-pencil-mapping.md   # Element → node + op rule
│   ├── tailwind-to-pencil-styles.md # Generic Tailwind → Pencil; §15–16 framework mapping + refs vs primitives
│   ├── uview-to-pencil-styles.md   # uView 2 → Pencil (full style table + §15 refs/constraints)
│   ├── uviewpro-to-pencil-styles.md
│   ├── element-to-pencil-styles.md
│   ├── bootstrap-to-pencil-styles.md
│   ├── layui-to-pencil-styles.md
│   └── vant-to-pencil-styles.md
└── examples/
    ├── usage.md                    # When to use, steps, MCP flow, example prompts
    ├── sample-batch-ops.md         # Minimal page → one batch_design (≤25 ops)
    ├── sample-multi-batch.md       # Header + card + form rows → four batches
    ├── sample-with-framework-refs.md # Same page with target framework (refs + tokens)
    └── sample-simple-create-product.md # Simplified Create Product (1–2 batches) for quick validation
```

## Keywords

**English:** Stitch, Pencil, batch_design, .pen, HTML to design, Tailwind, layout, fidelity.  
**中文关键词：** Stitch、Pencil、绘图、HTML 转设计稿、批动作。

## References

- [Stitch MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
- [Pencil MCP tools](https://github.com/google-labs-code/pencil-skills) / pencil-skills [stitch-html-to-pencil-batch.md](../../docs/stitch-html-to-pencil-batch.md)
- [HTML → Pencil mapping](references/html-to-pencil-mapping.md)
- [Tailwind → Pencil styles](references/tailwind-to-pencil-styles.md) (includes §15–16 framework mapping and refs vs primitives)
- Per-framework style tables (incl. refs/constraints §15): [uview](references/uview-to-pencil-styles.md), [uviewpro](references/uviewpro-to-pencil-styles.md), [element](references/element-to-pencil-styles.md), [bootstrap](references/bootstrap-to-pencil-styles.md), [layui](references/layui-to-pencil-styles.md), [vant](references/vant-to-pencil-styles.md)
- [Examples](examples/usage.md): [usage](examples/usage.md), [single batch](examples/sample-batch-ops.md), [multi-batch](examples/sample-multi-batch.md), [with framework refs](examples/sample-with-framework-refs.md), [simplified Create Product](examples/sample-simple-create-product.md)

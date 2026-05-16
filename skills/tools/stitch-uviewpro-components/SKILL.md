---
name: stitch-uviewpro-components
version: 1.0.0
description: "Convert Stitch designs into uni-app + Vue 3 + uView Pro pages and components. Use when the user mentions uView Pro, uviewpro, or uni-app Vue 3 conversion from Stitch. Retrieves screen HTML via Stitch MCP get_screen, maps Tailwind to rpx/theme, enforces u-* component contracts (u-tabs, u-form, u-picker, u-card) with script setup."
author: Fullstack Skills Community
category: tools
tags: [stitch-uviewpro-components]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-----|-------------------------------------|----------------------|
| **Tab switcher** | Custom `<view class="tab-header">` + `<view class="tab-item">` | **Always use `<u-tabs :list="..." :current="..." @change="...">`**; do not build tabs with raw views/divs |
| Tabs props | `lineColor`, `activeStyle`, `inactiveStyle`, `itemStyle` | **:current**, **@change(index)** (number), **active-color**, **inactive-color** |
| Picker | `:show="show"`, `:columns="[['A','B']]"` (2D) | **v-model="show"**; **mode="selector"** + **:range** (1D array, e.g. `['A','B']`); **@confirm**; do not use :columns |
| Radio | `name="opt1"`, `customStyle`, `placement="row"` | **value="opt1"** (not name), **label** for text; no customStyle/placement |
| Slots (Vue 3) | `slot="label"`, `slot="suffix"` | **#label**, **#suffix**, **v-slot:label** — never `slot="..."` |
| Form-item label | `slot="label"` | **#label** or **v-slot:label** |
| Input type=select | — | Pair with **u-picker**; use **:select-open** bound to picker visibility |

**Pre-generation checklist** — before writing the template, ensure: (1) **Card/section** use **u-card** (with `title` or + **u-section** for title+right), not view.card + card-header + card-title. (2) **Label hints and tips** use **u-text** (type="info"/"warning", size="24"), not text with .label-optional/.tips-text/.unit. (3) **Divider** use **u-line** or **u-divider**, not view + border. (4) Tab switcher uses **u-tabs**, not custom divs. (5) All slots use **#slotname** or **v-slot:slotname**. (6) Picker uses **v-model** and **:range** (1D). (7) Radio uses **value** and **label**, not name/customStyle/placement.

## Integration with This Repo

- **Get screen**: Use **stitch-mcp-get-screen** with projectId and screenId. Obtain IDs either by parsing a **Stitch design URL** (projectId from path, screenId from `node-id`) or by using **stitch-mcp-list-projects** and **stitch-mcp-list-screens** when no URL is given or when the user needs to browse/select.
- **Design spec**: If Stitch was generated with **stitch-ui-design-spec-uviewpro** constraints, map to uni-app pages and uView Pro components. If converting from Stitch HTML (e.g. `htmlCode` from get_screen), use [references/stitch-html-patterns.md](references/stitch-html-patterns.md) for page structure and form fields; [references/tailwind-to-uviewpro.md](references/tailwind-to-uviewpro.md) for Tailwind utility → rpx/theme (spacing, typography, colors, borders, shadows); then [references/contract.md](references/contract.md) for component API and anti-patterns.
- **Design system**: If the project has DESIGN.md (from **stitch-design-md**), align colors and rpx spacing with that system when mapping to uView Pro tokens.

## Troubleshooting

- **Fetch errors**: Quote the URL in the bash command; ensure `scripts/fetch-stitch.sh` is executable.
- **Component mapping**: Use [references/component-index.md](references/component-index.md) to pick the right u-* for each element; follow [references/contract.md](references/contract.md) for layout (u-row, u-col, u-gap), forms (u-form, u-input), nav (u-navbar, u-tabs, u-tabbar), list (u-swipe-action, u-list), feedback (u-toast, u-modal, u-popup, u-empty, uni.$u). Do not substitute raw HTML for u-* components.

## Skill testing (command-triggered)

Testing is triggered by user instruction, not by calling MCP directly. Flow: user pastes the **test command** below into the chat → Agent runs this skill → resolve URL → call get_screen → fetch/parse design → generate uView Pro code → output page file or full code.

- **Test command** (paste into Cursor chat):
  ```text
  Use the Stitch skill to convert https://stitch.withgoogle.com/projects/3492931393329678076?node-id=375b1aadc9cb45209bee8ad4f69af450 into a uView Pro page
  ```
- **Expected**: Parse projectId and screenId from URL → call Stitch MCP get_screen → generate uni-app + uView Pro .vue (u-navbar, u-tabs, u-form, u-picker, u-radio, etc.) per contract and stitch-html-patterns.

## Keywords

**English:** Stitch, uni-app, uView Pro, Vue 3, u-button, u-navbar, rpx.  
**中文关键词：** Stitch、uni-app、uView Pro、组件。

## References

- **Component API**: [api/component-api.md](api/component-api.md)
- **Examples**: [examples/usage.md](examples/usage.md)
- **Contract & Patterns**:
    - [references/contract.md](references/contract.md) (Core mapping rules)
    - [references/official.md](references/official.md) (Official docs links)
    - [references/stitch-html-patterns.md](references/stitch-html-patterns.md) (HTML structure handling)
    - [references/tailwind-to-uviewpro.md](references/tailwind-to-uviewpro.md) (Style conversion)
    - [references/component-index.md](references/component-index.md) (Component list)
- **Resources**:
    - [resources/architecture-checklist.md](resources/architecture-checklist.md) (QA Checklist)
- **Scripts**:
    - [scripts/fetch-stitch.sh](scripts/fetch-stitch.sh) (High-reliability fetcher)

- **[Component index (must read)](references/component-index.md)** — Full uView Pro component list (80+) with minimal usage; consult when generating so you use u-modal, u-popup, u-action-sheet, u-empty, u-avatar, u-picker, u-tabbar, etc., instead of raw HTML.
- [Stitch HTML patterns](references/stitch-html-patterns.md) — Stitch HTML → uView Pro (page structure, forms); use when converting from get_screen htmlCode.
- [Tailwind → uView Pro](references/tailwind-to-uviewpro.md) — Tailwind utility classes → rpx / theme (spacing, typography, colors, borders, shadows); use so output is framework-native, not raw Tailwind.
- [Contract (uView Pro mapping + anti-patterns)](references/contract.md)
- [Component API (props/events)](api/component-api.md)
- [Official documentation](references/official.md)
- [Architecture checklist](resources/architecture-checklist.md)
- [Page template](resources/page-template.vue)
- [Stitch API / MCP](https://stitch.withgoogle.com/docs/mcp/guide/)

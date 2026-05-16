---
name: uview-vue2
version: 1.0.0
description: "Builds Vue 2 mobile UIs in uni-app using the uView UI component library with Button, Input, Form, Table, Modal, Tabs, and built-in $u tools (toast, http, storage, route). Use when the user needs to create uni-app interfaces with uView UI for Vue 2, customize themes via SCSS variables, or use $u utility methods."
author: Fullstack Skills Community
category: development
tags: [uview-vue2]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-------|-----------|---------------|
| Form | Button, Input, Form, Picker, Tabs | `examples/components/form.md`, `button.md` |
| Display | List, Card, Badge, Grid, Swiper, Table | `examples/components/list.md`, `table.md` |
| Feedback | Modal, Toast, Loading | `examples/components/modal.md` |
| Navigation | Navbar, Tabs | `examples/components/navbar.md` |

### $u Tools Reference

| Tool | Usage | Example File |
|------|-------|-------------|
| Toast | `this.$u.toast('message')` | `examples/tools/toast.md` |
| HTTP | `this.$u.http.get(url)` | `examples/tools/http.md` |
| Storage | `this.$u.storage.set(key, val)` | `examples/tools/storage.md` |
| Route | `this.$u.route('/pages/home')` | `examples/tools/route.md` |
| Debounce | `this.$u.debounce(fn, 300)` | `examples/tools/debounce.md` |

### API Reference

- `api/components.md` - Component props, events, and slots
- `api/tools.md` - $u utility method signatures
- `api/theme-variables.md` - SCSS theme variables

## Best Practices

1. **Use easycom** - Configure easycom in pages.json for automatic component registration
2. **SCSS theme variables** - Override uView SCSS variables for custom branding, not inline styles
3. **Use rpx units** - Ensure responsive layouts across screen sizes in uni-app
4. **Leverage $u tools** - Use built-in HTTP, storage, and route helpers instead of extra libraries
5. **Test cross-platform** - Verify on H5, WeChat mini-program, and native App

## Resources

- **Official Docs**: https://www.uviewui.com/
- **GitHub**: https://github.com/umicro/uView

## Keywords

uView UI, uView, Vue 2, uni-app, $u, component library, 组件库, Button, Form, Table, Modal, Toast, 按钮, 表单, 表格, 模态框, mobile UI

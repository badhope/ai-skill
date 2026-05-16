---
name: uview-pro-vue3
version: 1.0.0
description: "Builds Vue 3 mobile UIs in uni-app using the uView Pro component library (100+ components). Covers Button, Form, List, Modal, Tabs, NavBar, plus built-in HTTP, storage, router, and validator utilities. Use when the user needs to create uni-app interfaces with uView Pro, configure themes, or use uView Pro utility tools."
author: Fullstack Skills Community
category: development
tags: [uview-pro-vue3]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-------|-----------|---------------|
| Form | Button, Input, Form, Select, Switch, Checkbox, Radio, Upload | `examples/components/form.md` |
| Display | List, Card, Avatar, Badge, Tag, Empty | `examples/components/list.md` |
| Feedback | Toast, Modal, Loading, Popup, Drawer | `examples/components/modal.md` |
| Navigation | Tabs, NavBar, Pagination, Dropdown | `examples/components/tabs.md` |

### Tools Reference

| Tool | File | Purpose |
|------|------|---------|
| HTTP | `examples/tools/http.md` | Request wrapper with interceptors |
| Storage | `examples/tools/storage.md` | Local storage utilities |
| Router | `examples/tools/router.md` | Navigation helpers |
| Validator | `examples/tools/validator.md` | Form validation |

### API Reference

- `api/component-api.md` - Component props, events, methods, and slots
- `api/tools-api.md` - Utility function signatures and parameters
- `api/config-api.md` - Global and theme configuration

## Best Practices

1. **On-demand import** - Import only used components to reduce bundle size
2. **Composition API** - Prefer `<script setup>` for cleaner Vue 3 code
3. **Theme variables** - Customize via uView theme config rather than overriding CSS
4. **Use built-in tools** - Leverage HTTP, storage, and router utilities instead of adding extra dependencies
5. **Test on device** - Verify uni-app behavior on actual mobile devices, not just H5

## Resources

- **Official Docs**: https://uviewpro.cn/

## Keywords

uView Pro, uview-pro, Vue 3, uni-app, component library, 组件库, Button, Form, List, Modal, Tabs, NavBar, mobile UI, 表单, 列表

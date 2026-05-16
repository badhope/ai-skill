---
name: ant-design-mobile
version: 1.0.0
description: "Builds React mobile UIs with Ant Design Mobile (antd-mobile) components including Button, Form, List, Modal, Picker, Tabs, PullToRefresh, InfiniteScroll, and 50+ mobile-optimized components. Use when the user needs to create mobile-first React interfaces, implement mobile navigation, forms, or data display with Ant Design Mobile."
author: Fullstack Skills Community
category: development
tags: [ant-design-mobile]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-------|-----------|---------------|
| Navigation | NavBar, TabBar, Tabs, SideBar | `examples/components/nav-bar.md`, `tabs.md` |
| Data Entry | Input, Form, Picker, DatePicker, Switch, Checkbox | `examples/components/form.md`, `picker.md` |
| Data Display | List, Card, Badge, Tag, Avatar, Image | `examples/components/list.md`, `card.md` |
| Feedback | Modal, Toast, Dialog, ActionSheet, Loading | `examples/components/modal.md`, `toast.md` |
| Gestures | PullToRefresh, InfiniteScroll, Swiper | `examples/components/pull-to-refresh.md` |

### API Reference

- `api/components.md` - All component props and APIs
- `api/config-provider.md` - Global configuration and theming

## Best Practices

1. **Import CSS first** - Add `import 'antd-mobile/es/global'` in your entry file
2. **Wrap with ConfigProvider** - Set locale and theme at the app root
3. **Use CSS variables for theming** - Override `--adm-color-primary` etc. for custom branding
4. **Tree-shake imports** - Import individual components (`import { Button } from 'antd-mobile'`) for smaller bundles
5. **Test on real devices** - Mobile touch behavior differs from desktop browser emulation

## Resources

- **Official Website**: https://ant-design-mobile.antgroup.com/
- **GitHub**: https://github.com/ant-design/ant-design-mobile

## Keywords

antd-mobile, Ant Design Mobile, React mobile, mobile UI, 移动端, 组件库, Button, Form, List, Modal, Tabs, PullToRefresh, InfiniteScroll, Toast, NavBar, TabBar, mobile components

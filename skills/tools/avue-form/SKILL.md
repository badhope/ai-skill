---
name: avue-form
version: 1.0.0
description: "Builds configuration-driven dynamic forms with Avue Form, including field types (input, select, date, upload), validation rules, form groups, tabbed layouts, and event handling. Use when the user needs to create forms with Avue in Vue applications, implement form validation, or build dynamic multi-step forms."
author: Fullstack Skills Community
category: tools
tags: [avue-form]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

------|------|
| Dynamic form | `examples/features/dynamic-form.md` |
| Form layout | `examples/features/form-layout.md` |
| Validation rules | `examples/features/form-rules.md` |
| Form groups | `examples/features/form-group.md` |
| Tabbed forms | `examples/features/form-tabs.md` |
| Custom components | `examples/features/custom-components.md` |

### API Reference

- `api/form-api.md` - Component props, events, and slots
- `api/columns-api.md` - Column types and properties
- `api/options-api.md` - Form option configuration

## Best Practices

1. **Use column types** - Set `type: 'select'`, `type: 'date'`, `type: 'upload'` for automatic controls
2. **Call done() after submit** - Always call `done()` in the submit handler to re-enable the button
3. **Use span for layout** - Set `span: 12` for half-width fields (24 = full width grid)
4. **Group related fields** - Use `group` option to organize complex forms into sections
5. **Validate on blur** - Set `trigger: 'blur'` for a less intrusive validation experience

## Resources

- **Official Docs**: https://avuejs.com/form/form-doc.html

## Keywords

Avue Form, avue-form, Vue form, dynamic form, 表单组件, 表单验证, form validation, form configuration, form columns, form rules

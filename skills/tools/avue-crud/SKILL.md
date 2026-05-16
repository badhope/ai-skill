---
name: avue-crud
version: 1.0.0
description: "Builds configuration-driven CRUD tables with the Avue framework, including column definition, pagination, search, sorting, row operations (add/edit/delete), data export, and form validation. Use when the user needs to create data management interfaces with Avue CRUD tables in Vue 2 applications."
author: Fullstack Skills Community
category: tools
tags: [avue-crud]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

------|------|
| Column config | `examples/features/columns.md` |
| CRUD operations | `examples/features/crud-operations.md` |
| Pagination | `examples/features/pagination.md` |
| Search | `examples/features/search.md` |
| Export | `examples/features/export.md` |
| Form validation | `examples/advanced/validation.md` |

### API Reference

- `api/crud-api.md` - Component props, events, methods
- `api/column-api.md` - Column types, renderers, formatters
- `api/option-api.md` - Table, form, and button options

## Best Practices

1. **Configuration-driven** - Define all table behavior in the `option` object, not in template markup
2. **Call done() in event handlers** - Always call `done()` after save/update to close the dialog
3. **Use column types** - Set `type: 'select'`, `type: 'date'`, etc. for automatic form controls
4. **Paginate server-side** - Use `@on-load` with page params for large datasets
5. **Add search columns** - Set `search: true` on columns to enable the search bar

## Resources

- **Official Docs**: https://avuejs.com/crud/crud-doc.html

## Keywords

Avue CRUD, avue-crud, table, CRUD, 增删改查, pagination, search, column, form, 表格, 分页, data management

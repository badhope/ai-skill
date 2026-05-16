
# 贡献指南

感谢你对 AI-SKILL 项目的兴趣！我们欢迎各种形式的贡献。

## 如何贡献

### 1. 提交 Issue

- 报告 Bug
- 提出新功能建议
- 改进文档

### 2. 提交 Pull Request

- 修复 Bug
- 添加新技能
- 改进文档
- 优化代码

## 开发流程

### 1. Fork 仓库

点击 GitHub 上的 "Fork" 按钮。

### 2. 克隆仓库

```bash
git clone https://github.com/你的用户名/AI-SKILL.git
cd AI-SKILL
```

### 3. 创建分支

```bash
git checkout -b feature/你的技能名称
```

### 4. 添加技能

按照 [SKILL 格式规范](docs/SKILL_FORMAT.md) 创建新技能：

```bash
mkdir -p skills/分类/你的技能名称
# 创建 SKILL.md 和其他文件
```

### 5. 提交更改

```bash
git add .
git commit -m "feat: 添加 你的技能名称 技能"
git push origin feature/你的技能名称
```

### 6. 创建 Pull Request

在 GitHub 上创建 PR。

## 技能审核标准

提交的技能需要满足以下标准：

### ✅ 必须满足

- [ ] 符合 [SKILL.md 格式规范](docs/SKILL_FORMAT.md)
- [ ] 有完整的 YAML Frontmatter
- [ ] 包含概述、使用场景、工作流程
- [ ] 有至少一个使用示例
- [ ] 没有版权问题
- [ ] 无恶意代码

### ⭐ 推荐包含

- [ ] 最佳实践章节
- [ ] 常见问题解答
- [ ] 参考资料链接
- [ ] 相关脚本和模板
- [ ] 测试用例

## 代码规范

### Git 提交信息格式

```
&lt;type&gt;: &lt;subject&gt;

&lt;body&gt;

&lt;footer&gt;
```

Type 类型：
- `feat`: 新技能/新功能
- `fix`: 修复问题
- `docs`: 文档更新
- `refactor`: 重构
- `style`: 格式调整
- `test`: 测试相关

### 示例

```
feat: 添加 code-reviewer 技能

- 添加代码审查技能
- 包含最佳实践检查清单
- 提供多种语言的审查规则

Closes #123
```

## 社区行为准则

- 尊重他人
- 保持友好
- 接受建设性批评
- 专注于项目目标

## 获取帮助

如有问题，请：
1. 查看 [文档](docs/)
2. 搜索现有 Issue
3. 创建新 Issue 提问

## 许可证

通过贡献代码，你同意你的贡献将遵循项目的许可证：
- 个人使用免费
- 商业使用需联系 badhope 获得许可

请参阅 [LICENSE](LICENSE) 了解完整条款。

---

再次感谢你的贡献！🎉

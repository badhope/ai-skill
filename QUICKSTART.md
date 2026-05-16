# Quick Start Guide

## Quick Setup

### 1. Clone the repository

```bash
git clone https://github.com/badhope/AI-SKILL.git
cd AI-SKILL
```

### 2. Configure your settings

```bash
cp config.example.json config.json
# Edit config.json and fill in your API keys and settings
```

### 3. Use the skills

#### Claude Code

1. Open Claude Code
2. Navigate to Settings → Plugins
3. Add this repository as a plugin
4. Start using the skills!

#### Cursor

1. Open your Cursor project
2. Copy the `skills` directory to your project root
3. Or configure in Cursor rules settings

#### Gemini CLI

1. Follow Gemini CLI's documentation
2. Configure the skills directory
3. Start using!

#### Doubao (豆包)

1. Open Doubao
2. Import skills from the skills directory
3. Start using!

#### Qwen (通义千问)

1. Open Qwen
2. Configure skills path
3. Start using!

#### Spark (讯飞星火)

1. Open Spark
2. Import skills
3. Start using!

## Important Note

This is a curated collection of skills from multiple sources. All credit goes to the original authors:

- Anthropic Official Skills
- Matt Pocock's Collection
- Alireza Rezvani's Skills
- Fullstack Skills
- Antigravity Awesome Skills
- AI Research Skills
- Agent Skills Hub
- Agent Skills Library

See README.md for full details and links to original sources.

## Available Skills (2200+)

### AI & Agents (800+)
Skill creation, agent design, RAG architecture, prompt engineering, LLM tools, AI workflows, research tools, and more.

### Development (600+)
Code reviewer, dev workflow, diagnose, TDD, prototype, MCP builder, web artifacts builder, web app testing, and more.

### Tools (400+)
PDF, DOCX, PPTX, XLSX processing, file organization, Slack GIF creator, screenshot OCR, and more.

### Product (80+)
PRD writer, OKR, retro, RICE, code to PRD, competitive analysis, and more.

### Business & Marketing (100+)
SEO auditor, content creator, internal comms, growth strategist, and more.

### Other Categories
Design, Finance, Compliance, Leadership, DevOps, Data, Docs, Knowledge, Learning.

## Smart Navigation

This library includes intelligent indexing for easy discovery:

- **skills/index.html** - Visual navigation with search
- **skills/all_skills.json** - Complete skill list
- **skills/by_category.json** - Skills organized by category
- **skills/by_platform.json** - Skills organized by platform
- **skills/by_keyword.json** - Skills organized by keyword

## Creating New Skills

1. Copy the `SKILL_TEMPLATE.md`
2. Fill in your skill details
3. Place in the appropriate category directory
4. Run `python scripts/build_index.py` to update the index

## License

MIT License. Individual skills may have their own licenses (Apache-2.0, MIT, etc.) - check each skill's directory or the original source repositories.

## Author

Curated and modified by [badhope](https://github.com/badhope)
Original skills by respective authors - see README.md for full credits

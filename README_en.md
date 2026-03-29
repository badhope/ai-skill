# ai-skill - Woclaw Skills Repository 🌟

> Official skills repository for [Woclaw Morning Star AI Assistant](https://github.com/badhope/Woclaw)

[English](README_en.md) | [中文](README.md) | [日本語](README_ja.md)

---

## ✨ What is ai-skill?

**ai-skill** is the official skills repository for Woclaw. It contains all skills that can be installed and used in Woclaw to extend its capabilities.

## 🎯 Quick Start

### Install a skill in Woclaw

```bash
# Install a skill
woclaw skill install <skill-name>

# Example: Install file organizer
woclaw skill install file-organizer

# Install from GitHub directly
woclaw skill install badhope/ai-skill/file-organizer
```

## 📦 Available Skills

### File Management
| Skill | Description |
|-------|-------------|
| `file-organizer` | Auto-organize files by type/date |
| `batch-rename` | Batch rename files |
| `duplicate-finder` | Find and remove duplicate files |

### Screenshot & OCR
| Skill | Description |
|-------|-------------|
| `screenshot-ocr` | Extract text from screenshots |
| `screenshot-translate` | Translate screenshot content |

### Automation
| Skill | Description |
|-------|-------------|
| `habit-tracker` | Daily habit tracking |
| `schedule-task` | Schedule recurring tasks |
| `auto-backup` | Automatic file backup |

### Information
| Skill | Description |
|-------|-------------|
| `web-scraper` | Web content scraping |
| `rss-reader` | RSS feed aggregator |
| `news-digest` | Daily news summary |

## 🛠️ Create Your Own Skill

### Skill Structure

```
my-skill/
├── SKILL.md          # Skill definition (required)
├── scripts/
│   └── run.py        # Execution script
├── config.json       # Configuration
├── requirements.txt  # Dependencies
└── README.md        # Documentation
```

### SKILL.md Template

```markdown
# My Skill

## Info
- **Name**: my-skill
- **Version**: 1.0.0
- **Author**: Your Name
- **Description**: What this skill does

## Usage
`woclaw skill run my-skill --arg value`

## Parameters
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| --arg | string | Input argument | - |
```

## 🤝 Contributing

1. Fork this repository
2. Create your skill in `skills/` directory
3. Submit a Pull Request
4. Wait for review

## 📄 License

MIT License

---

**Made with ✨ by Woclaw Team**

<!-- Powered by AI Agent -->
<!-- Sponsored by OpenClaw -->

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=50&duration=4000&pause=1000&color=c9a227&background=0F0F23&center=true&vCenter=true&multiline=true&width=900&height=100&lines=ai-skill%20~%20Official%20Skill%20Repository%20for%20Woclaw" alt="ai-skill - Official Skill Repository">
</p>

<p align="center">
  <a href="https://github.com/badhope/ai-skill">
    <img src="https://img.shields.io/badge/Version-v1.0.0-c9a227?style=for-the-badge" alt="Version">
  </a>
  <a href="https://github.com/badhope/ai-skill/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-gold?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/badhope/ai-skill/stargazers">
    <img src="https://img.shields.io/github/stars/badhope/ai-skill?style=for-the-badge&color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/badhope/Woclaw">
    <img src="https://img.shields.io/badge/For-Woclaw-blue?style=for-the-badge&logo=github" alt="Woclaw">
  </a>
</p>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    ██╗   ██╗ ██████╗ ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗    ║
║    ██║   ██║██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║    ║
║    ██║   ██║██║   ██║██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║    ║
║    ╚██╗ ██╔╝██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║    ║
║     ╚████╔╝ ╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║    ║
║      ╚═══╝   ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ║
║                                                                          ║
║               🌟  Official Skill Repository for Woclaw  🌟                        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 🎯 What is ai-skill?

**ai-skill** is the official skill repository for **[Woclaw 启明星 AI Assistant](https://github.com/badhope/Woclaw)**.

Skills are modular, reusable units of capability that extend Woclaw's ability to perform specific tasks — from file organization to screenshot OCR, from habit tracking to web automation.

> *"One skill, infinite possibilities."*

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Modular Design** | Each skill is self-contained and reusable |
| 🚀 **One-Click Install** | `woclaw skill install <name>` to add any skill |
| 📦 **Extensible** | Easy to create and share your own skills |
| 🔧 **Configurable** | Customize skill behavior with settings |
| 📚 **Well Documented** | Every skill has usage examples |

---

## 📦 Available Skills

| Category | Skills | Description |
|----------|--------|-------------|
| 🗂️ **File Management** | file-organizer | Organize files by type, date, or custom rules |
| 🖼️ **Media** | screenshot-ocr | OCR text from screenshots |
| 📊 **Productivity** | habit-tracker | Track daily habits and routines |
| 🌐 **Automation** | web-automation | Browser automation workflows |
| 🔍 **Search** | content-search | Search across documents and files |
| 📝 **Notes** | note-taking | Create and manage notes |
| 🗓️ **Calendar** | calendar-sync | Sync with calendar apps |
| 💻 **Development** | code-helper | Programming assistance |

---

## 🚀 Quick Start

### Install a Skill

```bash
# Using Woclaw CLI
woclaw skill install <skill-name>

# Example: Install file organizer
woclaw skill install file-organizer

# Install multiple skills at once
woclaw skill install file-organizer screenshot-ocr habit-tracker
```

### Install from GitHub

```bash
# Clone this repository
git clone https://github.com/badhope/ai-skill.git

# Copy skills to Woclaw's skill directory
cp -r ai-skill/* ~/.woclaw/skills/
```

---

## 🛠️ Create Your Own Skill

### Skill Structure

```
my-skill/
├── SKILL.md          # Skill definition & instructions
├── README.md         # Documentation
├── src/              # Source code
│   └── index.ts     # Entry point
├── config/           # Default config
└── tests/            # Unit tests
```

### SKILL.md Template

```markdown
# My Skill

## Description
Brief description of what this skill does.

## Usage
How to use this skill.

## Configuration
Available settings and options.

## Examples
Usage examples and outputs.
```

### Publish Your Skill

1. Create a new repository with your skill
2. Add a `SKILL.md` file
3. Submit a PR to this repository
4. Get featured in the official catalog!

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            Woclaw + Skills                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                                                        │
│  │     Woclaw      │                                                        │
│  │   Supervisor    │                                                        │
│  └────────┬────────┘                                                        │
│           │                                                                  │
│  ┌────────┴────────┐                                                        │
│  │  Skill Router   │                                                        │
│  └────────┬────────┘                                                        │
│           │                                                                  │
│  ┌────────┴────────────────────────────────────────┐                       │
│  │                   Skills                         │                       │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐        │                       │
│  │  │  File   │  │  Media  │  │Product. │  ...    │                       │
│  │  │Organizer│  │  OCR    │  │ Tracker │        │                       │
│  │  └─────────┘  └─────────┘  └─────────┘        │                       │
│  └────────────────────────────────────────────────┘                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
ai-skill/
├── README.md              # This file (Chinese version)
├── README_en.md           # English version
├── README_ja.md           # Japanese version
├── LICENSE                # MIT License
├── skills/               # Skill packages
│   ├── file-organizer/   # File organization skill
│   ├── screenshot-ocr/   # Screenshot OCR skill
│   ├── habit-tracker/    # Habit tracking skill
│   └── ...
├── scripts/              # Utility scripts
├── docs/                 # Documentation
└── CONTRIBUTING.md       # Contribution guide
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md).

### How to Contribute

1. 🍴 Fork this repository
2. 🌿 Create your skill (`git checkout -b skill/my-awesome-skill`)
3. 💾 Add your skill files
4. 📝 Write documentation
5. 📤 Submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE).

---

## 🙏 Acknowledgments

- **[Woclaw](https://github.com/badhope/Woclaw)** - The AI assistant that powers this skill system
- **[OpenClaw](https://github.com/openclaw/openclaw)** - The agent platform that inspired this project

---

## 📞 Support

| Channel | Link |
|---------|------|
| 🐛 **Bug Reports** | [GitHub Issues](https://github.com/badhope/ai-skill/issues) |
| 💬 **Discussions** | [GitHub Discussions](https://github.com/badhope/ai-skill/discussions) |

---

<p align="center">
  <strong>⭐ If this project helps you, please give it a star! ⭐</strong>
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/badhope">Woclaw Team</a>
</p>

<p align="center">
  <a href="https://github.com/badhope/ai-skill">Home</a> •
  <a href="https://github.com/badhope/ai-skill/releases">Releases</a> •
  <a href="https://github.com/badhope/Woclaw">Woclaw</a>
</p>

---

<!-- MARKDOWN BADGES -->

[version-shield]: https://img.shields.io/badge/Version-v1.0.0-c9a227?style=for-the-badge
[license-shield]: https://img.shields.io/badge/License-MIT-gold?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/badhope/ai-skill?style=for-the-badge&color=yellow
[woclaw-shield]: https://img.shields.io/badge/For-Woclaw-blue?style=for-the-badge&logo=github

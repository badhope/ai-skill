
#!/usr/bin/env python3
"""
技能收集工具 - 自动收集并转换各大厂商的技能
"""

import os
import sys
import shutil
from pathlib import Path
from convert_skill import convert_skill


def collect_anthropic_skills(vendor_dir: Path, target_dir: Path):
    """收集 Anthropic 官方技能"""
    print("\n=== Collecting Anthropic Skills ===")
    
    skill_mapping = {
        "pdf": "tools",
        "docx": "tools",
        "pptx": "tools",
        "xlsx": "tools",
        "skill-creator": "ai",
        "webapp-testing": "development",
        "algorithmic-art": "design",
        "brand-guidelines": "business",
        "canvas-design": "design",
        "frontend-design": "design",
        "internal-comms": "business",
        "mcp-builder": "development",
        "slack-gif-creator": "tools",
        "theme-factory": "design",
        "web-artifacts-builder": "development",
        "claude-api": "development",
        "doc-coauthoring": "docs"
    }
    
    skills_dir = vendor_dir / "anthropic-skills" / "skills"
    if not skills_dir.exists():
        print("Anthropic skills not found")
        return
    
    converted = 0
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            category = skill_mapping.get(skill_dir.name, "tools")
            if convert_skill(skill_dir, target_dir, category, "Anthropic"):
                converted += 1
    
    print(f"Converted {converted} Anthropic skills")


def collect_mattpocock_skills(vendor_dir: Path, target_dir: Path):
    """收集 Matt Pocock 技能"""
    print("\n=== Collecting Matt Pocock Skills ===")
    
    skill_mapping = {
        "caveman": "tools",
        "cook-anything": "tools",
        "grill-me": "productivity",
        "handoff": "tools",
        "write-a-skill": "ai",
        "tdd": "development",
        "to-prd": "product",
        "to-issues": "project-management",
        "improve-codebase-architecture": "development",
        "prototype": "design",
        "diagnose": "development",
        "triager": "development",
        "zoom-out": "tools",
        "git-guardrails-claude-code": "tools",
        "migrate-to-shoehorn": "tools",
        "scaffold-exercises": "learning",
        "setup-pre-commit": "development"
    }
    
    skills_dir = vendor_dir / "mattpocock-skills" / "skills"
    if not skills_dir.exists():
        print("Matt Pocock skills not found")
        return
    
    converted = 0
    for category_dir in skills_dir.iterdir():
        if category_dir.is_dir():
            for skill_dir in category_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    category = skill_mapping.get(skill_dir.name, category_dir.name)
                    if convert_skill(skill_dir, target_dir, category, "Matt Pocock"):
                        converted += 1
    
    print(f"Converted {converted} Matt Pocock skills")


def collect_alirezarezvani_skills(vendor_dir: Path, target_dir: Path):
    """收集 Alireza Rezvani 技能"""
    print("\n=== Collecting Alireza Rezvani Skills ===")
    print("(Skipping - too many skills, manual curation recommended)")


def collect_fullstack_skills(vendor_dir: Path, target_dir: Path):
    """收集 Full Stack 技能"""
    print("\n=== Collecting Full Stack Skills ===")
    print("(Skipping - too many skills, manual curation recommended)")


def update_skill_index(target_dir: Path):
    """更新技能索引"""
    print("\n=== Updating Skill Index ===")
    
    index_path = target_dir / "skills" / "index.json"
    
    categories = {}
    total_skills = 0
    
    skills_base = target_dir / "skills"
    if not skills_base.exists():
        print("No skills directory found")
        return
    
    for category_dir in skills_base.iterdir():
        if category_dir.is_dir() and category_dir.name != "index.json":
            category_name = category_dir.name
            categories[category_name] = {
                "name": category_name,
                "description": f"{category_name.capitalize()} skills",
                "skills": []
            }
            
            for skill_dir in category_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    skill_path = skill_dir / "SKILL.md"
                    content = skill_path.read_text(encoding="utf-8")
                    
                    frontmatter = {}
                    if content.startswith('---'):
                        import re
                        import yaml
                        match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                        if match:
                            try:
                                frontmatter = yaml.safe_load(match.group(1))
                            except:
                                pass
                    
                    skill_info = {
                        "name": frontmatter.get("name", skill_dir.name),
                        "version": frontmatter.get("version", "1.0.0"),
                        "description": frontmatter.get("description", ""),
                        "path": f"skills/{category_name}/{skill_dir.name}"
                    }
                    categories[category_name]["skills"].append(skill_info)
                    total_skills += 1
    
    index_data = {
        "version": "2.0.0",
        "description": "AI-SKILL - Universal Skill Library",
        "categories": categories,
        "total_skills": total_skills
    }
    
    import json
    index_path.write_text(json.dumps(index_data, indent=2, ensure_ascii=False))
    print(f"Updated index with {total_skills} skills in {len(categories)} categories")


def main():
    base_dir = Path(__file__).parent.parent
    vendor_dir = base_dir / "vendor"
    target_dir = base_dir
    
    print("=" * 60)
    print("AI-SKILL - Universal Skill Collector")
    print("=" * 60)
    
    collect_anthropic_skills(vendor_dir, target_dir)
    collect_mattpocock_skills(vendor_dir, target_dir)
    
    update_skill_index(target_dir)
    
    print("\n" + "=" * 60)
    print("Collection complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()


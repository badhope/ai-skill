
#!/usr/bin/env python3
"""
技能转换工具 - 将第三方技能转换为万能格式
"""

import os
import re
import shutil
import yaml
import argparse
from pathlib import Path


def extract_frontmatter(content):
    """
    从内容中提取 YAML frontmatter
    """
    frontmatter = {}
    body = content
    
    if content.startswith('---'):
        match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            try:
                frontmatter = yaml.safe_load(match.group(1))
                body = content[match.end():]
            except Exception as e:
                print(f"Warning: Failed to parse frontmatter: {e}")
    
    return frontmatter, body


def build_universal_frontmatter(original, skill_name, category="tools"):
    """
    构建万能格式的 frontmatter
    """
    fm = {
        "name": original.get("name", skill_name),
        "version": original.get("version", "1.0.0"),
        "description": original.get("description", ""),
        "author": original.get("author", ""),
        "category": category,
        "tags": original.get("tags", []),
        "license": original.get("license", "MIT"),
        "platforms": ["claude", "cursor", "gemini"]
    }
    
    if "allowed-tools" in original:
        fm["allowed-tools"] = original["allowed-tools"]
    
    return fm


def convert_skill(source_dir, target_dir, category="tools", author="Community"):
    """
    转换单个技能
    """
    source_skill = source_dir / "SKILL.md"
    if not source_skill.exists():
        print(f"Skipping {source_dir.name}: no SKILL.md")
        return False
    
    print(f"Converting: {source_dir.name}")
    
    content = source_skill.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(content)
    
    skill_name = source_dir.name.lower().replace("_", "-").replace(" ", "-")
    new_fm = build_universal_frontmatter(frontmatter, skill_name, category)
    new_fm["author"] = frontmatter.get("author", author)
    
    target_skill_dir = target_dir / category / skill_name
    target_skill_dir.mkdir(parents=True, exist_ok=True)
    
    new_content = "---\n"
    new_content += yaml.dump(new_fm, allow_unicode=True, sort_keys=False)
    new_content += "---\n"
    new_content += body
    
    (target_skill_dir / "SKILL.md").write_text(new_content, encoding="utf-8")
    
    for item in ["scripts", "references", "assets", "tests", "examples"]:
        item_path = source_dir / item
        if item_path.exists():
            shutil.copytree(item_path, target_skill_dir / item, dirs_exist_ok=True)
    
    for file in ["README.md", "LICENSE", "CONTRIBUTING.md"]:
        file_path = source_dir / file
        if file_path.exists():
            shutil.copy(file_path, target_skill_dir / file)
    
    return True


def scan_and_convert(vendor_dir, target_dir, category="tools"):
    """
    扫描并转换目录中的所有技能
    """
    converted = 0
    skipped = 0
    
    if not vendor_dir.exists():
        print(f"Directory not found: {vendor_dir}")
        return
    
    for item in vendor_dir.iterdir():
        if item.is_dir():
            if (item / "SKILL.md").exists():
                if convert_skill(item, target_dir, category):
                    converted += 1
                else:
                    skipped += 1
            else:
                for subdir in ["skills", "engineering", "productivity"]:
                    subdir_path = item / subdir
                    if subdir_path.exists():
                        for skill_dir in subdir_path.iterdir():
                            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                                if convert_skill(skill_dir, target_dir, category):
                                    converted += 1
                                else:
                                    skipped += 1
    
    print(f"\nConversion complete!")
    print(f"Converted: {converted}")
    print(f"Skipped: {skipped}")


def main():
    parser = argparse.ArgumentParser(description="Convert skills to universal format")
    parser.add_argument("source", help="Source directory with skills")
    parser.add_argument("target", help="Target directory for converted skills")
    parser.add_argument("--category", default="tools", help="Category for skills")
    parser.add_argument("--author", default="Community", help="Default author name")
    
    args = parser.parse_args()
    
    scan_and_convert(Path(args.source), Path(args.target), args.category)


if __name__ == "__main__":
    main()


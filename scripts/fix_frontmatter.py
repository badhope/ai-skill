#!/usr/bin/env python3
"""修复重复的frontmatter问题"""

import re
from pathlib import Path


def fix_skill_file(skill_path):
    """修复单个技能文件的frontmatter"""
    content = skill_path.read_text(encoding='utf-8')
    
    # 检查是否有两个frontmatter
    if content.count('---') > 2:
        # 找到第一个frontmatter结束位置
        first_end = content.find('---', 3)
        if first_end != -1:
            # 找到第二个frontmatter
            second_start = first_end + 3
            second_end = content.find('---', second_start + 3)
            
            if second_end != -1:
                # 提取第一个frontmatter的内容
                first_fm = content[4:first_end].strip()
                
                # 提取body（第二个frontmatter之后的内容）
                body = content[second_end + 3:].strip()
                
                # 重新组合
                new_content = f"---\n{first_fm}\n---\n\n{body}\n"
                skill_path.write_text(new_content, encoding='utf-8')
                return True
    return False


def main():
    skills_dir = Path(__file__).parent.parent / 'skills'
    fixed = 0
    
    for skill_md in skills_dir.glob('*/**/SKILL.md'):
        if fix_skill_file(skill_md):
            print(f"Fixed: {skill_md}")
            fixed += 1
    
    print(f"\nTotal fixed: {fixed} files")


if __name__ == '__main__':
    main()

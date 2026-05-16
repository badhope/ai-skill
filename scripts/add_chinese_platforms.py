#!/usr/bin/env python3
"""为所有技能添加国内平台支持"""

import re
from pathlib import Path


def add_chinese_platforms_to_skill(skill_path):
    """为单个技能文件添加国内平台"""
    content = skill_path.read_text(encoding='utf-8')
    
    # 查找并替换 platforms 字段
    old_pattern = r'(platforms:\s*\[)[^\]]*(\])'
    new_platforms = 'claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance'
    
    # 先检查是否已经有国内平台
    if 'doubao' in content or 'qwen' in content or 'spark' in content:
        return False  # 已经有国内平台了
    
    new_content = re.sub(old_pattern, r'\1' + new_platforms + r'\2', content)
    
    if new_content != content:
        skill_path.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    skills_dir = Path(__file__).parent.parent / 'skills'
    updated = 0
    skipped = 0
    
    print("=" * 70)
    print("为所有技能添加国内平台支持")
    print("=" * 70)
    print()
    
    for skill_md in skills_dir.glob('*/**/SKILL.md'):
        if add_chinese_platforms_to_skill(skill_md):
            print(f"✅ 更新: {skill_md}")
            updated += 1
        else:
            skipped += 1
    
    print()
    print("=" * 70)
    print(f"更新完成！")
    print(f"更新的技能: {updated}")
    print(f"已包含国内平台的技能: {skipped}")
    print()
    print("新增的国内平台:")
    print("- doubao (豆包)")
    print("- qwen (通义千问)")
    print("- spark (讯飞星火)")
    print("- moonshot (月之暗面)")
    print("- baidu (文心一言)")
    print("- alibaba (阿里云)")
    print("- bytedance (字节跳动)")
    print()
    print("所有技能现在支持: 13个平台")


if __name__ == '__main__':
    main()

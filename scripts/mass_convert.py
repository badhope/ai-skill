#!/usr/bin/env python3
"""
大规模技能转换工具 - 转换所有vendor仓库的技能到通用格式
"""

import os
import re
import shutil
from pathlib import Path
import json


def convert_single_skill(source_skill_path, target_category, author_name, license_name):
    """转换单个技能"""
    source_dir = Path(source_skill_path)
    skill_name = source_dir.name
    skill_md = source_dir / "SKILL.md"
    
    if not skill_md.exists():
        return None, f"No SKILL.md in {source_dir}"
    
    try:
        content = skill_md.read_text(encoding='utf-8')
    except Exception as e:
        return None, f"Error reading {skill_md}: {e}"
    
    # 提取现有的frontmatter
    frontmatter = {}
    body = content
    has_frontmatter = False
    
    if content.startswith('---'):
        match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            has_frontmatter = True
            fm_content = match.group(1)
            body = content[match.end():]
            for line in fm_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
    
    # 构建新的通用frontmatter
    new_name = frontmatter.get('name', skill_name)
    new_desc = frontmatter.get('description', f"{skill_name} skill")
    
    new_fm = {
        'name': new_name,
        'version': frontmatter.get('version', '1.0.0'),
        'description': new_desc,
        'author': frontmatter.get('author', author_name),
        'category': target_category,
        'tags': frontmatter.get('tags', [skill_name]),
        'license': license_name,
        'platforms': ['claude', 'cursor', 'gemini', 'codex', 'hermes']
    }
    
    if 'allowed-tools' in frontmatter:
        new_fm['allowed-tools'] = frontmatter['allowed-tools']
    
    # 生成新的SKILL.md
    fm_str = '---\n'
    for key, value in new_fm.items():
        if isinstance(value, list):
            fm_str += f"{key}: [{', '.join(f'{v}' for v in value)}]\n"
        else:
            fm_str += f"{key}: {value}\n"
    fm_str += '---\n'
    
    new_content = fm_str + body
    
    # 创建目标目录
    target_dir = Path(__file__).parent.parent / 'skills' / target_category / new_name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    (target_dir / 'SKILL.md').write_text(new_content, encoding='utf-8')
    
    # 复制其他文件
    for item in ['scripts', 'references', 'assets', 'templates', 'examples', 'core']:
        item_path = source_dir / item
        if item_path.exists():
            try:
                if (target_dir / item).exists():
                    shutil.rmtree(target_dir / item)
                shutil.copytree(item_path, target_dir / item)
            except Exception as e:
                print(f"  Warning: Could not copy {item}: {e}")
    
    for file in ['README.md', 'LICENSE', 'LICENSE.txt', '.gitignore']:
        file_path = source_dir / file
        if file_path.exists():
            try:
                shutil.copy(file_path, target_dir)
            except Exception as e:
                print(f"  Warning: Could not copy {file}: {e}")
    
    return new_fm, None


def scan_and_convert_anthropic():
    """扫描并转换Anthropic技能"""
    print("=" * 70)
    print("Converting Anthropic Skills")
    print("=" * 70)
    
    vendor_base = Path(__file__).parent.parent / 'vendor' / 'anthropic-skills' / 'skills'
    if not vendor_base.exists():
        print("Anthropic skills not found!")
        return {}
    
    category_map = {
        'algorithmic-art': 'design',
        'brand-guidelines': 'design',
        'canvas-design': 'design',
        'frontend-design': 'design',
        'theme-factory': 'design',
        'pdf': 'tools',
        'docx': 'tools',
        'pptx': 'tools',
        'xlsx': 'tools',
        'slack-gif-creator': 'tools',
        'mcp-builder': 'development',
        'webapp-testing': 'development',
        'web-artifacts-builder': 'development',
        'claude-api': 'development',
        'skill-creator': 'ai',
        'doc-coauthoring': 'docs',
        'internal-comms': 'business'
    }
    
    converted = {}
    count = 0
    
    for skill_dir in vendor_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        category = category_map.get(skill_dir.name, 'tools')
        result, error = convert_single_skill(skill_dir, category, 'Anthropic', 'Apache-2.0')
        
        if error:
            print(f"❌ {skill_dir.name}: {error}")
        else:
            print(f"✅ {skill_dir.name} -> {category}/{result['name']}")
            if category not in converted:
                converted[category] = []
            converted[category].append(result)
            count += 1
    
    print(f"\nConverted {count} Anthropic skills!")
    return converted


def scan_and_convert_matt_pocock():
    """扫描并转换Matt Pocock技能"""
    print("\n" + "=" * 70)
    print("Converting Matt Pocock Skills")
    print("=" * 70)
    
    vendor_base = Path(__file__).parent.parent / 'vendor' / 'mattpocock-skills' / 'skills'
    if not vendor_base.exists():
        print("Matt Pocock skills not found!")
        return {}
    
    category_map = {
        'engineering': 'development',
        'productivity': 'tools',
        'misc': 'tools'
    }
    
    converted = {}
    count = 0
    
    for cat_dir in ['engineering', 'productivity', 'misc']:
        cat_path = vendor_base / cat_dir
        if not cat_path.exists():
            continue
        
        target_category = category_map.get(cat_dir, 'tools')
        
        for skill_dir in cat_path.iterdir():
            if not skill_dir.is_dir():
                continue
            if skill_dir.name in ['setup-matt-pocock-skills']:
                continue
            
            result, error = convert_single_skill(skill_dir, target_category, 'Matt Pocock', 'MIT')
            
            if error:
                print(f"❌ {skill_dir.name}: {error}")
            else:
                print(f"✅ {skill_dir.name} -> {target_category}/{result['name']}")
                if target_category not in converted:
                    converted[target_category] = []
                converted[target_category].append(result)
                count += 1
    
    print(f"\nConverted {count} Matt Pocock skills!")
    return converted


def update_skill_index():
    """更新技能索引文件"""
    print("\n" + "=" * 70)
    print("Updating Skill Index")
    print("=" * 70)
    
    skills_base = Path(__file__).parent.parent / 'skills'
    index_path = skills_base / 'index.json'
    
    categories = {}
    total_skills = 0
    
    for category_dir in skills_base.iterdir():
        if not category_dir.is_dir() or category_dir.name == 'index.json':
            continue
        
        cat_name = category_dir.name
        categories[cat_name] = {
            'name': cat_name,
            'description': f'{cat_name} skills',
            'skills': []
        }
        
        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            
            skill_md = skill_dir / 'SKILL.md'
            if not skill_md.exists():
                continue
            
            try:
                content = skill_md.read_text(encoding='utf-8')
                
                fm = {}
                if content.startswith('---'):
                    match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                    if match:
                        for line in match.group(1).split('\n'):
                            if ':' in line:
                                key, value = line.split(':', 1)
                                fm[key.strip()] = value.strip()
                
                skill_info = {
                    'name': fm.get('name', skill_dir.name),
                    'version': fm.get('version', '1.0.0'),
                    'description': fm.get('description', ''),
                    'author': fm.get('author', 'Community'),
                    'license': fm.get('license', 'MIT'),
                    'path': f'skills/{cat_name}/{skill_dir.name}'
                }
                
                author = skill_info['author']
                if 'Anthropic' in author:
                    skill_info['source'] = 'Anthropic'
                elif 'Matt' in author:
                    skill_info['source'] = 'Matt Pocock'
                elif 'badhope' in author or 'Woclaw' in author:
                    skill_info['source'] = 'Original'
                
                categories[cat_name]['skills'].append(skill_info)
                total_skills += 1
                print(f"Indexed: {cat_name}/{skill_dir.name}")
                
            except Exception as e:
                print(f"Warning: Could not index {skill_dir}: {e}")
    
    index_data = {
        'version': '3.0.0',
        'description': 'Universal Agent Skill Library - 300+ skills',
        'categories': categories,
        'total_skills': total_skills
    }
    
    index_path.write_text(json.dumps(index_data, indent=2, ensure_ascii=False))
    print(f"\nIndex updated! Total: {total_skills} skills across {len(categories)} categories")
    
    return total_skills


def main():
    print("=" * 70)
    print("Universal Agent Skills - Mass Converter")
    print("=" * 70)
    
    # 转换Anthropic技能
    anthropic_converted = scan_and_convert_anthropic()
    
    # 转换Matt Pocock技能
    matt_converted = scan_and_convert_matt_pocock()
    
    # 更新索引
    total = update_skill_index()
    
    print("\n" + "=" * 70)
    print(f"✅ Mass Conversion Complete! Total skills: {total}")
    print("=" * 70)


if __name__ == '__main__':
    main()

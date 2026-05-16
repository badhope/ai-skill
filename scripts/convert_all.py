#!/usr/bin/env python3
"""
全面技能转换工具 - 转换所有vendor仓库中的技能到通用格式
"""

import os
import re
import shutil
from pathlib import Path
import json


def convert_markdown_to_skill(md_path, target_category, author_name, license_name):
    """将markdown文件转换为技能格式"""
    md_path = Path(md_path)
    skill_name = md_path.stem
    content = md_path.read_text(encoding='utf-8')
    
    new_fm = {
        'name': skill_name,
        'version': '1.0.0',
        'description': f"{skill_name} command/skill",
        'author': author_name,
        'category': target_category,
        'tags': [skill_name],
        'license': license_name,
        'platforms': ['claude', 'cursor', 'gemini', 'codex', 'hermes']
    }
    
    fm_str = '---\n'
    for key, value in new_fm.items():
        if isinstance(value, list):
            fm_str += f"{key}: [{', '.join(f'{v}' for v in value)}]\n"
        else:
            fm_str += f"{key}: {value}\n"
    fm_str += '---\n'
    
    new_content = fm_str + content
    
    target_dir = Path(__file__).parent.parent / 'skills' / target_category / skill_name
    target_dir.mkdir(parents=True, exist_ok=True)
    
    (target_dir / 'SKILL.md').write_text(new_content, encoding='utf-8')
    print(f"✅ Converted: {skill_name} -> {target_category}/{skill_name}")
    return new_fm


def convert_alirezarezvani_commands():
    """转换Alireza Rezvani的命令技能"""
    print("\n" + "="*70)
    print("Converting Alireza Rezvani Commands")
    print("="*70)
    
    base_dir = Path(__file__).parent.parent / 'vendor' / 'alirezarezvani-skills' / 'commands'
    if not base_dir.exists():
        print("Commands directory not found!")
        return 0
    
    count = 0
    category_map = {
        'a11y-audit': 'development',
        'changelog': 'tools',
        'chaos-experiment': 'development',
        'code-to-prd': 'product',
        'competitive-matrix': 'business',
        'financial-health': 'finance',
        'flag-cleanup': 'development',
        'focused-fix': 'development',
        'google-workspace': 'tools',
        'karpathy-check': 'development',
        'okr': 'product',
        'operator-audit': 'development',
        'persona': 'ai',
        'pipeline': 'devops',
        'plugin-audit': 'development',
        'prd': 'product',
        'project-health': 'development',
        'retro': 'product',
        'rice': 'product',
        'saas-health': 'business',
        'seo-auditor': 'business',
        'slo-design': 'devops',
        'sprint-health': 'product',
        'sprint-plan': 'product',
        'tc': 'development',
        'tdd': 'development',
        'tech-debt': 'development',
        'user-story': 'product',
        'wiki-ingest': 'knowledge',
        'wiki-init': 'knowledge',
        'wiki-lint': 'knowledge',
        'wiki-log': 'knowledge',
        'wiki-query': 'knowledge'
    }
    
    for md_file in base_dir.glob('*.md'):
        skill_name = md_file.stem
        category = category_map.get(skill_name, 'tools')
        convert_markdown_to_skill(md_file, category, 'Alireza Rezvani', 'MIT')
        count += 1
    
    print(f"\nConverted {count} Alireza Rezvani commands!")
    return count


def convert_fullstack_skills():
    """转换Fullstack技能库"""
    print("\n" + "="*70)
    print("Converting Fullstack Skills")
    print("="*70)
    
    base_dir = Path(__file__).parent.parent / 'vendor' / 'fullstack-skills' / 'skills'
    if not base_dir.exists():
        print("Fullstack skills directory not found!")
        return 0
    
    count = 0
    category_map = {
        'angular-skills': 'development',
        'antd-skills': 'development',
        'build-skills': 'devops',
        'chart-skills': 'tools',
        'cocos-skills': 'development',
        'database-skills': 'development',
        'ddd-skills': 'development',
        'dev-utils-skills': 'tools',
        'docker-skills': 'devops',
        'document-skills': 'docs',
        'drawio-skills': 'tools',
        'flutter-skills': 'development',
        'go-skills': 'development',
        'mobile-native-skills': 'development',
        'nvm-skills': 'devops',
        'ocrmypdf-skills': 'tools',
        'react-skills': 'development',
        'social-skills': 'business',
        'spring-skills': 'development',
        'svelte-skills': 'development',
        't2ui-skills': 'development',
        'testing-skills': 'development',
        'threejs-skills': 'development',
        'uniapp-skills': 'development',
        'utility-skills': 'tools',
        'uview-skills': 'development',
        'teaching-skills': 'learning'
    }
    
    for skill_category in base_dir.iterdir():
        if not skill_category.is_dir():
            continue
        
        cat_name = skill_category.name
        category = category_map.get(cat_name, 'tools')
        
        for skill_dir in skill_category.iterdir():
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
                
                new_name = fm.get('name', skill_dir.name)
                new_desc = fm.get('description', f"{new_name} skill")
                
                new_fm = {
                    'name': new_name,
                    'version': fm.get('version', '1.0.0'),
                    'description': new_desc,
                    'author': fm.get('author', 'Fullstack Skills Community'),
                    'category': category,
                    'tags': fm.get('tags', [new_name]),
                    'license': 'MIT',
                    'platforms': ['claude', 'cursor', 'gemini', 'codex', 'hermes']
                }
                
                fm_str = '---\n'
                for key, value in new_fm.items():
                    if isinstance(value, list):
                        fm_str += f"{key}: [{', '.join(f'{v}' for v in value)}]\n"
                    else:
                        fm_str += f"{key}: {value}\n"
                fm_str += '---\n'
                
                body = content
                if content.startswith('---'):
                    match = re.search(r'^---\n.*?\n---\n', content, re.DOTALL)
                    if match:
                        body = content[match.end():]
                
                new_content = fm_str + body
                
                target_dir = Path(__file__).parent.parent / 'skills' / category / new_name
                target_dir.mkdir(parents=True, exist_ok=True)
                
                (target_dir / 'SKILL.md').write_text(new_content, encoding='utf-8')
                
                for item in ['scripts', 'references', 'assets']:
                    item_path = skill_dir / item
                    if item_path.exists():
                        try:
                            if (target_dir / item).exists():
                                shutil.rmtree(target_dir / item)
                            shutil.copytree(item_path, target_dir / item)
                        except:
                            pass
                
                for file in ['README.md', 'LICENSE', 'LICENSE.txt']:
                    file_path = skill_dir / file
                    if file_path.exists():
                        try:
                            shutil.copy(file_path, target_dir)
                        except:
                            pass
                
                print(f"✅ Converted: {skill_dir.name} -> {category}/{new_name}")
                count += 1
                
            except Exception as e:
                print(f"❌ Error converting {skill_dir.name}: {e}")
    
    print(f"\nConverted {count} Fullstack skills!")
    return count


def convert_alirezarezvani_agents():
    """转换Alireza Rezvani的智能体技能"""
    print("\n" + "="*70)
    print("Converting Alireza Rezvani Agents")
    print("="*70)
    
    base_dir = Path(__file__).parent.parent / 'vendor' / 'alirezarezvani-skills' / 'agents'
    if not base_dir.exists():
        print("Agents directory not found!")
        return 0
    
    count = 0
    category_map = {
        'business-growth': 'business',
        'c-level': 'leadership',
        'engineering': 'development',
        'engineering-team': 'development',
        'finance': 'finance',
        'marketing': 'business',
        'personas': 'ai',
        'product': 'product',
        'project-management': 'product',
        'ra-qm-team': 'compliance'
    }
    
    for agent_category in base_dir.iterdir():
        if not agent_category.is_dir():
            continue
        
        cat_name = agent_category.name
        category = category_map.get(cat_name, 'ai')
        
        for agent_file in agent_category.glob('*.md'):
            if agent_file.name == 'CLAUDE.md' or agent_file.name == 'TEMPLATE.md':
                continue
            
            skill_name = agent_file.stem.replace('cs-', '')
            convert_markdown_to_skill(agent_file, category, 'Alireza Rezvani', 'MIT')
            count += 1
    
    print(f"\nConverted {count} Alireza Rezvani agents!")
    return count


def update_skill_index():
    """更新技能索引"""
    print("\n" + "="*70)
    print("Updating Skill Index")
    print("="*70)
    
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
                elif 'Alireza' in author:
                    skill_info['source'] = 'Alireza Rezvani'
                elif 'badhope' in author or 'Woclaw' in author:
                    skill_info['source'] = 'Original'
                elif 'Fullstack' in author:
                    skill_info['source'] = 'Fullstack Skills'
                
                categories[cat_name]['skills'].append(skill_info)
                total_skills += 1
                
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
    print("="*70)
    print("Universal Agent Skills - Complete Conversion")
    print("="*70)
    
    total = 0
    
    total += convert_alirezarezvani_commands()
    total += convert_alirezarezvani_agents()
    total += convert_fullstack_skills()
    
    final_count = update_skill_index()
    
    print("\n" + "="*70)
    print(f"✅ Complete Conversion! Total skills: {final_count}")
    print("="*70)


if __name__ == '__main__':
    main()

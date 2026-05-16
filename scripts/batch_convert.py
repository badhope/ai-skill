#!/usr/bin/env python3
"""Batch convert skills from vendor directories to universal format"""

import os
import sys
import shutil
import re
from pathlib import Path


def convert_skill_to_universal(source_dir, target_dir, default_category='tools', default_author='Anthropic', default_license='Apache-2.0'):
    """Convert a single skill to universal format"""
    source_skill = Path(source_dir) / 'SKILL.md'
    if not source_skill.exists():
        print(f"Skipping {source_dir}: no SKILL.md")
        return False

    try:
        content = source_skill.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {source_skill}: {e}")
        return False

    frontmatter = {}
    body = content
    
    if content.startswith('---'):
        match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            fm_content = match.group(1)
            body = content[match.end():]
            
            for line in fm_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()

    name = frontmatter.get('name', Path(source_dir).name)
    description = frontmatter.get('description', '')
    original_license = frontmatter.get('license', '')
    
    target_name = name.replace('_', '-').replace(' ', '-')
    
    new_fm = {
        'name': target_name,
        'version': '1.0.0',
        'description': description,
        'author': default_author,
        'category': default_category,
        'tags': [name],
        'license': default_license if 'Apache' in original_license or 'MIT' in original_license else 'Apache-2.0',
        'platforms': ['claude', 'cursor', 'gemini']
    }

    new_fm_str = '---\n'
    for key, value in new_fm.items():
        if isinstance(value, list):
            quoted_values = [f"'{v}'" for v in value]
            new_fm_str += f"{key}: [{', '.join(quoted_values)}]\n"
        else:
            new_fm_str += f"{key}: {value}\n"
    new_fm_str += '---\n'

    new_content = new_fm_str + body

    target_skill_dir = Path(target_dir) / 'skills' / default_category / target_name
    target_skill_dir.mkdir(parents=True, exist_ok=True)

    (target_skill_dir / 'SKILL.md').write_text(new_content, encoding='utf-8')
    
    for subdir in ['scripts', 'references', 'assets', 'templates', 'examples', 'core']:
        subdir_path = Path(source_dir) / subdir
        if subdir_path.exists() and subdir_path.is_dir():
            try:
                shutil.copytree(subdir_path, target_skill_dir / subdir, dirs_exist_ok=True)
            except Exception as e:
                print(f"Warning: Could not copy {subdir}: {e}")
    
    for file in ['README.md', 'LICENSE.txt', 'LICENSE']:
        file_path = Path(source_dir) / file
        if file_path.exists():
            try:
                shutil.copy(file_path, target_skill_dir)
            except Exception as e:
                print(f"Warning: Could not copy {file}: {e}")

    print(f"✓ Converted: {name} -> {default_category}/{target_name}")
    return True


def get_category_for_skill(skill_name):
    """Map skill names to appropriate categories"""
    categories = {
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
        'skill-creator': 'ai',
        'claude-api': 'development',
        'doc-coauthoring': 'docs',
        'internal-comms': 'business',
    }
    return categories.get(skill_name, 'tools')


def convert_anthropic_skills(vendor_dir, target_dir):
    """Convert all Anthropic skills"""
    print("\n" + "="*60)
    print("Converting Anthropic Skills")
    print("="*60)
    
    skills_dir = Path(vendor_dir) / 'anthropic-skills' / 'skills'
    if not skills_dir.exists():
        print(f"Skills directory not found: {skills_dir}")
        return
    
    converted = 0
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
            category = get_category_for_skill(skill_dir.name)
            if convert_skill_to_universal(skill_dir, target_dir, category, 'Anthropic', 'Apache-2.0'):
                converted += 1
    
    print(f"\nTotal Anthropic skills converted: {converted}")


def convert_matt_pocock_skills(vendor_dir, target_dir):
    """Convert Matt Pocock skills"""
    print("\n" + "="*60)
    print("Converting Matt Pocock Skills")
    print("="*60)
    
    base_dir = Path(vendor_dir) / 'mattpocock-skills' / 'skills'
    if not base_dir.exists():
        print(f"Skills directory not found: {base_dir}")
        return
    
    converted = 0
    category_mapping = {
        'engineering': 'development',
        'productivity': 'tools',
        'misc': 'tools',
        'personal': 'tools',
    }
    
    for cat_dir in ['engineering', 'productivity', 'misc']:
        cat_path = base_dir / cat_dir
        if cat_path.exists():
            target_cat = category_mapping.get(cat_dir, 'tools')
            for skill_dir in cat_path.iterdir():
                if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
                    if skill_dir.name in ['setup-matt-pocock-skills']:
                        continue
                    if convert_skill_to_universal(skill_dir, target_dir, target_cat, 'Matt Pocock', 'MIT'):
                        converted += 1
    
    print(f"\nTotal Matt Pocock skills converted: {converted}")


def update_skill_index(target_dir):
    """Update the skill index.json"""
    print("\n" + "="*60)
    print("Updating Skill Index")
    print("="*60)
    
    skills_base = Path(target_dir) / 'skills'
    index_path = skills_base / 'index.json'
    
    categories = {}
    total_skills = 0
    
    for category_dir in skills_base.iterdir():
        if category_dir.is_dir() and category_dir.name != 'index.json':
            cat_name = category_dir.name
            categories[cat_name] = {
                'name': cat_name,
                'description': f'{cat_name} skills',
                'skills': []
            }
            
            for skill_dir in category_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
                    skill_path = skill_dir / 'SKILL.md'
                    try:
                        content = skill_path.read_text(encoding='utf-8')
                        
                        fm = {}
                        if content.startswith('---'):
                            match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                            if match:
                                fm_content = match.group(1)
                                for line in fm_content.split('\n'):
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
                        
                        if 'Anthropic' in skill_info['author']:
                            skill_info['source'] = 'Anthropic'
                        elif 'Matt' in skill_info['author']:
                            skill_info['source'] = 'Matt Pocock'
                        
                        categories[cat_name]['skills'].append(skill_info)
                        total_skills += 1
                    except Exception as e:
                        print(f"Warning: Could not read {skill_path}: {e}")
    
    index_data = {
        'version': '2.0.0',
        'description': 'AI-SKILL - Universal Agent Skill Library',
        'categories': categories,
        'total_skills': total_skills
    }
    
    import json
    index_path.write_text(json.dumps(index_data, indent=2, ensure_ascii=False))
    print(f"Index updated with {total_skills} skills in {len(categories)} categories")


def main():
    base_dir = Path(__file__).parent.parent
    vendor_dir = base_dir / 'vendor'
    target_dir = base_dir
    
    convert_anthropic_skills(vendor_dir, target_dir)
    convert_matt_pocock_skills(vendor_dir, target_dir)
    update_skill_index(target_dir)
    
    print("\n" + "="*60)
    print("Batch conversion complete!")
    print("="*60)


if __name__ == '__main__':
    main()

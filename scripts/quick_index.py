#!/usr/bin/env python3
"""Quick script to generate proper index"""

import json
from pathlib import Path
import re


def main():
    base_dir = Path(__file__).parent.parent
    skills_dir = base_dir / 'skills'
    
    categories = {}
    total_skills = 0
    
    for cat_dir in skills_dir.iterdir():
        if cat_dir.is_dir() and cat_dir.name != 'index.json':
            cat_name = cat_dir.name
            categories[cat_name] = {
                'name': cat_name,
                'description': f'{cat_name} skills',
                'skills': []
            }
            
            for skill_dir in cat_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / 'SKILL.md').exists():
                    skill_path = skill_dir / 'SKILL.md'
                    try:
                        content = skill_path.read_text(encoding='utf-8')
                        
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
                        elif 'badhope' in author:
                            skill_info['source'] = 'Original'
                        
                        categories[cat_name]['skills'].append(skill_info)
                        total_skills += 1
                        print(f"Found: {cat_name}/{skill_dir.name} by {skill_info['author']}")
                    except Exception as e:
                        print(f"Error: {skill_path}: {e}")
    
    index_data = {
        'version': '2.0.0',
        'description': 'AI-SKILL - Universal Agent Skill Library',
        'categories': categories,
        'total_skills': total_skills
    }
    
    index_path = skills_dir / 'index.json'
    index_path.write_text(json.dumps(index_data, indent=2, ensure_ascii=False))
    
    print(f"\nTotal skills: {total_skills}")
    print(f"Categories: {list(categories.keys())}")


if __name__ == '__main__':
    main()

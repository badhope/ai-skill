#!/usr/bin/env python3
"""
智能去重系统 - 检测并去除几乎完全重复的技能
"""

import os
import json
import hashlib
from pathlib import Path
from difflib import SequenceMatcher

def get_content_hash(path):
    """计算文件内容哈希"""
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return hashlib.md5(f.read().encode()).hexdigest()

def get_skill_hash(skill_dir):
    """获取技能目录的组合哈希"""
    hashes = []
    for md_file in sorted(skill_dir.rglob("*.md")):
        hashes.append(get_content_hash(md_file))
    return hashlib.md5(''.join(hashes).encode()).hexdigest()[:12]

def scan_skills():
    """扫描所有技能"""
    skills = []
    skill_dir = Path("skills")
    
    for category in skill_dir.iterdir():
        if not category.is_dir() or category.name.startswith('.'):
            continue
        
        for skill_path in category.iterdir():
            if not skill_path.is_dir() or skill_path.name.startswith('.'):
                continue
            
            main_file = skill_path / "SKILL.md"
            if not main_file.exists():
                continue
            
            with open(main_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            name = skill_path.name
            desc = ""
            author = "unknown"
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    for line in parts[1].split('\n'):
                        if ':' in line:
                            k, v = line.split(':', 1)
                            k = k.strip().lower()
                            v = v.strip().strip('"\'')
                            if k == 'name':
                                name = v
                            elif k == 'description':
                                desc = v
                            elif k == 'author':
                                author = v
            
            main_content = content.split('---', 2)[-1] if '---' in content else content
            main_hash = hashlib.md5(main_content.encode()).hexdigest()[:16]
            
            skills.append({
                'name': name,
                'path': str(skill_path),
                'category': category.name,
                'description': desc,
                'author': author,
                'main_hash': main_hash,
                'content': main_content.lower()[:1000]
            })
    
    return skills

def find_duplicates(skills):
    """检测重复技能"""
    duplicates = []
    content_hashes = {}
    name_similar = {}
    
    for skill in skills:
        h = skill['main_hash']
        if h in content_hashes:
            content_hashes[h].append(skill)
        else:
            content_hashes[h] = [skill]
        
        name_key = skill['name'].lower().replace('-', '').replace('_', '')
        if name_key not in name_similar:
            name_similar[name_key] = []
        name_similar[name_key].append(skill)
    
    exact_dups = [(k, v) for k, v in content_hashes.items() if len(v) > 1]
    
    for h, dup_list in exact_dups:
        print(f"\n🔴 完全重复 (哈希: {h}):")
        for s in dup_list:
            print(f"   - {s['path']}")
        duplicates.extend([s['path'] for s in dup_list[1:]])
    
    for name_key, name_list in name_similar.items():
        if len(name_list) > 1 and all(len(k) > 5 for k in name_key):
            similar = []
            for i in range(len(name_list)):
                for j in range(i+1, len(name_list)):
                    sim = SequenceMatcher(None, name_list[i]['content'][:500], name_list[j]['content'][:500]).ratio()
                    if sim > 0.85:
                        similar.append((name_list[i], name_list[j], sim))
            
            if similar:
                print(f"\n🟡 高度相似 ({name_key}):")
                for s1, s2, sim in similar:
                    print(f"   {s1['path']} <-> {s2['path']} ({sim:.1%})")
                    if s2['path'] not in duplicates:
                        duplicates.append(s2['path'])
    
    return list(set(duplicates))

def remove_duplicates(paths_to_remove):
    """删除重复技能"""
    removed = []
    for path in paths_to_remove:
        try:
            import shutil
            shutil.rmtree(path)
            removed.append(path)
            print(f"🗑️  删除: {path}")
        except Exception as e:
            print(f"❌ 删除失败: {path} - {e}")
    return removed

def main():
    print("="*60)
    print("🔍 智能去重系统")
    print("="*60)
    
    print("\n📂 扫描技能...")
    skills = scan_skills()
    print(f"✅ 找到 {len(skills)} 个技能")
    
    print("\n🔎 检测重复...")
    duplicates = find_duplicates(skills)
    
    print(f"\n📊 检测结果:")
    print(f"   发现 {len(duplicates)} 个重复技能")
    
    if duplicates:
        print("\n⚠️  将要删除的重复技能:")
        for d in duplicates[:20]:
            print(f"   - {d}")
        if len(duplicates) > 20:
            print(f"   ... 还有 {len(duplicates) - 20} 个")
        
        print("\n🔄 自动删除重复技能...")
        removed = remove_duplicates(duplicates)
        print(f"\n✅ 已删除 {len(removed)} 个重复技能")
    else:
        print("\n✅ 没有发现重复技能!")

if __name__ == '__main__':
    main()

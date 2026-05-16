#!/usr/bin/env python3
"""
智能技能索引系统 - 优化版
"""

import os
import json
import hashlib
from pathlib import Path
from collections import defaultdict

def main():
    skills_dir = Path("skills")
    all_skills = []
    by_category = defaultdict(list)
    by_platform = defaultdict(list)
    by_keyword = defaultdict(list)
    
    platforms = ['claude', 'cursor', 'gemini', 'codex', 'doubao', 'qwen', 'spark', 'moonshot', 'baidu', 'alibaba', 'bytedance']
    keywords = ['code', 'web', 'api', 'data', 'test', 'deploy', 'security', 'debug', 'database', 'cloud', 'devops', 'frontend', 'backend', 'mobile', 'automation', 'analysis', 'writing', 'design', 'prompt', 'llm', 'ai', 'ml', 'python', 'javascript', 'typescript', 'rust', 'go', 'docker', 'kubernetes', 'aws', 'azure', 'git']
    
    print("🔍 扫描所有技能...")
    
    for category in sorted(skills_dir.iterdir()):
        if not category.is_dir() or category.name.startswith('.'):
            continue
        
        for skill_dir in sorted(category.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue
            
            skill_file = skill_dir / "SKILL.md"
            if not skill_file.exists():
                continue
            
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            name = skill_dir.name
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
            
            if not desc:
                main_content = content.split('---', 2)[-1] if '---' in content else content
                desc = main_content[:200].replace('\n', ' ').strip()
            
            path = str(skill_dir)
            skill_info = {
                'name': name,
                'path': path,
                'category': category.name,
                'description': desc[:150],
                'author': author
            }
            
            all_skills.append(skill_info)
            by_category[category.name].append({'name': name, 'path': path, 'description': desc[:80]})
            
            desc_lower = desc.lower() + ' ' + name.lower()
            for platform in platforms:
                if platform in desc_lower:
                    by_platform[platform].append({'name': name, 'path': path})
            
            for keyword in keywords:
                if keyword in desc_lower:
                    by_keyword[keyword].append({'name': name, 'path': path})
    
    print(f"✅ 找到 {len(all_skills)} 个技能")
    
    print("📝 保存索引文件...")
    
    with open('skills/all_skills.json', 'w', encoding='utf-8') as f:
        json.dump(all_skills, f, ensure_ascii=False, indent=2)
    
    with open('skills/by_category.json', 'w', encoding='utf-8') as f:
        json.dump({k: list(v) for k, v in sorted(by_category.items())}, f, ensure_ascii=False, indent=2)
    
    with open('skills/by_platform.json', 'w', encoding='utf-8') as f:
        json.dump({k: list(v) for k, v in sorted(by_platform.items())}, f, ensure_ascii=False, indent=2)
    
    with open('skills/by_keyword.json', 'w', encoding='utf-8') as f:
        json.dump({k: list(v) for k, v in sorted(by_keyword.items())}, f, ensure_ascii=False, indent=2)
    
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-SKILL 技能导航</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; }
        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
        header { text-align: center; padding: 3rem 0; border-bottom: 1px solid #334155; margin-bottom: 2rem; }
        h1 { font-size: 2.5rem; margin-bottom: 1rem; background: linear-gradient(135deg, #60a5fa, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .stats { display: flex; justify-content: center; gap: 3rem; margin-top: 1rem; }
        .stat { text-align: center; }
        .stat-number { font-size: 2rem; font-weight: bold; color: #60a5fa; }
        .stat-label { color: #94a3b8; font-size: 0.9rem; }
        .search-box { max-width: 600px; margin: 2rem auto; }
        .search-box input { width: 100%; padding: 1rem 1.5rem; border-radius: 12px; border: 2px solid #334155; background: #1e293b; color: white; font-size: 1rem; }
        .search-box input:focus { outline: none; border-color: #60a5fa; }
        .categories { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }
        .category-card { background: #1e293b; border-radius: 12px; padding: 1.5rem; border: 1px solid #334155; }
        .category-card h2 { color: #60a5fa; margin-bottom: 1rem; font-size: 1.2rem; display: flex; justify-content: space-between; align-items: center; }
        .category-card .count { background: #334155; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.85rem; }
        .skill-list { list-style: none; max-height: 300px; overflow-y: auto; }
        .skill-list li { padding: 0.5rem 0; border-bottom: 1px solid #334155; }
        .skill-list li:last-child { border-bottom: none; }
        .skill-list a { color: #94a3b8; text-decoration: none; transition: color 0.2s; display: block; }
        .skill-list a:hover { color: #60a5fa; }
        .skill-list .desc { font-size: 0.8rem; color: #64748b; margin-top: 0.25rem; }
        .platforms { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
        .platform-tag { background: #334155; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.8rem; }
        footer { text-align: center; padding: 2rem; margin-top: 3rem; color: #64748b; border-top: 1px solid #334155; }
        footer a { color: #60a5fa; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI-SKILL 技能导航</h1>
            <p style="color: #94a3b8; font-size: 1.1rem;">''' + str(len(all_skills)) + '''+ 通用智能体技能库 | 支持 11 平台</p>
            <div class="stats">
                <div class="stat"><div class="stat-number">''' + str(len(by_category)) + '''</div><div class="stat-label">分类</div></div>
                <div class="stat"><div class="stat-number">''' + str(len(all_skills)) + '''+</div><div class="stat-label">技能</div></div>
                <div class="stat"><div class="stat-number">''' + str(len(by_platform)) + '''</div><div class="stat-label">平台</div></div>
            </div>
            <div class="platforms">
'''
    
    for platform in sorted(by_platform.keys()):
        html += f'<span class="platform-tag">{platform}</span>'
    
    html += '''
            </div>
        </header>
        
        <div class="search-box">
            <input type="text" id="search" placeholder="搜索技能..." onkeyup="filterSkills()">
        </div>
        
        <div class="categories" id="categories">
'''
    
    icons = {'ai': '🤖', 'development': '💻', 'tools': '🔧', 'product': '📦', 'business': '💼', 'devops': '🚀', 'docs': '📝', 'design': '🎨', 'knowledge': '📚', 'learning': '📖', 'finance': '💰', 'leadership': '👔', 'compliance': '✅', 'data': '📊'}
    
    for cat_name in sorted(by_category.keys()):
        icon = icons.get(cat_name, '📁')
        skills = by_category[cat_name][:15]
        html += f'''
            <div class="category-card" data-category="{cat_name}">
                <h2>{icon} {cat_name.title()} <span class="count">{len(by_category[cat_name])}</span></h2>
                <ul class="skill-list">
'''
        for skill in skills:
            html += f'<li><a href="#{skill["path"]}">{skill["name"]}</a><div class="desc">{skill.get("description", "")}</div></li>\n'
        if len(by_category[cat_name]) > 15:
            html += f'<li style="text-align:center;"><a href="#" style="color:#60a5fa;">查看全部 {len(by_category[cat_name])} 个技能 →</a></li>'
        html += '</ul></div>\n'
    
    html += '''
        </div>
        
        <footer>
            <p>AI-SKILL | 作者: <a href="https://github.com/badhope">badhope</a></p>
        </footer>
    </div>
    
    <script>
        function filterSkills() {
            const q = document.getElementById('search').value.toLowerCase();
            document.querySelectorAll('.category-card').forEach(c => {
                c.style.display = c.textContent.toLowerCase().includes(q) ? 'block' : 'none';
            });
        }
    </script>
</body>
</html>'''
    
    with open('skills/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✅ 索引构建完成!")
    print(f"   总技能数: {len(all_skills)}")
    print(f"   分类数: {len(by_category)}")
    print(f"   平台支持: {len(by_platform)}")
    print(f"   关键词索引: {len(by_keyword)}")
    print(f"\n📁 生成文件:")
    print(f"   - skills/all_skills.json")
    print(f"   - skills/by_category.json")
    print(f"   - skills/by_platform.json")
    print(f"   - skills/by_keyword.json")
    print(f"   - skills/index.html")

if __name__ == '__main__':
    main()

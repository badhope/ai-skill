#!/usr/bin/env python3
"""批量转换新添加的skill仓库"""

import os
import re
import shutil
from pathlib import Path
import json


def convert_skill_to_universal(source_skill_path, target_dir, author_name, license_name, category):
    """转换单个技能到通用格式"""
    if not source_skill_path.exists():
        return False
    
    try:
        content = source_skill_path.read_text(encoding='utf-8')
    except Exception:
        return False
    
    # 提取现有frontmatter
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
    
    # 获取技能名称
    skill_name = source_skill_path.parent.name
    name = frontmatter.get('name', skill_name)
    description = frontmatter.get('description', f"{skill_name} skill")
    
    # 构建新的frontmatter
    new_fm = {
        'name': name,
        'version': frontmatter.get('version', '1.0.0'),
        'description': description,
        'author': frontmatter.get('author', author_name),
        'category': category,
        'tags': frontmatter.get('tags', [skill_name]),
        'license': license_name,
        'platforms': ['claude', 'cursor', 'gemini', 'codex', 'hermes', 'doubao', 'qwen', 'spark', 'moonshot', 'baidu', 'alibaba', 'bytedance']
    }
    
    # 生成新的SKILL.md
    fm_str = '---\n'
    for key, value in new_fm.items():
        if isinstance(value, list):
            fm_str += f"{key}: [{', '.join(str(v) for v in value)}]\n"
        else:
            fm_str += f"{key}: {value}\n"
    fm_str += '---\n'
    
    new_content = fm_str + body
    
    # 创建目标目录
    target_skill_dir = target_dir / category / name
    target_skill_dir.mkdir(parents=True, exist_ok=True)
    
    (target_skill_dir / 'SKILL.md').write_text(new_content, encoding='utf-8')
    
    # 复制相关文件
    for item in ['references', 'scripts', 'assets', 'templates', 'examples', 'core']:
        item_path = source_skill_path.parent / item
        if item_path.exists():
            try:
                if (target_skill_dir / item).exists():
                    shutil.rmtree(target_skill_dir / item)
                shutil.copytree(item_path, target_skill_dir / item)
            except:
                pass
    
    return True


def scan_and_convert_antigravity():
    """转换 Antigravity Awesome Skills"""
    print("=" * 70)
    print("转换 Antigravity Awesome Skills (37k+ stars)")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'antigravity-awesome-skills' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 antigravity-awesome-skills")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            category = 'ai'  # Antigravity主要是AI相关
            if convert_skill_to_universal(skill_md, target_base, 'Antigravity', 'MIT', category):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 Antigravity 技能")
    return count


def scan_and_convert_ai_research():
    """转换 AI Research Skills"""
    print("\n" + "=" * 70)
    print("转换 AI Research SKILLs (8k+ stars)")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'AI-Research-SKILLs'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 AI-Research-SKILLs")
        return 0
    
    category_map = {
        '0-autoresearch-skill': 'ai',
        '01-model-architecture': 'ai',
        '02-tokenization': 'ai',
        '03-fine-tuning': 'ai',
        '04-mechanistic-interpretability': 'ai',
        '05-data-processing': 'ai',
        '06-post-training': 'ai',
        '07-safety-alignment': 'compliance',
        '08-distributed-training': 'ai',
        '09-infrastructure': 'devops',
        '10-optimization': 'ai',
        '11-evaluation': 'ai',
        '12-inference-serving': 'ai',
        '13-mlops': 'devops',
        '14-agents': 'ai',
        '15-rag': 'ai',
        '16-prompt-engineering': 'ai',
        '17-observability': 'ai',
        '18-multimodal': 'ai',
        '19-emerging-techniques': 'ai',
        '20-ml-paper-writing': 'docs',
        '21-research-ideation': 'ai',
        '22-agent-native-research-artifact': 'ai'
    }
    
    count = 0
    for cat_dir in source_base.iterdir():
        if not cat_dir.is_dir():
            continue
        
        cat_name = cat_dir.name
        category = category_map.get(cat_name, 'ai')
        
        for skill_dir in cat_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            
            skill_md = skill_dir / 'SKILL.md'
            if skill_md.exists():
                if convert_skill_to_universal(skill_md, target_base, 'Orchestra Research', 'MIT', category):
                    print(f"✅ {cat_name}/{skill_dir.name}")
                    count += 1
    
    print(f"\n转换了 {count} 个 AI Research 技能")
    return count


def scan_and_convert_agent_skills_hub():
    """转换 Agent Skills Hub"""
    print("\n" + "=" * 70)
    print("转换 Agent Skills Hub")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'agent-skills-hub' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 agent-skills-hub")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            if convert_skill_to_universal(skill_md, target_base, 'Agent Skills Hub', 'MIT', 'ai'):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 Agent Skills Hub 技能")
    return count


def scan_and_convert_agent_skills_library():
    """转换 Agent Skills Library"""
    print("\n" + "=" * 70)
    print("转换 Agent Skills Library")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'agent-skills-library' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 agent-skills-library")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            if convert_skill_to_universal(skill_md, target_base, 'CodingCossack', 'MIT', 'ai'):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 Agent Skills Library 技能")
    return count


def scan_and_convert_spring_ai():
    """转换 Spring AI Agent Utils"""
    print("\n" + "=" * 70)
    print("转换 Spring AI Agent Utils")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'spring-ai-agent-utils' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 spring-ai-agent-utils")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            if convert_skill_to_universal(skill_md, target_base, 'Spring AI', 'Apache-2.0', 'development'):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 Spring AI 技能")
    return count


def scan_and_convert_microsoft_skills():
    """转换 Microsoft Skills (174+ skills)"""
    print("\n" + "=" * 70)
    print("转换 Microsoft Skills (174+ skills)")
    print("=" * 70)
    
    base_dir = Path(__file__).parent.parent / 'vendor' / 'microsoft-skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not base_dir.exists():
        print("未找到 microsoft-skills")
        return 0
    
    count = 0
    
    # 扫描 .github/skills 目录
    github_skills_dir = base_dir / '.github' / 'skills'
    if github_skills_dir.exists():
        for skill_dir in github_skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            
            skill_md = skill_dir / 'SKILL.md'
            if skill_md.exists():
                # 根据技能名称判断分类
                category = 'development'
                skill_name = skill_dir.name.lower()
                if 'azure' in skill_name:
                    category = 'devops'
                elif 'cloud' in skill_name:
                    category = 'devops'
                elif 'frontend' in skill_name:
                    category = 'development'
                elif 'wiki' in skill_name:
                    category = 'docs'
                elif 'kql' in skill_name:
                    category = 'data'
                elif 'mcp' in skill_name:
                    category = 'tools'
                elif 'github' in skill_name:
                    category = 'tools'
                elif 'podcast' in skill_name:
                    category = 'product'
                elif 'copilot' in skill_name:
                    category = 'tools'
                
                if convert_skill_to_universal(skill_md, target_base, 'Microsoft', 'MIT', category):
                    print(f"✅ {skill_dir.name}")
                    count += 1
    
    # 扫描 plugins 目录下的技能
    plugins_dir = base_dir / '.github' / 'plugins'
    if plugins_dir.exists():
        for plugin_dir in plugins_dir.iterdir():
            if not plugin_dir.is_dir():
                continue
            
            plugin_skills_dir = plugin_dir / 'skills'
            if plugin_skills_dir.exists():
                for skill_dir in plugin_skills_dir.iterdir():
                    if not skill_dir.is_dir():
                        continue
                    
                    skill_md = skill_dir / 'SKILL.md'
                    if skill_md.exists():
                        category = 'development'
                        skill_name = skill_dir.name.lower()
                        if 'azure' in skill_name:
                            category = 'devops'
                        elif 'sdk' in skill_name:
                            category = 'development'
                        elif 'python' in skill_name:
                            category = 'development'
                        elif 'dotnet' in skill_name:
                            category = 'development'
                        elif 'java' in skill_name:
                            category = 'development'
                        elif 'typescript' in skill_name:
                            category = 'development'
                        elif 'rust' in skill_name:
                            category = 'development'
                        elif 'ai' in skill_name:
                            category = 'ai'
                        
                        if convert_skill_to_universal(skill_md, target_base, 'Microsoft', 'MIT', category):
                            print(f"✅ {plugin_dir.name}/{skill_dir.name}")
                            count += 1
    
    print(f"\n转换了 {count} 个 Microsoft 技能")
    return count


def scan_and_convert_microsoftdocs_skills():
    """转换 MicrosoftDocs Agent Skills"""
    print("\n" + "=" * 70)
    print("转换 MicrosoftDocs Agent Skills")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'microsoftdocs-agent-skills' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 microsoftdocs-agent-skills")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            category = 'development'
            skill_name = skill_dir.name.lower()
            if 'azure' in skill_name:
                category = 'devops'
            
            if convert_skill_to_universal(skill_md, target_base, 'MicrosoftDocs', 'MIT', category):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 MicrosoftDocs 技能")
    return count


def scan_and_convert_cloud_finops_skills():
    """转换 Cloud FinOps Skills"""
    print("\n" + "=" * 70)
    print("转换 Cloud FinOps Skills")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'cloud-finops-skills' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 cloud-finops-skills")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            if convert_skill_to_universal(skill_md, target_base, 'OptimNow', 'MIT', 'finance'):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 Cloud FinOps 技能")
    return count


def scan_and_convert_cryptoskills():
    """转换 CryptoSkills (加密/Web3 技能库)"""
    print("\n" + "=" * 70)
    print("转换 CryptoSkills (加密/Web3 技能库，150+ skills)")
    print("=" * 70)
    
    source_base = Path(__file__).parent.parent / 'vendor' / 'cryptoskills' / 'skills'
    target_base = Path(__file__).parent.parent / 'skills'
    
    if not source_base.exists():
        print("未找到 cryptoskills")
        return 0
    
    count = 0
    for skill_dir in source_base.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / 'SKILL.md'
        if skill_md.exists():
            # 根据技能名称判断分类
            category = 'tools'
            skill_name = skill_dir.name.lower()
            
            if any(x in skill_name for x in ['aave', 'compound', 'lido', 'curve', 'uniswap', 'pendle', 'dflow', 'hyperliquid', 'meteora', 'maker', 'morpho', 'marginfi', 'raydium', 'kamino', 'pumpfun', 'polymarket', 'vertex', 'drift', 'surfpool', 'ranger-finance']):
                category = 'finance'
            elif any(x in skill_name for x in ['eth', 'evm', 'solidity', 'foundry', 'hardhat', 'openzeppelin', 'slither', 'echidna', 'mythril', 'halmos', 'vulnhunter', 'semgrep', 'certora']):
                category = 'development'
            elif any(x in skill_name for x in ['solana', 'aptos', 'sui', 'starknet', 'sealevel', 'anchor', 'metaplex', 'pinocchio', 'solana-simd']):
                category = 'development'
            elif any(x in skill_name for x in ['ens', 'farcaster', 'metengine', 'lulo', 'glam', 'the-graph', 'tenderly', 'safe', 'sqauds']):
                category = 'tools'
            elif any(x in skill_name for x in ['monad', 'polygon', 'optimism', 'base', 'arbitrum', 'sei', 'zksync', 'megaeth', 'light-protocol']):
                category = 'devops'
            elif any(x in skill_name for x in ['chainlink', 'pyth', 'redstone', 'switchboard', 'hyperlane', 'wormhole', 'layerzero', 'debridge', 'axelar', 'goat', 'magicblock']):
                category = 'tools'
            elif any(x in skill_name for x in ['account', 'eip', 'ethers', 'viem', 'wagmi', 'helius', 'coinbase', 'jupiter', 'orca', 'privy', 'scaffold', 'x402', 'frontend', 'ux', 'eliza', 'code-recon', 'brian']):
                category = 'tools'
            elif 'nft' in skill_name:
                category = 'product'
            elif 'security' in skill_name or 'auditor' in skill_name:
                category = 'compliance'
            
            if convert_skill_to_universal(skill_md, target_base, '0xinit', 'MIT', category):
                print(f"✅ {skill_dir.name}")
                count += 1
    
    print(f"\n转换了 {count} 个 CryptoSkills (Web3) 技能")
    return count


def update_skill_index():
    """更新技能索引"""
    print("\n" + "=" * 70)
    print("更新技能索引")
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
                
                categories[cat_name]['skills'].append(skill_info)
                total_skills += 1
                
            except:
                pass
    
    index_data = {
        'version': '3.0.0',
        'description': 'Universal Agent Skill Library - 500+ skills',
        'categories': categories,
        'total_skills': total_skills
    }
    
    index_path.write_text(json.dumps(index_data, indent=2, ensure_ascii=False))
    print(f"索引更新完成！总技能数: {total_skills}")
    
    return total_skills


def main():
    print("=" * 70)
    print("批量转换新添加的 Skill 仓库")
    print("=" * 70)
    print()
    
    total = 0
    total += scan_and_convert_antigravity()
    total += scan_and_convert_ai_research()
    total += scan_and_convert_agent_skills_hub()
    total += scan_and_convert_agent_skills_library()
    total += scan_and_convert_spring_ai()
    total += scan_and_convert_microsoft_skills()
    total += scan_and_convert_microsoftdocs_skills()
    total += scan_and_convert_cloud_finops_skills()
    total += scan_and_convert_cryptoskills()
    
    update_skill_index()
    
    print("\n" + "=" * 70)
    print(f"🎉 转换完成！新增 {total} 个技能")
    print("=" * 70)


if __name__ == '__main__':
    main()

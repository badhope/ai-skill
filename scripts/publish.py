#!/usr/bin/env python3
"""
AI-SKILL 自动化发布工具
支持发布到多个平台：Claude Code、Cursor、Gemini CLI、豆包、通义千问等
"""

import os
import json
import shutil
from pathlib import Path
import argparse


class SkillPublisher:
    """技能发布器"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.skills_dir = self.base_dir / 'skills'
        self.output_dir = self.base_dir / 'dist'
        
    def publish_to_claude_code(self, output_path=None):
        """发布到 Claude Code 插件市场"""
        print("📦 发布到 Claude Code 插件市场...")
        
        target_dir = output_path or self.output_dir / 'claude-code'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # 复制 marketplace.json
        marketplace_src = self.base_dir / '.claude-plugin' / 'marketplace.json'
        if marketplace_src.exists():
            shutil.copy(marketplace_src, target_dir / 'marketplace.json')
            print("  ✅ 复制 marketplace.json")
        else:
            # 创建简化版
            marketplace = {
                "name": "AI-SKILL",
                "description": "2200+ universal agent skills curated from multiple sources by badhope",
                "version": "4.0.0",
                "platforms": ["claude-code", "claude-ai", "cursor", "gemini-cli", "doubao", "qwen"],
                "sources": [
                    "Anthropic Official Skills",
                    "Matt Pocock's Collection",
                    "Alireza Rezvani's Skills",
                    "Fullstack Skills",
                    "Antigravity Awesome Skills",
                    "AI Research Skills",
                    "Agent Skills Hub",
                    "Agent Skills Library"
                ]
            }
            (target_dir / 'marketplace.json').write_text(json.dumps(marketplace, indent=2))
            print("  ✅ 创建 marketplace.json")
        
        # 复制技能文件
        skills_target = target_dir / 'skills'
        skills_target.mkdir(exist_ok=True)
        
        for skill_md in self.skills_dir.glob('*/**/SKILL.md'):
            rel_path = skill_md.relative_to(self.skills_dir)
            target_file = skills_target / rel_path
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(skill_md, target_file)
        
        print(f"  ✅ 复制 {len(list(self.skills_dir.glob('*/**/SKILL.md')))} 个技能")
        print(f"  📁 输出目录: {target_dir}")
        return target_dir
    
    def publish_to_cursor(self, output_path=None):
        """发布到 Cursor 编辑器"""
        print("\n📦 发布到 Cursor...")
        
        target_dir = output_path or self.output_dir / 'cursor'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建 Cursor 规则格式
        rules = []
        
        for skill_md in self.skills_dir.glob('*/**/SKILL.md'):
            content = skill_md.read_text(encoding='utf-8')
            category = skill_md.parent.parent.name
            skill_name = skill_md.parent.name
            
            # 提取元数据
            import re
            fm_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            fm = {}
            if fm_match:
                for line in fm_match.group(1).split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        fm[key.strip()] = value.strip()
            
            rule = {
                "name": fm.get('name', skill_name),
                "description": fm.get('description', f"{skill_name} skill"),
                "category": category,
                "trigger": fm.get('tags', [skill_name]),
                "content": content,
                "version": fm.get('version', '1.0.0')
            }
            rules.append(rule)
        
        cursor_config = {
            "version": "1.0",
            "name": "AI-SKILL",
            "description": "2200+ universal agent skills for Cursor by badhope",
            "rules": rules
        }
        
        (target_dir / 'ai-skill-rules.json').write_text(
            json.dumps(cursor_config, indent=2, ensure_ascii=False)
        )
        print(f"  ✅ 生成 {len(rules)} 条规则")
        print(f"  📁 输出目录: {target_dir}")
        return target_dir
    
    def publish_to_gemini(self, output_path=None):
        """发布到 Gemini CLI"""
        print("\n📦 发布到 Gemini CLI...")
        
        target_dir = output_path or self.output_dir / 'gemini'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        skills = []
        
        for skill_md in self.skills_dir.glob('*/**/SKILL.md'):
            content = skill_md.read_text(encoding='utf-8')
            category = skill_md.parent.parent.name
            skill_name = skill_md.parent.name
            
            import re
            fm_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            fm = {}
            if fm_match:
                for line in fm_match.group(1).split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        fm[key.strip()] = value.strip()
            
            skill = {
                "id": f"ai-skill-{skill_name}",
                "name": fm.get('name', skill_name),
                "description": fm.get('description', ''),
                "category": category,
                "instructions": content,
                "version": fm.get('version', '1.0.0'),
                "author": fm.get('author', 'Community'),
                "license": fm.get('license', 'MIT')
            }
            skills.append(skill)
        
        gemini_config = {
            "version": "4.0.0",
            "author": "badhope",
            "name": "AI-SKILL",
            "skills": skills
        }
        
        (target_dir / 'skills.json').write_text(
            json.dumps(gemini_config, indent=2, ensure_ascii=False)
        )
        print(f"  ✅ 生成 {len(skills)} 个技能")
        print(f"  📁 输出目录: {target_dir}")
        return target_dir
    
    def publish_to_doubao(self, output_path=None):
        """发布到豆包平台"""
        print("\n📦 发布到豆包...")
        
        target_dir = output_path or self.output_dir / 'doubao'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        skills = []
        
        for skill_md in self.skills_dir.glob('*/**/SKILL.md'):
            content = skill_md.read_text(encoding='utf-8')
            category = skill_md.parent.parent.name
            skill_name = skill_md.parent.name
            
            import re
            fm_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            fm = {}
            if fm_match:
                for line in fm_match.group(1).split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        fm[key.strip()] = value.strip()
            
            skill = {
                "name": fm.get('name', skill_name),
                "description": fm.get('description', ''),
                "category": category,
                "content": content,
                "version": fm.get('version', '1.0.0'),
                "tags": fm.get('tags', [])
            }
            skills.append(skill)
        
        doubao_config = {
            "version": "1.0",
            "plugin_version": "4.0.0",
            "name": "AI-SKILL",
            "description": "2200+ 通用智能体技能库 by badhope",
            "provider": "badhope",
            "skills": skills
        }
        
        (target_dir / 'plugin.json').write_text(
            json.dumps(doubao_config, indent=2, ensure_ascii=False)
        )
        print(f"  ✅ 生成 {len(skills)} 个技能")
        print(f"  📁 输出目录: {target_dir}")
        return target_dir
    
    def publish_to_qwen(self, output_path=None):
        """发布到通义千问"""
        print("\n📦 发布到通义千问...")
        
        target_dir = output_path or self.output_dir / 'qwen'
        target_dir.mkdir(parents=True, exist_ok=True)
        
        skills = []
        
        for skill_md in self.skills_dir.glob('*/**/SKILL.md'):
            content = skill_md.read_text(encoding='utf-8')
            category = skill_md.parent.parent.name
            skill_name = skill_md.parent.name
            
            import re
            fm_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            fm = {}
            if fm_match:
                for line in fm_match.group(1).split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        fm[key.strip()] = value.strip()
            
            skill = {
                "skill_id": f"skill.{skill_name}",
                "skill_name": fm.get('name', skill_name),
                "description": fm.get('description', ''),
                "category": category,
                "content": content,
                "version": fm.get('version', '1.0.0'),
                "author": fm.get('author', 'Community')
            }
            skills.append(skill)
        
        qwen_config = {
            "version": "2.0",
            "name": "AI-SKILL",
            "description": "2200+ universal agent skills by badhope",
            "author": "badhope",
            "skills": skills
        }
        
        (target_dir / 'skills.json').write_text(
            json.dumps(qwen_config, indent=2, ensure_ascii=False)
        )
        print(f"  ✅ 生成 {len(skills)} 个技能")
        print(f"  📁 输出目录: {target_dir}")
        return target_dir
    
    def publish_all(self):
        """发布到所有平台"""
        print("=" * 70)
        print("AI-SKILL 自动化发布工具")
        print("=" * 70)
        print()
        
        self.publish_to_claude_code()
        self.publish_to_cursor()
        self.publish_to_gemini()
        self.publish_to_doubao()
        self.publish_to_qwen()
        
        print("\n" + "=" * 70)
        print("🎉 所有平台发布完成！")
        print(f"📁 输出目录: {self.output_dir}")
        print("=" * 70)
        
        return self.output_dir


def main():
    parser = argparse.ArgumentParser(description="AI-SKILL 自动化发布工具")
    parser.add_argument('--platform', '-p', choices=['all', 'claude', 'cursor', 'gemini', 'doubao', 'qwen'],
                        default='all', help='选择发布平台')
    parser.add_argument('--output', '-o', help='输出目录')
    
    args = parser.parse_args()
    
    publisher = SkillPublisher()
    
    if args.platform == 'all':
        publisher.publish_all()
    elif args.platform == 'claude':
        publisher.publish_to_claude_code(args.output)
    elif args.platform == 'cursor':
        publisher.publish_to_cursor(args.output)
    elif args.platform == 'gemini':
        publisher.publish_to_gemini(args.output)
    elif args.platform == 'doubao':
        publisher.publish_to_doubao(args.output)
    elif args.platform == 'qwen':
        publisher.publish_to_qwen(args.output)


if __name__ == '__main__':
    main()

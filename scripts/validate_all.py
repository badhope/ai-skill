#!/usr/bin/env python3
"""全面验证所有技能文件"""

import os
import re
from pathlib import Path


def validate_skill(skill_path):
    """验证单个技能文件"""
    errors = []
    warnings = []
    
    # 检查文件是否存在
    if not skill_path.exists():
        errors.append("文件不存在")
        return errors, warnings
    
    # 读取文件内容
    try:
        content = skill_path.read_text(encoding='utf-8')
    except Exception as e:
        errors.append(f"读取失败: {e}")
        return errors, warnings
    
    # 检查是否为空
    if not content.strip():
        errors.append("文件内容为空")
        return errors, warnings
    
    # 检查frontmatter（忽略开头空白）
    if not content.strip().startswith('---'):
        errors.append("缺少YAML frontmatter")
    else:
        # 检查frontmatter结构（允许开头有空白）
        match = re.search(r'^\s*---\n(.*?)\n---\n', content, re.DOTALL)
        if not match:
            errors.append("frontmatter格式错误")
        else:
            fm_content = match.group(1)
            fm_lines = fm_content.split('\n')
            
            required_fields = ['name', 'version', 'description', 'author', 'category']
            for field in required_fields:
                found = False
                for line in fm_lines:
                    if line.strip().startswith(f'{field}:'):
                        found = True
                        value = line.split(':', 1)[1].strip()
                        if not value or value in ['[]', '{}']:
                            warnings.append(f"{field}字段值为空")
                        break
                if not found:
                    errors.append(f"缺少必需字段: {field}")
            
            # 检查platforms字段
            has_platforms = False
            for line in fm_lines:
                if line.strip().startswith('platforms:'):
                    has_platforms = True
                    break
            if not has_platforms:
                warnings.append("缺少platforms字段")
    
    # 检查编码问题（乱码）
    if '\ufffd' in content:
        errors.append("文件包含乱码字符")
    
    # 检查内容长度
    if len(content) < 20:
        warnings.append("文件内容过短")
    
    return errors, warnings


def main():
    skills_dir = Path(__file__).parent.parent / 'skills'
    
    total_files = 0
    passed = 0
    failed = 0
    total_warnings = 0
    error_list = []
    
    print("=" * 70)
    print("全面验证所有技能文件")
    print("=" * 70)
    print()
    
    for skill_md in skills_dir.glob('*/**/SKILL.md'):
        total_files += 1
        errors, warnings = validate_skill(skill_md)
        
        if errors:
            failed += 1
            error_list.append(f"❌ {skill_md}")
            for e in errors:
                error_list.append(f"   - {e}")
            for w in warnings:
                total_warnings += 1
        else:
            passed += 1
            if warnings:
                total_warnings += len(warnings)
    
    print("=" * 70)
    print("验证结果汇总")
    print("=" * 70)
    print(f"总文件数: {total_files}")
    print(f"✅ 通过: {passed}")
    print(f"❌ 失败: {failed}")
    print(f"⚠️ 警告: {total_warnings}")
    print()
    
    if error_list:
        print("失败的文件列表:")
        for item in error_list:
            print(item)
    else:
        print("🎉 所有技能文件验证通过！")


if __name__ == '__main__':
    main()

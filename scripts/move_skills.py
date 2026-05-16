#!/usr/bin/env python3
"""Move skills from root to skills directory"""

import shutil
from pathlib import Path


def main():
    base_dir = Path(__file__).parent.parent
    skills_dir = base_dir / 'skills'
    
    for cat_dir in ['ai', 'business', 'design', 'development', 'docs', 'tools']:
        src_dir = base_dir / cat_dir
        if not src_dir.exists() or not src_dir.is_dir():
            continue
        
        target_dir = skills_dir / cat_dir
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for skill_dir in src_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            
            dest_dir = target_dir / skill_dir.name
            
            if dest_dir.exists():
                print(f"Removing existing: {dest_dir}")
                shutil.rmtree(dest_dir)
            
            print(f"Moving: {skill_dir} -> {dest_dir}")
            shutil.move(str(skill_dir), str(dest_dir))
        
        if not any(src_dir.iterdir()):
            src_dir.rmdir()
    
    print("Done!")


if __name__ == '__main__':
    main()

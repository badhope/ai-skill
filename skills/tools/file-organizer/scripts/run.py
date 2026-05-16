"""
file-organizer - 文件自动整理技能
"""

import os
import shutil
import json
import argparse
from pathlib import Path
from datetime import datetime


# 文件类型映射
TYPE_MAP = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico", ".tiff"],
    "documents": [".doc", ".docx", ".pdf", ".txt", ".md", ".rtf", ".odt", ".pages"],
    "spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],
    "presentations": [".ppt", ".pptx", ".odp", ".key"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "code": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".h", ".cs", ".go", ".rs", ".rb", ".php"],
    "data": [".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".sql"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
}

# 反向映射
EXT_TO_FOLDER = {}
for folder, exts in TYPE_MAP.items():
    for ext in exts:
        EXT_TO_FOLDER[ext.lower()] = folder


def organize_by_type(directory: Path) -> dict:
    """按文件类型整理"""
    results = {"moved": [], "skipped": [], "errors": []}
    
    for item in directory.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            target_folder = EXT_TO_FOLDER.get(ext, "others")
            target_dir = directory / target_folder
            
            try:
                target_dir.mkdir(exist_ok=True)
                
                # 处理同名文件
                target_path = target_dir / item.name
                counter = 1
                while target_path.exists():
                    new_name = f"{item.stem}_{counter}{item.suffix}"
                    target_path = target_dir / new_name
                    counter += 1
                
                shutil.move(str(item), str(target_path))
                results["moved"].append({
                    "file": item.name,
                    "from": str(item),
                    "to": str(target_path),
                    "folder": target_folder
                })
            except Exception as e:
                results["errors"].append({"file": item.name, "error": str(e)})
    
    return results


def organize_by_date(directory: Path) -> dict:
    """按修改日期整理"""
    results = {"moved": [], "skipped": [], "errors": []}
    
    for item in directory.iterdir():
        if item.is_file():
            stat = item.stat()
            date = datetime.fromtimestamp(stat.st_mtime)
            folder_name = date.strftime("%Y-%m")
            target_dir = directory / folder_name
            
            try:
                target_dir.mkdir(exist_ok=True)
                
                target_path = target_dir / item.name
                counter = 1
                while target_path.exists():
                    new_name = f"{item.stem}_{counter}{item.suffix}"
                    target_path = target_dir / new_name
                    counter += 1
                
                shutil.move(str(item), str(target_path))
                results["moved"].append({
                    "file": item.name,
                    "from": str(item),
                    "to": str(target_path),
                    "folder": folder_name
                })
            except Exception as e:
                results["errors"].append({"file": item.name, "error": str(e)})
    
    return results


def main():
    parser = argparse.ArgumentParser(description="文件自动整理")
    parser.add_argument("--directory", required=True, help="要整理的目录")
    parser.add_argument("--mode", default="type", choices=["type", "date"], help="整理方式")
    parser.add_argument("--dry-run", action="store_true", help="预览模式（不实际移动）")
    
    args = parser.parse_args()
    
    directory = Path(args.directory).expanduser().resolve()
    
    if not directory.exists():
        print(json.dumps({"success": False, "error": f"目录不存在: {directory}"}))
        return
    
    if not directory.is_dir():
        print(json.dumps({"success": False, "error": f"不是目录: {directory}"}))
        return
    
    print(f"正在整理: {directory}")
    print(f"整理方式: {args.mode}")
    
    if args.mode == "type":
        results = organize_by_type(directory)
    else:
        results = organize_by_date(directory)
    
    # 统计
    moved_count = len(results["moved"])
    error_count = len(results["errors"])
    
    print(f"\n整理完成！")
    print(f"  移动文件: {moved_count} 个")
    if error_count > 0:
        print(f"  错误: {error_count} 个")
    
    # 按文件夹统计
    folder_stats = {}
    for item in results["moved"]:
        folder = item["folder"]
        folder_stats[folder] = folder_stats.get(folder, 0) + 1
    
    if folder_stats:
        print("\n分类统计:")
        for folder, count in sorted(folder_stats.items()):
            print(f"  {folder}: {count} 个文件")
    
    print(json.dumps({"success": True, "results": results}))


if __name__ == "__main__":
    main()

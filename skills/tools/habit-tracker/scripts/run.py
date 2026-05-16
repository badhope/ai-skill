"""
habit-tracker - 习惯追踪技能
"""

import argparse
import json
import os
from pathlib import Path
from datetime import datetime, date


DATA_DIR = Path.home() / ".woclaw" / "habits"
DATA_FILE = DATA_DIR / "habits.json"


def load_data():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"habits": {}, "records": {}}


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_habit(name, description="", frequency="daily"):
    data = load_data()
    habit_id = name.lower().replace(' ', '-')
    data["habits"][habit_id] = {
        "name": name,
        "description": description,
        "frequency": frequency,
        "created": date.today().isoformat(),
        "streak": 0
    }
    save_data(data)
    print(f"✅ 习惯已添加: {name}")
    return {"success": True, "habit_id": habit_id}


def checkin(habit_id):
    data = load_data()
    today = date.today().isoformat()
    
    if habit_id not in data["habits"]:
        print(f"❌ 习惯不存在: {habit_id}")
        return {"success": False, "error": "习惯不存在"}
    
    if today not in data["records"]:
        data["records"][today] = []
    
    if habit_id in data["records"][today]:
        print(f"ℹ️  今天已经打卡了: {data['habits'][habit_id]['name']}")
        return {"success": True, "already_done": True}
    
    data["records"][today].append(habit_id)
    
    # 计算连续天数
    streak = calculate_streak(data, habit_id)
    data["habits"][habit_id]["streak"] = streak
    
    save_data(data)
    
    habit_name = data["habits"][habit_id]["name"]
    print(f"✅ 打卡成功: {habit_name}")
    print(f"🔥 连续 {streak} 天！")
    
    return {"success": True, "streak": streak}


def calculate_streak(data, habit_id):
    streak = 0
    check_date = date.today()
    
    while True:
        date_str = check_date.isoformat()
        if date_str in data["records"] and habit_id in data["records"][date_str]:
            streak += 1
            check_date = date(check_date.year, check_date.month, check_date.day - 1)
        else:
            break
    
    return streak


def list_habits():
    data = load_data()
    today = date.today().isoformat()
    
    if not data["habits"]:
        print("暂无习惯，使用 --add 添加")
        return
    
    print("\n📋 我的习惯列表:")
    print("-" * 50)
    
    for habit_id, habit in data["habits"].items():
        done_today = today in data["records"] and habit_id in data["records"][today]
        status = "✅" if done_today else "⬜"
        streak = habit.get("streak", 0)
        
        print(f"{status} {habit['name']}")
        if habit.get("description"):
            print(f"   {habit['description']}")
        print(f"   🔥 连续 {streak} 天 | 频率: {habit['frequency']}")
        print()


def stats():
    data = load_data()
    today = date.today().isoformat()
    
    total_habits = len(data["habits"])
    done_today = len(data["records"].get(today, []))
    
    print(f"\n📊 今日统计:")
    print(f"  总习惯数: {total_habits}")
    print(f"  今日完成: {done_today}/{total_habits}")
    
    if total_habits > 0:
        completion_rate = done_today / total_habits * 100
        print(f"  完成率: {completion_rate:.0f}%")
    
    # 最长连续
    max_streak = max((h.get("streak", 0) for h in data["habits"].values()), default=0)
    print(f"  最长连续: {max_streak} 天")


def main():
    parser = argparse.ArgumentParser(description="习惯追踪")
    parser.add_argument("--add", help="添加习惯")
    parser.add_argument("--checkin", help="打卡")
    parser.add_argument("--list", action="store_true", help="列出所有习惯")
    parser.add_argument("--stats", action="store_true", help="查看统计")
    parser.add_argument("--description", default="", help="习惯描述")
    
    args = parser.parse_args()
    
    if args.add:
        result = add_habit(args.add, args.description)
        print(json.dumps(result))
    elif args.checkin:
        result = checkin(args.checkin)
        print(json.dumps(result))
    elif args.list:
        list_habits()
    elif args.stats:
        stats()
    else:
        # 默认显示今日状态
        list_habits()
        stats()


if __name__ == "__main__":
    main()

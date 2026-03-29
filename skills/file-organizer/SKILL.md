# file-organizer - 文件自动整理

## 基本信息
- **名称**: file-organizer
- **版本**: 1.0.0
- **分类**: 文件处理
- **描述**: 自动将文件夹中的文件按类型或日期分类整理

## 使用方法

```bash
# 按类型整理（默认）
woclaw skill run file-organizer --directory ~/Downloads

# 按日期整理
woclaw skill run file-organizer --directory ~/Downloads --mode date
```

## 参数说明

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| --directory | string | 要整理的目录路径 | 必填 |
| --mode | string | 整理方式: type/date | type |

## 整理规则

### 按类型（type）
```
Downloads/
├── images/     # .jpg .png .gif .webp .svg
├── documents/  # .doc .docx .pdf .txt .md
├── videos/     # .mp4 .avi .mkv .mov
├── audio/      # .mp3 .wav .flac .aac
├── archives/   # .zip .rar .7z .tar
├── code/       # .py .js .ts .java .cpp
└── others/     # 其他文件
```

### 按日期（date）
```
Downloads/
├── 2026-03/
├── 2026-02/
└── 2026-01/
```

## 示例

```
你：帮我整理下载文件夹
星灵：好的！正在整理...

✅ 扫描完成（找到 47 个文件）
✅ 创建分类文件夹
✅ 移动文件：
   - 12 张图片 → images/
   - 8 个文档 → documents/
   - 5 个视频 → videos/
   - 22 个其他 → others/
✨ 整理完成！
```

## 注意事项

- 不会删除任何文件，只是移动
- 如果目标文件夹已有同名文件，会自动重命名
- 支持撤销操作（保留操作日志）

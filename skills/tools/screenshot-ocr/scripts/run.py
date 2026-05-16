"""
screenshot-ocr - 截图文字识别
"""

import argparse
import json
import sys
from pathlib import Path


def take_screenshot(region=None):
    """截图"""
    try:
        import pyscreeze
        if region:
            img = pyscreeze.screenshot(region=region)
        else:
            img = pyscreeze.screenshot()
        return img
    except ImportError:
        print("请安装 pyscreeze: pip install pyscreeze")
        sys.exit(1)


def ocr_image(image_path=None, image=None):
    """OCR 识别"""
    try:
        import pytesseract
        from PIL import Image
        
        if image_path:
            img = Image.open(image_path)
        elif image:
            img = image
        else:
            return ""
        
        # 中英文识别
        text = pytesseract.image_to_string(img, lang='chi_sim+eng')
        return text.strip()
    except ImportError:
        # 尝试使用 Windows OCR
        return ocr_windows(image_path or image)


def ocr_windows(image):
    """使用 Windows 内置 OCR"""
    try:
        import subprocess
        import tempfile
        import os
        
        # 保存临时文件
        if hasattr(image, 'save'):
            tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
            image.save(tmp.name)
            image_path = tmp.name
        else:
            image_path = str(image)
        
        # 使用 PowerShell Windows OCR
        ps_script = f"""
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]
$null = [Windows.Foundation.IAsyncOperation`1, Windows.Foundation, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Foundation, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.RandomAccessStream, Windows.Storage, ContentType = WindowsRuntime]

function Await($WinRtTask, $ResultType) {{
    $asTask = [System.WindowsRuntimeSystemExtensions]::AsTask($WinRtTask)
    $asTask.Wait(-1) | Out-Null
    $asTask.Result
}}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync('{image_path}')) ([Windows.Storage.StorageFile])
$stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
$decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
$bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
$result.Text
"""
        result = subprocess.run(
            ['powershell', '-Command', ps_script],
            capture_output=True, text=True, timeout=30
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        return ""
    except Exception as e:
        return f"OCR 失败: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description="截图文字识别")
    parser.add_argument("--image", help="图片路径（不指定则截取全屏）")
    parser.add_argument("--region", help="截图区域 x,y,w,h")
    parser.add_argument("--save", help="保存截图到路径")
    
    args = parser.parse_args()
    
    if args.image:
        # 识别指定图片
        image_path = Path(args.image)
        if not image_path.exists():
            print(json.dumps({"success": False, "error": f"图片不存在: {args.image}"}))
            return
        
        text = ocr_image(image_path=str(image_path))
    else:
        # 截图并识别
        region = None
        if args.region:
            parts = [int(x) for x in args.region.split(',')]
            region = tuple(parts[:4])
        
        print("正在截图...")
        img = take_screenshot(region=region)
        
        if args.save:
            img.save(args.save)
            print(f"截图已保存: {args.save}")
        
        print("正在识别文字...")
        text = ocr_image(image=img)
    
    if text:
        print("\n识别结果:")
        print("-" * 40)
        print(text)
        print("-" * 40)
        print(json.dumps({"success": True, "text": text}))
    else:
        print("未识别到文字")
        print(json.dumps({"success": True, "text": ""}))


if __name__ == "__main__":
    main()

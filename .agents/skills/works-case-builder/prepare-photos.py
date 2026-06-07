"""
prepare-photos.py

スマホで撮ったランダムな写真を、施工事例ページ用に前処理するスクリプト。

【処理内容】
1. raw/ フォルダ内の全画像（JPEG/HEIC/PNG/WebP）を読み込み
2. EXIFの撮影日時で時系列ソート（EXIF無ければファイル更新日時）
3. WebP変換、800px幅にリサイズ、品質85で統一
4. 親ディレクトリに photo-001.webp, photo-002.webp ... の連番で出力
5. raw/ の元ファイルはそのまま残す（バックアップ）

【使い方】
python prepare-photos.py images/works/{area}/{NNN}/raw/

【依存】
- Pillow（必須）
- pillow-heif（HEICを処理するため。無くてもJPEG/PNG/WebPは動く）
  インストール: pip install pillow-heif
"""

import sys
import os
from pathlib import Path
from PIL import Image, ExifTags
from datetime import datetime

# HEIC対応（任意）
HEIC_SUPPORTED = False
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIC_SUPPORTED = True
except ImportError:
    pass

SUPPORTED_EXT = {".jpg", ".jpeg", ".png", ".webp"}
if HEIC_SUPPORTED:
    SUPPORTED_EXT |= {".heic", ".heif"}

MAX_WIDTH = 800
QUALITY = 85


def get_capture_time(filepath: Path) -> datetime:
    """EXIFから撮影日時を取得。無ければファイル更新日時を返す。"""
    try:
        img = Image.open(filepath)
        exif = img.getexif()
        if exif:
            # EXIF tag 36867 = DateTimeOriginal
            for tag_id, value in exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass
    return datetime.fromtimestamp(filepath.stat().st_mtime)


def process_image(src: Path, dst: Path):
    """1枚を読み込み、800pxにリサイズ、WebPで保存。"""
    img = Image.open(src)

    # EXIFの向き情報を反映
    try:
        img = Image.open(src)
        exif = img.getexif()
        orientation = exif.get(274) if exif else None  # 274 = Orientation
        if orientation == 3:
            img = img.rotate(180, expand=True)
        elif orientation == 6:
            img = img.rotate(270, expand=True)
        elif orientation == 8:
            img = img.rotate(90, expand=True)
    except Exception:
        pass

    # リサイズ
    w, h = img.size
    if w > MAX_WIDTH:
        ratio = MAX_WIDTH / w
        new_size = (MAX_WIDTH, int(h * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    # RGB変換（PNGのアルファチャンネル等を統一）
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    # WebP保存
    img.save(dst, "WEBP", quality=QUALITY, method=6)


def main():
    if len(sys.argv) < 2:
        print("Usage: python prepare-photos.py <raw_folder>")
        print("Example: python prepare-photos.py images/works/abashiri/003/raw/")
        sys.exit(1)

    raw_dir = Path(sys.argv[1])
    if not raw_dir.exists() or not raw_dir.is_dir():
        print(f"ERROR: Folder not found: {raw_dir}")
        sys.exit(1)

    out_dir = raw_dir.parent
    print(f"Input:  {raw_dir}")
    print(f"Output: {out_dir}/photo-NNN.webp")
    print(f"HEIC support: {'YES' if HEIC_SUPPORTED else 'NO (pip install pillow-heif で有効化)'}")
    print()

    # 全対象ファイルを収集
    files = [
        f for f in raw_dir.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXT
    ]

    if not files:
        print(f"ERROR: No images found in {raw_dir}")
        print(f"Supported extensions: {SUPPORTED_EXT}")
        sys.exit(1)

    # 撮影日時でソート
    print(f"Reading EXIF from {len(files)} files...")
    files_with_time = [(f, get_capture_time(f)) for f in files]
    files_with_time.sort(key=lambda x: x[1])

    # 変換
    print(f"\nConverting {len(files_with_time)} files to WebP (800px, q{QUALITY})...\n")
    total_before = 0
    total_after = 0
    for i, (src, capture_time) in enumerate(files_with_time, start=1):
        dst = out_dir / f"photo-{i:03d}.webp"
        before = src.stat().st_size
        total_before += before
        try:
            process_image(src, dst)
            after = dst.stat().st_size
            total_after += after
            print(
                f"  [{i:03d}] {src.name:40s} "
                f"({before // 1024:5d}KB) -> photo-{i:03d}.webp ({after // 1024:5d}KB) "
                f"[{capture_time.strftime('%Y-%m-%d %H:%M:%S')}]"
            )
        except Exception as e:
            print(f"  [{i:03d}] SKIP {src.name}: {e}")

    print(f"\n=== Summary ===")
    print(f"Files: {len(files_with_time)}")
    print(f"Total size: {total_before // 1024}KB -> {total_after // 1024}KB ({100 * total_after // total_before}%)")
    print(f"\nNext step: Claude reads photo-001.webp ... photo-NNN.webp and classifies them.")


if __name__ == "__main__":
    main()

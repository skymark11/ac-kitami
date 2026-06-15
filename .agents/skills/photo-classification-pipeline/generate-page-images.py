"""
ページ用画像生成スクリプト（汎用版）
案件フォルダの IMG_*.jpg を、セマンティックな名前でリサイズ＋WebP化する。

使い方:
1. 案件フォルダの _classification/ に mapping.json を用意する:

    {
        "IMG_9124.jpg": "hero-before",
        "IMG_9128.jpg": "hero-after",
        "IMG_9089.jpg": "ba-before",
        ...
    }

2. このスクリプトを実行:
    python generate-page-images.py <案件フォルダのパス>

出力: 案件フォルダ配下に semantic-name.webp / .jpg を生成
"""

import json
import sys
from pathlib import Path
from PIL import Image

MAX_WIDTH = 800
WEBP_QUALITY = 80
JPG_QUALITY = 85


def main(case_root: Path) -> None:
    mapping_path = case_root / "_classification" / "mapping.json"
    if not mapping_path.exists():
        sys.exit(
            f"ERROR: {mapping_path} not found.\n"
            "_classification/mapping.json に IMG_XXXX.jpg → semantic-name のマッピングを書いてください。"
        )

    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    print(f"=== {len(mapping)} 枚を変換 ===\n")

    for src_name, target in mapping.items():
        src = case_root / src_name
        if not src.exists():
            print(f"  SKIP: {src_name} not found")
            continue

        img = Image.open(src)
        if img.mode != "RGB":
            img = img.convert("RGB")

        w, h = img.size
        if w > MAX_WIDTH:
            new_w = MAX_WIDTH
            new_h = int(h * MAX_WIDTH / w)
            img = img.resize((new_w, new_h), Image.LANCZOS)

        webp_path = case_root / f"{target}.webp"
        jpg_path = case_root / f"{target}.jpg"
        img.save(webp_path, "WEBP", quality=WEBP_QUALITY)
        img.save(jpg_path, "JPEG", quality=JPG_QUALITY, optimize=True)

        wp_kb = webp_path.stat().st_size // 1024
        jp_kb = jpg_path.stat().st_size // 1024
        print(f"  {src_name} -> {target}  size={img.size}  webp={wp_kb}KB  jpg={jp_kb}KB")

    print("\n=== 完了 ===")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python generate-page-images.py <案件フォルダのパス>")
    main(Path(sys.argv[1]).resolve())

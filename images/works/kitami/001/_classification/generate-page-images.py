"""
kitami-001 ページ用画像生成スクリプト
分類結果に基づく14枚の元画像（IMG_*.jpg）を、セマンティックな名前でリサイズ＋WebP化する。
出力先: images/works/kitami/001/ (同フォルダ)
"""

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent.parent  # images/works/kitami/001/

# 元画像 → 新ファイル名 (拡張子なし)
MAPPING = {
    "IMG_9124.jpg": "hero-before",          # 室内・施工前（カーテン側）
    "IMG_9128.jpg": "hero-after",           # 同じ場所・室内機完成
    "IMG_9089.jpg": "ba-before",            # 室外・施工前（壁面のみ）
    "IMG_9166.jpg": "ba-after",             # 室外・屋根付き架台完成
    "IMG_9113.jpg": "process-1-floor",      # 床下確認
    "IMG_9133.jpg": "process-2-panel",      # 既設の主幹ブレーカー確認（補正後・銘板接写）
    "IMG_9121.jpg": "process-3-wall",       # 室内壁・配線引込み
    "IMG_9127.jpg": "process-4-pipe",       # 外壁・配管引き出し
    "IMG_9129.jpg": "done-1-indoor-unit",   # 室内機（別アングル）
    "IMG_9119.jpg": "done-2-panel-circuit", # 分電盤・専用回路完成（補正後・カバー外して見せる）
    "IMG_9169.jpg": "done-3-outlet",        # 専用コンセント接写
    "IMG_9168.jpg": "done-4-cover",         # 化粧カバー（スリムダクト）
    "IMG_9399.jpg": "done-5-outdoor-unit",  # 室外機正面
    "IMG_9401.jpg": "done-6-roof-bracket",  # 屋根板接写
}

MAX_WIDTH = 800
WEBP_QUALITY = 80
JPG_QUALITY = 85


def main():
    print(f"=== {len(MAPPING)} 枚を変換 ===\n")
    for src_name, target in MAPPING.items():
        src = ROOT / src_name
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

        webp_path = ROOT / f"{target}.webp"
        jpg_path = ROOT / f"{target}.jpg"
        img.save(webp_path, "WEBP", quality=WEBP_QUALITY)
        img.save(jpg_path, "JPEG", quality=JPG_QUALITY, optimize=True)

        wp_kb = webp_path.stat().st_size // 1024
        jp_kb = jpg_path.stat().st_size // 1024
        print(f"  {src_name} -> {target}  size={img.size}  webp={wp_kb}KB  jpg={jp_kb}KB")

    print("\n=== 完了 ===")


if __name__ == "__main__":
    main()

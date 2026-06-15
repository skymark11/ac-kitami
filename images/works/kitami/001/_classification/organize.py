"""
kitami-001 写真分類フォルダ生成スクリプト
classification.json を読み込み、images/works/kitami/001/_classification/by_category/ 配下に
ユーザー確認用のフォルダ構造を生成（コピーベース、Dropbox安全）。
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent  # images/works/kitami/001/
CLASS_JSON = ROOT / "_classification" / "classification.json"
OUT_DIR = ROOT / "_classification" / "by_category"

CATEGORIES = {
    "01_施工前": lambda p: p["stage"] == "施工前" and p["best_use"] != "除外",
    "02_工程中": lambda p: p["stage"] == "工程中" and p["best_use"] != "除外",
    "03_施工後_室内機": lambda p: p["stage"] == "施工後" and p["primary_subject"] == "室内機",
    "03_施工後_室外機": lambda p: p["stage"] == "施工後" and p["primary_subject"] == "室外機",
    "03_施工後_分電盤コンセント": lambda p: p["stage"] == "施工後" and p["primary_subject"] in ("分電盤", "コンセント"),
    "03_施工後_化粧カバー": lambda p: p["stage"] == "施工後" and p["primary_subject"] == "化粧カバー",
    "03_施工後_据置金具屋根付き": lambda p: p["stage"] == "施工後" and p["primary_subject"] in ("据置金具", "屋根付き架台"),
    "04_詳細接写": lambda p: p["composition"] in ("接写", "手元") and p["best_use"] == "detail",
    "99_除外_書類個人情報": lambda p: p["best_use"] == "除外" and p["personal_info"],
    "99_除外_関係薄い": lambda p: p["best_use"] == "除外" and not p["personal_info"],
}


def main():
    data = json.loads(CLASS_JSON.read_text(encoding="utf-8"))

    # 既存出力を削除して再生成
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    for cat_name in CATEGORIES:
        (OUT_DIR / cat_name).mkdir()

    placed = {p["filename"]: [] for p in data["photos"]}

    for photo in data["photos"]:
        src = ROOT / photo["filename"]
        if not src.exists():
            print(f"  WARNING: {photo['filename']} not found in {ROOT}")
            continue

        matched = False
        for cat_name, predicate in CATEGORIES.items():
            if predicate(photo):
                dst = OUT_DIR / cat_name / photo["filename"]
                shutil.copy2(src, dst)
                placed[photo["filename"]].append(cat_name)
                matched = True

        if not matched:
            # 未分類 → _未分類フォルダへ
            unsorted_dir = OUT_DIR / "00_未分類"
            unsorted_dir.mkdir(exist_ok=True)
            shutil.copy2(src, unsorted_dir / photo["filename"])
            placed[photo["filename"]].append("00_未分類")

    # 報告
    print(f"\n=== 振り分け完了 (出力先: {OUT_DIR}) ===")
    for cat in sorted(OUT_DIR.iterdir()):
        if cat.is_dir():
            files = sorted(cat.iterdir())
            print(f"\n[{cat.name}]  {len(files)}枚")
            for f in files:
                print(f"    {f.name}")

    # 各写真がどこに行ったか
    print("\n=== 各写真の配置先 ===")
    for fn, cats in sorted(placed.items()):
        cats_str = " / ".join(cats) if cats else "(未配置)"
        print(f"  {fn}  →  {cats_str}")


if __name__ == "__main__":
    main()

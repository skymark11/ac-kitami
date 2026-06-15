"""
写真分類フォルダ生成スクリプト（汎用版）
classification.json を読み込み、_classification/by_category/ 配下に
ユーザー確認用のフォルダ構造を生成（コピーベース、Dropbox安全）。

使い方:
    python organize.py <案件フォルダのパス>

例:
    python .agents/skills/photo-classification-pipeline/organize.py images/works/kitami/001
"""

import json
import shutil
import sys
from pathlib import Path


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


def main(case_root: Path) -> None:
    class_dir = case_root / "_classification"
    class_json = class_dir / "classification.json"
    out_dir = class_dir / "by_category"

    if not class_json.exists():
        sys.exit(f"ERROR: {class_json} not found. classification.json を先に作成してください。")

    data = json.loads(class_json.read_text(encoding="utf-8"))

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    for cat_name in CATEGORIES:
        (out_dir / cat_name).mkdir()

    placed = {p["filename"]: [] for p in data["photos"]}

    for photo in data["photos"]:
        src = case_root / photo["filename"]
        if not src.exists():
            print(f"  WARNING: {photo['filename']} not found in {case_root}")
            continue

        matched = False
        for cat_name, predicate in CATEGORIES.items():
            if predicate(photo):
                dst = out_dir / cat_name / photo["filename"]
                shutil.copy2(src, dst)
                placed[photo["filename"]].append(cat_name)
                matched = True

        if not matched:
            unsorted_dir = out_dir / "00_未分類"
            unsorted_dir.mkdir(exist_ok=True)
            shutil.copy2(src, unsorted_dir / photo["filename"])
            placed[photo["filename"]].append("00_未分類")

    print(f"\n=== 振り分け完了 (出力先: {out_dir}) ===")
    for cat in sorted(out_dir.iterdir()):
        if cat.is_dir():
            files = sorted(cat.iterdir())
            print(f"\n[{cat.name}]  {len(files)}枚")
            for f in files:
                print(f"    {f.name}")

    print("\n=== 各写真の配置先 ===")
    for fn, cats in sorted(placed.items()):
        cats_str = " / ".join(cats) if cats else "(未配置)"
        print(f"  {fn}  ->  {cats_str}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python organize.py <案件フォルダのパス>")
    main(Path(sys.argv[1]).resolve())

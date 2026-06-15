---
name: photo-classification-pipeline
description: 施工写真フォルダの中身（IMG_*.jpg など未分類のスマホ写真群）をAIで視覚分類し、用途別フォルダに振り分け、ページ用にWebP化までを行うパイプライン。誤分類リスクを前提に「Claude自身による再確認フェーズ」を必須プロセスとして組み込む。
metadata:
  type: pipeline
  scope: ac-kitami.com
  related_skills: [works-case-builder, image-to-webp]
---

# 写真分類パイプライン

## このスキルの狙い

施工写真は**スマホで撮ったままドサッと入れる**のが現場のリアル。ユーザーが1枚ずつ「これは室内機」「これは分電盤」と振り分けるのは現実的でない。
このスキルでは、**「中身を見て分類する」**ステップを正面から組み込み、ページに正しいキャプションを付けられる状態まで持っていく。

**過去の失敗例:**
- 写真名 (before-01.jpg) だけ見て中身を確認せず「採寸・墨出し」と勝手なキャプションを付けた
- 結果、実物と全然違う説明文がページに載った
- ユーザーが目視で発見して指摘 → 大量の修正

このスキルはこの失敗パターンを根絶することを目的とする。

---

## 全体フロー（5フェーズ）

```
ユーザー作業              Claude作業（写真を実際に「見る」）         ユーザー確認
───────────             ─────────────────────────             ──────────
Phase 1: 投入  →  Phase 2: AI分類  →  Phase 3: 振り分け  →  Phase 4: ベスト写真選定 + 再確認  →  Phase 5: ページ反映
```

---

## Phase 1: 投入（ユーザーの作業）

```
images/works/{area}/{NNN}/
  ├─ IMG_9089.jpg  ← スマホから一括コピー
  ├─ IMG_9090.jpg
  ├─ ...
  └─ {地域}-{場所}-aircon-review-{NNN}.jpg  ← アンケート用紙（任意）
```

または `_inbox/{area}/{案件}/raw/` 配下に投入してもOK。
リネーム不要・HEIC OK・順番ランダムでOK。

---

## Phase 2: AI分類（Claude → サブエージェント派遣）

メイン会話のコンテキストを節約するため、**general-purpose サブエージェント**を派遣して全画像を Read tool で視覚解析させる。

### サブエージェントへの依頼テンプレート

詳細は `classify-photos-prompt-template.md` を参照。要点:

- 1枚ずつ Read tool で実画像を見る（推測禁止）
- 5〜10枚ずつ並列発行で効率化
- 各画像について以下を判定:

```json
{
  "filename": "IMG_XXXX.jpg",
  "primary_subject": "室外機 / 室内機 / 分電盤 / コンセント / 配管 / 化粧カバー / 据置金具 / 屋根付き架台 / 工具 / 採寸 / 壁面 / 配線 / 天井裏 / 床下 / その他",
  "location": "室内 / 室外 / 玄関 / 浴室 / 床下 / 天井裏 / 不明",
  "stage": "施工前 / 工程中 / 施工後 / 判定不能",
  "secondary_tags": [...付属設備],
  "composition": "全景 / 接写 / 中距離 / 手元",
  "quality": "good / blurry / dark / duplicate",
  "people_visible": true/false,
  "personal_info": true/false (表札・車のナンバー・顔・書類等),
  "description": "30〜80字で客観的に描写",
  "best_use": "hero-before / hero-after / before / after / process / detail / 除外",
  "suggested_caption": "10〜20字"
}
```

### 出力先

`images/works/{area}/{NNN}/_classification/classification.json`

---

## Phase 3: 振り分けフォルダの自動生成

`organize.py` を実行して `_classification/by_category/` 配下にカテゴリフォルダを生成（**コピーベース**でDropbox安全）。

```
_classification/by_category/
  ├─ 01_施工前/
  ├─ 02_工程中/
  ├─ 03_施工後_室内機/
  ├─ 03_施工後_室外機/
  ├─ 03_施工後_分電盤コンセント/
  ├─ 03_施工後_化粧カバー/
  ├─ 03_施工後_据置金具屋根付き/
  ├─ 04_詳細接写/
  ├─ 99_除外_書類個人情報/     ← 必ず人手確認
  └─ 99_除外_関係薄い/
```

同じ写真が複数カテゴリに該当する場合は**複数フォルダにコピー**（タグ管理）。

ユーザーはエクスプローラーでサムネイル確認 → 間違いがあればフォルダ間で移動。

---

## Phase 4: ベスト写真選定 + Claude自身による再確認（最重要）

### 4-1. ページ用に14枚程度を選定

セクション構成（kitami-001 で確立した型）:

| セクション | 枚数 | 命名 |
|---|---|---|
| ヒーロー Before/After | 2 | hero-before, hero-after |
| ビフォー・アフター | 2 | ba-before, ba-after |
| 施工工程（時系列）| 4 | process-1-XXX, process-2-XXX, process-3-XXX, process-4-XXX |
| 完成写真（各部）| 6 | done-1-XXX, done-2-XXX, ..., done-6-XXX |

セマンティック名で意味が一目で分かるようにする（例: `done-2-panel-circuit.webp`）。

### 4-2. ★Claude自身による再確認★（**絶対省略不可**）

サブエージェントの分類JSONを**鵜呑みにしない**。各スロットに配置する候補画像について、Claude自身が Read tool で実画像を見て「キャプションと一致するか」を1枚ずつ確認する。

**理由（kitami-001 で発生した実例）:**
- IMG_9133 → エージェント「TOSHIBA分電盤の全景」← 実際は古い主幹ブレーカー接写
- IMG_9119 → エージェント「工程中」← 実際は完成写真（カバー外して見せる）
- IMG_9165 → エージェント「主幹ブレーカー接写」← 実際は室外機+縦パイプ

**詳細: [[feedback-photo-classification-verification]]**

### 4-3. WebP生成

`generate-page-images.py` の `MAPPING` 辞書を編集し、IMG_*.jpg → セマンティック名 のマッピングを定義してから実行。

```python
MAPPING = {
    "IMG_9124.jpg": "hero-before",
    "IMG_9128.jpg": "hero-after",
    ...
}
```

出力: `images/works/{area}/{NNN}/` 配下に WebP + JPG ペアを生成（800px幅・WebP品質80・JPG品質85）。

---

## Phase 5: HTMLページに反映

`works-case-builder` スキルに引き継ぐか、HTMLを直接更新:

- 各 `<figure>` の `<img src>` / `<source srcset>` を新ファイル名に変更
- `data-pswp-width` / `data-pswp-height` を新サイズに更新（PhotoSwipe用）
- `alt` / `figcaption` を実画像内容に即して書く（前述の再確認で確認した内容）
- OGP・Article JSON-LD の image URL も更新
- 旧ファイル（自動生成された誤命名画像）を削除

---

## トリガーワード

ユーザーが以下のいずれかを発言したら、このスキルを起動:

- 「写真の分類お願い」「写真振り分けて」
- 「○○○○の施工事例の写真整理して」
- 「ベスト写真選んで」
- works-case-builder 実行時の Phase 1 として自動で呼ばれる

---

## 必須スクリプト

このスキルフォルダに同梱:

- `classify-photos-prompt-template.md` - サブエージェント派遣用プロンプト
- `organize.py` - 振り分けフォルダ生成
- `generate-page-images.py` - WebP生成（MAPPING辞書を案件ごとに編集）

これらを案件ディレクトリにコピーして使うか、パラメータで対象ディレクトリを指定して実行する。

---

## 既知の落とし穴

1. **エージェントは銘板接写を誤認しやすい** → 必ず再確認
2. **「カバー外した分電盤」は工程中とも完成後とも見える** → 撮影意図がないと判別不能。前後の写真の連番と合わせて判断
3. **書類・見積書・請求書が混入** → 個人情報なので絶対除外（kitami-001 では36枚中5枚が書類）
4. **連写の重複** → ベスト1枚だけ採用、それ以外は除外フォルダへ
5. **アンケート用紙の手書き内容** → ページに転記する場合は原文ママ（[[feedback-survey-verbatim-transcription]]）

---

## 関連メモリ

- [[feedback-photo-classification-verification]] - 分類エージェント誤分類の再確認ルール
- [[feedback-case-study-author-voice]] - 担当者コメントはヒアリング必須
- [[feedback-survey-verbatim-transcription]] - アンケートは原文ママ
- [[feedback-case-summary-table-columns]] - 施工概要テーブルから費用/工期/担当者を外す

## 関連スキル

- works-case-builder - このスキルの後段（HTMLページ生成）
- unified-header-footer - 共通ヘッダー・フッター適用
- image-to-webp - 単発のWebP変換ユーティリティ

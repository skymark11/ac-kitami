---
description: 施工事例 1 件を Google Drive の写真フォルダから取得し、AI 分類 → WebP 変換 → HTML 生成まで一気通貫で実行する（ステージ 1：既存スキル束ねバージョン）
argument-hint: <case-id> 例: kitami-004
---

# /case-study {case-id}

施工事例 1 件を Google Drive 上の写真フォルダから取り出し、分類・変換・HTML 生成まで自動実行する。

このコマンドはハーネスエンジニアリング学習プランの **ステージ 1** に相当する。詳細プラン: [`C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md`](C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md)

## 引数

- `$1` = case-id（例: `kitami-004`、`abashiri-007`）

## 前提

- Google Drive 上に `エアコン写真素材/{市名}/{case-id}_{地域}_{お客さま名}/` というフォルダがあり、施工写真 5 枚以上が入っている
- このコマンドは ac-kitami プロジェクト配下で実行する

---

## 実行手順

### Step 1: case-id 解析と市名取得

引数 `$1` を `{市名コード}-{連番3桁}` に分解する（例: `kitami-004` → 市名コード `kitami`、連番 `004`）。

市名コード対応表（`.agents/skills/js-case-studies-section/SKILL.md` Phase 1.5 の規約と同一）:

| 市名コード | 日本語市名 |
|---|---|
| kitami | 北見市 |
| abashiri | 網走市 |
| bihoro | 美幌町 |
| monbetsu | 紋別市 |
| kunneppu | 訓子府町 |
| engaru | 遠軽町 |
| tsubetsu | 津別町 |

未対応の市名コードが渡されたら、表に追加するか入力ミスかを Joe に確認して停止する。

---

### Step 2: Google Drive で対象フォルダを検索

`mcp__claude_ai_Google_Drive__search_files` を使い、Drive 上のフォルダを検索する。

- name: `{case-id}_` で始まるもの（例: `kitami-004_`）
- mimeType: `application/vnd.google-apps.folder`
- 親フォルダ階層: `エアコン写真素材` / `{日本語市名}` 配下にあること

ヒット 0 件: Joe に「Drive に該当フォルダが見つかりません。`エアコン写真素材/{日本語市名}/{case-id}_地域_お客さま名/` の形で作成してください」と返して停止。

ヒット 2 件以上: Joe にどれを使うか確認してから進む。

ヒット 1 件: そのフォルダの ID とフォルダ名（地域・お客さま名を抽出）を記録して Step 3 へ。

---

### Step 3: フォルダ内のファイル一覧取得と早期撤退チェック

ヒットしたフォルダ ID を親に指定して、再度 `mcp__claude_ai_Google_Drive__search_files` で内部ファイルを列挙。

mimeType が `image/jpeg`、`image/png`、`image/webp` のいずれかのファイルだけを抽出。

**早期撤退チェック**: 画像ファイル数 < 5 ならここで停止し、Joe に以下を返す:

```
Drive フォルダに画像が {N} 枚しかありません（必要: 5 枚以上）。

施工事例ページの Rubric では「写真 5 枚以上」が固定 5 点減点項目です。
本文加筆では取り戻せないため、Drive にもう {5-N} 枚追加してから再実行してください。

不足分のヒント:
- before: 工事前の状態（古いエアコン、配管前の壁など）
- process: 工事中の作業ショット（取付中、配管中、真空引きなど）3 枚以上
- after: 工事完了後の全景
```

---

### Step 4: 各画像を 1 枚ずつローカルに保存

ローカル保存先（無ければ作成）:

```
e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\assets\photos\_inbox\エアコン写真素材\{日本語市名}\{case-id}_{地域}_{お客さま名}\
```

各画像について **1 枚ずつ順番に** 以下を実行（並列禁止、MCP レスポンス上限対策）:

1. `mcp__claude_ai_Google_Drive__download_file_content` で base64 文字列を取得
2. PowerShell で base64 デコード → バイナリ保存

```powershell
$base64 = 'MCPから取得した base64 文字列'
$bytes = [Convert]::FromBase64String($base64)
$path = 'C:\full\path\to\save\image.jpg'
[System.IO.File]::WriteAllBytes($path, $bytes)
```

**重要**: `Write` ツールに base64 文字列をそのまま渡すと、テキストファイルとして保存されて画像が壊れる。必ず PowerShell でデコードしてバイナリ書き出しする。

20 枚以上ある場合は所要時間を Joe に伝える（1 枚あたり数秒〜10 秒）。

---

### Step 5: AI 分類（before / process / after の判定）

Step 4 でローカル保存した各画像を、`Read` ツールで 1 枚ずつ開いて視覚的に判定する（Read は画像 MIME をマルチモーダルに処理する）。

| 分類 | 判定基準 |
|---|---|
| **before** | 工事前。古いエアコン、空いた壁、配管がない状態など |
| **process** | 工事中。配管作業、室内機の取付中、室外機の設置中、真空引き、配線中など |
| **after** | 工事完了後。新品のエアコンが綺麗に設置され、配管も整理され、完成した状態 |

判定したら、ファイルを以下の規則でリネーム:

- `before_01.jpg`, `before_02.jpg`, ...
- `process_01.jpg`, `process_02.jpg`, ..., `process_05.jpg`
- `after_01.jpg`, `after_02.jpg`

連番は EXIF の撮影日時で並べる（取得できなければファイルの作成日時で代替）。

判定結果サマリーを Joe に表示:

```
【AI 分類結果】
- before: 2 枚 (before_01.jpg, before_02.jpg)
- process: 5 枚 (process_01.jpg 〜 process_05.jpg)
- after: 3 枚 (after_01.jpg, after_02.jpg, after_03.jpg)
合計 10 枚

分類に違和感があれば教えてください。問題なければ次に進みます。
```

Joe から OK が出てから Step 6 へ。違和感を指摘されたら該当ファイルだけ再判定してリネーム。

---

### Step 6: WebP 変換と公開フォルダへの配置

`image-to-webp` スキルを呼び出して以下を実行:

1. ローカル `_inbox` 配下の JPG/PNG を WebP に変換（品質 80）
2. ファイル名のアンダースコアをハイフンに置換（`before_01.webp` → `before-01.webp`）
3. 公開フォルダにコピー:

```
e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\images\works\{市名コード}\{連番3桁}\
```

例: case-id が `kitami-004` なら `images\works\kitami\004\` に配置。

**注**: ac-kitami の実際の公開フォルダ構造は `images/works/{市名コード}/{連番3桁}/`（既存の `001/`, `002/`, `003/` を踏襲）。SKILL.md の `{project}/assets/images/works/{case-id}/` とは異なるので、こちらの実態を優先する。

Use the `image-to-webp` skill to convert and rename the images in the `_inbox` folder, then copy the WebP files to the public folder above.

---

### Step 7: 施工情報のヒアリング

`js-case-studies-section` スキル Phase 1.5/1.6 に従い、Joe に以下を質問する:

```
施工事例詳細ページの本文を作るため、以下を教えてください（箇条書きで OK）:

1. 施工日（例: 2026年6月20日）
2. 地域（町名まで）（例: 北見市長椅町）
3. 建物種別・築年数（例: 戸建て木造・築25年）
4. 工事内容（例: エアコン新規取付）
5. 機種・メーカー（例: ダイキン スゴ暖 S40ZTAXP）
6. 追加工事（例: 化粧カバー、200V電源工事）
7. お客様の困りごと（依頼の背景）
8. 施工担当者からのコメント
   - 大変だったこと / 苦労した点
   - 特に気を付けたポイント
   - 全体的な感想
```

回答が得られたら Step 8 へ。「全部後で書く」と言われたら、テンプレ生成だけで進めて該当箇所はプレースホルダ `[要入力]` で残す。

---

### Step 8: HTML 生成

`js-case-studies-section` スキル Phase 2-6 に従って、施工事例詳細ページを生成する。

- テンプレート: `e:\Dropbox\apps\remotely-save\.agents\skills\js-case-studies-section\templates\detail-page.html`
- 参考事例（v2 仕様で 99/100 達成）:
  - `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\002\index.html`
  - `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\003\index.html`
- 出力先: `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\{連番3桁}\index.html`

サイト固有設定（アナリティクスコード等）は `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\CLAUDE.md` に従う。

Use the `js-case-studies-section` skill (Phase 2-6) to generate the HTML using the template, the WebP photos prepared in Step 6, and the hearing data from Step 7.

---

### Step 9: Joe への結果報告

最後に以下を表示する:

```
施工事例ページの生成が完了しました。

- 生成 HTML: htdocs/ac-kitami/works/{連番3桁}/index.html
- 画像フォルダ: htdocs/ac-kitami/images/works/{市名コード}/{連番3桁}/
- 写真総数: N 枚 (before: A, process: B, after: C)

【次のステップ】
1. ブラウザで開いて見た目を確認
   Invoke-Item htdocs\ac-kitami\works\{連番3桁}\index.html
2. Rubric 採点をお願いします（ステージ 1 では手動）
   `js-case-studies-section` の `references/quality-checklist.md` で 100 点満点採点
3. 95+ なら git commit／不足なら修正

ステージ 2（Verifier サブエージェント実装）後は、Rubric 採点も自動化されます。
```

---

## ハマりどころメモ

- **base64 デコード**: `download_file_content` の戻りは base64 文字列。必ず PowerShell の `[Convert]::FromBase64String` + `[System.IO.File]::WriteAllBytes` でバイナリ保存すること。Write ツール直渡しは画像が壊れる
- **大容量画像**: スマホ 4000x3000 級（5MB）20 枚一気は MCP の上限近い。1 枚ずつ順次取得、並列禁止
- **写真不足は早期撤退**: 5 枚未満は本文加筆で取り戻せない減点項目（5 点固定）なので Step 3 でブロックする
- **公開フォルダの構造**: SKILL.md の `{project}/assets/images/works/{case-id}/` ではなく、ac-kitami の実態 `images/works/{市名コード}/{連番3桁}/` を優先
- **Dropbox 同期**: 実行前に必ず停止確認。同期中だと書き込み中の画像が `.tmp` 化されて分類ミスの原因になる

---

## このコマンドの位置づけ（ハーネス学習）

これは **ステージ 1** = スラッシュコマンドで既存スキルを束ねただけの最も軽量なハーネス。

次のステージ:

| ステージ | 追加要素 | 学べる概念 |
|---|---|---|
| 2 | Verifier サブエージェント | Maker-Checker 分離 |
| 3 | PostToolUse フック | Edit/Write 直後の自動検証 |
| 4 | `/loop` か Stop フック | Rubric 95+ までの自動リトライ |

全体プラン: [`C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md`](C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md)

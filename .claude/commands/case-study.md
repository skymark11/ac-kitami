---
description: 施工事例 1 件を写真フォルダ（ローカル or Google Drive）から取得し、AI 分類 → 絞り込み → WebP 変換 → HTML 生成まで一気通貫で実行する（ステージ 1：既存スキル束ねバージョン）
argument-hint: <case-id> 例: kunneppu-001
---

# /case-study {case-id}

施工事例 1 件を写真フォルダから取り出し、分類・絞り込み・変換・HTML 生成まで自動実行する。

このコマンドはハーネスエンジニアリング学習プランの **ステージ 1** に相当する。詳細プラン: [`C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md`](C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md)

## 引数

- `$1` = case-id（例: `kunneppu-001`、`kitami-004`、`abashiri-003`）

## 前提

- 写真はローカル `e:\Dropbox\apps\remotely-save\assets\photos\_inbox\エアコン写真素材\{日本語市名}\{case-id}_{お客様地域}_{お客様名}\` か Google Drive 上の同階層に配置されている
- このコマンドは ac-kitami プロジェクト配下で実行する
- ローカルと Drive の両方にある場合はローカルを優先（Drive は予備）

---

## 実行手順

### Step 1: case-id 解析と市名取得

引数 `$1` を `{市名コード}-{連番3桁}` に分解する（例: `kunneppu-001` → 市名コード `kunneppu`、連番 `001`）。

**市名コード対応表**:

| 市名コード | 日本語市名（inbox 第一階層） |
|---|---|
| kitami | 北見市 |
| abashiri | 網走市 |
| bihoro | 美幌町 |
| monbetsu | 紋別市 |
| kunneppu | 訓子府町 |
| engaru | 遠軽町 |
| tsubetsu | 津別町 |

**連番ルール**: 市町村ごとに 001 から振る（市町村別に独立した連番）。

未対応の市名コードが渡されたら、表に追加するか入力ミスかを Joe に確認して停止する。

---

### Step 2: 写真フォルダの検索（ローカル優先・Drive 予備）

#### Step 2a: ローカル検索

```powershell
$caseId = 'kunneppu-001'  # $1
$cityName = '訓子府町'     # Step 1 で確定
$inboxRoot = "e:\Dropbox\apps\remotely-save\assets\photos\_inbox\エアコン写真素材\$cityName"
Get-ChildItem -Path $inboxRoot -Directory -Filter "$caseId`_*" -ErrorAction SilentlyContinue
```

ヒット 1 件: フルパスを記録して Step 3 へ。フォルダ名から `{お客様地域}_{お客様名}` を抽出（ヒアリング初期値に使う）。

ヒット 2 件以上: Joe にどれを使うか確認してから進む。

ヒット 0 件: Step 2b（Drive 検索）に進む。

#### Step 2b: Drive 検索（ローカル 0 件の場合のみ）

`mcp__claude_ai_Google_Drive__search_files` で:

- name: `{case-id}_` で始まるフォルダ
- mimeType: `application/vnd.google-apps.folder`

ヒット 0 件: Joe に「ローカル `{日本語市名}/{case-id}_*` にも Drive にも見つかりません。`{日本語市名}/{case-id}_お客様地域_お客様名/` の形で作成してから再実行してください」と返して停止。

ヒット 1 件以上: フォルダ ID を記録 → Step 4b（Drive ダウンロード）へ進む。Step 3 のファイル数チェックは Drive 上で実施。

---

### Step 3: ファイル一覧取得と早期撤退チェック

ローカル経路:

```powershell
Get-ChildItem -Path $caseFolder -File -Include *.jpg,*.JPG,*.png,*.PNG,*.webp,*.heic,*.HEIC
```

`.mov` や `.MOV`、サブフォルダ（過去案件で `before/process/after` 等が既に作られている場合）は除外する。

**サブフォルダが既にある場合**: Joe に「振り分け済みのようです。再分類しますか、既存構造を尊重しますか」と確認してから進む。

**早期撤退チェック**: 画像ファイル数 < 5 ならここで停止し、Joe に以下を返す:

```
画像が {N} 枚しかありません（必要: 5 枚以上）。

施工事例ページの Rubric では「写真 5 枚以上」が固定 5 点減点項目です。
本文加筆では取り戻せないため、もう {5-N} 枚追加してから再実行してください。

不足分のヒント:
- before: 工事前の状態（古いエアコン、配管前の壁、分電盤、穴あけ位置など）
- process: 工事中の作業ショット（取付中、配管中、真空引きなど）3 枚以上
- after: 工事完了後の全景
```

**過剰枚数の注意**: 50 枚を大きく超える場合は Joe に枚数を伝え「適正は 10-15 枚なので AI 分類後に絞り込みます」と通告してから進む。

---

### Step 4: 画像準備

ローカル経路の場合: 何もしない（既に存在）。Step 5 へ。

---

### Step 4b: Drive フォールバック時のダウンロード

ローカル保存先（無ければ作成）:

```
e:\Dropbox\apps\remotely-save\assets\photos\_inbox\エアコン写真素材\{日本語市名}\{case-id}_{お客様地域}_{お客様名}\
```

各画像について以下を実行（同時に 5-10 枚を並列ダウンロードしてよい）:

1. `mcp__claude_ai_Google_Drive__download_file_content` を呼ぶ
2. レスポンスがコンテキスト上限を超えるため、自動で **ツール結果ファイル** に保存される:
   - 保存先パターン: `C:\Users\shishido\.claude\projects\<proj>\<session>\tool-results\mcp-claude_ai_Google_Drive-download_file_content-<timestamp>.txt`
   - 中身は JSON: `{content: <base64>, id, mimeType, title}`
3. PowerShell でツール結果ファイル → 画像バイナリに変換:

```powershell
$toolResult = Get-Content $toolResultPath -Raw | ConvertFrom-Json
$bytes = [Convert]::FromBase64String($toolResult.content)
$savePath = Join-Path $caseFolder $toolResult.title
[System.IO.File]::WriteAllBytes($savePath, $bytes)
```

**ハマりどころ**:
- base64 文字列を `Write` ツールにそのまま渡すと、テキストファイルとして保存されて画像が壊れる。必ず PowerShell バイナリ書き出し。
- ツール結果 JSON 経由なら **メインコンテキストが汚れない**（並列ダウンロード可）。

---

### Step 5: AI 分類（before / process / after の判定）

各画像を `Read` ツールで開いて **画像内容で視覚的に判定する**（Read は画像 MIME をマルチモーダルに処理する）。

**判定原則（Joe フィードバック）**:

> 室内機がついているかどうか、ビフォーアフター、分電盤、穴あけ等で判断する

EXIF 日付や撮影順は判定に使わない（順序サンプリングでは偏った結果になることが過去事例で実証された）。

| 分類 | 判定基準 |
|---|---|
| **before** | 工事前の現場状況。古いエアコン、配管なしの壁、既設分電盤の状態、事前下見の経路調査、穴あけ予定位置のマーキングなど |
| **process** | 工事中の作業ショット。配管作業、室内機の取付中、室外機の設置中、真空引き、配線中、化粧カバー取付中など |
| **after** | 工事完了後の状態。新品のエアコンが綺麗に設置され、配管も整理され、完成した室内機・室外機の全景 |
| **excluded** | 公開不向き。人物が大きく写る、機材や搬入車のみ、ピンボケ・ブレ、重複構図、書類のみなど |

**バッチ処理の進め方**（写真が多い場合）:

- 10 枚程度を **並列 Read**（1 メッセージ内に複数 Read ツール呼び出し）して効率化する
- 各バッチ後に判定結果を Joe に提示してフィードバックをもらう（特に「事前下見と工事中の境界」のような微妙なケース）

判定が確定したら、ファイルを **サブフォルダに振り分ける**（kitami-005/006 で確立されたパターン）:

```
{case-id}_*/
├── before/
│   ├── (元のファイル名のまま)
│   └── ...
├── process/
├── after/
└── excluded/  (公開しない素材)
```

ファイル名の改名はこの段階では行わない（後の絞り込み確定後に最終命名する）。

判定結果サマリーを Joe に表示:

```
【AI 分類結果】
- before: {A} 枚
- process: {B} 枚
- after: {C} 枚
- excluded: {D} 枚
合計 {N} 枚

分類に違和感があれば教えてください。問題なければ絞り込みに進みます。
```

Joe から OK が出てから Step 5.5 へ。違和感を指摘されたら該当ファイルだけ再判定して移動し直す。

---

### Step 5.5: 絞り込み（適正枚数まで削減）

施工事例ページの適正枚数は **10-15 枚**（before 2-3 / process 5-8 / after 2-4 が目安）。

各サブフォルダから残すべき写真を選定する。選定原則:

- **before**: 「依頼前の困りごとがビジュアルで伝わる」枚数だけ残す。重複構図は削る
- **process**: 「工事のストーリー（経路設計 → 取付 → 仕上げ）」が時系列で追えるように 5-8 枚
- **after**: ファーストビュー用ヒーロー候補 + 室内機・室外機の全景 + 細部の仕上がり

採否の最終判断は Joe に提示してから実行する:

```
【絞り込み案】
- before: {N1} 枚 → {採用ファイル名リスト}
- process: {N2} 枚 → {採用ファイル名リスト}
- after: {N3} 枚 → {採用ファイル名リスト}
不採用は excluded/ に移動します。

問題なければこの構成で進めます。
```

**Joe が事前に Drive 上で枚数を絞ってきている場合** はこの工程をスキップして Step 6 へ。

Joe OK 後、不採用ファイルを `excluded/` に移動。採用ファイルは Step 6 で連番リネームする。

---

### Step 6: WebP 変換と公開フォルダへの配置

採用ファイルを最終命名し、WebP に変換して公開フォルダに配置する。

#### 最終命名（連番付与）

各サブフォルダで以下のように改名:

- `before/` → `before-01.jpg`, `before-02.jpg`, ...
- `process/` → `process-01.jpg`, `process-02.jpg`, ...
- `after/` → `after-01.jpg`, `after-02.jpg`, ...

連番はストーリーが自然に流れる順序で振る（EXIF 撮影時刻は当てにしない。Joe との対話で決めた順序を優先）。

#### WebP 変換

`image-to-webp` スキルを呼び出して以下を実行:

1. 採用 JPG/PNG を WebP に変換（品質 80）
2. 用途別にリサイズ（`.claude/rules/coding.md`「画像」セクションに従う）:
   - ヒーロー（after-01 など）: 最大幅 800px
   - サービスカード・サムネイル相当: 600px
3. 公開フォルダにコピー:

```
e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\images\works\{市名コード}\{連番3桁}\
```

例: `kunneppu-001` なら `images\works\kunneppu\001\`。

JPG/WebP 両方をペアで配置する（HTML 側で `<picture>` フォールバック用）。

Use the `image-to-webp` skill to convert and copy the WebP/JPG pair into the public folder.

---

### Step 7: 施工情報のヒアリング

`js-case-studies-section` スキル Phase 1.5/1.6 に従い、Joe に以下を質問する:

```
施工事例詳細ページの本文を作るため、以下を教えてください（箇条書きで OK）:

1. 施工日（例: 2026年6月20日）
2. 地域（町名まで）（例: 訓子府町弥生）
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

フォルダ名から推測できる項目（地域・お客様名）は初期値として提示し、Joe に確認・修正してもらう。

回答が得られたら Step 8 へ。「全部後で書く」と言われたら、テンプレ生成だけで進めて該当箇所はプレースホルダ `[要入力]` で残す。

---

### Step 8: HTML 生成

`js-case-studies-section` スキル Phase 2-6 に従って、施工事例詳細ページを生成する。

- テンプレート: `e:\Dropbox\apps\remotely-save\.agents\skills\js-case-studies-section\templates\detail-page.html`
- 参考事例（v2 仕様で 99/100 達成）:
  - `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\002\index.html`
  - `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\003\index.html`
- 出力先: `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\works\{連番3桁}\index.html`
  - **注**: 出力先連番は市町村別の連番（kunneppu-001 → `works/001/`）ではなく、**works 全体の通し連番** にする可能性あり。既存の `works/001/`, `002/`, `003/` を踏まえ、Joe に確認して決定。

サイト固有設定（アナリティクスコード等）は `e:\Dropbox\apps\remotely-save\htdocs\ac-kitami\CLAUDE.md` に従う。

ファーストビューの Before/After は **被写体統一が鉄則**（kitami-002 学習）。「室内 Before → 室外 After」のように被写体が飛ぶ構成は避け、同じ被写体（外壁・室内機設置面など）で B/A を組む。

Use the `js-case-studies-section` skill (Phase 2-6) to generate the HTML using the template, the WebP photos prepared in Step 6, and the hearing data from Step 7.

---

### Step 9: Joe への結果報告

最後に以下を表示する:

```
施工事例ページの生成が完了しました。

- 生成 HTML: htdocs/ac-kitami/works/{連番3桁}/index.html
- 画像フォルダ: htdocs/ac-kitami/images/works/{市名コード}/{連番3桁}/
- 採用写真: N 枚 (before: A, process: B, after: C)
- 元素材保管: assets/photos/_inbox/エアコン写真素材/{日本語市名}/{case-id}_*/

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

- **写真は適正枚数の 10 倍ある可能性**: AI 分類後の絞り込み（Step 5.5）は省略不可
- **EXIF 日付・順序サンプリングを信用しない**: スマホ一括アップで createdTime が同一になる、EXIF が剥離していることもある。**画像内容で判断する**のが鉄則
- **サブフォルダ振り分けは kitami-005/006 パターンに従う**: `before/process/after/excluded` の 4 サブフォルダ
- **base64 デコード（Drive 経路時）**: `download_file_content` の戻りはコンテキスト超過時にツール結果ファイルに保存される。JSON 経由でデコードすればメインコンテキスト汚れずに済む
- **公開フォルダの構造**: `images/works/{市名コード}/{連番3桁}/`（既存 `kitami/001/`, `kitami/002/` を踏襲）
- **Dropbox 同期**: 実行前に必ず停止確認。同期中だと書き込み中の画像が `.tmp` 化されて分類ミスの原因になる
- **被写体統一**: ファーストビュー B/A は同じ被写体で組む（室内 → 室外のような飛びは避ける）
- **市町村別連番**: 市名コードごとに 001 から振る（kitami-001 と kunneppu-001 は別シリーズ）
- **works/ 連番との関係**: 公開ページ側 `works/NNN/` の連番は別管理の可能性あり（既存 001-003 は北見市案件で開始）。Step 8 で要確認

---

## このコマンドの位置づけ（ハーネス学習）

これは **ステージ 1** = スラッシュコマンドで既存スキルを束ねただけの最も軽量なハーネス。

次のステージ:

| ステージ | 追加要素 | 学べる概念 |
|---|---|---|
| 2 | Verifier サブエージェント | Maker-Checker 分離（AI 分類の妥当性を別エージェントが再確認） |
| 3 | PostToolUse フック | Edit/Write 直後の自動検証 |
| 4 | `/loop` か Stop フック | Rubric 95+ までの自動リトライ |

全体プラン: [`C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md`](C:\Users\shishido\.claude\plans\swirling-stirring-dusk.md)

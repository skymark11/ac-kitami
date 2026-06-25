# 過去ログ 2026-06 およびそれ以前

NOW.md からアーカイブした作業履歴。直近の状況は NOW.md を参照。

---

## 2026-06-22 (5) works/003 を v2 仕様化（公開水準まで引き上げ）

### 実施内容
1. **PhotoSwipe v5 実装**: head に CSS（非同期読み込み + `.pswp-gallery` スタイル）追加、6つのギャラリー（FV B/A・室内機 B/A・室外機 B/A・配管穴 B/A・施工工程 4枚・完成写真 5枚）に `<a>` ラップ + `data-pswp-width/height`、body 末尾に init script 追加
2. **alt 属性強化**: 全画像に「北見市春光町」「機種名」「部位名」を含めた説明的記述に改善
3. **関連事例リンク切れ修正**:
   - 001 サムネ: `after-01.webp`（削除済み）→ `hero-after.webp`
   - 002 サムネ: `after-04.webp`（v2 刷新で削除済み）→ `done-1-indoor-unit.webp`
4. **SEO 監査レポート作成**: `works/003/seo-audit/kitami-003-seo-audit-2026-06-22.md`
   - **総合スコア 99/100**（works/002 と同水準）
   - クリティカル指摘なし、公開可能水準

---

## 2026-06-22 (4) works/004 を works/003 にリネーム（番号詰め）

### 経緯
- 旧 works/003 案件は After 写真が無く公開不可と判断 → やらない
- 旧 works/004（北見市春光町 市営団地）を 003 として位置付けて公開する方針

### 実施内容
1. `images/works/kitami/003/` の旧コンテンツ（IMG_*.jpg 33枚 + thumbnail）を `git rm -r` で削除
2. `images/works/kitami/004/` を `images/works/kitami/003/` にリネーム
3. `works/004/` を `works/003/` にリネーム
4. `works/003/index.html` 内の URL/パスを 004 → 003 に置換（39箇所、PowerShellで一括）
5. トップ index.html の事例3 画像パス + 詳細リンク `works/003/` 追加
6. works/002/index.html の関連事例リンク `../004/` → `../003/`
7. /works/ ハブに 003 カード追加（CollectionPage 構造化データも 001/002/003 に更新）
8. sitemap.xml に `/works/003/` 追加
9. DEPLOY-STATUS.md を全体最新化

---

## 2026-06-22 (3) kitami/works/001/ → /works/001/ 統合完了

### 実施内容

1. **`/works/001/index.html` を kitami/001 の v2 完成版で上書き**
   - PowerShell で `../../../` → `../../` パス置換、canonical/OGP/URL を `/kitami/works/001/` → `/works/001/` に置換
   - ヘッダーナビ・パンくず・BreadcrumbList の「施工事例」リンクを `トップ#works` → `/works/` ハブに統一（works/002 と整合）
2. **`/works/index.html` ハブ** に 001 カードを追加（CollectionPage 構造化データも 001/002 両方掲載に更新）
3. **トップ index.html** の事例1 リンクを `kitami/works/001/` → `works/001/` に修正
4. **sitemap.xml**: `/kitami/works/001/` を削除、`/works/001/` を追加（lastmod 2026-06-22）
5. **.htaccess に 301 リダイレクト追加**
   ```apache
   Redirect 301 /kitami/works/001/ https://ac-kitami.com/works/001/
   ```
6. **`/kitami/` フォルダを git rm -r で完全削除**（ローカルから物理削除済み）

### Search Console 対応（実施済み 2026-06-25）

1. 新URL `/works/001/` を URL 検査 → インデックス登録リクエスト完了
2. 旧URL `/kitami/works/001/` は削除しない（301 で自動置換を待つ）
3. サイトマップ再送信完了

---

## 2026-06-22 works/002 公開準備完了

### 完了タスク

1. **方針確認**: 二系統 `/works/00X/`（旧・2026-03-16）と `/kitami/works/001/`（新・2026-06-15）が併存していたが、`/works/` に統一する方針を確定
2. **`works/002/index.html`** に **PhotoSwipe v5 を実装**
   - kitami/works/001/ と同じ仕様（PC=ホイールズーム / スマホ=ピンチズーム）
   - 8つのギャラリーに分割
3. **トップ index.html** の事例2修正
   - サムネ画像パス: `after-04.webp`（v2 刷新で削除済み・リンク切れ）→ `done-1-indoor-unit.webp` に変更
   - 「詳細を見る」リンク追加
4. **sitemap.xml** に `https://ac-kitami.com/works/002/` 追加
5. **`/works/index.html`（北見施工事例ハブ）を新規作成**
6. **プライバシー対応: 完成写真の和室全景写真を削除**
   - `images/works/kitami/002/after-1-room.webp / .jpg` を削除
   - 理由: お客様の部屋全体が映り込んでおりプライバシー観点で公開不可

---

## 2026-06-15〜16 kitami-001 施工事例ページ完成 + 写真分類パイプライン実証 + SEO最適化

ブランチ: 全て main にマージ済み・origin に push 済み

### SEO最適化10項目（スコア 77→約93点）

コミット `0734b50` → マージ `13d99b5`

- meta description / og:description / Article JSON-LD から削除済み「209,220円」を全て除去
- 主要キーワード「エアコン取付」を本文・要約・FAQ・CTAに5回挿入（従来0回）
- LocalBusiness + HVACBusiness JSON-LD 新規追加（areaServed 8市町村）
- FAQPage JSON-LD 新規追加（5問）+ 本文FAQセクション（`<details>` 形式）
- アンサーファースト要約段落をH1直下に追加（AI Overviews引用率向上目的）
- Article JSON-LD に publisher / dateModified / author.url 追加、datePublished をアンケート用紙日付 2025-07-23 に正確化
- Twitter Card メタタグ4種追加
- photoswipe.css を `media="print" + onload` で非同期化
- 関連事例をリンク1本 → 画像付きカード2件（abashiri 001/002）に拡充
- CTA: 「エアコン取付・工事」+「中央三輪・端野・常呂・留辺蘂・相内・東相内」周辺地名追加
- 本文文字数 2,988 → 3,926字

### 主な成果

1. **kitami-001 施工事例ページ完成** (`kitami/works/001/index.html`)
   - 北見市中央三輪・三菱霧ヶ峰GV2825・専用回路増設・屋根付き架台
   - 全15画像配置（ヒーロー・施工工程・完成写真・アンケート）
   - PhotoSwipe v5 による画像クリック拡大表示（PC=ホイールズーム / スマホ=ピンチズーム）
   - お客様アンケートを手書き原文ママでテキスト化
   - 担当者コメントは施工主ヒアリング内容を屋号で書き起こし（個人名なし）
   - 施工概要テーブルから費用/工期/担当者を恒久除外

2. **写真分類パイプライン実証** （`images/works/kitami/001/_classification/`）
   - 36枚の IMG_*.jpg をサブエージェントで視覚分類 → JSON出力
   - カテゴリ別フォルダ振り分け（_classification/by_category/）
   - 個人情報含む書類5枚（見積書/請求書）を確実に除外
   - 選定14枚をセマンティック名で WebP+JPG 化
   - **エージェント誤分類3枚を Claude 自身の Read 再確認で検知・修正**

3. **新規スキル `photo-classification-pipeline` 作成**（`.agents/skills/photo-classification-pipeline/`）
   - SKILL.md + プロンプトテンプレート + organize.py + generate-page-images.py
   - 「Claude自身による再確認フェーズ」を必須プロセスとして組み込み（誤分類対策）

4. **ワークフロールール4件をメモリに保存**
   - feedback-case-study-author-voice（担当者コメントはヒアリング必須・個人名NG）
   - feedback-case-summary-table-columns（費用/工期/担当者をテーブルから恒久除外）
   - feedback-survey-verbatim-transcription（アンケートは原文ママ転記）
   - feedback-photo-classification-verification（分類エージェント出力は誤分類前提）

---

## 2026-06-15 秘書ハブからの引き継ぎ（FVデザイン整え + SEO死守）

### ユーザー要望
エアコンラボ（ac-kitami）のヘッダー〜ファーストビューの **ぱっと見の印象・レイアウト・文字・キャッチコピー** を整えたい。

### **絶対条件: SEO順位を維持する（最重要ポイント）**

ac-kitami.com は「北見市エアコン取付」等の重要キーワードで **検索結果1位〜2位の上位表示** を取れている。FV改修で順位を落とすのは絶対にNG。

### 変更可・不可の整理

#### 変更してはいけない（SEO死守）

- `<title>` 文言「北見市エアコン販売・設置取付工事 | 地域密着のエアコン専門店」
- `<meta name="description">` 文言
- og:title / og:description
- 構造化データ（LocalBusiness / FAQPage / Article 等のJSON-LD）
- `<h1>` 文言「エアコンラボ北見店」
- `<h2>` メインキャッチコピー「北見市で**エアコン取付**なら地域密着の当店へ」
- canonical URL
- 既存画像の URL パス
- 既存画像の alt 属性内のキーワード
- 内部リンク構造（hash アンカー含む）

#### 自由に整えてよい（SEOに影響なし）

- CSS（フォント、色、余白、シャドウ、トランジション、グラデーション、レスポンシブ）
- フォントサイズ・行間・字間
- ヘッダーの装飾（背景透過、固定ヘッダーの挙動）
- ボタンの形状・色・サイズ・ホバーエフェクト
- お問い合わせカードのデザイン
- アイコン・装飾要素の追加・差し替え
- 画像の WebP 最適化（同URL・同寸法維持）

#### 慎重に変更（ベースライン記録 → 1〜2週間モニタリング）

- サブキャッチコピー
- CTAボタンの文言・色・サイズ
- 画像の差し替え（alt属性のキーワードは絶対維持）
- セクションの順番

### モニタリング指標

| 指標 | 目標 | 確認場所 |
|---|---|---|
| 「北見市エアコン取付」順位 | 1〜2位維持 | Search Console |
| 「北見市エアコン」順位 | 上位維持 | 同上 |
| LCP | 2.5秒以下維持 | PageSpeed Insights |
| INP | 200ms以下維持 | 同上 |
| CLS | 0.1以下維持 | 同上 |

**ステータス**: 2026-06-25 時点で着手未了（必要に応じて将来タスク化）

---

## 2026-06-07 abashiri/works/* Git 反映 + スマホブランチ整理

### 1. abashiri/works/* FTP公開済み内容を Git に反映（c4ab384 / 73ファイル）
- 施工事例ハブ + 詳細001/002 ページ
- 既存画像のWebP再変換による大幅軽量化（after-04: 1.9MB→78KB 等、合計数十MB削減）
- sitemap.xml、index.html フッター・対応エリアリンク整備
- DEPLOY-STATUS.md 更新

### 2. `.agents/skills/` を Git 管理に追加
- unified-header-footer
- works-case-builder

### 3. Dropbox同期競合コピー削除

### 4. スマホ作業ブランチ5件すべて整理（リモート削除）

| ブランチ | 判定 |
|---|---|
| claude/ac-2027-kitami-page-YxKMG | main に別実装で取込み済み → 削除 |
| claude/ac-lab-landing-page-L8yXi | 古いLP試作 → 削除 |
| claude/fix-construction-examples-jIzqM | 北見side works/ 試作（別案件）→ 削除 |
| claude/issue-content-review-7Gmgv | お客様の声セクション → 後日改めるとして削除 |
| claude/kitami-gbp-local-seo-ohvfJ | LocalBusiness強化 → 別タスク化して削除 |

### 5. about: 防虫キャップ無料サービスの記載削除（779f856）

→ FTP 公開済み（2026-06-25 FTP アップで反映完了）

---

## 参考: kitami-001 施工情報（確定済み）

| 項目 | 内容 |
|---|---|
| 施工日 | 2025年7月 |
| 地域 | 北見市中央三輪 |
| 建物 | 戸建て（平屋） |
| 機種 | 三菱 霧ヶ峰 GV2825（10畳用） |
| 工期 | 1日（約5-8時間） |
| 担当者 | 宍戸 尚貴（第二種電気工事士） |
| 追加工事 | 屋根付き据置金具、室外化粧カバー、専用回路増設 |

---

## 構造化データ強化スプリント（保留・別タスク）

旧ブランチ claude/kitami-gbp-local-seo-ohvfJ の内容を**現main基準で再実装**。

- **index.html の LocalBusiness JSON-LD に追加**:
  - `@type` を `["LocalBusiness", "HVACBusiness"]` 併用に
  - `address`（北海道北見市）
  - `geo`（緯度経度: 43.8024, 143.8913）
  - `openingHoursSpecification`（毎日 09:00-19:00）
  - `priceRange`（$$）
  - `image`（ヒーロー画像）
- **about/index.html の LocalBusiness にも**:
  - `address` / `geo` / `openingHoursSpecification` を追加
- 効果: GBP（Googleビジネスプロフィール）連携・ローカルSEO向上

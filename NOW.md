## セッション引き継ぎ

最終更新: 2026-06-22

### 2026-06-22 (5) works/003 を v2 仕様化（公開水準まで引き上げ）

#### 実施内容
1. **PhotoSwipe v5 実装**: head に CSS（非同期読み込み + `.pswp-gallery` スタイル）追加、6つのギャラリー（FV B/A・室内機 B/A・室外機 B/A・配管穴 B/A・施工工程 4枚・完成写真 5枚）に `<a>` ラップ + `data-pswp-width/height`、body 末尾に init script 追加
2. **alt 属性強化**: 全画像に「北見市春光町」「機種名」「部位名」を含めた説明的記述に改善
3. **関連事例リンク切れ修正**:
   - 001 サムネ: `after-01.webp`（削除済み）→ `hero-after.webp`
   - 002 サムネ: `after-04.webp`（v2 刷新で削除済み）→ `done-1-indoor-unit.webp`
4. **SEO 監査レポート作成**: `works/003/seo-audit/kitami-003-seo-audit-2026-06-22.md`
   - **総合スコア 99/100**（works/002 と同水準）
   - クリティカル指摘なし、公開可能水準

#### これで works/003 は FTP アップ可能

すべてアップ前の準備（PhotoSwipe・SEO 監査・リンク切れ修正）が完了。

### 2026-06-22 (4) works/004 を works/003 にリネーム（番号詰め）

#### 経緯
- 旧 works/003 案件は After 写真が無く公開不可と判断 → やらない
- 旧 works/004（北見市春光町 市営団地）を 003 として位置付けて公開する方針

#### 実施内容
1. `images/works/kitami/003/` の旧コンテンツ（IMG_*.jpg 33枚 + thumbnail）を `git rm -r` で削除
2. `images/works/kitami/004/` を `images/works/kitami/003/` にリネーム
3. `works/004/` を `works/003/` にリネーム
4. `works/003/index.html` 内の URL/パスを 004 → 003 に置換（39箇所、PowerShellで一括）
5. トップ index.html の事例3 画像パス + 詳細リンク `works/003/` 追加
6. works/002/index.html の関連事例リンク `../004/` → `../003/`
7. /works/ ハブに 003 カード追加（CollectionPage 構造化データも 001/002/003 に更新）
8. sitemap.xml に `/works/003/` 追加
9. DEPLOY-STATUS.md を全体最新化

#### 注意事項
- **works/003/ は v1 仕様のまま**（2026-03-16作成のオリジナル中身）
- PhotoSwipe 未実装、画像 semantic 命名化されていない、SEO 監査未実施
- 公開は可能（旧仕様だが完成形）
- **v2 仕様化（PhotoSwipe・semantic命名・SEO最適化）は別タスク**として未着手

### 2026-06-22 (3) kitami/works/001/ → /works/001/ 統合完了

#### 実施内容

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
   既存インデックスを引き継ぐため必須。
6. **`/kitami/` フォルダを git rm -r で完全削除**（ローカルから物理削除済み）

#### 公開後の必須対応

**FTP アップ時に以下を必ず実施**:
1. `/works/001/index.html` を新規アップロード
2. `/works/index.html` を上書きアップロード（001 カード追加版）
3. `/index.html` を上書きアップロード（事例1 リンク修正）
4. `/sitemap.xml` を上書きアップロード
5. **`/.htaccess` を上書きアップロード**（301 リダイレクト反映）← **これを忘れると重複コンテンツ問題発生**
6. **FTP サーバー側の `/kitami/works/001/` フォルダを手動削除**（.htaccess の 301 が機能していれば 301 が優先されるが、安全のため削除推奨）

#### Search Console での対応

1. **新URL `/works/001/` を URL 検査 → インデックス登録リクエスト**
2. 旧URL `/kitami/works/001/` は **「削除」しない**（301 で自動置換されるのを待つ。削除すると一時的に検索結果から消える）
3. サイトマップ再送信
4. 1-2週間後にインデックス状況確認:
   - `/kitami/works/001/` のインデックスが `/works/001/` に置き換わっているか
   - 主要キーワード（「北見市 エアコン 工事」「北見市中央三輪」等）の順位推移

#### リスクと対処

- **301 が効くまで 1-2 週間**: その間 `/kitami/works/001/` のインデックスは残るが、Googleが順次置換する
- **旧URL に流入があった場合**: 301 で `/works/001/` に自動転送されるので問題なし
- **`/kitami/works/001/` のソーシャル共有・外部被リンク**: 301 でリンクジュースが転送される

### 2026-06-22 works/002 公開準備完了

#### 今回の作業範囲（最小公開準備）

ユーザー判断: **B案（旧系統 `/works/` に統一）**、今回は **works/002/ + /works/ ハブ作成**。

#### 追加対応（コミット 2fbfa6f 後）

1. **`/works/index.html`（北見施工事例ハブ）を新規作成**
   - `/abashiri/works/index.html` をテンプレに、北見用にパス/タイトル/メタ情報を調整
   - 002 カード1件のみ掲載（001/004 公開時にカード追加予定）
   - CollectionPage + BreadcrumbList の構造化データ付き
   - **重要**: これがないと works/002/ のパンくず・構造化データの「施工事例」リンクが全て 404 になっていた（公開漏れ）
   - sitemap.xml に `/works/` も追加

2. **プライバシー対応: 完成写真の和室全景写真を削除**
   - `images/works/kitami/002/after-1-room.webp / .jpg` を削除
   - works/002/index.html から該当ブロック削除
   - 理由: お客様の部屋全体が映り込んでおりプライバシー観点で公開不可
   - 完成写真セクションは6枚グリッドのみに（B/A セクションで主要な部位は別途網羅されている）

#### 完了タスク

1. **方針確認**: 二系統 `/works/00X/`（旧・2026-03-16）と `/kitami/works/001/`（新・2026-06-15）が併存していたが、`/works/` に統一する方針を確定
2. **`works/002/index.html`** に **PhotoSwipe v5 を実装**
   - kitami/works/001/ と同じ仕様（PC=ホイールズーム / スマホ=ピンチズーム）
   - 8つのギャラリーに分割（FV B/A・室外機 B/A・室内機 B/A・分電盤 B/A・化粧モール・完成写真全景・完成写真グリッド・アンケート）
3. **トップ index.html** の事例2修正
   - サムネ画像パス: `after-04.webp`（v2 刷新で削除済み・リンク切れ）→ `done-1-indoor-unit.webp` に変更
   - 「詳細を見る」リンク追加（→ `works/002/`）
4. **sitemap.xml** に `https://ac-kitami.com/works/002/` 追加（lastmod 2026-06-22）
5. **DEPLOY-STATUS.md** 更新
   - `/kitami/works/001/`（2026-06-16公開）を「FTP公開済み」に記録（漏れていた）
   - `/works/002/` を「公開準備中（今回FTPアップ予定）」に
   - `/works/001/` `/works/004/` を「未公開・別途対応」に

#### FTPアップ待ち（今回まとめて反映）

| 種別 | パス | 備考 |
|---|---|---|
| 新規 | `/works/002/` フォルダ一式 | v2 仕様・SEO 99/100・PhotoSwipe 実装済み |
| 新規 | `/js/photoswipe/` フォルダ一式 | photoswipe.css / photoswipe.esm.min.js / photoswipe-lightbox.esm.min.js（既にローカルにある。FTPには未アップの可能性高い） |
| 新規 | `/images/works/kitami/002/` の semantic 命名ファイル一式 | hero-*, ba-*, done-*, after-1-room, アンケート画像（19枚相当） |
| 更新 | `/index.html` | 事例2 サムネ + リンク修正 |
| 更新 | `/sitemap.xml` | `/works/002/` 追加 |
| 残: 前回未反映 | `/about/index.html` | 779f856 防虫キャップ削除（前回FTP漏れ） |
| 残: 前回未反映 | `/kitami/works/001/` 関連一式 | 既に FTP 公開済み・最新の SEO 最適化 10項目反映分が未反映の可能性。要確認 |
| 残: 前回未反映 | `/js/photoswipe/` | kitami-001 公開時に上げたかも。要確認 |

**FTPにアップしないフォルダ**（既存ルール踏襲）:
- `/works/002/seo-audit/`（監査レポート・公開不要）
- `/images/works/kitami/002/_classification/`（分類用JSON・元素材30枚）
- `.agents/`, `.claude/`, `.git/`, `.github/`, `NOW.md`, `CLAUDE.md`, `DEPLOY-STATUS.md` 等

#### 公開前にユーザー対応が必要な事項

1. **ベースライン記録**（順位モニタリング用・FTPアップ前に必須）
   - Search Console で「北見市エアコン取付」「北見市エアコン」「北見市 エアコン 工事」等の主要KW直近30日順位・CTR・表示回数をスクショ
   - 既存 `/kitami/works/001/` の表示回数・クエリも控える
   - PageSpeed Insights でトップページ・`/kitami/works/001/`・`/works/002/`（公開後）の LCP/INP/CLS を記録
   - 保存先: `seo-audit/baseline-2026-06-22.md`
2. **FTPアップロード手順**
   - 上記「FTPアップ待ち」の項目を反映
   - 特に `/js/photoswipe/` と `/images/works/kitami/002/` の新ファイル群を**フォルダごとアップ**忘れに注意
3. **アップ後の即時確認**
   - https://ac-kitami.com/works/002/ が 200 で表示
   - PhotoSwipe が動作（画像クリック→拡大）
   - https://ac-kitami.com/ の事例2 サムネ＆「詳細を見る」リンク
   - https://ac-kitami.com/sitemap.xml に `/works/002/` 含まれる
4. **Search Console**
   - sitemap.xml 再送信
   - `/works/002/` を URL 検査 → インデックス登録リクエスト

### 将来タスク: kitami/works/001/ → works/001/ 統合（今回はやらない）

B案統一に従い、いずれ `/kitami/works/001/` を `/works/001/` に移植・統合する必要あり。

**移行時の必須手順**:
1. `/works/001/index.html` を kitami/works/001/ の内容（SEO 93点版）で置き換え
2. `.htaccess` に `Redirect 301 /kitami/works/001/ https://ac-kitami.com/works/001/` を追加（インデックス引き継ぎ）
3. sitemap.xml の URL 入れ替え
4. トップページ index.html の事例1 リンク `kitami/works/001/` → `works/001/`
5. Search Console で新URL 再申請、旧URL は削除しない（301で自動置換）

**インデックス影響**: `/kitami/works/001/` は既に Google にインデックスされている可能性大（公開 + sitemap 登録 + 1週間経過）。301 リダイレクトで対処可能。

### 2026-06-15〜16 kitami-001 施工事例ページ完成 + 写真分類パイプライン実証 + SEO最適化

ブランチ: 全て main にマージ済み・origin に push 済み

#### 追加コミット（SEO最適化10項目・スコア 77→約93点）

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

#### 今回の主な成果

1. **kitami-001 施工事例ページ完成** (`kitami/works/001/index.html`)
   - 北見市中央三輪・三菱霧ヶ峰GV2825・専用回路増設・屋根付き架台
   - 全15画像配置（ヒーロー・施工工程・完成写真・アンケート）
   - PhotoSwipe v5 による画像クリック拡大表示（PC=ホイールズーム / スマホ=ピンチズーム）
   - お客様アンケートを手書き原文ママでテキスト化
   - 担当者コメントは施工主ヒアリング内容を屋号で書き起こし（個人名なし）
   - 施工概要テーブルから費用/工期/担当者を恒久除外
   - sitemap.xml に `/kitami/works/001/` 追加
   - トップページ index.html の001カードに「詳細を見る」リンク追加 + サムネを hero-after.webp に更新

2. **写真分類パイプライン実証** （`images/works/kitami/001/_classification/`）
   - 36枚の IMG_*.jpg をサブエージェントで視覚分類 → JSON出力
   - カテゴリ別フォルダ振り分け（_classification/by_category/）
   - 個人情報含む書類5枚（見積書/請求書）を確実に除外
   - 選定14枚をセマンティック名で WebP+JPG 化（hero-before, ba-after, process-1-floor, done-1-indoor-unit など）
   - **エージェント誤分類3枚を Claude 自身の Read 再確認で検知・修正**

3. **新規スキル `photo-classification-pipeline` 作成**（`.agents/skills/photo-classification-pipeline/`）
   - SKILL.md + プロンプトテンプレート + organize.py + generate-page-images.py
   - 「Claude自身による再確認フェーズ」を必須プロセスとして組み込み（誤分類対策）

4. **ワークフロールール4件をメモリに保存**（C:\Users\shishido\.claude\projects\...\memory\）
   - feedback-case-study-author-voice（担当者コメントはヒアリング必須・個人名NG・因果順序を保持）
   - feedback-case-summary-table-columns（費用/工期/担当者をテーブルから恒久除外）
   - feedback-survey-verbatim-transcription（アンケートは原文ママ転記）
   - feedback-photo-classification-verification（分類エージェント出力は誤分類前提・Claude自身が再確認）

#### feature/photo-pipeline-foundation ブランチの扱い

睡眠中Claude（2026-06-11）が作った `feature/photo-pipeline-foundation` ブランチは、今回別アプローチで実証済みのため不要。
新スキル `photo-classification-pipeline` がそれを置き換えるので、`feature/photo-pipeline-foundation` ブランチは **削除推奨**。

```bash
git -C "e:/Dropbox/apps/remotely-save/htdocs/ac-kitami" branch -D feature/photo-pipeline-foundation
```

#### 次にやること

1. **FTPアップロード待ち**（下記「FTPアップ待ち」セクション参照・項目大幅増）
2. feature/kitami-001-case-page を main にマージするか PR を作るかユーザー判断
3. パイプラインを kitami-002, abashiri-003 等の他案件に適用してみる
4. 別タスク: FVデザイン整え（下記 2026-06-15 秘書ハブ引き継ぎ参照）

---

### 2026-06-15 秘書ハブからの引き継ぎ（FVデザイン整え + SEO死守）

#### ユーザー要望

エアコンラボ（ac-kitami）のヘッダー〜ファーストビューの **ぱっと見の印象・レイアウト・文字・キャッチコピー** を整えたい。

#### **絶対条件: SEO順位を維持する（最重要ポイント）**

ac-kitami.com は「北見市エアコン取付」等の重要キーワードで **検索結果1位〜2位の上位表示** を取れている。FV改修で順位を落とすのは絶対にNG。

#### 現状FV構造の把握（index.html）

| 行 | 要素 | 内容 | SEO重要度 |
|---|---|---|---|
| L20 | `<meta name="description">` | 「北見市でエアコン取付なら地域密着の当店へ。北見市を中心に、低価格でエアコン販売から取付工事までワンストップでご提供。最短で翌日対応可能！」 | **最重要・触らない** |
| L21 | `<title>` | 「北見市エアコン販売・設置取付工事 \| 地域密着のエアコン専門店」 | **最重要・触らない** |
| L104-105 | og:title / og:description | 同上の内容 | 重要・触らない |
| L120付近 | 構造化データ (LocalBusiness JSON-LD) | エアコンラボ北見店の事業情報 | 重要・触らない |
| L195-263 | `<header>` ＋ LINEバナー | ヘッダー・グロナビ・サブCTA | デザイン整え可 |
| L199 | `<h1>` | 「エアコンラボ北見店」（Pacificoフォント） | **触らない**（H1文言は順位影響大） |
| L265-295 | hero-section | 背景画像 + キャッチコピー + CTAボタン2つ | 要慎重 |
| L270-272 | `<h2>` メインキャッチ | 「北見市で**エアコン取付**なら地域密着の当店へ」（lg:text-5xl） | **触らない**（キーワード密度の核） |
| L273-275 | サブキャッチ | 「北見市を中心に、低価格でエアコン販売から取付工事までワンストップでご提供。最短で翌日対応可能！取付工事のみも対応致します！」 | 慎重に（A/B推奨） |
| L277-295 | CTAボタン | 「エアコン購入＋設置工事」「設置工事のみ」 | 慎重に（CV率影響） |
| L298-320 | お問い合わせカード | 電話/メール/LINEボタン | デザイン整え可 |
| 背景画像 | hero-bg.webp / hero-bg.jpg | FV背景 | 同URL・同サイズ維持なら変更可 |

#### 変更可・不可の整理

##### ❌ 変更してはいけない（SEO死守）

- `<title>` 文言
- `<meta name="description">` 文言
- og:title / og:description
- 構造化データ（LocalBusiness / FAQPage / Article 等のJSON-LD）
- `<h1>` 文言「エアコンラボ北見店」
- `<h2>` メインキャッチコピー「北見市で**エアコン取付**なら地域密着の当店へ」
- canonical URL
- 既存画像の URL パス（hero-bg.* の URL を変えると OGP キャッシュ・CDN キャッシュが崩れる）
- 既存画像の alt 属性内のキーワード（「北見市」「エアコン取付」等）
- 内部リンク構造（hash アンカー含む）

##### ✅ 自由に整えてよい（SEOに影響なし）

- CSS（フォント、色、余白、シャドウ、トランジション、グラデーション、レスポンシブ）
- フォントサイズ・行間・字間（読みやすさ向上）
- ヘッダーの装飾（背景透過、固定ヘッダーの挙動）
- ボタンの形状・色・サイズ・ホバーエフェクト
- お問い合わせカードのデザイン
- アイコン・装飾要素の追加・差し替え
- 画像の WebP 最適化（同URL・同寸法維持）
- レイアウト微調整（重要キーワードを含むブロック自体は削除・移動しない）

##### ⚠️ 慎重に変更（必ずベースライン記録 → 1〜2週間モニタリング）

- サブキャッチコピー（L273-275）
- CTAボタンの文言・色・サイズ
- 画像の差し替え（hero背景含む。alt属性のキーワードは絶対維持）
- セクションの順番

#### 推奨フロー（実装側）

1. **着手前: ベースライン記録**
   - Search Console で「北見市エアコン取付」等の主要キーワードの直近30日順位・CTR・表示回数をスクショ
   - Core Web Vitals（LCP/INP/CLS）の現状値を PageSpeed Insights で記録
   - `seo-audit/baseline-2026-06-15.md` として保存
2. **第1フェーズ: CSS主体の安全改修**
   - 上記「自由に整えてよい」項目のみ変更（HTML本文の文言・タグ構造は触らない）
   - ローカル `npm run dev` でデザイン確認
   - ユーザー目視OK → main マージ → FTPアップ
3. **第2フェーズ（必要なら）: 慎重項目の改修**
   - サブキャッチや CTA文言の変更は A/B テスト的に1要素ずつ
   - 変更ごとに Search Console で順位モニタリング（最低1週間）
   - 順位悪化兆候があれば即ロールバック
4. **ロールバック準備**
   - 各 commit を細かく分けて、戻しやすい状態に
   - git tag `before-fv-redesign-2026-06-15` で着手前状態を保存

#### モニタリング指標

| 指標 | 目標 | 確認場所 |
|---|---|---|
| 「北見市エアコン取付」順位 | 1〜2位維持 | Search Console |
| 「北見市エアコン」順位 | 上位維持 | 同上 |
| LCP | 2.5秒以下維持 | PageSpeed Insights |
| INP | 200ms以下維持 | 同上 |
| CLS | 0.1以下維持 | 同上 |
| 検索CTR | 現状以上 | Search Console |

#### 補足

- ユーザーは「ぱっと見の印象を整えたい」と言っているだけで、具体的な不満点は未確定。**第1フェーズ着手前に「現状のここが気になる」を具体ヒアリング推奨**（例: フォントが古い? CTA が目立たない? 画像が暗い? 余白が窮屈? お問い合わせカードが大きすぎる?）
- 既存の FTPアップ未反映 `about/index.html`（779f856）も忘れずに今回のFTPアップで一緒に上げる
- 親 CLAUDE.md のSEOルール・デザインルールを必ず読む

---

### セッション状態
- **休憩中**（次のセッションでそのまま再開できる状態）
- フェーズ1「リポジトリ整合性整理」完了
- 次回着手予定: **kitami-001 施工事例ページ作成**

---

### ⚠️ FTPアップ待ち（最優先の引き継ぎ事項）

**ローカル・GitHub には反映済みだが FTP に未反映の変更:**

| ファイル/フォルダ | 変更内容 | 由来 |
|---|---|---|
| `about/index.html` | 「防虫キャップ無料サービス」の記載削除 | コミット 779f856 |
| `index.html` | 施工事例セクション001カードに詳細リンク追加 + サムネ画像更新（hero-after.webp/jpg） | feature/kitami-001-case-page |
| `sitemap.xml` | `/kitami/works/001/` 追加 | feature/kitami-001-case-page |
| `kitami/works/001/` フォルダ一式 | 新規施工事例ページ index.html | feature/kitami-001-case-page |
| `images/works/kitami/001/` | 旧ファイル28枚削除（before-01〜02, after-01〜08, process-01〜04）+ 新ファイル28枚追加（hero/ba/process-N/done-N の.webp/.jpg）| feature/kitami-001-case-page |
| `js/photoswipe/` フォルダ一式 | PhotoSwipe v5 三点セット（photoswipe.css / .esm.min.js / -lightbox.esm.min.js）| feature/kitami-001-case-page |

→ 次回FTPアップロード時に **上記すべてを反映する**こと。
特に `kitami/works/001/` と `js/photoswipe/` は新フォルダなので、フォルダごとアップロード忘れに注意。
`images/works/kitami/001/` 内の旧ファイル（before-01.* など）はFTP側からも削除推奨。

**FTPにアップしないフォルダ（公開不要）:**
- `images/works/kitami/001/_classification/`（分類用JSONとスクリプト）
- `images/works/kitami/001/IMG_*.jpg`（元写真36枚・容量大）
- `.agents/skills/photo-classification-pipeline/`（スキル定義）
- `.claude/`, `.git/`, `.github/`, `NOW.md`, `CLAUDE.md`, `PIPELINE-PLAN.md` 等

---

### 今回完了したこと（2026-06-07）

#### 1. abashiri/works/* FTP公開済み内容を Git に反映（c4ab384 / 73ファイル）
- 施工事例ハブ + 詳細001/002 ページ
- 既存画像のWebP再変換による大幅軽量化（after-04: 1.9MB→78KB 等、合計数十MB削減）
- sitemap.xml、index.html フッター・対応エリアリンク整備
- DEPLOY-STATUS.md 更新

#### 2. `.agents/skills/` を Git 管理に追加
- unified-header-footer
- works-case-builder

#### 3. Dropbox同期競合コピー削除
- `.claude/settings.local (...競合コピー...).json`

#### 4. スマホ作業ブランチ5件すべて整理（リモート削除）

| ブランチ | 判定 |
|---|---|
| claude/ac-2027-kitami-page-YxKMG | main に別実装で取込み済み → 削除 |
| claude/ac-lab-landing-page-L8yXi | 古いLP試作 → 削除 |
| claude/fix-construction-examples-jIzqM | 北見side works/ 試作（別案件）→ 削除 |
| claude/issue-content-review-7Gmgv | お客様の声セクション → 後日改めるとして削除 |
| claude/kitami-gbp-local-seo-ohvfJ | LocalBusiness強化 → 別タスク化して削除 |

#### 5. NOW.md 更新（d922798）

#### 6. about: 防虫キャップ無料サービスの記載削除（779f856・FTPアップ未済）

#### 7. `.tmp` 系一時ファイル 16件 削除（0.28MB）
- index.html.tmp, sitemap.xml.tmp, settings.local.json.tmp など
- Dropbox同期残骸の掃除

---

### 決定事項
- **整合性**: ローカル = GitHub main = （abashiri/works/* についてはFTP）が揃った
- **about/index.html の防虫キャップ削除は FTP 未反映**（次回アップ時に忘れず反映）
- **kitami-001 計画は有効**: 画像WebP変換（Step 1）は完了済み（`images/works/kitami/001/` に15枚配置済み）
- **お客様の声セクション再実装**は別タスク
- **構造化データ強化スプリント**は別タスク

---

### 次にやるべきこと（優先順位）

#### 1. kitami-001 施工事例ページ作成（最優先・継続中）
- ✅ Step 1 画像WebP変換: 完了済み
- ⬜ Step 2: index.html 施工事例セクション（行719-778付近）を実データカードに置換
- ⬜ Step 3: `kitami/works/001/index.html` 新規作成（`abashiri/works/001/` をテンプレに）
- ⬜ Step 4: Rubric採点 80点以上確認
- **プランファイル**: `C:\Users\shishido\.claude\plans\twinkling-snuggling-ocean.md`
- **施工情報**: 下記「kitami-001 施工情報」参照

#### 2. お客様の声セクション再実装（別タスク・後日）
- 旧ブランチ claude/issue-content-review-7Gmgv の方向性を参考に:
  - 独立した `#reviews` セクションを作る
  - 3カードグリッド形式・星評価付き
  - LINE / Googleレビュー投稿の誘導CTA
- 現在 main の「お客様満足度98.5%」セクションを土台に統合する形で

#### 3. 構造化データ強化スプリント（別タスク・後日）
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

#### 4. その他保留中
- **ローカルブランチ `feature/200v-column`** の処置（中身要確認・リモートには無し）
- `/monbetsu/` 内容確定後のFTP公開
- `/bihoro/` 内容確定後のFTP公開
- `/abashiri/works/003/` 駒場入れ替え事例の生成（works-case-builder スキル使用予定）

---

### 参考: kitami-001 施工情報（確定済み）

| 項目 | 内容 |
|---|---|
| 施工日 | 2025年7月 |
| 地域 | 北見市中央三輪 |
| 建物 | 戸建て（平屋） |
| 機種 | 三菱 霧ヶ峰 GV2825（10畳用） |
| 費用 | 209,220円（税込）※請求額を掲載 |
| 工期 | 1日（約5-8時間） |
| 担当者 | 宍戸 尚貴（第二種電気工事士） |
| 追加工事 | 屋根付き据置金具、室外化粧カバー、専用回路増設 |

**使用画像（info-template.txt 記載）**:
- before: before-00, before-02
- after: after-02, 05, 06, 08, 09, 11, 17, 20
- process: process-01, 02, 14, 19
- アンケート: kitami-chuomiwa-aircon-review-001.jpg

**画像ソース**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/`
**画像出力先**: `htdocs/ac-kitami/images/works/kitami/001/`（既存IMG_*.jpgと共存）

### 注意事項・文脈
- **網走市ページとの改善点**: 費用表示追加、4軸タグ、width/height属性、担当者名・資格記載、アンケート画像追加
- **process-18.jpg vs process-19.jpg**: info-template には process-18 とあるが、_inbox フォルダには process-19.jpg が存在。要確認
- **002/003 の画像**: 分類未完了のため、`htdocs/ac-kitami/images/works/kitami/002/, 003/` の IMG_*.jpg から代表1枚を選定して使う
- **index.html の施工事例セクション**: 現在位置は行719-778
- **info-template.txt**: `assets/photos/_inbox/エアコン写真素材/北見市/kitami-001_中央三輪_梅津様/info-template.txt` に施工ポイントの詳細テキストあり（ストーリー化の元ネタ）

---

### 新セッション開始時の確認チェックリスト
新しいClaude会話を始めるときに、このNOW.mdを読んだ上で以下を確認:

- [ ] 現在のブランチが `main` であることを確認（`git branch`）
- [ ] ローカル変更がないことを確認（`git status` → clean想定）
- [ ] GitHub main の最新状態と一致していることを確認（`git pull` または `git fetch`）
- [ ] **FTPアップ待ち項目**（上記表）が残っていれば、次のFTPアップで反映する
- [ ] kitami-001 に着手する場合は、プランファイル `C:\Users\shishido\.claude\plans\twinkling-snuggling-ocean.md` を必ず先に読む

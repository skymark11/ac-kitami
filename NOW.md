# NOW.md — ac-kitami.com 作業引き継ぎ

最終更新: 2026-06-29 深夜（美幌・小清水・訓子府 一気に新規ページ追加完了）

---

## 🆕 2026-06-29 深夜セッション完了サマリー

**美幌・小清水・訓子府 3 エリアにわたって計 7 ファイル新規作成 / 1 ファイル差し替え:**

| 案件 | ファイル | 状態 |
|---|---|---|
| 美幌 bihoro-001（柏倉様 取替・既設再利用）| `/bihoro/works/001/index.html` | 新規作成 |
| 美幌 works ハブ | `/bihoro/works/index.html` | 新規作成 |
| 美幌エリア index 施工事例セクション | `/bihoro/index.html` (差し替え) | プレースホルダ → 実事例カード |
| 小清水 koshimizu-001（平野様 2台新設・補助金活用）| `/koshimizu/works/001/index.html` | 新規作成（寝室・子供部屋 After 室内機写真はプレースホルダ） |
| 小清水 works ハブ | `/koshimizu/works/index.html` | 新規作成 |
| 小清水エリア（補助金独自セクション含む）| `/koshimizu/index.html` | 新規作成（bihoro 雛形 + 小清水カスタマイズ） |
| 訓子府エリア（マーケターブリーフ Phase 1A）| `/kunneppu/index.html` | 新規作成（既存 /works/004/ 引用） |

**画像処理:**
- bihoro/001: 11 枚 → 8 枚採用、800px WebP+JPG、セマンティック命名（before-01 / after-01〜06 / process-01）
- koshimizu/001: 23 枚 → 12 枚採用、9 枚除外（個人情報写り込み 1・重複・低品質）

**ヒアリング素材（独自コンテンツ・E-E-A-T 核心）:**
- 美幌: 大雨の中の事前調査・既設架台の錆落しスプレー対応・既設パーツ最大活用でコスト圧縮・お客様持込み機対応・撤去品はお客様自身でリサイクル
- 小清水: ホール 1 台設計の限界補完・床下から基礎貫通の隠蔽配線・三菱ズバ暖 2 台・1階屋根上＋高置き二段架台の冬対策・小清水町補助金制度（5万町内/4万町外）の申請サポート（お客様 4 万円受領完了）

**CLAUDE.md ルール遵守:**
- ページ本体（フォルダ + index.html + 画像）のみ作成
- sitemap.xml / 他ページのフッター・ナビ / トップページからの内部リンクは **未追加**（「公開する」指示時まで保留）

**動作確認:**
- ローカル `python -m http.server 8765` で全 9 リソース 200 OK 確認済み（7 ページ + 2 サンプル画像）

**FTP アップ待ち（次回 PC 帰宅時 / 「公開する」指示時）:**
- `/bihoro/works/`、`/bihoro/works/001/`、`/bihoro/index.html` 差し替え
- `/koshimizu/`、`/koshimizu/works/`、`/koshimizu/works/001/`
- `/kunneppu/`
- `/images/works/bihoro/001/*.webp`、`*.jpg`（raw/ は FTP 不要）
- `/images/works/koshimizu/001/*.webp`、`*.jpg`（raw/ は FTP 不要）
- 公開時は sitemap.xml 追加・他ページ内部リンク追加も併せて実施

**未完で次セッションへ持ち越し:**
- 小清水 koshimizu-001 の 2 階室内機 After 写真（寝室・子供部屋）→ ユーザーから後日受領予定。受領次第プレースホルダを差し替え
- 訓子府 kunneppu-002（杉山様邸）→ 写真到着後に `/kunneppu/works/002/` 作成（マーケターブリーフ Phase 1B）
- 訓子府ブリーフの「Phase 2」（`/works/004/` → `/kunneppu/works/001/` 301 移行）→ Phase 1A 順位安定後に別ブリーフ起票

**DEPLOY-STATUS.md の案件 ID 対応表に追加すべき新規行:**
- `bihoro-001` | `/bihoro/works/001/` | `/images/works/bihoro/001/` | ローカル完成・FTP 未公開
- `koshimizu-001` | `/koshimizu/works/001/` | `/images/works/koshimizu/001/` | ローカル完成・FTP 未公開（2 階室内機 After 写真未受領）

---

## 🟢 現在の状態

works/001-004 すべて FTP 公開済み・本番稼働中。Search Console 設定 B-1〜B-5 全完了。

**B-4 リッチリザルトテスト合格**: 4 件有効（Article・パンくず・LocalBusiness・Organization）・重大エラー 0・軽微な指摘 2 件（推奨フィールドのみ・表示には無影響）。

**B-5 PageSpeed Insights 結果（モバイル/works/004）判明**:

| 指標 | 結果 | 目標 |
|---|---|---|
| パフォーマンス | **57** 🔴 | 80 以上 |
| ユーザー補助 | 89 🟡 | 90 以上 |
| おすすめの方法 | 100 🟢 | - |
| SEO | 100 🟢 | - |
| LCP | **9.4 秒** 🔴 | 2.5 秒以下 |
| FCP | 8.4 秒 🔴 | 1.8 秒以下 |
| TBT / CLS | 0 / 0 🟢 | - |

主因: **レンダーブロック 7.1 秒**（Tailwind CDN / Google Fonts / Font Awesome）。改善余地は CSS 89KB + JS 65KB + 画像 103KB + キャッシュ 16KB。

---

## 🔴 次にやるべきこと（優先順位順）

### ★最優先（2026-06-29 _marketer ブリーフ着信）: 訓子府町専用エリアページ新設

**ブリーフ**: [`../_marketer/briefs/2026-06-29_kunneppu-area-page-brief.md`](../_marketer/briefs/2026-06-29_kunneppu-area-page-brief.md)

**サマリー**:
- 「訓子府町 エアコン 取付」で ac-kitami は `/works/` ハブが表示されてしまっており、専用エリアページがない（網走・美幌・紋別は専用 LP あり）
- 訓子府町は人口 5,000 人・ライバル極小 KW → `/kunneppu/index.html` を `abashiri/index.html` パターンで新設すれば #1〜3 取得確実視
- **Phase 1A スコープ**: `/kunneppu/index.html` のみ。既存 `/works/004/` は URL も内容も触らない（SEO 死守ライン 99/100）
- 施工事例カードは `/works/004/`（小林様）1 枚 + 「02 件目（杉山様邸）近日公開」プレースホルダー 1 枚
- Phase 1B（杉山様写真到着後）と Phase 2（works/004 → kunneppu/works/001 301 移行）は別ブリーフ

**実装順序**: ベースライン記録 → `kunneppu/index.html` 作成（abashiri 完コピ→置換）→ works ハブと works/004 への最小リンク追加 → sitemap → トップの対応エリア欄追加 → SEO 監査 → 構造化データ監査 → ローカル確認 → FTP → Search Console 再送信

詳細は上記ブリーフを参照。

---

### 既存タスク: 施工事例追加

**パフォーマンス改修は一旦終了**。施工事例追加に注力。

### 📊 パフォーマンス改修の最終結果

| 指標 | 改修前 | Phase 1+2 後 | preload+optional 後 | 目標 |
|---|---|---|---|---|
| モバイル Perf 平均 | 58.8 | 62.3 | 60.0 (ばらつき) | 80+ |
| モバイル LCP works/002 | 8.3s | 8.4s | **4.5s** ✨ | 2.5s 以下 |
| モバイル LCP works/004 | 9.5s | 9.4s | **4.7s** ✨ | 2.5s 以下 |
| PC Perf 平均 | 90.8 | 95.7 | 93.7 | 維持 |
| works/001 CLS | 0 | 0.176 ⚠️ | 0.176 ⚠️ | 0.1 未満 |

詳細は `seo-audit/baseline-2026-06-25.md`「5. 改修前後比較」「6. 2 回目改修後」セクション。

### 完了事項

- Phase 1: `.htaccess` 強化（Gzip・キャッシュ・セキュリティ）✅
- Phase 2: Google Fonts 非同期化（17 ファイル）✅
- 画像 preload tag 追加（6 ページ）✅ → works/002, 004 で LCP 大幅短縮
- Google Fonts display=optional（17 ファイル）✅

### 未完で温存（将来時間ができたら）

- ⚠️ works/001 モバイル CLS 0.176（フォント以外の要因と推測・要追加調査）
- Phase 4: icons.css 軽量化（52KB→10-15KB）
- Phase 5: Tailwind purge 強化（21KB→5-10KB）
- Xserver nginx キャッシュ設定変更（管理画面操作）

### 次に注力する方向

1. **施工事例追加**（写真分類パイプラインで効率化済み）
2. **未公開ページの本番公開**（monbetsu / bihoro はローカル完成済み・FTP アップだけ）
3. **(任意)** FTP 側 `/kitami/works/001/` フォルダ削除 — 301 で実害なし
4. **(任意)** FTP 側 `_classification/`・`seo-audit/` フォルダ掃除 — 公開不要・SEO ノイズ

### PSI 再計測の方法（参考）

API キーは `seo-audit/.psi-key` に保存済み（gitignored）。再計測するときは:

```
cd seo-audit
PYTHONIOENCODING=utf-8 python _psi_fetch.py mobile
PYTHONIOENCODING=utf-8 python _psi_fetch.py desktop
```

結果は `_psi_results_mobile.json` / `_psi_results_desktop.json` に保存される（gitignored）。

---

## ⚠️ 不変の前提・注意事項

### サイト基本情報
- ドメイン: ac-kitami.com / 屋号: エアコンラボ北見店 / 電話: 070-4080-0965
- 対応エリア: 北見市・網走市・美幌町・訓子府町・置戸町
- 主要キーワード「北見市エアコン取付」「北見市エアコン」**1〜2 位維持絶対条件**

### 命名規則の二重構造（意図的）
- ページ URL = **通し番号** (`/works/001/` `/002/` `/003/` `/004/`)
- 画像フォルダ = **地域別** (`/images/works/kitami/001/` `/kitami/002/` `/kitami/003/` `/kunneppu/001/`)
- 詳細対応表は `DEPLOY-STATUS.md`「案件 ID と URL/画像フォルダの対応表」参照

### .htaccess の 301 リダイレクト
- `/kitami/works/001/` → `/works/001/`（インデックス引き継ぎ用・動作確認済み）
- 旧 URL のままインデックスが残っているケースは 301 で自動置換される

### 写真分類パイプライン
- スキル: `.agents/skills/photo-classification-pipeline/`
- 分類エージェントの出力は誤分類前提 → Claude 自身が Read で再確認するのが必須プロセス
- 個人情報含む書類（見積書/請求書）は確実に除外

### SEO 死守 (作業ルール)
- title / meta description / og:* / 構造化データ / H1 / H2 メインキャッチ / canonical / 既存画像 URL / 既存画像 alt のキーワードは **触らない**
- CSS / 余白 / フォント装飾 / ボタン形状 / 画像最適化（同 URL・同寸法）は自由
- サブキャッチ / CTA 文言 / 画像差替 / セクション順序は慎重に（ベースライン記録 + 1-2 週間モニタリング）

### 担当エンジニアモデル v1
- チーフエンジニア (`_engineer`): 全サイト共通の汎用施工事例生成
- ac-kitami 担当: SEO 死守ルール暗黙知が必要な最終チェック・公開判定
- 写真フォルダ（不変アーカイブ）: `e:/Dropbox/apps/remotely-save/assets/photos/_inbox/エアコン写真素材/`

---

## 📋 直近 1 ヶ月の経緯（要約）

### 2026-06-27 00:00（パフォーマンス改修一旦終了）
- 画像 preload tag 追加（works/001-004 + abashiri/works/001-002 = 6 ページ・コミット `ef6c536`）
- Google Fonts display=swap → display=optional 全 17 ファイル変更（コミット `08d2167`）
- FTP 反映後 PSI 再計測 → works/002 と 004 で大ヒット（LCP 8.3→4.5・9.5→4.7）
- 一方で works/001 CLS 0.176 は改善せず（フォント以外の要因と推測）
- 全体平均は PSI のばらつきで Phase 1+2 時と変わらず横ばい
- パフォーマンス改修一旦終了・施工事例追加に注力する判断

### 2026-06-26 22:00（ベースライン計測セッション）
- Google Cloud Console で PSI API キー取得（プロジェクト「Cursor-Gemini-Project」内・「PageSpeed Insights Key」）
- PSI API 経由で 9 ページ × モバイル/PC = 18 計測完了
- `seo-audit/baseline-2026-06-25.md` に数値転記済み
- **判明事項**:
  - PC は全ページ 88-93 点（合格、改修対象外）
  - モバイルは全ページ 56-61 点・LCP 7-10 秒（要改修）
  - TBT 全 0ms / CLS ほぼ 0 → JS とレイアウト面は健全
  - **真の課題は LCP/FCP（最初のコンテンツ表示の遅さ）→ Phase 1+2 が直接効く**
- API キーは `seo-audit/.psi-key` に保存（gitignore 済、git に上がらない）
- Phase 1+2 ローカル実装は前セッションで完了、FTP アップ待ちのまま

### 2026-06-25 深夜（Phase 0+1+2 セッション）
- Phase 0: `seo-audit/baseline-2026-06-25.md` 雛形作成・Git タグ `before-perf-2026-06-25` 作成 + push（コミット `ab31ff0`）
- Phase 1: `.htaccess` 強化（Gzip + 1年キャッシュ + セキュリティ + ETag無効 + KeepAlive・既存 301 リダイレクトとXserver設定は完全保持・コミット `f6d1ef6`）
- Phase 2: Google Fonts 非同期化を 16 HTML + テンプレート 1 に展開（コミット `87eec9f`）
- Phase 3: works/001-004 FV 画像は既に `<picture>` + WebP 対応済みで作業不要と判明
- 順位モニタリング手段がない（GRC 機能停止中）ため、改修後比較は PageSpeed 数値のみ
- ローカル動作確認 OK（python -m http.server で目視確認）→ FTP アップ待ち

### 2026-06-25 夜
- works/004 メタ情報統一（H3 + meta description + og:description + Article JSON-LD 4 箇所一貫化）
- 施工日プライバシー配慮（`2025年11月9日` → `2025年11月`）+ 工期 `1日間`
- DEPLOY-STATUS.md に「案件 ID とパスの対応表」追記（命名二重構造を文書化）
- FTP 本番デプロイ完了: `/js/photoswipe/`, `/images/works/kunneppu/001/`, `/works/004/`, トップ index.html, about, sitemap.xml, .htaccess
- 動作確認 OK: works/004 表示・PhotoSwipe・301 リダイレクト・sitemap.xml
- **Search Console B-1〜B-5 全完了**（サイトマップ・URL 検査 7 件・robots.txt 検証・リッチリザルトテスト合格 4 件・PageSpeed 計測）
- B-5 PageSpeed Insights 計測 → モバイル 57 点・要改善判明
- NOW.md 圧縮実施 664 → 120 行 (commit `d4c73fe`)

### 2026-06-24
- works/004 SEO 監査完了（99/100・クリティカル指摘 = 施工日/工期 [要入力] 2 箇所のみ）
- ac-kitami 担当エンジニアが SEO 死守ルール暗黙知を踏まえて監査・組織モデル v1 確定

### 2026-06-22〜23
- works/004 (kunneppu-001 訓子府町・小林様 軒天天吊り) チーフエンジニアが作成 (commit `ba2f99e`)
- works/003 v2 仕様化（PhotoSwipe・alt 強化・関連事例リンク切れ修正）SEO 99/100
- works/004 → works/003 リネーム（旧 003 案件 After 写真欠落で公開不可と判断）
- kitami/works/001 → /works/001 統合（.htaccess 301 リダイレクト追加）
- /works/ ハブページ新規作成・/works/002 公開準備完了 (SEO 99/100)

### 2026-06-15〜16
- kitami-001 施工事例ページ完成（北見市中央三輪・三菱霧ヶ峰 GV2825）
- 写真分類パイプライン実証（36 枚 → セマンティック命名 14 枚 WebP 化）
- 新スキル `photo-classification-pipeline` 作成・誤分類対策プロセス組込
- SEO 最適化 10 項目（スコア 77 → 約 93 点）

### 2026-06-07
- abashiri/works/* FTP 公開済み内容を Git に反映 (c4ab384・73 ファイル)
- スマホ作業ブランチ 5 件すべて整理（リモート削除）
- about: 防虫キャップ無料サービスの記載削除（779f856）→ 2026-06-25 FTP 反映完了

---

## 📁 過去ログ索引

- [LOG/2026-06-and-earlier.md](LOG/2026-06-and-earlier.md) — works/002・003・kitami-001 公開準備、写真パイプライン実証、FV デザイン整え引き継ぎ、abashiri 反映、kitami-001 施工情報詳細、構造化データ強化保留タスク

---

## 🆕 新セッション開始時のチェック

- [ ] 現在のブランチが `main` であることを確認（`git branch`）
- [ ] working tree clean を確認（`git status`）
- [ ] `git fetch` で GitHub 最新と一致確認
- [ ] 施工事例追加 or 新エリア展開のどちらを優先するか確認
- [ ] パフォーマンス改修は一旦終了済み（再開する場合は `seo-audit/baseline-2026-06-25.md` 参照）
- [ ] Phase 4+5（icons.css / Tailwind purge）に進むか判断

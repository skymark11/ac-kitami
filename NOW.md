# NOW.md — ac-kitami.com 作業引き継ぎ

最終更新: 2026-06-25 深夜（PC セッション・Phase 1+2 実装完了・FTP アップ待ち）

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

`PERFORMANCE-PLAN.md` 準拠で進行中。

1. **🔥 FTP アップ待ち** — Phase 1+2 の変更を本番反映
   - `.htaccess`（Gzip + 1年キャッシュ + セキュリティヘッダー追加）
   - 16 HTML ファイル（Google Fonts 非同期化）：works/index, works/001-004, about, abashiri/index, abashiri/works/index, abashiri/works/001-002, monbetsu, bihoro, relocation, column/200v-aircon-check, column/aircon-2027-mondai
   - 注意: `.htaccess` は **必ずバックアップ取得後にアップ**（万一壊れるとサイト全体 500 エラー）
2. **FTP アップ後の検証**
   - https://ac-kitami.com/ で表示・スタイル崩れがないか確認
   - DevTools Network タブで Response Header に `Content-Encoding: gzip` と `Cache-Control: public, max-age=31536000, immutable` (CSS/JS/画像) が出ているか
   - https://ac-kitami.com/works/004/ をモバイル PageSpeed 再計測 → 57 点からどこまで上がったか
   - `seo-audit/baseline-2026-06-25.md` に「改修後」セクションを追記
3. **Phase 4+5（効果次第で判断）**
   - Phase 4: icons.css 軽量化（52KB → 10-15KB 想定）
   - Phase 5: Tailwind purge 強化（21KB → 5-10KB 想定）
   - Phase 1+2 だけで目標達成（LCP 2.5 秒以下）するなら見送り可
4. **(任意)** FTP 側 `/kitami/works/001/` フォルダ削除 — 301 で実害なし
5. **(任意)** FTP 側 `_classification/`・`seo-audit/` フォルダ掃除 — 公開不要・SEO ノイズ

### 📦 FTP アップ対象ファイル一覧

```
.htaccess
works/index.html
works/001/index.html, 002/index.html, 003/index.html, 004/index.html
about/index.html
abashiri/index.html
abashiri/works/index.html
abashiri/works/001/index.html, 002/index.html
monbetsu/index.html
bihoro/index.html
relocation/index.html
column/200v-aircon-check/index.html
column/aircon-2027-mondai/index.html
```

Phase 3（works/001-004 FV 画像 WebP 化）は**既に対応済み**だったため作業不要。

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
- [ ] Phase 1+2 の FTP アップが終わっているか（NOW.md「FTP アップ対象ファイル一覧」参照）
- [ ] アップ後、https://ac-kitami.com/works/004/ のモバイル PageSpeed 再計測 → 57 点 → ?
- [ ] Phase 4+5（icons.css / Tailwind purge）に進むか判断
